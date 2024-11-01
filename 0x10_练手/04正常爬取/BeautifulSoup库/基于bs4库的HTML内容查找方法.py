import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.icourse163.org/home.htm?userId=1034112247#/home/course')
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
soup.find_all(name,attrs,recursive,string,**kwargs)
"""
∙ name : 对标签名称的检索字符串
∙ attrs: 对标签属性值的检索字符串，可标注属性检索
∙ recursive: 是否对子孙全部检索，默认True
∙ string: <>…</>中字符串区域的检索字符串


<tag>(..) 等价于 <tag>.find_all(..)
soup(..)  等价于 soup.find_all(..)
"""
