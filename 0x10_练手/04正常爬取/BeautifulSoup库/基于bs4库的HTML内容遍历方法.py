import requests
from bs4 import BeautifulSoup
r=requests.get('https://mm.58.com/?utm_source=market&spm=u-2dwj95zvg97pnc46zg.360PCPZ_BT')
demo=r.text
soup=BeautifulSoup(demo,"html.parser")

#标签树的下行遍历
print(soup.head)
print(soup.head.contents)
print(soup.body.contents)
len(soup.body.contents)
soup.body.contents[1]

#遍历儿子节点
for child in soup.body.children:
    print(child)
#遍历子孙节点
for child in soup.body.descendants:
    print(child)

#标签树的上行遍历
print(soup.title.parent)
print(soup.html.parent)
print(soup.parent)

#遍历所有先辈节点，包括soup本身
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
        
#标签树的平行遍历
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)
print(soup.a.previous_sibling.previous_sibling)
print(soup.a.parent)

#遍历后续节点
for sibling in soup.a.next_sibling:
    print(sibling)
#遍历前续节点
for sibling in soup.a.previous_sibling:
    print(sibling)
