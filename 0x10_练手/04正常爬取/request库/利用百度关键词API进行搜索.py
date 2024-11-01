import requests

keyword="Python"  #在这里修改百度搜索关键词

try :

    kv={'wd':keyword}

    r = requests.get("http://www.baidu.com/s",params=kv)

    print(r.request.url)

    r.raise_for_status()

    print(len(r.text))

except :

    print ("爬取失败")




# 百度的关键词接口：http://www.baidu.com/s?wd=keyword
