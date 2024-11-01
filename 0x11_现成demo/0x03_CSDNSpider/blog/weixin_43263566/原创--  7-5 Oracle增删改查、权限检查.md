# 原创
：  7-5 Oracle增删改查、权限检查

# 7-5 Oracle增删改查、权限检查

### 一、增 

创建一个hedxtablespace目录

```
# 切换到oracle数据库的目录下
cd /opt/oracle/oradata/ORCLCDB
# 创建目录
mkdir -p hedxtablespace
# 赋予权限
chmod 777 /opt/oracle/oradata/ORCLCDB/hedxtablespace/
```

`oracle/oradata/ORCLCDB`是Oracle数据库的默认数据文件存储目录。在安装Oracle数据库时，可以选择不同的位置来存储数据和日志文件。（我的Oracle数据库是安装的`opt目录下`）

#### 创建表空间

**语法**

```
CREATE TABLESPACE 表空间名称
LOGGING  -- 指定该表空间是否启用重做日志记录。如果出现任何故障，启用日志记录可以恢复表空间中的数据。
DATAFILE '数据文件路径'
SIZE 初始大小
AUTOEXTEND ON  -- 允许自动扩展
NEXT 下一个大小
MAXSIZE 最大大小
EXTENT MANAGEMENT LOCAL;  -- 使用本地extent管理
```

示例

```
CREATE TABLESPACE hgdxtablespace
LOGGING
DATAFILE '/opt/oracle/oradata/ORCLCDB/hedxtablespace/hgdxtablespace.dbf'
SIZE 500M 
AUTOEXTEND ON 
NEXT 200M 
MAXSIZE 2000M 
EXTENT MANAGEMENT LOCAL;
```
