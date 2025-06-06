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


def run(url):
    try:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        res = requests.get(url=url, headers=headers)
        json_text = res.json()
        data = json_text["Data"]
        img_srcs = []
        for item in data:
            img_srcs.extend(item["ImageSrcs"])
        long_str = "\n".join(img_srcs)
        save(long_str)

    except Exception as e:
        print(e)


def save(long_str):
    try:
        with open(f"./imgs.csv", "a+") as f:
            f.write("\n"+long_str)
    except Exception as e:
        print(e)


def save_img(img_src):
    try:
        url = img_src
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        res = requests.get(url=url, headers=headers, verify=False)
        data = res.content

        with open(f"./hanfu/{int(time.time())}.jpg", "wb+") as f:
            f.write(data)
    except Exception as e:
        print(e)


if __name__ == '__main__':

    with open("./imgs.csv","r") as f:
        while True:
            img_url = f.readline().strip()
            if img_url is None:
                break
            real_url = f"{img_url}_700x.jpg"
            save_img(real_url)


        # print(img_url)
    # urls = []
    # for i in range(1, 10):
    #     print(f"正在爬取第{i}批数据")
    #     run(f"https://api5.hanfugou.com/Trend/GetTrendListForHot?maxid=3396754&objecttype=album&page={i}&count=500")

    print("全部爬取完毕")
