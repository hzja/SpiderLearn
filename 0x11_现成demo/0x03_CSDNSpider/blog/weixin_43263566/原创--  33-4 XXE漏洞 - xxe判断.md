# 原创
：  33-4 XXE漏洞 - xxe判断

# 33-4 XXE漏洞 - xxe判断

#### **判断是否存在 XXE 攻击漏洞：**

##### **1）有源码情况：**

##### **2）无源码情况：**

 <img alt="" height="686" src="https://img-blog.csdnimg.cn/direct/74d344b4cc5d420d96ea3e43eb4c8d4e.png" width="1092"/>

##### 3）直接传递 XML 代码并检测服务器是否支持外部实体 

```
&lt;?xml version="1.8" encoding="ISO-8859-1"?&gt;
&lt;!DOCTYPE poc [
   &lt;!ENTITY shell "xxe"&gt;]&gt;

&lt;!-- 引用实体 --&gt;
&amp;shell;
```
