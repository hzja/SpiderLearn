from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import xlwt
import time

driverPath =r'F:\Google\GoogleChrome_80.0.3987.106_PortableSoft\ChromePortable\App\Google Chrome\chromedriver.exe'
driver = webdriver.Chrome(driverPath)
WAIT = WebDriverWait(driver,20)

book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('科比比赛集锦',cell_overwrite_ok=True)
sheet.write(0,0,'视频名称')
sheet.write(0,1,'视频介绍')
sheet.write(0,2,'视频地址')
sheet.write(0,3,'视频播放量')
n = 1

def gettotal():
    try:
        url = 'https://www.bilibili.com/'
        driver.get(url)
        print('正在打开b站......')
        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#nav_searchform > input')))
        button = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#nav_searchform > div > button')))
        input.send_keys('科比比赛集锦')
        button.click()
        print('正在跳转页面.....')
        handles = driver.window_handles
        driver.switch_to_window(handles[1])
        getinfo()
        total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.last > button')))
        return int(total.text)
    except TimeoutError:
        return ''

def getinfo():
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    print(soup)
    list = soup.find(class_='video-list clearfix').find_all(class_='video-item matrix')
    for item in list:
        item_name = item.find(class_='headline clearfix').find(class_='title').text
        item_introduction = item.find(class_='des hide').text
        item_address = item.a.attrs['href']
        item_address = 'https:' + item_address
        item_play = item.find(class_='so-icon watch-num').text

        print('正在爬取:' + item_name + '(' + item_address +')')

        global n

        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_introduction)
        sheet.write(n, 2, item_address)
        sheet.write(n, 3, item_play)
        n = n + 1

def nextpage(pagenumber):
    try:
        print('正在获取第' + str(pagenumber) + '页数据')
        button = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.next > button')))
        button.click()
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.active'),str(pagenumber)))
        getinfo()
    except TimeoutError:
        return ''

def main():
    try:
        total = gettotal()
        for i in range(2,int(total)+1):
            nextpage(i)
    finally:
        driver.close
        book.save('科比比赛集锦.xls')

main()



