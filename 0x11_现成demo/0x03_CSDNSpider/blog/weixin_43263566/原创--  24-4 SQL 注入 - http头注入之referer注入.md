# 原创
：  24-4 SQL 注入 - http头注入之referer注入

# 24-4 SQL 注入 - http头注入之referer注入

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

####  一、Referer注入条件：

1. 使用了HTTP头的Referer；
1. 没有对Referer进行过滤；
1. 使用Referer进行SQL操作实验演示，例如Less-19

```
&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;
&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;head&gt;
&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8" /&gt;
&lt;title&gt;Less-19 Header Injection- Referer- Error Based- string&lt;/title&gt;
&lt;/head&gt;

&lt;body bgcolor="#000000"&gt;

&lt;div style=" margin-top:20px;color:#FFF; font-size:24px; text-align:center"&gt; Welcome&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;font col
```
