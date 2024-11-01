import requests
import json
import pymysql
import time 
'运行成功,爬取到2903条数据'

url = 'https://neris.csrc.gov.cn/falvfagui/rdqsHeader/informationController'
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
db = pymysql.connect(host='localhost',user='root',password='root',database='finance')#用于连接数据库
mycursor = db.cursor()#获取数据库指针
#创建数据表
sql = 'CREATE TABLE IF NOT EXISTS falvzixun (id INT AUTO_INCREMENT PRIMARY KEY, filename VARCHAR(500), filenumber VARCHAR(500), filedepartment VARCHAR(500),filedate VARCHAR(150) )CHARSET=utf8; '
mycursor.execute(sql)

for i in range(76,146):
    time.sleep(15)
    #获取数据
    data= {'pageNo' : i,'lawType' : 1}
    requests.packages.urllib3.disable_warnings()
    jsons = requests.post(url,headers=headers,data=data,verify=False)
    print('成功获取数据第{}页数据'.format(i))
    jsons.content.decode('UTF-8')
    data = jsons.json()#把获取到的字典类型页面变成json()格式
    pageList = data['pageUtil']['pageList']

    for page in pageList:
        file_name=page['secFutrsLawName']
        file_number=page['fileno']
        file_department=page['lawPubOrgName']
        file_date=page['secFutrsLawVersion']
        
        #把获取到的数据写入到数据表中
        mycursor = db.cursor()
        sql = 'INSERT INTO falvzixun (filename,filenumber,filedepartment,filedate) VALUE (%s,%s,%s,%s)'
        val = (file_name,file_number,file_department,file_date)
        mycursor.execute(sql,val)
        db.commit()#更新数据表

        print('成功写入数据:{},{},{},{}'.format(file_name,file_number,file_department,file_date))