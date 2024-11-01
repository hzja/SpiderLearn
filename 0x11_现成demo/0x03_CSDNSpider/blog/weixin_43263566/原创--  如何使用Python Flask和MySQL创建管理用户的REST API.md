# 原创
：  如何使用Python Flask和MySQL创建管理用户的REST API

# 如何使用Python Flask和MySQL创建管理用户的REST API

**部分数据来源：**ChatGPT 

#### 引言

        在现代化的应用开发中，数据库是一个非常重要的组成部分。关系型数据库（例如：MySQL、PostgreSQL）在这方面尤其是很流行。Flask是一个Python的web框架，非常适合实现REST API。在这篇文章中，我们将介绍如何使用Python Flask和MySQL创建一个管理用户的REST API。如果你是一个新手，这篇文章将很适合你。

#### **在这篇文章中，我们将：**

#### **安装所需的软件和工具**

在开始之前，您需要确保已经安装了以下软件：

#### **您还需要安装以下Python库：**

#### 创建Python Flask应用程序

我们现在准备开始编写Python代码。打开一个您喜欢的文本编辑器（如Visual Studio Code），创建一个新文件，我们将文件命名为`app.py`。在这个文件中，我们首先要导入所需的库和模块。这里，我们需要导入MySQL驱动程序和Flask库。

```
import mysql.connector
from flask import Flask, request, jsonify

```

接下来，我们需要连接到MySQL数据库。从这里，我们将创建一个连接到数据库（名为`management_system`）的名为`mydb`的数据库对象。我们需要指定MySQL服务器的用户名和密码。这将允许我们使用Python操作MySQL。

```
mydb = mysql.connector.connect(
    host="localhost",
    user="root",  # 替换为您的MySQL用户名
    password="password",  # 替换为您的MySQL密码
    database="management_system" # 数据库名称
)

```

现在，我们可以创建一个Flask应用程序对象。创建一个名为“app”的新Flask应用程序对象。

```
app = Flask(__name__)

```

在此之后，我们需要定义两个路由。一个用于创建/添加新用户，一个用于获取所有用户。使用装饰器`@app.route()`为应用程序定义路径。使用`methods`参数来定义允许的HTTP方法。对于创建用户的路由，我们使用POST方法，而对于获取所有用户的路由，我们使用GET方法。

```
@app.route('/users', methods=['POST'])
def create_user():
    # 从页面中获取用户信息
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']

    # 使用MySQL驱动程序在MySQL数据库中插入新用户
    cursor = mydb.cursor()
    sql = "INSERT INTO user (name, email, phone) VALUES (%s, %s, %s)"
    val = (name, email, phone)
    cursor.execute(sql, val)
    mydb.commit()

    # 返回一个JSON响应以表示用户已成功添加
    return "User created successfully"

@app.route('/users/get', methods=['GET'])
def get_all_users():
    # 从MySQL数据库中获取所有用户信息
    cursor = mydb.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    users = cursor.fetchall()

    # 将所有用户信息存储在一个列表中
    user_list = []
    for user in users:
        user_list.append(user)

    # 返回以JSON格式表示所有用户的响应
    return jsonify(user_list)

```

现在，我们的Flask应用程序已经准备就绪。我们只需要使用以下命令在命令行中运行它：

`python app.py`

此命令将启动我们的Flask应用程序，并在本地主机上的端口5000上运行。您现在可以使用POST请求向`/users`路由添加新用户，也可以使用GET请求请求`/users/get`路由来获取所有用户的信息。

#### 完整代码 

```
import mysql.connector
from flask import Flask, request,jsonify

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="management_system"
)


@app.route('/users', methods=['POST'])
def create_user():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']

    cursor = mydb.cursor()
    sql = "INSERT INTO user (name, email, phone) VALUES (%s, %s, %s)"
    val = (name, email, phone)
    cursor.execute(sql, val)
    mydb.commit()

    return "User created successfully"


@app.route('/users/get', methods=['GET'])
def get_all_users():
    cursor = mydb.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    users = cursor.fetchall()

    user_list = []
    for user in users:
        user_list.append(user)

    return jsonify(user_list)

if __name__ == '__main__':
    app.run(debug=True)
```

<img alt="" height="312" src="https://img-blog.csdnimg.cn/0b42bfda9b4348d8a1db803e7a902ea7.png" width="1183"/>  

#### 总结

        在本篇文章中，我们学习了如何使用Python Flask和MySQL数据库创建REST API来管理用户。我们首先安装了所需的软件和库，并连接到MySQL数据库。然后，我们创建了一个名为`app`的Flask应用程序对象，并定义了两个路由。一个用于添加新用户，一个用于获取所有用户信息。最后，我们启动了Flask应用程序并测试了我们的REST API。如果您是新手，可以通过此示例了解如何构建您的第一个REST API，尤其是在与MySQL有关的情况下。
