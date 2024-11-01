# 原创
：  内网神器cobaltstrike使用教程

# 内网神器cobaltstrike使用教程

## 一、安装使用

<br/>**安装**

系统环境：需要java环境Oracle Java 1.8，Oracle Java 11

下载解压就可以使用

**使用**<br/> 首先要运行服务端，如果你有个外网的机器，可以把服务端运行于外网的机器上，也可以运行于本地

服务端启动命令

windows<br/> 运行teamserver.bat<br/> teamserver.bat 1.1.1.1 123456

linux

需要有足够权限，可以通过chmod +x teamserver 来提高权限<br/> ./teamserver 1.1.1.1 123456

这里为设定一个服务端，前面为服务端所在机器的ip ，后面为密码

启动服务端后，我们就可以启动客户端去连接了

**运行<br/> windows**

```
双击start.bat运行客户端，选择相应服务器连接

```

<br/>**linux**

```
需要有足够权限，可以通过chmod +x start.sh 来提高权限
切换到相应目录下，使用start.sh来运行客户端
```

## <br/> 二、监听器 listner

<br/> cobaltstrike里的监听器类似于msf里的exploit,一个监听器是一个payload配置信息，同时也用于cobaltstrike起的一个用于接受来自这个payload的连接指示，beacon 是cobaltstrike的内置监听器

使用<br/> 点击配置监听，就会列举出所有配置的payload和监听器

```
Add添加新的监听
edit编辑已有监听
remove删除监听
restart重启监听

```

<img alt="" height="240" src="https://img-blog.csdnimg.cn/direct/92ebf58398584a20a61628461d6db048.png" width="764"/><br/> 要添加监听器可以点击Add，这里的监听器根据所通过的协议和监听器位置分为8种

**不同监听介绍**

```
1.beacon dns
2.beacon http
3.beacon https
4.beacon smb
5.beacon tcp
6.external c2
7.foreign reverse_http8.foreign reverse_https
```

**这里选择不同协议的监听器就是让这个beacon通过不同的协议和方式去出口网络**

**beacon dns**

beacon dns通过使用dns来进行通信，传达命令，攻击机将请求信息这些通过dns域名中转发送给被攻击者

DNS host中填入所用到的dns域名，host(stager) 处也同样填入dns域名信息，port处填入端口，用于重定向

**beacon http**

通过http来进行通信，传达命令<img alt="" height="524" src="https://img-blog.csdnimg.cn/direct/005fc13bc4db438d95c3ab941bc5a7ed.png" width="451"/>

http hosts 和 http host(stager) 都填写攻击机的ip或C2域名，http port处填写端口，bind处的端口用于绑定web服务端口，一般用于重定向，host header用于域前置技术，用于隐藏C2，proxy 用于代理设置

**beacon https**

通过https来进行通信，传达命令，和http的区别在于https加密了信息

**beacon smb**

beacon smb使用命名管道进行通信，将流量封装在smb协议里，smb这个一般不用于直接生成可用载荷，一般结合PsExec 或 stageless payload使用

**beacon tcp**

通过tcp协议进行通信，可以通过cobaltstrike里的stageless payload去运行，其他的和beacon smb 差不多，但是tcp的可以直接生成载荷去运行

**external c2**

external c2允许第三方程序充当cobaltstrike的teamserver 和beacon之间处理C2通信的接口，通常用于目标无法出网的情况，第三方程序使用外置的C2服务器和cobaltstrike服务器交互

**foreign reverse_http**

把会话信息传递给msf，将目标权限通过http的方式传给msf

**foreign reverse_https**<br/> 和foreign reverse_http利用方式类似，只不过通过https去传递会话信息

## 三、木马

<br/> 生成后门

常用生成后门方法有

```
HTML Application
MS Office Macro
Payload Generator
Windows Executable
Windows Executables
```

**1.HTML Application**

一个html应用程序类型的后门，有三种文件生成方式，分别为VBA，Powershell，Executable这三种方式

**2.MS Office Macro**

MS Office Macro生成一个宏文件，该宏文件用于嵌入Microsoft word 或 Microsoft execl文件里，生成该宏文件并提供嵌入的方法

