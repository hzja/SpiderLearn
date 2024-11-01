import requests
from bs4 import BeautifulSoup
r=requests.get('https://mm.58.com/?utm_source=market&spm=u-2dwj95zvg97pnc46zg.360PCPZ_BT',timeout=30)
r.encoding=r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
soup.title#Tag标签
soup.a #Tag标签
soup.a.name #Tag的名字
soup.a.parent.name #Tag的前一个标签的名字
soup.a.parent.parent.name #Tag的上上个标签的名字
soup.a.attrs #Tag的属性
soup.a.attrs[''] #Tag的某一个属性
type(soup.a.attrs) #Tag属性的类型
type(soup.a) #Tag的类型
soup.a.string #标签的非属性字符串
type(soup.a.string) #标签的非属性字符串的类型
newsoup=BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>","html.parser")
newsoup.b.string#标签内字符串的注释部分
type(newsoup.b.string)#标签内字符串的注释部分的类型
newsoup.p.string#标签的非属性字符串
type(newsoup.p.string)#标签的非属性字符串的类型
