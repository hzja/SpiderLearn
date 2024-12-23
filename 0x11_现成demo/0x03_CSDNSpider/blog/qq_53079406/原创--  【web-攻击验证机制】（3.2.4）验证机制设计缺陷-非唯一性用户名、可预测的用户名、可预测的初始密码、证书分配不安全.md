# 原创
：  【web-攻击验证机制】（3.2.4）验证机制设计缺陷：非唯一性用户名、可预测的用户名、可预测的初始密码、证书分配不安全

# 【web-攻击验证机制】（3.2.4）验证机制设计缺陷：非唯一性用户名、可预测的用户名、可预测的初始密码、证书分配不安全

**目录**

[验证机制设计缺陷](#%E9%AA%8C%E8%AF%81%E6%9C%BA%E5%88%B6%E8%AE%BE%E8%AE%A1%E7%BC%BA%E9%99%B7)

[1.1、非唯一性用户名](#1.1%E3%80%81%E9%9D%9E%E5%94%AF%E4%B8%80%E6%80%A7%E7%94%A8%E6%88%B7%E5%90%8D)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[1.2、可预测的用户名](#1.2%E3%80%81%E5%8F%AF%E9%A2%84%E6%B5%8B%E7%9A%84%E7%94%A8%E6%88%B7%E5%90%8D)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[1.3、可预测的初始密码](#1.3%E3%80%81%E5%8F%AF%E9%A2%84%E6%B5%8B%E7%9A%84%E5%88%9D%E5%A7%8B%E5%AF%86%E7%A0%81)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[1.4、证书分配不安全](#1.4%E3%80%81%E8%AF%81%E4%B9%A6%E5%88%86%E9%85%8D%E4%B8%8D%E5%AE%89%E5%85%A8)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

---


## 验证机制设计缺陷

> 
<h3>1.1、非唯一性用户名</h3>
<h4>简述：</h4>
1、支持自我注册的应用程序允许用户指定他们自己的用户名， 而且并不强制要求用户使用唯一的用户名（极其少见）由于两方面的原因， 这种设计存在一些缺陷。
2、在注册阶段或随后修改密码的过程中，共享同一个用户名的两个用户可能碰巧选择相同的密码。如果出现这种情况， 应用程序要么拒绝第二名用户选择的密码， 要么允许两个账户使用相同的证书。如果属于前者， 应用程序将会向一名用户泄霞另一名用户的证书，如果属于后者， 其中一名用户登录后会访问另一名用户的账户。

3、即使由于登录失败尝试次数方面的限制， 在其他地方不可能实施这种攻击， 攻击者仍然可以利用这种行为成功实施蛮力攻击。攻击者可以使用不同的密码， 多次用一个特殊的用户名注册， 同时监控说明使用该用户名和密码的账户已经存在的不同响应。攻击者不需以目标用户进行任何一次登录尝试， 即可获取该用户的密码

设计存在缺陷的自我注册功能还可能造成用户枚举漏洞。如果应用程序禁止使用相同的用户名， 那么攻击者可以注册大量常见的用户名， 从而确定遭到拒绝的现有用户名
<hr/>
<h4>过程：</h4>
1、如果应用程序允许自我注册， 尝试用不同的密码两次注册同一个用户名
2、如果应用程序阻止第二次注册企图， 也可以利用这种行为枚举现有的用户名， 虽然在主登录页面或其他地方不可能这样做。用一组常见的用户名进行多次注册尝试， 设法确定被应用程序阻止的已注册用户名
3、如果可成功注册完全相同的用户名， 尝试用相同的密码注册两个相同的用户名， 以此确定应用程序的行为。
A、如果以上做法得到错误消息， 也可以利用这种行为实施一次蛮力攻击， 虽然在主登录页面不可能实施这种攻击。针对一个枚举或猜测出的用户名发动攻击， 尝试用一组常用密码多次注册这个用户名。如果应用程序拒绝某个特殊的密码， 就可以发现目标账户的现有密码。
B、如果没有得到错误消息， 使用指定的证书登录，看看出现什么结果。可能需要注册几个用户， 修改每个账户保存的不同数据， 以确定这种行为是否可用于未授权访问其他用户的账户


#### 过程：

> 
<h3>1.2、可预测的用户名</h3>
<h4>简述：</h4>
一些应用程序根据某种可以预测的顺序自动生成账户用户名。如果应用程序以这种方式运转， 弄清了用户名顺序的攻击者就可以很快获得全部有效用户名， 以此作为后续攻击的基础。与依赖不断提交由词汇驱动请求的枚举方法不同， 这种确定用户名的方法不需实施入侵， 也很少给应用程序造成干扰
<hr/>
<h4>过程：</h4>
1、如果用户名由应用程序生成， 设法获得几个连续的用户名， 看能否从中君出任何顺序或模式。
2、如果存在某种顺序或模式． 向后推断列出所有可能的有效用户名。这种方法可作为需要有效用户名的登录蛮力攻击和其他攻击的基础， 如利用访问控制漏洞


#### 过程：

> 
<h3>1.3、可预测的初始密码</h3>
<h4>简述：</h4>
一些应用程序一次性或大批量创建用户，并自动指定初始密码， 然后以某种方式将密码分配给所有用户。这种生成密码的方式可让攻击者能够预测其他应用程序用户的密码。基于内联网的企业应用程序常常存在这种漏洞。应用程序为每位雇员创建一个账户，并向其发送一份打印好的密码通知。
如果所有用户收到相同的密码， 或者根据其用户名或工作职能创建的密码， 这种密码最容易被攻破。生成的密码可能包含某种顺序， 攻击者在行少数几个初始密码样本即可确定或猜测出其他用户的密码。
<hr/>
<h4>过程：</h4>
1、如果密码由应用程序生成． 设法获得几个连续的密码， 看能否从中看出任何顺序或模式
2、如果存在某种顺序或模式， 根据这种模式推断， 获取其他应用程序用户的密码
3、如果密码呈现出一种可能与用户名相联系的模式， 可以设法使用已知或猜测出的用户名与相应推断出的密码进行登录
4、可以使用推断出的密码列表作为利用一组枚举出的用户名或常见用户名实施蛮力攻击的基础


#### 过程：

> 
<h3>1.4、证书分配不安全</h3>
<h4>简述：</h4>
1、许多应用程序并不在用户与应用程序正常交互的过程中分配新建账户的证书（如通过邮寄或电子邮件）。有时， 采用这种分配方式主要出于安全考虑， 例如， 确保用户提供的邮寄或电子邮件地址属于其本人
2、这种分配方式有时会带来安全风险。如果分配证书的邮件中同时包含用户名和密码，没有给邮件设置使用时间限制， 没有要求用户在第一次登录时修改密码，大多数甚至是绝大部分应用程序用户都不会修改初始证书，并且将收到的邮件保存很长一段时间， 而未授权方有可能在此期间访问这些分配证书的邮件
3、有时应用程序并不分配证书， 而是传送一个“账户激活” URL, 用户通过它设置自己的初始密码。如果发送给连续用户的URL表现出某种顺序， 攻击者就可以通过注册几个紧密相连的用户确定这种顺序， 以此推断出发送给最近与后续用户的激活URL
4、某些Web应用程序表现的一种相关行为是， 允许新用户以相似安全的方式注册账户然后向每个新用户发送一封包含其完整的登录证书的欢迎电子邮件。具有安全意识的用户决定立即修改可能已被攻破的密码， 但随后又收到一封电子邮件， 其中包含“以备日后参考”
<hr/>
<h4>过程：</h4>
1、获得一个新账户。如果应用程序并不要求在注册阶段设置所有证书， 弄清应用程序如何向新用户分配证书。
2、如果应用程序使用账户激活URL，设法注册几个紧密相连的新账户， 确定收到的URL中的任何顺序。如果确定某种模式， 尝试预测应用程序发送给最近与后续用户的激活URL, 尝试使用这些URL占有他们的账户。
3、尝试多次重复使用同一个激活URL. 看看应用程序是否允许这样做。如果遭到拒绝，尝试在重复使用URL之前锁定目标账户， 看看现在这种方法是否可行



#### 过程：
