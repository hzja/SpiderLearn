# 原创
：  实战| apikey泄露

# 实战| apikey泄露

今天挖小程序时测了很久，一直没有头绪，后来想要测试一下支付漏洞，但是这里却出问题了

<br/> 添加地址时我发现，当我添加一个地址时，他会显示腾讯地图的logo和一部分小图，那时候我就在想，既然这里可以调用腾讯地图，那是否会包含一个api key呢？

所以我打开bp开始抓包，点击确认时抓包

<br/> 包要一个一个放，主打的就是仔细，然后讲一个小技巧，如果在数据包里你知道某个参数很重要，如key，sessionid，admin之类，可以在bp下方的那个框里填入，然后他会高亮显示，还是很有用的

就可以提交了，思路就是这样，遇到这种敏感的logo就想想api会不会被调用，然后下方输入个key，慢慢放包就行了

> 
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


**没看够~？欢迎关注！**
