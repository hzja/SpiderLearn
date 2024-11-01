# 原创
：  Flask-文件上传

# Flask-文件上传

**app.py**

```
#coding:utf-8
import time
import platform
import os
from os import path
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from form import UploadForm

app = Flask(__name__)
if platform.system() == 'Windows':
    slash = '\\'
elif platform.system() == 'Linux':
    slash = '/'

UPLOAD_PATH = os.path.curdir + slash + 'uploads' + slash

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        if not os.path.exists(UPLOAD_PATH):
            os.makedirs(UPLOAD_PATH)    # 判断文件保存路径是否存在，不存在则创建目录

        form = UploadForm(CombinedMultiDict([request.form, request.files]))     # 表单验证

        if form.validate():
            f = request.files['file']   # 获取文件流
            filename = secure_filename(f.filename)  # 获取文件名称
            ext = filename.rsplit('.', 1)[1]    # 获取文件后缀
            unix_time = int(time.time())    # 获取时间
            new_filename = str(unix_time) + '.' + ext   # 对文件进行重命名

            file_url = UPLOAD_PATH + new_filename
            f.save(path.join(UPLOAD_PATH, new_filename))    # 文件保存

            return '上传成功！'
        else:
            return '上传失败，请检查上传文件格式！'

@app.route('/images/&lt;filename&gt;/', methods=['GET', 'POST'])
def get_img(filename):
    dirpath = os.path.join(app.root_path, 'uploads')
    return send_from_directory(dirpath, filename)   # 在线浏览方式

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='4399')

```

**form.py**

```
from wtforms import Form, FileField, StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class UploadForm(Form):
    file = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'])])

```

**upload.html**

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;文件上传&lt;/title&gt;
    &lt;style type="text/css"&gt;
        .div1 {
            height: 180px;
            width: 380px;
            border: 1px solid #8A8989;
            margin: 0 auto;
        }
        .input {
            display: block;
            width: 250px;
            height: 30px;
            margin: 10px auto;
        }
        .button {
            background: #2066C5;
            color: white;
            font-size: 18px;
            font-weight: bold;
            height: 30px;
            border-radius: 4px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div class="div1"&gt;
    &lt;form action="" method="post" enctype="multipart/form-data"&gt;
        &lt;input type="file" name="file" class="input"&gt;
        &lt;input type="submit" name="上传" class="input button"&gt;
    &lt;/form&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```
