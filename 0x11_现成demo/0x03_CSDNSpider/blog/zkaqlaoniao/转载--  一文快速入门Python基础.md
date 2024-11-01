# 转载
：  一文快速入门Python基础

# 一文快速入门Python基础

## 一、简介

<br/>         Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言；Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构；

## 二、环境搭建

### <br/> 1.python搭建环境

<br/>         传送：零基础python环境搭建(详细)

### 2.PyCharm安装

<br/> 下载网址：PyCharm：JetBrains为专业开发者提供的Python IDE

        选择适用windows的社区免费版下载，下载其.exe文件；双击安装包根据提示进行安装即可安装

**PyCharm常用插件**

        chinese language：中文语言包

        translation：用于翻译不理解的英文(选中后右键即可选择翻译)

## 三、python基础语法

### <br/> 1.字面量

<br/>         在代码中，被写下来的固定的值，称为字面量；如整数10、浮点数10.6、字符串“hh”等都可以称为字面量；

### 2.注释

<br/>         #用于单行注释，三单引号''' '''和三双引号""" """用于多行注释；

```
a = 10
b = 6.6
# c = "haha"
c = 6
"""
print("%s" % a)
print("%s" % b)
"""
print("%s" % c)
print(666)
 
 
#输出
6
666
```

### <br/> 3.变量

<br/>         变量是在程序运行时，能存储计算结果或能表示值的抽象概念；

变量定义格式：变量名=变量值

```
a = 1
b = "haha"
```

### <br/> 4.标识符

<br/>         变量名、方法名、类名等统称为标识符，用于作内容的标识；

标识符命名规则：大小写敏感、不可使用关键字、内容限定(只能使用英文、数字和下划线且不能以数字开头，python也可以使用中文命名但是不推荐使用）

```
a1 = 10
A1 = 11
_a = 6
# 1a = 5     #使用数字开头，不符合命名规则
# for = 1    #使用关键字，不符合命名规则
print(f"{a1}\n{A1}\n{_a}")
 
 
#输出
10
11
6
```

### <br/> 5.运算符

<br/>**算术运算符**

<img alt="" height="292" src="https://img-blog.csdnimg.cn/direct/27c10454b7fe4fc2ad138a057258aa4a.png" width="528"/><br/><br/>**赋值运算符**

```
a = 3
b = 2
print(a+b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
a *= b
b /= a
print(a)
print(b)
 
 
#输出
5
6
1.5
1
9
6
0.3333333333333333
```

### <br/> 6.字符串

<br/>**字符串定义方法**：单引号定义法、双引号定义法、三引号定义法；

**转义字符 \**：当字符串本身包含引号时，为防止发生歧义需要在字符串的引号前加转义字符\，使其成为普通引号(也可以不用转义字符但需要有正确的引号层次结构)；

**字符串拼接**：字符串之间通过加号+拼接；

**字符串格式化**：%s占位格式化(将变量转换为字符串放到占位处，还有%d、%f等，%5.2f表示浮点数长5位四舍五入保留2位小数)、f"{变量}"格式化；

**表达式格式化**：将表达式的返回值当成变量格式化；

```
a = 'h'
b = "h\"h"
c = """hhh"""
d = "hh"+"gg"
 
print("123-%s-%s-10" % (456, 789))
print("%6.2f" % 10.77777)
print(f"{a}\n{b}\n{d}")
print(f"{1+3}--{2*3}--{type(11)}")
 
 
#输出
123-456-789-10
 10.78
h
h"h
hhgg
4--6--&lt;class 'int'&gt;
```

<br/> 7.数据输入<br/>         使用input()获取键盘输入，并用变量接收键盘输入(input()的参数是输入提示，输入提示可有可无，输入值都为字符串类型，若需要变为其他类型需使用类型转换)；

```
a = input("输入你的名字：")
b = input("输入你的年龄：")
print(f"哦，原来你是{a}，{b}岁")
print(f"a的类型是{type(a)},b的类型是{type(b)}")
 
 
#输入输出
输入你的名字：哈哈
输入你的年龄：19
哦，原来你是哈哈，19岁
a的类型是&lt;class 'str'&gt;,b的类型是&lt;class 'str'&gt;
```

### <br/> 8.缩进

<br/>         python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}；

