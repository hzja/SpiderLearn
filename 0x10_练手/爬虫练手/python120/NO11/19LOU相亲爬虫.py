import requests
from lxml import etree
from fake_useragent import UserAgent
import time


def save(src, title):
    try:
        res = requests.get(src)
        with open(f"imgs/{title}.jpg", "wb+") as f:
            f.write(res.content)
    except Exception as e:
        print(e)


def run(url):
    # ua = UserAgent(cache=False)
    ua = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
    headers = {
        "User-Agent": ua,
        "Host": "www.19lou.com",
        "Referer": "https://www.19lou.com/r/1/19lnsxq-233.html",
        "Cookie": "_Z3nY0d4C_=37XgPK9h"  # 从反爬代码中获取到的值
    }
    try:
        res = requests.get(url=url, headers=headers)
        text = res.text
        # 将 html 转换成 Element 对象
        html = etree.HTML(text)
        # xpath 路径提取 @class 为选取 class 属性
        divs = html.xpath("//div[@class='pics']")
        # print(len(divs))
        # 遍历 Elements 节点
        for div in divs:
            # 提取地址，注意提取的属性为 data-src 而不是 src
            src = div.xpath("./img/@data-src")[0]
            # 提取标题
            title = div.xpath("./img/@alt")[0]
            save(src, title)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    urls = ["https://www.19lou.com/r/1/19lnsxq.html"]
    for i in range(114, 243):
        urls.append(f"https://www.19lou.com/r/1/19lnsxq-{i}.html")
    for url in urls:
        print(f"正在抓取{url}")
        run(url)
        # time.sleep(5)

    print("全部爬取完毕")
