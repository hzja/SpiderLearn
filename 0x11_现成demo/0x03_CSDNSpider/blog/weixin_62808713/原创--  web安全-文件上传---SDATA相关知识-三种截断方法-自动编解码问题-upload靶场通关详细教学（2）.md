# 原创
：  web安全-文件上传-::SDATA相关知识-三种截断方法-自动编解码问题-upload靶场通关详细教学（2）

# web安全-文件上传-::SDATA相关知识-三种截断方法-自动编解码问题-upload靶场通关详细教学（2）

### &lt;Pass-07&gt;

```
提示：
本pass禁止上传.php|.php5|.php4|.php3|.php2|php1|.html|.htm|.phtml|.pHp|.pHp5|.pHp4|.pHp3|.pHp2|pHp1|.Html|.Htm|.pHtml|.jsp|.jspa|.jspx|.jsw|.jsv|.jspf|.jtml|.jSp|.jSpx|.jSpa|.jSw|.jSv|.jSpf|.jHtml|.asp|.aspx|.asa|.asax|.ascx|.ashx|.asmx|.cer|.aSp|.aSpx|.aSa|.aSax|.aScx|.aShx|.aSmx|.cEr|.sWf|.swf后缀文件！

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess",".ini");
        $file_name = $_FILES['upload_file']['name'];
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        
        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.date("YmdHis").rand(1000,9999).$file_ext;
            if (move_uploaded_file($temp_file,$img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件不允许上传';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

```
缺少的代码：
$file_ext= trim($file_ext); //首尾去空
```

没有首尾去空的代码。

所以考虑使用空格绕过。

使用BURP抓包后，在php后缀名的后面添加一个空格后放包。

访问发现可以执行。

### &lt;Pass-08&gt;

```
提示：
本pass禁止上传所有可以解析的后缀！

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess",".ini");
        $file_name = trim($_FILES['upload_file']['name']);
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        $file_ext = trim($file_ext); //首尾去空
        
        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.$file_name;
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件类型不允许上传！';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

```
缺少的代码：
$file_name = deldot($file_name);//删除文件名末尾的点
```

没有删除文件名末尾后的点。

所以考虑使用点进行绕过。

使用BURP抓包后，在php后缀名的后面添加一个“.”后放包。

访问发现可以执行。

### &lt;Pass-09&gt;+::SDATA相关知识

```
提示：
本pass禁止上传.php|.php5|.php4|.php3|.php2|php1|.html|.htm|.phtml|.pHp|.pHp5|.pHp4|.pHp3|.pHp2|pHp1|.Html|.Htm|.pHtml|.jsp|.jspa|.jspx|.jsw|.jsv|.jspf|.jtml|.jSp|.jSpx|.jSpa|.jSw|.jSv|.jSpf|.jHtml|.asp|.aspx|.asa|.asax|.ascx|.ashx|.asmx|.cer|.aSp|.aSpx|.aSa|.aSax|.aScx|.aShx|.aSmx|.cEr|.sWf|.swf|.htaccess后缀文件！

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess",".ini");
        $file_name = trim($_FILES['upload_file']['name']);
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = trim($file_ext); //首尾去空
        
        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.date("YmdHis").rand(1000,9999).$file_ext;
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件类型不允许上传！';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

```
缺少的代码：
$file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
```

没有去除字符串::$DATA。

所以考虑上传后缀名添加::$DATA。

---


知识补充：

php在window的时候如果文件名+“::SDATA”会把::SDATA之后的数据当成文件流处理，也就是不会检测后缀名，且保持“::SDATA"之前的文件名。

总而言之。它的目的就是不检查后缀名。

---


使用BURP抓包后，在php后缀名的后面添加一个“::$DATA”后放包。

右键后点击“新建标签页打开图像”。

在新打开的标签页内将网址末尾的“::$DATA”删除掉后访问便可执行。

### &lt;Pass-10&gt;

```
提示：
本pass只允许上传.jpg|.png|.gif后缀的文件！

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess",".ini");
        $file_name = trim($_FILES['upload_file']['name']);
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        $file_ext = trim($file_ext); //首尾去空
        
        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.$file_name;
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件类型不允许上传！';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

deldot()函数的作用是从字符串的尾部开始，从后向前删除“.”，直到该字符串的末尾字符不是“.”为止。

但是这个原码里只进行了一次deldot()过滤，不是循环过滤。

在最后还进行了一次首尾去空的过滤。

因此我们可以想到使用BURP抓包后，在php后缀名的后面添加“. . ”后放包来对其进行绕过。

访问发现可以执行。

### &lt;Pass-11&gt;

