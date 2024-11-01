# 转载
：  某众测黑盒0day挖掘获得奖金上限

# 某众测黑盒0day挖掘获得奖金上限

黑盒测试多细心观察每一处地方

刚开学没多久在宿舍隔离上网课，无聊看漏洞众测平台发布了新项目（好好学习，好好听课，不要逛SRC）

最高奖金一千块。然后成功报名并通过审核占到茅坑（占着茅坑不拉屎）

使用奇安信的资产收集平台直接找到用户服务系统。<br/> 访问地址：[http://user.xxx.cc/newlogin](http://user.xxx.cc/newlogin)

然后拿自己手机号码注册个账号登录进去。因为是众测，贵公司也关了好多功能不给用，所以注册的账号进去只是个空壳，并没有什么功能点。

然后点击右上角的应用中心会跳过这个系统进入下一个子站。然后使用F12大法开始审计JS，看看JS文件里有没有开发遗留的账号和链接接口。

最终在一处文件中发现一处接口：<br/>[https://xxx.xxx.cn/xxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode](https://xxx.xxx.cn/xxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode)=

访问接口：[https://xxx.xxx.cn/xxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode=](https://xxx.xxx.cn/xxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode=)

页面提示无法获取到UserCode参数：

根据UserCode参数里面的User，猜测是关联用户名，于是加个admin尝试：[https://xxx.xxx.cn/xxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode=admin](https://xxx.xxx.cn/xxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode=admin)<br/> 提示该用户没有关联GS用户，验证了我们的猜测。

然后抓包遍历用户名，发现有几个302重定向跳转了：

然后在UserCode参数后面加上遍历出来的用户名。（这里不使用真实用户名）

wsh<br/> wshwsh<br/> wshwshwsh<br/> wshwshwshwsh

选取其中一个去访问：[https://xxx.xxx.cn/xxxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode=wsh](https://xxx.xxx.cn/xxxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode=wsh)

然后302跳转进入到核心系统：[https://xxxxx.xxxx.cn/xxxxx/web/gsprtf/main.aspx](https://xxxxx.xxxx.cn/xxxxx/web/gsprtf/main.aspx)?

然后进入应用里面查看，全是合同等敏感数据，还可对其增删改查。

看到了我最喜欢的报账功能：

里面的功能模块还有很多可以测。但是因为系统比较敏感，就不做多余的测试（其实是奖金池奖金不多了）。然后提交漏洞获取赏金，点到为止。

最后去fofa指纹识别一下，发现是一个通用漏洞（意外收获），但是使用的资产不是特别多：

随便找一个站测试：

贴上跟前面一个系统一样的接口：[https://xx.xxx.com.cn/xxxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode=](https://xx.xxx.com.cn/xxxxx/web/singlelogin.aspx?AuthType=UserMap&amp;AppCode=BI&amp;UserCode=)

得到一样的结果。证明了通用性。

**如果文章对你有帮助，欢迎关注、点赞、收藏一键三连支持以下哦！<br/> 想要一起交流学习的小伙伴可以加zkaq222（备注CSDN，不备注通不过哦）进入学习，共同学习进步 **
