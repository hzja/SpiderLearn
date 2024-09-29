import requests
from bs4 import BeautifulSoup
import time
import threading
import xlwt

#设置网址，用一个列表封装
urls = []
for i in range(1,11):
    start = 25*(i-1)
    url = 'https://movie.douban.com/top250?start=%s&filter=' % (str(start))
    urls.append(url)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE',
}
#创建一个列表并写入一部分数据
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('豆瓣评分前250电影',cell_overwrite_ok=True)
sheet.write(0,0,'序号')
sheet.write(0,1,'电影名称')
sheet.write(0,2,'电影介绍')
sheet.write(0,3,'相关人员')
sheet.write(0,4,'评分')
sheet.write(0,5,'主题')
n = 1

def craw(url):#用于爬取网页
    r = requests.get(url,headers = headers)
    time.sleep(2)
    return r.content

def parse(html):#用于处理网页内容
    soup = BeautifulSoup(html,'lxml')
    items = soup.find('ol',class_='grid_view').find_all('li')
    for item in items:#设置这种for-try-except-continue结构可以在循环报错时跳过异常继续执行程序
        try:#在网页中获取内容并写入列表
            xuhao = item.find(class_='pic').find('em').text
            dianying_introduction_path = item.find(class_='hd')
            dianying_introduction = dianying_introduction_path.a.attrs['href']
            dianying_name = item.find(class_='title').text
            xiangguanrenyuan_path = item.find(class_='bd')
            xiangguanrenyuan = xiangguanrenyuan_path.p.text
            pingfen = item.find('span',class_='rating_num').text
            zhuti = item.find('span',class_='inq').text

            global n
            sheet.write(n, 0, str(xuhao))
            sheet.write(n, 1, str(dianying_name))
            sheet.write(n, 2, str(dianying_introduction))
            sheet.write(n, 3, str(xiangguanrenyuan))
            sheet.write(n, 4, str(pingfen))
            sheet.write(n, 5, str(zhuti))
            print('已爬取：%s %s,简介地址：%s,相关工作人员有：%s,评分是：%s,主题是关于%s' %(xuhao,dianying_name,dianying_introduction,xiangguanrenyuan,pingfen,zhuti))
            n = n + 1

        except:
            pass
        continue

def craw_and_parse(url):#爬取链接内容并处理数据
    html = craw(url)
    result = parse(html)

def thread_craw(urls):#创建多线程并用多线程获取网页，处理数据
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw_and_parse,args=(url,))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':#多线程爬虫并保存数据
    thread_craw(urls)
    book.save(u'豆瓣前250评分最高电影.xls')