```
a = 2
if a &gt; 0:
    print(f'{a}是正数')
else:
    print(f'{a}不是正数')
```

## <br/> 四、数据类型

### <br/> 1.数据类型

### <br/> 2.数据类型查看

<br/>         type(变量)可以返回变量存储的数据的数据类型，而变量本身无类型区别；

```
a = 10
b = 1.1
c = True
d = "haha"
e = list()
f = tuple()
print(f"{type(a)}\n{type(b)}\n{type(c)}\n{type(d)}\n{type(e)}\n{type(f)}")
 
 
//输出
&lt;class 'int'&gt;
&lt;class 'float'&gt;
&lt;class 'bool'&gt;
&lt;class 'str'&gt;
&lt;class 'list'&gt;
&lt;class 'tuple'&gt;
```

### <br/> 3.数据类型转换

<br/>         新类型(变量)可返回转换为新类型后的变量；

        任何类型都可以转换为字符串，浮点型转整型只保留整数部分；

```
a = 10
b = 1.1
 
c = bool(a)
d = int(b)
 
print(f"c={c},c的类型为:{type(c)}")
print(f"d={d},c的类型为:{type(d)}")
 
 
//输出
c=True,c的类型为:&lt;class 'bool'&gt;
d=1,c的类型为:&lt;class 'int'&gt;
```

### <br/> 4.数据容器

<br/>         数据容器是指一种可以容纳多个数据元素的数据类型，其中数据元素可以是任意数据类型的数据，如字符串、列表、元组等都可以称为数据容器；

### 5.数据容器对比

## 五、python解释器

<br/>         Python解释器由编译器和虚拟机构成，编译器将源代码转换成字节码，然后再通过Python虚拟机来逐行执行这些字节码；简单来说，Python解释器就是把Python代码解释为计算机能理解的二进制数据，以实现程序的运行；<br/>         Python解释器种类较多，最常用的是CPython，它是C语言开发、使用最广、默认的解释器；

## 六、条件控制语句

### <br/> 1.布尔类型与比较运算符

        非零、非空字符串和成立的表达式都为True，零、空字符串和不成立的表达式为False；

```
a = True
b = False
a1 = 12
b1 = 0
a2 = "hh"
b2 = ""
a3 = 1 == 1
b3 = 1 &gt;= 0
print(f"a为{a}--a1为{bool(a1)}--a2为{bool(a2)}--a3为{a3}")
print(f"b为{b}--b1为{bool(b1)}--b2为{bool(b2)}--b3为{b3}")
 
 
#输出
a为True--a1为True--a2为True--a3为True
b为False--b1为False--b2为False--b3为True
```

### <br/><br/> 2.if语句

> 
<br/> if        判断条件:
        条件成立时需要执行的代码


```
a = 19
if a &gt;= 18:
    print("你已经成年了")
 
 
#输出
你已经成年了
```

<br/> 注意：需要严格使用缩进控制代码的执行层次结构，判断条件后的冒号不可少；

### 3.if [elif] else语句

> 
<br/> if        判断条件1:
        执行代码1
elif      判断条件2:
        执行代码2
else:
        条件都不满足时需要执行的代码


```
a = 19
if a &lt; 18:
    print("你还是个孩子")
elif 18 &lt;= a &lt; 60:
    print("你已经是个成年人了")
else:
    print("你老了")
 
 
#输出
你已经是个成年人了
```

<br/>  注意：if语句尽管有多个执行代码块，只能执行其中一个，判断条件满足时执行对应代码后退出if语句，条件都不满足时执行else对应的代码；

### 4.条件语句的嵌套

```
a = 19
if a &lt; 18:
    print("你还是个孩子")
else:
    if a &lt; 60:
        print("你已经是个成年人了")
    else:
        print("你老了")
 
 
#输出
你已经是个成年人了
```

<br/> 注意：缩进不能错

## 七、循环语句

### <br/> 1.while循环

> 
<br/> while 判断条件:
        只要条件成立循环执行的代码


```
a = 1
while a &lt; 10:
    a += 1
print(f"a={a},a&gt;=10")
 
 
#输出
a=10，a&gt;=10
```

## <br/> 2.for循环

<br/>         for循环是一种轮询机制，对数据容器的元素逐个处理；而while循环是自定义循环条件的；

for 临时变量 in 数据集

        对数据逐个处理的代码

