# 原创
：  【HTML中隐写】Snow免安装、网站版，基本使用方法

# 【HTML中隐写】Snow免安装、网站版，基本使用方法

**目录**

[Snow](#Snow)

[准备阶段：](#%E5%87%86%E5%A4%87%E9%98%B6%E6%AE%B5%EF%BC%9A)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[使用方法：](#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[Options（选项）](#Options%EF%BC%88%E9%80%89%E9%A1%B9%EF%BC%89)

[Examples（例子）](#Examples%EF%BC%88%E4%BE%8B%E5%AD%90%EF%BC%89)

[使用：](#%E4%BD%BF%E7%94%A8%EF%BC%9A)

[对比：](#%E5%AF%B9%E6%AF%94%EF%BC%9A)

[用浏览器打开瞅瞅](#%E7%94%A8%E6%B5%8F%E8%A7%88%E5%99%A8%E6%89%93%E5%BC%80%E7%9E%85%E7%9E%85)

[使用工具](#%E4%BD%BF%E7%94%A8%E5%B7%A5%E5%85%B7)

[换网站：](#%E6%8D%A2%E7%BD%91%E7%AB%99%EF%BC%9A)

[Decryption（解密）](#Decryption%EF%BC%88%E8%A7%A3%E5%AF%86%EF%BC%89)

[Encryption（加密）](#Encryption%EF%BC%88%E5%8A%A0%E5%AF%86%EF%BC%89)

[让我来浅试一下：](#%E8%AE%A9%E6%88%91%E6%9D%A5%E6%B5%85%E8%AF%95%E4%B8%80%E4%B8%8B%EF%BC%9A)

[总结：](#%E6%80%BB%E7%BB%93%EF%BC%9A)

---


（又是一个隐写细节，更完所有隐写工具，整合集）

以蝼蚁之行，展鸿鹄之志

## Snow

### 准备阶段：

> 
 下载地址（开源的）：
[The SNOW Home Page (darkside.com.au)](https://www.darkside.com.au/snow/)
使用Snow 的网络版：
[Snow web-page encryption/decryption (misty.com)](https://fog.misty.com/perry/ccs/snow/snow/snow.html)


（里面有Windows可执行的，无需安装的，直接用）
选择适合自己的下




### 原理：

> 
Snow 的man 手册中讲到"通过在文本文件末尾追加由制表位隔开的空格可以实现数据隐藏， 最多可以添加 7 个空格， 这使得每 8 列可以嵌入 3 位” 。
也就是说找到很多空格的地方说明隐写成功了


### 使用方法：

#### Options（选项）

> 
**-C**
如果隐藏，则压缩数据，或者如果提取，则会解压缩。
**-Q**
静音模式。如果未设置，则程序报告统计信息，例如压缩百分比和可用存储空间的数量。
**-S**
报告文本文件中隐藏消息的近似空间量。考虑线长度，但忽略其他选项。
**-p** **password**
如果设置为此，则在隐藏期间将使用此密码加密数据，或在提取期间解密。
**-l** **line-length**
在附加空格时，Snow将始终产生比此值短的线条。默认情况下，它设置为80。
**-f** **message-file**
此文件的内容将隐藏在输入文本文件中。
**-m** **message-string**
此字符串的内容将被隐藏在输入文本文件中。请注意，除非在字符串中包含一个换行符，否则在提取邮件时，否则不会打印换行符。


#### Examples（例子）

> 
以下命令将隐藏文件infile中的消息“I am lying”中，压缩，并使用密码“Hello World”加密。生成的文本将被存储在外档中。
`snow -C -m "I am lying" -p "hello world" infile outfile`

要提取消息，命令将是
`snow -C -p "hello world" outfile`
请注意，生成的消息不会被换行符终止。

为防止线包装，如果通过邮件或新闻读卡器缩进隐藏空间的文本，可以使用72或更小的线长度。
`snow -C -l 72 -m "I am lying" infile outfile`

可以使用-s选项确定文件的近似存储容量。
`snow -S -l 72 infile`


### 使用：

> 
第一步：
先将文件都放在Snow文件夹中，再进行操作
原始文件也留一个做对比





第二步：先进入到文件夹中
然后再执行隐写命令
snow.exe -C -m "flag" -p "123456" test.html


这里显示压缩了34.38%


最后显示：消息使用大约1.60％的可用空间。



### 对比：

#### 用浏览器打开瞅瞅

> 
可以说看起来一模一样



#### 使用工具

> 
用Winhex（010 Editor 我更喜欢这个软件，看起来跟舒服）对比试试


对比结果是全部一样（大无语事件右发生了） 
 <img alt="" height="929" src="https://img-blog.csdnimg.cn/0d9e22d7eda5446b8fd6ddf6725cc526.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_20,color_FFFFFF,t_70,g_se,x_16" width="1200"/>






我认为可能写入的太小了 
这次把写的变多一点

 这次占了22.07%了<img alt="" height="108" src="https://img-blog.csdnimg.cn/73693bb32b0945c1812a9e7bbe1e00e2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_17,color_FFFFFF,t_70,g_se,x_16" width="700"/>




（隐写成功，也没见你写进去，感觉是在坑孩子）

### 换网站：

> 
Snow 的网络版：
[Snow web-page encryption/decryption (misty.com)](https://fog.misty.com/perry/ccs/snow/snow/snow.html)

 Snow网页加密/解密
另请参阅applet版本jsnowapp，它可以使用本地文件而不是URL
以下使用的URL必须是直接的，即，它们不得生成重定向，否则它将无法正常工作。


<h4>Decryption（解密）</h4>
包含隐藏消息的URL：……
<h4>Encryption（加密）</h4>
隐藏消息的URL：……
要加密的消息：


#### Encryption（加密）

#### 让我来浅试一下：

> 
在本地搭建的好的靶场中新建一个进行测试




 脚本失败 脚本失败：未找到主机：localhost：8080
<img alt="" height="308" src="https://img-blog.csdnimg.cn/5e72d052174a476c98b12dc4e23a4869.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6buR6Imy5Zyw5bimKOW0m-i1tyk=,size_17,color_FFFFFF,t_70,g_se,x_16" width="710"/> 但实际上我自己是能访问的



#### 总结：

> 
虽然失败告终，但是还是搞清楚了他的写入原理
（放话：每一步都有它特殊的意义）


推荐：

[【数据隐藏】一起入门隐写吧，宝？word、图像、移动设备、文件压缩数据隐藏](https://blog.csdn.net/qq_53079406/article/details/123537834?spm=1001.2014.3001.5501)
