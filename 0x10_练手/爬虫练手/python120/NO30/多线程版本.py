import requests_html
import threading
import time
import fcntl


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global page, lock, page_size
        while True:
            lock.acquire(True)
            if page >= page_size:
                lock.release()
                break
            else:
                page += 1
                lock.release()
                requests_html.DEFAULT_ENCODING = "gb18030"
                session = requests_html.HTMLSession()

                print("正在采集第{}页".format(page), "*" * 50)
                try:
                    page_url = f'http://www.world68.com/top.asp?t=5star&page={page}'
                    world = session.get(page_url, timeout=10)
                    print("正在采集数据", world.url)
                    # print(world.html)
                    title_a = world.html.find('dl>dt>a')
                    print(title_a)
                    my_str = ""

                    for item in title_a:
                        name = item.text
                        url = item.attrs['href']
                        my_str += f"{name.encode('utf-8').decode('utf-8')},{url}\n"

                    with open('thread_webs.txt', "a+", encoding="utf-8") as f:
                        fcntl.flock(f.fileno(), fcntl.LOCK_EX)  # 文件加锁
                        f.write(f"{my_str}")

                except Exception as e:
                    print(e, page_url)


if "__main__" == __name__:
    page_size = int(input("请输入总页码："))
    page = 0
    thread_list = []

    # 获取开始时间
    start = time.perf_counter()

    lock = threading.Lock()
    for i in range(1, 5):
        t = MyThread()
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    # 获取时间间隔
    elapsed = (time.perf_counter() - start)
    print("程序运行完毕，总耗时为：", elapsed)
