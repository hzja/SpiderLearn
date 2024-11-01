import requests

url = 'https://gdtv-api.gdtv.cn/api/search/v1/news'

headers = {
        "Host": "gdtv-api.gdtv.cn",
        "Origin":"https://www.gdtv.cn",
        "Referer":"https://www.gdtv.cn/",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "acw_tc=0bdd26e617066981569778308e53f3bf9d0204619da0476e9ea95d1ab74fb0; DEVICEID=WEB_64df7380-c026-11ee-ab39-fd12bbb279be; UM_distinctid=18d5f2346175e-0fe46483f8166a-7f5d547e-1fa400-18d5f234618ac1; CNZZDATA1278159012=545433178-1706698164-https%253A%252F%252Fcn.bing.com%252F%7C1706699351",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76",
        "X-ITOUCHTV-CLIENT": "WEB_PC",
        "X-ITOUCHTV-Ca-Key": "89541443007407288657755311869534",
        "X-ITOUCHTV-Ca-Signature": "2Vwp6Y9ahfHjXzO3QNDf7/Gtg0WEpzscFrH7cF4EfcE=",
        "X-ITOUCHTV-Ca-Timestamp": "1706700795746",
        "X-ITOUCHTV-DEVICE-ID": "WEB_64df7380-c026-11ee-ab39-fd12bbb279be"
    }

params = {
        'keyword': "七十二家房客",
        'pageNum': 3,
        'type': 3,
        'pageSize': 15
    }

response = requests.post(url, headers=headers, params=params)

print(response.status_code)

print(response.text)
