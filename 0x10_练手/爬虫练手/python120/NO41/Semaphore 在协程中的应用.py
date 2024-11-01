import time

import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def get_title(semaphore, url):
    async with semaphore:
        print("正在采集：", url)
        async with aiohttp.request('GET', url) as res:
            html = await res.text()
            soup = BeautifulSoup(html, 'html.parser')
            title_tags = soup.find_all(attrs={'class': 'item-title'})
            event_names = [item.a.text for item in title_tags]
            print(event_names)


async def main():
    semaphore = asyncio.Semaphore(10)  # 控制每次最多执行 10 个线程
    tasks = [asyncio.ensure_future(get_title(semaphore, "http://www.lishiju.net/hotevents/p{}".format(i))) for i in
             range(111)]
    dones, pendings = await asyncio.wait(tasks)
    # for task in dones:
    #     print(len(task.result()))


if __name__ == '__main__':

    start_time = time.perf_counter()
    asyncio.run(main())
    print("代码运行时间为：", time.perf_counter() - start_time)

    # # 创建事件循环。
    # event_loop = asyncio.get_event_loop()
    # # 启动事件循环并等待协程main()结束。
    # event_loop.run_until_complete(main())
    # # 代码运行时间为： 2.227831242
