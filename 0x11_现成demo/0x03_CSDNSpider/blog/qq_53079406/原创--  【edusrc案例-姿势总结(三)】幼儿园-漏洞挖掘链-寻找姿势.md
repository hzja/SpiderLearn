# 原创
：  【edusrc案例-姿势总结(三)】幼儿园-漏洞挖掘链-寻找姿势

# 【edusrc案例-姿势总结(三)】幼儿园-漏洞挖掘链-寻找姿势

edusrc漏洞挖掘链-思路总结（三）
| 漏洞点 | 漏洞挖掘链 

漏洞挖掘链
| .net程序-未授权访问 | 收集*.xxx.edu.cn子域名 ===》 httpx观察子域名响应 ===》 403响应（一个子域名带admin） ===》 .net的程序的403===》尝试后台和越权路径 ===》 绕过存在admin/login.aspx ===》 测试路径admin/top.aspx和admin/main.aspx ===》 成功访问后台 

收集*.xxx.edu.cn子域名 ===》 httpx观察子域名响应 ===》 403响应（一个子域名带admin） ===》 .net的程序的403===》尝试后台和越权路径 ===》 绕过存在admin/login.aspx ===》 测试路径admin/top.aspx和admin/main.aspx ===》 成功访问后台
| Sql注入 | 抓取到通知的请求包---&gt;包含id参数---&gt;单引号报错（存在注入）---&gt;确定数据库类型---&gt;对应的注入构造 

抓取到通知的请求包---&gt;包含id参数---&gt;单引号报错（存在注入）---&gt;确定数据库类型---&gt;对应的注入构造
| 登录绕过 | 登录---&gt;提示平台正在维护（error）---&gt;查看前端源码---&gt;登录模式（submit(login)、sumbit(error)）---&gt;将数据包中的lay-filter=”error”改为lay-filter=”login”。即登录成功 

登录---&gt;提示平台正在维护（error）---&gt;查看前端源码---&gt;登录模式（submit(login)、sumbit(error)）---&gt;将数据包中的lay-filter=”error”改为lay-filter=”login”。即登录成功
| 文件上传+XSS | 上传照片处---&gt;将filename改为xxx.html---&gt;内容为XSS payload 

上传照片处---&gt;将filename改为xxx.html---&gt;内容为XSS payload
| 微信小程序任意用户绑定 | 第一次打开小程序---&gt;抓取数据包---&gt;返回数据包中显示微信号未绑定+一个陌生参数值（其值为数字）---&gt;修改为其他参数---&gt;可查看其他用户的相关数据（并可进行一切用户可进行的操作） 

第一次打开小程序---&gt;抓取数据包---&gt;返回数据包中显示微信号未绑定+一个陌生参数值（其值为数字）---&gt;修改为其他参数---&gt;可查看其他用户的相关数据（并可进行一切用户可进行的操作）
| 任意手机号注册、登录 | 使用任何手机号---&gt;进行账号注册（登录）---&gt;返回的数据包中返回了验证码 

使用任何手机号---&gt;进行账号注册（登录）---&gt;返回的数据包中返回了验证码
| 敏感接口泄露 | 同一ip下发现了更多的接口文档---&gt;xxx/Employees/id---&gt;然后使用get请求方法---&gt;获取到任意id参数代表用户的数据 

同一ip下发现了更多的接口文档---&gt;xxx/Employees/id---&gt;然后使用get请求方法---&gt;获取到任意id参数代表用户的数据
| 水平越权 | 在服务中心---&gt;有很多模块---&gt;点击跳转到其他业务模块---&gt;在此时抓住跳转的数据包---&gt;然后将学号对应的参数---&gt;改为其他学号---&gt;水平越权到其他的账号上去了（相关的操作也可以测试水平越权操作） 

在服务中心---&gt;有很多模块---&gt;点击跳转到其他业务模块---&gt;在此时抓住跳转的数据包---&gt;然后将学号对应的参数---&gt;改为其他学号---&gt;水平越权到其他的账号上去了（相关的操作也可以测试水平越权操作）
| 信息泄露 | 点击申请的功能---&gt;抓取申请的数据包(post)---&gt;返回敏感个人信息---&gt;修改post数据包中鉴别判断用户身份的参数---&gt;此处改user-id---&gt;返回任意对应账号的用户信息 

