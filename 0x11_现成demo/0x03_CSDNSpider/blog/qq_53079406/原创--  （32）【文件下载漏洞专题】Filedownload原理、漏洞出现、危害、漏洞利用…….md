# 原创
：  （32）【文件下载漏洞专题】Filedownload原理、漏洞出现、危害、漏洞利用……

# （32）【文件下载漏洞专题】Filedownload原理、漏洞出现、危害、漏洞利用……

**目录**

[一、前言：](#%E4%B8%80%E3%80%81%E5%89%8D%E8%A8%80%EF%BC%9A)

[二、简介：](#%E4%BA%8C%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[三、原理：](#%E4%B8%89%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[四、产生的原因：](#%E5%9B%9B%E3%80%81%E4%BA%A7%E7%94%9F%E7%9A%84%E5%8E%9F%E5%9B%A0%EF%BC%9A)

[五、漏洞出现地方：](#%E4%BA%94%E3%80%81%E6%BC%8F%E6%B4%9E%E5%87%BA%E7%8E%B0%E5%9C%B0%E6%96%B9%EF%BC%9A)

[5.1、功能上出现：](#5.1%E3%80%81%E5%8A%9F%E8%83%BD%E4%B8%8A%E5%87%BA%E7%8E%B0%EF%BC%9A)

[5.2、链接上出现：](#5.2%E3%80%81%E9%93%BE%E6%8E%A5%E4%B8%8A%E5%87%BA%E7%8E%B0%EF%BC%9A)

[5.3、参数上出现爱：](#5.3%E3%80%81%E5%8F%82%E6%95%B0%E4%B8%8A%E5%87%BA%E7%8E%B0%E7%88%B1%EF%BC%9A)

[六、危害：](#%E5%85%AD%E3%80%81%E5%8D%B1%E5%AE%B3%EF%BC%9A)

[七、相关漏洞：](#%E4%B8%83%E3%80%81%E7%9B%B8%E5%85%B3%E6%BC%8F%E6%B4%9E%EF%BC%9A)

[八、系统文件路径](#%E5%85%AB%E3%80%81%E7%B3%BB%E7%BB%9F%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84)

[8.1、Linux：](#5.1%E3%80%81Linux%EF%BC%9A)

[8.2、Windows：](#5.3%E3%80%81Windows%EF%BC%9A)

[8.3、TomCat：](#5.2%E3%80%81TomCat%EF%BC%9A)

[九、漏洞利用：](#%E4%B9%9D%E3%80%81%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%EF%BC%9A)

[9.1、目的：](#9.1%E3%80%81%E7%9B%AE%E7%9A%84%EF%BC%9A)

[9.2、pikachu（Filedownload）](#9.2%E3%80%81pikachu%EF%BC%88Filedownload%EF%BC%89)

[9.2.1、第一步：点击链接修改参数](#9.2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E7%82%B9%E5%87%BB%E9%93%BE%E6%8E%A5%E4%BF%AE%E6%94%B9%E5%8F%82%E6%95%B0)

[9.2.1、第二步：分析](#9.2.1%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90)

---


（当你足够强大才能俯瞰一切） 

## 一、前言：

> 
文件下载漏洞，最终目的还是为了进一步获得更多的信息
即信息收集


---


## 二、简介：

> 
我们在浏览器上下载软件的许多网站（根据网站具体用途存在下载功能），都是具备文件下载功能的，功能的实现是通过对参数filename的值的对应，获取在服务器上所需下载的文件的绝对路径，然后读取文件内容并发送给客户端进行下载

换一个角度想的话，如果知道了文件所代表的变量，然后一个一个爆破，是不是就有可能获得一些敏感信息。即如果这些有下载功能的网站对用户查看或下载的文件没有做出限制的话，用户就可能下载到一些敏感文件（文件下载漏洞）


---


## 三、原理：

> 
文件下载漏洞，顾名思义，就是对前端用户的下载请求，没有对其所请求的文件类型、目录做合理严谨的规则进行过滤，导致用户通过路径回溯符…/等相关操作，跳出了程序本身的限制目录，然后再利用文件下载功能，使前端下载请求可以下载服务器中的任意文件。


---


## 四、产生的原因：

> 
给用户提供了一个下载的功能，并能接收相关的参数变量
开发时候，使用了读去文件的相关函数
对前端用户读取文件请求，没有进行相应的控制或控制不严（限制、校验）
能输出请求文件的内容，提供给前端下载


---


## 五、漏洞出现地方：

（找到地方后1，一遍会尝试下载多个，然后分析URL中的参数变量，但是一般要先解码）

### 5.1、功能上出现：

> 
一般可以根据下载功能去找，一些明显的软件下载网站等


### 5.2、链接上出现：

> 
download.php?path=<br/> download.php?file=<br/> down.php?file=<br/> data.php?file=<br/> readfile.php?file=<br/> read.php?filename=<br/> （前人总结，后人乘凉）


### 5.3、参数上出现爱：

> 
&amp;RealPath=<br/> &amp;FilePath=<br/> &amp;ﬁlepath=<br/> &amp;Filepath=<br/> &amp;Path=<br/> &amp;path=<br/> &amp;inputFile=<br/> &amp;Inputfile=<br/> &amp;url=<br/> &amp;urls=<br/> &amp;Lang=<br/> &amp;dis=<br/> &amp;data=<br/> &amp;Data=<br/> &amp;readﬁle=<br/> &amp;ﬁlep=<br/> &amp;src=<br/> &amp;menu=<br/> META-INF<br/> WEB-INF
（前人总结，后人乘凉）


---


## 六、危害：

> 
可以下载服务器的任意文件：
eg：
获得网站web源码，再对代码进行审计，以获得更多的漏洞
获得网站、服务器、系统、数据库等中间件配置文件
获得应用于系统配置文件
对内网的信息进行一个探测
下载各种.log文件，并寻找后台地址、文件上传点等地方


---


## 七、相关漏洞：

> 
参数后面所接的不一样，可能出现的漏洞不一样
但是漏洞之间都是可以你帮我，我帮你，哈哈（看改为思维理解）
eg：
文件被解析执行了，可能存在文件包含漏洞
文件源代码被显示，可能存在文件查看读取漏洞
提示文件进行下载，可能存在文件下载漏洞


---


## 八、系统文件路径

### 8.1、Linux：

> 
/etc/passwd
        //保存了系统中所有的用户信息
/etc/shadow
        //用户的密码信息
/root/.ssh/authorized_keys
        //公钥文件
/root/.bash_history
        //用户终端操作历史记录
/usr/local/app/apache2/conf/httpd.conf
        //apache2默认配置文件
/usr/local/app/apache2/conf/extra/httpd-vhosts.conf
        //虚拟网站设置
/usr/local/app/php5/lib/php.ini
        //php相关设置
/etc/httpd/conf/httpd.conf
        //apache
/etc/php5/apache2/php.ini
        //ubuntu系统的默认路径


### 8.2、Windows：

> 
C:\boot.ini
        //查看系统版本
C:\windows\system32\inetsrv\MetaBase.xml
        //查看IIS虚拟主机配置文件
C:\windows\repair\sam
        //存储Windows系统初次安装的密码
C:\Program Files\mysql\my.ini
        //mysql配置，记录管理员登陆过的MYSQL用户名和密码
C:\Program Files\mysql\data\mysql\user.MYD
        //mysql.user表中的数据库连接密码
C:\windows\php.ini php.ini
        //php配置文件
C:\Windows\system.in
        //winnt的php配置信息
C:\Windows\win.ini
        //winnt的mysql配置文件
C:\Program Files\RhinoSoft.com\Serv-U\ServUDaemon.ini
        //存储虚拟主机网站路径和密码
C:\Program Files\Apache Group\Apache\conf\httpd.conf 或C:\apache\conf\httpd.conf
        //查看WINDOWS系统apache文件
C:/Resin-3.0.14/conf/resin.conf
        //查看jsp开发的网站resin文件配置信息.
C:\Windows\System32\drivers\etc\hostswinserver
        //配置Telnet信息


### 8.3、TomCat：

> 
apache-tomcat-8.5.51/conf/tomcat-users.xml
        //tomcat的角色(授权用户)配置文件
apache-tomcat-8.5.51/conf/server.xml 
        //tomcat的主配置文件
apache-tomcat-8.5.51/conf/web.xml
        //tomcat应用程序的部署描述符文件
apache-tomcat-8.5.51/logs/catalina.out
         //即tomcat的标准输出和标准出错，所有输出到这两个位置的都会进入catalina.out，这里包含tomcat运行自己输出的日志以及应用里向console输出的日志。


---


## 九、漏洞利用：

### 9.1、目的：

> 
咱就说，危害即我们对漏洞的利用，就是要去霍霍：)
文件下载漏洞利用主要为了进一步的信息收集
eg：
获得网站web源码，再对代码进行审计，以获得更多的漏洞
获得网站、服务器、系统、数据库等中间件配置文件
获得应用于系统配置文件
对内网的信息进行一个探测
下载各种.log文件，并寻找后台地址、文件上传点等地方


### 9.2、pikachu（Filedownload）

> 
<h4>9.2.1、第一步：点击链接修改参数</h4>
先打开burpsuite代理拦截
burpsuite问题解决：
[【burpsuite抓包问题合集】【六种解决方法】第一种：连接配置问题，拦截不到任何包；第二种：设置问题，抓不到部分包](https://blog.csdn.net/qq_53079406/article/details/124068136?spm=1001.2014.3001.5501)






放包以后，就下载了kb了 


<h4>9.2.1、第二步：分析</h4>
真正运用的时候，可能就要把路径先扫出来了
burpsuite也有扫描功能，但是它的scan可能不是最强的




#### 9.2.1、第二步：分析
