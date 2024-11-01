# 转载
：  学会Python开发的第一步：写一个桌面小程序

# 学会Python开发的第一步：写一个桌面小程序

当使用桌面应用程序的时候，有没有那么一瞬间，

### 想学习一下桌面应用程序开发？

建议此次课程大家稍作了解不要浪费太多时间，

因为没有哪家公司会招聘以为Python程序员开发桌面程序吧？

### 开发环境：

Python是一种代表简单主义思想的语言。

阅读一个良好的Python程序就感觉像是在读英语一样。

它使你能够专注于解决问题而不是去搞明白语言本身。

PyCharm是一种Python IDE（Integrated Development Environment，集成开发环境），

带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具

比如调试、语法高亮、项目管理、代码跳转、智能提示、自动完成、单元测试、版本控制。

此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发。

### 代码

<br/> 界面设置

1.导入模块

```
import tkinter as tk
```

<br/> 2.实例化一个窗体对象

```
root = tk.Tk()
```

<br/> 3.标题

```
root.title('计算器')
```

<br/> 4.大小以及出现的位置

```
root.geometry("295x280+150+150")

```

<br/> 5.透明度

```
root.attributes("-alpha", 0.9)
```

<br/> 6.背景

```
root["background"] = "#ffffff"
```

<br/> 7.标签

```
lable1 = tk.Label(root, textvariable=result_num, width=20, height=2, font=('宋体', 20), justify='left', background='#ffffff', anchor='se')
```

<br/> 8.布局

```
lable1.grid(padx=4, pady=4, row=0, column=0, columnspan=4)
```

<br/> 9.按钮

```
button_clear = tk.Button(root, text='C', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: clear())
button_back = tk.Button(root, text='←', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: back())
button_division = tk.Button(root, text='/', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: operator('/'))
button_multiplication = tk.Button(root, text='x', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: operator('*'))
 
button_clear            .grid(padx=4, row=1, column=0)
button_back             .grid(padx=4, row=1, column=1)
button_division         .grid(padx=4, row=1, column=2)
button_multiplication   .grid(padx=4, row=1, column=3)
 
button_seven = tk.Button(root, text='7', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('7'))
button_eight = tk.Button(root, text='8', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('8'))
button_nine = tk.Button(root, text='9', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('9'))
button_subtraction = tk.Button(root, text='—', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: operator('-'))
button_seven        .grid(padx=4, row=2, column=0)
button_eight        .grid(padx=4, row=2, column=1)
button_nine         .grid(padx=4, row=2, column=2)
button_subtraction  .grid(padx=4, row=2, column=3)
 
 
button_four = tk.Button(root, text='4', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('4'))
button_four.grid(padx=4, pady=4, row=3, column=0)
button_five = tk.Button(root, text='5', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('5'))
button_five.grid(padx=4, row=3, column=1)
button_six = tk.Button(root, text='6', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('6'))
button_six.grid(padx=4, row=3, column=2)
button_addition = tk.Button(root, text='+', width=5, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: operator('+'))
button_addition.grid(padx=4, row=3, column=3)
 
button_one = tk.Button(root, text='1', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('1'))
button_one.grid(padx=4, row=4, column=0)
button_two = tk.Button(root, text='2', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('2'))
button_two.grid(padx=4, row=4, column=1)
button_three = tk.Button(root, text='3', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('3'))
button_three.grid(padx=4, row=4, column=2)
button_equal = tk.Button(root, text='=', width=5, height=3, font=('宋体', 16), relief='flat', background='#C0C0C0', command=lambda: equal())
button_equal.grid(padx=4, row=4, rowspan=5, column=3)
 
button_zero = tk.Button(root, text='0', width=12, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('0'))
button_zero.grid(padx=4, pady=4, row=5, column=0, columnspan=2)
button_decimal = tk.Button(root, text='.', width=5, font=('宋体', 16), relief='flat', background='#FFDEAD', command=lambda: append_num('.'))
button_decimal.grid(padx=4, row=5, column=2)
```

<br/> 现在得出界面效果<br/> ————————————————<br/> 原文链接：https://blog.csdn.net/m0_72282564/article/details/127904445
