# 原创
：  【upload靶场1-11】基础关卡：特点、分析、利用

# 【upload靶场1-11】基础关卡：特点、分析、利用

**目录**

[Pass1（前端验证）](#Pass1%EF%BC%88%E5%89%8D%E7%AB%AF%E9%AA%8C%E8%AF%81%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass2（MIME之content-type验证）](#Pass2%EF%BC%88MIME%E4%B9%8Bcontent-type%E9%AA%8C%E8%AF%81%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass3（黑名单后端验证）](#Pass3%EF%BC%88%E9%BB%91%E5%90%8D%E5%8D%95%E5%90%8E%E7%AB%AF%E9%AA%8C%E8%AF%81%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass4（.htaccess文件配置）](#Pass4%EF%BC%88.htaccess%E6%96%87%E4%BB%B6%E9%85%8D%E7%BD%AE%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass5（用户自定义配置文件）](#Pass5%EF%BC%88%E7%94%A8%E6%88%B7%E8%87%AA%E5%AE%9A%E4%B9%89%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass6（大写未统一，绕过黑名单）](#Pass6%EF%BC%88%E5%A4%A7%E5%86%99%E6%9C%AA%E7%BB%9F%E4%B8%80%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass7（未去空格，绕过黑名单）](#Pass7%EF%BC%88%E6%9C%AA%E5%8E%BB%E7%A9%BA%E6%A0%BC%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass8（未去点号，绕过黑名单）](#Pass8%EF%BC%88%E6%9C%AA%E5%8E%BB%E7%82%B9%E5%8F%B7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass9（添加::$DATA，绕过黑名单）](#Pass9%EF%BC%88%E6%B7%BB%E5%8A%A0%3A%3A%24DATA%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass10（检测规则的一次性，绕过黑名单）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass11（双写绕过，绕过黑名单）](#Pass11%EF%BC%88%E5%8F%8C%E5%86%99%E7%BB%95%E8%BF%87%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

---


## Pass1（前端验证）

> 
<h3>特点：</h3>
上传文件后缀限制


> 
<h3>分析：</h3>
要求上传jpg png gif 类型文件

 右键查看元源码
这里调用了一个checkFile函数，找到它
是前端验证

可以知道这个函数是用来检测文件类型的<img alt="" height="446" src="https://img-blog.csdnimg.cn/719a493a2a484aeba843fbb20021b052.png" width="1190"/>



> 
<h3>利用：</h3>
1、可以尝试把checkFile函数删了，变成return true ，或者直接删了
2、使网页处在JS disabled状态，再上传（Script Switch插件）
3、上传shell.png，而后使用bp抓包改为shell.php
<hr/>
使用方法三：

 改后----&gt;放包

 上传成功了<img alt="" height="772" src="https://img-blog.csdnimg.cn/fe4724b5bd41467e8c7895812abcc7f1.png" width="1042"/>
 打开图片获得图片地址


 复制shell地址<img alt="" height="217" src="https://img-blog.csdnimg.cn/f2868a0fbb344c8ca0a40049fa5d33dd.png" width="1054"/>
 粘贴shell地址，和自己设置的密码

 连接成功<img alt="" height="516" src="https://img-blog.csdnimg.cn/43f48de28a7a44c983ed1e254f3896cc.png" width="1200"/>



---


---


## Pass2（MIME之content-type验证）

> 
<h3>特点：</h3>
后端检测
content-type检测


> 
<h3>分析：</h3>

 右键查看元源码
这里调用了一个checkFile函数

未在前端找到这个函数，应该是后端检查
<hr/>
上传正常的jpg文件

 

 上传非正常后缀的php文件

 

 
<hr/>
正常文件和非正常文件的content-type值不一样，可能是这里存在后端检查


---


> 
<h3>利用：</h3>
1、上传正常文件（png，jpg，gif），bp抓包修改文件
2、上传非正常文件（php），bp抓包修改content-type值
<hr/>
使用方法一：

 改后----&gt;放包

 <img alt="" height="746" src="https://img-blog.csdnimg.cn/7bca1f80140a4661ab322e889f8c75f0.png" width="634"/>
 

 上传成功了

 
 打开图片获得图片地址

 复制shell的地址
蚁剑（菜刀、冰蝎）连接
 粘贴shell地址，和自己设置的密码



---


---


## Pass3（黑名单后端验证）

> 
<h3>特点：</h3>
绕过黑名单


> 
<h3>分析：</h3>
 右键查看元源码
这里调用了一个checkFile函数

未在前端找到这个函数，应该是后端检查
<hr/>
上传非正常后缀的php文件无法上传

考虑是否是后端设置了白名单、黑名单


> 
<h3>利用：</h3>
1、上传配置的.htaccess（将所有文件解析为php）（针对白名单）
2、上传非正常文件（php），bp抓包对后缀进行爆破（针对黑名单）
<hr/>
使用方法二：

 抓包----&gt;爆破

 ​​​​​​<img alt="" height="795" src="https://img-blog.csdnimg.cn/38f8e047d6d9410d8abe382704e9a0aa.png" width="1200"/>
 这里可以使用爆破的字典

 <img alt="" height="327" src="https://img-blog.csdnimg.cn/17df14f060254d2aa93902d2a6a09cbd.png" width="843"/>
 推测是基于黑名单的过滤，因为存在能够注入的

 
 上传成功了


 
 打开图片获得图片地址
 复制shell的地址
蚁剑（菜刀、冰蝎）连接
 粘贴shell地址，和自己设置的密码



---


---


## Pass4（.htaccess文件配置）

> 
<h3>特点：</h3>
.htaccess文件（分布式配置文件）：
1、默认：不开启此功能
2、作用：针对目录改变配置的方法
3、位置：在特定的文档目录中放置一个包含一个或多个指令的文件
4、影响：作用于当前目录及其所有子目录
5、功能：文件夹密码保护、用户自定义重定向、自定义404页面、扩展名伪静态化、禁止特定IP地址的用户、只允许特定IP地址的用户、禁止目录列表
6、用法：（有效影响范围内）
AddType application/x-httpd-php .png (.png文件会被当做php文件解析)
SetHandler application/x-httpd-php（所有文件都被当做php文件来解析）


> 
<h3>分析：</h3>
.htaccess前提：
1、服务器：apache
2、功能点：能够上传.htaccess文件
3、配置：httpd.conf中AllowOverride All 并且有LoadModule rewrite_module modules/mod_rewrite.so
4、权限：上传的目录有可执行权限
<hr/>
右键查看元源码
这里调用了一个checkFile函数

未在前端找到这个函数，应该是后端检查
<hr/>
使用第二、三关方法，上传修改后的非正常后缀的文件都无法上传
所有可能的都已经进黑名单（从题目设计目的理解）
考虑利用特殊后缀去除问题


---


> 
<h3>利用：</h3>
1、上传配置的.htaccess（将所有文件解析为php）
2、添加特殊文件名后缀拼接php后
因为windows系统限制，当0x81~0x99（使用Hex添加）在文件名结尾时，会被自动去掉，结尾的空格和点（在文件名后加）也是同理
<hr/>
配置好.htaccess文件
SetHandler application/x-httpd-php

 上传.htaccess文件
（如果禁止上传，可以先命名为1.htaccess，后抓包修改为.htaccess）

<img alt="" height="645" src="https://img-blog.csdnimg.cn/522a77e3967a4d95b99ba9f89018961f.png" width="900"/> 
上传图片马 
 ​​​<img alt="" height="407" src="https://img-blog.csdnimg.cn/71caef151aba4f72ae899e2f4af46a4d.png" width="893"/>
上传成功
<img alt="" height="585" src="https://img-blog.csdnimg.cn/db7c035fce9649dcaeba0398711bd981.png" width="878"/> 
 
打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


## Pass5（用户自定义配置文件）

> 
<h3>特点：</h3>
.user.ini用户自定义配置文件使用


> 
<h3>分析：</h3>
.user.ini使用前提：
1、脚本语言：PHP
2、服务器：使用CGI／FastCGI模式
3、配置：php.ini中user_ini.filename = ".user.ini"，user_ini.cache_ttl =某个数
4、权限：上传的目录有可执行权限
<hr/>
右键查看元源码
这里调用了一个checkFile函数

未在前端找到这个函数，应该是后端检查
<hr/>
使用第二、三、四关方法，上传修改后的非正常后缀的文件都无法上传
考虑：
是否将大小写统一后过滤
是否可利用系统特性
是否存在爆破可能
是否可以利用配置文件


---


> 
<h3>利用：</h3>
1、使用bp抓包后，将文件名改为shell.php. .（点空格点）
2、本关未将大小写统一，然后验证，可以尝试爆破
3、利用用户自定义配置文件.user.ini
<hr/>
配置好.user.ini文件
auto_propend_file=shell.png

 
 
 上传.user.ini配置文件
（如果禁止上传，可以尝试修改后改包）


<img alt="" height="544" src="https://img-blog.csdnimg.cn/26b59ff1c1394503b7e71823d3e3a6da.png" width="915"/> 
 
上传图片马 

 
上传成功

 

打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


## Pass6（大写未统一，绕过黑名单）

> 
<h3>特点：</h3>
未使用strtolower()函数，是大小写统一


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
前面的.htaccess文件.user.ini等都在黑名单中了
考虑：
是否将大小写统一后过滤（strtolower函数）
是否可利用系统特性（即点空格点，还有考虑能否被解析）
是否存在爆破可能（即黑名单过滤不全）


> 
<h3>利用：</h3>
1、使用大写绕过黑名单
<hr/>



上传图片马 

 
上传成功


 


打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


## Pass7（未去空格，绕过黑名单）

> 
<h3>特点：</h3>
没有使用trim()函数，进行首尾去空


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
是否可利用系统特性（即点空格点，还有考虑能否被解析）
是否存在爆破可能（即黑名单过滤不全）
是否能够利用空格绕过


> 
<h3>利用：</h3>
1、后缀首位加空格
<hr/>

在后缀点后面加一个空格
上传图片马 

 

上传成功

 

打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


## Pass8（未去点号，绕过黑名单）

> 
<h3>特点：</h3>
没有使用deldot()函数，去掉文件名末尾的点号


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
MIME检测：如content-type值
点空格点：是否可利用系统特性（还有考虑能否被解析）
过滤不全：是否存在爆破可能
空格：是否能够利用空格绕过黑名单
点号：是否能够利用点号绕过黑名单


> 
<h3>利用：</h3>
1、在文件名后加点号
（windows可能会将点号直接去掉，需要在bp里面改）
<hr/>


上传图片马 （在bp里面加点号）


<img alt="" height="785" src="https://img-blog.csdnimg.cn/9ef4afb2599543b4b9fb358bf38f7261.png" width="665"/> 
上传成功


 

打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


## Pass9（添加::$DATA，绕过黑名单）

> 
<h3>特点：</h3>
没有对::$DATA（流文件）进行过滤


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
MIME检测：如content-type值
点空格点：是否可利用系统特性（还有考虑能否被解析）
过滤不全：是否存在爆破可能
空格：是否能够利用空格绕过黑名单
点号：是否能够利用点号绕过黑名单
流文件：是否能够利用::$DATA流文件进行绕过


> 
<h3>利用：</h3>
1、在文件名后加点号
（windows可能会将点号直接去掉，需要在bp里面改）
<hr/>
还是需要在bp里面改

 

上传图片马 （在bp里面加::$DATA）


 不知道对这个content-Type有没有检测

在文件名后加上::$DATA<img alt="" height="753" src="https://img-blog.csdnimg.cn/aeaf73d8b8bf4bbe85450993402c964d.png" width="655"/>
 
上传成功

 
打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


## Pass10（检测规则的一次性，绕过黑名单）

> 
<h3>特点：</h3>
检测规则，会去掉对应的预先设定字符
但未循环执行


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
MIME检测：如content-type值
点空格点：是否可利用系统特性（还有考虑能否被解析）
过滤不全：是否存在爆破可能
空格：是否能够利用空格绕过黑名单
点号：是否能够利用点号绕过黑名单
流文件：是否能够利用::$DATA流文件进行绕过
逻辑漏洞：是否循环执行检测


> 
<h3>利用：</h3>
1、使用.空格.来绕过，即shell.php. .
（还剩余的未过滤的点号，因为windows会将点号直接去掉）
<hr/>

上传图片马 （在bp里面加. . ）


 
 不知道对这个content-Type有没有检测

 
在文件名后加上. .（点空格点）

 
上传成功

 

打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


## Pass11（双写绕过，绕过黑名单）

> 
<h3>特点：</h3>
检测规则，会去掉对应的预先设定字符
但未循环执行


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
MIME检测：如content-type值
点空格点：是否可利用系统特性（还有考虑能否被解析）
过滤不全：是否存在爆破可能
空格：是否能够利用空格绕过黑名单
点号：是否能够利用点号绕过黑名单
流文件：是否能够利用::$DATA流文件进行绕过
逻辑漏洞：是否循环执行检测
双写：绕过一次检测


> 
<h3>利用：</h3>
1、使用双写来绕过一次检测，如phphpp
<hr/>

上传图片马 （在bp里面加. . ）

 


上传成功

 


打开图片获得图片地址
复制shell的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码