```
提示：
本pass会从文件名中去除.php|.php5|.php4|.php3|.php2|php1|.html|.htm|.phtml|.pHp|.pHp5|.pHp4|.pHp3|.pHp2|pHp1|.Html|.Htm|.pHtml|.jsp|.jspa|.jspx|.jsw|.jsv|.jspf|.jtml|.jSp|.jSpx|.jSpa|.jSw|.jSv|.jSpf|.jHtml|.asp|.aspx|.asa|.asax|.ascx|.ashx|.asmx|.cer|.aSp|.aSpx|.aSa|.aSax|.aScx|.aShx|.aSmx|.cEr|.sWf|.swf|.htaccess字符！

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array("php","php5","php4","php3","php2","html","htm","phtml","pht","jsp","jspa","jspx","jsw","jsv","jspf","jtml","asp","aspx","asa","asax","ascx","ashx","asmx","cer","swf","htaccess","ini");

        $file_name = trim($_FILES['upload_file']['name']);
        $file_name = str_ireplace($deny_ext,"", $file_name);
        $temp_file = $_FILES['upload_file']['tmp_name'];
        $img_path = UPLOAD_PATH.'/'.$file_name;        
        if (move_uploaded_file($temp_file, $img_path)) {
            $is_upload = true;
        } else {
            $msg = '上传出错！';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

此关主要是对如下代码进行绕过

```
$file_name = str_ireplace($deny_ext,"", $file_name);
```

这个代码的意思就是如果上传的文件的后缀名与黑名单里的后缀名对应了，就将其替换为空。

但是这里只过滤了一次，不是循环过滤。

因此考虑双后缀名来对此进行绕过。

使用BURP抓包后，将后缀名改为“.pphphp”后放包来对其进行绕过。

访问发现可以执行。

### &lt;Pass-12&gt;+三种截断方法讲解

```
提示：
本pass上传路径可控！

原码：
$is_upload = false;
$msg = null;
if(isset($_POST['submit'])){
    $ext_arr = array('jpg','png','gif');
    $file_ext = substr($_FILES['upload_file']['name'],strrpos($_FILES['upload_file']['name'],".")+1);
    if(in_array($file_ext,$ext_arr)){
        $temp_file = $_FILES['upload_file']['tmp_name'];
        $img_path = $_GET['save_path']."/".rand(10, 99).date("YmdHis").".".$file_ext;

        if(move_uploaded_file($temp_file,$img_path)){
            $is_upload = true;
        } else {
            $msg = '上传出错！';
        }
    } else{
        $msg = "只允许上传.jpg|.png|.gif类型文件！";
    }
}
```

此关便不是黑名单来进行过滤了，采用的是白名单。

```
$file_ext = substr($_FILES['upload_file']['name'],strrpos($_FILES['upload_file']['name'],".")+1);
```

这个语句的可以防止使用多个“.”进行绕过。

“+1”是指最后一个点，将最后一个点后的后缀名取出来，给参数$file_ext来进行下一步的判断。

---


知识补充：

在url中“%00”表示ascii码中的“0” ，而ascii码中“0”作为特殊字符保留，表示[字符串](https://so.csdn.net/so/search?q=%E5%AD%97%E7%AC%A6%E4%B8%B2&amp;spm=1001.2101.3001.7020)结束，所以当url中出现“%00”时就会认为读取已结束。

举例：

?save path=../upload/shell.jpg--------------------&gt;shell.jpg

?save path=../upload/shell.php%00.jpg-----------&gt;shell.php

“0x”开头表示16进制，“0”在十六进制中是“00”，“ 0x00”就是“%00”解码成的16进制。

先在php的后面添加一个空格来占位（为了更加容易找到修改“00”的位置）。

然后打开“Hex”，前面占位的空格的16进制为“20”，因此修改16进制内容，将“20”改成“00”即可。

0x0a是十六进制表示方法，表示ASCII码为/n的换行字符，具体为换行至下一行行首起始位置。

当 save_path 通过POST方法传入，与上面一样，但要注意同时要在二进制文件当中进行修改(%00 不能再自动解码)

php版本要小于5.3.4，5.3.4及以上已经修复此问题。

magic_quotes_gpc（魔术引号）需要为关闭状态。

---


此关就需要用到“%00截断”的方法了。

在下图所示的位置插入“去后缀的文件名+.php%00“。

然后放包即可。

访问发现可以执行。

### &lt;Pass-13&gt;+自动编解码问题

```
提示：
本pass上传路径可控！

原码：
$is_upload = false;
$msg = null;
if(isset($_POST['submit'])){
    $ext_arr = array('jpg','png','gif');
    $file_ext = substr($_FILES['upload_file']['name'],strrpos($_FILES['upload_file']['name'],".")+1);
    if(in_array($file_ext,$ext_arr)){
        $temp_file = $_FILES['upload_file']['tmp_name'];
        $img_path = $_POST['save_path']."/".rand(10, 99).date("YmdHis").".".$file_ext;

        if(move_uploaded_file($temp_file,$img_path)){
            $is_upload = true;
        } else {
            $msg = "上传失败";
        }
    } else {
        $msg = "只允许上传.jpg|.png|.gif类型文件！";
    }
}
```

此关依然是白名单，与上一关的区别在于此关的接收方式是“POST”，而上一关的是“GET”。

```
上一关：
$img_path = $_GET['save_path']."/".rand(10, 99).date("YmdHis").".".$file_ext;

此关：
$img_path = $_POST['save_path']."/".rand(10, 99).date("YmdHis").".".$file_ext;
```

采用“0x00截断”的方法进行绕过。

在下图所示位置插入“去后缀名的文件名+.php+空格”。

在“Hex”内找到对应的位置，将上一步添加的末尾的空格对应的“20”，修改为“00”后放包。

访问发现可以执行。

---


知识补充：

get：会自动解码

post：不会自动解码，所以想以post提交数据%00需要把它进行url编码

---


此关需要在下图所示位置插入“去后缀的文件名+.php%00“。

插入后将“%00”进行URL编码。

编码后放包即可。

访问发现可以执行。

---


剩余关卡详解见下一篇文章。

---

