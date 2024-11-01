# 原创
：  【Python脚本进阶】1.2、python脚本基础知识（上）

# 【Python脚本进阶】1.2、python脚本基础知识（上）

**目录**

[一、基础](#%E4%B8%80%E3%80%81%E5%9F%BA%E7%A1%80)

[1.1、解释](#1.1%E3%80%81%E8%A7%A3%E9%87%8A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[1.2、交互](#1.2%E3%80%81%E4%BA%A4%E4%BA%92)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[二、Python语言](#%E4%BA%8C%E3%80%81Python%E8%AF%AD%E8%A8%80)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、变量：](#1.2%E3%80%81%E5%8F%98%E9%87%8F%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[1.3、字符串：](#1.3%E3%80%81%E5%AD%97%E7%AC%A6%E4%B8%B2%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[1.4、列表](#1.4%E3%80%81%E5%88%97%E8%A1%A8)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[1.5、词典](#1.5%E3%80%81%E8%AF%8D%E5%85%B8)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[1.6、网络：](#1.6%E3%80%81%E7%BD%91%E7%BB%9C%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[1.7、条件选择语句](#1.7%E3%80%81%E6%9D%A1%E4%BB%B6%E9%80%89%E6%8B%A9%E8%AF%AD%E5%8F%A5)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


(我所用为python3+pycharm)

## 一、基础

> 
<h3>1.1、解释</h3>
<h4>简介：</h4>
顾名思义，带.py的输入进去，把内容给运行了
<hr/>
<h4>示例：</h4>



#### 示例：

> 
<h3>1.2、交互</h3>
<h4>简介：</h4>
调用Python解释器并直接与之交互，输入python命令即可

<hr/>
<h4>示例：</h4>
＞＞＞提示符，即正在使用交互式解释器



#### 示例：

---


---


## 二、Python语言

> 
<h3>1.1、简介：</h3>
变量、数据类型、字符串、复杂的数据结构、网络、条件选择语句、迭代、文件处理、异常处理， 以及与操作系统的交互操作等概念


> 
<h3>1.2、变量：</h3>
<h4>简介：</h4>
变量是指存储在某个内存地址上的数据。这个内存地址可以存储不同的值， 如整型数、实数、布尔值、字符串， 或是列表(list)或词典这类更复杂的数据
<hr/>
<h4>示例：</h4>
1、整型数的变量a，字符串的变量b，把两个变量合并成一个字符串，先用str(）函数把变量a转换成一个字符串



2、声明一个字符串、整型数、列表或布尔值， 而解释器正确地自动确定每个变量的类型



#### 示例：

 

> 
<h3>1.3、字符串：</h3>
<h4>简介：</h4>
非常强大的处理字符串的方法（可参考官方文档）
<hr/>
<h4>示例：</h4>
upper()是将字符串转成大写形式
lower()是将字符串转成小写形式
replace(old,new)是用new子串取代old子串
find(）返回子串在字符串中第一次出现时的偏移量。




#### 示例：

> 
<h3>1.4、列表</h3>
<h4>简介：</h4>
list（列表）还内置了执行添加、插入、删除、出站、索引、计数、排序、反转等操作的方法
第一个是从0开始排序的
<hr/>
<h4>示例：</h4>
创建表：list=['a','aa',2]
删除元素：del来删除，del list[nmu]
访问表值：list2[1:5]
比较两个列表的元素：cmp(list1, list2)
列表元素个数：len(list)
返回列表元素最大值：max(list)
返回列表元素最小值：min(list)
将元组转换为列表：list(seq)
……


#### 示例：

> 
<h3>1.5、词典</h3>
<h4>简介：</h4>
词典由n对键和值的项组成，创建词典时， 每个键和它的值都是以冒号分隔的， 同时用逗号分隔各个项。用途广泛，如创建了一个相关的词典， 查找FTP之类的关键字， 就返回与之关联的端口值21
<hr/>
<h4>示例：</h4>
.keys()：返回的是词典中所有键的列表
.items()：返回的是词典中所有项的完整信息的列表
services = {'ftp':21,'ssh':22,'smtp':25,'http':80}
services.keys()
services.items()



#### 示例：

> 
<h3>1.6、网络：</h3>
<h4>简介：</h4>
socket 模块提供了一个用Python 进行网络连接的库。
<hr/>
<h4>示例：</h4>
编写一个抓取banner 的(banner-grabbing) 脚本，会在连上指定的IP 地址和TCP 端口后， 将banner 打印出来。
1、导入socket 模块之后
2、实例化一个socket 类的新变量s。
3、用connect()方法建立与指定IP 地址和端口的网络连接，连接成功， 就可以通过套接字进行读／写操作。
4、recv(l024)方法将读取套接字中接下来的1024B 数据
5、把该方法的返回结果放在一个变量中， 并把这个来自服务器的响应结果打印出来
<hr/>
import socket<br/> socket.setdefaulttimeout(2)<br/> s = socket. socket ()<br/> s.connect (("192.168. 190.131", 21))<br/> ans = s.recv(1024)<br/> print(ans）
<hr/>
发现Linux没有开什么端口


 在Windows中找了一个端口


 就返回一个b''
不理解
再准备连其他的，返现确实是连接上了，所有报错了




#### 示例：

---


> 
<h3>1.7、条件选择语句</h3>
<h4>简介：</h4>
IF 语句是对逻辑表达式进行求值， 并根据求值结果做出决定
if 判断条件1:
        执行语句1……
elif 判断条件2:
        执行语句2……
……
else:
        执行语句4……
<hr/>
<h4>示例：</h4>
想要知道某个指定的FTP 服务器中是否存在可以攻击的漏洞。这就需要将服务器的响应结果与一些已知存在漏洞的FTP 服务器版本（的banner) 进行比较   
 <pre><code>import socket
socket.setdefaulttimeout(2)
s = socket. socket ()
s.connect (("192.168. 190.131", 21))
ans = s.recv(1024)
print(ans）

if "FreeFloat Ftp Server (Version 1.00)" in ans:
    print(" FreeFloat FTP Server is vulnerable.")
elif "3Com 3CDaemon FTP Server Version 2.0" in ans:
    print(" FreeFloat FTP Server is vulnerable.")
elif "Ability Server 2.34" in banner:
    print(" FreeFloat FTP Server is vulnerable.")
elif "Sami FTP Server 2.0.2" in ans:
    print(" FreeFloat FTP Server is vulnerable.")
else:
    print("FTP Server is not vulnerable.")</code></pre>



#### 示例：
