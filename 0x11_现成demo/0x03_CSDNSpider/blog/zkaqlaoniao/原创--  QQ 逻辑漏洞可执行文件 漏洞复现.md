# 原创
：  QQ 逻辑漏洞可执行文件 漏洞复现

# QQ 逻辑漏洞可执行文件 漏洞复现

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


首先拿到QQ的版本，目前可测试版本包括QQ最新版本，TIM最新版本

新创建一个bat文件（这个可以随意，上马的也可以，exe也可以） ，本次测试内容如下

 首先向你的手机端发一下文件：

发完了以后使用QQ内置的回复功能

回复了以后将该文件再次进行转发

<img alt="02da8e53b0084e1eb57ba99eb5c2ce3b.png" src="https://img-blog.csdnimg.cn/02da8e53b0084e1eb57ba99eb5c2ce3b.png"/>  <img alt="7a396121a7974c368e21e8d02c6c0dbf.png" src="https://img-blog.csdnimg.cn/7a396121a7974c368e21e8d02c6c0dbf.png"/>

点击以后可以直接落地并执行成功（期间没有任何提示或选择项）

漏洞原理：该漏洞为逻辑漏洞，腾讯QQ windows客户端的“文件传输消息”在经过“回复消息”功能处理后，该文件会变为无需任何弹管确认，点击消息文本后即可自动下载并打开文件的处理式。

经过测试cs也可以上线看

**没看够~？欢迎关注！**
