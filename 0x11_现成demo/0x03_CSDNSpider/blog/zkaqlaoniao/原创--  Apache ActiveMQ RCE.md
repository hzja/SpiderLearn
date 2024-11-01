# 原创
：  Apache ActiveMQ RCE

# Apache ActiveMQ RCE

### 影响版本

Apache ActiveMQ &lt; 5.18.3

### 利用条件

需要访问到61616端口(默认)。

### 漏洞分析

这里需要的是Apache ActiveMQ &lt; 5.18.3,我这里直接下的5.18.2

https://github.com/apache/activemq/commit/958330df26cf3d5cdb63905dc2c6882e98781d8f

在新版本中添加了一个`OpenWireUtil.validateIsThrowable(clazz);`在5.18.2中的代码如下

把5.18.3的代码下下来，看看`validateIsThrowable`方法，代码如下

```
package org.apache.activemq.openwire;

public class OpenWireUtil {

    /**
     * Verify that the provided class extends {@link Throwable} and throw an
     * {@link IllegalArgumentException} if it does not.
     *
     * @param clazz
     */
    public static void validateIsThrowable(Class&lt;?&gt; clazz) {
        if (!Throwable.class.isAssignableFrom(clazz)) {
            throw new IllegalArgumentException("Class " + clazz + " is not assignable to Throwable");
        }
    }
}

```

这里如果传进来的clazz不是继承自Throwable类，就会抛出异常。在上面是通过反射获取一个类，然后调用对应的构造方法。在5.18.3在中对这个反射获取到的类进行了过滤。 现在就需要找到一个可以命令执行的类去反射获取。这里是用的`BaseDataStreamMarshaller`的classloader。

找到BaseDataStreamMarshaller的子类ExceptionResponseMarshaller，在其中的tightUnmarshal方法中调用了tightUnmarsalThrowable，具体代码如下

```
public void tightUnmarshal(OpenWireFormat wireFormat, Object o, DataInput dataIn, BooleanStream bs) throws IOException {
    super.tightUnmarshal(wireFormat, o, dataIn, bs);
    ExceptionResponse info = (ExceptionResponse)o;
    info.setException((java.lang.Throwable) tightUnmarsalThrowable(wireFormat, dataIn, bs));
}

```

tightUnmarsalThrowable具体代码如下

在其中说到了上文当中的createThrowable，可以反射获取一个类并且调用对应的含一个string参数的构造方法，其中`ExceptionResponseMarshaller`类是对ExceptionResponse进行序列化操作的类

来看`tightUnmarsalThrowable`的主要逻辑

从BooleanStream读入一个Boolean的数据，分别调用tightUnmarshalString去获取clazz和message，应该是把类名和message从clazz从二进制流中读取出来，然后作为参数调用`createThrowable`方法，tightUnmarsalThrowable方法最后返回了一个o，根据如下代码，这个o应该是ExceptionResponse的Exception属性

```
public void tightUnmarshal(OpenWireFormat wireFormat, Object o, DataInput dataIn, BooleanStream bs) throws IOException {
    super.tightUnmarshal(wireFormat, o, dataIn, bs);

    ExceptionResponse info = (ExceptionResponse)o;
    info.setException((java.lang.Throwable) tightUnmarsalThrowable(wireFormat, dataIn, bs));

}

```

我们这只要构造一个ExceptionResponse包含恶意的类名和message发送给服务器，服务器接受到并且反序列化就可以调用`createThrowable`

```
来源：https://ch1e.cn/post/apache-activemq-rce/
```

> 
声明：⽂中所涉及的技术、思路和⼯具仅供以安全为⽬的的学习交流使⽤，任何⼈不得将其⽤于⾮法⽤途以及盈利等⽬的，否则后果⾃⾏承担。**所有渗透都需获取授权**！


@**学习更多渗透技能！体验靶场实战练习**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/f2ec7ae79dfe46a1ab7a0bcc3e164ddd.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/3ddef41cc8a34002a53f5d630894e325.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/0086537980904f6a83ed121c2f2edb9f.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/0c01e99f02ae44638413e782c06aae63.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/ccc34edf1fc44195a2413ff1dcac5c0c.png" width="665"/>

应急响应笔记

学习路线
