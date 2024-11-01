import random
import logging
import threading
from typing import Optional, Text
import requests
from bs4 import BeautifulSoup
import lxml

logging.basicConfig(level=logging.WARNING)
thread_lock = threading.Lock()


class PngImg(threading.Thread):
    # 构造函数
    def __init__(self, thread_name, headers_func, requests_func) -> None:
        threading.Thread.__init__(self)
        self._headers = headers_func()
        self._timeout = 5
        self.requests_func = requests_func
        self._thread_name = thread_name

    def run(self) -> None:
        bast_host = "http://pngimg.com"
        while True:
            # 全局锁，获取地址
            thread_lock.acquire()
            global all_links
            if all_links is None:
                break

            list_url = bast_host + all_links.pop().get('href')
            thread_lock.release()
            print(self._thread_name + " 正在运行，采集的地址是 " + list_url)

            list_html_str = self.requests_func(url=list_url, headers=self._headers, timeout=self._timeout)
            ret_imgs = self._get_imgs(list_html_str)

            self._save(ret_imgs)

    def _get_imgs(self, html) -> list:
        """获取所有的图片地址
        :return: 图片 list
        """
        soup = BeautifulSoup(html, 'lxml')
        # 获取图片所在 div 标签
        div_imgs = soup.find_all(attrs={'class': 'png_imgs'})
        # 图片地址为空，用来保存图片 tag

        imgs_src = []
        for div_img in div_imgs:
            # 遍历 div 标签，检索后代标签中的 img 图片标签
            imgs_src.append(div_img.a.img.get("src"))

        return imgs_src

    def _save(self, imgs):
        """保存图片 """
        for img in imgs:
            img = img.replace('small/', '')  # 去除 small 标记，获取大图
            img_url = "https://pngimg.com{}".format(img)  # 拼接完整图片访问地址
            name = img[img.rfind('/') + 1:]
            # print(img_url)
            # print(name)

            try:
                res = requests.get(url=img_url, headers=self._headers, timeout=self._timeout)
            except Exception as e:
                logging.error(e)

            if res is not None:
                name = name.replace("/", "_")
                with open(f'./imgs/{self._thread_name}_{name}', "wb+") as f:
                    f.write(res.content)


def get_headers():
    uas = [
        "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
        "Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)",
        "Baiduspider-image+(+http://www.baidu.com/search/spider.htm)",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 YisouSpider/5.0 Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; Googlebot-Image/1.0; +http://www.google.com/bot.html)",
        "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Sogou News Spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "Sosospider+(+http://help.soso.com/webspider.htm)",
        "Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)"
    ]
    ua = random.choice(uas)
    headers = {
        "user-agent": ua
    }
    return headers


# 通用的 requests get 请求方法
def get_html(url: Text, headers: dict, timeout: int) -> Optional[Text]:
    try:
        res = requests.get(url=url, headers=headers, timeout=timeout)
    except Exception as e:
        logging.error(e)

    if res is not None:
        return res.text
    else:
        return None


if __name__ == '__main__':
    url = "http://pngimg.com/"
    headers = get_headers()
    # 获取首页的 HTML 数据
    html_str = get_html(url, headers, 5)
    # 解析首页的HTML数据，获取所有列表页链接
    soup = BeautifulSoup(html_str, 'lxml')


    div_parents = soup.find_all(attrs={'class': 'sub_category'})

    # 获取到所有的详情页地址
    all_links = []
    for div in div_parents:
        all_links.extend(div.find_all('a'))

    print("累计获取到",len(all_links),"个列表页数据")

    # 通过第一个地址进行测试
    # first_url = all_links[0]
    #
    # list_url = first_url.get('href')
    # bast_host = "http://pngimg.com"
    # real_url = bast_host + list_url

    threads = ["Thread A", "Thread B", "Thread C", "Thread D", "Thread E"]
    for t in threads:
        my_thread = PngImg(t, get_headers, get_html)
        my_thread.start()
