import requests
import re
import os
import time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "host": 'www.cosplay8.com'
}


def get_list(url):
    """
    获取全部详情页链接
    """
    all_list = []

    res = requests.get(url, headers=headers)
    html = res.text
    pattern = re.compile('<li><a href="(.*?)">')
    all_list = pattern.findall(html)

    return all_list


def save_img(path, title, first_img, index):
    try:
        # 请求图片
        img_res = requests.get(
            f"http://www.cosplay8.com{first_img}", headers=headers)
        img_data = img_res.content

        with open(f"{path}/{title}_{index}.png", "wb+") as f:
            f.write(img_data)
    except Exception as e:
        print(e)


def get_detail(url):
    res = requests.get(url=url, headers=headers)
    res.encoding = "utf-8"
    html = res.text

    # 拆解页码，保存第一张图片
    size_pattern = re.compile('<span>共(\d+)页: </span>')
    # title_pattern = re.compile('<title>(.*?)-Cosplay中国</title>')
    title_pattern = re.compile('<title>(.*?)-Cosplay(中国|8)</title>')
    first_img_pattern = re.compile("<img src='(.*?)' id='bigimg'")
    try:
        page_size = size_pattern.search(html).group(1)
        title = title_pattern.search(html).group(1)
        first_img = first_img_pattern.search(html).group(1)

        print(f"URL对应的数据为{page_size}页", title, first_img)
        path = f'.images/{title}'
        if not os.path.exists(path):
            os.makedirs(path)

        # 请求第一张图片
        save_img(path, title, first_img, 1)

        # 请求更多图片
        urls = [f"{url[0:url.rindex('.')]}_{i}.html" for i in range(
            2, int(page_size)+1)]

        for index, child_url in enumerate(urls):
            try:
                res = requests.get(url=child_url, headers=headers)

                html = res.text
                first_img_pattern = re.compile("<img src='(.*?)' id='bigimg'")
                first_img = first_img_pattern.search(html).group(1)

                save_img(path, title, first_img, index)
            except Exception as e:
                print("抓取子页", e)

    except Exception as e:
        print(url, e)


def run(category, start, end):
    # 待爬取的列表页
    wait_url = [
        f"http://www.cosplay8.com/pic/chinacos/list_{category}_{i}.html" for i in range(int(start), int(end)+1)]
    print(wait_url)

    url_list = []
    for item in wait_url:
        ret = get_list(item)

        print(f"已经抓取：{len(ret)} 条数据")
        url_list.extend(ret)

    print(url_list)
    # print(len(url_list))
    for url in url_list:
        get_detail(f"http://www.cosplay8.com{url}")


if __name__ == "__main__":

    # http://www.cosplay8.com/pic/chinacos/list_22_2.html
    category = input("请输入分类编号：")
    start = input("请输入起始页：")
    end = input("请输入结束页：")
    run(category, start, end)
