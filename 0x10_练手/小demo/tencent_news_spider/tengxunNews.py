import requests
from urllib.parse import urlencode
'''失败了,没法获取数据,问题出在url没有成功拼接,很迷。。。。'''
for i in range(1,2):
    data={
        'sub_srv_id':'tech',
        'srv_id':'pc',
        'offset':i*20,
        'limit':20,
        'strategy':1,
        'ext':{"pool":["top"],"is_filter":10,"check_type":True}
    }
    url = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?'
    for key,value in data.items():
        if str(key)=='ext':
            url = url + str(key) + '=' + str(value)
        else:
            url = url + str(key) + '=' + str(value) + '&'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
print(url)
response = requests.get(url,headers=headers)
res = response.json()
print(response.content)