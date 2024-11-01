# 转载
：  从webpack开始发现的漏洞大礼包

# 从webpack开始发现的漏洞大礼包

### 前言

**信息收集贯穿渗透测试的全过程**

### webpack发现后台地址

日常SRC发现一个比较偏僻的域名，很有可能存在漏洞。git搜域名没找到源码。顺手翻了下js，发现webpack打包的源码，然后赶紧去搜了搜这个怎么利用，发现主要是用来找里面的接口，尝试未授权的思路。这个站点的webpack没有发现什么能未授权的接口，但是发现了config.js文件。这个肯定得进去看看，里面发现了3个地址，都是后台应该有两个是测试阶段的站点，另一个是生产环境。

### 后台常规的信息收集和初步测试

常规登录框测试手段，简单测口令，然后验证码能不能绕过开始爆破，扫目录什么的。

thinkphp3.2.3然后就是已知漏洞测试，再加上有位师傅提过的日志泄露，都测试了一遍，无果

### github泄露源码

过了好几天想起来这个站点，不甘心在后台晃悠，想起来有位师傅提起过，可以把页面上的东西都扔到github搜一下，前面已经在github上搜过域名了不好使。然后看到后台底下有个技术支持qq号码

反正没有入手点，就把qq号码扔到github上面搜索发现源码。

这里发现了两个入手点，一个是ueditor,一个是swfupload。ueditor php版本已知的应该是1.4.3 ssrf漏洞，但是是云服务器，危害不大，重心放在swfupload上面

进去swfupload文件夹里面结构是下面这样子的。

### 任意文件删除

第一个就看到任意文件删除

### 任意文件上传

upload.php太长了，最快的方法就是码云直接找个swfupload的源码，扔phpstudy，直接上传php，抓包复制过来，然后重新上传。

访问代码执行成功。

```
文章来源：https://xz.aliyun.com/t/8547</code><code>文章作者：aoteman
```

##### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
