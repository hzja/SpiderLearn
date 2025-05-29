# 原创
：  【APP逆向百例】某蜂窝逆向分析

# 【APP逆向百例】某蜂窝逆向分析

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 逆向目标

### 抓包分析

打开 app，在首页进行刷新，charles 配合 SocksDroid 进行抓包，结果如下：

其中要逆向的参数有很多，这里只对 zzzghostsign 参数展开分析。

### 逆向分析

对 Java 常见的 api 进行 hook 操作：

定位这个参数的方法有很多，这里我们使用 frida 对 java 的 StringBuilder 类进行 hook，`StringBuilder` 是 Java 中用于创建和操作可变字符串的类，一般操作字符串都会使用这个类，hook 代码如下：

```
function showStacks() {
    Java.perform(function () {
      console.log(Java.use("android.util.Log").getStackTraceString(
        Java.use("java.lang.Throwable").$new()
    ));
	})
}

function hook_StringBuilder(){
    var stringBuilderClass = Java.use("java.lang.StringBuilder");
    stringBuilderClass.toString.implementation = function (){
    var res = this.toString.apply(this,arguments);
    showStacks();
    console.log("StringBuilder--&gt;" + res.toString())
    return res
    }
}
Java.perform(function() {
    hook_StringBuilder()
});

```

通过使用 `frida -UF -l demo.js -o 1.txt` 进行 frida 注入，命令解释如下：

注意，捕获的东西有点多，可能导致卡死、应用闪退，可以在输出一段时间后手动关掉，或者根据相关字段进行过滤。

输出结果如下，直接输入 zzzghostsign 的值，会发现存在，并打印出了相关堆栈：

### java 层分析

把 apk 文件拖到 jadx，根据堆栈信息进行搜索，最终定位到下图这个地方：

其中 ghostSign 函数就是参数生成处，可以使用 frida 代码验证位置是否正确，鼠标放到 ghostSign 右键复制 frida 代码：

```
function hook1(){
    let AuthorizeHelper = Java.use("com.mfw.tnative.AuthorizeHelper");
    AuthorizeHelper["xPreAuthencode"].implementation = function (context, str, str2) {
    console.log('xPreAuthencode is called' + ', ' + 'context: ' + context + ', ' + 'str: ' + str + ', ' + 'str2: ' + str2);
    let ret = this.xPreAuthencode(context, str, str2);
    console.log('xPreAuthencode ret value is ' + ret);
    return ret;
};

```

发现结果一致，我们继续向下分析，点进去这个函数，发现跳到了 java iterface 接口处：

java 的接口本身不能实例化。因此我们需要找到他具体的实现方式，可以搜索这个 java 类 Authorizer：

下面就是接口实现的具体方法，我们进入到 m22665c 方法中去：

最后定位到 native 层加密，并加载 mfw.so 文件：

把这个加密写成主动调用的方式，方便我们后续进行分析，代码如下：

```
// xPreAuthencode
function call_mfw(){
    let AuthorizeHelper = Java.use("com.mfw.tnative.AuthorizeHelper");
    var current_application = Java.use('android.app.ActivityThread').currentApplication();
    var context = current_application.getApplicationContext();
    let str = "GET&amp;https%3A%2F%2Fmapi.mafengwo.cn%2Fdiscovery%2Fget_index%2Fv7&amp;app_code%3Dcom.mfw.roadbook%26app_ver%3D11.0.2%26app_version_code%3D1052%26brand%3Dgoogle%26channel_id%3DMFW-WDJPPZS-1%26dev_ver%3DD2313.0%26device_id%3D82d917db80c8eae2%26device_mid%3D860000000000001%26device_type%3Dandroid%26hardware_model%3DPixel%25203%26has_notch%3D0%26jsondata%3D%257B%2522top_tab_id%2522%253A%252255%2522%252C%2522filter_id%2522%253A%2522all%2522%252C%2522top_refresh%2522%253A%25221%2522%252C%2522by_user%2522%253A%25221%2522%257D%26mfwsdk_ver%3D20140507%26o_coord%3Dwgs%26o_lat%3DMzAuNDg5NjIy%26o_lng%3DMTE0LjQyMDQ5MQ%253D%253D%26oauth_consumer_key%3D5%26oauth_nonce%3D536f6e42-bc4c-463f-acb5-ee145e63f10e%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1732784973%26oauth_token%3D0_0969044fd4edf59957f4a39bce9200c6%26oauth_version%3D1.0%26open_udid%3D82d917db80c8eae2%26screen_height%3D2028%26screen_scale%3D2.88%26screen_width%3D1080%26shumeng_id%3DDUx0wb9S3BzdWvrdsQ8G8T6MnVVJL6kbZPb2RFV4MHdiOVMzQnpkV3ZyZHNROEc4VDZNblZWSkw2a2JaUGIyc2h1%26sys_ver%3D11%26time_offset%3D480%26x_auth_mode%3Dclient_auth"
    let str2 = "com.mfw.roadbook"
    let ret = AuthorizeHelper.$new("com.mfw.roadbook").xPreAuthencode(context, str, str2);
    console.log('主动调用 ret value is ' + ret);
}

```

