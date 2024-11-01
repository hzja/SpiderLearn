# 原创
：  【Python脚本进阶】2.1、端口扫描器（下）：NMAP端口扫描

# 【Python脚本进阶】2.1、端口扫描器（下）：NMAP端口扫描

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、扩展](#1.1%E3%80%81%E6%89%A9%E5%B1%95)

[1.2、端口扫描类型](#1.2%E3%80%81%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F%E7%B1%BB%E5%9E%8B)

[ 1.3、实现：](#%C2%A01.3%E3%80%81%E5%AE%9E%E7%8E%B0%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、扩展</h3>
由TCP连接扫描脚本，到其他类型的扫描，Nmap端口扫描工具包提供了大量的功能，如提供的ACK、RST、FIN或SYN-ACK 扫描等。
<hr/>
Nmap中也能使用C和Lua编写的脚本， 但是Nmap还能被非常好地整合到Python 中。Nmap可以生成基于XML的输出。Python库能够解析这类基于XML的输出。能在Python 脚本中使用Nmap的全部功能。必须安装Python - Nmap[python-nmap : nmap from python (xael.org)<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://xael.org/pages/python-nmap-en.html](https://xael.org/pages/python-nmap-en.html)安装时请注意对Python 3.x和Python 2.x不同版本的注意事项提醒


> 
<h3>1.2、端口扫描类型</h3>
TCP SYN SCAN一一半开放扫描， 这种类型的扫描发送一个SYN包， 启动一个TCP会话，并等待响应的数据包。如果收到的是一个reset 包， 表明端口是关闭的， 而如果收到的是一个SYN / ACK包， 则表示相应的端口是打开的
<hr/>
TCP NULLS CAN——NULL扫描，把TCP头中的所有标志位都设为NULL。 如果收到的是一个RST包， 则表示相应的端口是关闭的
<hr/>
TCP FIN SCAN——TCP FIN 扫描发送一个表示拆除一个活动的TCP 连接的FIN包， 让对方关闭连接。如果收到了一个RST包， 则表示相应的端口是关闭的
<hr/>
TCP XMAS SCAN——TCP XMAS 扫描发送PSH、FIN、URG和TCP标志位被设为1的数据包。如果收到了一个RST包， 则表示相应的端口是关闭的


---


> 
<h3> 1.3、实现：</h3>
安装Python-Nmap后，就可以将Nmap导入到现有的脚本中，并在Python脚本中直接使用Nrnap扫描功能。
创建一个PortScanner()类对象，用这个对象完成扫描操作。PortScanner类有一个scan()函数， 它可将目标和端口的列表作为参数输入， 并对它们进行基本的Nmap 扫描。还可以把目标主机的地址／端口放入数组中备查， 并打印出端口的状态。依靠该功能来定位和识别目标。

<pre><code>import mmap
import optparse


def nmapScan(tgtHost,tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan( tgtHost, tgtPort )
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print(" [*] "+tgtHost + " tcp/ " +tgtPort +" "+state)



def main():
    parser = optparse.OptionParser("usage%prog " + "-H &lt;target host&gt; -p &lt;target port&gt;")
    parser.add_option('-H', dest＝'tgtHost', type='string',help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',help='specify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split (', ')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    for tgtPort in tgtPorts:
        nmapScan( tgtHost, tgtPort )


if __name__ == '__main__':
    main()</code></pre>
像Nmap这样功能齐全的扫描器， 能够发现过滤器， 而单一的TCP连接扫描是不行的