点击申请的功能---&gt;抓取申请的数据包(post)---&gt;返回敏感个人信息---&gt;修改post数据包中鉴别判断用户身份的参数---&gt;此处改user-id---&gt;返回任意对应账号的用户信息
| 水平越权 | 在学生申请xxx的地方---&gt;修改post数据包中带的学号信息---&gt;替他人进行了申请 

在学生申请xxx的地方---&gt;修改post数据包中带的学号信息---&gt;替他人进行了申请
| 后台越权访问 | GET请求/user接口---&gt;拦截返回的数据包---&gt;将permission参数改为1---&gt;直接出现管理员后台---&gt;然后每一步请求中都需要修改返回数据包参数为1 

GET请求/user接口---&gt;拦截返回的数据包---&gt;将permission参数改为1---&gt;直接出现管理员后台---&gt;然后每一步请求中都需要修改返回数据包参数为1
| 越权操作 | 有管理员账号后---&gt;将管理员执行的操作保存---&gt;退出管理员登录---&gt;重放一遍管理员执行的操作（也可以通过使用BP的插件，来鉴定是否有越权） 

有管理员账号后---&gt;将管理员执行的操作保存---&gt;退出管理员登录---&gt;重放一遍管理员执行的操作（也可以通过使用BP的插件，来鉴定是否有越权）
| 隐藏菜单 | 右键查看源码---&gt;查看到前端有一段自定义的menuClick菜单函数（并且使用case语法）----&gt;case语法中带有相关的路径(只有一部分)---&gt;将路径拼接---&gt;访问管理操作界面（需要注意的是路径的拼接，未透出出来的路径多半是加密的路径，在考虑前端加密的情况下，还要使用已有账号尝测试） 

右键查看源码---&gt;查看到前端有一段自定义的menuClick菜单函数（并且使用case语法）----&gt;case语法中带有相关的路径(只有一部分)---&gt;将路径拼接---&gt;访问管理操作界面（需要注意的是路径的拼接，未透出出来的路径多半是加密的路径，在考虑前端加密的情况下，还要使用已有账号尝测试）
| Xss点击弹窗 | &lt;form&gt;&lt;button formaction=javascript:alert(1)&gt;CLICK ME 

&lt;form&gt;&lt;button formaction=javascript:alert(1)&gt;CLICK ME
| 变量覆盖 | 注册账号admin---&gt;提示账号已经存在---&gt;注册账号admin1---&gt;抓取数据包修改为admin---&gt;这里有2种情况，有防护的话，那么会报错，如果无防护就直接注册成功了 

注册账号admin---&gt;提示账号已经存在---&gt;注册账号admin1---&gt;抓取数据包修改为admin---&gt;这里有2种情况，有防护的话，那么会报错，如果无防护就直接注册成功了
| 越权 | 获取到管理员账号---&gt;在使用账号登录到后台的时候抓取返回数据包---&gt;会有参数对权限进行验证---&gt;如将value值的false改为true等（可能会有多个参数需要修改，比如2改为1等）（如role由2改为1可能变成超级管理员） 

获取到管理员账号---&gt;在使用账号登录到后台的时候抓取返回数据包---&gt;会有参数对权限进行验证---&gt;如将value值的false改为true等（可能会有多个参数需要修改，比如2改为1等）（如role由2改为1可能变成超级管理员）
| 爆破 | 输入学号+错误密码----&gt;提示学号错误---&gt;根据提示信息使用BP爆破学号（先问问他们群看看他们账号组成）---&gt;然后使用（大量）学号+一个（或多个）弱口令爆破 

输入学号+错误密码----&gt;提示学号错误---&gt;根据提示信息使用BP爆破学号（先问问他们群看看他们账号组成）---&gt;然后使用（大量）学号+一个（或多个）弱口令爆破
| 字典制作 | 随着安全意识的提高---&gt;弱口令成功的概率已经变得非常微小---&gt;每次针对不同的系统的时候---&gt;收集制作对应的弱口令字典 

随着安全意识的提高---&gt;弱口令成功的概率已经变得非常微小---&gt;每次针对不同的系统的时候---&gt;收集制作对应的弱口令字典
| 任意文件删除 | 首先有删除按钮---&gt;修改post请求包中的id（为管理员文章、或其他用户文章）---&gt;删除任意文章（或者添加删除参数尝试越权删除，如_xxxid_delete_action=1、action=delete等） 

首先有删除按钮---&gt;修改post请求包中的id（为管理员文章、或其他用户文章）---&gt;删除任意文章（或者添加删除参数尝试越权删除，如_xxxid_delete_action=1、action=delete等）

---


---


## 实战中心：

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
