# 原创
：  【kali-漏洞扫描】（2.1）Nessus解除IP限制、扫描快无结果、插件plugins被删除（中）

# 【kali-漏洞扫描】（2.1）Nessus解除IP限制、扫描快无结果、插件plugins被删除（中）

**目录**

[一、解除IP限制](#%E4%B8%80%E3%80%81%E8%A7%A3%E9%99%A4IP%E9%99%90%E5%88%B6)

[1.1、识别版本号](#1.1%E3%80%81%E8%AF%86%E5%88%AB%E7%89%88%E6%9C%AC%E5%8F%B7)

[1.2、修改配置文件](#1.2%E3%80%81%E4%BF%AE%E6%94%B9%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)

[1.3、重启服务](#1.3%E3%80%81%E9%87%8D%E5%90%AF%E6%9C%8D%E5%8A%A1)

[1.4、访问](#1.4%E3%80%81%E8%AE%BF%E9%97%AE)

[二、解决插件被删除](#%E4%BA%8C%E3%80%81%E8%A7%A3%E5%86%B3%E6%8F%92%E4%BB%B6%E8%A2%AB%E5%88%A0%E9%99%A4)

[2.1、分析](#2.1%E3%80%81%E5%88%86%E6%9E%90)

[ 2.2、方法一：](#%C2%A02.2%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A)

[2.3、方法二：](#2.2%E3%80%81%E9%85%8D%E7%BD%AE)

[三、扫描快无结果](#%E4%B8%89%E3%80%81%E6%89%AB%E6%8F%8F%E5%BF%AB%E6%97%A0%E7%BB%93%E6%9E%9C)

[3.1、分析](#3.1%E3%80%81%E5%88%86%E6%9E%90)

[3.2、恢复](#3.2%E3%80%81%E6%81%A2%E5%A4%8D)

---


## 一、解除IP限制

> 
<h3>1.1、识别版本号</h3>
在浏览器中输入
 [https://plugins.nessus.org/v2/plugins.php](https://plugins.nessus.org/v2/plugins.php)



> 
<h3>1.2、修改配置文件</h3>
修改 plugin_feed_info.inc 文件
sudo find /opt -name plugin_feed_info.inc 


看不见，就用root打开

<hr/>

如果是真的没有就新建一个plugin_feed_info.inc
并将内容改为
（有的话就替换原文件/opt/nessus/lib/nessus/plugin_feed_info.inc）
<pre><code>PLUGIN_SET = "202208020542";
PLUGIN_FEED = "ProfessionalFeed (Direct)";
PLUGIN_FEED_TRANSPORT = "Tenable Network Security Lightning";</code></pre>
<hr/>

将 /opt/nessus/lib/nessus/plugins/plugin_feed_info.inc 文件删除
（或者把这里面的也替换掉）
<pre>`rm -rf /opt/nessus/lib/nessus/plugins/plugin_feed_info.inc`</pre>


---


> 
<h3>1.3、重启服务</h3>
重启nessus服务
<pre>`sudo service nessusd restart`</pre>


> 
<h3>1.4、访问</h3>
浏览器访问nessus（https://localhost:8843）
等待nessus初始化插件
设置页面显示 unlimited,则解除IP限制


---


---


## 二、解决插件被删除

> 
<h3>2.1、分析</h3>
Nessus服务每次重启后，都会重置plugin_feed_info.inc，会使nessus/plugins目录下所有的插件都被删除，无法扫描


> 
<h3> 2.2、方法一：</h3>
每次都手动更新插件包
plugins文件内容可以再次更新插件获得（利用我们获得的那个插件包）




> 
<h3>2.3、方法二：</h3>
先停止nessus服务，将nessus服务设置为手动
<pre><code>sudo systemctl disable nessusd

sudo service nessusd stop</code></pre>
<hr/>
每次重置后都是一样的操作，重新配置
可以写成批处理
<pre>`sudo vim crack_nessus.sh`</pre>
<pre><code>service nessusd stop;
cp /root/plugin_feed_info.inc /opt/nessus/var/nessus/;
rm -rf /opt/nessus/lib/nessus/plugins/plugin_feed_info.inc;
service nessusd start;</code></pre>

<hr/>
将crack_nessus.sh写到系统启动的脚本里
每次重启，就会自动执行解除IP限制
<pre><code>sudo chmod +x /etc/rc.d/rc.local
sudo vim /etc/rc.d/rc.local</code></pre>
<hr/>
添加如下内容到rc.local
<pre>`/bin/bash /root/crack_nessus.sh`</pre>
nessus解除IP限制


---


---


---


## 三、扫描快无结果

> 
<h3>3.1、分析</h3>
新建扫描项目时，很快就结束，无扫描结果
查看plugins目录内容是否被删除
sudo du -h /opt/nessus/lib/nessus/plugins
一般查看文件大小


> 
<h3>3.2、恢复</h3>
使用备份（前提是备份好了plugins目录）
<pre><code>service nessusd stop;
rm -rf /opt/nessus/lib/nessus/plugins
cp -r ./plugins /opt/nessus/lib/nessus/
cp /root/plugin_feed_info.inc /opt/nessus/var/nessus/;
rm -rf /opt/nessus/lib/nessus/plugins/plugin_feed_info.inc;
service nessusd start;
</code></pre>
然后打开浏览器，访问nessus（https://localhost:8843）<br/> 等待更新完成

