# 原创
：  【网络安全带你练爬虫-100练】第16练：使用session发送请求

# 【网络安全带你练爬虫-100练】第16练：使用session发送请求

**目录**

[一、目标1：使用seesion进去请求](#%E4%B8%80%E3%80%81%E7%9B%AE%E6%A0%871%EF%BC%9A%E4%BD%BF%E7%94%A8seesion%E8%BF%9B%E5%8E%BB%E8%AF%B7%E6%B1%82)

[二、网络安全O](#%E4%B8%89%E3%80%81%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%B0%8F%E5%9C%88%E5%AD%90)

---


## 一、目标1：使用seesion进去请求

（1）应用：

通过创建会话（session）对象来请求并爬取返回的数据包

情景：需要登录才能爬取的网站

作用：会话对象可以在多个请求之间保持登录状态

---


（2）步骤：

第一步：创建session对象

第二步：模拟登录，获取到session

第三步：携带cookie，使用session进行爬取

第四步：数据包的处理

---


（3）代码部分：

```
import requests

data = {}
headers1={}

#part1:
# 创建一个session对象
session = requests.Session()

#part2:
# 发送POST请求（登录,数据包我就不带了，简写一下）
response = session.post(login_url，json=data)


#part3:
#需要携带cookie
headers2={}

# 发送GET请求进行爬取
response = session.get('https://baidu.com')
# 设置响应的编码方式为UTF-8
response.encoding = 'utf-8'
# 获取返回的数据包

#part4:
data = response.text
print(data)
# 处理数据包
# ...

# 关闭session
session.close()
```

---


---


> 
<h2>二、网络安全O</h2>

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)
[GitHub - BLACKxZONE/Treasure_knowledge<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)


