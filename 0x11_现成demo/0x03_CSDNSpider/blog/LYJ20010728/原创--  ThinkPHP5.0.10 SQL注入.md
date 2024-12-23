# 原创
：  ThinkPHP5.0.10 SQL注入

# ThinkPHP5.0.10 SQL注入

#### ThinkPHP5.0.10 SQL注入

## 漏洞概要

> 



## 初始配置

> 
获取测试环境代码


```
composer create-project --prefer-dist topthink/think=5.0.10 tpdemo

```

> 
将 composer.json 文件的 require 字段设置成如下


```
"require": {
    "php": "&gt;=5.4.0",
    "topthink/framework": "5.0.10"
},

```

> 
然后执行 `composer update` ，并将 `application/index/controller/Index.php` 文件代码设置如下


```
&lt;?php
namespace app\index\controller;

class Index
{
    public function index()
    {
        $username = request()-&gt;get('username/a');
        $result = db('users')-&gt;where(['username' =&gt; $username])-&gt;select();
        var_dump($result);
        return '&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } .think_default_text{ padding: 4px 48px;} a{color:#2E5CD5;cursor: pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: "Century Gothic","Microsoft yahei"; color: #333;font-size:18px} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:)&lt;/h1&gt;&lt;p&gt; ThinkPHP V5&lt;br/&gt;&lt;span style="font-size:30px"&gt;十年磨一剑 - 为API开发设计的高性能框架&lt;/span&gt;&lt;/p&gt;&lt;span style="font-size:22px;"&gt;[ V5.0 版本由 &lt;a href="http://www.qiniu.com" target="qiniu"&gt;七牛云&lt;/a&gt; 独家赞助发布 ]&lt;/span&gt;&lt;/div&gt;&lt;script type="text/javascript" src="http://tajs.qq.com/stats?sId=9347272" charset="UTF-8"&gt;&lt;/script&gt;&lt;script type="text/javascript" src="http://ad.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;thinkad id="ad_bd568ce7058a1091"&gt;&lt;/thinkad&gt;';
    }
}
?&gt;

```

> 
在 `config/database.php` 文件中配置数据库相关信息，并开启 `config/app.php` 中的 `app_debug` 和 `app_trace` ，创建数据库信息如下


```
create database thinkphp;
use thinkphp;
create table users(
	id int primary key auto_increment,
	username varchar(50) not null
);
insert into users(id,username) values(1,'H3rmesk1t');

```

## 漏洞利用

> 
Payload


```
http://127.0.0.1/cms/public/index.php/index/index?username[0]=not%20like&amp;username[1][0]=%%&amp;username[1][1]=233&amp;username[2]=)%20union%20select%201,user()%23

```

## 漏洞分析

> 
首先，不管以哪种方式传递数据给服务器，这些数据在 ThinkPHP 中都会经过 `Request` 类的 `input` 方法，数据不仅会被强制类型转换，还都会经过 `filterValue` 方法的处理，该方法是用来过滤表单中的表达式，但是代码少过滤了 `NOT LIKE` ，而本次漏洞正是利用了这一点


> 
跟进 `thinkphp/library/think/Request.php`，在 `input` 方法中，传入的数据会经过 `filterValue` 过滤和强制类型转换，然后返回


> 
跟进 `filterValue` 方法，查看是如何实现的，发现调用到 `filterExp` 方法，可以看到没有过滤 `NOT LIKE`


> 
继续跟进 ThinkPHP处理 SQL 语句的方法，首先程序先调用 `Query` 类的 `where` 方法，通过其 `parseWhereExp` 方法分析查询表达式，然后再返回并继续调用 `select` 方法准备开始构建 `select` 语句


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2a2a4df416a24d009187ce18d000f330.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5f6348d163c84d78884284e0442114d1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
此处的 `$this-&gt;builder` 为 `think\db\builder\Mysql` 类，而 `Mysql` 类继承于 `Builder` 类，所以会继续调用到 `Builder` 类的 `select` 方法，该方法调用了`parseWhere` 方法，然后调用了 `buildWhere` 方法，该方法继续调用了 `parseWhereItem` 方法，跟进该方法


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bba6e107e264477c80505659edf5e5c9.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5c0dabb4b6b04dc7a618510b717429f5.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
此处到操作符 `$exp` 为 `NOT LIKE` 或 `LIKE` 时，MySQL的逻辑控制符可控，后进行拼接返回带入SQL语句中执行，导致了SQL注入漏洞


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d7ccb54cc93445eb9454fac2ff94eb27.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d26d15a2ba4e460783ec90ed7f364373.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
执行的SQL语句为：


```
(`username` NOT LIKE '%%' ) UNION SELECT 1,USER()# `username` NOT LIKE '233')

```

> 
完整的方法调用，从下往上


## 漏洞修复

> 
在 5.0.10 之后的版本，官方的修复方法是：在 `Request.php` 文件的 `filterValue` 方法中，过滤掉 `NOT LIKE` 关键字，而在 5.0.10 之前的版本中，这个漏洞是不存在的，但是其代码也没有过滤掉 `NOT LIKE` 关键字；经过调试，发现原来在 5.0.10 之前的版本中，其默认允许的表达式中不存在 `NOT LIKE`，所以即便攻击者可以通过外部控制该操作符号，也无法完成攻击，相反， 5.0.10 版本其默认允许的表达式中，存在 `NOT LIKE` ，因而可以触发漏洞


## 攻击总结

> 
参考Mochazz师傅的审计流程