```
a = "hello"
for i in a:
    print(f"{i}-", end="")   #end=""，end为空表示不换行，默认是换行的
print()
for i in range(0, 10):       #range(0, 10)表示0至9的数字集，左闭右开
    print(f"{i}-", end="")
 
 
#输出
h-e-l-l-o-
0-1-2-3-4-5-6-7-8-9-


```

### <br/> 3.break与continue

<br/>         break结束当前层的循环，continue跳过本次循环继续执行下次循环；

```
print("continue的结果：")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"{i}-", end="")
print("\nbreak的结果：")
for i in range(1, 6):
    if i == 3:
        break
    print(f"{i}-", end="")
 
 
#输出
continue的结果：
1-2-4-5-
break的结果：
1-2-
```

### <br/> 4.循环语句的嵌套

<br/> #利用循环嵌套实现九九乘法表的输出<br/>  

```
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={j*i}\t",end="")
    print()
```

//输出<br/> 1*1=1    <br/> 1*2=2    2*2=4    <br/> 1*3=3    2*3=6    3*3=9    <br/> 1*4=4    2*4=8    3*4=12    4*4=16    <br/> 1*5=5    2*5=10    3*5=15    4*5=20    5*5=25    <br/> 1*6=6    2*6=12    3*6=18    4*6=24    5*6=30    6*6=36    <br/> 1*7=7    2*7=14    3*7=21    4*7=28    5*7=35    6*7=42    7*7=49    <br/> 1*8=8    2*8=16    3*8=24    4*8=32    5*8=40    6*8=48    7*8=56    8*8=64    <br/> 1*9=9    2*9=18    3*9=27    4*9=36    5*9=45    6*9=54    7*9=63    8*9=72    9*9=81

##     <br/> 八、字符串

### <br/> 1.定义

```
#可使用单引号、双引号或三引号定义字符串
str1 = 'ha'
str2 = "haha"
str3 = '''hahaha'''
str4 = """hahaha"""
 
print(f"{str1}\n{str2}\n{str3}\n{str4}")
 
 
#输出
ha
haha
hahaha
hahaha
```

### <br/> 2.下标索引

```
my_str = 'hello word!'
# 下标索引正向从0开始，反向从-1开始
print(f"{my_str[0]}-{my_str[1]}-{my_str[2]}-{my_str[-1]}-{my_str[-2]}")
 
 
#输出
h-e-l-!-d
```

### 3.常用方法

### <img alt="" height="435" src="https://img-blog.csdnimg.cn/direct/bcdf15ad174c4479bf733190c407f96c.png" width="521"/><br/><br/> 4.特点

<br/>         可容纳多个字符、元素仅字符、数据是有序存储的(即有下标)、允许存在重复元素、数据是不可修改的；

## 九、列表

### <br/> 1.定义

```
# 定义列表
a1 = [1, 'ha', True]
# 定义空列表
a2 = []
a3 = list()
 
print(f"{a1}\n{a2}\n{a3}")
 
 
#输出
[1, 'ha', True]
[]
[]
```

### <br/> 2.下标索引

```
a = ['ha', 23, True, [1, 2, 3]]
# 下标索引正向从0开始，反向从-1开始
print(f"{a[0]}\n{a[1]}\n{a[2]}\n{a[3]}\n{a[-1]}\n{a[-2]}")
# 容器中嵌套容器时使用多层索引取元素,字符串、列表、元组等作为容器元素时都属于容器嵌套
print(f"{a[3][0]}-{a[3][1]}-{a[3][2]}-{a[0][0]}-{a[0][1]}")
 
 
#输出
ha
23
True
[1, 2, 3]
[1, 2, 3]
True
1-2-3-h-a
```

### <br/> 3.常用方法

### <br/> 4.特点

<br/>         可容纳多个元素、元素可以为不同类型、数据是有序存储的(即有下标)、允许存在重复元素、数据是可修改的；

### 5.列表的循环遍历

```
a = [1, 4, 6, 'haha', True, [1, 2], (7, 8)]
# while循环遍历列表
index = 0
while index &lt; len(a):
    print(f"{a[index]}---", end='')
    index += 1
print()
# for循环遍历列表
for i in a:
    print(f"{i}__", end='')
 
 
#输出
1---4---6---haha---True---[1, 2]---(7, 8)---
1__4__6__haha__True__[1, 2]__(7, 8)__


```

