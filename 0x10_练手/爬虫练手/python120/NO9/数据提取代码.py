import os
import re
import requests


def reade_html():
    path = r"E:\pythonProject\test\html"
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()
            img_pattern = re.compile('<div class="img_book"[.\s]*style="background:url\((.*?)\)')
            title_pattern = re.compile("<a href='(?P<url>.*?)'>(?P<title>.*?)</a> <br /> \[(?P<author>.*?)\] <br />")
            score_pattern = re.compile('<p style=".*?"><b>(.*?)</b></p>')
            img_urls = img_pattern.findall(html)
            details = title_pattern.findall(html)
            scores = score_pattern.findall(html)

            # save(details, scores)
            for index, url in enumerate(img_urls):
                save_img(details[index][1], url)


def save(details, scores):
    for index, detail in enumerate(details):
        my_str = "%s,%s,%s,%s\n" % (detail[1].replace(",", "，"), detail[0], detail[2].replace(",", "，"), scores[index])
        with open("./comic.csv", "a+", encoding="utf-8") as f:
            f.write(my_str)


def save_img(title, url):
    print(f"正在抓取{title}--{url}")
    headers = {
        "User-Agent": "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
    }
    try:
        res = requests.get(url, headers=headers, allow_redirects=False, timeout=10)

        data = res.content
        with open(f"imgs/{title}.jpg", "wb+") as f:
            f.write(data)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    reade_html()
