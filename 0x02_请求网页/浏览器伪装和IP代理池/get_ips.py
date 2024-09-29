# import os
# import requests
# from bs4 import BeautifulSoup
# import threading
# import time
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
# }
# page = input('请问想爬取多少页IP代理：')
# urls = []
# proxies = []
#
# for i in range(2,int(page)+1):
#     url = 'https://www.kuaidaili.com/free/inha/%s/' % (i)
#     urls.append(url)
#     print(url)
#
# def craw(url):
#     print('现在爬取：%s'%(url))
#     time.sleep(2)
#     html = requests.get(url,headers = headers)
#     return html.text
#
# def parse(html):
#     global proxies
#     soup = BeautifulSoup(html,'lxml')
#     body = soup.find('tbody').find_all('tr')
#     for item in body:
#         http = item.find(name='td',attrs={"data-title":"IP"}).text #BeautifulSoup模块中find函数的新用法
#         port = item.find(name='td',attrs={"data-title":"PORT"}).text
#         leixing = item.find(name='td',attrs={"data-title":"类型"}).text
#         if leixing == 'HTTP':
#             leixing = 'http'
#             href = leixing + '://' + http + ':' + port + '/'
#             proxies.append(href)
#             print('已经爬取到：%s' %(href))

# def craw_and_parse(url):
#     html = craw(url)
#     parse(html)
#
# if __name__ == '__main__':
#     for url in urls:
#         craw_and_parse(url)

# import requests
# proxypoolurl = 'http://localhost:5555/random'
# targeturl = 'http://httpbin.org/get'
# def getrandomproxy():
#     """ get random proxy from proxypool :return: proxy """
#     return requests.get(proxypool_url).text.strip()
#
# def crawl(url, proxy):
#     """ use proxy to crawl page :param url: page url :param proxy: proxy, such as 8.8.8.8:8888 :return: html """
#     proxies = {'http': 'http://' + proxy}
#     return requests.get(url, proxies=proxies).text
#
# def main():
#     """ main method, entry point :return: none """
#     proxy = getrandomproxy()
#     print('get random proxy', proxy)
#     html = crawl(target_url, proxy)
#     print(html)
#
# if '__name__' == 'main':
#     main()

import requests

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None

def main():
    proxy = get_proxy()
    print(proxy)

if '__name__'=='__main__':
    main()