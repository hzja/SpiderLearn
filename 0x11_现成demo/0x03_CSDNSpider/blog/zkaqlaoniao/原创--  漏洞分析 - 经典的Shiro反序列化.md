# 原创
：  漏洞分析 | 经典的Shiro反序列化

# 漏洞分析 | 经典的Shiro反序列化

## 0x01、前言

---


相信大家总是面试会问到java反序列化，或者会问到标志性的漏洞，比如shiro反序列化，或者weblogic反序列化漏洞。

那我就这篇文章为大家讲解一下，不懂的哥哥直接背一下，理解一下就好了。

至于为什么要选择shiro反序列化呢，不讲weblogic呢？

因为我上次有幸参与金鸡电影节的临时安全负责人，具体我就不细说了。当时是内部涉及到shiro反序列化漏洞。

准确的来说是Shiro&lt;1.2.4-RememberMe反序列化漏洞。

而它也被称为Shiro 550反序列化漏洞。

细品细品...

## 0x02、环境搭建

---


下载地址：https://codeload.github.com/apache/shiro/zip/shiro-root-1.2.4

环境：Tomcat 8.5.27 + idea 2020.2 + jdk 1.8 +maven 3.6

下载之后之后直接打开，并open这个web文件夹即可，其他自行百度就行，其中还需要导入一些jstl的jar等等

## 0x03、漏洞原理

---


shiro默认使用了`CookieRememberMeManager`，其处理cookie的流程是

```
得到rememberMe的cookie值 --&gt; Base64解码 --&gt; AES解密 --&gt; 反序列化

```

然而AES的密钥是硬编码的，就导致了攻击者可以构造恶意数据造成反序列化的RCE漏洞。

payload 构造的顺序则就是相对的反着来：

```
恶意命令--&gt;序列化--&gt;AES加密--&gt;base64编码--&gt;发送cookie

```

在整个漏洞利用过程中，比较重要的是AES加密的密钥，该秘钥默认是默认硬编码的，所以如果没有修改默认的密钥，就自己可以生成恶意构造的cookie了。

shiro特征：

## 0x04、漏洞复现

---


复现文章https://blog.csdn.net/weixin_43571641/article/details/108182722

## 0x05、漏洞分析

简单介绍利用：

### 5.1、加密

---


那既然我们要分析，那入口点在哪呢？

Shiro≤1.2.4版本默认使用`CookieRememberMeManager`

而我们看看这边`CookieRememberMeManager`类继承了`AbstractRememberMeManager`，我们进去看看是什么梗

我们可以看到这边这个类里面有硬编码。

然后它又继承了`RememberMeManager`接口；我们继续进去看看是怎么回事

看名字的话可以知道这些是登陆成功，登陆失败，退出的一些service；既然如此，肯定会调用这个登陆成功的接口，然后再去实现这个接口。

所以我们直接在这个接口下个断点，看看是怎么个流程；

这里看到调用了`isRememberMe()`可以发现这个就是一个判断用户是否选择了`RememberMe`选项。而我们是勾选了的

所以我们我们条件满足，这边判断返回True，我们则进入`this.rememberIdentity(subject, token, info);`

`subject`存储的一些登陆信息如session等等，而`authcInfo`存储的则是用户名；

而PrincipalCollection是一个身份集合，因为我们可以在Shiro中同时配置多个Realm，所以呢身份信息可能就有多个；因此其提供了PrincipalCollection用于聚合这些身份信息，具体我们不细讲，不深入去懂原理。

然后我们再F7继续跟进this.rememberIdentity(subject, principals);

这我们有点懵，将身份信息干嘛？

我们进入该`convertPrincipalsToBytes()`方法查看；

看到了`serialize()`方法，难道这边开始是进行序列化了还是啥？

通过此处我们可以知道是跳了两层，到`DefaultSerializer`类的`serialize`方法；

看到这里就懂了，这里先转为byte，写入缓冲区；

然后进行了一个序列化，最后通过`toByteArray()`方法返回序列化后的Byte数组。

然后返回到原来的地方`convertPrincipalsToBytes()`内，接下来if判断`getCipherService()`方法不为空，则进入条件里面里面。

我们f7进去内部看看；

发现又是一个`cipherService`，这是什么；我们翻译一下，因为大部分开发都会用简称；

也就是获取密码服务？？什么密码服务？我们再继续F7跟进发现直接推出了。

那我们就 `Ctrl+左键` 继续进去看。可以，发现是new了一个aes加密服务。

那我们点击debugger处，回到刚刚那个地方；我们就不用继续进入了，我们就思考一下，这边是要获取到加密服务，如果没获取到，则不进入。

获取到的话，则进入该条件；

直接F8下来，进入，然后我们再手动添加变量监视。

可以发现正如我们所想的，获取aes加密服务；

然后调用`encrypt()`方法，而懂点英文的，都知道这个单词是加密的意思。

