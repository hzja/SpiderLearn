import threading
import requests
import random

class Common:
    def __init__(self):
        pass

    def get_headers(self):
        uas = [
            "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
            "你自己的UA值，或者可以从之前的博客中获取"
        ]
        ua = random.choice(uas)
        headers = {
            "user-agent": ua,
            "referer": "https://www.baidu.com"
        }
        return headers


def run(index, url, semaphore, headers):
    semaphore.acquire()  # 加锁
    res = requests.get(url, headers=headers, timeout=5)
    res.encoding = 'utf-8'
    text = res.text
    save(index,text)
    semaphore.release()  # 释放

# 存储的数据中文进行了 UNICODE 编码，分析的时候注意转化
def save(index, text):
    with open(f"./非遗数据/{index}.json", "w", encoding="utf-8") as f:
        f.write(f"{text}")
    print("该URL地址数据写入完毕")


if __name__ == '__main__':
    c = Common()
    url_format = 'http://www.ihchina.cn/Article/Index/getProject.html?province=&rx_time=&type=&cate=&keywords=&category_id=16&limit=10&p={}'
    # 拼接URL，全局共享变量，362 页直接设置，没有动态获取
    urls = [url_format.format(i) for i in range(1, 362)]
    # 最多允许5个线程同时运行
    semaphore = threading.BoundedSemaphore(5)
    for i, url in enumerate(urls):
        t = threading.Thread(target=run, args=(i, url, semaphore, c.get_headers()))
        t.start()
    while threading.active_count() != 1:
        pass
    else:
        print('所有线程运行完毕')
