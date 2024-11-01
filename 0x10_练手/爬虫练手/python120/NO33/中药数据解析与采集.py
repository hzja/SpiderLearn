from pyquery import PyQuery as pq
import time
import requests
import os
import re


def get_html(page):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }
    res = requests.get(url='http://www.zhongyoo.com/name/page_{}.html'.format(page), headers=headers, timeout=5)

    res.encoding = "gb2312"

    pq_data = pq(res.text)
    titles = pq_data.find("strong>a.title")

    for item in titles:
        # 下面两种写法都能获取到 href 属性
        # print(pq(item).attr('href'))
        # print(item.attrib['href'])
        link = pq(item).attr('href')
        print(link)
        save(link)
    # return len(res.text)


def save(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }
    doc = pq(url=link, headers=headers, encoding='gbk')
    title = doc('title')
    print(title.text())
    if title:
        title = title.text().split('_')[0]

    text = doc.html()

    with open("./html/{}.html".format(title), "w+") as f:
        f.write(text.encode("gbk", "ignore").decode("gbk"))


def extract_data():
    file_names = os.listdir("./html/")
    for file in file_names:
        with open(f"./html/{file}", "r") as f:
            html_content = f.read()
            # 解析数据
            pq_obj = pq(html_content)
            items = pq_obj.find('div.text p')
            print("获取到的段落数为，", len(items))
            # 等待提取的字符串
            item_str = ""
            for item in items:
                text = pq(item).text()
                item_str += text
            # 使用正则提取数据
            # 正名/中药名/药名
            name_p = re.compile('【(正名|中药名|药名)】([\s\S]*?)【')
            name = name_p.findall(item_str)
            # 别名
            alias_p = re.compile('【别名】([\s\S]*?)【')
            alias = alias_p.findall(item_str)
            # 英文名
            en_name_p = re.compile('【英文名】([\s\S]*?)【')
            en_name = en_name_p.findall(item_str)
            print(name, alias, en_name)


if __name__ == '__main__':
    # 静态页面获取代码逻辑
    """
    page_data = list(range(1, 46))
    ret = map(get_html, page_data)
    for item in ret:
        print(item)
    
    """

    # 数据提取
    extract_data()
