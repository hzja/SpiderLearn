import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}


def get_list(url):
    """
    获取全部详情页链接
    """
    all_list = []

    res = requests.get(url, headers=headers)
    html = res.text
    start = '<ul class="list2">'
    end = '<ul class="pagination">'

    html = html[res.text.find(start):res.text.find(end)]
    pattern = re.compile(
        '<h3><a href="(.*?)" target="_blank" title="(.*?)">.*?</a></h3>')
    all_list = pattern.findall(html)

    return all_list


def save_img(title, index, url):
    try:
        img_res = requests.get(url, headers=headers)
        img_data = img_res.content
        print(f"抓取：{url}")
        with open(f"images/{title}_{index}.png", "wb+") as f:
            f.write(img_data)
    except Exception as e:
        print(e)


def get_detail(title, url):
    res = requests.get(url=url, headers=headers)
    html = res.text
    # print(html)
    pattern = re.compile(
        '<img  alt=".*?" src="(.*?)"')
    imgs = pattern.findall(html)
    for index, url in enumerate(imgs):
        # print(title, index, url)
        save_img(title, index, url)


def run(start, end):
    wait_url = [
        f"https://www.zhimengo.com/duoroutu?page={i}" for i in range(int(start), int(end)+1)]
    print(wait_url)

    url_list = []
    for item in wait_url:
        ret = get_list(item)
        # print(len(ret))
        print(f"已经抓取：{len(ret)} 条数据")
        url_list.extend(ret)

    # print(len(url_list))
    for url, title in url_list:
        get_detail(title, url)


if __name__ == "__main__":
    start = input("请输入起始页：")
    end = input("请输入结束页：")
    run(start, end)
