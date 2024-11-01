import requests
from lxml.html import etree
import random
import time


class SSS:
    def __init__(self):
        self.start_url = 'http://xiangmu.1637.com/p1.html'
        self.url_format = 'http://xiangmu.1637.com/p{}.html'
        self.session = requests.Session()
        self.headers = self.get_headers()

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

    def get_pagesize(self):

        with self.session.get(url=self.start_url, headers=self.headers, timeout=5) as res:
            if res.text:
                element = etree.HTML(res.text)
                # 通过 cssselect 选择器，选择 em 标签
                div_total = element.cssselect('#div_total>em')
                # 获取 em 标签内部文本 div_total[0].text，并将其转换为整数
                total = int(div_total[0].text)
                # 获取页码
                pagesize = int(total / 10) + 1
                # print(pagesize)
                # 总数恰好被10整数，不用额外增加一页数据
                if total % 10 == 0:
                    pagesize = int(total / 10)

                return pagesize
            else:
                return None

    def get_detail(self, page):
        with self.session.get(url=self.url_format.format(page), headers=self.headers, timeout=5) as res:
            if res.text:
                with open(f"./加盟网站数据包/{page}.html", "w+", encoding="utf-8") as f:
                    f.write(res.text)
            else:
                # 如果无数据，重新请求
                print(f"页码{page}请求异常，重新请求")
                self.get_detail(page)

    def run(self):
        pagesize = self.get_pagesize()
        # 测试数据，可临时修改 pagesize = 20
        for page in range(1, pagesize):
            self.get_detail(page)
            time.sleep(2)
            print(f"页码{page}抓取完毕！")


# 数据提取类
class Analysis:
    def __init__(self):
        pass

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
        div_xminfos = html.cssselect('div.xminfo')
        for xm in div_xminfos:
            adtexts = self.remove_character(xm.cssselect('a.adtxt')[0].text)  # 获取广告词列表
            url = xm.cssselect('a.adtxt')[0].attrib.get('href')  # 获取详情页地址

            brands = xm.cssselect(':nth-child(2)>:nth-child(2)')[1].text  # 获取品牌列表
            categorys = xm.cssselect(':nth-child(2)>:nth-child(3)>a')[0].text  # 获取分类，例如 ["餐饮","小吃"]
            types = ''
            try:
                # 此处可能不存在二级分类
                types = xm.cssselect(':nth-child(2)>:nth-child(3)>a')[1].text  # 获取分类，例如 ["餐饮","小吃"]
            except Exception as e:
                pass
            creation = xm.cssselect(':nth-child(2)>:nth-child(6)')[0].text  # 品牌建立时间列表
            franchise = xm.cssselect(':nth-child(2)>:nth-child(9)')[0].text  # 加盟店数量列表
            company = xm.cssselect(':nth-child(3)>span>a')[0].text  # 公司名称列表

            introduce = self.remove_character(xm.cssselect(':nth-child(4)>span')[0].text)  # 品牌介绍
            pros = self.remove_character(xm.cssselect(':nth-child(5)>:nth-child(2)')[0].text)  # 经营产品介绍
            investment = xm.cssselect(':nth-child(5)>:nth-child(4)>em')[0].text  # 投资金额
            # 拼接字符串
            long_str = f"{adtexts},{categorys},{types},{brands},{creation},{franchise},{company},{introduce},{pros},{investment},{url}"
            with open("./加盟数据.csv", "a+", encoding="utf-8") as f:
                f.write(long_str + "\n")

    def run(self):
        for i in range(1, 5704):
            with open(f"./加盟网站数据包/{i}.html", "r", encoding="utf-8") as f:
                text = f.read()
                self.format(text)


if __name__ == '__main__':
    # 采集数据，运行哪部分，去除注释即可
    # s = SSS()
    # s.run()
    # 提取数据
    a = Analysis()
    a.run()