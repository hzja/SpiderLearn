# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlencode
from requests import codes
import os
from multiprocessing.pool import Pool
from bs4 import BeautifulSoup as bsp
import json
import time
import re

"""
info:
author:CriseLYJ
github:https://github.com/CriseLYJ/
update_time:2019-3-7
可以登录运行，就是数据暂时获取不了，需要经过修改
"""


def get_index(offset):
    base_url = 'http://www.guokr.com/apis/minisite/article.json?'
    data = {
        'retrieve_type': "by_subject",#retrieve，检索;subject,主题;
        'limit': "20",
        'offset': offset,#offset,偏移量
    }
    url = base_url + urlencode(data)#urlencode：返回字符串，此字符串中除了-_.之外的所有非字母数字字符都将被替换成百分号（%）后跟两位十六进制数，空格则编码为加号（+）
    # print(url)
    try:
        resp = requests.get(url)
        if codes.ok == resp.status_code:#codes.ok，requests库内置的状态码查询对象
            return resp.json()#resp.json()是把json数据转换成字典
    except requests.ConnectionError:
        return None


# 解析出文章的url
def get_url(json):
    if json.get('result'):
        result = json.get('result')#json.get()方法用于获取json中的数据
        for item in result:
            if item.get('cell_type') is not None:
                continue
            yield item.get('url')#带有yield的函数是一个迭代器，函数返回某个值时，会停留在某个位置，返回函数值后，会在前面停留的位置继续执行， 直到程序结束
    """
    try:
        result=json.load(json)
        if result:
            for i in result.get('result'):
                yield i.get('url')
    """


# 解析文章详情页
def get_text(url):
    html = requests.get(url).text
    print(html)
    soup = bsp(html, 'lxml')
    title = soup.find('h1', id='articleTitle').get_text()
    autor = soup.find('div', class_="content-th-info").find('a').get_text()
    article_content = soup.find('div', class_="document").find_all('p')
    all_p = [i.get_text() for i in article_content if not i.find('img') and not i.find('a')]  # 去除标签
    article = '\n'.join(all_p)#.join()函数，用于连接字符串数组，将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
    yield {"title": title, "autor": autor, "article": article}


def save_article(content):
    try:
        if content.get('title'):
            file_name = str(content.get('title')) + '.txt'
            with open(file_name, 'w', encoding='utf-8') as f:
                # f.write(json.dumps(content,ensure_ascii=False))
                f.write('\n'.join([str(content.get('title')), str(content.get('autor')), str(content.get('article'))]))
                print('Downloaded article path is %s' % file_name)
        else:
            file_name = str(content.get('title')) + '.txt'
            print('Already Downloaded', file_name)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % content)


def main(offset):
    result = get_index(offset)
    all_url = get_url(result)
    for url in all_url:
        article = get_text(url)
        for art in article:
            # print(art)
            save_article(art)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    for i in range(GROUP_START, GROUP_END + 1):
        main(offset=i * 20 + 18)
        time.sleep(1)
