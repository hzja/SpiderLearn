# 原创
：  使用Hydra以及John对Linux账户密码破解-crunch以及pydictor字典生成工具

# 使用Hydra以及John对Linux账户密码破解-crunch以及pydictor字典生成工具

## 一、使用Hydra破解弱密码

### 1.介绍：

Hydra是一款非常强大的暴力破解工具， 它是由著名的黑客组织THC开发的一款开源暴力破解工具。Hydra是一个验证性质的工具， 主要目的是：展示安全研究人员从远程获取一个系统认证权限。

### 2.参数：

### 3.操作：
1. kali内通过命令“echo ```要向字典内添加的内容```&gt;&gt; passlist.txt/userlist.txt”创建用户名和密码的字典并向字典文档里添加内容（passlist.txt和userlist.txt），因为本实验只是为了了解操作，所以自己创建简陋的字典使用也没关系，创建之后可以通过命令“cat ``````”查看文件内容。1. 靶机内通过命令查看ip。1. 使用命令“hydra -L userlist.txt -P passlist.txt -f ```ip```（通过ip addr在靶机内查看ip） ssh -t ```1```（表示进程数，可以修改，会使破解速度改变） -v”开始进行破解。1. 密码破解成功！
## 二、使用John the ripper破解弱密码：

### 1.说明：

使用John工具需掌握两个命令， 分别是：unshadow和john命令。

在Kali Linux下默认安装了John工具， 在爆破过程中将使用默认字典进行匹配爆破，默认字典存储在Kali Linux下的/usr/share/john/password.lst文件中。

当然我们也可以自己创建弱密码字典(例如：crunch、pydictor等工具)。

crunch 是创建密码字典工具，按照指定的规则生成密码字典，可以根据情况灵活的生成字典。

pydictor是一个使用python语言开发，遵循GPLv3协议的开源命令行工具，主要用来帮助安全研究人员生成称心如意的暴力破解字典。

### 2.操作：
1. 靶机内通过命令查看靶机ip。1. kali内使用namp命令扫描靶机存在的端口，可以发现存在ssh端口。1. 靶机内为靶机创建用户abc并设置密码。1. 靶机内通过命令将两个目标文件导出。1. kali内配置kali的ssh服务：1. kali内重启ssh配置文件，开启ssh服务：1. kali内查看kali的ip为接下来传输文件做准备。1. 靶机内将之前步骤中导出的两个文件传入kali内。1. 进入kali内将两个文件提取到test_passwd中。1. kali内使用 John 破解密码。1. 密码破解成功！
### 3.注意：

破解过的用户的密码保存在/home文件夹下的隐藏文件./john/john.pot里,删除后才可以再次运行。操作过程如下:

## 三、相关文章
1. kali中开启ssh连接功能：1. 黑客工具之hydra详细使用教程