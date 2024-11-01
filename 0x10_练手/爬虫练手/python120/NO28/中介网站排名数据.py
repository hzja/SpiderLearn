from queue import Queue
import time
import threading
import requests
from lxml import etree
import random
import re


def get_headers():
    uas = [
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
        "Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
        "Baiduspider-image+(+http://www.baidu.com/search/spider.htm)",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 YisouSpider/5.0 Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; Googlebot-Image/1.0; +http://www.google.com/bot.html)",
        "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Sogou News Spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Sosospider+(+http://help.soso.com/webspider.htm)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)"
    ]
    ua = random.choice(uas)
    headers = {
        "user-agent": ua
    }
    return headers


def get_total_page():
    res = requests.get(
        'https://www.zhongjie.com/top/rank_all_1.html', headers=get_headers(), timeout=5)
    element = etree.HTML(res.text)
    last_page = element.xpath("//a[@class='weiye']/@href")[0]
    pattern = re.compile('(\d+)')
    page = pattern.search(last_page)
    return int(page.group(1))


# 生产者
def producer():
    while True:
        # 取一个分类ID
        url = urls.get()
        urls.task_done()
        if url is None:
            break

        res = requests.get(url=url, headers=get_headers(), timeout=5)
        text = res.text
        element = etree.HTML(text)
        links = element.xpath('//a[@class="copyright_title"]/@href')
        for i in links:
            wait_list_urls.put("https://www.zhongjie.com" + i)


# 消费者


def consumer():
    while True:
        url = wait_list_urls.get()
        wait_list_urls.task_done()
        if url is None:
            break

        res = requests.get(url=url, headers=get_headers(), timeout=5)
        text = res.text
        element = etree.HTML(text)

        title = element.xpath('//div[@class="info-head-l"]/h1/text()')
        link = element.xpath('//div[@class="info-head-l"]/p[1]/a/text()')
        description = element.xpath('//div[@class="info-head-l"]/p[2]/text()')
        print(title, link, description)


if __name__ == "__main__":

    # 初始化一个队列
    urls = Queue(maxsize=0)
    last_page = get_total_page()
    for p in range(1, last_page + 1):
        urls.put(f"https://www.zhongjie.com/top/rank_all_{p}.html")

    wait_list_urls = Queue(maxsize=0)
    # 开启2个生产者线程
    for p_in in range(1, 3):
        p = threading.Thread(target=producer)
        p.start()

    # 开启2个消费者线程
    for p_in in range(1, 2):
        p = threading.Thread(target=consumer)
        p.start()