## <br/> 十、元组

### <br/> 1.定义

```
# 定义元组
t1 = (1, 'ha', True)
# 定义的元组只有一个元素时需要在元素后加逗号
t2 = ('haha',)
# 定义空元组
t3 = ()
t4 = tuple()
 
print(f"{t1}\n{t2}\n{t3}\n{t4}")
 
 
#输出
(1, 'ha', True)
haha
()
()
```

### <br/> 2.下标索引

<br/>         与列表类似，下标索引正向从0开始，反向从-1开始，存在容器嵌套时使用多层索引取元素；

### 3.常用方法

### <br/> 4.特点

<br/>         可容纳多个元素、元素可以为不同类型、数据是有序存储的、允许存在重复元素、数据是不可修改的；

### 5.元组的循环遍历

<br/>         与列表类似；

## 十一、序列的切片

<br/>**序列**：有序的数据集合，包括字符串、列表和元组；

**切片**：从序列中取出一个子序列；

**语法**：序列[起始下标:结束下标:步长]

```
my_str = 'hello word!'
 
# 起始下标对应的为第一个元素，结束下标减一对应的为最后一个元素，即左闭右开，步长表示每个隔步长个元素取
print(my_str[0:5:1])
# 留空表示默认取，起始下标默认为0，结束下标默认为最大下标，步长默认为1
print(my_str[:5:1])
print(my_str[0::])
print(my_str[::2])
# 步长为负数表示反向取，反向取时起始下标和结束下标也需要反向标记
print(my_str[-1::-1])
print(my_str[-1:-3:-1])
 
 
#输出
hello
hello
hello word!
hlowr!
!drow olleh
!d
 
#元组和列表与字符串类似，都可以切片
 
my_list = [12, 'hj', True, 6, 'k', False, 88]
print(my_list[1:5:1])
 
my_tuple = (12, 3, 'jjj', True)
print(my_tuple[-1::-1])
 
#输出
['hj', True, 6, 'k']
(True, 'jjj', 3, 12)
十二、集合
1.定义
# 定义集合
set1 = {1, 3, 'haha'}
set2 = {}
# 集合元素不可重复，若存在重复元素自动去重
set3 = {1, 2, 2, 'ha', 'ha'}
 
print(f"{set1}\n{set2}\n{set3}")
 
 
#输出
{1, 3, 'haha'}
{}
{1, 2, 'ha'}
```

### <br/> 2.常用方法<br/><img alt="" height="373" src="https://img-blog.csdnimg.cn/direct/f7287772f41849c5a4d58c38ecc2f2b4.png" width="526"/><br/> 3.特点

<br/>         不允许存在重复元素、数据是无序存储的(即无下标)；

## 十三、字典

### <br/> 1.定义

```
# 定义字典
d1 = {'name': '小明', 'age': 17, 'sex': '男'}
d2 = {}
d3 = dict()
# 字典的value可重复，而key不可重复，若key重复后面的key会覆盖前面的
d4 = {'name': '小红', 'age': 17, 'name': '小美'}
print(f"{d1}\n{d2}\n{d3}\n{d4}")
 
 
#输出
{'name': '小明', 'age': 17, 'sex': '男'}
{}
{}
{'name': '小美', 'age': 17}
```

### <br/> 2.Key取元素

```
dd = {
    'name': '小明', 
    'age': 17, 
    'haha': {'name': '小美', 'age': 17}, 
    'my_list': [1, 3, True, 'hello']
}
# 通过Key获取Value
print(dd['name'])
# 容器嵌套获取元素
print(dd['haha']['name'])
print(dd['my_list'][0:3:1])
 
 
#输出
小明
小美
[1, 3, True]
```

### 3.常用方法

<br/> 方法    作用<br/> 字典[Key]    获取Key对于的Value值<br/> 字典[Key]=Value    增加或更新键值对(Key存在更新而不存在增加键值对)<br/> 字典.pop(Key)    取出并删除Key对应的键值对<br/> 字典.clear()    清空字典<br/> 字典.keys()    获取所有Key，用于for循环<br/> len(字典)    返回字典的元素总数

### <br/> 4.特点

<br/>         Key不可重复、数据是无需存储的；

## 十四、函数

### <br/> 1.介绍

