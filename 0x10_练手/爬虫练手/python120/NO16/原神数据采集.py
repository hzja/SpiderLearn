import requests
import sys
import random
import re
import sys
import os


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
        "user-agent": ua,
        "referer": "https://www.baidu.com"
    }
    return headers


# 数据提取函数
def format_text(text):
    # element = etree.HTML(text)
    # print(text)
    # all_li = element.cssselect("li.swiper-slide")
    # print(all_li)
    try:
        div_pattern = re.compile('charList:(\[.*?),mod3Index')
        match = div_pattern.search(text)
        div_html = match.group(1)
        title_pattern = re.compile('title:"(.*?)"')
        cover1_pattern = re.compile('cover1:"(.*?)"')
        cover2_pattern = re.compile('cover2:"(.*?)"')
        icon_pattern = re.compile('icon:"(.*?)"')
        # 该正则表达式比较复杂，需要重点理解
        cv_pattern = re.compile(
            'cv:\[\{name:[\"]?(?P<cn_name>.*?)[\"]?\,audio:\[(?P<cn_audios>.*?)\]\}\,\{name:[\"]?(?P<jp_name>.*?)[\"]?\,audio:\[(?P<jp_audios>.*?)\]\}\]\}')
        titles = title_pattern.findall(div_html)
        cover1s = cover1_pattern.findall(div_html)
        cover2s = cover2_pattern.findall(div_html)
        icons = icon_pattern.findall(div_html)
        cvs = cv_pattern.findall(div_html)
        print(cvs)
        # print(titles,cover1s,cover2s,icons,cvs)
        for index in range(0, len(titles)):
            my_dict = {
                "title": titles[index],
                "cover1": cover1s[index],
                "cover2": cover2s[index],
                "icon": icons[index],
                "cn_name": cvs[index][0],  # 中文配音名称
                "jp_name": cvs[index][2],  # 日文配音名称
                "cn_audios": cvs[index][1].split(","),
                "jp_audios": cvs[index][3].split(","),
            }
            save(my_dict)
    except Exception as e:
        print("格式化数据异常",e)
    # print("https:\\u002F\\u002Fuploadstatic.mihoyo.com\\u002Fcontentweb\\u002F20210508\\u002F2021050818254152089.png".encode('utf-8').decode("unicode-escape"))
    # print(len(titles),len(cover1s),len(cover2s))


# 创建文件夹
def save(my_dict):
    is_exists = os.path.exists("./download")

    # 判断结果
    if not is_exists:
        os.mkdir("./download")

    # 提取数据

    title = my_dict["title"]
    cover1 = my_dict["cover1"]
    cover2 = my_dict["cover2"]
    icon = my_dict["icon"]
    cn_name = my_dict["cn_name"]
    jp_name = my_dict["jp_name"]
    cn_audios = my_dict["cn_audios"]
    jp_audios = my_dict["jp_audios"]

    # 创建目录
    if not os.path.exists(f"./download/{title}"):
        os.mkdir(f"./download/{title}")
    # 保存封面图1
    save_img(cover1, title, "cover1")
    # 保存封面图2
    save_img(cover2, title, "cover2")
    # 保存大头贴
    save_img(icon, title, "icon")
    save_audio(title, cn_name, cn_audios)
    save_audio(title, jp_name, jp_audios)

def save_img(url, title, img_name):
    # 去除 \u 字符
    url = url.encode('utf-8').decode("unicode-escape")
    try:
        res = requests.get(url, headers=get_headers(), timeout=5)
        with open(f'./download/{title}/{img_name}.png', "wb") as f:
            f.write(res.content)
    except Exception as e:
        print(e)


def save_audio(title, cn_name, cn_audios):
    try:
        for index in range(0, len(cn_audios)):
            # 去除 \u 字符
            url = cn_audios[index].encode('utf-8').decode("unicode-escape")
            # 去除 url 左右双引号
            url = url.strip('"')

            res = requests.get(url, headers=get_headers(), timeout=5)
            with open(f'./download/{title}/{cn_name}_{index}.mp3', "wb") as f:
                f.write(res.content)
    except Exception as e:
        print(e)


def run(url):
    try:
        res = requests.get(url, headers=get_headers(), timeout=5)
        format_text(res.text)
    except Exception as e:
        print(url)
        print("请求数据发生异常", e)


if __name__ == "__main__":
    argvs = sys.argv
    # 获取传递进来的参数
    category = argvs[1]
    # category = 'liyue'
    url = "https://ys.mihoyo.com/main/character/{}?char=0".format(category)
    print(url)
    run(url)
