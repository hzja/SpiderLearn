import random
import threading
import logging

from bs4 import BeautifulSoup
import requests
import lxml

logging.basicConfig(level=logging.NOTSET) # 设置日志输出级别

# 声明一个 LiYang 类，其继承自 threading.Thread
class LiYangThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self) # 实例化多线程对象
        self._headers = self._get_headers() # 随机获取 ua
        self._timeout = 5 # 设置超时时间

    # 每个线程都去获取全局资源
    def run(self):
        # while True: # 此处为多线程开启位置
        try:
            res = requests.get(url="http://www.jsly001.com/thread-htm-fid-45-page-1.html", headers=self._headers,
                               timeout=self._timeout) # 测试获取第一页数据
        except Exception as e:
            logging.error(e)

        if res is not None:
            html_text = res.text
            self._format_html(html_text) # 调用html解析函数

    def _format_html(self, html):
        # 使用 lxml 进行解析
        soup = BeautifulSoup(html, 'lxml')

        # 获取板块主题分割区域，主要为防止获取置顶的主题
        part_tr = soup.find(attrs={'class': 'bbs_tr4'})

        if part_tr is not None:
            items = part_tr.find_all_next(attrs={"name": "readlink"}) # 获取详情页地址
        else:
            items = soup.find_all(attrs={"name": "readlink"})

        # 解析出标题与数据
        data = [(item.text, f'http://www.jsly001.com/{item["href"]}') for item in items]
        # 进入标题内页
        for name, url in data:
            self._get_imgs(name, url)

    def _get_imgs(self, name, url):
        """解析图片地址"""
        try:
            res = requests.get(url=url, headers=self._headers, timeout=self._timeout)
        except Exception as e:
            logging.error(e)

        if res is not None:
            soup = BeautifulSoup(res.text, 'lxml')
            origin_div1 = soup.find(attrs={'class': 'tpc_content'})
            origin_div2 = soup.find(attrs={'class': 'imgList'})
            content = origin_div2 if origin_div2 else origin_div1

            if content is not None:
                imgs = content.find_all('img')

                # print([img.get("src") for img in imgs])
                self._save_img(name, imgs) # 保存图片

    def _save_img(self, name, imgs):
        """保存图片"""
        for img in imgs:
            url = img.get("src")
            if url.find('http') < 0:
                continue
            id_ = img.find_parent('span').get("id")

            try:
                res = requests.get(url=url, headers=self._headers, timeout=self._timeout)
            except Exception as e:
                logging.error(e)

            if res is not None:
                name = name.replace("/", "_")
                with open(f'./imgs/{name}_{id_}.jpg', "wb+") as f: # 注意在 python 运行时目录提前创建 imgs 文件夹
                    f.write(res.content)

    def _get_headers(self):
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


if __name__ == '__main__':
    my_thread = LiYangThread()
    my_thread.run()