<br/>         函数是组织好的、可重复使用的用于实现特定功能的代码段；

### 2.函数的定义

```

#普通函数的定义

def        函数名(参数):                #参数和return返回值可有可无

             函数体

             return      返回值

#匿名函数的定义

lambda  参数 : 函数体(只能有一行代码)

def add():
    a = 3
    b = 4
    return a + b
 
 
print(add())
 
 
def ha(hh, x, y):
    print(hh(x, y))
 
 
ha(lambda x, y: x + y, 10, 4)
ha(lambda x, y: x - y, 10, 4)
ha(lambda x, y: x ** y, 10, 4)
 
 
//输出
7
14
6
10000
```

<br/>  注意：匿名函数每定义一次只能使用一次，多用于简化计算逻辑的传参

### 3.函数的参数

<br/> 位置参数：调用函数时根据函数定义的参数位置来传参；

关键字参数：函数调用时通过键=值的形式传参；

缺省参数：缺省参数也称为默认参数，调用函数若未传递缺省参数的值时使用默认值作参数值；

不定长参数：不定长参数也称为可变参数，用于不确定调用函数时传递多少个参数的场景(*表示位置传参不定长，**表示关键字传参不定长)；

```
def hello(name, age, sex='男'):
    print(f"{name}的年龄是{age},性别为{sex}")
 
 
hello('小明', 10, '男')                 # 位置参数
hello(sex='男', age=10, name='小明')     # 关键字参数
hello('小明', 10)                    # 缺省参数
hello('小明', 10, '女')              # 缺省参数可被覆盖
 
 
def t1(*args):
    print(f"传入了{len(args)}个参数，它们是：{args}，以{type(args)}类型的形式传入参数")
 
 
t1('a', 123, 'b', 456, 'c', 789)   # 以元组的形式传入不确定个参数
 
 
def t2(**kwargs):
    print(f"传入了{len(kwargs)}个参数，它们是：{kwargs}，以{type(kwargs)}类型的形式传入参数")
 
 
t2(a=123, b=456, c=789)             # 以字典的形式传入不确定个参数
 
 
#输出
小明的年龄是10,性别为男
小明的年龄是10,性别为男
小明的年龄是10,性别为男
小明的年龄是10,性别为女
传入了6个参数，它们是：('a', 123, 'b', 456, 'c', 789)，以&lt;class 'tuple'&gt;类型的形式传入参数
传入了3个参数，它们是：{'a': 123, 'b': 456, 'c': 789}，以&lt;class 'dict'&gt;类型的形式传入参数
```

<br/> 注意：位置参数必须在关键字参数前面，缺省参数可被覆盖，不定长参数传入的是存有数据元素的元组或字典；args和kwargs是规范命名而不是规则命名；

### 4.函数的返回值

<br/>         使用return关键字返回值，若返回多个值返回值之间用逗号隔开且需要多个以逗号隔开的变量接收(无返回值时返回None类型，即空类型)；

```
def haha():
    return 1
 
 
def ha():
    return 1, 2, 3
 
 
a = haha()
print(a)
b1, b2, b3 = ha()
print(f"{b1}, {b2}, {b3}")
 
 
#输出
1
1, 2, 3
```

### <br/> 5.函数的说明文档

<br/>         函数的说明文档对函数及函数参数解释说明，更有利于对函数及函数参数的理解；

```
def add(x, y):
    """
    实现两数相加的功能       #PyCharm在定义函数中输入三个引号后回车会自动补全说明文档的格式
    :param x: 相加的一个值
    :param y: 相加的另一个值
    :return: 返回两数相加的结果
    """
    return x + y
 
 
print(add(5, 2))
 
 
#输出
7
```

### <br/> 6.函数的嵌套调用

        在定义函数时调用另一个函数，即为函数的嵌套调用(需要注意嵌套调用后代码的执行顺序)；

```
def a1(x, y):
    return x + y
 
 
def a2():
    print(123)
    print(a1(17, 6))
    print(456)
 
 
a2()
 
 
#输出
123
23
456
```

### <br/> 7.变量的作用域

<br/>         变量作用域是指变量的作用范围，按作用范围分为局部变量(只在特定范围能生效)和全局变量(全局生效)；

