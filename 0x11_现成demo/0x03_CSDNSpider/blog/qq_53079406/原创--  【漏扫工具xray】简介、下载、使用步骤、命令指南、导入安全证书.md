# 原创
：  【漏扫工具xray】简介、下载、使用步骤、命令指南、导入安全证书

# 【漏扫工具xray】简介、下载、使用步骤、命令指南、导入安全证书

**目录**

[一、简介：](#3.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、下载：](#3.2%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[三、使用方法](#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)

[3.1、使用步骤：](#3.1%E3%80%81%E4%BD%BF%E7%94%A8%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[3.1.1、第一步：文件夹中打开Windows powershell（或者cmd进入）](#3.1.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%96%87%E4%BB%B6%E5%A4%B9%E4%B8%AD%E6%89%93%E5%BC%80Windows%20powershell%EF%BC%88%E6%88%96%E8%80%85cmd%E8%BF%9B%E5%85%A5%EF%BC%89)

[3.1.2、第二步：在终端使用XRAY.exe程序](#3.1.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%9C%A8%E7%BB%88%E7%AB%AF%E4%BD%BF%E7%94%A8XRAY.exe%E7%A8%8B%E5%BA%8F)

[3.2、命令指南：](#3.2%E3%80%81%E5%91%BD%E4%BB%A4%E6%8C%87%E5%8D%97%EF%BC%9A)

[3.2.1、单一扫描](#3.2.1%E3%80%81%E5%8D%95%E4%B8%80%E6%89%AB%E6%8F%8F)

[3.2.2、单一扫描、爬取](#3.2.2%E3%80%81%E5%8D%95%E4%B8%80%E6%89%AB%E6%8F%8F%E3%80%81%E7%88%AC%E5%8F%96)

[3.2.3、被动扫描](#3.2.3%E3%80%81%E8%A2%AB%E5%8A%A8%E6%89%AB%E6%8F%8F)

[3.2.4、输出文件格式](#3.2.4%E3%80%81%E8%BE%93%E5%87%BA%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F)

[3.2.5、指定扫描插件](#3.2.5%E3%80%81%E6%8C%87%E5%AE%9A%E6%89%AB%E6%8F%8F%E6%8F%92%E4%BB%B6)

[3.3、支持模块](#3.3%E3%80%81%E6%94%AF%E6%8C%81%E6%A8%A1%E5%9D%97)

[四、导入证书：](#%E5%9B%9B%E3%80%81%E5%AF%BC%E5%85%A5%E8%AF%81%E4%B9%A6%EF%BC%9A)

[4.1、第一步：导出证书](#4.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%AF%BC%E5%87%BA%E8%AF%81%E4%B9%A6)

[4.2、第二步：安装此证书](#4.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%AE%89%E8%A3%85%E6%AD%A4%E8%AF%81%E4%B9%A6)

[4.3、第三步：导入到浏览器](#4.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E5%AF%BC%E5%85%A5%E5%88%B0%E6%B5%8F%E8%A7%88%E5%99%A8)

---


---


 

> 
<h2>一、简介：</h2>
**xray** 是从长亭洞鉴核心引擎中提取出的社区版漏洞扫描神器，支持主动、被动多种扫描方式，自备盲打平台、可以灵活定义 POC，功能丰富，调用简单，支持 Windows / macOS / Linux 多种操作系统，可以满足广大安全从业者的自动化 Web 漏洞探测需求。


> 
<h2>二、下载：</h2>
[Releases · chaitin/xray (github.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/chaitin/xray/releases](https://github.com/chaitin/xray/releases)我在Windows中直接下载exe文件，不想再搭建环境了，哈哈哈


<hr/>
直接点开，提示再终端调用它，不是直接双击打开的






## 三、使用方法

> 
<h3>3.1、使用步骤：</h3>
<h4>3.1.1、第一步：文件夹中打开Windows powershell（或者cmd进入）</h4>
空白处右键（或者按住shift再右键）
 <img alt="" height="499" src="https://img-blog.csdnimg.cn/2f6539e292714eb9a1d356da04d35b5f.png" width="1185"/> 
<hr/>

<h4>3.1.2、第二步：在终端使用XRAY.exe程序</h4>
（exe文件名字别打错了）
我这输入的是：
.\xray_windows_amd64.exe webscan --url 127.0.0.1
更多命令请看后面
 <img alt="" height="892" src="https://img-blog.csdnimg.cn/5221d602ba444a23931fa7b20e690f02.png" width="1200"/> 



#### 3.1.2、第二步：在终端使用XRAY.exe程序

> 
<h3>3.2、命令指南：</h3>
<h4>3.2.1、单一扫描</h4>
只扫描单一URL（不爬虫）
xray webscan --url URL（网址）
<hr/>
<h4>3.2.2、单一扫描、爬取</h4>
爬虫、扫描一个指定的URL
 使用基础爬虫爬取并对爬虫爬取的链接进行漏洞扫描
xray webscan --basic-crawler URL（网址） 
<hr/>
<h4>3.2.3、被动扫描</h4>
使用 HTTP 代理进行被动扫描
xray webscan --listen 127.0.0.1:7777 --html-output proxy.html
设置浏览器 http 代理为 http://127.0.0.1:7777，就可以自动分析代理流量并扫描。
（需要我们导入 xray 运行目录下的`ca.crt`证书到浏览器里面）
<hr/>
<h4>3.2.4、输出文件格式</h4>
输出文件的形式（直接加在命令后面）
无参数：输出到控制台的标准输出
--text-output 文件名.text：输出到文本文件中
--json-output 文件名.json：输出到 JSON 文件中
--html-output 文件名.html：输出到 HTML 文件中

<hr/>

<h4>3.2.5、指定扫描插件</h4>
 手动指定本次运行的插件，多个插件之间可使用逗号分隔
默认情况下，将会启用所有内置插件，可以使用下列命令指定本次扫描启用的插件。
 xray webscan --plugins cmd-injection,sqldet --url http://example.com
xray webscan --plugins cmd-injection,sqldet --listen 127.0.0.1:7777


#### 3.2.2、单一扫描、爬取

---


#### 3.2.4、输出文件格式

---


> 
<h3>3.3、支持模块</h3>



---


---


## 四、导入证书：

> 
<h3>4.1、第一步：导出证书</h3>
genca导出证书
.\xray_windows_amd64.exe genca
 <img alt="" height="335" src="https://img-blog.csdnimg.cn/9597851f6c7e4d5ca65cd14af290b9fe.png" width="1140"/> 
导出的证书将会在.\xray_windows_amd64.exe同一个目录里面
 <img alt="" height="346" src="https://img-blog.csdnimg.cn/8ac715c54e454dbb978022536e88a532.png" width="1043"/> 


> 
<h3>4.2、第二步：安装此证书</h3>
双击ca.crt
 <img alt="" height="740" src="https://img-blog.csdnimg.cn/27d8978d22b949abb1f9694138a11320.png" width="1200"/> 

导入全部点下一步基本上就可以了 <img alt="" height="785" src="https://img-blog.csdnimg.cn/180fe42798fa404492ed60ade9bff027.png" width="750"/> 


 <img alt="" height="784" src="https://img-blog.csdnimg.cn/8e4d3137045d4a4fa79c341a21e83ba4.png" width="755"/> 

 <img alt="" height="784" src="https://img-blog.csdnimg.cn/5ebb35b2ea26416b8dc0c56b4827781f.png" width="758"/> 

 <img alt="" height="205" src="https://img-blog.csdnimg.cn/b7d033b6d0ee4e23bd31a2395b6d7ff9.png" width="193"/> 


> 
<h3>4.3、第三步：导入到浏览器</h3>
浏览器设置中直接搜证书
 <img alt="" height="608" src="https://img-blog.csdnimg.cn/1eb66988104e4903b303e0db22df98ed.png" width="1200"/> 
 <img alt="" height="565" src="https://img-blog.csdnimg.cn/a61772bc24794e22b45bb5a45b0cda8a.png" width="781"/> 
到目录中找到刚刚导出的证书，然后选中
 <img alt="" height="537" src="https://img-blog.csdnimg.cn/42f5eb5447984c889513b2ca42a696e3.png" width="759"/> 

勾选信任
 <img alt="" height="553" src="https://img-blog.csdnimg.cn/843c4b54720d448794b55357772146d0.png" width="769"/> 
然后就可以用XRAY来代理浏览器了
可以进行被动扫描

