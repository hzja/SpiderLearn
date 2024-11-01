import requests
import re
import threading
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

# 全局 urls
urls = []

mutex = threading.Lock()


# 循环获取URL
def get_image(start_url):
    global urls
    urls.append(start_url)
    next_url = start_url
    while next_url != "#":
        res = requests.get(url=next_url, headers=headers)

        if res is not None:
            html = res.text
            pattern = re.compile('<a class="next_main_img" href="(.*?)">')
            match = pattern.search(html)
            if match:
                next_url = match.group(1)
                if next_url.find('www.keaitupian') < 0:
                    next_url = f"https://www.keaitupian.net{next_url}"
                print(next_url)
                # 上锁
                mutex.acquire()

                urls.append(next_url)
                mutex.release()


# 保存图片线程
def save_image():
    global urls
    print(urls)

    while True:
        mutex.acquire()  # 上锁
        if len(urls) > 0:
            img_url = urls[0]
            del urls[0]
            mutex.release()
            res = requests.get(url=img_url, headers=headers)

            if res is not None:
                html = res.text

                pattern = re.compile(
                    '<img class="img-responsive center-block" src="(.*?)"/>')

                img_match = pattern.search(html)

                if img_match:
                    img_data_url = img_match.group(1)
                    print("抓取图片中：", img_data_url)
                    try:
                        res = requests.get(img_data_url)
                        with open(f"images/{time.time()}.png", "wb+") as f:
                            f.write(res.content)
                    except Exception as e:
                        print(e)
        else:
            print("等待中，长时间等待，可以直接关闭")


if __name__ == '__main__':
    # 获取图片线程
    gets = threading.Thread(target=get_image, args=(
        "https://www.keaitupian.net/article/202389.html",))
    gets.start()

    save = threading.Thread(target=save_image)
    save.start()