首先选择MS Office Macro

选择好监听器

直接生成利用的代码

复制下来，然后放到文档的宏里去

这里用Microsoft Office Word 2003去测试，首先打开word文档，点击工具找到宏<br/> 然后添加进去

然后在文档里启用该宏，得到会话

**3.Payload Generator**

使用不同的格式语言导出cobaltstrike的shellcode，然后使用其他语言去编译生成，

使用时选择好监听器，并选择不同的输出格式

选择监听器，再选择相应输出的语言

**4.Windows Executable**

生成一个可执行的exe木马

选择好监听器和输出的文件格式

分别有

windows exe，windows server exe，windwos DLL 32位，windwos DLL 64位

windows exe

生成一个windwos可执行文件

windows server exe<br/> windows server exe也是一个windwos可执行文件

和上面的区别在于，windows server exe可响应Service Control Manager 命令，windows server exe可作为服务器自启动的exe,而一般生成的windows exe则不能

windwos DLL 32位，windwos DLL 64位分别生成不同位数的dll文、生成的dll文件可以通过捆绑等方式进行利用

**5.Windows ExecutableS**<br/> 和Windows Executable区别在于，它是直接导出一个beacon,这个beacon是直接写好的32或64位的dll，直接和监听器连接，传输数据和命令，它还可以导出powershell脚本，还可以通过raw选项调出.bin 文件，使用和Windows Executable差不多

生成payload，目标机点击触发上线

钓鱼攻击

cobaltstrike里有多种钓鱼攻击的方式，适用于不同环境

web服务管理

用于管理cobaltstrike web服务器上的可用程序，通过文件下载去添加管理

克隆网站

<img alt="" height="335" src="https://img-blog.csdnimg.cn/direct/2a91108349fb456b9dce5a560dc67236.png" width="356"/><br/> 通过克隆复制站点，诱使受害者访问

克隆网址：添加目标站点的URL，此处需要添加完整的url，包含http协议和端口

local url：本地站点的克隆路径<br/> local host：本地站点主机ip<br/> local port：本地站点端口 Attack:<br/> 此处用于添加克隆站点后执行的漏洞脚本

点击clone后，会返回生成的克隆站点地址

访问测试站点地址<img alt="" height="687" src="https://img-blog.csdnimg.cn/direct/15d101b310574da197587fdc373730dd.png" width="931"/>

开启键盘记录后就可以在web日志中看到输入记录<img alt="" height="263" src="https://img-blog.csdnimg.cn/direct/55fbb03b49b54f68aa207e1820879b9c.png" width="739"/>

attack处可以结合Scripted Web Delivery攻击，通过Scripted Web Delivery生成的payload来在克隆站点添加payload去攻击，也可以通过在生成后门处的HTML Application

生成一个后门去结合使用

**文件下载**

作用是提供一个文件管理，并且我们可以修改里面的mine信息，上传的文件会发送到团队服务器里，供团队成员使用

实际使用时，可以上传后门等攻击文件，结合克隆站点里的attack使用

**Scripted Web Delivery**

生成一个payload(类似Windows Executable生成的)，放在cobaltstrike的服务器上，并生成一个下载运行的命令语句，方式有powershel，python,

bitsadmin(windows下载命令)

以powershell举例

目标机执行后，就会从设置的cobaltstrike的服务器的站点上下载并运行，生成新的会话

签名applet攻击

启动一个web服务器来托管一个自签名的java applet，被攻击者会被提示给这个applet权限来运行，一但允许就可以获得权限

选择相应的监听器进行攻击

**智能攻击**<br/> 在一个程序里包含多种漏洞利用方式，启动一个web服务器去托管applet，可以分析环境并决定使用哪种漏洞利用方式

注：此攻击在目前新的环境中难以发挥作用

**邮件钓鱼**

<br/>**内容**

targets

选择保存有发送目标的文档

tmplate<br/> 邮件模板，在邮箱里导出一个邮件文件

attachment<br/> 附件，可以通过上传恶意附件来进行攻击，典型的可以通过和MS Office Macro结合发送恶意的word文档来结合攻击

