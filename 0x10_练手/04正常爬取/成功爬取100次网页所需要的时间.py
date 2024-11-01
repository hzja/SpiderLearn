import requests
import time
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_ecoding
        return r.text
    except:
        return "产生异常"
if __name__ == "__main__":
    start = time.perf_counter()
    url = "https://hao.360.com/"
     
    for i in range(100):
        textstr = getHTMLText(url)
    dur = time.perf_counter() - start
    print("爬取100次网页的时间为{:5f}s".format(dur))
