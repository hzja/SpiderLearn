import os 
from bs4 import BeautifulSoup
import requests
import pymysql

url = 'https://movie.douban.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'referer':'https://movie.douban.com/',
    
}
db = pymysql.connect(host='localhost',user='root',password='root',database='examples')#用于连接数据库
cursor = db.cursor()


response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'lxml')
items = soup.find(class_='ui-slide-content').find_all('li')
i = 1
print(len(items))
for item in items:
    try:
        mycursor = db.cursor
        movie_name = item['data-title']
        movie_preview = item['data-trailer']
        movie_tiem = item['data-duration']
        movie_location = item['data-region']
        movie_actor = item['data-director']
        movie_content = item.find(class_='subject-rate').text
        movie_ticket = item.find(class_='ticket_btn').span.a['href']

        sql = 'INSERT INTO douban_info (movie_name,movie_preview,movie_tiem,movie_location,movie_actor,movie_content,movie_ticket) VALUE (%s,%s,%s,%s,%s,%s,%s)'
        val = (movie_name,movie_preview,movie_tiem,movie_location,movie_actor,movie_content,movie_ticket)
        cursor.execute(sql,val)
        db.commit()#更新数据表
        i = i + 1
    except:
        pass
