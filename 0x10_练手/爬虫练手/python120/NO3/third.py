import requests
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}


# 获取分页
def get_pagesize(html):
    # 编写简单的正则表达式 <a href='68_(\d+).html'>末页</a>
    pagesize = re.search("<a href='68_(\d+).html'>末页</a>", html)
    if pagesize is not None:
        return pagesize.group(1)
    else:
        return 0


# 获取待抓取列表
def get_wait_list(url):
    wait_urls = []
    try:
        res = requests.get(url=url, headers=HEADERS, timeout=5)
        res.encoding = "gb2312"
        html_text = res.text
        pagesize = int(get_pagesize(html_text))
        if pagesize > 0:
            print(f"获取到{pagesize}页数据")
            # 生成待抓取列表
            for i in range(1, pagesize + 1):
                wait_urls.append(f"http://p.ik123.com/zt/maomi/68_{i}.html")
        return wait_urls

    except Exception as e:
        print("获取分页异常", e)


# 正则匹配详情页链接
def format_detail(html):
    # 多次模拟得到正则表达式 <a class=preview href="(.*?)"
    # 注意单引号与双引号嵌套
    detail_urls = re.findall('<a class=preview href="(.*?)"', html)
    return detail_urls


# 获取所有详情页链接数据
def get_detail_list(url):
    try:
        res = requests.get(url=url, headers=HEADERS, timeout=5)
        res.encoding = "gb2312"
        html_text = res.text
        return format_detail(html_text)

    except Exception as e:
        print("获取详情页异常", e)


def format_mao_img(html):
    # 匹配猫咪图正则表达式 <img alt=".*?" src=".*?" />
    mao_img_urls = re.findall('<img alt=".*?" src="(.*?)" />', html)
    return mao_img_urls


# 获取猫咪图片地址
def get_mao_img(detail_url):
    try:
        res = requests.get(url=detail_url, headers=HEADERS, timeout=5)
        res.encoding = "gb2312"
        html_text = res.text
        return format_mao_img(html_text)

    except Exception as e:
        print("获取猫咪图片异常", e)


if __name__ == '__main__':
    start_url = "http://p.ik123.com/zt/maomi/68_1.html"
    wait_urls = get_wait_list(url=start_url)
    detail_list = []
    for url in wait_urls:
        print(f"正在抓取{url}")
        detail_list.extend(get_detail_list(url))

    print(f"获取到{len(detail_list)}条详情页")
    mao_imgs = []
    for index, mao_detail in enumerate(detail_list):
        if len(mao_detail) > 0:
            print(f"正抓取第{index}页数据")
            mao_imgs.extend(get_mao_img(mao_detail))
            # 以下代码测试用
            if len(mao_imgs) > 100:
                break

    print(f"获取到{len(mao_imgs)}条猫咪图")
    print(mao_imgs[:5])
