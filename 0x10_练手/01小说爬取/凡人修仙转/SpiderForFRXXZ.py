import requests
from bs4 import BeautifulSoup
import os
import sys
import time

def GetContent(url,headers):
  response = requests.get(url, headers)
  response.encoding = response.apparent_encoding
  content = BeautifulSoup(response.text, 'html.parser')
  contentdiv = content.find("div", attrs={"id": "nr1"})
  bookcontent = contentdiv.text
  bookcontent = bookcontent.replace("\n", "\n\n")
  return bookcontent

def CreateFile(bookname, bookcontent):
  os.chdir("凡人修仙传")
  if os.path.exists(bookname + ".txt"):
      print(f"{bookname},文件已存在")
  else:
    with open(bookname + ".txt", "w", encoding="utf-8") as f:
      f.write(bookname)
      f.write("\n\n")
      f.write(bookcontent)
    print(f"已经爬取{bookname}内容\n")
  os.chdir("..")

def GetUrls():
  BaseUrl = "https://www.kunnu.com/fanren/"
  headers ={
    'Rerferer': 'https://cn.bing.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
    'Cookie': '__gads=ID=44e58611dd7a0c69:T=1715338175:RT=1716739124:S=ALNI_MZiEgvVjgNSuY4atE3ofKTnj8e-dw; __gpi=UID=00000e15f5d31bf2:T=1715338175:RT=1716739124:S=ALNI_MY7LVk7-xekxoWwn7UKPzKYpRZPSA; __eoi=ID=0afbeda79b9c393a:T=1715338175:RT=1716739124:S=AA-AfjbN3auoCchl5zRB2XvIiynT; cf_clearance=Knrtjnq9T2f0OP37ZuuILnyJcG3U1yMwKTEcdtbt5vY-1716739316-1.0.1.1-2zd93bnzGH5sf8NFkgoMHvib84ofrAqEW7I1P6GWHhag180OR5WSMlrFBMpg5P4WdnhrEE1O38hwM9AlRrI42A'
  }
  response = requests.get(BaseUrl, headers)
  response.encoding = response.apparent_encoding
  UrlsPage = BeautifulSoup(response.text, 'html.parser')
  UrlsDiv = UrlsPage.find("div", class_="book-list clearfix")
  UrlsPoints = UrlsDiv.ul.find_all("li")
  urls = []

  if os.path.exists("凡人修仙传"):
    print("凡人修仙转文件夹已存在")
  else:
    os.mkdir("凡人修仙传")

  for UrlsPoint in UrlsPoints:
    try:
      time.sleep(5)
      url = UrlsPoint.a["href"]
      urls.append(url)
      title = UrlsPoint.a["title"]
      title = title.replace(" ", "")
      print(f"{title}的网址 : {url}")
      bookcontent = GetContent(url, headers)
      CreateFile(title, bookcontent)
    except Exception as e:
      print("捕获到的异常:")
      print("异常类型:", type(e))
      print("异常信息:", e)
      continue

if  __name__ == '__main__':
  GetUrls()
  print("爬取完成")