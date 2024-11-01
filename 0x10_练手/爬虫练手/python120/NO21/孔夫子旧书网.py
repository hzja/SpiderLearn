import requests
from lxml.html import etree
import random
import time


class SSS:
    def __init__(self):

        self.url_format = 'https://book.kongfz.com/C{}/v6w{}/'
        # 待抓取的分类，可以扩展
        self.types = ["wenxue", "xiaoshuo"]
        self.session = requests.Session()
        self.headers = self.get_headers()
        self.categorys = []

    def get_categorys(self):

        with self.session.get(url='https://book.kongfz.com/Cfalv/', headers=self.headers) as res:
            if res:
                html = etree.HTML(res.text)
                items = html.cssselect('.tushu div.link-item a')
                # 匹配出URL中的type
                for item in items:
                    # print(item)
                    # print(item.get("href"))
                    href = item.get("href")
                    type = href[href.find('C') + 1:-1]
                    self.categorys.append(type)

    def get_headers(self):
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
            "user-agent": ua,
            "referer": "https://www.baidu.com"
        }
        return headers

    def get_detail(self, type, page):
        with self.session.get(url=self.url_format.format(type, page), headers=self.headers, timeout=5) as res:
            if res.text:
                with open(f"./孔夫子/{type}_{page}.html", "w+", encoding="utf-8") as f:
                    f.write(res.text)
            else:
                # 如果无数据，重新请求
                print(f"页码{page}请求异常，重新请求")
                self.get_detail(page)

    def run(self):
        pagesize = 5
        for type in self.types:
            for page in range(1, pagesize):
                self.get_detail(type, page)
                time.sleep(2)
                print(f"分类：{type}，页码：{page}页面储存完毕！")


# 数据提取类
class Analysis:
    def __init__(self):
        # 待抓取的分类，可以扩展
        self.types = ["wenxue", "xiaoshuo"]

    # 去除特殊字符
    def remove_character(self, origin_str):
        if origin_str is None:
            return
        origin_str = origin_str.replace('\n', '')
        origin_str = origin_str.replace(',', '，')
        return origin_str

    def format(self, text):
        html = etree.HTML(text)
        # 获取所有项目区域 div
        div_books = html.cssselect('div#listBox>div.item')
        for book in div_books:
            # 获取标题属性值
            title = book.cssselect('div.item-info>div.title')[0].get('title')
            # 作者默认给空值
            author = None
            author_div = book.cssselect('div.item-info>div.zl-isbn-info>span:nth-child(1)')
            if len(author_div) > 0:
                author = author_div[0].text
            # 出版社相同操作
            publisher = None
            publisher_div = book.cssselect('div.item-info>div.zl-isbn-info>span:nth-child(2)')
            if len(publisher_div) > 0:
                # 进行数据提取与截取
                publisher = publisher_div[0].text.split(' ')[1]
            # print(publisher)

            # 数据整合
            print(title, author, publisher)

    def run(self):
        pagesize = 5
        for type in self.types:
            for page in range(1, pagesize):
                with open(f"./孔夫子/{type}_{page}.html", "r", encoding="utf-8") as f:
                    text = f.read()
                    # print(text)
                    self.format(text)


if __name__ == '__main__':
    # 采集数据，运行哪部分，去除注释即可
    # s = SSS()
    # s.run()
    # 提取数据
    # s.get_categorys()
    a = Analysis()
    a.run()
