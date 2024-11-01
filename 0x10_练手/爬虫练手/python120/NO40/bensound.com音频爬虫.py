import time

import asyncio
import aiohttp

from bs4 import BeautifulSoup
import lxml


async def get_html(client, url):
    print("正在采集", url)
    async with client.get(url, timeout=5) as resp:
        html = await resp.text()
        soup = BeautifulSoup(html, 'lxml')
        divs = soup.find_all(attrs={'class': 'img_mini'})
        mp3_urls = [get_mp3_url("https://www.bensound.com/" + div.a.img["src"]) for div in divs]
        return mp3_urls


def get_mp3_url(img_url):
    img_url = img_url
    name = img_url[img_url.rfind("/") + 1:img_url.rfind(".")]

    mp3_url = f"https://www.bensound.com/bensound-music/bensound-{name}.mp3"
    return mp3_url


async def get_mp3_file(client, url):
    print("正在采集 mp3 文件", url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        "Referer": "https://www.bensound.com/royalty-free-music"
    }
    mp3_file_name = url[url.rfind('-') + 1:url.rfind('.')]
    print(mp3_file_name)
    async with client.get(url, headers=headers) as resp:
        content = await resp.read()
        with open(f'./mp3/{mp3_file_name}.mp3', "wb") as f:
            f.write(content)
        return (url, "success")


async def main(urls):
    timeout = aiohttp.ClientTimeout(total=600)  # 将超时时间设置为600秒
    connector = aiohttp.TCPConnector(limit=50)  # 将并发数量降低
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as client:
        tasks = [asyncio.ensure_future(get_html(client, urls[i])) for i in range(len(urls))]

        dones, pendings = await asyncio.wait(tasks)
        print("异步执行完毕，开始输出对应结果：")
        all_mp3 = []
        for task in dones:
            all_mp3.extend(task.result())

        totle = len(all_mp3)
        print("累计获取到【", totle, "】个 MP3 文件")
        print("_" * 100)
        print("准备下载 MP3 文件")

        # 每次下载10个
        totle_page = totle // 10 if totle % 10 == 0 else totle // 10 + 1

        for page in range(0, totle_page):
            print("正在下载第{}页 MP3 文件".format(page + 1))
            start_page = 0 if page == 0 else page * 10
            end_page = (page + 1) * 10
            print("待下载地址")
            print(all_mp3[start_page:end_page])
            mp3_download_tasks = [asyncio.ensure_future(get_mp3_file(client, url)) for url in
                                  all_mp3[start_page:end_page]]
            mp3_dones, mp3_pendings = await asyncio.wait(mp3_download_tasks)
            for task in mp3_dones:
                print(task.result())


if __name__ == '__main__':
    url_format = "https://www.bensound.com/royalty-free-music/{}"
    urls = [url_format.format(i) for i in range(1, 5)]
    start_time = time.perf_counter()
    asyncio.run(main(urls))
    print("aiohttp 异步采集消耗时间为：", time.perf_counter() - start_time)
