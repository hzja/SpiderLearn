import requests
from bs4 import BeautifulSoup
import os
import sys

def GetContent(url,headers):
  response = requests.get(url,headers)
  response.encoding = response.apparent_encoding
  content = BeautifulSoup(response.text, 'html.parser')
  booknametag = content.find("div", "bookname")
  bookname = booknametag.text
  bookname = bookname.strip()
  bookname = bookname.split("作者")[0]
  bookcontenttag = content.find("div", attrs={"id": "content", "name": "content"})
  bookcontent = bookcontenttag.text.strip()
  bookcontent = bookcontent.split("笔趣阁 www.biquge5.la，最快更新剑来 ！")[1]
  bookcontent = bookcontent.replace("    ", "\n\n    ")
  return bookname, bookcontent

def CreateFile(bookname, bookcontent):
  os.chdir("剑来")
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
  BaseUrl = "https://www.biquge5.la/book/5653/"
  headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'
  }
  response = requests.get(BaseUrl, headers)
  response.encoding = response.apparent_encoding
  UrlsPage = BeautifulSoup(response.text, 'html.parser')
  UrlsPoints = UrlsPage.find_all("dd")
  urls = []

  if os.path.exists("剑来"):
    print("剑来文件夹已存在")
  else:
    os.mkdir("剑来")

  for UrlsPoint in UrlsPoints:
    try:
      url = BaseUrl + UrlsPoint.a["href"]
      urls.append(url)
      title = UrlsPoint.a.string
      print(f"{title}的网址 : {url}")
      bookname, bookcontent = GetContent(url, headers)
      CreateFile(bookname, bookcontent)
    except Exception as e:
      print("捕获到的异常:")
      print("异常类型:", type(e))
      print("异常信息:", e)
      continue

if  __name__ == '__main__':
  GetUrls()
  print("爬取完成")