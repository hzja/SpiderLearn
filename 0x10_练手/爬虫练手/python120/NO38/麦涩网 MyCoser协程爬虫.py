import threading
import asyncio
import time
import requests
import lxml
from bs4 import BeautifulSoup


async def get(url):
    return requests.get(url)


async def get_html(url):
    print("准备抓取：", url)
    res = await get(url)
    return res.text


async def save_img(img_url):
    # thumbMid_5ae3e05fd3945 将小图替换为大图
    img_url = img_url.replace('thumb','thumbMid')
    img_url = "http://mycoser.com/" + img_url
    print("图片下载中：", img_url)
    res = await get(img_url)
    if res is not None:
        with open(f'./new_imgs/{time.time()}.jpg', 'wb') as f:
            f.write(res.content)
            return img_url,"ok"


async def main(url_list):
    # 创建 5 个任务
    tasks = [asyncio.ensure_future(get_html(url_list[_])) for _ in range(len(url_list))]

    dones, pending = await asyncio.wait(tasks)
    for task in dones:
        html = task.result()
        soup = BeautifulSoup(html, 'lxml')
        divimg_tags = soup.find_all(attrs={'class': 'workimage'})

        for div in divimg_tags:
            ret = await save_img(div.a.img["data-original"])
            print(ret)


if __name__ == '__main__':
    urls = [f"http://mycoser.com/picture/lists/p/{page}" for page in range(1, 17)]
    totle_page = len(urls) // 5 if len(urls) % 5 == 0 else len(urls) // 5 + 1
    # 对 urls 列表进行切片，方便采集
    for page in range(0, totle_page):
        start_page = 0 if page == 0 else page * 5
        end_page = (page + 1) * 5

        # 循环事件对象
        # loop = asyncio.get_event_loop()
        #
        # loop.run_until_complete(main(urls[start_page:end_page]))
        asyncio.run(main(urls[start_page:end_page]))
