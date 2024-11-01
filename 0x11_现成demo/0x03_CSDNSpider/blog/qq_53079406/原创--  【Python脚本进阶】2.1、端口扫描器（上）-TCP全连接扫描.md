# 原创
：  【Python脚本进阶】2.1、端口扫描器（上）：TCP全连接扫描

# 【Python脚本进阶】2.1、端口扫描器（上）：TCP全连接扫描

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、基础：](#1.1%E3%80%81%E5%9F%BA%E7%A1%80%EF%BC%9A)

[1.2、TCP：](#1.2%E3%80%81TCP%EF%BC%9A)

[二、TCP全连接扫描](#%E4%BA%8C%E3%80%81TCP%E5%85%A8%E8%BF%9E%E6%8E%A5%E6%89%AB%E6%8F%8F)

[2.1、简介：](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.2、函数：](#2.2%E3%80%81%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.3、实现：](#2.3%E3%80%81%E5%AE%9E%E7%8E%B0%EF%BC%9A)

[ 第一步：获得主机名和端口](#%C2%A0%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%BE%97%E4%B8%BB%E6%9C%BA%E5%90%8D%E5%92%8C%E7%AB%AF%E5%8F%A3)

[ 第二步： connScan和portScan函数](#%C2%A0%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%20connScan%E5%92%8CportScan%E5%87%BD%E6%95%B0)

[ 第三步：抓应用的Banner](#%C2%A0%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%8A%93%E5%BA%94%E7%94%A8%E7%9A%84Banner)

[ 第四步：线程扫描](#%C2%A0%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E7%BA%BF%E7%A8%8B%E6%89%AB%E6%8F%8F)

[ 第五步：加锁](#%C2%A0%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E5%8A%A0%E9%94%81)

[2.4、合体：](#2.4%E3%80%81%E5%90%88%E4%BD%93%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、基础：</h3>
扫描目标主机开放的TCP 端口的侦查脚本。当然， 为了与TCP 端口进行交互， 要建立TCP 套接字。
<hr/>
Python 也提供了访问BSD 套接字的接口。BSD 套接字提供了一个应用编程接口(API) ， 使程序员能编写在主机之间进行网络通信的应用程序。通过一系列的套接字API 函数， 我们可以创建、绑定、监听、连接， 或在TCP/IP 套接字上发送数据。在这一点上， 为了进一步开发我们自己的攻击程序， 必须对TCP/lP 套接字有一个更深入的了解。


> 
<h3>1.2、TCP：</h3>
大多数能访问互联网的应用使用的都是TCP 协议。例如， Web 服务器可能位于TCP 80 端口， 电子邮件服务器在TCP25 端口， FTP 服务器在TCP21 端口。要连接目标组织中的任一服务器， 攻击者必须知道与服务器相关联的IP 地址和TCP 端口。
<hr/>
网络攻击一般都是以端口扫描开始。有一种类型的端口扫描会向一系列常用的端口发送TCP SYN 数据包， 并等待TCP ACK 响应一一这能让我们确定这个端口是开放的。相反，TCP 连接扫描是使用完整的三次握手来确定服务器或端口是否可用的


---


---


## 二、TCP全连接扫描

> 
<h3>2.1、简介：</h3>
用TCP 全连接扫描来识别主机的TCP 端口的扫描器。
要导入Python 的BSD 套接字API 实现。套接字API 会为我们提供一些在实现TCP 端口扫描程序时有用的函数。要更深入地了解Python 标准库文档


> 
<h3>2.2、函数：</h3>
socket.gethostbyname(hostname)
此功能以主机名这样如www.syngress.com并返回IPv4地址格式69.163.177.2
<hr/>
socket.gethostbyaddr(ip address)
此功能采用IPv4地址并重新添加一个包含HOS名称的三倍，替代名称。主机名和同一接口的IPv4/V6地址列表在主机上。
<hr/>
socket.socket(\[family\[, type\[, proto]]])
此功能创建一个一个新socket的实例给定family。socket的选项family为af_inet，af_inet6或af_unix。此外，socket可以指定为tcp套接字或sock_dgram的sock_streamUDPsocket。最后，协议编号通常为零，并且在大多数情况下被省略。
<hr/>
socket.create_connection(address\[, timeout\[, source_address]])
这个功能采用2核（主机，端口），并返回一个实例网络socket。此外，它还可以选择超时和源地址。


---


### 2.3、实现：

> 
<h4> 第一步：获得主机名和端口</h4>
从用户那里获得主机名和端口。为了做到这一点， 我们在程序中使用optparse 库解析命令行参数。调用optparse.OptionPaser ([usage message]）会生成一个参数解析器(option parser) 类的实例。接着， 在parser.add_option 中指定这个脚本具体要解析哪个命令行参数。下面的例子显示了一个快速解析要扫描的目标主机名和端口的方法。

<pre><code>import optparse
parser = optparse.OptionParser('usage %prog - H' + '&lt;target host&gt; -p &lt;targe port&gt;')
parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort
if (tgtHost == None) | (tgtPort == None) :
    print(parser.usage)
    exit(0)</code></pre>



> 
<h4> 第二步： connScan和portScan函数</h4>
两个函数： connScan和portScan
portScan函数以参数的形式接收主机名和目标端口列表。它首先会尝试用gethostbyname()函数确定主机名对应的IP地址。
<hr/>
使用connScan函数输出主机名（或IP地址）， 并使用connScan(）函数尝试逐个连接我们要连接的每个端口。connScan 函数接收两个参数： tgtHost 和tgtPort, 它会去尝试建立与目标主机和端口的连接。如果成功， connScan将打印出一个端口开放的消息。如果不成功，它会打印出端口关闭的消息。

<pre><code>import optparse
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        print('[+] %d/tcp open' % tgtPort)
        connSkt.close()
    except:
        print('[-] %d/tcp closed' % tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve ' %s ':Unknown host' %tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: '+ tgtName[0])
    except:
        print('\n[+] Scan Results for: '+ tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('[+] Scanning port ' + tgtPort)
        connScan(tgtHost,int(tgtPort))</code></pre>



> 
<h4> 第三步：抓应用的Banner</h4>
为了抓取目标主机上应用的Banner, 先在connScan 函数中插入一些新增的代码。找到开放的端口后， 向它发送一个数据串并等待响应。跟进收集到的响应，推断出在目标主机和端口上运行的应用

<pre><code>import optparse
import socket
from socket import *


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send(bytes('ViolentPython\r\n',"utf8"))
        results = connSkt.recv(100)
        print('[+] %d/tcp open' % tgtPort)
        print( '[+] ' + str( results ) )
        connSkt.close()
    except:
        print('[-] %d/tcp closed' % tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve ' %s ':Unknown host' %tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: '+ tgtName[0])
    except:
        print('\n[+] Scan Results for: '+ tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + tgtPort)
        connScan(tgtHost,int(tgtPort))

def main():
    parser = optparse.OptionParser("usage%prog " + "-H &lt;target host&gt; -p &lt;target port&gt;")
    parser.add_option('-H', dest＝'tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split (', ')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print('[一] You must specify a target host and port[s].')
        exit(0)
    portScan(tgtHost,tgtPorts)



if __name__ == '__main__':
    main()</code></pre>



> 
<h4> 第四步：线程扫描</h4>
根据套接字中timeout变量的值， 每扫描一个套接字都会花费几秒钟。 但如果我们要扫描多个主机或端口， 时间总量就会成倍增加。同时扫描多个套接字进行扫描。必须引入Python线程， 线程是一种能提供这类同时执行多项任务的方法。具体到我们这个扫描器， 我们要修改的是portScan(）函数中迭代循环里的代码
<pre><code>for tgtPort in tgtPorts:
    t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
    t.start()</code></pre>


> 
<h4> 第五步：加锁</h4>
速度显著提升， 但connScanO函数在屏幕上打印一个输出。如果多个线程同时打印输出， 就可能会出现乱码和失序。
<hr/>
为了让一个函数获得完整的屏幕控制权， 需要使用一个信号量(semaphore)。一个简单的信号量就能阻止其他线程运行。注意， 在打印输出前， 我们用screenLock.acquire(）执行一个加锁操作。如果信号量还没被锁上， 线程就有权继续运行， 并输出打印到屏幕上。如果信号量已经被锁定， 只能等待， 直到持有信号量的线程释放信号量。通过利用信号量， 能够确保在任何给定的时间点上只有一个线程可以打印屏幕。在异常处理代码中， 位千fmally关键字前面的是在终止阻塞（其他线程）之前需要执行的代码
<pre><code>screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send(bytes('ViolentPython\r\n',"utf8"))
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+] %d/tcp open' % tgtPort)
        print( '[+] ' + str( results ) )
    except:
        screenLock.acquire()
        print('[-] %d/tcp closed' % tgtPort)
    finally:
        screenLock.release()
        connSkt.close()</code></pre>



> 
<h3>2.4、合体：</h3>
把所有的函数放入同一个脚本中， 并添加一些参数解析代码， 这就有了我们最终的端口扫描器脚本。
<pre><code>import optparse
import socket
from socket import *


screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send(bytes('ViolentPython\r\n',"utf8"))
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+] %d/tcp open' % tgtPort)
        print( '[+] ' + str( results ) )
    except:
        screenLock.acquire()
        print('[-] %d/tcp closed' % tgtPort)
    finally:
        screenLock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve ' %s ':Unknown host' %tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: '+ tgtName[0])
    except:
        print('\n[+] Scan Results for: '+ tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread( target=connScan, args=(tgtHost, int( tgtPort )) )
        t.start()


def main():
    parser = optparse.OptionParser("usage%prog " + "-H &lt;target host&gt; -p &lt;target port&gt;")
    parser.add_option('-H', dest＝'tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split (', ')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost,tgtPorts)


if __name__ == '__main__':
    main()</code></pre>




