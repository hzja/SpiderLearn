# 原创
：  熊海cms-文件包含漏洞

# 熊海cms-文件包含漏洞

#### 熊海cms-文件包含漏洞

## 环境搭建

> 
- 下载熊海cms V1.0- 使用phpstudy搭建web环境- 把下载好的源码放到网站根目录下，开启phpstudy,，浏览器访问即可


## 漏洞复现

> 
文件包含点一：根目录下index.php文件


> 
文件包含点二：admin目录下的index.php文件


## 漏洞分析

> 
两个index.php文件均为以下内容，代码中对GET传参只进行了一个 `addslashes`过滤操作，但该操作对预防文件包含没有什么作用，我们只需要在对应的files文件下存在以 `.php`结尾的文件，即可利用文件名(不包含.php后缀)作为参数 `r`的内容，达到文件包含的目的


```
&lt;?php
//单一入口模式
error_reporting(0); //关闭错误显示
$file=addslashes($_GET['r']); //接收文件名
$action=$file==''?'index':$file; //判断为空或者等于index
include('files/'.$action.'.php'); //载入相应文件
?&gt;

```
