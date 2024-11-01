# 原创
：  burpsuite模块介绍之compare

# burpsuite模块介绍之compare

#### 导语

Burp Comparer是Burp Suite中的一个工具，主要提供一个可视化的差异比对功能，可以用于分析比较两次数据之间的区别。它的应用场景包括但不限于：
1.  枚举用户名过程中，对比分析登陆成功和失败时，服务器端反馈结果的区别。 1.  使用Intruder进行攻击时，对于不同的服务器端响应，可以很快地分析出两次响应的区别在哪里。 1.  进行SQL注入的盲注测试时，比较两次响应消息的差异，判断响应结果与注入条件的关联关系。 
通过Burp Comparer，你可以方便地比较和分析不同版本的数据，发现其中的差异点，并针对这些差异点进行相应的处理和调整。

#### 使用示例

可以找个靶场进行密码爆破然后对比请求成功也请求失败的，我感觉太麻烦了就随便找个网站进行登录：先输入一个错误的账号在输入一个正确的账号进行对比、

<img alt="" height="720" src="https://img-blog.csdnimg.cn/direct/1f953b73a1bc4e4fb369222def5bfdfb.png" width="1200"/>对比结果 <img alt="" height="594" src="https://img-blog.csdnimg.cn/direct/2c02c673402e4d5aac69c3d02d1946f0.png" width="1200"/>
