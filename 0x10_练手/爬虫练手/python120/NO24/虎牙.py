import threading
import requests
import random

class Common:
    def __init__(self):
        pass

    def get_headers(self):
        uas = [
            "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
            "其余内容"
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
    text = text.replace('getLiveListJsonpCallback(', '')
    text = text[:-1]
    # print(text)
    # json_data = json.loads(text)
    # print(json_data)
    save(index,text)
    semaphore.release()  # 释放


def save(index, text):
    with open(f"./虎牙/{index}.json", "w", encoding="utf-8") as f:
        f.write(f"{text}")
    print("该URL地址数据写入完毕")


if __name__ == '__main__':
    # 获取总页码
    first_url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&callback=&page=1'
    c = Common()
    res = requests.get(url=first_url, headers=c.get_headers())
    data = res.json()
    if data['status'] == 200:
        total_page = data['data']['totalPage']

    url_format = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&callback=&page={}'
    # 拼接URL，全局共享变量
    urls = [url_format.format(i) for i in range(1, total_page)]
    # 最多允许5个线程同时运行
    semaphore = threading.BoundedSemaphore(5)
    for i, url in enumerate(urls):
        t = threading.Thread(target=run, args=(i, url, semaphore, c.get_headers()))
        t.start()
    while threading.active_count() != 1:
        pass
    else:
        print('所有线程运行完毕')
