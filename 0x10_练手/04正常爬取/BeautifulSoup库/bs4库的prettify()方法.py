import requests
r=requests.get('https://mm.58.com/?utm_source=market&spm=u-2dwj95zvg97pnc46zg.360PCPZ_BT')
demo=r.text
print(demo)
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,'html.parser')

soup.prettify()
print(soup.prettify())#.prettify()为HTML文本<>及其内容增加'\n' 或者.prettify()可用于标签,方法：<tag>.prettify()
