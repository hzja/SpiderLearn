import requests

from queue import Queue
import random
import threading
import time


def get_headers():
    user_agent_list = [
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
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent, 'referer': 'https://sucai.gaoding.com/'}
    return headers


# 生产者线程
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    # 测试爬取 3 页，实际采集的时候，可以放大到100页
    def run(self):
        # 测试数据，爬取3页
        for i in range(1, 101):
            print("线程名: %s，序号：%d， 正在向队列写入数据 " % (self.getName(), i))
            url = 'https://api-sucai.gaoding.com/api/search-api/sucai/templates/search?q=&sort=&colors=&styles=&filter_id=1617130&page_size=100&page_num={}'.format(
                i)
            res = requests.get(url=url, headers=get_headers(), timeout=5)
            if res:
                data = res.json()
                for item in data:
                    title = item["title"]
                    img_url = item["preview"]["url"]
                    self.data.put((title, img_url))
        print("%s: %s 写入完成!" % (time.ctime(), self.getName()))


# 消费者线程
class Consumer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        while True:
            val = self.data.get()
            if val is not None:
                print("线程名：%s，正在读取数据：%s" % (self.getName(), val))
                title, url = val
                res = requests.get(url=url, headers=get_headers(), timeout=5)
                if res:
                    try:
                        with open(f"./imgs/{title}.png", "wb") as f:
                            f.write(res.content)
                            print(f"{val}", "写入完毕")
                    except Exception as e:
                        pass

# 主函数
def main():
    queue = Queue()
    producer = Producer('生产者', queue)
    consumer = Consumer('消费者', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('所有线程执行完毕')


if __name__ == '__main__':
    main()