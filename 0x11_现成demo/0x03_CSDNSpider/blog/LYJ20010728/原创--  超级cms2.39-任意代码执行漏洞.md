# 原创
：  超级cms2.39-任意代码执行漏洞

# 超级cms2.39-任意代码执行漏洞

#### 超级CMS2.39-文件上传漏洞

## 环境搭建

> 
- 下载超级CMS V2.39，[下载地址](http://www.chaojicms.com/)- 使用phpstudy搭建web环境- 把下载好的源码放到网站根目录下，开启phpstudy，浏览器访问安装后即可


## 漏洞复现

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621015059869.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621015108133.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621015113713.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70"/>

## 漏洞分析

> 
超级cms后台未对文件内容编辑做限制，所以我们可以利用文件管理器对其文件内容进行任意的编辑，来达到getshell的目的

