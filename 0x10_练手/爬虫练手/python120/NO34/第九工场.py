from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(level=logging.NOTSET)


def get_html(url, headers) -> None:
    try:
        res = requests.get(url=url, headers=headers, timeout=3)
    except Exception as e:
        logging.debug("采集异常", e)

    if res is not None:
        html_str = res.text
        soup = BeautifulSoup(html_str, "html.parser")
        imgs = soup.find_all(attrs={'class': 'lazy'})
        print("获取到的数据量是", len(imgs))
        datas = []
        for item in imgs:
            name = item.get('alt')
            src = item["src"]
            logging.info(f"{name},{src}")
            # 获取拼接数据
            datas.append((name, src))
        save(datas, headers)


def save(datas, headers) -> None:
    if datas is not None:
        for item in datas:
            try:
                # 抓取图片
                res = requests.get(url=item[1], headers=headers, timeout=5)
            except Exception as e:

                logging.debug("图片采集异常" + str(e))

            if res is not None:
                img_data = res.content
                with open("./imgs/{}.jpg".format(item[0]), "wb+") as f:
                    f.write(img_data)
    else:
        return None


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        "Referer": "https://www.9thws.com/"
    }
    url_format = "https://www.9thws.com/#p{}"
    urls = [url_format.format(i) for i in range(2, 3)]
    # 由于该网站是POST 请求，所以仅抓取一页，目的是测试 BS 的用法
    get_html(urls[0], headers)
