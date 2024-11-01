import threading
from threading import Lock,Thread
import random,requests
from lxml import etree

def get_headers():
    uas = [
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    ]
    ua = random.choice(uas)
    headers = {
        "user-agent": ua,
        "referer": "https://www.baidu.com/"
    }
    return headers


def run(url,semaphore):
    headers = get_headers()
    semaphore.acquire()   #加锁
    res = requests.get(url,headers=headers,timeout=5)
    if res:
        text = res.text
        element = etree.HTML(text)
        titles = element.xpath('//a[@class="book-item-name"]/text()')
        authors = element.xpath('//a[@class="author"]/text()')
        weakens = element.xpath('//a[@class="g-user-shutdown"]/text()')
        save(url,titles,authors,weakens)


    semaphore.release()    #释放

def save(url,titles,authors,weakens):
    data_list = zip(titles,authors,weakens)
    for item in data_list:
        with open("./data.csv","a+",encoding="utf-8") as f:
            f.write(f"{item[0]},{item[1]},{item[2]}\n")
    print(url,"该URL地址数据写入完毕")
if __name__== '__main__':
    lock = Lock()
    url_format = 'https://www.lrts.me/book/category/1/recommend/{}/20'
    # 拼接URL，全局共享变量
    urls = [url_format.format(i) for i in range(1, 1372)]
    l = []
    semaphore = threading.BoundedSemaphore(5)   # 最多允许5个线程同时运行
    for url in urls:
        t = threading.Thread(target=run,args=(url,semaphore))
        t.start()
    while threading.active_count() !=1:
        pass
    else:
        print('所有线程运行完毕')
