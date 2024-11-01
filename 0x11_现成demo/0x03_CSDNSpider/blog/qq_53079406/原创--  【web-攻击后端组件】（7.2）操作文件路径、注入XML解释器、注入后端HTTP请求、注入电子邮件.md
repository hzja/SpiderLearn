# 原创
：  【web-攻击后端组件】（7.2）操作文件路径、注入XML解释器、注入后端HTTP请求、注入电子邮件

# 【web-攻击后端组件】（7.2）操作文件路径、注入XML解释器、注入后端HTTP请求、注入电子邮件

**目录**

[一、操作文件路径](#%E4%B8%80%E3%80%81%E6%93%8D%E4%BD%9C%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[ 路径遍历漏洞：](#%C2%A0%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E%EF%BC%9A)

[文件包含漏洞：](#%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E6%BC%8F%E6%B4%9E%EF%BC%9A)

[二、注入XML解释器](#%E4%BA%8C%E3%80%81%E6%B3%A8%E5%85%A5XML%E8%A7%A3%E9%87%8A%E5%99%A8)

[三、注入后端HTTP请求](#%E4%B8%89%E3%80%81%E6%B3%A8%E5%85%A5%E5%90%8E%E7%AB%AFHTTP%E8%AF%B7%E6%B1%82)

[四、注入电子邮件](#%E5%9B%9B%E3%80%81%E6%B3%A8%E5%85%A5%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6%EF%BC%9A)

---


## 一、操作文件路径

> 
<h3>简述：</h3>
Web应用程序中的许多功能通常都需要处理用户以文件或目录名提交的输入。一般情况下，这些输入会传递给接受文件路径的API（如用于检索本地文件系统中的文件）。应用程序将在它对用户请求的响应中处理该API调用的结果。如果用户提交的输人未经过正确确认， 这种行为就可能导致各种安全漏洞， 最常见的是文件路径遍历漏洞和文件包含漏洞


> 
<h3> 路径遍历漏洞：</h3>
[【路径遍历漏洞】查找、利用、预防<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/126428076?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/126428076?spm=1001.2014.3001.5501)
<h3>文件包含漏洞：</h3>
[【文件包含漏洞】简介、原理、危害、分类、函数、伪协议、利用过程……<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124059321?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166089586316782248575650%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=166089586316782248575650&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124059321-null-null.nonecase&amp;utm_term=%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124059321?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166089586316782248575650%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=166089586316782248575650&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124059321-null-null.nonecase&amp;utm_term=%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB&amp;spm=1018.2226.3001.4450)


### 文件包含漏洞：

---


---


> 
<h2>二、注入XML解释器</h2>
[【XML漏洞专题】必备的基础知识、利用原理、构建规则<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124360513?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166099819416782248543923%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=166099819416782248543923&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124360513-null-null.nonecase&amp;utm_term=39.1&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/124360513?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166099819416782248543923%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=166099819416782248543923&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-124360513-null-null.nonecase&amp;utm_term=39.1&amp;spm=1018.2226.3001.4450)


---


---


> 
<h2>三、注入后端HTTP请求</h2>
[【注入后端HTTP请求】服务器端HTTP重定向、HTTP参数注入<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/126444127?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/126444127?spm=1001.2014.3001.5501)


---


---


> 
<h2>四、注入电子邮件</h2>
[【注入电子邮件】SMTP命令漏洞查找、注入、防止<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/126448886?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/126448886?spm=1001.2014.3001.5501)

