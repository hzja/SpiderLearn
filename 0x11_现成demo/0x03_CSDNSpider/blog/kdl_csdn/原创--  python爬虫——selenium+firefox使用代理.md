# 原创
：  python爬虫——selenium+firefox使用代理

# python爬虫——selenium+firefox使用代理

本文中的知识点：

### 搭建开发环境：

PS：安装了的同学可以跳过了接着下一步，没安装的同学还是跟着我的步骤走一遍

##### 安装selenium库

```
pip install selenium

```

##### 安装[firefox geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.26.0)

这里要注意要配置**系统环境**，把firefox geckodriver解压后放到python路径的Scripts目录下，跟pip在一个目录下。<br/> 这里可以教大家一个查看python安装路径的命令

```
# windows系统，打开cmd
where python
# linux系统
whereis python

```

#### [火狐浏览器](http://www.firefox.com.cn/)

安装火狐官方浏览器

---


### 代码样例

以请求百度为例

```
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox = webdriver.Firefox()
firefox.get('https://www.baidu.com/')
print(firefox.page_source)
firefox.close()
firefox.quit()

```

结果如下<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/39bcf97881226421a8cd06e42b8c4f7f.png"/><br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/9b85ad9b95cc7f825035951b0b105da1.png"/>

##### 使用代理

```
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

profile = webdriver.FirefoxProfile()
proxy = '42.51.13.68:16816'
ip, port = proxy.split(":")
port = int(port)
# 不使用代理的协议，注释掉对应的选项即可
settings = {
    'network.proxy.type': 1,  # 0: 不使用代理；1: 手动配置代理
    'network.proxy.http': ip,
    'network.proxy.http_port': port,
    'network.proxy.ssl': ip,  # https的网站,
    'network.proxy.ssl_port': port,
}
# 更新配置文件
for key, value in settings.items():
    profile.set_preference(key, value)
profile.update_preferences()


options = Options()
firefox = webdriver.Firefox(firefox_profile=profile, options=options)
firefox.get('http://dev.kdlapi.com/testproxy')
print(firefox.page_source)
firefox.close()
firefox.quit()
    

```

运行下，结果如下图<br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/9ee1aca77515470080c278f2f5099b36.png"/><br/> <img alt="在这里插入图片描述" src="https://i-blog.csdnimg.cn/blog_migrate/f636afcf9a83ab158dbd48dfadd22dc7.png"/>

### 进阶学习
