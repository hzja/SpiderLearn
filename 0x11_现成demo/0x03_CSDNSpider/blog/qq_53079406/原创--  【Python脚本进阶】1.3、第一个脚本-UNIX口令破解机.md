# 原创
：  【Python脚本进阶】1.3、第一个脚本：UNIX口令破解机

# 【Python脚本进阶】1.3、第一个脚本：UNIX口令破解机

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[1.2、crypt：](#1.2%E3%80%81crypt%EF%BC%9A)

[二、示例：](#%E4%BA%8C%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[2.1、示例1：](#2.1%E3%80%81%E7%A4%BA%E4%BE%8B1%EF%BC%9A)

[2.2、示例2：](#2.2%E3%80%81%E7%A4%BA%E4%BE%8B2%EF%BC%9A)

[思路：](#%E6%80%9D%E8%B7%AF%EF%BC%9A)

[main()函数](#main%28%29%E5%87%BD%E6%95%B0)

[testPass()函数](#testPass%28%29%E5%87%BD%E6%95%B0)

[2.3、注：](#2.3%E3%80%81%E6%B3%A8%EF%BC%9A)

[split()：](#split%28%29%EF%BC%9A)

[2.4、总结：](#2.4%E3%80%81%E6%80%BB%E7%BB%93%EF%BC%9A)

---


## 一、简介：

> 
<h3>1.1、概述：</h3>
编写UNIX口令破解机时，需使用UNIX计算口令hash的crypt()算法
The crypt module is not supported on Windows（Windows不支持crypt模块）


> 
<h3>1.2、crypt：</h3>
crypt.crypt(word, salt=None)
验证 Unix 口令的函数
<hr/>
启动Python 解释器，Python 标准库中已自带有crypt 库。要计算一个加密的UNIX 口令hash, 只需调用函数crypt.crypt()， 并将口令和salt作为参数传递给它。该函数会以字符串形式返回口令的hash




---


---


## 二、示例：

> 
<h3>2.1、示例1：</h3>
明文是单词egg 和salt 就是开头的两个字节是HX
使用crypt(）函数快速计算口令的hash。将库导入之后， 我们将口令“ egg" 与salt"HX"传递给函数。该函数返回口令的hash一一字符串为“ HX9LLTdc/jiDE" 。
<pre><code>&gt;&gt;&gt; import crypt
&gt;&gt;&gt; crypt.crypt("egg","HX")
'HX9LLTdc/jiDE'</code></pre>




> 
<h3>2.2、示例2：</h3>
<h4>思路：</h4>
可以编写一个程序来遍历整个字典， 将每一个单词加上指定的salt 的计算结果都与加密的口令hash 做比较
首先要创建两个函数： main 和testpass。根据各自特定的作用， 将程序分隔成相互独立的函数，便于重用代码，易于阅读。
<hr/>
<h4>main()函数</h4>
用main 函数打开加密口令文件” password.txt", 并逐行读取口令文件中的内容。每一行中的用户名和口令hash 都是分隔开的。对每个口令hash, main 函数都调用testPass()函数， 尝试用字典中的单词破解它。
<hr/>
<h4>testPass()函数</h4>
testPass()函数会以参数形式获得加密的口令hash, 并在找到密码或搜遍字典无果后返回。要注意的是， 该函数首先将加密的口令hash 的前两个字符视为salt, 并提取出来。然后， 它打开字典并遍历字典中的每个单词， 用每个单词和salt 计算一个新的加密口令hash。
如果计算结果与我们加密口令hash 匹配， 函数会打印一条消息显示找到密码， 并返回。否<br/> 则， 它会在词库中继续对每个单词进行测试。
<pre><code>import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
dictFile = open ('dictionary.txt', 'r')
for word in dictFile.readlines():
        word = word.strip( '\n' )
        cryptWord = crypt.crypt(word, salt)
        if cryptWord==cryptPass:
            print("Found Password: " + word + "\n")
        print("Password Not Found.\n")
        



def main():
    passFile = open('passwords. txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("Cracking Password For: " + user)
            testPass(cryptPass)

if __name__ == '__main__':
    main()</code></pre>




#### main()函数

---


> 
<h3>2.3、注：</h3>
<h4>split()：</h4>
**简介：**
通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
**语法：**
str.split(str="", num=string.count(str)).
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。
返回分割后的字符串列表。



> 
<h2>2.4、总结：</h2>
(root) 一般是使用了我们字典之外的作为口令
<hr/>
基于＊Nix 的现代操作系统中，／etc/shadow 文件中存储了口令的hash, 并能使用更多安<br/> 全的hash 算法
<hr/>
依此类推，根据python库中的安全算法，破解其他的加密算法


---

