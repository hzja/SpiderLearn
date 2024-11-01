import requests
import time 
from bs4 import BeautifulSoup
import pymysql
 
# 缺点：没有把网站的网址和网站简介爬下来，但大体上成功了

url="https://top.chinaz.com/alltop/index_up.html"
headers = {
     'Cookie':'Hm_lvt_266467aad3d41076dffb7ee6c5fb460a=1637551952; UM_distinctid=17d45b3d1c928d-02acdfee23fcf4-3a36570a-100200-17d45b3d1ca6c0; CNZZDATA5936831=cnzz_eid%3D797462690-1637541883-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1637541883; cz_statistics_visitor=16ba99e4-a0be-fed7-6a9f-5373081ffc70; __gads=ID=da2f20d79fe202c5-22c3ad3c34cf00fc:T=1637552051:RT=1637552051:S=ALNI_MZX_n2FAntFd9z8VTXthx3GJBXFNw; C3VK=2bd9d2; Hm_lpvt_266467aad3d41076dffb7ee6c5fb460a=1637551977',
     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

db=pymysql.connect(host='localhost',user='root',password='root',database='examples')
mycursor=db.cursor()

sql = "CREATE TABLE IF NOT EXISTS `zhanzhangzhijia_zongpaihang` (`id` INT UNSIGNED AUTO_INCREMENT,`paiming` VARCHAR (500),`website` VARCHAR (500),`website_url` VARCHAR (500),`Alexa_index` VARCHAR (500),`website_defen` VARCHAR (500),`paiming_change` VARCHAR (500),PRIMARY KEY (`id`)) ENGINE = INNODB DEFAULT CHARSET = utf8 ;"
mycursor.execute(sql)
print('创建数据表成功')

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.content,'lxml')
items=soup.find_all(class_='ContTit ulli clearfix')

for item in items:
    index = item.find(class_='w90 col-red03 fz16').text
    website = item.find(class_='w320 PCop').a.text
    website_url = url + item.find(class_='w320 PCop').a['href']
    Alexa_index = item.find(class_='w120').text
    website_defen = item.find(class_='w110')
    website_defen = website_defen.next_sibling.next_sibling.text
    paiming_change = item.find(class_='w120 col-green').span.text

    sql = 'INSERT INTO zhanzhangzhijia_zongpaihang (paiming,website,website_url,Alexa_index,website_defen,paiming_change) VALUE (%s,%s,%s,%s,%s,%s)'
    val = (index,website,website_url,Alexa_index,website_defen,paiming_change)
    mycursor.execute(sql,val)
    db.commit()      
print('成功爬取了第{}页'.format(1))


pages = soup.find(class_='ListPageWrap').find_all('a')[-2].text

for i in range(2,int(pages)+1):
    urls = 'https://top.chinaz.com/alltop/index_up_{}.html'.format(str(i))
    time.sleep(10)
    res=requests.get(urls,headers=headers)
    soup = BeautifulSoup(res.content,'lxml')
    items=soup.find_all(class_='ContTit ulli clearfix')

    for item in items:
        index = item.find(class_='w90 col-red03 fz16').text
        website = item.find(class_='w320 PCop').a.text
        website_url = url + item.find(class_='w320 PCop').a['href']
        Alexa_index = item.find(class_='w120').text
        website_defen = item.find(class_='w110')
        website_defen = website_defen.next_sibling.next_sibling.text
        paiming_change = item.find(class_='w120 col-green').span.text
        
        sql = 'INSERT INTO zhanzhangzhijia_zongpaihang (paiming,website,website_url,Alexa_index,website_defen,paiming_change) VALUE (%s,%s,%s,%s,%s,%s)'
        val = (index,website,website_url,Alexa_index,website_defen,paiming_change)
        mycursor.execute(sql,val)
        db.commit()     

    print('成功爬取了第{}页'.format(i))