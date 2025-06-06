# 原创
：  【web-解析目标】（1.2.4）解析应用程序：解析受攻击面

# 【web-解析目标】（1.2.4）解析应用程序：解析受攻击面

**目录**

[解析受攻击面](#%E8%A7%A3%E6%9E%90%E5%8F%97%E6%94%BB%E5%87%BB%E9%9D%A2)

[1.1、解析应用过程](#1.1%E3%80%81%E8%A7%A3%E6%9E%90%E5%BA%94%E7%94%A8%E8%BF%87%E7%A8%8B)

[1.2、分析：](#1.2%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[1.3、基于路径攻击：](#1.3%E3%80%81%E5%9F%BA%E4%BA%8E%E8%B7%AF%E5%BE%84%E6%94%BB%E5%87%BB%EF%BC%9A)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


## 解析受攻击面

> 
<h3>1.1、解析应用过程</h3>
（1）确定全部用户输入入口点， 包括URL、参数、POST数据、oookie和其他由应用程序处理的HITP消息头
<hr/>
（2）分析应用程序使用的查询字符串格式。如果应用程序井未使用标准格式，设法了解它如何通过URL传参。几乎所有定制方案仍然使用名／值模型的某种变化形式．因此要设法了解名／值对如何被封装到已经确定的非标准URL中
<hr/>
(3)确定任何向应用程序处理过程引入用户可控制或其他第三方数据的带外通道
<hr/>
(4)查看应用程序返回的HTTP服务器旗标。注意，在某些情况下， 应用程序的不同区域由不同的后端组件处理，因此可能会收到不同的Server消息头
<hr/>
(5)检查所有定制HTTP消息头或HTML源代码注释中包含的任何其他软件标识符
<hr/>
(6)运行Httprecon工具识别Web服务器
<hr/>
(7)如果获得关于Web服务器和其他组件的详细信息， 搜索其使用的软件版本，在发动攻击前找到可供利用的漏洞
<hr/>
(8)分析应用程序URL列表，确定任何看似重要的文件扩展名、目录或其他提供服务器使用技术相关线索的内容
<hr/>
(9)分析应用程序发布的全部会话令牌的名称， 确定其使用的技术
<hr/>
(10)使用常用技术列表或Google推测服务器所使用的技术， 或者查找其他明显使用相同技术的Web站点和应用程序
<hr/>
(11)在Google上搜索可能属于第三方软件组件的任何不常见的cook记、脚本、HTTP消息头名称。如果发现使用相同组件的应用程序， 对其进行分析， 确定该组件支持的任何其他功能和参数， 并确定目标应用程序是否具有这些功能、使用这些参数。
注： 品牌不同，相同第三方组件可能看上去不一样， 但其核心功能（包括脚本和参数名称）往往并无变化。下载并安装组件， 对其进行分析以充分了解它的功能、查找其中存在的所有漏洞。同时， 查询已知漏洞库， 确定相关组件中存在的所有已知漏洞


---


---


---


---


---


> 
<h3>1.2、分析：</h3>
解析过程的最后一个步骤是确定应用程序暴露的各种受攻击面，以及与每个受攻击面有关的潜在漏洞
<hr/>
客户端确认——服务器没有采用确认检查
数据库交互——SQL注入
文件上传与下载——路径遍历漏洞、保存型跨站点脚本
显示用户提交的数据一跨站脚本
动态项定向——重定向与消息头注人攻击
社交网络功能——用户名枚举、保存型跨站点脚本
登录——用户名枚举、脆弱密码、能使用蛮力
多阶段登录——登录缺陷
会话状态——可推测出的令牌、令牌处理不安全
访问控制——水平权限和垂直权限提升
用户伪装功能——权限提升
使用明文通信——会话劫持、收找证书和其他敏感数据
站外链接——Referer消息头中查询字符串参数泄漏
外部系统接口——处理会话与/或访问控制的快捷方式
错误消息——信息泄漏。
电子邮件交互——电子邮件与命令注入
本地代码组件或交互——缓冲区溢出。
使用第三方应用程序组件——已知漏洞。
已确定的Web服务器软件——常见薄弱配置环节，已知软件程序缺陷


> 
<h3>1.3、基于路径攻击：</h3>
<h4>简介：</h4>
解析应用程序的内容和功能后， 可以通过各种路径对该应用程序实施攻击
使用bp，在网站map中分析每个路径的特点和所包含的功能
<hr/>
<h4>示例：</h4>
/auth，包含验证功能。检查所有验证功能、会话处理和访问控制，包括其他内容搜索攻击
/core，站点状态页面接受管道符(I)分隔的参数构成的数组。除传统的输入的攻击外， 还可对source 、location和IP值实施蛮力攻击，揭示有关其他用户或在pageID中指定的页面的详细信息。搜索有关无法访问的资源的信息，或在pageID中尝试使用通配符， 如pageID=all或pageID=*。由于显示的pageID值中包含斜杠，表示应用程序可能正从文件系统检索资源，可以对其实施路径遍历攻击。
/gb，包含该站点的留言板。访问此页面后发现， 这是一个由管理员主持的讨论论坛。虽然其中的消息由管理员进行管理，但却采用了登录避开机制login=true，攻击者可以尝试批准恶意消息（以实施跨站脚本攻击）， 以及阅读其他用户发送给管理员的私有消息
/home，经过验证的用户内容。尝试实施水平权限提升攻击，以访问其他用户的个人信息，确保在每个页面实施了访问控制
 /icons和/images，静态内容。简单尝试对属于第三方软件的图标名称实施蛮力攻击，并检查这些目录的目录索引
/pub路径的/pub/media和pub/user目录下包含的是REST风格的资源。可以针对/pub/user/1中的数字值实施蛮力攻击，以查找其他应用程序用户的个人资料页面。与此功能类似的社交网络功能可以揭示用户信息、用户名和其他用户的登录状态
/shop路径中包含网上购物站点和大量URL。URL的结构大致相同。仅查行一或两个URL就可以确定所有相关的受攻击面。购物过程中可能包含逻辑缺陷，利用这些缺陷获得未授权折扣或逃避支付


#### 简介：
