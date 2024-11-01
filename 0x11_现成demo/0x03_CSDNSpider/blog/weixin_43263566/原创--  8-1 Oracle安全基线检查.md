# 原创
：  8-1 Oracle安全基线检查

# 8-1 Oracle安全基线检查

### 一、账户安全

#### 1、禁止SYSDBA用户远程连接

用户具备数据库超级管理员（SYSDBA）权限的用户远程管理登录SYSDBA用户只能本地登录，不能远程。REMOTE_LOGIN_PASSWORDFILE函数的Value值为NONE。这意味着禁止共享口令文件，只能通过操作系统认证登录Oracle数据库。

##### 1）检查`REMOTE_LOGIN_PASSWORDFILE` 参数的值，可以执行以下 SQL 语句：

```
show parameter REMOTE_LOGIN_PASSWORDFILE;
```

remote_login_passwordfile 参数表示用于远程登录数据库时所需的身份验证类型。它可以有以下值：

##### 2）加固方式：

将 "remote_login_passwordfile" 参数的值修改为 "NONE"，以加固数据库安全性：

```
ALTER SYSTEM SET remote_login_passwordfile=NONE SCOPE=SPFIL
```
