# 原创
：  【sql注入-WAF绕过】编写sqlmap的tamper进行sql注入

# 【sql注入-WAF绕过】编写sqlmap的tamper进行sql注入

**目录**

[编写sqlmap的绕过脚本](#sqlmap%E7%9A%84%E7%BB%95%E8%BF%87%E8%84%9A%E6%9C%AC)

[二、理论知识2](#%E4%BA%8C%E3%80%81%E7%90%86%E8%AE%BA%E7%9F%A5%E8%AF%862)

[sqlmap的tamper脚本](#sqlmap%E7%9A%84tamper%E8%84%9A%E6%9C%AC)

[三、实战部分](#%E4%B8%89%E3%80%81%E5%AE%9E%E6%88%98%E9%83%A8%E5%88%86)

---


## <br/><br/>一、理论知识1

### 编写sqlmap的绕过脚本

编写sqlmap的一个简单WAF绕过脚本

```
#!/usr/bin/env python

"""
Copyright (c) 2006-2023 sqlmap developers (https://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOW

def dependencies():
    pass

def tamper(payload, **kwargs):

    hex_str = ''.join([r'~' + hex(ord(c))[2:].zfill(2) for c in payload])
    return hex_str
```

挑重点来讲述一下：

**<u>核心代码：</u>**

hex_str = ''.join([r'~' + hex(ord(c))[2:].zfill(2) for c in payload])

**<u>实现功能：</u>**

使用列表推导式将给定的payload字符串转换为一个十六进制字符串。它遍历payload中的每个字符，将其转换为ASCII码的十六进制表示，并在前面添加~符号和适当的填充零。最后，使用''.join()方法将所有转换后的十六进制字符串连接成一个字符串

**<u>函数含义：</u>**

`1、hex_str = ''`

 定义一个空字符串，用于存储最终的十六进制表示。

2、[r'~' + hex(ord(c))[2:].zfill(2) for c in payload]

 这是一个列表推导式（list comprehension），用于遍历字符串 `payload` 中的每个字符并进行处理。对于每个字符 `c`，它会执行以下操作：

最终，该列表推导式将生成一个包含每个字符十六进制表示的列表。

3、`''.join(...)`: 使用空字符串作为连接符，将列表中的元素连接起来形成一个字符串。也就是将每个字符的十六进制表示拼接在一起。

---


---


## 二、理论知识2

### sqlmap的tamper脚本

sqlmap的tamper中的更多脚本
|序号|脚本名称|注释
|1|0x2char|将每个编码后的字符转换为等价表达
|2|apostrophemask|单引号替换为Utf8字符
|3|apostrophenullencode|替换双引号为%00%27
|4|appendnullbyte|有效代码后添加%00
|5|base64encode|使用base64编码
|6|between|比较符替换为between
|7|bluecoat|空格替换为随机空白字符，等号替换为like
|8|chardoubleencode|双url编码
|9|charencode|将url编码
|10|charunicodeencode|使用unicode编码
|11|charunicodeescape|以指定的payload反向编码未编码的字符
|12|commalesslimit|改变limit语句的写法
|13|commalessmid|改变mid语句的写法
|14|commentbeforeparentheses|在括号前加内联注释
|15|concat2concatws|替换CONCAT为CONCAT_WS
|16|equaltolike|等号替换为like
|17|escapequotes|双引号替换为\\\\
|18|greatest|大于号替换为greatest
|19|halfversionedmorekeywords|在每个关键字前加注释
|20|htmlencode|html编码所有非字母和数字的字符
|21|ifnull2casewhenisnull|改变ifnull语句的写法
|22|ifnull2ifisnull|替换ifnull为if(isnull(A))
|23|informationschemacomment|标示符后添加注释
|24|least|替换大于号为least
|25|lowercase|全部替换为小写值
|26|modsecurityversioned|空格替换为查询版本的注释
|27|modsecurityzeroversioned|添加完整的查询版本的注释
|28|multiplespaces|添加多个空格
|29|nonrecursivereplacement|替换预定义的关键字
|30|overlongutf8|将所有字符转义为utf8
|31|overlongutf8more|以指定的payload转换所有字符
|32|percentage|每个字符前添加%
|33|plus2concat|将加号替换为concat函数
|34|plus2fnconcat|将加号替换为ODBC函数{fn CONCAT()}
|35|randomcase|字符大小写随机替换
|36|randomcomments|/**/分割关键字
|37|securesphere|添加某字符串
|38|sp_password|追加sp_password字符串
|39|space2comment|空格替换为/**/
|40|space2dash|空格替换为--加随机字符
|41|space2hash|空格替换为#加随机字符
|42|space2morecomment|空格替换为/**_**/
|43|space2morehash|空格替换为#加随机字符及换行符
|44|space2mssqlblank|空格替换为其他空符号
|45|space2mssqlhash|空格替换为%23%0A
|46|space2mysqlblank|空格替换为其他空白符号
|47|space2mysqldash|空格替换为--%0A
|48|space2plus|空格替换为加号
|49|space2randomblank|空格替换为备选字符集中的随机字符
|50|symboliclogical|AND和OR替换为&amp;&amp;和||
|51|unionalltounion|union all select替换为union select
|52|unmagicquotes|宽字符绕过GPC
|53|uppercase|全部替换为大写值
|54|varnish|添加HTTP头
|55|versionedkeywords|用注释封装每个非函数的关键字
|56|versionedmorekeywords|使用注释绕过
|57|xforwardedfor|添加伪造的HTTP头

注：不同的脚本可以针对不同的数据库、不同的版本进行使用

---


---


## 三、实战部分

​​​​​​​[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
