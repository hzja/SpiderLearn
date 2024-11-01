# 原创
：  Wireshark流量分析

# Wireshark流量分析

#### Wireshark流量分析

## 开始抓包

> 
打开wireshark后，按ctrl+K，勾选需要抓包的网卡<br/> 点击Start开始抓包


## wireshark过滤器表达式

> 
协议过滤



> 
IP过滤



> 
端口过滤



> 
过滤HTTP协议



> 
连接符<br/> and，or<br/> 如：tcp.port == 80 and ip.addr = 192.168.116.138


> 
过滤包长度



## wireshark着色规则

> 
点开左上角视图中的着色规则就能看到


## 数据流的追踪

> 
我们的一个完整的数据流一般都是由很多个包组成的；<br/> 所以当我们想查看某条数据包对于的数据流的话。可以选中数据，右键选择追踪流；<br/> 里面就会有tcp流、udp流、ssl流、http流。数据包属于哪种流就选择对应的流；<br/> 当我们选择了追踪流时，会弹出该流的完整的数据流还有这个数据流中包含的数据包，对话框下面可以选择数据流方向，顶部的过滤器就是该流的过滤规则


## 数据包的统计分析

> 
统计中的协议分级功能可以查看所选包协议的分布情况，帮助识别可疑协议，和不正常的网络应用程序


> 
在Endpoints窗口中，可以通过排序Bytes和Tx Bytes来判断占用带宽最大的主机


> 
Conversions窗口可以看到两个主机之间发送/接收数据包的数量、字节大小以及数据的流向情况，也可以通过排序来判断占用最大带宽的主机；<br/> 在Conversions窗口中只能看到会话的统计情况，无法看到包的具体内容；<br/> 这时可以使用快速过滤会话功能，过滤出想要查看的内容；<br/> 快速过滤会话的功能在Conversions窗口中进行操作，可以对选中的会话或者非选中的会话选择数据流向进行过滤


## 数据包的大致结构

> 



## 网络分析

### 只抓包头

> 
在进行网络分析时往往只需要知道两个节点是不是能够联通，具体的传输信息并不重要，所以抓包的时候可以设置只抓包头，这样就大大减少了数据包的大小，有利于数据分析；<br/> 设置方法：Capture（捕获）–&gt;Options（选项）–&gt;Snaplen（Snap长度）；<br/> 将这个值设置200以下就可以抓到所有网络层次的头信息了<br/> 另外也可以直接点击任务栏里的快捷键，快速设置


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514184513663.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514184520437.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### 只抓必要的包

> 
我们可以设置抓包的filter，只抓一些感兴趣的包；<br/> 设置方法：Capture（捕获）–&gt;Options（选项）–&gt;Capture Filter（捕获过滤器）<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514195848438.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
在输入框里输入规则，然后点击开始即可，比如输入<br/> dst host 220.181.38.148（捕获目标主机为220.181.38.148的数据包）<br/> 220.181.38.148是ping www.baidu.com的ip地址，不同地理位置ping的ip可能不一样，然后浏览器访问百度就可以看到我们想要的捕获结果


### 自动分析

> 
Wireshark有强大的统计分析功能，可以帮助分析人员快速统计出一些基本信息。比如点击Analyze（分析）–&gt;Expert InfoComposite（专家信息），就可以看到数据包的中的一些不同级别的信息统计，包含重传次数、链接建立次数、网络错误等，在分析网络性能时这个功能很有作用<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210514200844612.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> 单击Statistics（统计）–&gt;TCPStream Graph（TCP流图形），可以生成一些统计图表<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021051420091172.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
此外还可以统计分层信息、网络会话列表、网络端点列表、ip地址统计列表、应用层数据包信息等


### 搜索

> 
按“Ctrl+F”Wireshark也可以进行关键字搜索，选择“分组详情”后才可以搜索数据包中的内容，这样的搜索可以在CTF中也许会有意外收获

