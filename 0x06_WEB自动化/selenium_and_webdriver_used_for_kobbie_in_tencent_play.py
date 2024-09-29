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
sheet = book.add_sheet('腾讯视频——科比',cell_overwrite_ok=True)

sheet.write(0,0,'视频名称')
sheet.write(0,1,'视频地址')

n = 1

def gettotal():
    try:
        url = 'https://v.qq.com/'
        driver.get(url)
        print('正在打开腾讯视频......')
        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#keywords')))
        button = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#searchForm > button')))
        input.send_keys('科比')
        button.click()
        print('正在跳转页面.....')
        handles = driver.window_handles
        driver.switch_to_window(handles[-1])
        getinfo()
        total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.search_container > div.wrapper > div.wrapper_main > div.mod_pages > span > a:nth-child(9)')))
        return int(total.text)
    except TimeoutError:
        return ''

def getinfo():
    html = driver.page_source
    soup = BeautifulSoup(html,'lxml')
    list = soup.find(class_='wrapper_main').find_all(class_='result_item result_item_h _quickopen')
    for item in list:
        item_name = item.find(class_='result_title').a.text
        item_address = item.a.attrs['href']

        print('正在爬取:' + item_name + '(' + item_address +')')

        global n

        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_address)
        n = n + 1

def nextpage(pagenumber):
    try:
        print('正在获取第' + str(pagenumber) + '页数据')
        button = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.search_container > div.wrapper > div.wrapper_main > div.mod_pages > a.page_next')))
        button.click()
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'body > div.search_container > div.wrapper > div.wrapper_main > div.mod_pages > span > a.page_num.current'),str(pagenumber)))
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
        book.save('腾讯视频——科比.xls')

main()



