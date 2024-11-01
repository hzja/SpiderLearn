import requests
from lxml import etree
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


def run(url, index):
    try:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        res = requests.get(url=url, headers=headers)
        res.encoding = "utf-8"
        html = res.text
        with open(f"./html/{index}.html", "w+", encoding="utf-8") as f:
            f.write(html)
    except Exception as e:
        print(e)


def list_str(my_list):
    return ",".join(my_list)


def get_data():
    for i in range(1, 130):
        with open(f"./html/{i}.html", "r", encoding="utf-8") as f:
            html = f.read()
            element = etree.HTML(html)
            # contains 函数 获取包含 xxx 的元素，类似的还有 starts-with,ends-with,last
            origin_li = element.xpath("//ul[contains(@class,'xm-list')]/li")
            # 循环抓取 li 内部数据
            for item in origin_li:

                # 提取加盟名称
                # title = item.xpath(".//div[@class='r']/h4/text()")[0]
                title = item.xpath("./div[@class='top']/a/@title")[0]
                # 提取超链接
                detail_link = "http:" + item.xpath("./div[@class='top']/a/@href")[0]


                # 提取特殊标签
                special_tag = list_str(item.xpath("./@class"))
                # 当包含特殊标签 xm-list2 时，使用不同的提取规则

                if special_tag != "xm-list2":
                     # 提取标签
                    tags = "#".join(item.xpath(".//div[@class='bot']/span[@class='label']/text()"))
                    # 提取投资价格
                    price = list_str(item.xpath(".//div[@class='bot']/span[@class='money']/b/text()"))
                    # 地址和行业
                    city_industry = list_str(item.xpath("./div[@class='bot']/p/span/text()"))

                    long_str = f"{title},{detail_link}, {tags}, {price}, {city_industry}"
                    save(long_str)
                else:
                    # 地址和行业
                    city_industry = list_str(item.xpath("./div[@class='top']/a/div/p[2]/span/text()"))
                    long_str = f"{title},{detail_link}, {0}, {0}, {city_industry}"
                    save(long_str)

      
               
def save(long_str):
    try:
        with open(f"./jiameng.csv", "a+",encoding="utf-8") as f:
            f.write("\n"+long_str)
    except Exception as e:
        print(e)

if __name__ == '__main__':

    # for i in range(1, 130):
    #     print(f"正在爬取第{i}页数据")
    #     run(f"https://www.3158.cn/xiangmu/canyin/?pt=all&page={i}", i)

    get_data()

    print("全部提取完毕")


