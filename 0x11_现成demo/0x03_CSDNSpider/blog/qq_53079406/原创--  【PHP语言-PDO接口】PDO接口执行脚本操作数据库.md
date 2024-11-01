# 原创
：  【PHP语言-PDO接口】PDO接口执行脚本操作数据库

# 【PHP语言-PDO接口】PDO接口执行脚本操作数据库

**目录**

[前言：](#%E5%89%8D%E8%A8%80%EF%BC%9A)

[一、 PDO简介](#%E4%B8%80%E3%80%81%20PDO%E7%AE%80%E4%BB%8B)

[二、 PDO对象方法](#%E4%BA%8C%E3%80%81%20PDO%E5%AF%B9%E8%B1%A1%E6%96%B9%E6%B3%95)

[三、实战中心](#%E4%B8%89%E3%80%81%E5%AE%9E%E6%88%98%E4%B8%AD%E5%BF%83)

---


## 前言：

PDO：数据库抽象层

简介：PDO扩展为PHP访问数据库定义了一个轻量级的、一致性的接口，PDO解决了数据库连接不统一的问题。

---


---


## 一、 PDO简介

1、PDO简介<br/> （1）PHP的PDO（PHP Data Objects）是一种用于在PHP中访问数据库的扩展。它提供了一个统一的接口，使得开发人员可以使用相同的方式与不同类型的数据库进行交互，例如MySQL、PostgreSQL和SQLite等

（2）它与PHP5.1版本一起发布的，目前支持的数据库包括Firebird、FreeTDS、Interbase、MySQL、MS SQL Server、ODBC、Oracle、Postgre SQL、SQLite和Sybase。

（3）当操作不同数据库时，只需要修改PDO中的DSN（数据库源，如$dsn = "mysql:host=$host;dbname=$dbname;charset=utf8mb4";） ，即可使用PDO的统一接口进行操作。

---


2、PDO特性

（1）数据库支持: PDO提供了对多种数据库的支持，包括MySQL、SQLite、PostgreSQL、Oracle等，因此你可以在不改变代码逻辑的情况下切换使用不同的数据库。

（2）面向对象的接口: PDO使用面向对象的编程接口，通过实例化PDO类来连接数据库，并使用PDOStatement类执行查询和操作。

（3）预处理语句: PDO支持预处理语句（prepared statements），这是一种在执行前将SQL查询与数据分离的方式。预处理语句可以提高性能，并提供了更好的安全性，防止SQL注入攻击。

（4）绑定参数: 使用PDO的预处理语句，你可以绑定参数到查询中，而不是直接将值插入到SQL语句中。这种方式可以有效地防止SQL注入，并允许您重复使用准备好的语句，只需更改绑定的参数即可。

（5）事务支持: PDO支持数据库事务，你可以使用beginTransaction()开始一个事务，然后通过commit()提交事务或使用rollback()回滚事务以撤消之前的更改。

（6）错误处理: PDO使用异常机制来处理数据库操作中的错误。你可以捕获和处理PDOException异常，以便在出现错误时采取适当的措施。

（7）多个结果集: 在某些数据库中，你可以执行返回多个结果集的查询。PDO提供了方法来访问和处理这些结果集。

（8）支持命名占位符和问号占位符: PDO支持使用命名占位符（如:name）或问号占位符（如?）进行参数绑定。

（9）元数据获取: PDO提供了获取数据库元数据的方法，如获取表结构、列信息等。

（10）数据库连接管理: PDO提供了对数据库连接的管理，包括连接池管理、连接参数设置等。

---


3、PDO支持的数据库

---


<br/>4、PDO的配置

配置php配置文件，开启相应扩展<br/> extension=php_pdo.dll;

extension=php_pdo_mysql.dll;

---


5、PDO连接数据库<br/> 连接数据库：

1、参数形式

2、URL形式

3、配置文件

<br/> 参数形式连接数据库（掌握）

```
&lt;?php
$host = 'localhost';
$dbname = 'your_database_name';
$username = 'your_username';
$password = 'your_password';

try {
  $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
  // 设置PDO错误模式为异常
  $pdo-&gt;setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  echo "成功连接到数据库";
} catch(PDOException $e) {
  echo "数据库连接失败: " . $e-&gt;getMessage();
}
?&gt;

```

---


---


## 二、 PDO对象方法

<br/>1、对象方法：<img alt="" height="383" src="https://img-blog.csdnimg.cn/543b67daa5bb4ef2b689c4f1a6073fcb.png" width="776"/>

---


2、代码案例    

1、连接到数据库：

```
$dsn = 'mysql:host=localhost;dbname=mydatabase';
$username = 'username';
$password = 'password';

try {
    $pdo = new PDO($dsn, $username, $password);
    // 设置错误模式为异常
    $pdo-&gt;setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "成功连接到数据库";
} catch (PDOException $e) {
    echo "连接数据库失败: " . $e-&gt;getMessage();
}
```

###<br/> 2、执行查询语句并获取结果集：<br/>  

```
$query = "SELECT * FROM users";
$stmt = $pdo-&gt;query($query);

while ($row = $stmt-&gt;fetch(PDO::FETCH_ASSOC)) {
    echo $row['username'] . "&lt;br&gt;";
}
```

###<br/> 3、使用预处理语句执行带参数的查询：<br/>  

```
$query = "SELECT * FROM users WHERE age &gt; :age";
$stmt = $pdo-&gt;prepare($query);

$age = 18;
$stmt-&gt;bindParam(':age', $age, PDO::PARAM_INT);
$stmt-&gt;execute();

while ($row = $stmt-&gt;fetch(PDO::FETCH_ASSOC)) {
    echo $row['username'] . "&lt;br&gt;";
}
```

###<br/> 4、插入数据：

```
$query = "INSERT INTO users (username, email) VALUES (:username, :email)";
$stmt = $pdo-&gt;prepare($query);

$username = "john";
$email = "john@example.com";

$stmt-&gt;bindParam(':username', $username, PDO::PARAM_STR);
$stmt-&gt;bindParam(':email', $email, PDO::PARAM_STR);

$stmt-&gt;execute();
```

###<br/> 5、更新数据：

```
$query = "UPDATE users SET email = :email WHERE id = :id";
$stmt = $pdo-&gt;prepare($query);

$email = "newemail@example.com";
$id = 1;

$stmt-&gt;bindParam(':email', $email, PDO::PARAM_STR);
$stmt-&gt;bindParam(':id', $id, PDO::PARAM_INT);

$stmt-&gt;execute();
```

---


---


## 三、实战中心

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[BLACKxZONE/Treasure_knowledge<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
