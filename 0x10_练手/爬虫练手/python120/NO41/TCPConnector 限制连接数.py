import time

import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def get_title(session, url):
    async with session.get(url) as res:
        print("正在采集：", url)
        html = await res.text()
        soup = BeautifulSoup(html, 'html.parser')
        title_tags = soup.find_all(attrs={'class': 'item-title'})
        event_names = [item.a.text for item in title_tags]
        print(event_names)



async def main():
    connector = aiohttp.TCPConnector(limit=1)  # 限制同时连接数
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [asyncio.ensure_future(get_title(session, "http://www.lishiju.net/hotevents/p{}".format(i))) for i in
                 range(111)]
        await asyncio.wait(tasks)



if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main())
    print("代码运行时间为：", time.perf_counter() - start_time)
