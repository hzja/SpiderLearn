# 原创
：  基于 Python 的简单域名反查 IP 脚本

# 基于 Python 的简单域名反查 IP 脚本

**部分数据来源：**ChatGPT

#### 编程思路

本文中，我们将使用 Python 代码实现域名反查功能。具体思路如下：

1. 导入 `socket` 模块；
1. 指定需要反查的域名 `domain_name`；
1. 使用 `socket.getaddrinfo()` 方法获取域名对应的 IP 地址，即进行域名解析；
1. 提取解析结果，生成 IP 地址列表 `ip_list`；
1. 输出 `ip_list`。

#### 编码实现

下面是域名反查代码的具体实现：

`reverse_dns.py` 

```
import socket

# 指定需要反查的域名
domain_name = "www.baidu.com"

# 获取域名解析结果
result = socket.getaddrinfo(domain_name, None)

# 提取所有 IP 地址
ip_list = [item[4][0] for item in result if item[0] == socket.AddressFamily.AF_INET]

# 输出 IP 地址列表
if ip_list:
    print(f"域名 {domain_name} 反查到的 IP 地址是: {ip_list}")
else:
    print(f"域名 {domain_name} 没有匹配的 IP 地址")

```

        在以上代码中，我们通过调用 `socket.getaddrinfo()` 方法来获取域名对应的
