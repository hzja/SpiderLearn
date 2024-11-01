"""目的:用于爬取https://www.kunv.cc/taotu/网站爬取beautileg模特的长腿照套图
卡点：经常被封ip
"""
import threading
import requests
import os
from bs4 import BeautifulSoup
import re
import time
import multiprocessing

headers = {
    # 'Referer': 'https://www.baidu.com/link?url=Y2R0OKsLwtjalujLdMW9uEhAL2yUGc00ro4gth7BvmV_sBElBsEhGj5aXIMFjYTR&wd=&eqid=e2b362c30001c393000000036110ce4d%22',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
}

# def get_proxypool():
#     proxypool_url = 'http://127.0.0.1:5555/random'
#     proxy = requests.get(proxypool_url).text
#     proxypool = {
#         'http':'http://' + str(proxy)
#     }
#     return proxypool

def get_total(url):#得到总页数
    time.sleep(3)
    # proxies = get_proxypool()
    response = requests.get(url,headers=headers)
    html = response.content
    soup = BeautifulSoup(html,'lxml')
    page_path = soup.find(class_='pageinfo')
    page = page_path.strong.text
    return page

def get_urls(href):#得到某一页面中所有的图片的链接
    time.sleep(3)
    # proxies = get_proxypool()
    response = requests.get(href,headers=headers)
    html = response.content
    soup = BeautifulSoup(html,'lxml')
    items = soup.find(class_='img').find_all('li')
    urls = []
    for item in items:
        url = item.a.attrs['href']
        urls.append('https://www.kunv.cc'+url)
    return urls

def craw_and_save(url):#爬取某一套图的所有图片并保存
    time.sleep(3)
    # proxies = get_proxypool()
    response = requests.get(url,headers=headers)
    html = response.content
    soup = BeautifulSoup(html,'lxml')
    items = soup.find(id='pages').find_all('li')
    text = items[0].a.text
    pages = re.findall(r'\d{1,3}',text)
    pages = int(pages[0])

    weizhi = soup.find(class_='weizhi')
    name = weizhi.h1.text
    path = '.\图片爬取\美女图'+'\\'+str(name)
    try:
        os.mkdir(path)
        os.chdir(path)
    except:
        pass

    img_weizhi = soup.find(id='img_view')
    src = img_weizhi.img.attrs['src']
    time.sleep(3)
    # proxies=get_proxypool()
    img = requests.get(src, headers=headers, stream=True)
    with open('%s\%s.jpg'%(path,name),'wb') as f:
        f.write(img.content)
    print('已经下载：%s'%name)

    url_splits = url.split('.html')
    lianjies = []
    for i in range(2,pages+1):
        lianjies.append(url_splits[0] + '_%s.html'%(i))
    for lianjie in lianjies:
        time.sleep(3)
#        proxies = get_proxypool()
        response = requests.get(lianjie,headers=headers)
        html = response.content
        soup = BeautifulSoup(html, 'lxml')
        name_weizhi = soup.find(class_='weizhi')
        name = name_weizhi.h1.text
        img_weizhi = soup.find(id='img_view')
        src = img_weizhi.img.attrs['src']
        time.sleep(3)
        img = requests.get(src, headers=headers, stream=True)
        with open('%s\%s.jpg' % (path, name), 'wb') as f:
            f.write(img.content)
        print('已经下载：%s'%name)
#
# def multi_thread(urls):#创建多线程
#     threads = []
#     for url in urls:
#         threads.append(
#             threading.Thread(craw_and_save,(url,))
#         )


def main():
    url = "https://www.kunv.cc/taotu/"
    totals = get_total(url)
    urls = get_urls(url)
    # multi_process(urls)
    # for url1 in urls:
    #     craw_and_save(url1)

    for i in range(6,int(totals)+1):
        url = "https://www.kunv.cc/taotu/1-%s.html"%(i)
        urls = get_urls(url)
        # multi_process(urls)
        for url1 in urls:
            craw_and_save(url1)
        time.sleep(3)

main()
