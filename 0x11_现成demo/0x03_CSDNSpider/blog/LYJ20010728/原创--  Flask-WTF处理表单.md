# 原创
：  Flask-WTF处理表单

# Flask-WTF处理表单

**app.py**

```
#encoding:utf-8
from flask import Flask
from flask import flash
from flask import url_for
from flask import render_template
from flask_wtf.csrf import CSRFProtect
# 导入定义的BaseLogin
from form import BaseLogin
import config

app = Flask(__name__)
app.config.from_object(config)  # 配置文件初始化

@app.route('/login', methods=['GET', 'POST'])
def baselogin():
    form = BaseLogin()  # 进行表单验证
    if form.validate_on_submit():   # 判断验证提交是否通过
        # 消息闪现
        flash(form.name.data+'|'+form.password.data)
        return '消息提交成功'
    else:
        # 渲染
        return render_template('login.html', form=form)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='4399')

```

**config.py**

```
#coding:utf-8
import os

SECRET_KEY = os.urandom(24)     # 生成密钥
CSRF_ENABLED = True     # 开启CSRF保护

```

**form.py**

```
# 引入From基类
from flask_wtf import Form
# 引入From元素父类
from wtforms import StringField
from wtforms import PasswordField
# 引入From验证父类
from wtforms.validators import DataRequired
from wtforms.validators import Length

# 登录表蛋类，继承于From类
class BaseLogin(Form):
    # 用户名
    name = StringField('name', validators=[DataRequired(message="用户名不能为空"), Length(6, 16, message="用户名长度位于6到16位之间")], render_kw={'placeholder':'请输入用户名'})

    # 密码
    password = PasswordField('password', validators=[DataRequired(message="密码不能为空"), Length(6, 16, message="密码长度位于6到16位之间")], render_kw={'placeholder':'请输入密码'})


```

**login.html**

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Flase_WTF&lt;/title&gt;
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
        &lt;!--启动csrf--&gt;
        {{ form.hidden_tag() }}     &lt;!--CSRF表单--&gt;
        {{ form.name(size=16, id='name', class='input') }}
        {% for e in form.name.errors %}
            &lt;span style="color: red"&gt;{{ e }}&lt;/span&gt;     &lt;!--错误提示--&gt;
        {% endfor %}
        {{ form.password(size=16, id='password', class='input') }}
        {% for e in form.name.errors %}
            &lt;span style="color: red"&gt;{{ e }}&lt;/span&gt;     &lt;!--错误提示--&gt;
        {% endfor %}
        &lt;input type="submit" value="登录" class="input button"&gt;       &lt;!--登录用按钮--&gt;
    &lt;/form&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```
