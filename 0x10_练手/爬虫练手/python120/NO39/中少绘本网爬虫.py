import asyncio
import time
import requests
from bs4 import BeautifulSoup
import lxml

BASE_URL = "http://banan.huiben.61read.com"


async def requests_get(url):
    headers = {
        "Referer": "http://banan.huiben.61read.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36"
    }
    try:
        res = requests.get(url, headers=headers)
        return res
    except Exception as e:
        print(e)
        return None


async def get_video(name, url):
    res = await requests_get(url)
    if res is not None:
        with open(f'./mp4/{name}.mp4', "wb") as f:
            f.write(res.content)
        return (name, url, "success")
    else:
        return None


async def get_list_url():
    """获取列表页地址"""
    res = await requests_get("http://banan.huiben.61read.com/")
    soup = BeautifulSoup(res.text, "lxml")
    all_a = []
    for ul in soup.find_all(attrs={'class', 'inline'}):
        all_a.extend(BASE_URL + _['href'] for _ in ul.find_all('a'))
    return all_a


async def get_mp4_url(url):
    """获取MP4地址"""
    res = await requests_get(url)
    soup = BeautifulSoup(res.text, "lxml")
    mp4s = []
    for div_tag in soup.find_all(attrs={'class', 'item_list'}):
        # 获取图片缩略图
        src = div_tag.a.img['src']
        # 将缩略图地址替换为 mp4 视频地址
        src = src.replace('cover.jpg', 'web/1.mp4').replace('cover.png', 'web/1.mp4')
        name = div_tag.div.a.text.strip()
        mp4s.append((src, name))

    return mp4s


async def main():
    # 获取列表页地址任务
    task_list_url = asyncio.create_task(get_list_url())
    all_a = await task_list_url
    # 创建任务列表
    tasks = [asyncio.ensure_future(get_mp4_url(url)) for url in all_a]
    # 添加回调函数
    # ret = map(lambda x: x.add_done_callback(callback), tasks)
    # 异步执行
    dones, pendings = await asyncio.wait(tasks)
    all_mp4 = []
    for task in dones:
        all_mp4.extend(task.result())
    # 获取到所有的MP4地址

    totle = len(all_mp4)
    print("累计获取到【", totle, "】个视频")
    print("_" * 100)
    print("准备下载视频")

    # 每次下载10个
    totle_page = totle // 10 if totle % 10 == 0 else totle // 10 + 1
    # print(totle_page)
    for page in range(0, totle_page):
        print("正在下载第{}页视频".format(page + 1))
        start_page = 0 if page == 0 else page * 10
        end_page = (page + 1) * 10
        print("待下载地址")
        print(all_mp4[start_page:end_page])
        mp4_download_tasks = [asyncio.ensure_future(get_video(name, url)) for url, name in all_mp4[start_page:end_page]]
        mp4_dones, mp4_pendings = await asyncio.wait(mp4_download_tasks)
        for task in mp4_dones:
            print(task.result())


if __name__ == '__main__':
    asyncio.run(main())
