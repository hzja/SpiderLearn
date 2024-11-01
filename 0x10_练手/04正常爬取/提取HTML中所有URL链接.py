import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.icourse163.org/home.htm?userId=1034112247#/home/course')
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
