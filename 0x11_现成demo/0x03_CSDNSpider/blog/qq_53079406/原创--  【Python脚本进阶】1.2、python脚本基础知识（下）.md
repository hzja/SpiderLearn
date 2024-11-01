# 原创
：  【Python脚本进阶】1.2、python脚本基础知识（下）

# 【Python脚本进阶】1.2、python脚本基础知识（下）

**目录**

[一、文件输入/输出](#%E4%B8%80%E3%80%81%E6%96%87%E4%BB%B6%E8%BE%93%E5%85%A5%2F%E8%BE%93%E5%87%BA)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[二、sys模块](#%E4%BA%8C%E3%80%81sys%E6%A8%A1%E5%9D%97)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[三、OS模块](#%E4%B8%89%E3%80%81OS%E6%A8%A1%E5%9D%97)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[四、漏扫脚本](#%E5%9B%9B%E3%80%81%E6%BC%8F%E6%89%AB%E8%84%9A%E6%9C%AC)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


(我所用为python3+pycharm)

## 一、文件输入/输出

> 
<h3>简介：</h3>
假设有一个名为vuln_ b anners.txt 文本文件， 这个文件的每一行都列出了一个已知有漏洞的特定服务版本（的banner) 。
通过读取这个文本文件， 来判断banner 是否有漏洞的服务器，避免使用一大堆if语句去判断。


> 
<h3>示例：</h3>
<blockquote>
cat vuln_banners.txt<br/> 3Com 3CDaemon FTP Server Version 2.0<br/> Ability Server 2.34<br/> CCProxy Telnet Service Ready<br/> ESMTP TABS Mail Server for Windows NT<br/> FreeFloat Ftp Server (Version 1.00)<br/> IMAP4revl MDaemon 9.6.4 ready<br/> MailEnable Service, Version: 0-1.54<br/> NetDecision-HTTP-Server 1.0<br/> PSO Proxy 0.9<br/> SAMBAR<br/> Sami FTP Server 2.0.2<br/> Spipe 1.0<br/> TelSrv 1.5<br/> WDaemon 6.8.5<br/> WinGate 6.1.1<br/> Xitami<br/> YahooPOPs! Simple Mail Transfer Service Ready


---


在checkVulns函数中换上了新的代码。这里以只读模式('r')打开文本文件，用.readlinesO方法遍历文件中的每一行， 并将其与我们的banner做比较。

注： 必须用.strip('\r')方法去掉每一行的回车键。检测到匹配， 打印一个有漏洞的服务器的banner

```
def checkVulns(banner):
    f = open("vuln_banners.txt", 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print('Server is vulnerable: '+banner.strip('\n'))
```

---


---


## 二、sys模块

> 
<h3>简介：</h3>
内置的sys模块使我们能访问到由Python 解释器使用或维护的对象， 其中包括标志、版本、整型数的最大尺寸、可用的模块、hook路径、标准错误／输入／输出的位置， 以及调用解释器的命令行参数


> 
<h3>示例：</h3>
把一个文本文件的文件名作为命令行参数传递sys.argv 列表中含有所有的命令行参数
第一个sys.argv[0]元素中的是Python 脚本的名称
列表中的其余元素中则记录了之后所有的命令行参数
如果我们只是传递一个额外的参数， sys.argv 中应该包含两个元素（脚本名称、传入的参数）
<pre><code>import sys

if len(sys.argv) != 2:
    filename = sys.argv[1]
    print('Reading Vulnerabilities From: ' + filename)</code></pre>


---


---


## 三、OS模块

> 
<h3>简介：</h3>
内置的OS 模块提供了丰富的适用于Mac、NT 或Posix 的操作系统的函数。这个模块允许程序独立地与操作系统环境、文件系统、用户数据库以及权限进行交互


> 
<h3>示例：</h3>
用户把一个文本文件的文件名作为命令行参数传递进来， 先检查一下该文件是否存在、当前用户是否有权限读取该文件，其中任一条件不满足， 就向用户显示一条相应的错误信息
<pre><code>import sys
import os

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(filename + ' does not exist.')
        exit(0)
    if not os.access(filename, os.R_OK):
        print(filename + ' access denied.')
        exit(0)
    print('Reading Vulnerabilities From: ' + filename)</code></pre>


---


---


## 四、漏扫脚本

> 
<h3>示例：</h3>
重新整合上面学过的这些重新整合一下Python 漏洞扫描脚本的各个部分
<pre><code>import socket
import sys
import os

def retbanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv (1024)
        return banner
    except Exception as e:
        return e


def checkVulns(banner,filename):
    f = open(filename,'r')
    for line in f.readlines():
        if line.strip ('\n') in banner:
            print('Server is vulnerable: ' + banner.strip ('\n'))


def main():
if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(filename + ' does not exist.')
        exit(0)
    if not os.access(filename, os.R_OK):
        print(filename + ' access denied.')
        exit(0)
    else:
        print('Usage: ' + str(sys.argv[0]) + ' &lt;vuln filename&gt;')
        exit(0)
        portList = [21, 22, 25, 80, 110, 443]
        for x in range(147, 150 ):
            ip = '192.168.190.' + str( x )
            for port in portList:
                banner = retbanner(ip,port )
                if banner:
                    print(ip + str(banner))
                    checkVulns(banner, filename)

if __name__ == '__main__':
    main()</code></pre>

