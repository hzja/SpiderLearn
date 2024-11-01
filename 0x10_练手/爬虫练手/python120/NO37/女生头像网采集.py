from gevent import monkey

monkey.patch_all()

import threading
from bs4 import BeautifulSoup

import gevent
import requests
import lxml


def get_page(this_urls):
    while True:

        if this_urls is None:
            break
        url = this_urls.pop()
        print('正在抓取：{}，当前的虚拟线程为：{}'.format(url, threading.current_thread().getName()))
        res = requests.get(url=url)
        res.encoding = "gb2312"
        if res.status_code == 200:

            soup = BeautifulSoup(res.text, 'lxml')
            content = soup.find(attrs={'class': 'g-gxlist-imgbox'})
            img_tags = content.find_all('img')

            for img_tag in img_tags:
                img_src = img_tag['src']
                # 注意去除文件路径中的特殊符号，防止出错
                try:
                    name = img_tag['alt'].replace('/', '').replace('+', '').replace('?', '').replace('*', '')
                except OSError as e:
                    continue
                save_img(img_src, name)


def save_img(img_src, name):
    res = requests.get(img_src)
    with open(f'imgs/{name}.jpg', mode='wb') as f:
        f.write(res.content)


if __name__ == '__main__':
    urls = [f"https://www.qqtn.com/tx/nvshengtx_{page}.html" for page in range(1, 244)]
    # 开启 5 个协程
    gevent.joinall([gevent.spawn(get_page, urls) for i in range(5)])

    print("爬取完毕")