### so 层分析

我们从 apk 拿到 mfw.so 文件放到 ida 进行分析：

先在 Exports 表里搜索 java，看是否是静态注册的，发现没有任何内容，那么这个函数一般就是动态注册，那我们在搜索 `JNI_Onload`，点进去：

动态函数一般是通过 RegisterNatives 函数注册，一般有四个参数：

下图函数具体实现就是 `off_FF020`，注册方法数量是 4 个：

点到函数中去：

可以看到我们要的方法 xPreAuthencode 的偏移是 396C8，按下 G 搜索该地址，定位到 `sub_396C8` 函数，这里的 `sub_函数偏移` 是 ida 给我们取的函数名：

因为静态注册和动态注册函数，第一个参数值类型都是 JNIEnv，按 y 修改一下 a1 指针的类型为 `JNIEnv * a1`，这样 ida 就可以识别 JNI 相关的方法了：

这里为了方便分析，直接使用 traceNative 工具帮助我们分析，下载地址如下：

> 
Pr0214/trace_natives：https://github.com/Pr0214/trace_natives


我们把项目里面的 `traceNatives.py` 文件复制到我们本地 ida 目录下的 plugins 文件夹里面，再次打开 ida，我们就有该插件了：

运行插件：

结果如下：

traceNative 插件会把 so 文件里面相关的函数调给 hook，放入到 `__handlers__` 文件夹中，等待函数调用，我们刷新一下 app，会得到相关函数的调用堆栈：

我们把需要分析的函数的调用堆栈单独拿出来：

会发现加密函数首先调用了 `sub_3c9c4`，然后一直在调用 3e1d0 函数。我们先按 g 搜索 3c9c4 进入这个函数，按住 y 修改函数第一个、第二个参数类型：

这里获取到了 app 相关的签名信息，并调用了几个函数，最后成功执行返回布尔值 1。

接着再往下分析 `sub_3e1d0` 函数：

hook 一下这个函数：

```
function hook_sha1(){
    var addr = Module.findBaseAddress("libmfw.so");
    // console.log(addr)
    var func_addr = addr.add(0x3E1D0);
    // console.log(func_addr);
    Interceptor.attach(func_addr,{
        onEnter:function (args){
            console.log(args[1].readCString())
            console.log(hexdump(args[1]))
            // console.log(args[0].readCString())
        },
        onLeave:function (retval){
            // console.log(retval)
        }
    })
}
hook_sha1()

```

这个函数调用了很多次，对明文进行不断的处理，另外出现了很多 1518500249、1859775393、1894007588 等常数，这里为了方便观看，我们转化为 16 进制数据：

根据加密生成的位数以及这些常数，推测出为 sha1 算法，可以使用 k 哥工具站：https://www.kgtools.cn/secret/sha，来验证是否为标准算法：

可以看出不是标准算法，那么就有两种基本方案，第一是扣魔改的 sha1 算法，一步步分析是哪里魔改了。第二种就是使用 unidbg，补 unidbg 相关环境，让 unidbg 去执行 so 文件代码，得到最终的加密结果。

这里简要分析一下 sha1 算法的初始化常数是否魔改。回到 xPreAuthencode 函数：

