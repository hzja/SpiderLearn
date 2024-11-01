# 原创
：  Python字符串

# Python字符串

### 知识点

```
s1 = 'hello world'
print(s1.index('o'))
print(s1.find('o'))
print(s1.rindex('o'))
print(s1.rfind('o'))

s2 = 'hEllO WorLd'
# 转换后都将产生一个新的字符串对象
print(s2.upper())           # 转换为大写
print(s2.lower())           # 转换为小写
print(s2.swapcase())        # 大小写互转
print(s2.capitalize())      # 第一个字符转换为大写 其它的转换为小写
print(s2.title())           # 每个单词的第一个字符转换为大写 剩下的为小写

s3 = 'H3rmesk1t is so weak!'
print(s3.center(30))
print(s3.center(30,'-'))
print(s3.ljust(30))
print(s3.ljust(30,'-'))
print(s3.rjust(30))
print(s3.rjust(30,'-'))
print(s3.zfill(30))         # 右对齐 只能有一个参数填写宽度 用0填充

s4 = 'Hi Python'
s5 = 'Hi-Python-Hermes'
print(s4.split())
print(s5.split())
print(s5.split(sep='-'))
print(s5.split(sep='-',maxsplit=1))     # sep指定分隔符 maxsplit最大分割次数
print(s5.rsplit(sep='-',maxsplit=1))    # rsplit从右边开始分割

s6 = 'pythonissocool'
s7 = 'python1ss0cool'
print(s6.isidentifier())        # 判断指定的字符串是不是合法的标识符
print(s6.isspace())             # 判断指定的字符串是否全部由空白字符组成(回车、换行、水平制表符)
print(s6.isalpha())             # 判断指定的字符串是否全部由字母组成
print(s7.isalpha())
print(s6.isalnum())             # 判断字符串是否全部由字母和数字组成
print(s7.isalnum())
print(s6.isdecimal())           # 判断指定的字符串是否全部由十进制的数字组成
print(s7.isnumeric())           # 判断指定的字符串是否全部由数字组成

s8 = 'haaaaaa keep running'
list1 = ['haa','you','are','so','cool']
tuple1 = ('hoo','she','is','so','beautiful')
print(s8.replace('a','o',3))        # 参数一指定被替换字符 参数二指定替换所用的字符串 参数三表示最大替换次数
print("-".join(list1))              # 元组或列表中的字符串合并成一个字符串
print("~".join(tuple1))

# eval() 函数用来执行一个字符串表达式，并返回表达式的值
# eval(expression[, globals[, locals]])
s9 = '(3 * 7 - 1) // 5 + 100'
print(eval(s9))

# 大小比较
s10 = 'helloa'
s11 = 'hellob'
print(s10 &gt; s11)
print(s10 &lt; s11)

# 字符串切片操作
s12 = 'hello,python'
print(s12[:5] + '~' + s12[6:])
s13 = s12[::-1]
print(s13)
s14 = s13[:6] + ',' + s13[7:]
print(s14[::-1])
print(s12[::2])
print(s12[::-2])

# 格式化字符串
s15 = '{123456-qwerty-1qaz-2wsx-mko08uhb}'
print('flag is %s' % s15)           # 占位符方法 %s-&gt;字符串 %d-&gt;整数 %f-&gt;浮点数 %x.yf-&gt;x表示总宽度，y表示精度
print('%.7f' % 3.1415926)
print('%10.5f' % 3.1415926)
print('flag is {}'.format(s15))     # {}方法
print('{}'.format(3.1415926))       # {:.x}表示一共x位 {:.xf}表示小数点后x位
print('{:.3}'.format(3.1415926))
print('{:.3f}'.format(3.1415926))
print(f'flah is {s15}')             # f-string方法

# 字符串的编码与解码
s16 = '成都理工大学'
print(s16.encode(encoding='GBK'))       # 一个中文占两个字节
print(s16.encode(encoding='UTF-8'))     # 一个中文占三个字节

b1 = b'\xb3\xc9\xb6\xbc\xc0\xed\xb9\xa4\xb4\xf3\xd1\xa7'
b2 = b'\xe6\x88\x90\xe9\x83\xbd\xe7\x90\x86\xe5\xb7\xa5\xe5\xa4\xa7\xe5\xad\xa6'
print(b1.decode(encoding='GBK'))
print(b2.decode(encoding='UTF-8'))

```

### 输出结果

```
4
4
7
7
HELLO WORLD
hello world
HeLLo wORlD
Hello world
Hello World
    H3rmesk1t is so weak!     
----H3rmesk1t is so weak!-----
H3rmesk1t is so weak!         
H3rmesk1t is so weak!---------
         H3rmesk1t is so weak!
---------H3rmesk1t is so weak!
000000000H3rmesk1t is so weak!
['Hi', 'Python']
['Hi-Python-Hermes']
['Hi', 'Python', 'Hermes']
['Hi', 'Python-Hermes']
['Hi-Python', 'Hermes']
True
False
True
False
True
True
False
False
hoooaaa keep running
haa-you-are-so-cool
hoo~she~is~so~beautiful
104
False
True
hello~python
nohtyp,olleh
hello,python
hlopto
nhy,le
flag is {123456-qwerty-1qaz-2wsx-mko08uhb}
3.1415926
   3.14159
flag is {123456-qwerty-1qaz-2wsx-mko08uhb}
3.1415926
3.14
3.142
flah is {123456-qwerty-1qaz-2wsx-mko08uhb}
b'\xb3\xc9\xb6\xbc\xc0\xed\xb9\xa4\xb4\xf3\xd1\xa7'
b'\xe6\x88\x90\xe9\x83\xbd\xe7\x90\x86\xe5\xb7\xa5\xe5\xa4\xa7\xe5\xad\xa6'
成都理工大学
成都理工大学

```
