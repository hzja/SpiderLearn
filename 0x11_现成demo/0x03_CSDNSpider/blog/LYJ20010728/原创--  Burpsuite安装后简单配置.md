# 原创
：  Burpsuite安装后简单配置

# Burpsuite安装后简单配置

**1）设置代理地址和端口**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210427201226953.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> **在浏览器中设置代理服务器**

```
这一步推荐使用谷歌浏览器或者火狐浏览器
我使用的是谷歌浏览器
这里推荐一个谷歌浏览器的插件：Proxy SwitchyOmega(轻松快捷地管理和切换多个代理设置)

```

```
这里我们新建一个代理服务器，命名随意~

```

```
这里我们设置参数：
代理协议：HTTP
代理服务器：127.0.0.1（burpsuite设置的代理地址）
代理端口：8080（burpsuite设置的代理端口）

```

**3）证书导入**

```
启动我们上一步设置好的代理服务器，并且访问 http://burp(你设置的代理服务器名字)，点击右上角的按钮

```

```
打开我们下载的证书，开始安装

```

```
选择本地计算机安装 --&gt; 下一步

```

```
这里我们选择将所有的证书都放入下列存储 --&gt; 受信任的根证书颁发机构 --&gt; 确认 --&gt; 下一步

```

```
点击完成就可以使用我们的burpsuite开始快乐的抓包生活啦~

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210427202644884.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> **4）抓包**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210427202843668.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
