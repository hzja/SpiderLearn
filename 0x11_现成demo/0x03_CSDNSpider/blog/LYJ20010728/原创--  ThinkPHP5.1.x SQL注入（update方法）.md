# 原创
：  ThinkPHP5.1.x SQL注入（update方法）

# ThinkPHP5.1.x SQL注入（update方法）

#### ThinkPHP5 SQL注入（update方法）

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
        $username = request()-&gt;get('username/a');
        db('users')-&gt;where(['id' =&gt; 1])-&gt;update(['username' =&gt; $username]);
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
http://127.0.0.1/cms/public/index.php?username[0]=point&amp;username[1]=1&amp;username[2]=updatexml(1,concat(0x7,database(),0x7e),1)^&amp;username[3]=0 
或者
http://127.0.0.1/cms/public/index.php?username[0]=point&amp;username[1]=1&amp;username[2]=updatexml(1,concat(0x7,database(),0x7e),1)|&amp;username[3]=0 

```

## 漏洞分析

> 
先打断点，跟进一下payload，先接收变量


> 
跟进到`thinkphp/helper.php`中的`db`方法


> 
跟进到`thinkphp/library/think/db/Query.php`中`where`方法，接着进入`update`方法


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/83563ac2ac794d448e715778625a3b04.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/424b57587df04c6e9e7e88c397e6b312.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
进入到return里面，跟进到`thinkphp/library/think/db/Connection.php`中`connect`类的`update`方法，找到生成update的SQL语句`$sql = $this-&gt;builder-&gt;update($query);`，跟进该语句看看干了什么


> 
跟进`thinkphp/library/think/db/Builder.php`中的`update`方法，在`Builder`类中的`update`方法里又调用了`parseData`方法


> 
跟进`parseData`方法，在该方法中的swich语句中的default 语句中存在一个`parseArrayData`方法，跟进去看看


> 
跟进`thinkphp/library/think/db/builder/Mysql.php`中的`parseArrayData`方法，这里如果数组`$data`第一个变量的小写是`point`的话就进入到后续的判断语句中；由于`$data[2]`和`$data[3]`都不为空，所以就是传进来的值；if语句判断了一下`$data[1]`是不是数组，是的话就将一维数组的值连接为一个字符串；最后进入到拼接语句，拼接的形式为：`$data[2]('$data[3]($data[1])');`，参数均为可控参数


> 
用debug看看拼接后的值：`updatexml(1,concat(0x7,database(),0x7e),1)^('0(1)')`，成功造成SQL注入


## 漏洞修复

> 
参考官方修复方法，直接将 `parseArrayData` 方法删除


## 攻击总结

> 
参考Mochazz师傅的审计流程

