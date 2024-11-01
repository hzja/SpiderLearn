# 原创
：  HVV WPS0day复现

# HVV WPS0day复现

**HVV 第一天 WPS0day复现**<br/> 第一天hvv大家应该都看到了这个wps的0day的情报了吧：

“近期监测到 WPS For Windows 部分版本存在远程代码执行漏洞，攻击者可利用该漏洞在受害者目标主机上执行任意代码，控制主机等。<br/> 影响版本：<br/> WPS Office 2023 个人版 低于12.1.0.15120（含）<br/> WPS Office机构版本（如专业版、专业增强版） 低于11.8.2.12055（含）”

现在就尝试复现一下这个漏洞，在苦苦的寻找后找到了相关的poc：<br/> 下载链接先放上来：[https://pan.baidu.com/s/1pGesjeykUZHqW0VLJnkE7w?pwd=xaws](https://pan.baidu.com/s/1pGesjeykUZHqW0VLJnkE7w?pwd=xaws) 提取码：xaws

> 
注意不是钓鱼，不是钓鱼，介意者请勿下载！！！！！！！！！。


复现用到的wps版本也在下载链接中，各位可自行下载。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/30ded96dd4494b4f9b9e9e9bc27f4886.png"/><br/> 在poc目录下启动http服务,python3启动http服务命令如下，其他版本可能有所不同，可自行搜索。

```
python3 -m http.server 80

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6eec220de38d4b3c9136476481bed02d.png"/><br/> 修改hosts文件，目录一般在`C:\Windows\System32\drivers\etc`<br/> 在hosts文件后加上

```
127.0.0.1 clientweb.docer.wps.cn.cloudwps.cn

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/04f283d239b14ebd9d4d7fd437d5c53d.png"/><br/> 没有权限可先右键-&gt;属性-&gt;用户里面加上user修改属性。<br/> 用WPS打开poc，跳计算器。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6e56207a8a534f0eb28165d4176df01f.png"/><br/> 结束，撒花。
