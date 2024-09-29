import csv
import pandas

with open('test.csv',mode='w',) as f:#用于写csv文件
    fieldnames = ['我是谁','我在哪','我在干什么']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'我是谁':'hzj1','我在哪':'高州','我在干什么':'吃饭'})
    writer.writerow({'我是谁':'hzj2','我在哪':'保定','我在干什么':'读书'})
    writer.writerow({'我是谁':'hzj3','我在哪':'北京','我在干什么':'培训'})

hzj = pandas.read_csv('test.csv',encoding='GBK')#用于读取csv文件
print(hzj)

a = ['hzj1','hzj2','hzj3']
b = ['广东','河北','北京']
c = ['读书','读书','读书']

df = pandas.DataFrame({'我是谁':a,'我在哪':b,'我在干什么':c})
df.to_csv('test1.csv',index=False,sep='，')#to_csv,用于写成csv文件