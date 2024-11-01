import requests

keyword = "Python"  #在这里修改搜索关键词

try :

    kv = {'q':keyword}

    r = requests.get("http://www.so.com/s",params=kv)

    print (r.request.url)

    r .raise_for_status()

    print(len(r.text))

except :

    print ("爬取失败")


#360的关键词接口：http://www.so.com/s?q=keyword