hook 该函数：

```
function hook_sha1(){
    var addr = Module.findBaseAddress("libmfw.so");
    // console.log(addr)
    var func_addr = addr.add(0x3DEC4);
    // console.log(func_addr);
    Interceptor.attach(func_addr,{
        onEnter:function (args){
            console.log(args[0].readCString())
            console.log(hexdump(args[1]))
            console.log(args[2].toInt32())
        },
        onLeave:function (retval){
            // console.log(retval)
        }
    })
}
hook_sha1()

```

hook 结果如下：

其中包含了 sha1 算法加密的明文参数和明文长度，`&amp;v38` 包含了 sha1 算法的初始化模数，跳转到该函数位置：

点进 C0C30，并按字母 D 把伪指令 DCB 改成 DCD。DCB 占两个字节，DCD 占四个字节：

还有一个初始化模数通过指令的方式进行加载：

```
# 指令将值 0x5476 加载到寄存器 W8 的低 16 位中
.text:000000000003DEEC                 MOV             W8, #0x5476
# 将值 0x1032 加载到 W8 的第 16 位（高 16 位）中,不影响其他位的值
.text:000000000003DEF8                 MOVK            W8, #0x1032,LSL#16

# 最终得到的结果为：0x10325476

```

因此，sha1 的初始化模数为：

```
A = 0x67452301
B = 0xEFCDAB89
C = 0x98BADCFE
D = 0x5E4A1F7C
E = 0x10325476

```

可以看到初始化值已经魔改，那么后面就需要分析 sha1 算法是否在填充、明文、80 轮循环的什么地方进行了魔改，网上已经有教程，这里就不多介绍。

### unidbg 还原

unidbg 是一款基于 unicorn 和 dynarmic 的逆向工具，一个标准的 java 项目，它通过模拟 Android 运行时环境，让用户能够在没有实际设备的情况下，分析和调试 Android 应用的行为。

> 
zhkl0228/unidbg：https://github.com/zhkl0228/unidbg/releases


在使用之前，你需要提前配置好 java 和 maven 环境，安装配置网上有很多教程，这里不多做介绍。

关于 unidbg 的更多使用方法，可以看吾爱破解正己大佬写的文章：

> 
《安卓逆向这档事》第二十三课、黑盒魔法之 Unidbg：https://www.52pojie.cn/thread-1995107-1-1.html


另外作者也给了我们相关代码示例，我们只需要稍微修改一下就能用，主要代码如下：

执行 TTEncrypt 文件，看看我们的环境是否有问题：

能正常执行，接着我们在 com 目录下，新建自己的目录，这里命名为 mafengwo，再在该目录下新建 java 文件为 Mfw：

把作者给的样例，例如 TTEncrypt 代码 copy 一份，改一下，这个 app 检测环境较少，可以算入门 unidbg 的案例，基本上简单修改完作者给的代码样例就能使用。

最终代码如下：

