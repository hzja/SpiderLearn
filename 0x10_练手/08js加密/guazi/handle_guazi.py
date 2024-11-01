import requests
import execjs
import re

url = 'https://www.guazi.com/bj/buy/o1i7/#bread'

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36",
}

#首次请求返回203状态码，和JS加密文件
response = requests.get(url=url,headers=header)
print(response.text)
#设置返回的编码
response.encoding = 'utf-8'
if '正在打开中,请稍后' in response.text:
    #通过正则表达式获取了相关的字段和值
    value_search = re.compile(r"anti\('(.*?)','(.*?)'\);")
    string = value_search.search(response.text).group(1)
    key = value_search.search(response.text).group(2)
    #读取，破解的js文件
    with open('guazi.js','r') as f:
        f_read = f.read()
    #使用execjs包来封装这段JS,传入的是读取后的js文件
    js = execjs.compile(f_read)
    #调用JS文件内的函数
    js_return = js.call('anti',string,key)
    cookie_value = 'antipas='+js_return
    header['Cookie'] = cookie_value
    response_second = requests.get(url=url,headers=header)
    print(response_second.text)
else:
    print(response.text)