Embed URL<br/> 需要嵌入的站点地址，此处可嵌入钓鱼站点的地址

Mail server<br/> 用于配置smtp邮件服务，用于向邮件服务器进行身份验证，或将邮件服务器设置为目标的开放中继或邮件交换记录

SMTP Host和Port填入邮件服务器地址，端口

Username和password处填入用户名和密码

Random Delay处填入设置的延时发送邮件时间

Bounce to用于模仿发件人，提高钓鱼的成功率

设置完之后就可以发送进行攻击了

可以先通过Preview先预览下效果

## 四、功能

<br/> 常用功能有很多

上部选项栏<br/> 攻击部分已在上面的木马处写了相关功能及使用方式

cobaltstrike选项

<br/>**新建连接：**

用于一个新的cobaltstrike服务端进行连接

设置：cobaltstrike的设置，里面有多种选项

**1.cobalt strike**

用于配置cobalt strike

标签处用于设置标签颜色

工具栏处用于设置是否显示工具栏

VNC端口处用于设置VNC端口的范围

字体设置处用于设置字体

**2.Console**

用于 Console的界面设置

**3.Fingerprints**

用于设置服务器SSL证书的SHA-1哈希值的列表，可以操作删除

**4.Graph**

设置cobaltstrike的视图外表

选择字体及颜色，还可以选择界面布局方式(建议默认)

**5.报告**

用于自定义报告模板，设置颜色。logo并加载自定义报告

**6.状态栏**

用于设置cobaltstrike里控制台的状态栏外观，可以设置它的颜色<img alt="" height="284" src="https://img-blog.csdnimg.cn/direct/a6d3e344905b421e9e16d693c47248f2.png" width="643"/>

**7.服务器**

显示配置文件里已有的服务器地址列表，此处可删除操作

可视化：用于设置可视化选项，cobaltstrike有三种可视化的视图选项<br/> 分别为枢纽视图，会话列表，目标列表

枢纽视图

可以非常清楚的看到主机之间的联系，在大规模的渗透中非常有用(这里我只是在测试靶机)<img alt="" height="303" src="https://img-blog.csdnimg.cn/direct/b239d21b53144006bc25b8dfccc71050.png" width="527"/>

会话列表

显示当前可用的会话<img alt="" height="279" src="https://img-blog.csdnimg.cn/direct/4901eda88de94937a63a851047f56220.png" width="747"/>

显示目标内部和外部的ip地址，所用监听器，用户权限，设备名称，进程名，进程的pid值，payload的位数(x64或x86)及相应时间

目标列表

显示所有的目标

VPN 接口

设置VPN接口，用于添加和删除vpn接口(后面关于对会话的操作里会介绍到的)

监听器

设置监听器(前面监听器这块有介绍)

脚本管理器

用于管理功能扩展脚本

load为读取脚本，unload为移除脚本，reload为重新加载脚本

下载可用的脚本，选择cna文件并加载

就可以使用扩展脚本

视图

<br/> 此处的视图为cobaltstrike下面的视图显示栏里的

这里只挑一部分，后面的会在会话的目标操作处讲到

**应用信息**

> 
显示目标机器的应用信息


**凭证信息**

> 
显示已有的目标的凭证(账户密码这些)


**文件下载**<br/> (后面文件管理处会介绍到的)

**日志**

> 
显示服务器的日志信息


**代理信息**<img alt="" height="266" src="https://img-blog.csdnimg.cn/direct/5d631304060b4dd4bac140e22bf22c5b.png" width="787"/>

显示当前目标的代理，和socks server结合使用

stop为停止目标接口，tunnel 为在metasploit框架中使用此命令，通过此信标对漏洞利用和辅助模块进行隧道攻击。

使用未设置的代理停止通过信标的隧道

脚本控制台

> 
用于管理脚本，对脚本进行调试和修改


标

> 
列举所有目标，作用和目标列表作用相似


web日志

> 
cobaltstrike 可以把一些服务托管到一个web服务器上，web日志用于记录cobaltstrike web服务器上的记录


报告

> 
用于生成各类报告


活动报告

> 
活动报告用于提供红队的活动信息及时间，记录在后渗透时的活动，可导出为word或pdf


