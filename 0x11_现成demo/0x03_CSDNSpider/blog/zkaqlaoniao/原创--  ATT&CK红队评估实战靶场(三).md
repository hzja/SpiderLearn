# 原创
：  ATT&CK红队评估实战靶场(三)

# ATT&amp;CK红队评估实战靶场(三)

### 靶场描述

```
基本信息

作者：licong

环境配置

打开虚拟机镜像为挂起状态，第一时间进行快照，部分服务未做自启，重启后无法自动运行。

挂起状态，账号已默认登陆，centos为出网机，第一次运行，需重新获取桥接模式网卡ip。

除重新获取ip，不建议进行任何虚拟机操作。

参考虚拟机网络配置，添加新的网络，该网络作为内部网络。

注：名称及网段必须符合上述图片，进行了固定ip配置。

描述

目标：域控中存在一份重要文件。

本次环境为黑盒测试，不提供虚拟机账号密码。

```

### 利用漏洞进入内网

##### 端口扫描

##### 弱口令检测

##### 连接数据库

```
看到有joomla库，猜测有joomlaCMS

```

```
dirsearch扫一下目录
访问/administrator/目录

```

```
到数据库查看管理员账户密码尝试登录，失败 密码解密不出来

尝试重置管理员账户密码

官方文档：https://docs.joomla.org/How_do_you_recover_or_reset_your_admin_password%3F/zh-cn

```

##### 重置管理员密码

```
根据官方文档做出调整，否则无法修改

调整为：

INSERT INTO `am2zu_users`
   (`name`, `username`, `password`, `params`, `registerDate`, `lastvisitDate`, `lastResetTime`)
VALUES ('Administrator2', 'admin2',
    'd2064d358136996bd22421584a7cb33e:trd7TvKHx6dMeoMmBVxYmg0vuXEA4199', '', NOW(), NOW(), NOW());
INSERT INTO `am2zu_user_usergroup_map` (`user_id`,`group_id`)
VALUES (LAST_INSERT_ID(),'8');

新管理员账户admin2 密码解密后 secret

```

##### 文件上传getshell

```
在Extensions -&amp;gt; Templates -&amp;gt; Templates可以编辑模板文件

```

```
小马的位置在templates/beez3目录下，可以自己搭建cms了解一下

注意，这里有细节！！小马的名字要是nf.php

```

##### 连接蚁剑

```
命令执行不了，但文件管理处任然可以操作

看来是disable_functions的限制了，在之前的dirsearch扫描时看到了phpinfo的信息

```

```
果然是使用了disable_functions

我们利用 LD_PRELOAD 环境变量绕过

github下载地址https://github.com/yangyangwithgnu/bypass_disablefunc_via_LD_PRELOAD

把bypass_diablefunc.php和bypass_diablefunc_x64.so一起上传到一个目录下

访问http://192.168.3.23/templates/beez3/bypass_diablefunc.php?cmd=whoami&amp;amp;outpath=/tmp/baji&amp;amp;sopath=/var/www/html/templates/beez3/bypass_disablefunc_x64.so

在cmd传参后执行系统命令

```

```
查看ip地址，发现没有192.168.3.23的ip地址

猜测使用了反向代理，而当前能命令执行的机子又是不出网的

```

##### 敏感信息泄露

```
在启用反向代理的主机文件里发现了账户和密码

而刚好之前扫描出了22端口，尝试ssh远程连接

```

```
成功连接上之后发现时普通用户权限，尝试脏牛提权

github下载地址
https://github.com/FireFart/dirtycow

```

```
提权成功，通过反弹上线msf

```

```
开启apache服务，靶机wget下载木马连接msf

```

### 拿下反向代理的ubuntu

```
之前能够完成命令执行的机子，我花那么多功夫在他身上，怎么能拿不到shell呢？

之前苦于连接不通，现在有centos作为跳板就可以用木马连上了，我实验啊能连上的时候忘记截图了。。。

我用的是venom和proxychains完成连接的

```

### 内网渗透拿下域控

```
添加路由，use auxiliary/scanner/portscan/tcp进行内网信息收集

```

```
192.168.93.20开启了445端口

爆破密码

得到密码123qwe!ASD

下载wmi工具使用psexec登录到192.168.93.20

```

##### wmi工具的安装

```
下载地址：https://github.com/CoreSecurity/impacket/blob/master/examples/wmiexec.py

git clone https://github.com/CoreSecurity/impacket.git

cd impacket/

pip install .  （pip install . 两个空格）（若pip安装出错，尝试apt install gcc-9-base ，重新下载apt-get install python-pip）

```

使用msf上的psexec工具会出很多问题

```
到example目录下

执行 proxychains python3 wmiexec.py -debug 'administrator:123qwe!ASD@192.168.93.20'

```

##### mimikatz获取账号密码

```
用smbclient配合proxychain来上传mimikatz

抓取到密码zxcASDqwe123!!

```

##### 拿下域控

```
域控开了445端口，可以用psexec配合抓取到的密码拿下域控shell

```

靶场地址<br/> http://vulnstack.qiyuanxuetang.net/vuln/detail/5/

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/775b70a640f3406c9c43e158c0ee5de0.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/448eebe4ae134ec0a4d4f0940b179d6b.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/55002748c14044159cc4d3abc84e42bc.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4983f89af9b74cdea111e7eebb4ac013.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/422cc37b8a044fff86a69a71dca35368.png" width="665"/>

应急响应笔记

学习路线
