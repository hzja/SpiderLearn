# 原创
：  [GXYCTF2019]BabyUpload

# [GXYCTF2019]BabyUpload

#### [GXYCTF2019]BabyUpload

## 考点

> 
文件类型绕过、文件名后缀绕过


## 思路

> 
先正常传几张图片试试，发现不行，传不上去，猜测有某种检测；<br/> 传php文件显示不能传后缀名有ph的文件；<br/> 我们先传一个.htaccess；<br/> 接着抓包传一个一句话木马上去，但是&lt;?被过滤了，绕过一下<br/> 蚁剑连接，获取flag


## Payload

> 
上传.htaccess将后面上传的文件当成php解析


> 
由于过滤了&lt;?，我们用js的形式上传一句话木马


> 
蚁剑链接测试

