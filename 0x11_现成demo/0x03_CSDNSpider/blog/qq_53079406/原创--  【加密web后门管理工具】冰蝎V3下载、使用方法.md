# 原创
：  【加密web后门管理工具】冰蝎V3下载、使用方法

# 【加密web后门管理工具】冰蝎V3下载、使用方法

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、下载](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD)

[2.1、GitHub下载：](#2.1%E3%80%81GitHub%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[三、使用方法](#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)

[ 3.1、第一步：上传shell.php](#%C2%A03.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E4%B8%8A%E4%BC%A0shell.php)

[3.2、第二步：打开客户端](#3.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%89%93%E5%BC%80%E5%AE%A2%E6%88%B7%E7%AB%AF)

[3.3、第三步：连接](#3.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%BF%9E%E6%8E%A5)

[3.4、第四步：操作](#3.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%93%8D%E4%BD%9C)

[ 3.5、shell.php密码修改](#%C2%A03.5%E3%80%81shell.php%E5%AF%86%E7%A0%81%E4%BF%AE%E6%94%B9)

---


## 一、简介：

> 
冰蝎Shell管理工具是一款流行的、采用二进制动态加密传输数据的网站管理工具。
<hr/>
找到Web站点漏洞后，通常会在Web站点上传WebShell程序，从而实现对目标站点的控制。
加密WebShell防止被发现，由于流量加密，传统的WAF、WebIDS设备难以检测


---


---


## 二、下载

> 
<h3>2.1、GitHub下载：</h3>
[Releases · rebeyond/Behinder (github.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/rebeyond/Behinder/releases](https://github.com/rebeyond/Behinder/releases)




---


---


## 三、环境

> 
 需要JDK6-8
[jdk安装，环境配置，验证是否成功解决“不是内部或外部命令<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/122806725?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165295586316780357234458%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165295586316780357234458&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-122806725-null-null.nonecase&amp;utm_term=JDK&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/122806725?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165295586316780357234458%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165295586316780357234458&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-122806725-null-null.nonecase&amp;utm_term=JDK&amp;spm=1018.2226.3001.4450)
[【jdk快速设置/切换工具】一键设置/切换、附带插件链接、使用教程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124252949?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165295586316780357234458%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165295586316780357234458&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-124252949-null-null.nonecase&amp;utm_term=JDK&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124252949?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165295586316780357234458%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165295586316780357234458&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-124252949-null-null.nonecase&amp;utm_term=JDK&amp;spm=1018.2226.3001.4450)


---


---


## 四、使用方法

> 
<h3> 4.1、第一步：上传shell.php</h3>
文件在Behinder_v3.0\server中


将shell.php文件上传到网站中（随便找一个本地搭建的）
 <img alt="" height="536" src="https://img-blog.csdnimg.cn/f1208246a4984a0c8d7db6d05c90fea0.png" width="860"/>



> 
<h3>4.2、第二步：打开客户端</h3>
方法一：双击直接打开客户端（java环境配置好了的）
方法二：使用Windows powershell（或者win+R+cmd然后再进入文件夹）



 java -jar Behinder.jar

 <img alt="" height="632" src="https://img-blog.csdnimg.cn/d6b6087cc5c34edf80b7c3136766d28b.png" width="1197"/>



> 
<h3>4.3、第三步：连接</h3>
右键，新增


输入shell所在的URL
上传的shell.php默认密码是rebeyond







> 
<h3>4.4、第四步：操作</h3>
双击

 在里面就可以执行各种操作了




> 
<h3> 4.5、shell.php密码修改</h3>
该密钥为连接密码32位md5值的前16位，默认连接密码rebeyond



修改连接密码
需要修改md5的前16位 
我修改连接密码为123456

即改为
$key="49ba59abbe56e057"; 

