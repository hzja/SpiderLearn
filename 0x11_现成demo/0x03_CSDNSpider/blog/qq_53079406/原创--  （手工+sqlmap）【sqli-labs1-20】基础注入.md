# 原创
：  （手工+sqlmap）【sqli-labs1-20】基础注入

# （手工+sqlmap）【sqli-labs1-20】基础注入

**目录**

[一、手工注入：](#%E4%B8%80%E3%80%81%E6%89%8B%E5%B7%A5%E6%B3%A8%E5%85%A5%EF%BC%9A)

[二、sqlmap注入](#%E4%BA%8C%E3%80%81sqlmap%E6%B3%A8%E5%85%A5)

---


## 一、手工注入：

> 


[【sqli-labs靶场1-4】GET请求、错误注入、单引号、双引号、括号闭合、字符型、整型<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124964170](https://blog.csdn.net/qq_53079406/article/details/124964170)

[【sqli-labs5-6】GET方法、单双引号、报错注入：基本步骤、错误注入过程<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125015773](https://blog.csdn.net/qq_53079406/article/details/125015773)
[【sqli-labs7】GET请求、文件读写注入：使用方法<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125038406](https://blog.csdn.net/qq_53079406/article/details/125038406)
[【sqli-labs8-10】盲注：布尔盲注、时间盲注<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125638629](https://blog.csdn.net/qq_53079406/article/details/125638629)
[【sqli-labs11-12】POST注入：基本步骤、示例<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125655261](https://blog.csdn.net/qq_53079406/article/details/125655261)
[【sqli-labs13-14】POST注入：报错回显（基本步骤）<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125660497](https://blog.csdn.net/qq_53079406/article/details/125660497)
[【sqli-labs15-16】POST注入：布尔/时间盲注<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125666908](https://blog.csdn.net/qq_53079406/article/details/125666908)
[【sqli-labs17】update注入：原理、利用过程<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125676906](https://blog.csdn.net/qq_53079406/article/details/125676906)
[【sqli-labs18-19】Header注入：原理、利用过程<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125705459](https://blog.csdn.net/qq_53079406/article/details/125705459)
[【sqli-labs20】cookie注入:原理、利用过程<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125708073](https://blog.csdn.net/qq_53079406/article/details/125708073)


---


---


## 二、sqlmap注入

> 
[【sqli-labs靶场1-4】GET请求、错误注入、单引号、双引号、括号闭合、字符型、整型<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/124976294](https://blog.csdn.net/qq_53079406/article/details/124976294)[【sqli-labs5-6】GET方法、单双引号、报错注入<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125023495](https://blog.csdn.net/qq_53079406/article/details/125023495)[【sqli-labs7】GET请求、文件读写注入：使用方法<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125064753](https://blog.csdn.net/qq_53079406/article/details/125064753)[【sqli-labs8-10】盲注：布尔盲注、时间盲注<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125647160](https://blog.csdn.net/qq_53079406/article/details/125647160)[【sqli-labs11-20】爆破本地数据文件<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125658889](https://blog.csdn.net/qq_53079406/article/details/125658889)

