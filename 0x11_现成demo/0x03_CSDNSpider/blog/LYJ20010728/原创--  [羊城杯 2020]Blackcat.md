# 原创
：  [羊城杯 2020]Blackcat

# [羊城杯 2020]Blackcat

#### [羊城杯 2020]Blackcat

## 考点

> 
hash_hmac函数绕过、RCE、绕过


## 思路

> 



> 



> 
easy_bypass


## Payload

> 
strings 音频后得到的源码


```
if(empty($_POST['Black-Cat-Sheriff']) || empty($_POST['One-ear'])){
    die('
$clandestine = getenv("clandestine");
if(isset($_POST['White-cat-monitor']))
    $clandestine = hash_hmac('sha256', $_POST['White-cat-monitor'], $clandestine);
$hh = hash_hmac('sha256', $_POST['One-ear'], $clandestine);
if($hh !== $_POST['Black-Cat-Sheriff']){
    die('
echo exec("nc".$_POST['One-ear']);

```

> 
Payload

