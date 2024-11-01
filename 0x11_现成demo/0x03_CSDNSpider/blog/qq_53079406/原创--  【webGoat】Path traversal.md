# 原创
：  【webGoat】Path traversal

# 【webGoat】Path traversal

**目录**

[Path traversal](#lesson-title)

[第2题：](#%E7%AC%AC2%E9%A2%98%EF%BC%9A)

[第3题：](#%E7%AC%AC3%E9%A2%98%EF%BC%9A)

[第4题：](#%E7%AC%AC4%E9%A2%98%EF%BC%9A)

[第5题：](#%E7%AC%AC5%E9%A2%98%EF%BC%9A)

[第7题：](#%E7%AC%AC7%E9%A2%98%EF%BC%9A)

---


## Path traversal

> 
<h3>第2题：</h3>
题目要求的位置


选择了一张图片，然后点击update，然后抓到包了
发送到重发器
点击发送后，找到图片原本要发送的路径
也就是目标路径的上一级


请求包往下翻，找到了test，这个test可能是文件名test
修改为../test





 

> 
<h3>第3题：</h3>
选择了一张图片，然后点击update，然后抓到包了
再发送到重发器
修改为第二题的../test再点击发送
发现上传目录未变（存在过滤../）


 尝试双写绕过....//
发现题目完成成功了






> 
<h3>第4题：</h3>
再测试一下....//
发现文件的路径要传到上个文件夹中
而且双写也被过滤（可能是循环过滤，或者是上传到后端服务器，此处被后端修改）


发现文件名被重命名了
看能否上传到上级目录，那样就能避免重命名


加上../
（发现题目完成成功了）







> 
<h3>第5题：</h3>
题目要找到path-traversal-secret.jpg
抓包发发到重发器
在响应包中找到了参数id
 （在这个目录所对应的图片应该都是用数字表示，题目给出了文件名，应该是要遍历上一个目录）

 错误请求格式，所以确实是这样<img alt="" height="421" src="https://img-blog.csdnimg.cn/f60a0f0ba5f24a43a94dbcc5a5bfce95.png" width="997"/>

?id=../path-traversal-secret.jpg
提示：查询参数中不允许使用非法字符
应该是被过滤了


尝试编码绕过
../改为%2e%2e%2f
?id=%2e%2e%2fpath-traversal-secret.jpg


?id=%2e%2e%2f%2e%2e%2fpath-traversal-secret.jpg


 ?id=%2e%2e%2f%2e%2e%2fpath-traversal-secret
（返回包中提示：您发现它提交了您的用户名的SHA-512哈希值作为答案）

 我的用户名是admin123






> 
<h3>第7题：</h3>



