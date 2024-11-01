# 原创
：  【edusrc案例-思路总结(一)】幼儿园-挖掘链总结

# 【edusrc案例-思路总结(一)】幼儿园-挖掘链总结

【幼儿园】edusrc挖掘链-思路总结（一）
| 漏洞点 | 测试路径 | Payload | 总结 

测试路径

总结
| VPN（弱口令） | 1、开源信息（GitHub、使用手册、搜索语法）-学号-人名-密码规则----&gt;弱口令进入  2、寻找到了内网请求跳转url（被加密）---&gt;逆向加密算法 | 字典爆破、加密的逆向 | 搜索公开的敏感信息、生成字典爆破 

1、开源信息（GitHub、使用手册、搜索语法）-学号-人名-密码规则----&gt;弱口令进入

字典爆破、加密的逆向
| 已有账号（水平越权+垂直越权） | 1、功能点（对身份验证的参数）---&gt;改的学号---&gt;越权查看他人信息  2、将学号---&gt;admin 功能点，在请求数据里面知道了未完全加密的参数type=stu参数----&gt;teacher  3、修改密码---&gt;返回包中存在敏感信息（电话、邮件等） 修改密码---&gt;请求数据包中的userid修改---&gt;任意密码重置 | property value（参数值的修改，学号）  Type参数的寻找并修改 通过有身份鉴定的功能，查看是否能返回当前人的敏感信息  Id类型的敏感参数的修改 | 1、身份鉴定参数值的修改  观察每一个功能点的返回数据包  3、请求包中的敏感参数  

1、功能点（对身份验证的参数）---&gt;改的学号---&gt;越权查看他人信息

功能点，在请求数据里面知道了未完全加密的参数type=stu参数----&gt;teacher

修改密码---&gt;请求数据包中的userid修改---&gt;任意密码重置

Type参数的寻找并修改

Id类型的敏感参数的修改

观察每一个功能点的返回数据包
| 校园地图服务系统（未授权访问系统的目录）  | Dirsearch扫到springboot目录---&gt;工具分析出内存信息---&gt;post构造数据包---&gt;rec（带回数据） | Dirsearch、Eclipse Memory Analyzer | 寻找未授权访问目录---&gt;获取到敏感信息---&gt;rec 

Dirsearch扫到springboot目录---&gt;工具分析出内存信息---&gt;post构造数据包---&gt;rec（带回数据）

寻找未授权访问目录---&gt;获取到敏感信息---&gt;rec
| 信息泄露 | 通过谷歌语法（原本找注入漏洞inurl:.php?id=1）---&gt;找到了信息泄露 | 谷歌语法 | 熟悉谷歌语法 

通过谷歌语法（原本找注入漏洞inurl:.php?id=1）---&gt;找到了信息泄露

熟悉谷歌语法
| 批量挖掘 | 爬取edusrc中指定的测试对象（如只爬sql注入）----&gt;使用脚本poc进行批量测试 | 大量Poc | 存在同一漏洞的xx单位 

爬取edusrc中指定的测试对象（如只爬sql注入）----&gt;使用脚本poc进行批量测试

存在同一漏洞的xx单位
| 后台弱口令+文件上传getshell | 1、站点的各种目录爆破找后台---&gt;单引号报错、双引号正常---&gt;万能密码进入  2、后台上传功能点---&gt;%00截断---&gt;getshell | 找后台、找功能点 | 大量的寻找网站后台 

1、站点的各种目录爆破找后台---&gt;单引号报错、双引号正常---&gt;万能密码进入

找后台、找功能点
| 用户名漏洞 | 弱口令进后台---&gt;用户名改为admin（修改个人信息）---&gt;自己变为了admin | 参数的测试 | 想办法把自己变为admin 

弱口令进后台---&gt;用户名改为admin（修改个人信息）---&gt;自己变为了admin

想办法把自己变为admin
| 后台的Nday | 找到了后台---&gt;发现了使用的系统(老系统)---&gt;cnvd等漏洞平台找已知漏洞---&gt;复现nday | Nday | 识别使用的系统（cms） 

找到了后台---&gt;发现了使用的系统(老系统)---&gt;cnvd等漏洞平台找已知漏洞---&gt;复现nday

识别使用的系统（cms）
| 管理软件的nday | 信息收集各种资产---&gt;找到一个标有“用友”的管理网站---&gt;测试nday | Nday | 找大量的资产（直接标识所使用的系统cms） 

信息收集各种资产---&gt;找到一个标有“用友”的管理网站---&gt;测试nday

找大量的资产（直接标识所使用的系统cms）
| 弱口令+sql注入 | 1、谷歌搜索语法---&gt;工号+密码组成---&gt;爆破  2、拦截所有参数---&gt;加单引号---&gt;报错（存在注入点） | 爆破+单引号 | 账号的重要性、每个参数都测试sql（建议脚本测试） 

