import requests
from lxml import etree
from fake_useragent import UserAgent
import time
import re
import random

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]


def save(long_str):
    try:
        with open(f"exhibition.csv", "a+", encoding="utf-8") as f:
            f.write(long_str)
    except Exception as e:
        print(e)


def get_detail(url):
    try:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        res = requests.get(url=url, headers=headers)
        text = res.text
        # 将 html 转换成 Element 对象
        html = etree.HTML(text)
        # 详细地址
        address_detail = html.xpath("//span[@class='fl mr10']/text()")[0]
        # 时间间隔
        time_interval = html.xpath(
            "//div[@class='h25 line25 s6 f14 w100s mb10']/text()")[3].strip()

        # 票价
        ticket_price = html.xpath("//b[@class='f40']/text()")[0]
        # 匹配得分
        score_url = html.xpath("//div[@class='mt10']/img/@src")[0]
        score = re.search(
            r"//static.nyato.cn/expo-image/stars/star-(\d\.\d).png", score_url).group(1)
        # 其它信息
        other = ",".join(html.xpath(
            "//span[@class='sf6 f18 fwb ml15']/text()"))
        return ticket_price, time_interval, address_detail, score, other

    except Exception as e:
        print("详情页BUG")
        print(url)
        time.sleep(4)
        get_detail(url)
        print(e)


def run(url):

    try:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        res = requests.get(url=url, headers=headers)
        text = res.text
        # 将 html 转换成 Element 对象
        html = etree.HTML(text)
        # xpath 路径提取 @class 为选取 class 属性
        lis = html.xpath("//ul[@class='w980 pt20']/li")

        # 遍历 Elements 节点
        for li in lis:
            href = li.xpath(".//a/@href")[0]
            title = li.xpath(".//a/@title")[0]
            city = li.xpath(".//span[@class='w120 fl']/text()")[0].strip()
            ticket_price, time_interval, address_detail, score, other = get_detail(
                href)
            long_str = f"{href},{title},{city},{ticket_price},{time_interval},{address_detail},{score},{other}\n"
            save(long_str)

    except Exception as e:
        print("列表页BUG")
        print(url)
        time.sleep(4)
        run(url)
        print(e)


if __name__ == '__main__':
    urls = []
    for i in range(1, 1313):
        urls.append(f"https://www.nyato.com/manzhan/?type=expired&p={i}")
    for url in urls:
        print(f"正在抓取{url}")
        run(url)

    print("全部爬取完毕")
