# 原创
：  【网络安全带你练爬虫-100练】第9练：post提交/提取json数据包

# 【网络安全带你练爬虫-100练】第9练：post提交/提取json数据包

**目录**

[一、目标1：post提交json数据包](#%E7%9B%AE%E6%A0%871%EF%BC%9Apost%E6%8F%90%E4%BA%A4json%E6%95%B0%E6%8D%AE%E5%8C%85)

[二、目标2：接收json数据包](#%E4%BA%8C%E3%80%81%E7%9B%AE%E6%A0%872%EF%BC%9A%E6%8E%A5%E6%94%B6json%E6%95%B0%E6%8D%AE%E5%8C%85)

[三、目标3：提取指定的键值](#%E7%9B%AE%E6%A0%873%EF%BC%9A%E6%8F%90%E5%8F%96%E6%8C%87%E5%AE%9A%E7%9A%84%E9%94%AE%E5%80%BC)

[四、网络安全小圈子](#%E4%B8%89%E3%80%81%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%B0%8F%E5%9C%88%E5%AD%90)

---


## 一、目标1：post提交json数据包

（大家可以自己随便找一个，像一些登录过的网站刷新一下，基本上就有）

 

post提交的数据

将要使用post提交的json数据放到data中

```
        data = {
            '键名1'：'键值1'
            '键名2'：'键值2'
                }
```

获取请求的返回数据

```
        res = requests.post(url, data=data, headers=headers,timeout=10)

```

---


---


## 二、目标2：接收json数据包

获取的返回json数据

将其变成text格式，然后print打印

```
        if res.status == 200:
            json_data = json.loads(res.text)
            print(json_data)
        else:
            print('发包失败')
```

运行结果：

调试发现是403状态码（没有权限访问），然后跳出了

所以没有数据，无法打印出来了

（找不到好的数据包，先这样）

 

---


---


## 三、目标3：提取指定的键值

 

通过加['键名']来指定

```
        res = requests.post(url, data=data, headers=headers,timeout=10)
        json_data = json.loads(res.text)
        test1 = json_data['data']
        test2 = json_data['key_id']
        print(test1,test2)
```

如果键名内有多个[数组]时

我们需要使用[num]来选择使用第几个数组

提取内容1：['xxx'][0]

提取内容2：['xxx'][1]

```
'xxx':[
内容1
]
[
内容2
]
```

完整代码：

```
import requests
import json
from fake_useragent import UserAgent

def post_json():
    try:
        url = 'https://miao.baidu.com/abdr?_o=https%3A%2F%2Fquake.360.net'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
            'Cookie': '!!!!'
        }

        data = {
            "data":"!!!!",
            "key_id":"!!!!",
            "enc":2
                }

        res = requests.post(url, data=data, headers=headers,timeout=10)
        json_data = json.loads(res.text)
        test1 = json_data['data']
        test2 = json_data['key_id']
        print(test1,test2)


        # if res.status == 200:
        #     json_data = json.loads(res.text)
        #     print(json_data)
        # else:
        #     print('发包失败')

    except:
        return ""


if __name__ == '__main__':
    post_json()
```

---


---


## 四、网络安全小圈子

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