1、谷歌搜索语法---&gt;工号+密码组成---&gt;爆破

爆破+单引号
| 弱口令（看日志）+返回敏感数据+html（xss）+手机验证码复用 | 1、管理系统（弱口令）---&gt;查看了工号的登陆日志---&gt;登陆了教职工的后台  2、观察返回数据吧----&gt;敏感信息泄露---&gt;修改身份鉴别的参数(userkey爆破)---&gt;泄露了大量个人信息  3、上传HTML界面(可以被解析执行)----&gt;XSS 手机验证码复用 |  | 管理后台能否看日志、Html（xss） 

1、管理系统（弱口令）---&gt;查看了工号的登陆日志---&gt;登陆了教职工的后台

3、上传HTML界面(可以被解析执行)----&gt;XSS

管理后台能否看日志、Html（xss）
| 万能密码、未授权访问 | 1、找存在可能有注入的站点（登陆界面）---&gt;跑poc（万能密码）  2、某厂商存在未授权访问---&gt;然后把所有使用改厂商的单位跑一边 | 万能密码、未授权 | 找到一个漏洞后，大量测试 

1、找存在可能有注入的站点（登陆界面）---&gt;跑poc（万能密码）

万能密码、未授权
| 忘记密码+首次登陆修改密码验证（越权登陆） | 1、第一步使用目标邮箱+账号，在第二步发送邮件的时候，修改为自己的邮箱  2、isFirstLogin参数验证是否首次登陆（修改的返回包）---&gt;修改值为yrue---&gt;直接修改密码 | 特殊含义参数的修改 | 找一些判断参数 

1、第一步使用目标邮箱+账号，在第二步发送邮件的时候，修改为自己的邮箱

特殊含义参数的修改
| 前端验证+xss（获取到管理员cookie） | 密保信息前端验证 各种地方都插xss-payload---&gt;获取到管理员cookie | Xss-payload到处插 | Xss-payload到处插 

密保信息前端验证

Xss-payload到处插
| 登陆界面后台URL泄露 | 查看登陆界面处理的源码---&gt;找到了跳转的url（main.php）---&gt;直接访问（session.php身份验证）---&gt;修改返回数据包（删除错误信息，改为true） | 分析前端登录跳转逻辑 | 找后端跳转界面,修改返回会数据包 

查看登陆界面处理的源码---&gt;找到了跳转的url（main.php）---&gt;直接访问（session.php身份验证）---&gt;修改返回数据包（删除错误信息，改为true）

找后端跳转界面,修改返回会数据包
| 无验证码登陆界面爆破+越权修改密码 | 1、找到无验证码的登陆界面（找到账号密码规则）---&gt;爆破  2、修改密码功能，修改请求数据包loginname----&gt;实现越权修改密码 | 脆弱边界 | 寻找看似老、旧的系统（不安全） 

1、找到无验证码的登陆界面（找到账号密码规则）---&gt;爆破

脆弱边界
| Sql注入 | 登陆界面（index.aspx）---&gt;sqlmap跑出注入点（存在万能密码） | Sqlmap | 登陆界面存在注入点===存在万能密码 

登陆界面（index.aspx）---&gt;sqlmap跑出注入点（存在万能密码）

登陆界面存在注入点===存在万能密码
| 弱口令 | 厂商（存在大量单位使用）----&gt;用户手册---&gt;跑默认的用户名+密码 | 寻找默认密码 | 通过默认账号密码跑大量的同一厂商的系统 

厂商（存在大量单位使用）----&gt;用户手册---&gt;跑默认的用户名+密码

通过默认账号密码跑大量的同一厂商的系统
| 联动批量的漏扫 | FOfa+rad+burp+xray |  | 注意动作尺度 

FOfa+rad+burp+xray
| Api接口泄露 | 1、http历史流量---&gt;api接口---&gt;访问这个api接口---&gt;暴漏出很多URL---&gt;某些URL存在某个信息 ​ 2、有用户敏感信息后进行更多操作 | Api接口 | http历史流量找接口、忽略的细节 

1、http历史流量---&gt;api接口---&gt;访问这个api接口---&gt;暴漏出很多URL---&gt;某些URL存在某个信息

2、有用户敏感信息后进行更多操作

http历史流量找接口、忽略的细节
| Sql注入 | URL中存在id参数---&gt;sql手工测试存在注入点---&gt;sqlmap工具测试 | Sql-payload测试 | 先payload，再sqlmap 

URL中存在id参数---&gt;sql手工测试存在注入点---&gt;sqlmap工具测试

先payload，再sqlmap
| Cookie伪造 | Cookie使用base64加密---&gt;解密---&gt;用户id_用户名_权限id---&gt;admin账号的伪造 | Cookie的加密方法识别 | Cookie的组成解密 

Cookie使用base64加密---&gt;解密---&gt;用户id_用户名_权限id---&gt;admin账号的伪造

Cookie的组成解密

---


---


##  实战中心：

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