```
package com.mafengwo;

import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.Module;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.*;
import com.github.unidbg.memory.Memory;

import java.io.File;
import java.io.IOException;

public class Mfw extends AbstractJni {

    private final AndroidEmulator emulator;
    private final VM vm;
    private final Module module;
    private final DvmClass AuthorizeHelper;
    private final boolean logging;

    Mfw(boolean logging) {
        this.logging = logging;

        emulator = AndroidEmulatorBuilder.for64Bit().setProcessName("com.mfw.roadbook").build(); // 创建模拟器实例，要模拟32位或者64位，在这里区分
        final Memory memory = emulator.getMemory(); // 模拟器的内存操作接口
        memory.setLibraryResolver(new AndroidResolver(23)); // 设置系统类库解析

        vm = emulator.createDalvikVM(new File("unidbg-android/src/test/java/com/xxx/mafengwo/com.mfw.roadbook.apk")); // 创建Android虚拟机
        vm.setJni(this);
        vm.setVerbose(logging); // 设置是否打印Jni调用细节
        DalvikModule dm = vm.loadLibrary(new File("unidbg-android/src/test/java/com/xxx/mafengwo/libmfw.so"), false); // 加载libttEncrypt.so到unicorn虚拟内存，加载成功以后会默认调用init_array等函数
        dm.callJNI_OnLoad(emulator); // 手动执行JNI_OnLoad函数
        module = dm.getModule(); // 加载好的libttEncrypt.so对应为一个模块
        AuthorizeHelper = vm.resolveClass("com/mfw/tnative/AuthorizeHelper");
    }

    void destroy() throws IOException {
        emulator.close();
        if (logging) {
            System.out.println("destroy");
        }
    }

    public static void main(String[] args) throws Exception {
        Mfw test = new Mfw(true);
        test.callFunc();
        test.destroy();
    }

    void callFunc() {

        String data = "GET&amp;https%3A%2F%2Fmapi.mafengwo.cn%2Fdiscovery%2Fget_index%2Fv7&amp;app_code%3Dcom.mfw.roadbook%26app_ver%3D11.0.2%26app_version_code%3D1052%26brand%3Dgoogle%26channel_id%3DMFW-WDJPPZS-1%26dev_ver%3DD2313.0%26device_id%3D82d917db80c8eae2%26device_mid%3D860000000000001%26device_type%3Dandroid%26hardware_model%3DPixel%25203%26has_notch%3D0%26jsondata%3D%257B%2522top_tab_id%2522%253A%252255%2522%252C%2522filter_id%2522%253A%2522all%2522%252C%2522top_refresh%2522%253A%25221%2522%252C%2522by_user%2522%253A%25221%2522%257D%26mfwsdk_ver%3D20140507%26o_coord%3Dwgs%26o_lat%3DMzAuNDg5NjIy%26o_lng%3DMTE0LjQyMDQ5MQ%253D%253D%26oauth_consumer_key%3D5%26oauth_nonce%3D536f6e42-bc4c-463f-acb5-ee145e63f10e%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1732784973%26oauth_token%3D0_0969044fd4edf59957f4a39bce9200c6%26oauth_version%3D1.0%26open_udid%3D82d917db80c8eae2%26screen_height%3D2028%26screen_scale%3D2.88%26screen_width%3D1080%26shumeng_id%3DDUx0wb9S3BzdWvrdsQ8G8T6MnVVJL6kbZPb2RFV4MHdiOVMzQnpkV3ZyZHNROEc4VDZNblZWSkw2a2JaUGIyc2h1%26sys_ver%3D11%26time_offset%3D480%26x_auth_mode%3Dclient_auth";
        StringObject strResult = AuthorizeHelper.callStaticJniMethodObject(
                emulator,
                "xPreAuthencode(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;",
                vm.addLocalObject(vm.resolveClass("android/content/Context").newObject(null)),
                new StringObject(vm, data),
                new StringObject(vm, "com.mfw.roadbook")
        ); // 执行Jni方法
        System.out.println(strResult);
    }

}

```

最后也是成功返回了加密数据：

成功打印了加密结果，那么我们怎么给 python 使用呢？

### unidbg-boot-server 搭建接口服务

我们可以使用 unidbg-boot-server 项目，作者已经帮我们封装好了相关代码。下载地址：

> 
unidbg-server 提供 http api 服务：https://github.com/anjia0532/unidbg-boot-server


和 unidbg 使用一样，需要配置好 java 和 maven 环境，用法和 unidbg 差不多，我们把项目下载下来：

相关配置环境加载好后，直接运行 UnidbgServerApplication 文件，显示以下内容证明环境没有问题，可以正常执行：

作者也很贴心的给我们准备了代码样例，主要逻辑都在 com.anjia.unidbgserver 里面。

其中 `web.*Controller` 目录是暴露给外部 http 调用的：

`service.*ServiceWorker` 目录是用多线程包装了一层业务逻辑，主要用来调用我们的加密逻辑`service.*Service` 里的加密函数相关的逻辑，也就是 unidbg 的代码。

ServiceWorker：

Service：

仿造代码样例，写出加密函数的代码，运行 UnidbgServerApplication 结果如下：

最后通过 python 请求这个接口就可以得到加密参数了，不再赘述。

至此，该参数加密分析流程就结束了。

相关代码，会分享到知识星球当中，需要的小伙伴自取，仅供学习交流。

### 结果验证
