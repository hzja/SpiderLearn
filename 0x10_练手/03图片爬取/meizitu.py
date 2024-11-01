# encoding = utf-8
"""目的:爬取网站https://mmzztt.com/的照片"""
import os
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup


def header(referer):

    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }

    return headers

def get_proxypool():
    r = requests.get(url='http://127.0.0.1:5555/random')
    proxy = r.text
    proxypool={
        'http':'http://'+proxy,
    }
    print(r.text)
    return r.text

proxypool = get_proxypool()

def request_page(url):
    response = requests.get(url)
    return response.content



def get_page_urls():

    for i in range(2, 20):
        baseurl = 'https://mmzztt.com/page/{}'.format(i)
        html = request_page(baseurl)
        print(html)
        soup = BeautifulSoup(html, 'lxml')

        list = soup.find(class_='postlist').find_all('li')
        urls = []
        for item in list:
            url = item.find('span').find('a').get('href')
            print('页面链接：%s' % url)
            urls.append(url)

    return urls


def download_Pic(title, image_list):
    # 新建文件夹
    os.mkdir(title)
    j = 1
    # 下载图片
    for item in image_list:
        filename = '%s/%s.jpg' % (title, str(j))
        print('downloading....%s : NO.%s' % (title, str(j)))
        with open(filename, 'wb') as f:
            img = requests.get(item, headers=header(item),proxies=proxypool).content
            f.write(img)
        j += 1

def download(url):
    html = request_page(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find(class_='pagenavi').find_all('a')[-2].find('span').string
    title = soup.find('h2').string
    image_list = []

    for i in range(int(total)):
        html = request_page(url + '/%s' % (i + 1))
        soup = BeautifulSoup(html, 'lxml')
        img_url = soup.find('img').get('src')
        image_list.append(img_url)

    download_Pic(title, image_list)


def download_all_images(list_page_urls):
    # 获取每一个详情妹纸
    for url in list_page_urls:
        download(url)

def main():
    # 获取每一页的链接和名称
    list_page_urls = get_page_urls()

    download_all_images(list_page_urls)

main()

