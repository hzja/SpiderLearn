# 原创
：  【web-攻击用户】（9.7.2）本地隐私攻击：攻击ActiveX控件

# 【web-攻击用户】（9.7.2）本地隐私攻击：攻击ActiveX控件

**目录**

[攻击ActiveX控件](#%E6%94%BB%E5%87%BBActiveX%E6%8E%A7%E4%BB%B6)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、查找ActiveX漏洞](#1.2%E3%80%81%E6%9F%A5%E6%89%BEActiveX%E6%BC%8F%E6%B4%9E)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[1.3、防止ActiveX漏洞](#1.3%E3%80%81%E9%98%B2%E6%AD%A2ActiveX%E6%BC%8F%E6%B4%9E)

---


## 攻击ActiveX控件

> 
<h3>1.1、简介：</h3>
1、应用程序可以使用各种厚客户端技术将它的一些处理操作分配给客户端完成。ActiveX控件对于针对其他用户的攻击者特别有用，如果应用程序安装了一个可从自己的页面调用的控件， 该控件必须注册为"脚本执行安全",这样用户访问的任何其他Web站点都能够使用这个控件。
2、通常浏览器并不接受Web站点要求它们安装的任何ActiveX控件，默认情况下，当Web站点试图安装某个控件时，浏览器会显示一个安全警报，要求得到用户许可，是否信任发布该控件的Web站点以及是否允许安装该控件，将由用户自行决定。但如果用户安装该控件，并且其中包含任何漏洞， 则用户访问的任何恶意Web站点都可以利用这些漏洞

3、ActiveX控件中常见的对攻击者有用的漏洞主要分为两类：
A、由于ActiveX控件通常以C/C++之类的本地语言编写，它们之中很可能存在一些典型的软件漏洞，如缓冲区溢出、整数漏洞以及格式字符串漏洞。人们已经在流行Web应用程序发布的ActiveX控件中发现了大量这些类型的漏洞。通常攻击者可以利用这些漏洞在受害用户的计算机上执行任意代码
B、许多ActiveX控件中包含一些本质上存在风险、易被滥用的方法。

4、开发者往往会执行这些方法来提高控件的灵活性，以便于将来扩展控件的功能，而不必部署全新的控件，但一且安装了这些控件，任何恶意站点也可以通过同样的方式对其进行“扩展”， 从而执行针对用户的恶意操作


> 
<h3>1.2、查找ActiveX漏洞</h3>
<h4>简述：</h4>
1、当应用程序安装ActiveX控件时，除浏览器会显示一个要求获得安装控件许可的警报外，还应该可以在某个应用程序页面的HTML源代码中找到类似于下面的代码
&lt;object id="oMyObject"
        classid="CLSID:……"
        codebase="……"&gt;
&lt;/object&gt;

2、这段代码告诉浏览器用指定的名称和classid示例化ActiveX控件，并从指定的URL下载该控件。如果浏览器中已经安装有控件，就不需要使用codebase参数，浏览器会根据控件的唯一classid，从本地计算机中找到该控件
3、如果用户允许安装这个控件，浏览器会将其注册为"脚本执行安全"。这意味着将来任何Web站点都可以将其示例化，并调用它的方法。可以通过检查注册表项HKEY_CLASSES_ROOT\CLSID\从上面的HTML中提取的控件classid/Implemented Categories确认这一点。如果其中存在子注册表项，则表示该控件已经注册为"脚本执行安全"

4、浏览器示例化ActiveX控件后，就可以通过以下脚本调用它的方法：
&lt;script&gt;<br/>         document.omyObject.LaunchExe('myAppdemo.exe')<br/> &lt;/script&gt;
<hr/>
<h4>过程：</h4>
一种探在ActiveX漏洞的简单方法是，修改调用该控件的HTML代码， 向其提交自己的参数， 然后监控执行结果
1、攻击有效载荷可探查缓冲区溢出之类的漏洞，如果以不受控制的方式触发这种漏洞， 很可能会导致负责该控件执行的浏览器进程崩溃
2、本质上存在风险的方法通过其名称即可确定，如LaunchExe，在其他情况下，控件名称可能无害或含义模糊，但有一些有用的数据，如文件名、URL或系统命令，明显被用作控件的参数。应该尝试将这些参数修改为任意值，确定控件是否按预计的方式处理输入
<hr/>
应用程序并没有调用控件的所有方法。如一些方法主要用于测试目的、一些已被取代但尚未删除、一些可能是为了方便将来使用或用于自我更新目的，为了对控件进行综合测试，有必要枚举出它通过这些方法暴露的各种受攻击面，并对这些受攻击面进行彻底测试。
有各种工具可用于枚举和测试ActiveX控件方法。iDefense开发的COMRaider，就是一个有用的<br/> 工具，它能够显示一个控件的全部方法，并对每个方法执行基本的模糊测试


#### 过程：

---


> 
<h3>1.3、防止ActiveX漏洞</h3>
1、保护本地编译软件组件的安全，防止其受到攻击，是一个广泛而复杂的话题的讨论范围。基本上， ActivcX控件的设计者与开发者必须确保恶意Web站点无法调用该控件实施的方法， 用以对安装这个控件的用户执行恶惹操作。以下是一些应该注意的问题：
A、应对控件进行以安全为中心的源代码审查与渗透测试，以确定缓冲区溢出之类的漏洞
B、控件不得暴露任何使用用户可控制的输入调用外部文件系统或操作系统、本质上存在风险的方法，只需稍微做出一些努力，就可以找到更安全的替代方法。如果有必要，启动外部进程，则应编辑一个列表，列出所有可合法、安全启动的外部进程，然后创建单独的方法调用每个进程， 或使用一个方法提取这个列表中的索引号
2、为进行深层防御，一些ActiveX控件对发布HTML页面（这些控件即从中调用）的域名进行确认。微软的"SiteLock活动模板库"模板允许开发者将ActiveX控件仅限于特定的域名列表。
3、一些控件甚至更进一步，要求提交给它们的所有参数必须使用加密签名，如果提交的签名无效，控件不会执行请求的操作。还要注意如果允许调用这些控件的Web站点存在任何XSS漏洞，那么攻击者就有可能突破这类防御