主机报告

> 
用于提供cobaltstrike所收集的主机信息，服务，凭据和会话


目标报告

> 
类似于威胁情报报告里的侵害指表附录，包括了上传文件的hash值


会话报告

> 
记录了每个会话的指标和活动，包括了会话的通信路径，攻击目标的文件的md5哈希值，用于获取红队的活动信息


社会工程报告

> 
用于记录钓鱼行动的电子邮件，点击情况及从用户中收集的信息


TTPs

> 
用于把Cobalt Strike 行动映射到 MITRE 的 ATT＆CK 矩阵里的战术，MITRE ATT＆CK是一个攻击策略知识库


重置数据

> 
用于重置现有的数据


数据出口

> 
用于导出数据，有两种格式，分为TSV和xml


**下部工具栏**

选项数字按照下部选项栏顺序相对应<img alt="" height="86" src="https://img-blog.csdnimg.cn/direct/e844caabacc84b4c9a95a52c47f8998a.png" width="516"/>

1.1号为连接到cobaltstrike服务器<br/> 点击后选择一个新的cobaltstrike服务端进行连接

2.2号为断开与服务器之间的连接

3.3号为配置监听（前面监听器这块有介绍）

4.4号为切换到枢纽视图

切换为枢纽视图(上部选项栏里介绍视图部分讲到)

5.5号为切换到会话列表<br/> 切换视图为会话列表(上部选项栏里介绍视图部分讲到)

6.6号切换到目标列表<br/> 切换视图为目标列表(上部选项栏里介绍视图部分讲到)

7.7号为显示凭证信息，显示已有的目标的凭证(账户密码这些)

8.8号为文件下载(后面文件管理处会介绍到的)

9.9号为键盘记录，记录键盘的输入信息

10.10号为屏幕截图，截取目标当前屏幕

11.11号为Windows Executables，用于生成一个后门文件(前面关于木马处讲到)

12.12为设置java签名的applet攻击，上面的钓鱼攻击处讲到

13.13为MS Office 宏攻击，用于生成一个office宏病毒文件，上面生成后门处有讲到

14.14Scripted web Delivery<br/> 生成一个payload(类似Windows Executable生成的)，钓鱼攻击处会讲到

15.Host file 就是钓鱼攻击处的文件下载功能，钓鱼攻击功能处会讲到

16.web服务管理处，用于管理cobaltstrike web服务器上的可用程序，钓鱼攻击功能处会讲到

17.帮助，用于打开帮助文档

18.关于，用于查看当前cobaltstrike的版本信息

beacon的使用<br/> cobaltstrike 的beacon有许多功能，可以执行各种命令

注意，cobaltstrike有默认的60s心跳时间，导致执行命令或其他操作响应很慢，这里可以通过sleep命令去修改心跳时间

beacon常用命令

可以通过help命令去查询beacon常用指令

常用命令汉化

