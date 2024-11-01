import requests
r=requests.get('https://www.icourse163.org/learn/BIT-1001870001?tid=1450316449#/learn/content?type=detail&id=1214620498&cid=1218397662')    #修改网址  
r.encoding=r.apparent_encoding
print(r.text)
demo=r.text
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,'html.parser')
print(soup.prettify())
