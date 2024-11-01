# 原创
：  【Python脚本进阶】1.2、python脚本基础知识（中）

# 【Python脚本进阶】1.2、python脚本基础知识（中）

**目录**

[一、异常处理](#%E4%B8%80%E3%80%81%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、示例：](#1.2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[二、函数：](#%E4%BA%8C%E3%80%81%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.1、简介：](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.2、示例1：](#2.2%E3%80%81%E7%A4%BA%E4%BE%8B1%EF%BC%9A)

[2.3、示例2：](#2.3%E3%80%81%E7%A4%BA%E4%BE%8B2%EF%BC%9A)

[三、迭代](#%E8%BF%AD%E4%BB%A3)

[3.1、简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[3.2、示例1：](#%E7%A4%BA%E4%BE%8B1%EF%BC%9A)

[3.3、示例2：](#%E7%A4%BA%E4%BE%8B2%EF%BC%9A)

[3.4、示例3：](#%E7%A4%BA%E4%BE%8B3%EF%BC%9A)

[3.5、示例4：](#%C2%A0%E7%A4%BA%E4%BE%8B4%EF%BC%9A)

---


(我所用为python3+pycharm)

## 一、异常处理

> 
<h3>1.1、简介：</h3>
1、编写的程序语法完全正确， 在程序运行或执行时仍可能出错（最典型的就是除零错，因为0 不能作为除数， Python 解释器会显示该错误，并会终止程序的执行）
2、在正在运行的程序或脚本的上下文环境中处理错误：异常处理功能
try/except语句进行异常处理。当错误发生时， 异常处理捕获这一错误并在屏幕上打印一条消息
3、为了获取错误的确切信息，把异常存储到变量e中， 以便将其打印出来， 同时还要将变量e转换成一个字符串
<hr/>
try:
        print(''100/0 = "+str(100/0))
except Exception as e:
        print("Error = "+str(e))

注(版本兼容问题)：
python2：except Exception,e:
python3：except Exception as e:


> 
<h3>1.2、示例：</h3>
用异常处理来更新抓取banner 的脚本。把网络连接代码写在try 语句块中， 尝试连接到一台没有在TCP 端口21 上运行FTP 服务的机器。 就会看到一条报错的消息

import socket
socket.setdefaulttimeout(2)
s=socket.socket()
try:
        s.connect(('192.168.190.131',21))
except Exception as e:
        print('Error='+str(e))




---


---


## 二、函数：

> 
<h3>2.1、简介：</h3>
函数提供了高效的可重用代码块，python自带许多内置函数， 也可以创建定义的函数
关键字def(）表示函数开始，并且可以在括号内填写任何变量，这些变量会被以引用的方式传递给函数


> 
<h3>2.2、示例1：</h3>
创建一个函数来完成连接到FTP 服务器并返回banner的操作
(我直接使用pycharm运行的，节省调试时间)
<pre><code>import socket


def retbanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return e


def main():
    ip1 = '127.0.0.1'
    ip2 = '192.168.190.131'
    port = 8080
    banner1 = retbanner(ip1, port)
    if banner1:
        print(ip1 + ': ' + str(banner1))
    banner2 = retbanner(ip2, port)
    if banner2:
        print(ip2 + ': ' + str(banner2))


if __name__ == '__main__':
    main()</code></pre>



> 
<h3>2.3、示例2：</h3>
banner返回后， 我们的脚本需要把它们和一些已知有漏洞的程序（的banner)进行比较
checkVulns(）函数接收参数banner变量， 并以此来判断服务器中是否存在漏洞
<pre><code>import socket


def retbanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return e


def checkVulns(banner):
    if "FreeFloat Ftp Server (Version 1.00)" in banner:
        print(" FreeFloat FTP Server is vulnerable.")
    elif "3Com 3CDaemon FTP Server Version 2.0" in banner:
        print(" FreeFloat FTP Server is vulnerable.")
    elif "Ability Server 2.34" in banner:
        print(" FreeFloat FTP Server is vulnerable.")
    elif "Sami FTP Server 2.0.2" in banner:
        print(" FreeFloat FTP Server is vulnerable.")
    else:
        print("FTP Server is not vulnerable.")
    return


def main():
    ip1 = '127.0.0.1'
    ip2 = '192.168.190.131'
    port = 8080
    banner1 = retbanner(ip1, port)
    if banner1:
        print(ip1 + ': ' + str(banner1).strip('\n'))
        checkVulns(banner1)
    banner2 = retbanner(ip2, port)
    if banner2:
        print(ip2 + ': ' + str(banner2).strip('\n'))
        checkVulns(banner2)


if __name__ == '__main__':
    main()</code></pre>


---


---


## 三、迭代

> 
<h3>3.1、简介：</h3>
检查三个不同的IP地址，与写三次相同的程序相比， 用for循环遍历多个元素可能更容易


> 
<h3>3.2、示例1：</h3>
如果想遍历IP地址从192.168.95.1到192.168.95.254的整个/24子网， 使用for循环（范围从1<br/> 到255)可以打印出整个子网
<pre><code>for x in range(1,255):
    print("192.168.95."+str(x))</code></pre>
（range还可设置每个间距）



> 
<h3>3.3、示例2：</h3>
遍历所有已知端口列表的方式检查漏洞， 只需遍历某个list中的所有元素即可， 无须遍历某个范围内的所有数字
<pre><code>portList = [21, 22, 25, 80, 110]
for port in portList:
    print(port)</code></pre>



> 
<h3>3.4、示例3：</h3>
通过嵌套两个for循环， 我们可以打印出每个IP地址上的每个端口

<pre><code>portList = [21, 22, 25, 80, 110]
for port in portList:
    print(port)

for x in range(1, 255):
    for port in portList:
        print('Checking 192.168.190.' + str(x) + ': ' + str(port))</code></pre>



> 
<h3>3.5、示例4：</h3>
利用迭代IP 地址和端口， 更新漏洞检查脚本。现在， 脚本将测试192.168.190.0/24子网上的所有254个IP地址， 测试的端口包括telnet 、SSH、SMTP、HTTP、IMAP及HTTPS协议的端口
<pre><code>import socket


def retbanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return e


def checkVulns(banner):
    if "FreeFloat Ftp Server (Version 1.00)" in banner:
        print(" FreeFloat FTP Server is vulnerable.")
    elif "3Com 3CDaemon FTP Server Version 2.0" in banner:
        print(" FreeFloat FTP Server is vulnerable.")
    elif "Ability Server 2.34" in banner:
        print(" FreeFloat FTP Server is vulnerable.")
    elif "Sami FTP Server 2.0.2" in banner:
        print(" FreeFloat FTP Server is vulnerable.")
    else:
        print("FTP Server is not vulnerable.")
    return


def main():
    portList = [21, 22, 25, 80, 110, 443]
    for x in range(1,255):
        ip = '192.168.190.' + str(x)
        for port in portList:
            banner = retbanner(ip, port)
            if banner:
                print(ip + ': ' + str(banner))
                checkVulns(banner)


if __name__ == '__main__':
    main()</code></pre>

