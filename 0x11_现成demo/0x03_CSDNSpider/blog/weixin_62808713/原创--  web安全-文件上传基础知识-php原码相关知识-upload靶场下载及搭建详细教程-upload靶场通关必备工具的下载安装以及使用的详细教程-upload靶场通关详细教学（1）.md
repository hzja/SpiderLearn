# 原创
：  web安全-文件上传基础知识-php原码相关知识-upload靶场下载及搭建详细教程-upload靶场通关必备工具的下载安装以及使用的详细教程-upload靶场通关详细教学（1）

# web安全-文件上传基础知识-php原码相关知识-upload靶场下载及搭建详细教程-upload靶场通关必备工具的下载安装以及使用的详细教程-upload靶场通关详细教学（1）

## 一、文件上传常见的验证类型

包括：后缀名，类型，文件头等。

1.后缀名(直接验证)：黑名单,白名单；

```
黑名单：明确不让上传的格式后缀
asp php jsp aspx cgi war...

白名单：明确可以上传的格式后缀
jpg png zip rar gif...

白名单相对比黑名单更加安全一些，
因为黑名单可能存在漏写的情况，
而白名单则只允许上传白名单内存在的后缀。
```

2.文件类型(间接验证)：MIME（Content-Type值）；

```
通过后缀名和文件类型的联系，
通过文件类型来猜测后缀名，
这种方法并不严谨，
因为可以通过抓包进行二次修改来伪造。
```

上传gif格式文件

上传jsp格式文件

3.文件头(间接验证)：内容头信息；

```
通过文件头信息和文件类型的联系，
通过文件头信息来猜测后缀名，
这种方法并不严谨，
因为可以通过抓包进行二次修改来伪造。
```

打开两个png后缀的图片，可以看到最开始的部分都是相同的。

打开两个jif后缀的图片，可以看到最开始的部分都是相同的。

## 二、了解原码相关内容

1.“$_FILES”相关内容

其中['myFile']是表单里的参数名的值

客户端文件的原名称。

文件的MIME类型，需要浏览器提供该信息的支持，例如"image/gif"。

已上传文件的大小，单位为字节。

文件被上传后在服务端储存的临时文件名，一般是系统默认。可以在php.ini的upload _tmp_dir指定，但用putenv()函数设置是不起作用的。

2.实例解释

首先写一份如下图所示的原码（“action”设置为空，将上传提交给当前文件）。

访问网页后上传一个文件查看返回内容如下。

可以利用类似如下图所示的方法来进行上传文件过滤。

3.注意

下图中框选的二者要对应一致。

4.其它

## 三、upload-labs靶场下载配置及必备工具

### 靶场简介

upload-labs是一个使用php语言编写的，专门收集渗透测试和CTF中遇到的各种上传漏洞的靶场。旨在帮助大家对上传漏洞有一个全面的了解。目前一共21关，每一关都包含着不同上传方式。

### 靶场下载地址

