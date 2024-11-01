# 原创
：  13-4 tomcat PUT任意方法写文件

# 13-4 tomcat PUT任意方法写文件

#### 漏洞介绍

        该漏洞是Apache Tomcat服务器中的PUT方法任意写文件漏洞，可以让攻击者上传Webshell并获取服务器权限。

        该漏洞在2017年9月19日被Apache官方发布并修复[CVE-2017-12615](https://tomcat.apache.org/security-7.html#Fixed_in_Apache_Tomcat_7.0.81)。在conf/web.xml文件中，readonly默认为true，当设置为false时，可以通过PUT / DELETE进行文件操作，但jsp后缀的上传受到限制。

关于利用Tomcat漏洞的一些技术细节：

1.  使用%20绕过：将文件名中的空格替换为%20，即可实现绕过的效果。 
1.  在jsp后缀后面添加**/**：因为**/**在文件名中是非法的，在Windows和Linux系统中会自动去除。例如，在上传文件名为111.jsp的文件时，可使用111.jsp**/**作为文件名进行上传。 
1.  使用Windows NTFS流：在jsp后缀后面添加:$DATA，可以实现将文件写入到Windows NTFS流中的效果。 

#### **vmihub靶场搭建（**
