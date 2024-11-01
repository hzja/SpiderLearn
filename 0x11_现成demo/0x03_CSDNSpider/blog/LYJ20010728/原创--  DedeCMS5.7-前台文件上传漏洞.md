# 原创
：  DedeCMS5.7-前台文件上传漏洞

# DedeCMS5.7-前台文件上传漏洞

#### DedeCMS5.7-前台文件上传漏洞

## 环境搭建

> 
- 官方下载DeDeCMS V5.7 SP2(UTF-8)，[下载地址](http://www.dedecms.com/products/dedecms/downloads/)- 使用phpstudy搭建web环境- 把下载好的源码放到网站根目录下，开启phpstudy,，浏览器访问即可


> 
- 点击我已阅读并继续，进行环境检测，保存默认即可


> 
- 接下来是参数配置，需要设置的只有数据库密码，将本地数据库的密码填上即可


> 
环境搭建完成后，登录后台，开启会员功能


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210610144920421.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210610145050851.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 漏洞复现

> 
- 进入会员中心，由于后面上传文件有权限限制，所以我们必须用管理员的身份，进入会员中心后进入内容中心模块


> 
- 发布一个文章，点击编辑器的上传图片按钮，上传图片马


> 
- 抓包修改图片马后缀名


> 
- 访问上传成功的图片马


## 漏洞分析

> 
查看代码，在 `include\dialog\select_images_post.php`中，发现图片上传的限制


> 
从代码中我们可以发现，当上传的文件后缀名中存在 `[ \r\n\t\*\%\\\/\?&gt;&lt;\|\":]`时会被过滤成空，所以我们可以利用 `.ph*p`或者 `.ph%p`等来利用这个点绕过，来达到实现 `.php`后缀名的目的，跟进 `$cfg_imgtype`中看看过滤限制


> 
上传的文件后缀名中必须包括 `'jpg|gif|png'`中的内容，并且对 `Content-Type`做了限制，所以我们可以利用 `shell.gif.ph*p`来作为文件名来上传，利用二次渲染的GIF图片马，达到 getshell 的目的