```
a1 = 10
 
 
def test():
    a2 = 10
    global a1  # 在函数内部修改全局变量需要使用global关键字声明，否则会被当作新定义的局部变量
    a1 = 1
    print(a1)     # 全局变量可在所有范围内被调用
    print(a2)
 
 
# print(a2)        #调用函数内部的局部变量会报错
test()
print(a1)
 
 
#输出
1
10
1
```

## <br/> 十五、文件操作

### <br/> 1.文件的编码

<br/>         编码技术是指翻译的规则，记录了内容翻译成二进制及二进制翻译回内容的规则；编码方法有UTF-8、GBK、Unicode、Big5等；UTF-8是全球通用的，一般都使用UTF-8读写文件；

### 2.文件的读取

<img alt="" height="290" src="https://img-blog.csdnimg.cn/direct/6b8b8967c79449169d739025196933de.png" width="528"/><br/>  

```
# 打开文件获取文件对象
# f = open('1.txt', 'r', encoding='UTF-8')  #可使用文件的相对路径或绝对路径
 
# 读取文件指定字节数的内容
# print(f.read())           #读取文件后下次读取时从上次读取结束位置开始读取
 
# 读取文件全部内容
# print(f.read())
 
# 读取文件全部行，返回元素为行内容的列表
# print(f"内容为：{f.readlines()}，类型是：{type(f.readlines())}")
 
# for循环读取文件行
# for line in f:
#     print(line)
 
# 关闭文件
# f.close()
 
# 使用如下格式读取文件后可自动关闭文件
# with open('1.txt', 'r', encoding='UTF-8') as file:
#     for line in file:
#         print(line)
```

### <br/> 3.文件的写入

```
# 打开文件获取文件对象，w模式文件存在重写文件，文件不存在先创建再写文件
f = open('1.txt', 'w', encoding='UTF-8')
# 写入文件
f.write('hello world!')    # 实际上只是写入到了缓存区，并未真正写入文件
# 刷新内容
f.flush()            # 刷新内容，将写入缓存区的内容写入文件，可减少对硬盘的操作
# 关闭文件
f.close()           # close()方法内置了flush()方法
```

### <br/> 4.文件的追加

```
# 打开文件获取文件对象，a模式文件存在在文件末尾追加写入，文件不存在先创建再写文件
f = open('1.txt', 'a', encoding='UTF-8')
# 写入文件
f.write('\na ha ha ha')
# 刷新内容
f.flush()
# 关闭文件
f.close()
```

## <br/> 十六、异常

### <br/> 1.异常的概念

<br/>         当程序检测到错误时，Python解释器就会停止执行，出现错误提示，这就是异常，也称为Bug；

Bug的诞生：1945年9月9日下午三点，马克二型计算机无法正常工作，技术人员最后发现是一只飞蛾导致继电器异常，进而导致计算机无法工作，此后，引发软件失效的缺陷便称之为Bug；

```
# 打开文件获取文件对象，r模式只能打开存在的文件
f = open('1.txt', 'r', encoding='UTF-8')   #r打开不存在的文件会产生异常
# 关闭文件对象
f.close()
 
 
#输出
Traceback (most recent call last):
  File "E:\python Project\1.py", line 2, in &lt;module&gt;
    f = open('1.txt', 'r', encoding='UTF-8')
FileNotFoundError: [Errno 2] No such file or directory: '1.txt'
```

### <br/> 2.异常的捕获

<br/>         捕获异常的作用在于 提前假设某处会出现异常并做好提前处理方法，当异常真正出现时，程序能正确处理而不是中断程序的运行；

```
try:

        可能发生的错误代码

except:

        出现异常时执行的代码

[else:]

        无异常时执行的代码

[finally:]

        有无异常都要执行的代码

# 简单的异常捕获
# try:
#     # 可能出现异常的代码
#     f = open('1.txt', 'r', encoding='UTF-8')
# except:
#     # 出现异常后执行的代码
#     f = open('1.txt', 'w', encoding='UTF-8')
# else:                            # else表示没有出现异常时执行的代码，可有可无
#     print('没有出现异常‘)
# finally:                         # finally表示不管有无异常都要执行的代码，可有可无
#     f.close()
# f.close()
 
# 捕获指定异常
# try:
#     print(haha)
# except NameError as e:     # 未指定的异常不会被捕获，若出现将导致程序的终止
#     print('出现了变量未定义的异常')
#     print(e)     # e是自定义表示异常的对象
 
# 捕获多个异常
# try:
#     print(1/0)
# except (NameError, ZeroDivisionError) as e:
#     print('出现了变量未定义的异常或零计算异常')
#     print(e)
 
# 捕获所有异常
# try:
#     f = open('1.txt', 'r', encoding='UTF-8')
# except Exception as e:
#     print('出现了异常')
#     print(e)
```

