# 原创
：  【SQL注入】联合查询（最简单的注入方法）

# 【SQL注入】联合查询（最简单的注入方法）

**目录**

[一、介绍：](#%E4%B8%80%E3%80%81%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[二、原理：](#%E4%BA%8C%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[三、前提条件](#%E4%B8%89%E3%80%81%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6)

[四、利用过程](#%E5%9B%9B%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B)

---


> 
<h2>一、介绍：</h2>
是最简单的一种注入方法
联合查询注入  报错查询注入  布尔型注入  延时注入  堆叠查询注入


> 
<h2>二、原理：</h2>
就是可合并多个查询的结果的合集，顾名思义，就是将一个表追加到另一个表后，从而实现查询结果组合在一起。
<hr/>
在URL的参数位置中，将构造的语句注入到参数位置中
select （原始查询内容） union select （构造的内容）


---


> 
<h2>三、前提条件</h2>
①存在注入点，即未被过滤
②有显示位，即能回显结果
③两表列数相同，即order by 或union select 去判断列 数
④数据类型相同


---


> 
<h2>四、利用过程</h2>
1、判断是否存在注入点
（1）在参数位置修改参数值，eg：id=1修改为2后是否数据改变
（2）插入单、双引号的检测方法（常用），未闭合的单引号会引起SQL语句单引号未闭合的错误提示
<hr/>
2、判断注入点还是整形或字符型
（1）数字型：通过and 1=1
（2）字符串型：闭合单引号测试语句'and'1'='1进行判断
<hr/>
3、判断查询列数
order by 或 union select
<hr/>
4、判断显示位
报错回显，用不存在的id=-1加上union select……
或者and1=2加上union select……
<hr/>
下面的就都是通过报错后，在显示位构造要查找的信息
5、获取所有数据库名
6、获取数据库所有表名
7、获取字段名
8、获取字段中的数据


---


---

