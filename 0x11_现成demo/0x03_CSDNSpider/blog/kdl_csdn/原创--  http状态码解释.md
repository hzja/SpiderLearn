# 原创
：  http状态码解释

# http状态码解释

> 
之前我们讲了python的一些爬虫库的使用，有的同学可能还不太明白http状态码的意思，比如200,301等等。


这次咋们就说说，解释下http状态码。

---


本文知识点：
1. 常见的http状态码1. 进阶学习
### 常见的http状态码

不用说的特别多，就说一些常见的。大家对这个有一个认识即可。

#### 查看状态码

怎么看这个状态码呢？有会的同学吗？会的请点个赞（狗头.jpg），让我看到下，不会也没关系，手把手教学，跟着做就好了。

##### 浏览器的方式，以谷歌为例

比如我们访问一篇博文，这里以访问我之前写的[requests的使用教程](https://blog.csdn.net/kdl_csdn/article/details/103962098)为例，好的，开始了。

按下F12——[打开这篇博文](https://blog.csdn.net/kdl_csdn/article/details/103962098)（单击下）

如图，这里注意要切换到**Network**里来，看到了吗，这里的Status就是http 状态码。<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/27b78e1cc921f8ad951cad8db765dd81.png"/>

##### 代码的方式

```
import requests

r = requests.get('https://blog.csdn.net/kdl_csdn/article/details/103962098')
print(r.status_code)

```

结果如图<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/ad7a5a0ca3cbc5105dd9211fd5329282.png"/><br/> 看到了吧，这两种方式常用方式，非常方便。<br/> 大家有没有注意到，http状态码是200。这个意思就是OK的意思，正常，没问题。就跟你跟别人打ok的手势一样，ojbk。服务器也给咋们回应了，200么得问题。<br/> 再来试试其他的，话说找一些特定的http状态码还不太好找。。。<br/> 我直接总结下吧，大家碰到了可以也好个认识，至少认识它，是吧。

常见的一些状态码就是这些，200刚才咋们都见过了，正常的意思。<br/> 301与302是重定向到另一个页面，这里怎么能出现呢，找个登录的网站，就以csdn为例吧，发送个post请求，或者点评论试试，一般返回的http状态码就是301或302。<br/> 403一般是禁止访问，或者是爬虫爬的时候被限制了，不让你爬<br/> 404 找不到资源，页面不存在；404也好找，csdn的博文url，随便改下，我改好了，用我的吧，[点击打开](https://blog.csdn.net/kdl_csdn/article/details/103962012)<br/> 502 服务器的内部出了问题

### 进阶学习
