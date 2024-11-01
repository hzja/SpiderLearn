# 原创
：  【网络安全带你练爬虫-100练】第12练：pyquery解析库提取指定数据

# 【网络安全带你练爬虫-100练】第12练：pyquery解析库提取指定数据

**目录**

[一、目标1、基础/环境的准备工作](#%E4%B8%80%E3%80%81%E7%9B%AE%E6%A0%871%E3%80%81%E5%9F%BA%E7%A1%80%2F%E7%8E%AF%E5%A2%83%E7%9A%84%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)

[二、目标2：开始使用pyquery](#%E4%BA%8C%E3%80%81%E7%9B%AE%E6%A0%872%EF%BC%9A%E5%BC%80%E5%A7%8B%E4%BD%BF%E7%94%A8pyquery)

[三、目标3：提取到指定的数据](#%E4%B8%89%E3%80%81%E7%9B%AE%E6%A0%873%EF%BC%9A%E6%8F%90%E5%8F%96%E5%88%B0%E6%8C%87%E5%AE%9A%E7%9A%84%E6%95%B0%E6%8D%AE)

[四、目标3：通过列表的形式获取指定数据](#%E7%9B%AE%E6%A0%873%EF%BC%9A%E9%80%9A%E8%BF%87%E5%88%97%E8%A1%A8%E7%9A%84%E5%BD%A2%E5%BC%8F%E8%8E%B7%E5%8F%96%E6%8C%87%E5%AE%9A%E6%95%B0%E6%8D%AE)

[五、扩展：其他方法](#%E6%89%A9%E5%B1%95%EF%BC%9A%E5%85%B6%E4%BB%96%E6%96%B9%E6%B3%95)

[六、网络安全O](#%E4%B8%89%E3%80%81%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%B0%8F%E5%9C%88%E5%AD%90)

---


## 一、目标1、基础/环境的准备工作

1、文档：

PyQuery解析库的使用，我们可以对比jQuery来使用

[jQuery API 中文文档<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N658"/>https://www.94xh.com/](https://www.94xh.com/)

2、环境：

安装pyquery（或者直接在pycharm上安装）

```
pip install pyquery
```

3、定位

```
&lt;li&gt;
    &lt;div class="A"&gt;
        &lt;div id="B"&gt;
```

定位li---&gt;'li'

定位&lt;div class="A"&gt;---&gt;'li .A'

定位&lt;div id="B"&gt;---&gt;'li .A #B'

(与顺序无关，与标签有关)

<br/>  

---


---


## 二、目标2：开始使用pyquery

1、打印head数据

```
from pyquery import PyQuery as pq

doc = pq(url='http://www.baidu.com')
print(doc('head'))
```

head数据被打印出来了，其实可以看见汉字是出现了乱码的

2、编码：

解决乱码问题（就是使用utf-8编码，来解决中文乱码）

```
import requests
from pyquery import PyQuery as pq

response = requests.get('http://www.baidu.com')
content = response.content.decode('utf-8')
doc = pq(content)
print(doc('head'))
```

没有了乱码问题

 

3、提取对应属性

会提取所有满足条件的div标签

 

.official-newsbd爬取所有&lt;div class="official-newsbd"&gt;<img alt="" height="1030" src="https://img-blog.csdnimg.cn/b83862637df944e8bb3538b1261b7f30.png" width="1200"/>

 

```
import requests
from pyquery import PyQuery as pq

response = requests.get('https://www.chinaz.com/')
content = response.content.decode('utf-8')
doc = pq(content)
print(doc('.official-newsbd'))
```

 

---


---


## 三、目标3：提取到指定的数据

1、目标：

提取所有列表图片的相关信息

2、全提取： 

提取所有的&lt;div class="thumb"&gt;

```
import requests
from pyquery import PyQuery as pq

response = requests.get('https://www.chinaz.com/')
content = response.content.decode('utf-8')
doc = pq(content)
items = doc('.thumb')

print(item)
```

运行结果

 

3、逻辑提取：

这个是一步一步往下走提取内容

```
import requests
from pyquery import PyQuery as pq

response = requests.get('https://www.chinaz.com/')
content = response.content.decode('utf-8')
doc = pq(content)
items = doc('.official-newsbd')
item = items.find('.thumb')

print(item)
```

运行结果

4、列表数据提取

`children()`是一个函数或方法，用于获取一个元素的所有子元素

```
item = items.children()
```

---


---


## 四、目标3：通过列表的形式获取指定数据

假设我们要提取到链接URL

1、找到最小子标签

首先我们先到最小子标签

（可以不用逻辑一步一步往下走，也可以直接找到它）

```
import requests
from pyquery import PyQuery as pq

response = requests.get('https://www.chinaz.com/')
content = response.content.decode('utf-8')
doc = pq(content)
items = doc('.official-newsbd')
item = items.find('.thumb')
i = item('a')

print(i)
```

 

2、for循环-提取标签内URL

关键代码

（其实 实现的方法各种各样）

```
.attr('href')

.attr.href
```

完整代码

```
import requests
from pyquery import PyQuery as pq

response = requests.get('https://www.chinaz.com/')
content = response.content.decode('utf-8')
doc = pq(content)
items = doc('.official-newsbd')
item = items.find('.thumb')
for i in item:
    b = pq(i)('a')
    print(b.attr('href'))
```

改进前：

```
items = doc('.official-newsbd')
item = items.find('.thumb')
```

 改进后：

```
item = doc('.official-newsbd .thumb')
```

3、获取文本

关键代码

```
b.text()
```

（我这个目标标签没有文本去提取）

---


---


## 五、扩展：其他方法

1、兄弟类

<br/> siblings() 方法返回一个 PyQuery 对象，包含了当前元素的所有同级元素。这些同级元素是当前元素的直接兄弟节点（相同父节点下的其他子节点），不包括当前元素本身

```
from pyquery import PyQuery as pq

html = '''
&lt;div&gt;
  &lt;p class="first"&gt;First paragraph&lt;/p&gt;
  &lt;p class="second"&gt;Second paragraph&lt;/p&gt;
  &lt;p class="third"&gt;Third paragraph&lt;/p&gt;
&lt;/div&gt;
'''

doc = pq(html)
elem = doc('.second')

siblings = elem.siblings()
print(siblings)
```

2、父类

parent() 方法返回一个 PyQuery 对象，包含了当前元素的直接父级元素。父级元素是指当前元素的上一级节点，即当前元素的父节点<br/>  

```
from pyquery import PyQuery as pq

html = '''
&lt;div class="parent"&gt;
  &lt;p&gt;Child paragraph&lt;/p&gt;
&lt;/div&gt;
'''

doc = pq(html)
child = doc('p')

parent = child.parent()
print(parent)
```

---


---


## 六、网络安全O

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
