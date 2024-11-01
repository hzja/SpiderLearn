# 原创
：  【漏扫工具】WPscan简介、下载、更新漏洞库、用法

# 【漏扫工具】WPscan简介、下载、更新漏洞库、用法

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、下载：](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[三、更新漏洞库](#%E4%B8%89%E3%80%81%E6%9B%B4%E6%96%B0%E6%BC%8F%E6%B4%9E%E5%BA%93)

[四、用法：wpscan [选项]](#%E5%9B%9B%E3%80%81%E7%94%A8%E6%B3%95%EF%BC%9Awpscan%20%5B%E9%80%89%E9%A1%B9%5D)

[-h](#-h)

[-v](#-v)

[-o](#-o)

[-f](#-f)

[-t](#-t)

[-e](#-e)

[-P](#-P)

[-U](#-U)

---


## 一、简介：

> 
WPScan是Kali Linux默认自带的一款漏洞扫描工具，它采用Ruby编写
能够扫描WordPress网站中的多种安全漏洞，其中包括主题漏洞、插件漏洞和WordPress本身的漏洞。它不仅能够扫描类似robots.txt这样的敏感文件，而且还能够检测当前已启用的插件和其他功能。






---


---


## 二、下载：

> 
 GitHub下载：
[wpscanteam/wpscan: WPScan WordPress security scanner. Written for security professionals and blog maintainers to test the security of their WordPress websites. (github.com)<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/wpscanteam/wpscan](https://github.com/wpscanteam/wpscan)
输入
git clone https://github.com/wpscanteam/wpscan.git



---


---


## 三、更新漏洞库

> 
 wpscan --update



---


---


## 四、用法：wpscan [选项]

> 
--url URL
博客扫描的URL允许的协议：http，https默认协议如果没有提供：http此选项是强制性的

 


> 
<h3>-h</h3>
--help                                    
显示简单的帮助和退出
<hr/>
--hh                                      
显示全部帮助和退出
<hr/>
--version                                
显示版本和退出


---


> 
<h3>-v</h3>
--verbose                                
详细模式
<hr/>
--[no-]banner                      
是否显示横幅<br/> 默认值：正确
     


> 
<h3>-o</h3>
--output FILE                            
输出到文件


> 
<h3>-f</h3>
--format FORMAT                          
输出结果以提供的格式
可用选择：Cli-No-Colour，Cli-No-Color，JSON，CLI
<hr/>
--detection-mode MODE              
默认值: mixed
可用选择：mixed, passive, aggressive（混合，被动，侵略性）
<hr/>
--user-agent, --ua VALUE
<hr/>
--random-user-agent, --rua
每次扫描使用随机的用户代理          
<hr/>
--http-auth login:password


---


---


> 
<h3>-t</h3>
--max-threads VALUE                      
最大线程要使用<br/> 默认值：5
<hr/>
--throttle MilliSeconds          
毫秒等待，然后再执行另一个Web请求。如果使用，最大线程将设置为1。        
<hr/>
--request-timeout SECONDS                
请求超时在几秒钟内<br/> 默认值：60
<hr/>
--connect-timeout SECONDS                
连接超时以秒为单位<br/> 默认值：30
<hr/>
--disable-tls-checks                      
禁用SSL/TLS证书验证，并降级为TLS1.0+（后者需要cURL 7.66）
<hr/>
--proxy protocol://IP:port                
支持的协议取决于已安装的cURL
<hr/>
--proxy-auth login:password
<hr/>
--cookie-string COOKIE                
cookie字符串要在请求中使用，格式：cookie1 = value1 [; cookie2 = value2]
<hr/>
--cookie-jar FILE-PATH              
文件读写cookie<br/> 默认值：/tmp/wpscan/cookie_jar.txt
<hr/>
--force                
请勿检查目标是运行WordPress还是返回403
<hr/>
--[no-]update                            
是否更新数据库
<hr/>
--api-token TOKEN                        
WPSCAN API令牌显示漏洞数据，可从https://wpscan.com/profile获得
<hr/>
--wp-content-dir DIR              
wp-content目录（如果习惯或未检测到），例如“ WP-content”
<hr/>
--wp-plugins-dir DIR                      
插件目录如果自定义或未检测到，例如“ WP-CONTENT/插件”


---


---


---


---


---


---


> 
<h3>-e</h3>
--enumerate [OPTS]
枚举过程可用选择：
vp   脆弱的插件
ap   所有插件
p    流行插件
vt   脆弱的主题
at   所有主题
t    受欢迎的主题
tt   Timthumbs                       
cb   配置备份
dbe  Db 出口
u    
用户IDS范围。例如：U1-5<br/> 使用范围分隔符：' - '<br/> 如果没有提供参数，则价值：1-10
m    
媒体IDS范围。例如M1-15<br/> 注意：必须将固定链接设置设置为“平原”才能检测到那些<br/> 使用范围分隔符：' - '<br/> 值如果没有提供任何参数：1-100<br/> 分离器在值之间使用：'，'<br/> 默认值：所有插件，配置备份<br/> 值如果没有提供参数，则值：VP，VT，TT，CB，DBE，U，M<br/> 不兼容的选择（每组/S中只能使用一个）：
- vp, ap, p
- vt, at, t
<hr/>
--exclude-content-based REGEXP_OR_STRING  
排除枚举部分期间与RegexP（情况不敏感）匹配的所有响应。<br/> 总体和身体都被检查。不需要RegexP定界符。
<hr/>
--plugins-detection MODE                  
使用提供的模式来枚举插件。<br/> 默认值：被动<br/> 可用选择：mixed, passive, aggressive（混合，被动，侵略性）
<hr/>
--plugins-version-detection MODE          
使用提供的模式检查插件的版本。
默认值：mixed（混合）
可用选择：mixed, passive, aggressive（混合，被动，侵略性）
<hr/>
--exclude-usernames REGEXP_OR_STRING      
排除匹配RegexP/String（情况不敏感）的用户名。不需要RegexP定界符。


---


---


> 
<h3>-P</h3>
--passwords FILE-PATH          
密码攻击期间要使用的密码列表。如果没有提供 - 使用选项，则将运行用户枚举。          


> 
<h3>-U</h3>
--usernames LIST        
密码攻击期间要使用的用户名列表。示例：“ A1”，“ A1，A2，A3'，'/tmp/a.txt'
<hr/>
--multicall-max-passwords MAX_PWD        
使用XMLRPC Multicall发送请求发送的最大密码数
默认 : 500
<hr/>
--password-attack ATTACK        
迫使提供的攻击要被使用，而不是自动确定。可用选择： wp-login, xmlrpc, xmlrpc-multicall
<hr/>
--login-uri URI        
登录页面的URI如果不同于 /wp-login.php
<hr/>
--stealthy       
 - 随机 - 用户 - 代理 - 检测模式无源 -  plugins-version-vertection被动


---


---

