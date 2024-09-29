import  pymysql
import pandas
from sqlalchemy import create_engine

db = pymysql.connect(host='localhost',user='root',password='root',database='avidol')#用于连接数据库
cursor = db.cursor()#获取指针
#相应的SQL语句
sql = 'create table beautigirls (name char(200) not null,age int)'
sql1 = 'insert into beautigirls (name,age) value ("hzj","22")'
sql2 = 'delete from beautigirls where age = "22" '
try:
    cursor.execute(sql2)#执行sql语句
    db.commit()#用于对数据库进行更新
except:
    db.rollback()#回滚操作，让事务具有一致性

db.close()#关闭数据库

df = pandas.read_csv('test.csv',encoding='GBK')#读取文件
engine = create_engine('mysql://root@localhost/beautigirls?charset=utf8')#创建engine对象
with engine.connect as conn:#出现__enter__错误，是由于缺乏上下文协议，
    conn.begin()#开始连接
    df.to_sql('beautigirls',conn,if_exists='replace')#转换成SQL语句执行
