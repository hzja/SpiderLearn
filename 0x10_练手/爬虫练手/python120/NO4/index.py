import requests
import re
import time

# 声明 UA
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"
}
# 存储异常路径，防止出现爬取失败情况
error_list = []

# 爬虫入口
def run():
    url = "http://www.ultramanclub.com/allultraman/"
    try:
        # 网页访问速度慢，需要设置 timeout
        res = requests.get(url=url, headers=headers, timeout=10)
        res.encoding = "gb2312"
        html = res.text
        return get_detail_list(html)

    except Exception as e:
        print("请求异常", e)


# 获取全部奥特曼详情页
def get_detail_list(html):
    start_index = '<ul class="lists">'
    start = html.find(start_index)
    html = html[start:]
    links = re.findall('<li class="item"><a href="(.*)">', html)
    # links = list(set(links))
    links = [
        f"http://www.ultramanclub.com/allultraman/{i.split('/')[1]}/" for i in set(links)]
    return links


def get_image(url):
    try:
        # 网页访问速度慢，需要设置 timeout
        res = requests.get(url=url, headers=headers, timeout=15)
        res.encoding = "gb2312"
        html = res.text
        print(url)
        # 获取详情页标题，作为图片文件名
        title = re.search('<title>(.*?)\[', html).group(1)
        # 获取图片短连接地址
        image_short = re.search(
            '<figure class="image tile">[.\s]*?<img src="(.*?)"', html).group(1)

        # 拼接完整图片地址
        img_url = "http://www.ultramanclub.com/allultraman/" + image_short[3:]
        # 获取图片数据
        img_data = requests.get(img_url).content
        print(f"正在爬取{title}")
        if title is not None and image_short is not None:
            with open(f"images/{title}.png", "wb") as f:
                f.write(img_data)

    except Exception as e:
        print("*"*100)
        print(url)
        print("请求异常", e)

        error_list.append(url)


if __name__ == '__main__':
    details = run()
    for detail in details:
        get_image(detail)

    while len(error_list) > 0:
        print("再次爬取")
        detail = error_list.pop()
        get_image(detail)

    print("奥特曼图片数据爬取完毕")
