# 原创
：  手把手教你如何批量PTH获取主机权限

# 手把手教你如何批量PTH获取主机权限

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


——

利用CrakMapExec工具进行全网段批量PTH

CrackMapExec（CME）是一款后渗透利用工具，可帮助自动化大型活动目录(AD)网络安全评估任务。其缔造者@byt3bl33d3r称，该工具的生存概念是，“利用AD内置功能/协议达成其功能，并规避大多数终端防护/IDS/IPS解决方案。”

尽管这个项目带有攻击性，但是蓝队也可以用于自检评估账户权限，模拟攻击，配置错误权限

kali安装方法：apt-get install crackmapexec

它所支持的协议有：http,smb,mssql

如果在得到明文密码的情况下，可以批量去探测全网段账号密码

但如果你没有明文密码也没关系，用Mimikatz找到用户的hash，给他配置上去也可以批量探测hash

添加指定ip也可以单个扫描喔

得到一个可用的权限之后，可以执行一些相关命令得到对方的一些信息

例如执行命令：-x ipconfig

例如枚举共享：—shares

枚举有效sessions：—session

枚举磁盘：—disks

枚举登录用户：—loggedon-users

枚举域用户：—users

通过爆破RID枚举用户：—rid-brute

获取域密码策略：—pass-pol

翻译：

msf批量进行PTH渗透

我们先监听上线，得到session之后，我们获取一下administrator的hash

然后复制下来，待会用

攻击成功后，会返回一个meterpreter类型的session

在上一个设置参数的步骤RHOSTS可以设置全网段，可批量

> 

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/79cd923d77cd45b0abeb2f62af851fd8.png" width="1024"/>

渗透工具

学习路线
