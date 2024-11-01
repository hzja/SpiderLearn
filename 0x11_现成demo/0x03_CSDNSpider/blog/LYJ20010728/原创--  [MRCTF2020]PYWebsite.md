# 原创
：  [MRCTF2020]PYWebsite

# [MRCTF2020]PYWebsite

#### [MRCTF2020]PYWebsite

## 考点

> 
X-Forwarded-For


## 思路

> 



> 



## Payload

> 
JavaScript代码提示


```
function enc(code){
  hash = hex_md5(code);
  return hash;
}
function validate(){
  var code = document.getElementById("vcode").value;
  if (code != ""){
    if(hex_md5(code) == "0cd4da0223c0b280829dc3ea458d655c"){
      alert("您通过了验证！");
      window.location = "./flag.php"
    }else{
      alert("你的授权码不正确！");
    }
  }else{
    alert("请输入授权码");
  }
  
}

```

> 
利用Postman构造XFF并发包

