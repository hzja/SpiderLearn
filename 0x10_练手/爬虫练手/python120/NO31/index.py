from requests_html import HTMLSession, HTML
import random
import time
import os


def get_detail() -> list:
    # 待抓取的详情页地址
    wait_scrapy_urls = []
    # 声明一个 url 模板，用于批量生成待采集地址
    url_format = "http://landchina.mnr.gov.cn/land/crgg/gyyd/index_{}.htm"
    urls = ["http://landchina.mnr.gov.cn/land/crgg/gyyd/index.htm"]
    base_url = "http://landchina.mnr.gov.cn/land/crgg/gyyd/"
    # 测试只存储3页即可
    for page in range(1, 3):
        urls.append(url_format.format(page))
    for url in urls:
        try:
            res = session.get(url, timeout=3)
            res.html.encoding = "utf-8"
            # print(res.html.html)
            details = res.html.find("ul.gu-iconList>li>a")
            for detail in details:
                # http://landchina.mnr.gov.cn/land/crgg/gyyd/202109/t20210904_8081129.htm
                wait_scrapy_urls.append(base_url + detail.attrs['href'][2:])
        except Exception as e:
            print("采集分页数据异常", e)

        # 时间停留
        time.sleep(random.randint(1, 3))

    return wait_scrapy_urls


def save(index: int, url: str) -> str:
    try:
        print("正在采集：", url)
        res = session.get(url=url, timeout=3)
        res.html.encoding = "utf-8"
        with open(f"./htmls/{index}.html", "w+", encoding="utf-8") as f:
            f.write(res.html.html)
    except Exception as e:
        print("采集详情页数据异常", e)
        return save(index, url)


def analysis(html: str) -> list:
    return []


if __name__ == '__main__':
    session = HTMLSession()
    # 获取待抓取的详情页数据
    # scrapy_urls = get_detail()

    # 存储详情页HTML到本地，便于后续分析
    # for index, scrapy_url in enumerate(scrapy_urls):
    #     time.sleep(1)
    #     save(index, scrapy_url)

    # 提取数据
    file_names = os.listdir("./htmls/")
    for file in file_names:
        with open(f"./htmls/{file}", "r", encoding="utf-8") as f:
            html_content = f.read()

            html_doc = HTML(html=html_content)
            # zongdi = html_doc.xpath('//td[contains(text(),"宗地编号：")]/following-sibling::td[1]/text()')
            # #
            # mianji = html_doc.xpath('//td[contains(text(),"宗地总面积：")]/following-sibling::td[1]/text()')
            # for z in mianji:
            #     print(z.strip())
            # 宗地编号：

            zongdi = html_doc.xpath('//td[contains(text(),"宗地编号：")]/../../../table')
            print(file)
            for z in zongdi:
                card_id = z.xpath('.//td[contains(text(),"宗地编号：")]/following-sibling::td[1]/text()')[0].strip()
                mianji = z.xpath('.//td[contains(text(),"宗地总面积：")]/following-sibling::td[1]/text()')[0].strip()
                print(card_id, mianji)
