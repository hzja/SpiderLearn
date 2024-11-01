import requests

ur1 = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"

try :

    kv = {'user-agent':'Chrome/10'} #定义浏览器和其类别

    r = requests.get(ur1,headers=kv) #定义爬虫request请求的head中的user-agent域

    r.raise_for_status()

    r.encoding = r.apparent_encoding

    print(r. text[1000:2000] )

except :

    print ("爬取失败")
