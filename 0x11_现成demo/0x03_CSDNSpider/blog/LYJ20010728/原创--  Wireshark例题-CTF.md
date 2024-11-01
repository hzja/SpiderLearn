# 原创
：  Wireshark例题-CTF

# Wireshark例题-CTF

#### Wireshark例题-CTF

## 搜索

> 
题目文件：[key.pcapng](https://share.weiyun.com/BGLDMH44)


> 
题目描述：flag被盗，赶紧溯源！


> 
题目题解：<br/> ①可以只将这个数据包当做文本文件打开，比如用一些notepad++编辑器，然后直接搜索<br/> ②用Wireshark自带的搜索功能找尝试查找一些关键词（比如key、flag、shell、pass等），然后跟进可疑的数据包，根据数据包特征，很明显看出这是一个菜刀连接一句话木马的数据包，然后往下找，即可看到读取的flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514202540788.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514202550118.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 文件提取

### 例题一

> 
题目文件： caidao.pcapng


> 
题目描述：有人偷偷下载了文件！


> 
题目题解：<br/> 根据题意可能数据包中存在文件传输，尝试直接导出，选择File（文件）–&gt;Export Objexts（导出对象），然后可以看到一些协议，比如选中http就可以看到通过http传输的一些文件，在右下角有导出按钮，可生生成相应的文件。但是本题中无法用此方法直接看到被下载的文件，因为有些文件是直接通过tcp或udp协议传输的，http协议只能看到的访问的链接，但不会看到传输的内容（比如你去访问放一个链接download.php?file=test.rar，通过上述导出对象的方式看不出来下载的文件的内容的）


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021051420304775.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/202105142034432.png#pic_center"/>

> 
这个时候就需要找到那个执行下载的数据包，找到数据传输的部分再导出，比如下面这个数据包<br/> 大概是一个菜刀下载的过程，在最后一个包可以看到下载的文件，直接右键点击“导出分组字节流”，然后保存为.tar.gz文件


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514203505680.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514203811859.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
本题中最后还要使用16进制编辑器去除开头和结尾的X@Y字符，这个是菜刀的特征符号，不是文件内容


### 例题二

> 
题目文件：misc_fly.p.capng


> 
题目描述：抓到一只苍蝇！


> 
题目题解：<br/> 首先用HTTP条件过滤一下；<br/> 右键第一个包，追踪流；


> 
可以看到一些基本信息，首先这是一个POST数据包，发送了一些文件相关信息，包括名称（fly.rar）和大小（525701）等。接下来应该就是文件实际上传的数据包，将过滤条件改为：http.request.method==“POST”；


> 
从数据包的结构上看应该就是第二至第六个数据包是数据传输的过程。点开第二个可以看到MediaType的长度为131436=；<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514211954720.png#pic_center"/><br/> 第二到第五个都是一样的长度，第六个为1777，应该是剩余的最后一部分数据。但是131436*4+1777=527521！=525701，再看下第一个数据包；<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514212858993.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>


> 
都知道rar文件头应该是Rar，但是选中的数据部分前面却多出了很多，简单计算一下一共多出了364，且364*5+525701=527521，所以多出的也许是某种校验数据，在导出的时候将其忽略；<br/> 每个包都做同样的操作即可得出5个文件，再将这个文件按顺序拼接即可。拼接的话可以使用16进制编辑器手动拼接，也可以使用linux下cat命令，比如“cat 1 2 3 4 5 &gt; fly.rar”；’这道题还设置了伪加密，需要修改加密位，将0x84位置改为0x80即可；


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514214055408.png#pic_center"/><br/> 解压出来后是一个exe可执行文件，里面隐藏了一个png图片，是个二维码，扫描即可得到flag

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514214624500.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514214916636.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 信息提取

> 
题目文件： sqlmap.pcap


> 
题目描述：数据库中的flag被偷走了，好在全过程我们都有记录


> 
题目题解：<br/> 数据包记录的是sqlmap获取flag的过程，使用http &amp;&amp; http contains"flag"过滤一下


> 
将其payload解码一下是这样的，判断其ascii码是否大于64<br/> id=1 AND ORD(MID((SELECTIFNULL(CAST(`value` AS CHAR),0x20) FROM isg.flags ORDER BY `value` LIMIT0,1),1,1))&gt;64<br/> 然后一直到836个包判断第一位ascii码值大于72，然后开始从高到低递减，判断其ascii码不大于73，则第一位的ascii码值是73，对应的字符为I。以此类推，其flag为ISG{BLind_SQl_InJEcTi0N_DeTEcTEd}。本题需要一定的耐心和SQL注入基础。但是这么做可能有些繁琐，其实pcap数据包可以直接用文本编辑器打开，就可以看到其中的http请求


> 
所以可以使用字符串搜索的方式直接去查找其中的语句，然后判断flag，首先将原数据包中的http请求导出来，另存为sqli.pcap<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021051423395223.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

