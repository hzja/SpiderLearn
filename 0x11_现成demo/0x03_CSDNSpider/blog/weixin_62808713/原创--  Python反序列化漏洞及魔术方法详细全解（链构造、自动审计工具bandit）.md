# 原创
：  Python反序列化漏洞及魔术方法详细全解（链构造、自动审计工具bandit）

# Python反序列化漏洞及魔术方法详细全解（链构造、自动审计工具bandit）

**目录**

[一、Python序列化反序列化相关函数](#%E4%B8%80%E3%80%81Python%E5%BA%8F%E5%88%97%E5%8C%96%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E7%9B%B8%E5%85%B3%E5%87%BD%E6%95%B0)

[二、Python魔术方法](#%E4%BA%8C%E3%80%81Python%E9%AD%94%E6%9C%AF%E6%96%B9%E6%B3%95)

[三、魔术方法实例详解](#%E4%B8%89%E3%80%81%E9%AD%94%E6%9C%AF%E6%96%B9%E6%B3%95%E5%AE%9E%E4%BE%8B%E8%AF%A6%E8%A7%A3)

[&lt;__reduce__&gt;](#%3C__reduce__%3E)

[&lt;__setstate__&gt;](#%3C__setstate__%3E)

[&lt;__getstate__&gt;](#%3C__getstate__%3E)

[四、反序列化安全漏洞的产生](#%E5%9B%9B%E3%80%81%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E5%AE%89%E5%85%A8%E6%BC%8F%E6%B4%9E%E7%9A%84%E4%BA%A7%E7%94%9F)

[五、真题实例](#%E4%BA%94%E3%80%81%E7%9C%9F%E9%A2%98%E5%AE%9E%E4%BE%8B)

[六、CTF-CISCN华北-JWT&amp;反序列化](#%E5%85%AD%E3%80%81CTF-CISCN%E5%8D%8E%E5%8C%97-JWT%26%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96)

[七、代码审计自动化工具——bandit](#%E4%B8%83%E3%80%81%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1%E8%87%AA%E5%8A%A8%E5%8C%96%E5%B7%A5%E5%85%B7%E2%80%94%E2%80%94bandit)

---


## 一、Python序列化反序列化相关函数

## 二、Python魔术方法

## 三、魔术方法实例详解

### &lt;__reduce__&gt;

1.代码。

2.运行结果。 

### &lt;__setstate__&gt;

1.代码。

 2.运行结果。 

### &lt;__getstate__&gt;

1.代码。

 2.运行结果。 

## 四、反序列化安全漏洞的产生

1.代码。

​​​<img alt="" height="139" src="https://img-blog.csdnimg.cn/c1f798eda3294a288316b6b40ccf9272.png" width="562"/>

2.运行结果。

<img alt="" height="836" src="https://img-blog.csdnimg.cn/d432b5f1911b44499ee699e4a978db74.png" width="1200"/>3.当我们将调用计算器的代码更改为“ipconfig”后，执行代码可以看到成功执行了命令。

4.**总结：**

        魔术方法执行调用下面的代码，如果下面的代码可控的话，就可能存在反序列化漏洞。 

## 五、真题实例

1.环境介绍：

        利用Python-fask搭建的web应用，获职当前用户的信息，进行展示，在获取用户的信息时，通过对用户数据进行反序列化获取导致的安全漏洞! 

2.代码片段。

3.打开。

4.攻击思路：

        在cookie内植入user值，user值就是生成的恶意序列化数据。

5.构造exp。

<img alt="" height="252" src="https://img-blog.csdnimg.cn/5a03c055b78e4771b4e7aecd0b2d75fa.png" width="845"/>6.执行得到序列化代码。

7.在源代码中得知其会进行一次base64解码，所以我们需要对上面得到的序列化代码进行一次编码。对代码进行下面的修改。

<img alt="" height="165" src="https://img-blog.csdnimg.cn/8b973cd8b1e14777b4446de2050d0538.png" width="833"/>8.再次执行得到编码后的序列化代码。

9.抓取数据包，在数据包内添加下面的内容。

10.放包后可以看到计算器成功弹出。

## 六、CTF-CISCN华北-JWT&amp;反序列化

1.通过提示：

        寻找LV6 -&gt; 购买修改支付逻辑 -&gt; 绕过admin限制需修改jwt值 -&gt; 爆破jwt密匙 -&gt; 重组jwt值成为admin -&gt; 购买进入会员中心 -&gt; 源码找到文件压缩源码 -&gt; Python代码南计反序列化 -&gt; 构造读取flag代码进行序列化打印 -&gt; 提交获取。

2.考点：

3.找到并将靶场环境打开。

4.打开后页面如下。

5.可以看到目的是买到v6。

6.因为它分好多页，所以可以使用脚本来爬取找到v6。

7.用来爬取的代码如下图所示。

<img alt="" height="436" src="https://img-blog.csdnimg.cn/0ae812cf95e4427884245bd3c0e3120c.png" width="1113"/>8. 可以看到在第180页内找到了。

9.点击购买后跳转到了登陆页面。

10.注册好后再次点击购买可以看到调换到了下面的页面。

<img alt="" height="571" src="https://img-blog.csdnimg.cn/808053d9e1b745c19b5f407dd5dc1ff3.png" width="1104"/>11.但是点击结算后就又跳转到了下面的页面。

12.这是因为我们的存款不够购买v6的。

13.我们重新点击结算后抓包。

14.将上面数据包内的0.8（打的折）改成超级小的数。

15.放包后却又得到了下面的返回结果。

16.重新抓取数据包后我们注意到了数据包内的JWT值。

<img alt="" height="466" src="https://img-blog.csdnimg.cn/7871a3f9d3d144b4b618f2e79ac7c7b8.png" width="1089"/>17.我们将其粘贴到官网后进行解密，得到下面的结果。

<img alt="" height="730" src="https://img-blog.csdnimg.cn/c98399a41ef742f198bbc90a49614bcd.png" width="1112"/>18.使用脚本破解密匙。

19.将破解后的密匙填入后将username更改成admin，得到新的JWT值。

20.将其粘贴到数据包内后再次放包。

21.可以看到这次网站成功进行了执行。

22.但是当我们点击下面的一键成为大会员后网页却没有反应。

23.此时查看网页源代码后可以看到下面的内容。

24.将其进行下载解压后打开，可以看到下面的内容。

25. 可以得知是网站原码，我们将其打开后进行分析。

26.我们直接使用搜索功能搜索序列化相关内容。

27.定位后可以看到调用序列化的函数。

28.经过分析得知其是python2进行编码的，因此我们使用python构造payload。

 29.执行后可以看到成功构造了payload。

30.将value值改成我们刚刚生成的payload。

31.更改后再次点击一键成为大会员，可以看到成功获取到了flag。 

## 七、代码审计自动化工具——bandit

1.参考:

[GitHub - PyCQA/bandit: Bandit is a tool designed to find common security issues in Python code.](https://github.com/PyCQA/bandit)

[Test Plugins — Bandit documentation](https://bandit.readthedocs.io/en/latest/plugins/index.html)

2.安装: pip install bandit

        安装后会在当前Python目录下bin

        使用: bandit-r 需要审计的源码目录

        安装后会在当前Python目录下script

        使用: bandit -r 需要审计的源码目录

3.实操示例。
