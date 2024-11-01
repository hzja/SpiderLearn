import requests
r = requests.get("https://www.baidu.com/")
print(r.status_code)
r.encoding = 'utf-8'
r.text
