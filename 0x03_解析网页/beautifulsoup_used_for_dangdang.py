import requests
from bs4 import BeautifulSoup
import xlwt

url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1'
#当当网链接

r = requests.get(url=url)#获取当当网的网页内容
html = r.text
soup = BeautifulSoup(html,'lxml')#把网页内容做成汤

book = xlwt.Workbook(encoding='utf-8', style_compression=0) # 创建一个workbook，设置编码
sheet = book.add_sheet('当当网书籍', cell_overwrite_ok=True) # 创建一个worksheet

sheet.write(0, 0, '序号')
sheet.write(0, 1 ,'名字')
sheet.write(0, 2, '作者')
sheet.write(0, 3, '价格')
# 写入行，列，值
n = 1

list = soup.find(class_="bang_list clearfix bang_list_mode").find_all('li')#找到信息对应位置

for item in list:
    item_number = item.find(class_="list_num").string#获取序号
    item_name = item.find(class_="name").text#获取书名
    item_author = item.find(class_="publisher_info").text#获取作者名字
    item_price = item.find(class_='price_n').text#获取书本价格
    print("爬去电影:" + item_number + ' | '+item_name + " | " + item_author + ' | ' +item_price)
    sheet.write(n, 0, item_number) #写入序号
    sheet.write(n, 1, item_name) #写入书名
    sheet.write(n, 2, item_author) #写入作者
    sheet.write(n, 3, item_price) #写入价格
    n = n + 1

book.save(u'当当网书籍.xls')#保存workbook


print(r.text)
