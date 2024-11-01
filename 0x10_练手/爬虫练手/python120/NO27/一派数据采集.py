import requests
import threading
from queue import LifoQueue
import time
import random

# 初始化一个队列
q = LifoQueue(maxsize=0)
# 批量添加数据
for page in range(1, 7):
    # https://sspai.com/api/v1/bullet/search/page/get?type=0&limit=10&offset=0&created_at=0
    q.put('https://sspai.com/api/v1/bullet/search/page/get?type=0&limit=10&offset={}&created_at=0'.format((page-1)*10))


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


# 储存数据
def save(text):
    with open(f'{time.time()}.json', 'a+', encoding='utf-8') as f:
        f.write(text)
    print(text, "--- 保存成功")


if __name__ == "__main__":
    while q.qsize() > 0:
        url = q.get()
        q.task_done()
        res = requests.get(url=url, headers=get_headers(), timeout=10)
        save(res.text)

    q.join()
    print("所有任务都已完成")
