# 原创
：  【Python脚本进阶】1.3、第二个脚本：Zip文件口令破解机

# 【Python脚本进阶】1.3、第二个脚本：Zip文件口令破解机

**目录**

[一、简介](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B)

[概述：](#%E6%A6%82%E8%BF%B0%EF%BC%9A)

[二、示例](#%E4%BA%8C%E3%80%81%E7%A4%BA%E4%BE%8B)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[优化](#%E4%BC%98%E5%8C%96)

[提高性能](#%E6%8F%90%E9%AB%98%E6%80%A7%E8%83%BD)

[任意性](#%E4%BB%BB%E6%84%8F%E6%80%A7)

[注：](#%E6%B3%A8%EF%BC%9A)

[测试方法：](#%E6%B5%8B%E8%AF%95%E6%96%B9%E6%B3%95%EF%BC%9A)

---


## 一、简介

> 
<h3>概述：</h3>
编写Zip文件口令破解机要学习zipfile 库的使用方法
打开Python解释器， 我们用help('zipfile')命令进一步了解这个库， 并重点看一下ZipFile 类中的extractall()方法。这个类和这个方法对我们编程破解有口令保护的Zip文件是很有用的。extractall()方法用可选参数指定密码的方式





---


---


## 二、示例

> 
<h3>示例：</h3>
编写一个脚本知道口令情况，测试Zip 文件库的用法
导库， 用带有口令保护的Zip文件的文件名， 实例化一个新的ZipFile类。要解压这个Zip文件， 我们使用extractall(）方法， 并在可选参数pwd上填入口令
<pre><code>import zipfile
zFile = zipfile.ZipFile("1.zip")
zFile.extractall(pwd="secret")</code></pre>
<hr/>
分析错误密码会是什么情况，来捕获和处理异常代码
<pre><code>import zipfile
zFile = zipfile.ZipFile("1.zip")
try:
    zFile.extractall(pwd="wrong")
except Exception as e:
    print(e)</code></pre>
<hr/>

可以用因口令不正确而抛出的异常，来测试字典文件中是否有Zip 文件的口令。
实例化一个ZipFile 类， 打开字典文件， 遍历并测试字典中的每个单词，如extractall(）函数的执行没有出错， 则打印一条消息， 输出正确的口令。如果extractall()函数抛出口令错误， 就忽略这个异常， 并继续测试字典中的下一个口令
<pre><code>import zipfile
zFile = zipfile.ZipFile('1.zip')
passFile = open('dietionary.txt')
for line in passFile.readlines():
    password = line.strip('\n')
    try:
        zFile.extractall(pwd=password)
        print('Password = ' + password + '\n')
        exit(0)
    except Exception as e:
        pass</code></pre>


---


> 
<h3>优化</h3>
不再是线性执行的程序。将程序模块化成分离函数，用函数模块化脚本
<pre><code>import zipfile
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except Exception as e:
        return e

def main():
    zFile = zipfile.ZipFile('1.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zFile, password)
        if guess:
            print('Password = ' + password + '\n')
            exit(0)

if __name__ == '__main__':
    main()</code></pre>


> 
<h3>提高性能</h3>
利用线程同时测试多个口令， 而不是只能逐个测试词库中的单词。对词库中的每个单词， 都会生成一个新的线程去测试它。
<pre><code>import zipfile
from threading import Thread
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('Found password ' + password + '\n')
    except:
        pass

def main():
    zFile = zipfile.ZipFile('1.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()</code></pre>


> 
<h3>任意性</h3>
用户可以指定要破解的Zip 文件的文件名和字典文件的文件名。 需要导入optparse库，是用于解析下面脚本的标志和可选参数的。在zipfile-cracker脚本中，我们将添加两个强制性flags一zip文件名和字库名
<pre><code>import zipfile
import optparse
from threading import Thread


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print('Found password ' + password + '\n')
    except:
        pass


def main():
    parser = optparse.OptionParser("usage%prog" + "-f &lt;zipfile&gt; -d &lt;dictionary&gt;")
    parser.add_option('-f', dest='znarne', type='string', help='specify zip file')
    parser.add_option('-d', dest='dnarne', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dnarne == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()


if __name__ == '__main__':
    main()
</code></pre>
<h4>注：</h4>
1、OptionParser是python中用来处理命令行的模块，在我们使用python进行流程化开发中必要的工具
2、add_option
3、args)= parser.parse_args()属性给与args实例： 把parser中设置的所有"add_argument"给返回到args子类实例当中， 那么parser中增加的属性内容都会在args实例中，使用即可
<hr/>
<h4>测试方法：</h4>
Python  脚本.py   -f 文件.zip   -d 字典.txt


#### 注：
