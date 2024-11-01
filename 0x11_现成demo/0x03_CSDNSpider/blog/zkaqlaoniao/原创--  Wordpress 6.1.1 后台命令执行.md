# 原创
：  Wordpress 6.1.1 后台命令执行

# Wordpress 6.1.1 后台命令执行

## 0x01 前言

<br/> WordPress是使用PHP语言开发的博客平台，用户可以在支持PHP和MySQL数据库的服务器上架设属于自己的网站。也可以把 WordPress当作一个内容管理系统（CMS）来使用。WordPress是一款个人博客系统，并逐步演化成一款内容管理系统软件，它是使用PHP语言和MySQL数据库开发的，用户可以在支持 PHP 和 MySQL数据库的服务器上使用自己的博客。WordPress有许多第三方开发的免费模板，安装方式简单易用。不过要做一个自己的模板，则需要你有一定的专业知识。比如你至少要懂的标准通用标记语言下的一个应用HTML代码、CSS、PHP等相关知识。WordPress官方支持中文版，同时有爱好者开发的第三方中文语言包，如wopus中文语言包。WordPress拥有成千上万个各式插件和不计其数的主题模板样式。

wordpress网址：https://cn.wordpress.org/<br/> 受影响的版本：6.1.1<br/> 问题源码文件：wp-admin/update.php<br/> 行数：149

当变量action相等于upload-plugin的时候进入elseif循环语句内<br/> 在168行开始获取文件名<br/> 在182行，调用install函数，这个函数是用户自定义函数，定位下

来到这里，可以看到这个函数，是用来安装插件的

来到169行，全文追踪new_plugin_data这个函数

来看86行，这是获取插件的版本和名称，然后直接进入118行，<br/> 88-98行不用看，这是更新插件和插件降级的，<br/> 开始安装插件，但是却没有过滤危险函数，导致系统命令执行漏洞，来复现下漏洞

插件-&gt;上传插件-&gt;触发命令执行漏洞

首先先准备个恶意插件

这个插件可以在官网下载

准备好恶意插件后，来到后台-&gt;上传插件的地方

上传插件，插件上传完后成功返回phpinfo

## 0x02 CNVD证书

## <br/> 等了两个月才归档的证书。修复建议：卸载经典编辑器插件

## 扫码白嫖视频+工具+进群+靶场等资料

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/487799c8954446d2a796d7a302b2a0f4.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/48d5527af27a4db2b1c5761145e4570e.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/36b43da29a154e6185fb1dbf85b4d708.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/1d1e7d9d92a54b94a5762af2e34f55ca.png" width="665"/>

应急响应笔记

学习路线

 