### <br/> 3.异常的传递

<br/>         当存在异常的函数被不存在异常的函数调用时，在不存在异常的函数中作处理是可以捕获到异常的，这就是异常的传递性；

```
def a1():
    print(haha)
def a2():
    try:
        a1()
    except NameError as ee:
        print(f'捕获到了异常\n异常为：{ee}')
a2()
 
 
#输出
捕获到了异常
异常为：name 'haha' is not defined
```

## <br/> 十七、Python模块

### <br/> 1.概念

<br/>         Python模块(Module)是.py文件，其中能定义函数、类和变量，也可以包含可执行代码；调用不同的模块可以之间使用其中的函数、类等，更加方便代码功能的实现；

### 2.模块导入方式

```
[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

# 导入Python内置的time模块(即time.py文件)
# import time
# time.sleep(5)  # 调用模块内的函数
 
# 导入time模块中的sleep()函数，time模块中只有sleep()函数能被使用
# from time import sleep
# sleep(10)  # 调用导入的函数
 
# 导入time模块的全部内容(*号表示全部内容)
# from time import *    # 与import time的区别是调用模块内的内容时格式不同，如time.sleep()和sleep()
# sleep(5)
 
# 给导入的模块取别名，当模块名过于复杂时使用模块别名更加方便
# import time as t
# t.sleep(5)
```

### <br/>  3.自定义模块

<br/>         导入自定义模块即导入自定义的个性化.py文件；

```
# 自定义模块my_module.py
# __all__ = ['a1']      # 表示调用该模块时可被使用的内容，若无__all__声明默认所有可以被使用
 
 
# 这两个函数可在导入该模块后使用
def a1(x, y):
    return x + y
 
 
def a2(x, y):
    return x - y
 
 
if __name__ == '__main__':   # 表示只能在当前文件执行的代码，可有可无
    print(a1(3, 4))
 
print(a2(3, 4))                    # 该模块被调用时会自动执行可执行代码
```

### <br/> 4.Python标准库的模块

<br/> os 模块：

        os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。

sys 模块：

        sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。

time 模块：

        time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。

datetime 模块：

        datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。

random 模块：

        random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。

math 模块：

        math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。

re 模块：

        re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。

json 模块：

        json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。

urllib 模块：

        urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。

## 十八、Python包

### <br/> 1.概念

<br/>         当模块太多时不方便管理，需要使用Python包；Python包相当于一个文件夹，其内包括多个模块.py文件和__init__.py文件(Python包必不可少的)

### 2.自定义Python包

<br/>         在PyCharm项目处右键选择创建Python包即可，成功创建的Python包目录下会自动生成__init__.py文件

```
# __init__.py文件
 
# 可控制Python包内可以被导入的.py模块，无__all__声明则全部模块可被导入
__all__ = ['my_module']
```

### 3.Python包的模块调用

```

# 调用自定义Python包中的模块
import my_packge.my_module as h
print(h.a2(3, 4))
```

### 4.第三方Python包

<br/>         Python包包含许多模块，模块包含许多功能；为实现更多的功能，提高开发效率，在Python程序的生态中产生了非常多的第三方包(非官方的)；

### 5.pip安装Python包

<br/>         第三方Python包是非官方的，Python没有内置，需要自己安装第三方Python包；

**安装方式1：**

        命令行输入pip install 包名称

**安装方式2**：

        在Pycharm的python解释器设置中安装Python包

```
原文链接：https://blog.csdn.net/m0_73185293/article/details/131494324?spm=1001.2014.3001.5501
```

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/0370000f90714205909a625ff816ec91.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/26a40e4f4ac74089aa6014a2948f232b.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4b81cc6b801e42db85a0c27dfe1b4bf3.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/f29f338bd7a04806ae1c72c6c5b395d8.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/41838131765b4ee6989836fc71f0bb70.png" width="665"/>

应急响应笔记

学习路线
