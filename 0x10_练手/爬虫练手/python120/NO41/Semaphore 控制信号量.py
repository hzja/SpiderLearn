import threading
import time

import requests
from bs4 import BeautifulSoup


class MyThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.__url = url

    def run(self):
        if semaphore.acquire():  # 计数器 -1
            print("正在采集：", self.__url)
            res = requests.get(url=self.__url)
            soup = BeautifulSoup(res.text, 'html.parser')
            title_tags = soup.find_all(attrs={'class': 'item-title'})
            event_names = [item.a.text for item in title_tags]
            print(event_names)
            print("")
            semaphore.release()  # 计数器 +1


if __name__ == "__main__":
    semaphore = threading.Semaphore(5)  # 控制每次最多执行 5 个线程
    start_time = time.perf_counter()
    threads = []
    for i in range(111):  # 创建了110个线程。
        threads.append(MyThread(url="http://www.lishiju.net/hotevents/p{}".format(i)))
    for t in threads:
        t.start()  # 启动了110个线程。

    for t in threads:
        t.join()  # 等待线程结束

    print("累计耗时：", time.perf_counter() - start_time)
    # 累计耗时： 2.8005530640000003