```
argue                   匹配进程的欺骗参数

audit_uac              审查关于bypass uac 的方法

blockdlls               在子进程中阻止非Microsoft DLL

browserpivot       设置浏览器透视会话

cancel                 取消正在进行的下载

cd                       更改目录

checkin               呼叫总部并发布数据

clear                   清除信标队列

connect              通过TCP连接到信标对等方

covertvpn           部署隐蔽VPN客户端

cp                       复制文件 

dcsync                从DC中提取密码哈希

desktop              查看目标的桌面并与之交互

dllinject             将反射DLL注入进程

dllload               使用LoadLibrary（）将DLL加载到进程中

download          下载文件

downloads          列出正在进行的文件下载

drives                  列出目标上的驱动器

elevate                在提升的上下文中生成会话

execute                在目标上执行程序（无输出）

execute-assembly      在目标上的内存中执行本地.NET程序

exit                           终止信标会话

getprivs                     在当前令牌上启用系统权限

getsystem                尝试获取系统

getuid                      获取用户ID

hashdump               转储密码哈希

help                          帮助菜单

inject                       在特定进程中生成会话

jobkill                       杀死长时间运行的利用后任务

jobs                          列出长期运行的利用后任务

jump                           在远程主机上生成会话

kerberos_ccache_use      将kerberos票证从缓存应用到此会话

kerberos_ticket_purge      从此会话中清除kerberos票证

kerberos_ticket_use          将kerberos票证应用于此会话

keylogger                        将击键记录器注入进程

kill                                   终止进程

link                                 通过命名管道连接到信标对等点

logonpasswords               使用mimikatz转储凭据和哈希

ls                                    列出文件

make_token                    创建令牌以传递凭据

mimikatz                          运行mimikatz命令

mkdir                               制作目录

mode dns                        使用DNS A作为数据通道（仅DNS信标）

mode dns-txt                  使用DNS TXT作为数据通道（仅DNS信标

mode dns6                     使用DNS AAAA作为数据通道（仅DNS信标）

mv                                  移动文件

net                                  网络和主机枚举工具

note                                为该信标指定一个注释

portscan                         扫描网络中的开放服务

powerpick                      通过非托管PowerShell执行命令

powershell                      通过powershell.exe执行命令

powershell-import          导入powershell脚本

ppid                               为衍生的事后交货作业设置父PID

ps                                  显示进程列表

psinject                          在特定进程中执行PowerShell命令

pth                                使用Mimikatz传递散列

pwd                               打印当前目录

reg                                  查询注册表

remote-exec                    在远程主机上运行命令

rev2self                         还原为原始令牌

rm                                 删除文件或文件夹

rportfwd                      设置反向端口前进

run                              在目标上执行程序（返回输出）

runas                          以另一个用户的身份执行程序

runasadmin                在提升的上下文中执行程序

runu                           在另一个PID下执行程序

screenshot                   截图

setenv                        设置环境变量

shell                          通过cmd.exe执行命令

shinject                    将外壳代码注入进程

shspawn                  生成进程并将外壳代码注入其中

sleep                       设置信标睡眠时间

socks                        启动SOCKS4a服务器以中继流量

socks stop              停止SOCKS4a服务器

spawn                    生成会话

spawnas                 作为另一个用户生成会话

spawnto                 将可执行文件设置为将进程生成到

spawnu                   在另一进程下生成会话

ssh                          使用SSH在主机上生成SSH会话

ssh-key                    使用SSH在主机上生成SSH会话

steal_token              从进程中窃取访问令牌

timestomp               将时间戳从一个文件应用到另一个文件

unlink                     断开与父信标的连接

upload                     上传文件
```

<br/> 我用的是4.0版本的cobaltstrike， 命令和3版本的不同

**会话功能**

建立连接后，有许多会话功能可以供我们使用

在和目标建立的会话出右键，即可看到会话功能

**执行**<br/> 首先看执行处所有的功能

执行处的功能分别有

转储HASH，提权，黄金票据，制作令牌，one-liner，run mimikatz（运行mimikatz），spawn As（用其他用户去生成cobaltstrike监听器）

**1.转储HASH**<br/> 这里的转储HASH就是获取hash值

测试效果如下

得到了密码的hash值

**2.提权**<br/> 这里的提权利用了各种方式来提权

选择好相应的监听器和exploit进行提权

2.1 uac-token-duplication<br/> 是一种绕过uac方式的攻击，吧地权限提高到高权限，利用一个UAC漏洞，允许非提升进程使用提升进程中窃取的令牌来启动，适用于win7

2.2 svc-exe<br/> 用于提升权限，用法类似getsystem命令

2.3 ms14-058|ms15-015|ms16-016|ms16-032|ms16-032|ms16-315

这几种方式都差不多，通过windows的本地提权漏洞来提权

2.4 juicypotato

在cobaltstrike中使用烂土豆来提权，相对可靠

2.5 compmgmt

了解不多，似乎是通过windows的compmgmt去提权

2.6 rottenpotato

从Windows服务帐户到系统的本地权限升级

2.7 uac-eventvwr

通过注册表，利用eventvwr.exe 会自动加载我们的exp，这时的eventvwr.exe为高权限，达到提权效果

2.8 uac-dll

利用UAC漏洞，把我们的exp生成的dll复制到特定位置来达到提权效果，可绕过UAC<br/> uac-wscript

