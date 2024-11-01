# 原创
：  Flask处理表单

# Flask处理表单

**app.py**

```
#encoding:utf-8
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '这是get请求！'
    else:
        return '这是post请求！'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='4399')

```

**index.html**

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Title&lt;/title&gt;
    &lt;style type="text/css"&gt;
        .div1 {
            height: 180px;
            width: 380px;
            border: 1px solid #8A8989;
            margin: 0 auto;
        }
        .input {
            display: block;
            width: 350px;
            height: 40px;
            margin: 10px auto;
        }
        .button {
            background: #2066C5;
            color: white;
            font-size: 18px;
            font-weight: bold;
            height: 50px;
            border-radius: 4px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="div1"&gt;
        &lt;form action="login" method="post"&gt;
            &lt;input type="text" class="input" placeholder="请输入用户名："&gt;
            &lt;input type="password" class="input" placeholder="请输入密码："&gt;
            &lt;input type="submit" value="登录" class="input button"&gt;
        &lt;/form&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```
