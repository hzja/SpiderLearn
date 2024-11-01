import requests
import time
from bs4 import BeautifulSoup

def getcontent(chapter):
    url = "https://www.jjwxc.net/onebook.php?"
    params =  {
        "novelid":"5762871",
        "chapterid":f"{chapter}",
    }
    headers =  {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76",
        "Cookie": "testcookie=yes; JJSESS=%7B%22clicktype%22%3A%22%22%7D; timeOffset_o=4088.10009765625; Hm_lvt_bc3b748c21fe5cf393d26c12b2c38d99=1712809859; smidV2=20240411123059308c5cf8a304cab304f4e104fbef473300d64966d6e80bd10; JJEVER=%7B%22shumeideviceId%22%3A%22WC39ZUyXRgdFLkejW+Yp+mAlzPIWAUdgN25iwW2xsTJBkwx7zYI3GO1oeYa9trJR8afIK+dZ1q/SlsS7HazEq7VaNkCGnCUwLtL/WmrP2Tav+DYF2YqyHqz3TvYY0ILhc3fVLMpg6KnK+4M2GQH+t5J4mCbdPQ1BRajW7hxiYtqOGduzx9VSOoUCqgMwPBHjV0JSgM/vzIa0G7wWr0zokqyjkIpcb1KPXnJYefQjkrhF0sIc7uvoZ0gZlZvkF7JuG2eDSNFSlDac%3D1487577677129%22%7D; Hm_lpvt_bc3b748c21fe5cf393d26c12b2c38d99=1712809868"
    }

    response = requests.get(url, params=params)
    response.encoding = response.apparent_encoding
    beautiful_soup = BeautifulSoup(response.text, 'html.parser')
    content = beautiful_soup.find_all("div", attrs={"style":"font-size: 16px;line-height: 1.8;padding: 0 19px 25px;font-family: 'Microsoft YaHei', PingFangSC-Regular, HelveticaNeue-Light, 'Helvetica Neue Light', sans-serif !important", "onselectstart":"return false", "oncopy":"return false"})
    precontent = content[0].text.split(f"第 {params.get('chapterid')} 章")[1]
    precontent = precontent.split("插入书签")[0]
    precontent = precontent.replace("　　","\n")

    with open(f"第{params.get('chapterid')}章.txt", "w", encoding="utf-8") as f:
        f.write(precontent)

for i in range(1,110):
    getcontent(i)
    time.sleep(5)
    print(f"已完成第{i}章下载......................................\n")