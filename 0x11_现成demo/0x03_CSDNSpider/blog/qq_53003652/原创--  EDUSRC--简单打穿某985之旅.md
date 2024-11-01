# 原创
：  EDUSRC--简单打穿某985之旅

# EDUSRC--简单打穿某985之旅

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

今天菜鸡又来打edu了，挑战一下某顶尖985，试一下他们的网络安不安全（狗头）<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3620b558ed2546bc8286bd170a04d669.png"/>

### 一.打点

对该大学进行了一大波信息收集，竟然找到了前几天刚复现的confluence。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/54ebc373dbc7656881da17a1a567a6b4.jpeg"/><br/> 一波熟练的操作成功添加了用户，不知道的可以去看我之前的复现<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1056d0736e9eaf767a02089a1e1189cb.jpeg"/><br/> 新建管理员<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9abc9438209dc2114ef170a3e9e75101.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d097af38515a4c264f73ae85ec6f4750.jpeg"/><br/> 成功成功，直接登录梭哈<br/> 找到一个域名，再次确认资产<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/dcd82312b3ed637e7973fd1448e00df8.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/306f378969259f7705f91732aa6432cc.jpeg"/><br/> 这里面可是有好东西的，不看不知道，一看吓一跳，一大堆内网资产和设备账号密码！

### 二:梭哈资产

内网的资产就不展示了，这里打点一些公网服务<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/c34645c8d275b2086e9d6901d2debf60.jpeg"/><br/> 这心也太大了，直接账号密码放出来，nacos竟然也放在公网上这是我没想到的。<br/> **nacos**：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/21aa10d77f20120a773c0f44d5108d2b.jpeg"/><br/> 直接登录进来，按经验来讲，nacos就是内网大杀器，什么都放里面，找找看<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9d72dc8c21b4b5baa44b78f1b9b36d34.jpeg"/><br/> 好好好，数据库直接拿下<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/29e4e5cff830782a5727f200daee31cd.jpeg"/><br/> 点到为止<br/> **radis：**<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e68616c7174cd7223bc7018724290983.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/3a8bc1e91c5a4279a13e81d58bf94d47.jpeg"/><br/> mysql里找到了密码本，麻了，要是攻防上分和喝水。<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a3fd5f3afd509e8086255d36022b2845.jpeg"/><br/> radis写公钥，直接getshell，不展示了<br/> postgresql：<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a582434ac546e0c908947148eab503fa.jpeg"/><br/> 心也太大了，这么多资产安装配置过程全部写的明明白白<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/43a3fc07f858e73a1f0771dd0fe5ae46.jpeg"/><br/> 来来回回拿下了几十个资产，可以直接打进内网，点到为止，几乎都是nacos泄露的，所以一定要把nacos放在内网中啊！！
