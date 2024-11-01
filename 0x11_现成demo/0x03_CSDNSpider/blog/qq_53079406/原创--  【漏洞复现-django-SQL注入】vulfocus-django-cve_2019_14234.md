# 原创
：  【漏洞复现-django-SQL注入】vulfocus/django-cve_2019_14234

# 【漏洞复现-django-SQL注入】vulfocus/django-cve_2019_14234

**目录**

[一、靶场环境](#%E4%B8%80%E3%80%81%E9%9D%B6%E5%9C%BA%E7%8E%AF%E5%A2%83)

[1.1、平台：](#1.1%E3%80%81%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、知识:](#1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E7%89%88%E6%9C%AC%3A)

[1.3、描述：](#1.3%E3%80%81%E6%8F%8F%E8%BF%B0%EF%BC%9A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.4、解题：](#2.4%E3%80%81%E8%A7%A3%E9%A2%98%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[Vulfocus 漏洞威胁分析平台](https://vulfocus.cn/)
123.58.224.8:23290

 
（如果显示连接超时也是正常的，继续往后看）

 

1


> 
<h3>1.2、知识:</h3>
1、参数带入（白盒更容易分析参数，黑盒就在数据包里面看看运气）
源码分析，如果在Django中使用了JSONField并且查询的“键名”可控，就可以进行SQL注入
2、路径
源码审计，路径可以方便得到。黑盒的话，也得分析数据包，看天吃饭了



> 
<h3>1.3、描述：</h3>
Django是一款广为流行的开源web框架，由Python编写，许多网站和app都基于Django开发。Django采用了MTV的框架模式，即模型M，视图V和模版T，使用Django，程序员可以方便、快捷地创建高品质、易维护、数据库驱动的应用程序。而且Django还包含许多功能强大的第三方插件，使得Django具有较强的可扩展性。
该漏洞需要开发者使用了JSONField/HStoreField，且用户可控queryset查询时的键名，在键名的位置注入SQL语句


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
URL后面上加上
/admin/
从右上角可以看出已经处于登陆状态了

 
此时URL输入为
http://ip:port/admin/vuln/collection/
(这一看就是查询的地方)

 /admin/vuln/collection/?detail__a'b=1<img alt="" height="826" src="https://img-blog.csdnimg.cn/74f76bfb1fcf41c787f79b1dfff2eeff.png" width="1200"/>
 
<hr/>
其他思路：
1、考虑使用 or 1=1 永真带出数据
2、使用DNSLog带外


> 
<h3>2.4、解题：</h3>



