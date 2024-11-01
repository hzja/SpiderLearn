# 原创
：  【文件上传-配置文件】crossdomain.xml跨域策略配置文件上传

# 【文件上传-配置文件】crossdomain.xml跨域策略配置文件上传

**目录**

[一、0x00 前言](#%E4%B8%80%E3%80%810x00%20%E5%89%8D%E8%A8%80)

[二、基础知识](#%E4%BA%8C%E3%80%81%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86)

[1、Flash](#1%E3%80%81Flash%EF%BC%9A)

[2、crossdomain.xml文件](#2%E3%80%81crossdomain.xml%E6%96%87%E4%BB%B6%EF%BC%9A)

[3、crossdomain.xml格式](#3%E3%80%81crossdomain.xml%E6%A0%BC%E5%BC%8F)

[4、crossdomain.xml相关参数](#%C2%A04%E3%80%81crossdomain.xml%E7%9B%B8%E5%85%B3%E5%8F%82%E6%95%B0)

[三、漏洞利用](#%E4%B8%89%E3%80%81%E6%BC%8F%E6%B4%9E%E5%88%A9%E7%94%A8)

[1、方法：](#1%E3%80%81%E6%96%B9%E6%B3%95%EF%BC%9A)

[2、上传漏洞配置文件](#%C2%A02%E3%80%81%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6)

---


## 一、0x00 前言

在很多地方都会见查是否跨域

比如某些特定的步骤、CSRF、flash跨域劫持等链接

---


---


## 二、基础知识

> 
<h3>1、Flash</h3>
由于HTML语言的功能十分有限，无法达到人们的预期设计，以实现令人耳目一新的动态效果，在这种情况下，各种脚本语言应运而生，使得网页设计更加多样化。然而，程序设计总是不能很好地普及，因为它要求一定的编程能力，而人们更需要一种既简单直观又有功能强大的动画设计工具，而Flash的出现正好满足了这种需求。
<h3>​</h3>


### ​

> 
<h3>2、crossdomain.xml文件</h3>
一般在根目录下（在根目录下的配置文件称为“主策略文件”）。
若在根目录不存在主策略文件，则该域将禁止任何第三方域的flash跨域请求。


> 
<h3>3、crossdomain.xml格式</h3>
<pre><code>&lt;?xml version="1.0"?&gt;

&lt;cross-domain-policy&gt;
&lt;allow-access-from domain="www.xxx.com" /&gt;
&lt;/cross-domain-policy&gt;</code></pre>
其中www.xxx.com是可信任的域名


> 
<h3>4、crossdomain.xml相关参数</h3>
1、site-control标签（属性permitted-cross-domain-policies）
<pre><code>属性值：
none:             不允许使用loadPolicyFile方法加载任何策略文件，包括此主策略文件。
master-only:      只允许使用主策略文件[默认值]。
by-content-type:  只允许使用loadPolicyFile方法加载HTTP/HTTPS协议下Content-Type 为text/x-cross-domain-policy的文件作为跨域策略文件。文章来源地址:https://www.yii666.com/article/504083.html
by-ftp-filename:  只允许使用loadPolicyFile方法加载FTP协议下文件名为crossdomain.xml的文件作为跨域策略文件。
all:              可使用loadPolicyFile方法加载目标域上的任何文件作为跨域策略文件


示例：
&lt;cross-domain-policy&gt;
&lt;site-control permitted-cross-domain-policies="by-content-type"/&gt;
&lt;/cross-domain-policy&gt;</code></pre>

<hr/>
2、allow-access-from标签
<pre><code>属性值：
domain：    指定某IP地址、域或通配符域（任何域）
to-ports：  指定允许访问读取本域内容的socket连接端口范围（如to-ports="1100,1120-1125"，也可使用通配符（*）表示允许所有端口）
secure：    指明信息是否经加密传输。当crossdomain.xml文件使用https加载时，secure默认设为true


示例：
&lt;cross-domain-policy&gt;
&lt;allow-access-from domain="*.baidu.com" secure="true" /&gt;
&lt;/cross-domain-policy&gt;</code></pre>

<hr/>
3、allow-access-from-identity标签
该节点配置跨域访问策略为允许有特定证书的来源跨域访问本域上的资源
<pre><code>&lt;allow-access-from-identity&gt;
&lt;signatory&gt;
&lt;certificate
fingerprint="04:ac:……格式的证书"
fingerprint-algorithm="sha-1"/&gt;
&lt;/signatory&gt;
&lt;/allow-access-from-identity&gt;</code></pre>
<hr/>
4、allow-http-request-headers-from标签
此节点授权第三方域flash向本域发送用户定义的http头
<pre><code>属性值：
domain：     与allow-access-from中的domain相同
headers：    表明允许发送的http头。可用通配符（*）（以逗号隔开的列表）
secure：     与allow-access-from中的secure相同

示例：
&lt;cross-domain-policy&gt;
&lt;allow-http-request-headers-from domain="*" headers="*" /&gt;
&lt;/cross-domain-policy&gt;</code></pre>




---


---


---


## 三、漏洞利用

> 
<h3>1、方法：</h3>
1、找到任意文件上传点（先测试能否getshell）
2、若无法getshell（尝试xss）
3、若无法xss（尝试上传配置文件）
上传配置文件是我们最后的选择


> 
<h3>2、上传漏洞配置文件</h3>
如下crossdomain.xml文件就存在漏洞
（尝试上传存在漏洞配置文件到根目录）
<pre><code>&lt;?xml version="1.0"?&gt;

&lt;cross-domain-policy&gt;
&lt;allow-access-from domain="*" /&gt;
&lt;/cross-domain-policy&gt;</code></pre>
从*就可以看出存在漏洞了



