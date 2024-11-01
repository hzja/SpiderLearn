import requests
from fake_useragent import UserAgent
import re
import threading


def replace_mark(my_str):
    return my_str.replace(",", "，").replace('"', "“")


def format_html(html):
    li_pattern = re.compile(
        '<li\sclass="ret-search-item clearfix">[\s\S]+?</li>')
    title_url_pattern = re.compile(
        '<a href="(.*?)" target="_blank" title=".*?">(.*?)</a>')
    sign_pattern = re.compile('<i class="ui-icon-sign">签约</i>')
    exclusive_pattern = re.compile('<i class="ui-icon-exclusive">独家</i>')
    author_pattern = re.compile(
        '<p class="ret-works-author" title=".*?">(.*?)</p>')
    tags_pattern = re.compile('<span href=".*?" target="_blank">(.*?)</span>')
    score_pattern = re.compile('<span>人气：<em>(.*?)</em></span>')
    items = li_pattern.findall(html)
    for item in items:
        title_url = title_url_pattern.search(item)
        title = title_url.group(2)
        url = title_url.group(1)
        sign = 0
        exclusive = 0
        if sign_pattern.search(item) is not None:
            sign = 1
        if exclusive_pattern.search(item) is not None:
            exclusive = 1

        author = author_pattern.search(item).group(1)

        tags = tags_pattern.findall(item)

        score = score_pattern.search(item).group(1)
        lock.acquire()
        with open("./qq.csv", "a+", encoding="utf-8") as f:
            f.write(
                f'{replace_mark(title)},{url},{sign},{exclusive},{replace_mark(author)},{"#".join(tags)},"{replace_mark(score)}" \n')

        lock.release()


def run(index):

    ua = UserAgent(use_cache_server=False)

    response = requests.get(
        f"https://ac.qq.com/Comic/index/page/{index}", headers={'User-Agent': ua.random})
    html = response.text
    format_html(html)
    semaphore.release()


lock = threading.Lock()
if __name__ == "__main__":

    num = 0

    semaphore = threading.BoundedSemaphore(5)
    lst_record_threads = []
    for index in range(1, 462):
        print(f"正在抓取{index}")
        semaphore.acquire()
        t = threading.Thread(target=run, args=(index, ))
        t.start()
        lst_record_threads.append(t)

    for rt in lst_record_threads:
        rt.join()

    print("数据爬取完毕")
