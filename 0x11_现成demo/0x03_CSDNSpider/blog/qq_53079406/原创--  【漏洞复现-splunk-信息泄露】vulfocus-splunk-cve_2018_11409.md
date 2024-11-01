# 原创
：  【漏洞复现-splunk-信息泄露】vulfocus/splunk-cve_2018_11409

# 【漏洞复现-splunk-信息泄露】vulfocus/splunk-cve_2018_11409

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
123.58.224.8:56459
123.58.224.8:50009
123.58.224.8:27643
123.58.224.8:50147

 123.58.224.8:50009
admin/changeme

 然后需要改密码

选择默认的最下面一项

点击取消
<img alt="" height="581" src="https://img-blog.csdnimg.cn/3d2e87547d0c41a599866f50de6fe29a.png" width="1200"/> 
然后就进入到主页面
<img alt="" height="922" src="https://img-blog.csdnimg.cn/7359e9c5c0a94b98b6952142af09ffdc.png" width="1200"/> 


> 
<h3>1.2、知识:</h3>
1、测试页面的功能点
（此题的解题属于是有点大无语事件）
2、寻找未验证的接口


> 
<h3>1.3、描述：</h3>
Splunk 7.0.1及之前版本中存在安全漏洞。攻击者可通过将__raw/services/server/info/server-info?output_mode=json添加到查询中利用该漏洞泄露信息


---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
方法一：
第一步肯定都是测试功能点
设置 -----&gt; 添加数据

 监视 -----&gt; 文件和目录------&gt;浏览

<img alt="" height="768" src="https://img-blog.csdnimg.cn/4e2c86bd6d0d448ca5892f9a87f0219d.png" width="1200"/> 然后就可以读取到文件目录了
就get到了flag
<img alt="" height="884" src="https://img-blog.csdnimg.cn/c81b4ac92ddd457fb9aa4426b4b648a4.png" width="1200"/> 
<hr/>
方法二：
CVE给出的POC
http://ip:port/en-US/splunkd/__raw/services/server/info/server-info?output_mode=json

