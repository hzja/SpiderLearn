from queue import Queue
import time
import threading
import requests
from lxml import etree
import random


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


# 热门话题列表页待抓取链接
hot_subjects = Queue(maxsize=0)
for i in range(1, 11):
    url = f'https://www.jisilu.cn/topic/square/id-hot__feature_id-__page-{i}'
    hot_subjects.put(url)


# 初始化一个队列
q_data_ids = Queue(maxsize=0)

# 生产者


def producer():
    while hot_subjects.qsize() > 0:
        list_url = hot_subjects.get()
        hot_subjects.task_done()

        print("正在解析：", list_url)
        # 获取分页地址
        res = requests.get(list_url, headers=get_headers(), timeout=3)
        element = etree.HTML(res.text)
        data_ids = element.xpath('//a[@class="aw-topic-name"]/@data-id')
        for data_id in data_ids:
            q_data_ids.put(data_id)


# 消费者
def consumer():

    while True:
        # 取一个分类ID
        data_id = q_data_ids.get()
        q_data_ids.task_done()
        if data_id is None:
            break

        start_page = 1
        url = f'https://www.jisilu.cn/question/ajax/discuss/sort_type-new__topic_id-{data_id}__page-{start_page}'
        res = requests.get(url=url, headers=get_headers(), timeout=5)
        text = res.text
        while len(text) > 0:

            url = f'https://www.jisilu.cn/question/ajax/discuss/sort_type-new__topic_id-{data_id}__page-{start_page}'
            res = requests.get(url=url, headers=get_headers(), timeout=5)
            print(res.url)
            text = res.text
           
            start_page += 1
            if len(text)>0:
                element = etree.HTML(res.text)
                titles = element.xpath('//h4/a/text()')
                urls = element.xpath('//h4/a/@href')
                names = element.xpath('//a[@class="aw-user-name"]/text()')
                data = zip(titles,names,urls)
                save_list = [f"{item[0]},{item[1]},{item[2]}\n" for item in data]
                long_str = "".join(save_list)
                with open("./data.csv","a+",encoding="utf-8") as f:
                    f.write(long_str)


# 开启2个生产者线程
for p_in in range(1, 3):
    p = threading.Thread(target=producer)
    p.start()


# 开启2个消费者线程
for p_in in range(1, 2):
    p = threading.Thread(target=consumer)
    p.start()
