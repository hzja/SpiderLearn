# 原创
：  快速检测 GlassFish 任意文件读取漏洞的 Python 脚本

# 快速检测 GlassFish 任意文件读取漏洞的 Python 脚本

**部分数据来源：**ChatGPT

#### 引言

        当下，互联网安全问题正愈发严重，黑客利用各种漏洞进行攻击的频率也在持续增加。在2015年10月，一位名为“路人甲”的安全研究员在乌云上公开了一个名为“应用服务器glassfish存在通用任意文件读取漏洞”的漏洞（编号：wooyun-2010-0144595），该漏洞可以导致攻击者可以读取网站上任意文件，包括配置文件、密码文件等敏感信息。[应用服务器glassfish任意文件读取漏洞 - SecPulse.COM | 安全脉搏](https://www.secpulse.com/archives/42277.html)

### 漏洞描述

        该漏洞主要影响使用Java应用服务器GlassFish的网站，攻击者可以通过访问特定的URL来读取任意文件，包括敏感数据文件。具体而言，在发送请求时，攻击者可以将路径参数中的特殊字符进行编码，从而绕过路径校验，读取任意文件。

#### 例如，以下URL即可触发该漏洞：

url最后的/etc/passwd就是要读取的文件

```
http://localhost:4848/theme/META-INF/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd
```
