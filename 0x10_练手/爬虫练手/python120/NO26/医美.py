import requests
import threading
from queue import Queue
from lxml import etree
import time
import random

# 初始化一个队列
q = Queue(maxsize=0)
# 批量添加数据
for page in range(1, 4):
    q.put('https://www.huaroo.net/d/pg_{}/'.format(page))

# 获取头文件


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
        "user-agent": ua,
        "referer": "https://www.baidu.com"
    }
    return headers

# 格式化数据


def format(text):
    element = etree.HTML(text)
    # print(element)
    article_list = element.xpath('//div[contains(@class,"article_list")]')
    # print(article_list)
    wait_save_str = ""
    for article in article_list:

        title = article.xpath(
            "./a/div/div[@class='article_title']/text()")[0].strip()
        hospital = article.xpath(
            "./a/div/div[@class='hospital_list_content mt10 oh']/div[1]/text()")[0].strip()
        duties = article.xpath(
            "./a/div/div[@class='hospital_list_content mt10 oh']/div[2]/text()")[0].strip()
        practice = article.xpath(
            "./a/div/div[@class='hospital_list_content mt10 oh']/div[3]/text()")[0].strip()
        project = article.xpath(
            "./a/div/div[@class='hospital_list_content mt10 oh']/div[4]/text()")[0].strip()
        wait_save_str += f"{title},{hospital},{duties},{practice},{project}\n"
    save(wait_save_str)
# 储存数据


def save(wait_save_str):
    with open('./医美2.csv', 'a+', encoding='utf-8') as f:
        f.write(wait_save_str)
    print(wait_save_str, "---保存成功")


# 爬虫请求与解析入口
def run():
    while q.qsize() > 0:
        url = q.get()
        q.task_done()
        # print(url)
        res = requests.get(url=url, headers=get_headers(), timeout=10)
        format(res.text)
        


l = []
for i in range(2):
    t = threading.Thread(target=run)
    l.append(t)
    t.start()

for p in l:
    p.join()

print("多线程执行完毕")

q.join()
print("所有线程运行完毕")