这是一个empire中的绕过UAC模块，通过利用wscript.exe 去执行payload，以管理员权限去运行payload，只限于win7上使用

**3.黄金票据**<br/> 用于生成黄金票据

填入通过mimikatz得到的数据，去生成黄金票据

**4.制作令牌**<br/> 在当前的beacon上进行身份伪造

填入用户名，密码和Domain值来制作token

**5.one-liner**<br/> 为PowerShell one liner功能的会话。在beacon中承载一个运行有效负载的powershell脚本

powershell one-liner通常用于管理文件系统

选择监听器

随后会生成一段powershell命令，放到目标靶机上去运行，得到会话

在cobaltstrike通过beacon去运行powershell命令

得到了新的会话

**6.run mimikatz**<br/> 运行mimikatz,，会直接运行mimikatz得到结果

得到靶机的数据

**7.spawn As**<br/> 用于获取beacon后获取一个新的beacon，防止权限丢失，还可以和msf，empire等工具结合使用

填入信息，选择监听器

得到新的beacon

**目标**<br/> 对于目标操作<br/> cobaltstrike上有许多对于目标的操作方式

**浏览器代理**

<img alt="" height="222" src="https://img-blog.csdnimg.cn/direct/db5c4d62e5134af7ac5d042213c74cb2.png" width="651"/><br/> 配置好端口信息后点击开始，然后cobaltstrike就会开始注入dll到进程里，随后我们就可以把目标机器作为浏览器代理

**远程VNC**<br/> 可以直接与目标的桌面进行交互

1.刷新页面<br/> 2.仅查看<br/> 3.减小缩放<br/> 4.增大缩放<br/> 5.调整到适合的标签页<br/> 6.发送ctrl + Escape<br/> 7.锁定 Ctrl键<br/> 8.锁定 Alt键

**文件管理**<br/> 可以列出目标机器上的所有文件

upload

> 
用于上传文件


make directory

> 
用于创建文件夹


list drives

> 
用于显示盘符


refresh

> 
刷新当前目录


下载文件

> 
如果要下载文件的话，点击文件，右键dowload即可下载


复制文件

> 
如果要复制文件的话，点击文件，右键copy即可


执行文件

> 
点击文件，右键excute即可执行文件


删除文件

> 
点击文件，右键delete即可删除文件


net view

> 
用于查看目标所在域内的其他目标


(由于靶机没有设置域，故不作展示)

**端口扫描**

> 
用于扫描目标机器的端口，起到nmap的作用<img alt="" height="269" src="https://img-blog.csdnimg.cn/direct/8598dd32534c45428ef9088dfc3320df.png" width="510"/>


进程列表

> 
可以列出当前机器所有运行中的进程


<img alt="" height="408" src="https://img-blog.csdnimg.cn/direct/be39962b0c604680a9998d6511dcfa4b.png" width="903"/> 

**屏幕截图**

> 
直接点击屏幕截图，就可以获得目标机器当前屏幕画面


**中转**

中转分为3个部分

**SOCKES SERVER**<br/> SOCKES SERVER是cobaltstrike的内置sock，用于穿透目标机进入内网

运行成功

连接teamserver 的 36111端口即可进入内网

**Listener**

<img alt="" height="271" src="https://img-blog.csdnimg.cn/direct/8607403bce7546de86037af5c58cb30e.png" width="375"/><br/> 用于建立一个新的会话，将目标作为内网里其他beacon会话的中转器

设置好会话名称，选择相应的payload，再设定ip和端口，选择一个会话

**Deploy vpn client**<br/> 用于部署vpn连接

设置好MAC地址和端口，在channel处选择相应的通信协议

**增加会话**<br/> 在当前会话的基础上，再生成一个会话，增加对目标的控制

点击后，选择一个payload，选择后新增一个会话

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/df768d8b845b4feb95e5f8d71d387b12.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/26e8eb142014452490537fabb2a56d78.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/b035ed97f43e4202b4d030f3385457bd.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/92f121f9a6114bb0956841e6e510bf5d.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/25e843f9b600485ea2e516fde452666d.png" width="665"/>

应急响应笔记

学习路线
