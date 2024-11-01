import threading
from threading import Lock, Thread
import time
import os
import requests
import random


class MyThread(threading.Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        global urls
        lock.acquire()
        one_url = urls.pop()
        print("正在爬取：", one_url)
        lock.release()
        print("任意线程等待随机时间")
        time.sleep(random.randint(1,3))
        res = requests.get(one_url, headers=self.get_headers(), timeout=5)

        if  res.json()["code"] != 400:
            data = res.json()["data"]["list"]
            for user in data:
                name = user['username']
                nickname = self.remove_character(user['nickname'])
                userAvatar = user['userAvatar']
                blogUrl = user['blogUrl']
                blogExpert = user['blogExpert']
                briefIntroduction = self.remove_character(
                    user['briefIntroduction'])

                with open('./qing_gee_data.csv', 'a+', encoding='utf-8') as f:
                    print(
                        f'{name},{nickname},{userAvatar},{blogUrl},{blogExpert},{briefIntroduction}')
                    f.write(
                        f"{name},{nickname},{userAvatar},{blogUrl},{blogExpert},{briefIntroduction}\n")
        else:
            print(res.json())
            print("异常数据", one_url)
            with open('./error.txt', 'a+', encoding='utf-8') as f:
                f.write(one_url+"\n")
    # 去除特殊字符

    def remove_character(self, origin_str):
        if origin_str is None:
            return
        origin_str = origin_str.replace('\n', '')
        origin_str = origin_str.replace(',', '，')
        return origin_str

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
            'cookie': 'UserName=你的ID; UserInfo=你的UserInfo; UserToken=你的UserToken;',
            "referer": "https://blog.csdn.net/qing_gee?type=sub&subType=fans"
        }
        return headers


if __name__ == '__main__':
    lock = Lock()
    url_format = 'https://blog.csdn.net/community/home-api/v1/get-fans-list?page={}&size=20&noMore=false&blogUsername=qing_gee'
    urls = [url_format.format(i) for i in range(1, 13300)]
    l = []
    while len(urls) > 0:
        print(len(urls))
        for i in range(5):
            p = MyThread("t"+str(i))
            l.append(p)
            p.start()
        for p in l:
            p.join()