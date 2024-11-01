import requests

import os

url= "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"   #网页图片的链接

root= "G://图片//"

path= root + url. split('/') [-1] #保存图片的路径

try :

    if not os.path.exists(root):

        os.mkdir(root)

    if not os.path.exists(path):
    
        r = requests.get(url )

        with open (path,'wb') as f:

            f.write(r.content)

            f.close()

            print("文件保存成功")

    else :

        print("文件已存在")

except:

    print ("爬取失败")


""" 网络图片链接的格式：http://www.example.com/picture.jpg
    国家地理：http://www.nationalgeographic.com.cn/
    选择一个图片Web页面：http://www.nationalgeographic.com.cn/photography/photo_of_the_day/3921.html
    图片地址：http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg
"""
