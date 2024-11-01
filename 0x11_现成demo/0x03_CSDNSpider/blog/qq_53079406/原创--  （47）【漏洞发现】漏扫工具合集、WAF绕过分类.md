# 原创
：  （47）【漏洞发现】漏扫工具合集、WAF绕过分类

# （47）【漏洞发现】漏扫工具合集、WAF绕过分类

**目录**

[一、漏洞发现](#%E4%B8%80%E3%80%81%E6%BC%8F%E6%B4%9E%E5%8F%91%E7%8E%B0)

[ 1.1、综合漏 扫工具](#%C2%A01.1%E3%80%81%E7%BB%BC%E5%90%88%E6%BC%8F%20%E6%89%AB%E5%B7%A5%E5%85%B7)

[ 1.2、针对性漏 扫工具](#%C2%A01.2%E3%80%81%E9%92%88%E5%AF%B9%E6%80%A7%E6%BC%8F%20%E6%89%AB%E5%B7%A5%E5%85%B7)

[二、WAF绕过](#%E4%BA%8C%E3%80%81WAF%E7%BB%95%E8%BF%87)

[ 2.1、扫描效率](#%C2%A02.1%E3%80%81%E6%89%AB%E6%8F%8F%E6%95%88%E7%8E%87)

[延时](#%E5%BB%B6%E6%97%B6)

[代理池](#%E4%BB%A3%E7%90%86%E6%B1%A0)

[2.2、工具指纹](#2.2%E3%80%81%E5%B7%A5%E5%85%B7%E6%8C%87%E7%BA%B9)

[2.2.1、修改工具指纹特征](#2.2.1%E3%80%81%E4%BF%AE%E6%94%B9%E5%B7%A5%E5%85%B7%E6%8C%87%E7%BA%B9%E7%89%B9%E5%BE%81)

[2.2.2、模拟用户](#2.2.2%E3%80%81%E6%A8%A1%E6%8B%9F%E7%94%A8%E6%88%B7)

[ 2.3、漏洞payload](#%C2%A0%E6%BC%8F%E6%B4%9Epayload)

---


---


 

## 一、漏洞发现

> 
<h3> 1.1、综合漏 扫工具</h3>
[【漏扫工具】awvs、appscan、xray下载、安装、使用方法（附带网盘链接）<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124762050?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124762050?spm=1001.2014.3001.5501)



> 
<h3> 1.2、针对性漏 扫工具</h3>

[【漏扫工具】Struts Scan简介、下载、使用方法<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124789325?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124789325?spm=1001.2014.3001.5501)
[【漏扫工具】WPscan简介、下载、更新漏洞库、用法<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124783450?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124783450?spm=1001.2014.3001.5501)
[【TPscan漏扫工具】Java、python版本下载<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124781463?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124781463?spm=1001.2014.3001.5501)



---


---


## 二、WAF绕过

> 
<h3> 2.1、扫描效率</h3>

<h4>延时</h4>
sqlmap设置扫描的间隔
[直接使用kali Linux等渗透系统中sqlmap，简单的使用入门<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/122999341?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165269927716781683939935%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165269927716781683939935&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-122999341-null-null.nonecase&amp;utm_term=sqlmap&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/122999341?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165269927716781683939935%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165269927716781683939935&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-122999341-null-null.nonecase&amp;utm_term=sqlmap&amp;spm=1018.2226.3001.4450)
awvs设置扫描速度


<hr/>
<h4>代理池</h4>


[快代理 - 企业级代理云服务提供商 (kuaidaili.com)<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://www.kuaidaili.com/](https://www.kuaidaili.com/)
[【proxy_pool搭建】Windows版搭建、Redis依赖环境安装、proxy_pool依赖安装、proxy_pool搭建<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124766778?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124766778?spm=1001.2014.3001.5501)



#### 代理池

> 
<h3>2.2、工具指纹</h3>
<h4>2.2.1、修改工具指纹特征</h4>
eg：爬虫的头部修改为白名单列表里的爬虫特征
<hr/>
<h4>2.2.2、模拟用户</h4>
eg：（来源网络）
<pre><code>import requests 
import time 
headers={ 
'Connection': 'keep-alive', 
'Cache-Control': 'max-age=0', 
'Upgrade-Insecure-Requests': '1', 
#模拟用户Kit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 
#模拟引擎Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html) 
#更多爬虫引擎：https://www.cnblogs.com/iack/p/3557371.html 
'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider-render/2.0; 
+http://www.baidu.com/search/spider.html)', 
'Sec-Fetch-Dest': 'document', 
'Accept': 
'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/si
gned-exchange;v=b3;q=0.9', 
'Sec-Fetch-Site': 'none', 
'Sec-Fetch-Mode': 'navigate', 
'Sec-Fetch-User': '?1', 
'Accept-Encoding': 'gzip, deflate, br', 
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', 
'Cookie': 'xxx',#根据当前访问cookie 
} 
for paths in open('php_b.txt',encoding='utf-8'): 
url='http://192.168.0.103:8081/' 
paths=paths.replace('\n','') 
urls=url+paths 
#如需测试加代理，或加入代理池需加代理 
proxy = { 
'http': '127.0.0.1:7777' 
} 
try: 
code=requests.get(urls,headers=headers,verify=False).status_code 
print(urls+'|'+str(code)) 
if code==200 or code==403: 
print(urls+'|'+str(code)) 
except Exception as err: 
print('connecting error') 
#time.sleep(3)模拟用户需延时  引擎可用可不用（根据请求速度）
</code></pre>


#### 2.2.2、模拟用户

> 
<h3> 2.3、漏洞payload</h3>

[【WAF绕过】基于数据包的构造绕过、触发WAF、WAF分类<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124697406?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124697406?spm=1001.2014.3001.5501)
[【WAF绕过】基于WAF的规则绕过、旁路、云waf、白名单<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124698447?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124698447?spm=1001.2014.3001.5501)
[【WAF绕过】基于工具的使用绕过WAF、WAFNinja、burpsuite、sqlmap、Fuzz/爆破、wafw00f<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://blog.csdn.net/qq_53079406/article/details/124698526?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124698526?spm=1001.2014.3001.5501)


