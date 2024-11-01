# 原创
：  【web-代码审计】(14.4)ASP.NET

# 【web-代码审计】(14.4)ASP.NET

**目录**

[ASP.NET](#ASP.NET)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、确定用户提交的数据](#1.2%E3%80%81%E7%A1%AE%E5%AE%9A%E7%94%A8%E6%88%B7%E6%8F%90%E4%BA%A4%E7%9A%84%E6%95%B0%E6%8D%AE)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1.3、会话交互](#1.3%E3%80%81%E4%BC%9A%E8%AF%9D%E4%BA%A4%E4%BA%92)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[1.4、潜在危险的API](#1.4%E3%80%81%E6%BD%9C%E5%9C%A8%E5%8D%B1%E9%99%A9%E7%9A%84API)

[文件访问](#%E6%96%87%E4%BB%B6%E8%AE%BF%E9%97%AE)

[数据库访问](#%E6%95%B0%E6%8D%AE%E5%BA%93%E8%AE%BF%E9%97%AE)

[动态代码执行](#%E5%8A%A8%E6%80%81%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C)

[OS命令执行](#OS%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C)

[URL重定向](#URL%E9%87%8D%E5%AE%9A%E5%90%91)

[套接字](#%E5%A5%97%E6%8E%A5%E5%AD%97)

[配置ASP.NET环境](#%E9%85%8D%E7%BD%AEASP.NET%E7%8E%AF%E5%A2%83)

---


## ASP.NET

> 
<h3>1.1、简介：</h3>
在ASP.NET平台上获取用户提交的输入的方法、与用户会话交互的方式、其中存在的潜在危险的API以及与平台安全相关的配置选项。


> 
<h3>1.2、确定用户提交的数据</h3>
<h4>简述：</h4>
ASP.NET应用程序通过System.Web.HttpRequest类获取用户提交的输入，这个类中包含大量Web应用程序用于访问用户提交的数据的属性和方法


> 
<h3>1.3、会话交互</h3>
<h4>简述：</h4>
1、ASP.NET应用程序以各种方式与用户会话进行交互，以保存和检索信息。
2、使用Session属性可轻松保存和检索当前会话中的信息，这个属性的访问方式与任何其他索引集合类似
Session["Myname"] = txtMyName.Text;           //保存用户名
lblwelcome.Text = "wekcome " +Session["MyName"];       //检索用户名
3、ASP.NET个性化配置与Session属性的用法非常相似，其唯一不同之处在于，前者相对于一个特定的用户，因此在相同用户的不同会话中持续保存不变，在不同的会话中，用户的身份通过验证机制或一个特殊的持久性cookie得以重新确认，在用户个性化配置中，数据以下列方式保存和检索：
Profile.Myname = txtMyName.Text;           //保存用户名
lblwelcome.Text = "wekcome " +Profile.Myname;        //检索用户名

4、另外System.Web.SessionState.HttpSessionState类也可用于保存和检索会话中的信息。它以字符串名称与对象值之间映射的方式保存信息


> 
<h3>1.4、潜在危险的API</h3>
<h4>文件访问</h4>
System.IO.File是用于访问ASP.NET文件最主要的类，它的所有方法都是静态的，并且没有公共构造函数。
这个类的37个方法全都接受一个文件名作为参数，如果未检查其中是否包含点-点斜线序列，就提交用户可控制的数据，就会造成路径遍历漏洞
<hr/>
<h4>数据库访问</h4>
1、ASP.NE下许多用于访问数据库的API, 下面的类主要用于建立并执行SQL语句：
System.Data.SqlClient.SqlCommand
System.Data.SqlClient.SqlDataAdapter
System.Data.Oledb.OleDbCommand
System.Data.Ddbc.OdbcCommand
System.Data.SqlServerCe.SqlCeCommand
2、其中每个类都有一个构造函数，它接受一个包含SQL语句的字符串，而且每个类都有一个CommandText属性，可用于获取并设定SQL语句的当前值，如果适当地配置一个命令对象，通过调用Execute方法即可执行SQL语句。

3、如果用户提交的数据属于以查询执行的字符串的一部分，那么应用程序可能易于受到SQL注入攻击，但如果每一个类通过它们的Parameters属性支持预处理语句，允许应用程序创建一个包含参数占位符的SQL语句，并以可靠且类型安全的方式设定这些占位符的值，按正常的方式使用，这种机制就不易受到SQL注入攻击
<hr/>
<h4>动态代码执行</h4>
1、VBScript函数Eval接受一个包含VBScript表达式的字符串自变量，该函数求出这个表达式的值，并返回结果，如果用户可控制的数据被合并到要计算值的表达式中，那么用户就可以执行任意命令或修改应用程序的逻辑。
2、函数Execute和ExecuteGlobal接受一个包含ASP代码的字符串，这个ASP代码与直接出现在脚本中的代码的执行方式完全相同。冒号分隔符用于将几个语句连接在一起，如果向Execute函数提交用户可控制的数据，那么攻击者就可以在应用程序中执行任意命令
<hr/>
<h4>OS命令执行</h4>
1、下面的API可以各种方式在ASP.NET应用程序中运行外部进程
System.Diagnostics.Start.Process
System.Diagnostics.Start.ProcessStartInfo
2、在对对象调用Start之前，可以向静态Process.Start方法提交一个文件名字符串，或用一个文件名配置Process对象的StartInfo属性，如果文件名字符串可完全由用户控制，那么应用程序几乎可以肯定易于受到任意命令执行攻击。但如果用户仅能够控制提交给Start的部分字符串，那么应用程序仍然可能易于受到攻击

3、API并不解释＆与I等shell元字符，也不接受文件名参数中的命令行参数，因此如果用户仅控制文件名参数的一部分，这种攻击是唯一能够成功的攻击。
4、已被启动的进程的命令行参数可以使用ProcessStartInfo类的Arguments属性设定。如果只有Arguments参数可由用户控制，应用程序仍然易于受到除代码执行以外的其他攻击。例如，如果应用程序以用户可控制的参数作为目标URL执行wget程序，那么攻击者就可以向wget进程提交危险的命令行参数， 例如致使它下载一个文档，并将该文档保存在文件系统中的任何位置
<hr/>
<h4>URL重定向</h4>
1、下面的API 用于在ASP.NET中发布一个HTTP重定向：
System.Web.HttpResponse.Redirect
System.Web.HttpResponse.Status
System.Web.HttpResponse.StatusCode
System.Web.HttpResponse.AddHeader
System.Web.HttpResponse.AppendHeader
Server.Transfer
2、通常使用HttpResponse.Redirect方法可以引起一个重定向响应，该方法接受一个包含相对或绝对URL的字符串。如果这个字符串的值由用户控制，那么应用程序可能易于受到钓鱼攻击
3、还必须确保检查Status/StatusCode属性与AddHeader/ AppendHeader方法的用法，如果某个重定向包含一个含有HTTPLocation消息头的3xx响应，应用程序就可能使用这些API执行重定向

4、Server.Transfer方法有时也可用于实现重定向。实际上这个方法并不能实现HTTP重定向，而是应根据当前请求修改被服务器处理的页面。因此不能通过破坏它重定向到一个站外URL，这个方法对攻击者而言并没有多大用处
<hr/>
<h4>套接字</h4>
System.Net.Sockets.Socket类用于创建网络套接字，创建一个Socket对象后，再通过调用Connect方法连接这个对象，该方法接受目标主机的IP与端口信息为参数，如果用户能够以某种方式控制这些主机信息，攻击者就可以利用应用程序与任意主机建立网络连接、无论这些主机位于因特网上、私有DMZ中还是在应用程序上运行的内部网络内
<hr/>
<h4>配置ASP.NET环境</h4>
Web根目录下的web.config XML文件包含ASP.NET环境的配置设置，它还控制着应用程序的行为

如果数据库连接字符串之类的敏感数据保存在配置文件中，应使用ASP.NET"受保护配置"特性加密这些数据



#### 文件访问

---


#### 动态代码执行

---


#### URL重定向

---


#### 配置ASP.NET环境
