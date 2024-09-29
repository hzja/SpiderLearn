import requests
from bs4 import BeautifulSoup
import xlwt
import json

def get_Information(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        if r.status_code == 200:
            return r
        else:
            return "获取失败"
    except:
        return "获取失败"

def handle_Information(html):
    r = BeautifulSoup(html,'lxml')
    list = r.find(class_='row')
    for i in list:
        print(i)

def main():
    url = 'http://www.glidedsky.com/level/web/crawler-basic-1'
    html = get_Information(url)
    html = html.content
    handle_Information(html)
    # print(html)

main()