那我们初步判断这是个加密方法。

我们f7跟进去看看什么情况。

我们可以知道这个参数是`byte[] serialized`，也就是说，此处加密我们刚刚的序列化流的数据。

然后这边`this.getCipherService()`我们刚刚手动添加变量查看了，这边是获取到了aes加密服务；然后判断不问空，那肯定不为空啊，刚刚上面分析过了。然后我们进入条件判断股内部。

```
ByteSource byteSource = cipherService.encrypt(serialized, this.getEncryptionCipherKey());

```

这里调用`cipherService.encrypt()`方法并且传入序列化数据，和`getEncryptionCipherKey`方法。

加密过程，我们就应该不怎么感兴趣了；有兴趣的可以自己研究

我们通过`getEncryptionCipherKey()`名字可以知道是获取key的一个方法。

那我们f7进入看看

哦豁，那我们再进一层看一下；发现直接就返回了，emmmmm….怎么跟别人不一样。

那我们就不追了

第一步有说到，硬编码存储在这个地方，而构造方法就在这下面，可以看到这边设置了key。

我们继续回到原来的地方，知道这边是获取加密的key就ok了。

然后这边使用平台的默认字符集将字符串编码为 byte 序列，并将结果存储到一个新的 byte 数组中。那我们加密部分就结束了

### 5.2、解密

---


由于此处，我找不到，回溯不到，那咋办，烦恼；最后想到了我们加密的入口~~

既然自动跳到了这里，那么我们就直接在此处下个断点，重新开始

随后我们进入这个`getRememberedSerializedIdentity()`方法，看看是什么东西。

此处我们依然还很懵，没事；

一直f8，期间倒是没有什么有意思或者重点的地方；

直到我们走到这里，这个有一个`this.getCookie().readValue(request, response)`，这是要读取cookice中的数据了，这必须跟入了;

这里给进到了这个`readvalue()`方法中了，我们先看看什么情况。

根据名字可以知道是读取值的一个方法。读取什么值？请求包的值。

通过`getName()`方法得到了key为remeberMe。然后把value置空，再通过`getCookie`获取到cookie。

最后判断cookie不为空，则进入内部；

随后获取到cookie的值；值则为序列化内容。然后再 return回序列化内容；

随后返回到上一处地方现在`remeberMe`的值不是`delete`；而是序列化内容，所以进入到第二个条件分支。

一直到这一步，进行base64解码，成为二进制数据，给了decoded的byte数组；

```
得到rememberMe的cookie值 --&gt; Base64解码 --&gt; AES解密 --&gt; 反序列化

```

目前只进行了Base64解码，那还需要aes解码。我们继续跟进

返回到了上层，此处我们知道bytes是二进制数据，我们看看条件判断。当bytes数组不为空且长度大于0时，进入里面。那我们肯定满足，所以我们两步f8加一步F7进入到 `convertBytesToPrincipals`看看是什么

可以看出我们接下来的步骤要依依实现了。判断key不为空，然后进入内部

而从这里开始，就是进行aes解密的步骤了，我们F7跟进方法查看

这里重新把恶意的bytes数组重新赋值给`serialized`，然后再获取加密服务：AES/CBC/PKCS5Padding

同时到达了下一步；真真正正的开始解密了，其中两个参数，第一个是加密的bytes数组，第二个是获取到key，也就是硬编码；我们 就直接进入decrypt()方法中

解密过程的话，我不擅长密码学，这种看着我头晕，涉及到aes啥的加密解密我就会跳过。所以依旧一样，跳！！！

此处继续返回到了上一层，我们可以看出这个byteSource是aes解密出来的序列化流，然后再默认字符集将字符串编码为 byte 序列，并将结果存储到一个新的 byte 数组`serialized`中，那接下来我们就差反序列化了

```
得到rememberMe的cookie值 --&gt; Base64解码 --&gt; AES解密 --&gt; 反序列化

```

我们继续return，返回到上一层

顾名思义，一看名字就知道是反序列化的方法，我们跟进`deserialize()`方法查看

看到还有一层，我们继续F7跟进

形成反序列化漏洞的话，没有`readObject()`怎么可能呢？

所以我们看到了最后一道光，就这么愉快的结束了。

## 0x06、总结

其实这个还是得学习学习加密解密的方法，才能进行编写poc，但是此处只是了解个思路。具体可参考其他文章；

https://www.anquanke.com/post/id/225442#h2-7

https://mp.weixin.qq.com/s/ayZKDVnN7zEbKjo5w8uqxQ

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/03c2eb1f39994cb9b2ef6b8bdc977678.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/1a6f31cbcb53462485a3df10bb81327f.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/0862ad6d928e4c9e8d70ddcd9aeaa35d.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/cde9e100231a4e28aa06fb8238f90aca.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/99f4defa50624d2b87b1c484b179517a.png" width="665"/>

应急响应笔记

学习路线
