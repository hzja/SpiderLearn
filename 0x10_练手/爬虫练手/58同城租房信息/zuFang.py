from typing import AsyncGenerator
import requests
from bs4 import BeautifulSoup
from requests.models import cookiejar_from_dict
import time
import csv

"""
问题：
1.涉及到css加密;
2.关于如何加载更多的问题
3.页面中有些出现无法找到相关内容的问题
"""
page = 0
baseUrl = 'https://bj.58.com'
url = 'https://bj.58.com/pinpaigongyu/pn/{}/?minprice=2000_4000'.format(page)
headers={
        'Referer':'https://callback.58.com',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'Cookies':'f=n; commontopbar_new_city_info=1%7C%E5%8C%97%E4%BA%AC%7Cbj; id58=c5/nfGGAzPAT3QvjD933Ag==; 58tj_uuid=4fcb7f90-b12e-44f8-9364-c15f3c4d1782; new_uv=1; utm_source=; init_refer=; spm=; als=0; f=n; new_session=0; wmda_uuid=70cd0a5f6b5aae52d671bd8864de8f67; wmda_new_uuid=1; wmda_session_id_10104579731767=1635832008129-7e17ffb6-48f4-b376; wmda_visited_projects=%3B10104579731767; crmvip=""; dk_cookie=""; PPU="UID=21403642119175&UN=lihaili2014_02&TT=8a8cd8ed96bf47c67e92c7384f37886b&PBODY=gUw4EO5-bBeg4LinvOBqeFEOSMjooyQ1v1kt7AIKY1tkrEUKD5k_DBEPhLplbI9iO71T6NpBme-gdyZmefe2yH58ynze5xBxIIcG3GUpKBH_7FVuLJUo3kGSafv9fnnJnyQZOX__g7-Ej88oHbfztZ4LLMtYTTHcVtvXSBemu4I&VER=1&CUID=H5x5VOvYZHWbGmvVtbBlog"; www58com="UserID=21403642119175&UserName=lihaili2014_02"; 58cooper="userid=21403642119175&username=lihaili2014_02"; 58uname=lihaili2014_02; passportAccount="atype=0&bstate=0"; Hm_lvt_dcee4f66df28844222ef0479976aabf1=1635831091,1635832037; Hm_lpvt_dcee4f66df28844222ef0479976aabf1=1635832037; xzfzqtoken=0YTkPQi1KsYEm5onZ2Iitj5A%2FOxqHNdBw8WnX0kdbJnk%2FfZ77wgjSf745OFx4OGkin35brBb%2F%2FeSODvMgkQULA%3D%3D'
        }
with open('Info.csv',mode='w',) as f:
    fieldnames = ['details','rooms','info','key','tag','location','advise']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
while True:

    url = 'https://bj.58.com/pinpaigongyu/pn/{}/?minprice=2000_4000'.format(page)
    page += 1
    time.sleep(5)
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    info = BeautifulSoup(response.text,'lxml')
    list = info.find(class_='list').find_all('li')
    for item in list:
        details = item.find('a').attrs['href']
        details = baseUrl +details
        rooms = item.find(class_='bg-mask').text
        info = item.find(class_='des strongbox').find('h2').text
        key = item.find(class_='room').text
        tags = item.find(class_='spec').find_all('span')
        tag = ''
        for i in tags:
            tag = tag + str(i.text) + ','
        location = item.find(class_='dist').text
        advise = item.find(class_='small-logo').text
        with open(r'info.csv','a+',encoding='gb18030') as f:
            fieldnames = ['details','rooms','info','key','tag','location','advise']
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writerow({'details':details,'rooms':rooms,'info':info,'key':key,'tag':tag,'location':location,'advise':advise})
        print(str(details)+str(rooms)+str(info)+str(key)+str(tag)+str(location)+str(advise))
        print('*'*100)


