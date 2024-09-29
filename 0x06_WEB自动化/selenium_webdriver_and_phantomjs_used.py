from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import xlwt
import time

driverPath =r'F:\Google\phantomjs-2.1.1-windows\bin\phantomjs.exe'# phantomjs驱动文件所在的路径，路径必须全部是中文，否则会报错
driver = webdriver.PhantomJS(driverPath)#获取phantomjs驱动的对象,实现对浏览器的隐形调用
WAIT = WebDriverWait(driver,10)#driver是驱动，10是指最长超时时间不超过10秒

book = xlwt.Workbook(encoding='utf-8', style_compression=0)#创建一个workbook并设置编码为utf-8
sheet = book.add_sheet('菜虚坤篮球视频', cell_overwrite_ok=True)#创建一个worksheet
sheet.write(0,0,'名称')#写入excel，参数对应行、列、值（下同）
sheet.write(0,1,'播放地址')
sheet.write(0,2,'播放时长')
sheet.write(0,3,'视频简介')
sheet.write(0,4,'观看次数')
sheet.write(0,5,'弹幕条数')
sheet.write(0,6,'上传时间')
sheet.write(0,7,'up主')
n = 1

def gettotal():
    try:
        print('开始访问b站···')
        driver.get('https://www.bilibili.com')#使用浏览器打开bilibili网址
        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#nav_searchform > input')))#找到搜索框所在位置并获取对象
        input.send_keys('蔡徐坤')#向搜索框中输入值
        button = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#nav_searchform > div > button')))#找到搜索框对应的按钮并获取对象
        button.click()#对按钮进行点击操作
        print('跳转到新的页面')
        handles = driver.window_handles#获取浏览器现在所有的窗口
        driver.switch_to_window(handles[-1])#切换到最新的窗口，0是原来的窗口
        getsource()
        total = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.last > button')))#找到总页数所对应的元素并获取对象
        return int(total.text)#返回页面总数的值
    except TimeoutException:
        return ""

def getsource():
    html = driver.page_source#获取页面源码
    soup = BeautifulSoup(html,'lxml')#用BeautifulSoup库对页面源码进行解析
    list = soup.find(class_='video-list clearfix').find_all(class_='video-item matrix')#获取页面元素

    for item in list:#对页面元素进行处理
        item_name = item.a.attrs['title']
        item_location = item.a.attrs['href']
        item_time = item.find(class_='so-imgTag_rb').text
        item_introduction = item.find(class_='des hide').text
        item_watched_times = item.find(class_='so-icon watch-num').text
        item_danmu_numbers = item.find(class_='so-icon hide').text
        item_up_time = item.find(class_='so-icon time').text
        item_up = item.find(class_='up-name').text
        print('爬取:' + item_name)

        global n

        sheet.write(n,0,item_name)
        sheet.write(n,1,item_location)
        sheet.write(n,2,item_time)
        sheet.write(n,3,item_introduction)
        sheet.write(n,4,item_watched_times)
        sheet.write(n,5,item_danmu_numbers)
        sheet.write(n,6,item_up_time)
        sheet.write(n,7,item_up)
        #写入需要保存的信息
        n = n +1

def nextpage(pagenumber):
    try:
        print('获取第'+str(pagenumber)+'页数据')
        next = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.next > button')))
        #WAIT即WebDriverWait(driver,10).until(method，message="")，调用该方法提供的驱动程序作为参数，直到返回值为True
        #WAIT即WebDriverWait(driver,10).until_not(method，message="")调用该方法提供的驱动程序作为参数，直到返回值为False
        #在设置时间（10s）内，等待后面的条件发生。如果超过设置时间未发生，则抛出异常。在等待期间，每隔一定时间（默认0.5秒)，调用until或until_not里的方法，直到它返回True或False.
        next.click()
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.active > button'),str(pagenumber)))
        getsource()#获取页面源码
    except TimeoutException:
        return ""


def main():
    try:
        total = gettotal()#得到总页数
        print(total)
        getsource()#得到第一页的页面源码
        for i in range(2,int(total)+1):#对所有的页数进行遍历，并获取数据
            nextpage(i)
    finally:
        driver.close()#关闭chrome浏览器
        book.save(u'蔡虚坤打球视频.xls')#在同一目录下保存Excel文件


main()

#使用phantomjs前要使用webdriver进行显性处理，然后再用phantomjs进行隐性处理