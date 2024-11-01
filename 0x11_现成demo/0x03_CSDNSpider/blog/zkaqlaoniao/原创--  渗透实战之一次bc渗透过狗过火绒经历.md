# 原创
：  渗透实战之一次bc渗透过狗过火绒经历

# 渗透实战之一次bc渗透过狗过火绒经历

**目录**

[事件起因](#h2-1)

[开始渗透](#h2-2)

[此时面临的难处](#h2-3)

[过狗转折点](#h2-4)

---


> 
公众号：**黑客菌 **分享更多技术文章，欢迎关注一起探讨学习


### 事件起因

从某个大佬手上获取到含有漏洞指纹信息的bc的cms。于是想尝试一波。通过指纹找一个站点。

PS：本文仅用于技术研究与讨论，严禁用于非法用途，违者后果自负

### 开始渗透

打开链接，发现是一个登录框，说登录框有注入，直接可以得到 --os-shell的权限

登录页面，直接sqlmap进--os-shell 一把梭，得到shell了

<img alt="" height="339" src="https://img-blog.csdnimg.cn/5b5429f2c45042ed8592b8fe54e7680b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_19,color_FFFFFF,t_70,g_se,x_16" width="883"/> 将shell传给cs,先在cs上线之后，就试了一下在cs提权，发现不行，就把shell传给msf。使用土豆直接提权，很成功得到了系统权限<img alt="" height="205" src="https://img-blog.csdnimg.cn/f211937e90ea46848ebcd739731af9bd.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_12,color_FFFFFF,t_70,g_se,x_16" width="593"/>

 查看了桌面文件，是否有什么密码文件<img alt="" height="434" src="https://img-blog.csdnimg.cn/4901a4efe78a45b7b94f7d8bfb956f4b.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_15,color_FFFFFF,t_70,g_se,x_16" width="737"/>

桌面愕然显示安全狗、火绒。抱着侥幸的心里，尝试读取密码<img alt="" height="444" src="https://img-blog.csdnimg.cn/31381e4dc7554a468c1959af44a18596.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_16,color_FFFFFF,t_70,g_se,x_16" width="758"/> 密码字段无法显示出来，怀疑是安全狗搞鬼，通过taskkill 想把安全狗杀死,发现无法将安全狗杀死进程，守护进程无法杀死 <img alt="" height="482" src="https://img-blog.csdnimg.cn/2f98908bb2c149a080f46b65ada4f6df.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5riX6YCP5rWL6K-V6ICB6bifLeS5nemdkg==,size_19,color_FFFFFF,t_70,g_se,x_16" width="895"/>

 再尝试创建用户，也无法创建，于是尝试修改administrator密码，也不能。尝试重启服务器也不行。

### 此时面临的难处

无法创建用户、无法读取密码、无法杀死安全狗进程（版本4.2）。甚至重启的shutdown都无执行。也不能修改administrator密码。

### 过狗转折点

后面实在没办法了。就投向Guest用户，先开启起来

```
net user guest /active:yes
```

 很顺利，直接开启，也能成功加入administrator管理组，侥幸心理，直接登录行不。但是很遗憾，登录不上去，只是限制了登录。

于是尝试导出adminstrator的注册表值再还原回去，将值改成是Guest的，具体操作执行，修改limitblankpassworduse值为1

```
reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa\ /v limitblankpassworduse /t REG_DWORD /d 0 /f
```

 执行：

```
reg export "HKEY_LOCAL_MACHINE\SAM\SAM\Domains\Account\Users\000001F4" "C:1.reg"
```

通过msf下载下来，导出administrator的注册表值到某路径,修改内容，将"V"值删除，只留F值,将1F4修改为1F5,保存

修改以后导入到注册表里面。再执行导入注册表

```
regedit /s C:\2.reg
```

这样子直接登录了。最后上图

登陆后发现，果然火绒一大堆日志，看到拦截操作。

再看看web的管理页面控制台。

细品，细品，细品

自己细品，不多说了~ 

 

 
