# 原创
：  8-2 MSF暴力破解SID和检测Oracle漏洞

# 8-2 MSF暴力破解SID和检测Oracle漏洞

#### 暴力破解SID

        当我们发现 Oracle 数据库的 1521 端口时，我们可能考虑使用爆破 SID（System Identifier）来进行进一步的探测和认证。在 Oracle 中，SID 是一个数据库的唯一标识符。当用户希望远程连接 Oracle 数据库时，需要了解以下几个要素：SID、用户名、密码以及服务器的 IP 地址。

```
nmap 192.168.0.100
```

接下来，我们可以使用 Metasploit 框架 (msf) 提供的 sid brute 模块进行暴力破解。具体步骤如下：

1）使用 Metasploit 的命令行界面或控制台。

```
msfconsole
```

2）选择 auxiliary/admin/oracle/sid_brute 模块：

```
use auxiliary/admin/oracle/sid_brute
```

3）查看可配置选项。

```
show options
```

4）设置目标主机的 IP 地址。

```
set RHOSTS 192.168.0.100
```

5）运行模块，开始暴力破解过程。

```
run
```

请注意，在进行任何安全测试之前，请确保已经获得合法的授权，并且仅限于您拥有权限的系统。此外，强烈建议在测试中遵循道德规范和法律准则
