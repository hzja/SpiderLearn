# 原创
：  Python 3.10 正式发布，新增模式匹配，同事用了直呼真香！

# Python 3.10 正式发布，新增模式匹配，同事用了直呼真香！

---


> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


---


### <font color="#FFB11B">前言</font>

前几天，也就是 10 月 4 日，Python 发布了 3.10.0 版本，什么？3.9 之后居然不是 4.0？（手动狗头）其实龟叔（Guido van Rossum，吉多·范罗苏姆，Python 之父）早在去年 9 月就说了：
1. 3.9 之后的版本为 3.10；事实上，它已经存在（在 Github Master 主分支中）。1. 如果有版本 4，从 3 到 4 的过渡更像从 1 到 2，而不是从 2 到 3。
相比 Python 3.9，Python 3.10 主要的新功能如下：

---


### <font color="#FFB11B">PEP 634 - PEP 636：结构模式匹配</font>

在本次诸多的更新中，Structural Pattern Matching 结构模式匹配，`match-case` 语句无疑是最让人兴奋的功能，也就类似于 Java、C、Go 等其他语言中的 `switch-case` 语句，具体用法可以参考：[PEP 636](https://www.python.org/dev/peps/pep-0636/)

来看一个简单的例子：

```
def http_error(status):
    match status:
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I'm a teapot")
        case _:
            print("Something's wrong with the internet")


http_error(418)  # I'm a teapot
http_error(500)  # Something's wrong with the internet

```

以上代码中，最后一个 `case` 中的 `_` 并不作为变量名，而表示一种特殊的模式，在前面的 `case` 中都未命中的情况下，该 `case` 会是最后的保障，能确保命中，它相当于 Java、C、Go 等语言中的 `default` 分支：

```
public class HttpError {
   public static void main(String args[]){
      int status = 500;
      switch(status){
         case 400:
            System.out.println("Bad request");
         case 404:
            System.out.println("Not found");
         case 418:
            System.out.println("I'm a teapot");
         default:
            System.out.println("Something's wrong with the internet");
      }
   }
}

// Something's wrong with the internet

```

`match-case` 语法支持可变参数 `*args` 和 `**rest`。

`*args` 的用法与 Python 函数中的可变参数是一个用法，允许传入多个参数：

```
def create_user(command):
    match command.split():
        case ["quit"]:
            quit()
        case ["create", user]:
            print("create", user)
        case ["create", *user]:
            for u in user:
                print("create", u)
        case _:
            print("command '{command}' not understood")


create_user("create user1")
create_user("create user2 user3 user4")

# create user1
# create user2
# create user3
# create user4

```

`**rest` 会匹配到字典中所有的 `key` 和 `value`：

```
def get_dict(dic):
    match dic:
        case {**rest}:
            print("get dict:", rest)
        case _:
            print("parameter not understood")


get_dict({"400": "Bad request", "404": "Not found", "418": "I'm a teapot"})

# get dict: {'400': 'Bad request', '404': 'Not found', '418': "I'm a teapot"}

```

<font color="#ff0000">**需要注意的是，结构模式匹配在面对不同的对象时，匹配的规则也有所不同。**</font>

当匹配对象是列表（list）或者元组（tuple）的时候，需要长度和元素值都匹配，才能命中：

```
def create_user(param):
    match param:
        case ("quit"):
            quit()
        case ("create", user):
            print("create", user)
        case ("create", *user):
            for u in user:
                print("create", u)
        case _:
            print("command '{command}' not understood")


create_user(("create", "user1", "user2"))

# create user1
# create user2

```

当匹配对象是一个字典（dict）的时候，只要 case 表达式中的 键（key）在字典对象中存在即可命中，以下示例中，很可能会认为会执行第二个 case，但实际上执行了第一个 case：

```
def if_action(dic):
    match dic:
        case {"action": action}:
            print("action: %s, no object" % action)
        case {"action": action, "object": _}:
            print("action: %s, have object" % action)


if_action({"action": "create", "object": "user1"})

# action: create, no object

```

当匹配对象是类对象（class）的时候，匹配的规则和字典（dict）类似，只要对象类型和对象的属性满足条件即可命中，以下示例中，很可能会认为会执行第二个 case，但实际上执行了第一个 case：

```
class Info:
    def __init__(self, name, age):
        self.name, self.age = name, age


def get_info(people):
    match people:
        case Info(name="Bob"):
            print("case 1")
        case Info(name="Bob", age="20"):
            print("case 2")


people = Info(name="Bob", age="20")
get_info(people)

# case 1

```

---


### <font color="#FFB11B">PEP 604：新型联合运算符（Union Types）</font>

Python 是个弱类型语言，但是在 Python 3 中支持了定义传参和返回类型的写法：

```
def test(a: int) -&gt; int:
    return a**2

```

通常一个参数和返回值只能是一个类型，在 C/C++，Java，Go 等静态语言里，不可能返回两种类型，或者传参使用两种类型，但是在 Python 里可以：

```
def test(a: str or int) -&gt; str or int:
    return a**2

```

这里的 or 写法看着非常不舒服，所以在 Python 3.5 的时候引入了 typing 模块，推荐使用 Uinon 的写法：

```
from typing import Union

def test(a: Union[str, int]) -&gt; Union[str, int]:
    return a**2

```

在本次 Python 3.10.0 更新中，[PEP 604](https://www.python.org/dev/peps/pep-0604/) 允许将联合类型（Union Types）写为 X | Y：

```
def test(a: str | int) -&gt; str | int:
    return a**2

```

新的运算符也可以用作 `isinstance()` 和 `issubclass()` 的第二个参数：

```
print(isinstance(5, int | str))       # True
print(isinstance(None, int | None))   # True
print(issubclass(bool, int | float))  # True
print(isinstance(42, None | str))     # False

```

---


### <font color="#FFB11B">PEP 626：错误调试精确到行</font>

在 [PEP 626](https://www.python.org/dev/peps/pep-0626/) 中，报错提示可以精确到具体行，提示更加详细，在以前的版本中，错误消息一般会指向下一行，而不是实际错误所在的位置，现在可以指向错误代码所在的确切位置。

错误代码示例 1：

```
li = [1, 2, 3

```

之前版本报错：

```
  File "D:\python3Project\test.py", line 5
    
                 ^
SyntaxError: unexpected EOF while parsing

```

Python 3.10 版本报错：

```
  File "D:\python310Project\test.py", line 4
    li = [1, 2, 3
         ^
SyntaxError: '[' was never closed

```

错误代码示例 2：

```
expected = {"name": "Bob", "age": 20
some_other_code = foo()

```

之前版本报错：

```
  File "D:\python3Project\test.py", line 2
    some_other_code = foo()
                  ^
SyntaxError: invalid syntax

```

Python 3.10 版本报错：

```
  File "D:\python310Project\test.py", line 1
    expected = {"name": "Bob", "age": 20
               ^
SyntaxError: '{' was never closed

```

---


### <font color="#FFB11B">PEP 618：zip() 可选长度检查</font>

`zip()` 是 Python 中的内置函数，用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

在以前的版本中，如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，示例如下：

```
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped1 = zip(a, b)
zipped2 = zip(a, c)   # 元素个数与最短的列表一致

print([z for z in zipped1])  # [(1, 4), (2, 5), (3, 6)]
print([z for z in zipped2])  # [(1, 4), (2, 5), (3, 6)]

```

在 [PEP 618 ](https://www.python.org/dev/peps/pep-0618/)中，新增了 strict 参数，设置为 True 时，传入 `zip()` 的两个可迭代项长度必须相等，否则将抛出 `ValueError`

```
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped1 = zip(a, b, strict=True)
zipped2 = zip(a, c, strict=True)

print([z for z in zipped1])
print([z for z in zipped2])

```

报错：

```
[(1, 4), (2, 5), (3, 6)]
Traceback (most recent call last):
  File "D:\python310Project\test.py", line 8, in &lt;module&gt;
    print([z for z in zipped2])
  File "D:\python310Project\test.py", line 8, in &lt;listcomp&gt;
    print([z for z in zipped2])
ValueError: zip() argument 2 is longer than argument 1

```

---


### <font color="#FFB11B">BPO-12782：允许带括号的上下文管理器</font>

Python 上下文管理器对于打开/关闭文件、处理数据库连接和很多其他事情都非常有用，在 Python 3.10.0 中，它们的语法将有一点高质量的改进，在 [BPO-12782](https://bugs.python.org/issue12782) 正式允许带括号的上下文管理器，现在可以用一个 with 语句创建多行，示例如下：

```
with(
    open("text1.txt", encoding="utf-8") as f1,
    open("text2.txt", encoding="utf-8") as f2
):
    print(f1.read(), f2.read())

```

---


### <font color="#FFB11B">PEP 613：显式类型别名</font>

[PEP 613](https://www.python.org/dev/peps/pep-0613/) 使用 TypeAlias 显式标注类型别名，提高可读性。

以前版本，可以看到，x 很容易被搞混：

```
x = int

def plus_int(a: x, b: x) -&gt; x:
    return a+b

```

Python 3.10 中，使用 TypeAlias 表明这是个别名，消除歧义：

```
from typing import TypeAlias

x: TypeAlias = int

def plus_int(a: x, b: x) -&gt; x:
    return a+b

```

---


### <font color="#FFB11B">性能提升</font>

与所有最新版本的 Python 一样，Python 3.10 也带来了一些性能改进。首先是优化 `str()`，`bytes()` 和 `bytearray()` 构造函数，它们速度提升了 30% 左右，代码摘自 [BOP-41334](https://bugs.python.org/issue41334)：

```
$ ./python -m pyperf timeit -q --compare-to=../cpython-release2/python "str()"
Mean +- std dev: [/home/serhiy/py/cpython-release2/python] 81.9 ns +- 4.5 ns -&gt; [/home/serhiy/py/cpython-release/python] 60.0 ns +- 1.9 ns: 1.36x faster (-27%)

$ ./python -m pyperf timeit -q --compare-to=../cpython-release2/python "bytes()"
Mean +- std dev: [/home/serhiy/py/cpython-release2/python] 85.1 ns +- 2.2 ns -&gt; [/home/serhiy/py/cpython-release/python] 60.2 ns +- 2.3 ns: 1.41x faster (-29%)

$ ./python -m pyperf timeit -q --compare-to=../cpython-release2/python "bytearray()"
Mean +- std dev: [/home/serhiy/py/cpython-release2/python] 93.5 ns +- 2.1 ns -&gt; [/home/serhiy/py/cpython-release/python] 73.1 ns +- 1.8 ns: 1.28x faster (-22%)

```

另一个更值得注意的优化（如果你使用类型注释）是，函数参数及其注释不再在运行时（runtime）计算，而是在编译时计算，这使得创建一个带有参数注释的函数的速度提高了大约 2 倍。

除此之外，Python 核心的各个部分还有更多的优化，你可以在 Python bug tracker 的下列问题中找到更多的细节：[BPO-41718](https://bugs.python.org/issue41718)、[BPO-42927](https://bugs.python.org/issue42927)、[BPO-43452](https://bugs.python.org/issue43452)。

---


### <font color="#FFB11B">其他改变</font>
