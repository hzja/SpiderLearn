"""
用selenium软件自动爬取'https://mmzztt.com/photo/'网站内容，
卡点：无法爬取套图中后面的部分，只能获取第一张图
"""
import os
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driverPath = r'F:\Google\GoogleChrome_80.0.3987.106_PortableSoft\ChromePortable\App\Google Chrome\chromedriver.exe'
driver = webdriver.Chrome(driverPath)
WAIT = WebDriverWait(driver,20)

def headers(referer):
    headers = {

        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer':'{}'.format(referer)
    }
    return headers

def main():
    try:
        driver.get('https://mmzztt.com/photo/')
        print('正在打开网站......')
        html = driver.page_source
        soup = BeautifulSoup(html,'lxml')
        list = soup.find(class_='uk-child-width-1-3@m').find_all('article')
        for item in list:
            item_name = item.find(class_='uk-inline').find('img').get('alt')
            item_src = item.find(class_='uk-inline').get('href')
            item_number = item.find(class_='uk-card-badge uk-label u-label').string
            print('正在爬取：%s,链接是：%s,共%s张图片' % (str(item_name),str(item_src),str(item_number)))
            time.sleep(3)
            download(item_src,item_name,item_number)
    except TimeoutException:
        return ''

def download(src,name,number):
    time.sleep(3)
    driver.get(src)
    html = driver.page_source
    # button = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,''
    soup = BeautifulSoup(html, 'lxml')
    html1 = soup.find(class_='uk-inline').find('img').get('src')
    time.sleep(3)
    urllib_download(html1,src,name)
    time.sleep(5)
    button = WAIT.until(EC.element_to_be_clickable((By.CLASS_NAME,'uk-position-center-left')))
    button.click
    time.sleep(5)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])




def urllib_download(url,href,name):
    filename = '%s.jpg' % (name)
    time.sleep(3)
    html = requests.get(url,headers=headers(href))
    with open(filename,'wb') as f:
        f.write(html.content)
    print("已下载：%s.jpg" % (name))

main()