[https://github.com/c0ny1/upload-labs](https://github.com/c0ny1/upload-labs)

### 靶场环境下载地址——phpstudy

[https://www.xp.cn/download.html](https://www.xp.cn/download.html)

### 靶场搭建

将靶场下载后只需解压后粘贴到WWW目录下即可。

注意：PHP版本建议使用5.2.17，否则部分Pass可能无法绕过。

### 靶场通关必备工具——BurpSuite

[BurpSuite超详细安装教程-功能概述-配置-使用教程---(附下载链接)](https://blog.csdn.net/weixin_62808713/article/details/128719786)

## 四、upload-labs靶场通关教程

### &lt;Pass-01&gt;

```
提示：
本pass在客户端使用js对不合法图片进行检查！

原码：
function checkFile() {
    var file = document.getElementsByName('upload_file')[0].value;
    if (file == null || file == "") {
        alert("请选择要上传的文件!");
        return false;
    }
    //定义允许上传的文件类型
    var allow_ext = ".jpg|.png|.gif";
    //提取上传文件的类型
    var ext_name = file.substring(file.lastIndexOf("."));
    //判断上传文件类型是否允许上传
    if (allow_ext.indexOf(ext_name + "|") == -1) {
        var errMsg = "该文件不允许上传，请上传" + allow_ext + "类型的文件,当前文件类型为：" + ext_name;
        alert(errMsg);
        return false;
    }
}
```

选中事先创建好的“php.php”文件，修改前端代码，之后点击上传。

```
文件内容为：
&lt;?php
phpinfo();
?&gt;
```

访问发现可以执行。

### &lt;Pass-02&gt;

```
提示：
本pass在服务端对数据包的MIME进行检查！

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        if (($_FILES['upload_file']['type'] == 'image/jpeg') || ($_FILES['upload_file']['type'] == 'image/png') || ($_FILES['upload_file']['type'] == 'image/gif')) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH . '/' . $_FILES['upload_file']['name']            
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '文件类型不正确，请重新上传！';
        }
    } else {
        $msg = UPLOAD_PATH.'文件夹不存在,请手工创建！';
    }
}
```

选中事先创建好的“php.php”文件，开启代理，点击上传，使用Burp抓包修改Content-Type值（image/jpeg、image/png、image/gif）之后放包。

访问发现可以执行。

### &lt;Pass-03&gt;+php后缀常见别名

```
提示：
本pass禁止上传.asp|.aspx|.php|.jsp后缀文件！

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array('.asp','.aspx','.php','.jsp');
        $file_name = trim($_FILES['upload_file']['name']);
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        $file_ext = trim($file_ext); //收尾去空

        if(!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.date("YmdHis").rand(1000,9999).$file_ext;            
            if (move_uploaded_file($temp_file,$img_path)) {
                 $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '不允许上传.asp,.aspx,.php,.jsp后缀文件！';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

此关采用的是黑名单拦截，因此考虑到采用php文件的其它扩展名来绕过（包括：php3、php5、phtml等）。

修改php后缀名为php3，点击上传即可绕过。

---


知识补充：

php后缀常见别名：.php .phtml .php3 .php5 .php1 .php4 .php2 .pht

---


### &lt;Pass-04&gt;

```
提示：
本pass禁止上传.php|.php5|.php4|.php3|.php2|php1|.html|.htm|.phtml|.pHp|.pHp5|.pHp4|.pHp3|.pHp2|pHp1|.Html|.Htm|.pHtml|.jsp|.jspa|.jspx|.jsw|.jsv|.jspf|.jtml|.jSp|.jSpx|.jSpa|.jSw|.jSv|.jSpf|.jHtml|.asp|.aspx|.asa|.asax|.ascx|.ashx|.asmx|.cer|.aSp|.aSpx|.aSa|.aSax|.aScx|.aShx|.aSmx|.cEr|.sWf|.swf后缀文件！

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".php1",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".pHp1",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".ini");
        $file_name = trim($_FILES['upload_file']['name']);
        $file_name = deldot($file_name);//删除文件名末尾的点
        $file_ext = strrchr($file_name, '.');
        $file_ext = strtolower($file_ext); //转换为小写
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
        $file_ext = trim($file_ext); //收尾去空

        if (!in_array($file_ext, $deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH.'/'.$file_name;
            if (move_uploaded_file($temp_file, $img_path)) {
                $is_upload = true;
            } else {
                $msg = '上传出错！';
            }
        } else {
            $msg = '此文件不允许上传!';
        }
    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

此关与上一关的区别在于本关的黑名单包含了大多数脚本后缀名，因此上一关的办法在本关并不可行。

先上传.htaccess 文件，再上传一个文件名中包含“ranzi”的PHP代码文件。

```
.htaccess 文件的内容为：
&lt;FilesMatch "ranzi"&gt;
SetHandler application/x-httpd-php
&lt;/FilesMatch&gt;
```

注意：“.htaccess” 文件最好使用Notepad++创建。

命名为.htaccess这个文件是伪静态文件。

文件名中含有“ranzi”的文件用PHP代码解析执行。

### &lt;Pass-05&gt;

```
提示：
上传目录存在php文件（readme.php）

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array(".php",".php5",".php4",".php3",".php2",".html",".htm",".phtml",".pht",".pHp",".pHp5",".pHp4",".pHp3",".pHp2",".Html",".Htm",".pHtml",".jsp",".jspa",".jspx",".jsw",".jsv",".jspf",".jtml",".jSp",".jSpx",".jSpa",".jSw",".jSv",".jSpf",".jHtml",".asp",".aspx",".asa",".asax",".ascx",".ashx",".asmx",".cer",".aSp",".aSpx",".aSa",".aSax",".aScx",".aShx",".aSmx",".cEr",".sWf",".swf",".htaccess");
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

可以看到本关内将“.htaccess”后缀名文件也进行了过滤。

先上传.user.ini。

作用域是当前文件夹和当前文件夹中的子文件;包含指定的文件，显示在页面上。

```
.user.ini的内容：
Auto_prepend_file=phpinfo.jpg //在页面上部显示
Auto_prepend_file=phpinfo.jpg //在页面底部部显示
```

再上传phpinfo.jpg。

查看readme.php文件即可。

### &lt;Pass-06&gt;

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
        $file_ext = str_ireplace('::$DATA', '', $file_ext);//去除字符串::$DATA
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
$file_ext= strtolower($file_ext); //转换为小写
```

没有过滤大小写的代码。

所以考虑修改上传文件的后缀名为php.Php。

上传php.Php。

可以看到上传成功了，访问发现可以执行。

---


剩余关卡详解见下一篇文章。

---

