import requests
import time
# 爬取失败，缺少js参数,返回401未授权访问
url = "https://gdtv-api.gdtv.cn/api/search/v1/news"
payloads = {'keyword': '七十二家房客', 'pageNum': '4', 'pageSize':'15'}
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '67',
    'Content-Type': 'application/json',
    'Host': 'gdtv-api.gdtv.cn',
    'Origin': 'https://www.gdtv.cn',
    'Referer': 'https://www.gdtv.cn/',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76",
    "X-Itouchtv-Ca-Key": "89541443007407288657755311869534",
    "X-Itouchtv-Ca-Signature": "2ChooT/sckdOHEG75luWBGnXZn24skH8G0ir9f32idA=",
    "X-Itouchtv-Ca-Timestamp": str(int(time.time())),
    "X-Itouchtv-Client": "WEB_PC",
    "X-Itouchtv-Device-Id": "WEB_09d0ea60-f4d2-11ee-9329-e958638e0d08"
}
response = requests.post(url, data=payloads, headers=headers)
print(response.status_code)