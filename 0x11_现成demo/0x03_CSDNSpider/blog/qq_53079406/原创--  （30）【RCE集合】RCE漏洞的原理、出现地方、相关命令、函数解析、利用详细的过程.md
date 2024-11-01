# 原创
：  （30）【RCE集合】RCE漏洞的原理、出现地方、相关命令、函数解析、利用详细的过程

# （30）【RCE集合】RCE漏洞的原理、出现地方、相关命令、函数解析、利用详细的过程

**目录**

[一、介绍：](#%E4%B8%80%E3%80%81%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[二、原理：](#%E4%BA%8C%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[三、漏洞出现](#%E4%B8%89%E3%80%81%E6%BC%8F%E6%B4%9E%E5%87%BA%E7%8E%B0)

[3.1、代码执行：](#3.1%E3%80%81%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%EF%BC%9A)

[3.1.1、脚本：](#3.1.1%E3%80%81%E8%84%9A%E6%9C%AC%EF%BC%9A)

[3.1.2、产生：](#3.1.2%E3%80%81%E4%BA%A7%E7%94%9F%EF%BC%9A)

[3.2、命令执行：](#3.2%E3%80%81%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%EF%BC%9A)

[3.2.1、系统：](#3.2.1%E3%80%81%E7%B3%BB%E7%BB%9F%EF%BC%9A)

[3.2.2、产生：](#3.2.2%E3%80%81%E4%BA%A7%E7%94%9F%EF%BC%9A)

[四、命令：](#%E4%B8%89%E3%80%81%E5%91%BD%E4%BB%A4%EF%BC%9A)

[4.1、执行系统命令的函数（PHP中）](#3.1%E3%80%81%E6%89%A7%E8%A1%8C%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E7%9A%84%E5%87%BD%E6%95%B0%EF%BC%88PHP%E4%B8%AD%EF%BC%89)

[4.1.1、system()](#3.1.1%E3%80%81system%28%29)

[4.1.2、passthru()](#3.1.2%E3%80%81passthru%28%29)

[4.1.3、exec()](#3.1.3%E3%80%81exec%28%29)

[4.1.4、shell_exec()](#3.1.4%E3%80%81shell_exec%28%29)

[4.1.5、popen()](#3.1.5%E3%80%81popen%28%29)

[4.1.6、proc_open()](#3.1.6%E3%80%81proc_open%28%29)

[4.1.7、pcntl_exec()](#3.1.7%E3%80%81pcntl_exec%28%29)

[4.2Windows系统命令拼接](#3.2Windows%E7%B3%BB%E7%BB%9F%E5%91%BD%E4%BB%A4%E6%8B%BC%E6%8E%A5)

[4.2.1、“|”:commandA | commandB](#3.2.1%E3%80%81%E2%80%9C%7C%E2%80%9D%3AcommandA%20%7C%20commandB)

[4.2.2、“&amp;” commandA &amp; commandB](#3.2.2%E3%80%81%E2%80%9C%26%E2%80%9D%20commandA%20%26%20commandB)

[4.2.3、“||” commandA || commandB](#3.2.3%E3%80%81%E2%80%9C%7C%7C%E2%80%9D%20commandA%20%7C%7C%20commandB)

[4.2.4、“&amp;&amp;” commandA &amp;&amp; commandB](#3.2.4%E3%80%81%E2%80%9C%26%26%E2%80%9D%20commandA%20%26%26%20commandB)

[五、利用过程：](#%E5%9B%9B%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[ 5.1、pikachu（RCE-exec"ping"）](#%C2%A04.1%E3%80%81pikachu%EF%BC%88RCE-exec%22ping%22%EF%BC%89)

[5.1.1、 分析：](#4.1.1%E3%80%81%20%E5%88%86%E6%9E%90%EF%BC%9A)

[ 5.1.2、漏洞利用：](#%C2%A04.1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%EF%BC%9A)

[5.2、 pikachu（RCE-exec"evel"）](#4.2%E3%80%81%20pikachu%EF%BC%88RCE-exec%22evel%22%EF%BC%89)

[5.2.1、 分析：](#4.2.1%E3%80%81%20%E5%88%86%E6%9E%90%EF%BC%9A)

[5.2.2、漏洞利用：](#4.2.2%E3%80%81%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%EF%BC%9A)

---


## 一、介绍：

> 
利用RCE漏洞，有两种执行方式，向后台服务器远程注入操作系统命令（即远程命令执行RemoteCommand Exec）或者远程代码执行（Remote Code Exec），顾名思义就是远程执行，通过上述的远程注入后，从而执行系统命令，进而控制后台系统。


## 二、原理：

> 
我在软件工程等课程中都有看到，为满足用户远程执行等功能（如路由器、防火墙、入侵检测等设备的web管理界面上ping操作的web界面），在设计的时候都会设置提供给用户的接口。如果对用户的输入没有做严格的安全控制，这些接口可能会被攻击者利用提交远程执行命令或代码，进一步控制了整个后台系统。


## 三、漏洞出现

### 3.1、代码执行：

> 
<h4>3.1.1、脚本：</h4>
PHP、java、python
<h4>3.1.2、产生：</h4>
web源码：thinkphp、eyoucms、WordPress
中间件平台：Tomcat、Apache Struts2、Redis
其他环境：PHP-CGI、Jenkins-CI、Java RMI


#### 3.1.2、产生：

### 3.2、命令执行：

> 
<h4>3.2.1、系统：</h4>
Linux、windows
<h4>3.2.2、产生：</h4>
web源码：Nexus、Webmin、ElasticSearch
中间件平台：weblogic、Apache
其他环境：postgresql、samba、supervisord


#### 3.2.2、产生：

<br/>  

## 四、命令：

### 4.1、执行系统命令的函数（PHP中）

> 
<h4>4.1.1、system() </h4>
执行shell命令，向dos发送一条指令，如system("pause")可以实现冻结屏幕，便于观察程序的执行结果；system("CLS")可以实现清屏操作；而调用color函数可以改变控制台的前景色和背景。
int system(const char *command)

<h4>4.1.2、passthru() </h4>
只调用命令，不返回任何结果，但把命令的运行结果原样地直接输出到标准输出设备上

<h4>4.1.3、exec() </h4>
在PHP中，执行一个外部程序， exec() 执行 command 参数所指定的命令。 
语法： exec(string $command, array &amp;$output = ?, int &amp;$return_var = ?): string

<h4>4.1.4、shell_exec() </h4>
是PHP中的一个内置函数，用于通过shell执行命令并以字符串的形式返回完整的输出

<h4>4.1.5、popen() </h4>
通过创建一个管道，调用 fork 产生一个子进程，执行一个 shell 以运行命令来开启一个进程。这个进程必须由 pclose() 函数关闭，而不是 fclose() 函数。pclose() 函数关闭标准 I/O 流，等待命令执行结束，然后返回 shell 的终止状态。如果 shell 不能被执行，则 pclose() 返回的终止状态与 shell 已执行 exit 一样
语法：
FILE * popen ( const char * command , const char * type );
int pclose ( FILE * stream );

<h4>4.1.6、proc_open() </h4>
执行一个命令，并且打开用来输入/输出的文件指针
类似 popen() 函数， 但是 proc_open() 提供了更加强大的控制程序执行的能力。 
语法：resource proc_open ( string $cmd , array $descriptorspec , array &amp;$pipes [, string $cwd [, array $env [, array $other_options ]]] ) 

<h4>4.1.7、pcntl_exec()</h4>
在当前进程空间执行指定程序
语法：void pcntl_exec ( string $path [, array $args [, array $envs ]] ) 


#### 4.1.2、passthru() 

#### 4.1.4、shell_exec() 

#### 4.1.6、proc_open() 

### 4.2Windows系统命令拼接

> 
<h4>4.2.1、“|”:commandA | commandB</h4>
管道符，A命令的标准输出，作为B命令的标准输入

<h4>4.2.2、“&amp;” commandA &amp; commandB </h4>
先运行输出命令A，然后运行输出命令B

<h4>4.2.3、“||” commandA || commandB </h4>
先运行输出命令A，如果失败则运行输出命令B

<h4>4.2.4、“&amp;&amp;” commandA &amp;&amp; commandB </h4>
如果运行输出命令A成功，则继续运行输出命令B<br/> （命令A未执行成功，则命令B不执行）


#### 4.2.2、“&amp;” commandA &amp; commandB 

#### 4.2.4、“&amp;&amp;” commandA &amp;&amp; commandB 

（迟来的祝愿：愿远方只有快乐，挺帅一小伙子的，和我差不多帅，嘻嘻嘻） 

## 五、利用过程：

###  5.1、pikachu（RCE-exec"ping"）

> 
<h4>5.1.1、 分析：</h4>
可以看见给用户提供了一个ping操作的web界面
当输入目标网址后，点击提交，服务器后台会对输入的地址进行了ping测试，并返回了测试结果
www.iqiyi.com



www.iqiyi.com|dir
大多数操作系统（包括DOS及Windows）中dir命令基本上会列出目录中的文件及子目录的名称，也可以列出其文件大小，创建时间等相关信息，并且列出所在的磁盘、可用空间等信息。dir命令也可以寻找其文件名称符合特定条件的文件。
Linux中ls 命令显示当前目录的内容


127.0.0.1 &amp; ipconfig




111 &amp; whoamI
得到设备名，以及用户名



<h4> 5.1.2、漏洞利用：</h4>
查看权限
Linux下的话使用 ls -al  // a表示全部的包括u，g和o，l表示列出相关信息
windows下 attrib 1.txt   // 查看当前目录下1.txt的属性,包括读写操作属性


如果当前目录有写入权限，就写入木马
反之，没有写入权限，再进行反弹测试
        如果失败，寻找一个可写入可执行的文件（777），并利用RCE漏洞编写一个bash反弹脚本  
                再进行监听、并利用RCE漏洞执行脚本



####  5.1.2、漏洞利用：

### 5.2、 pikachu（RCE-exec"evel"）

> 
<h4>5.2.1、 分析：</h4>
要输入普通字符串，没什么大用（尝试试试php函数） 





再尝试输入一个php函数，看能不能被执行
phpinfo();


没有对用户的输入做严格的过滤，导致被当做PHP脚本执行了，产生了漏洞





<h4>5.2.2、漏洞利用：</h4>
查看数据包，可以知道表单的参数是txt 












我试的时候，直接复制粘贴过去会报错

 连接失败改错
我再尝试把这个URL编码的大写都改为了小写，然后就成功了
（再次查看值的时候自己变了大写）



利用system()函数,  或者shell_exec()函数，再写反弹脚本
也可直接写在服务器上后，在执行命令下载脚本（wegt）


#### 5.2.2、漏洞利用：
