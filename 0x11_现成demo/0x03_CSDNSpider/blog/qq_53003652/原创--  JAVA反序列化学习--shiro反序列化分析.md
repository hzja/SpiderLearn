# 原创
：  JAVA反序列化学习--shiro反序列化分析

# JAVA反序列化学习--shiro反序列化分析

最近参加了某攻防活动，也是遇到了很多的shiro反序列化，上手后也是直接拿起工具就用，原理也仅仅是了解，菜鸟对于shiro也是有太多不了解的，接下来就详细分析一下shiro反序列化产生的原理。

### shiro分类

在shiro版本小于1.2.5时，被称作shiro-550，shiro反序列化的产生原因主要是因为rememberMe内容，原因是AES密钥被硬编码在shiro源码中，导致在cookie中的rememberMe可以被插入恶意代码造成代码执行。在1.2.5之后，shiro使用了随机密钥，又因为padding oracle attack导致反序列化，被称作shiro-721。

### 详细分析

#### 一.shiro环境搭建：

1.下载shiro1.2.4:<br/> [https://codeload.github.com/apache/shiro/zip/shiro-root-1.2.4](https://codeload.github.com/apache/shiro/zip/shiro-root-1.2.4)<br/> 2.IDEA打开shiro,修改shiro/samples/web/pom.xml路径下jstl的依赖版本为1.2，没有就自己加一个<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d7aaf2f832b79d9ac62d00537e0184d1.jpeg"/><br/> 3.启动IDEA内置tomcat服务<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3e21571d7f067cc18915d453c4871be8.jpeg"/>

#### 加密分析

点击log in看到登录界面，开始一步一步分析。在AbstractShiroFilter.class下断点，大概在151行的位置，登录时会断在这里，<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1939e1967034c29d3965f4631b4b2ec7.jpeg"/><br/> 在第157行会创建subject，使用cookie，后续再分析。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e6d865469b86a12a624de6f6d70b3dc6.jpeg"/><br/> 步入executeChain<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a5323af5da509f25ca11d07421465893.jpeg"/><br/> 可以跟着来到AuthenticatingFilter.class，这里是在进行处理登录<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5e132a3e62de2f1c9ab9878662a3c655.jpeg"/><br/> 再往下看，登录成功后触发this.onLoginSuccess<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8432bf566566a1f7a2b35fc97b161bd9.jpeg"/><br/> 一直来到DefaultSecuirtyManager.class,找到rememberMeSuccessfulLogin函数<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/317a551d6b39fcfd105332e492df0721.jpeg"/><br/> 看到RememberMeManager不为空后，继续走到达AbstractRememberMeManager.java<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/31502bc15d861ae8e10385ac4f2b06f2.jpeg"/><br/> 跟进forgetIdentity，来到CookieRememberMeManager.class<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a5c562c54a3efeab5565da0e70f476be.jpeg"/><br/> 继续步入this.forgetIdentity，再单步步入this.getCookie().removeFrom(request, response)<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4056ed5bb0dfba35bb190cf9469ee8dc.jpeg"/><br/> 可以看到rememberMe和deleteMe字段，并且通过addCookieHeader写入cookie中，返回AbstractRememberMeManager.class，this.isRememberMe(token)检查是否选中登陆时Remember Me选项，接着单步步入rememberIdentity<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6842cc5cef0f3614e6e082bb4b5beb5c.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/71893485010bc7189f6d1a15a4f60e63.jpeg"/><br/> convertPrincipalsToBytes是转化成bytes，就在这里还进行了serialize序列化，然后判断不为空后进入this.encrypt,单步步入encrypt函数,密码服务为AES/CBC/PKCS5Padding<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/497e0b26448613fc02bfc9e92dfb8e14.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fe7f0117529bda54c36104340a6f50c9.jpeg"/><br/> 接着进入this.getEncryptionCipherKey()，单步步入，发现CipherKey就是AbstractRememberMeManager.class开头的DEFAULT_CIPHER_KEY_BYTES=”kPH+bIxk5D2deZiIxcaaaA==”<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b1d14435e8eb41aa1302a1e6f2b612a4.jpeg"/><br/> 获取了CipherKey返回后进入cipherService.encrypt函数中，生成初始化向量ivBytes后，进入具体的加密函数，最后return。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/83d3e5d620a95d92cdd39dd358c1b5de.jpeg"/><br/> 一步步return bytes后，回到rememberIdentity函数，下面的rememberSerializedIdentity实现了记住序列化身份的功能，跟进<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ab6f0c7836e9ee1565d3ed0491fa2a91.jpeg"/><br/> 在这里进行base64后，将信息加入到cookie中<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a997fa72adb96b8f26c5b87b0f9f00f3.jpeg"/><br/> 然后一直返回，到AuthenticatingFilter#executeLogin处理登录，返回成功登陆<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1270699b9c0c5128a4e6e8d3962c3ea8.jpeg"/>

#### 解密分析

在AbstractShiroFilter.class#doFilterInternal下断点，单步到DefaultSecurityManager#createSubject<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5776bc393270add5fdadfbe5419159e7.jpeg"/><br/> 进入resolvePrincipals，单步到getRememberedIdentity，RememberMeManager获取后进入rmm.getRememberedPrincipals(subjectContext)<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/250f2aadbf8748c487d169a2c78f2fbc.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/034914d613c0f2c2cf382355178ae185.jpeg"/><br/> 第一个函数getRememberedSerializedIdentity，可以看到先获取cookie中的值，然后base64解密，生成二进制数后返回<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7fa1672b7fe1910570679b5f794a5c76.jpeg"/><br/> 第二个函数convertBytesToPrincipals，先获取解密服务，解密服务不为空后，将二进制数据传入decrypt函数进行解密，之后return this.deserialize(bytes)<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/07731a644ed07c9e413c68e267f0be1c.jpeg"/><br/> 在deserialize(bytes)中有readObject()，触发apache.commons利用链漏洞<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/02234a95e52c8b85b6003820c638c18f.jpeg"/>

#### 结论

整个过程就是<br/> • 读取cookie中rememberMe值

• base64解码

• AES解密

• 反序列化<br/> 只要获取到密钥，就可以进行反序列化操作，在1.2.5之后，shiro采取了随机密钥，虽然阻止了shiro550的利用方式。但由于padding oracle attack也导致了反序列化。
