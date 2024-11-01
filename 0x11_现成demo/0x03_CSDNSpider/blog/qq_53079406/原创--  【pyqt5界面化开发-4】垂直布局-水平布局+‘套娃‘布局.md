# 原创
：  【pyqt5界面化开发-4】垂直布局/水平布局+‘套娃‘布局

# 【pyqt5界面化开发-4】垂直布局/水平布局+‘套娃‘布局

**目录**

[一、垂直布局](#%E4%B8%80%E3%80%81%E5%9E%82%E7%9B%B4%E5%B8%83%E5%B1%80)

[二、布局器的组合](#%E4%BA%8C%E3%80%81%E5%B8%83%E5%B1%80%E5%99%A8%E7%9A%84%E7%BB%84%E5%90%88)

[三、水平布局+垂直布局（套娃）](#%E4%B8%89%E3%80%81%E6%B0%B4%E5%B9%B3%E5%B8%83%E5%B1%80%2B%E5%9E%82%E7%9B%B4%E5%B8%83%E5%B1%80%EF%BC%88%E5%A5%97%E5%A8%83%EF%BC%89)

---


## 一、垂直布局

需要模块：QVBoxLayout

```
        # 垂直布局
        layout = QVBoxLayout()

        ………………

        # 应用设置的布局器
        self.setLayout(layout)
```

模块间的伸缩器（可以理解为弹簧，在组件之间添加，加哪哪位置变大）

注：括号内，加数字，可以用来区分不同弹簧间的比例

```
layout.addStretch()
```

代码封装到类中（前面的代码都是直接写的）

```
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget, QVBoxLayout


class Windows(QWidget):
    def __init__(self):
        # 调用父类的__init__方法(并传入子类，或实例)
        super(Windows, self).__init__()

        # 设置大小
        self.resize(700, 500)
        self.setWindowTitle("pyqt5程序")  # 窗口标题

        # 垂直布局
        layout = QVBoxLayout()

        # 按钮
        btn1 = QPushButton('账号')
        layout.addWidget(btn1)      # 添加到布局器
        btn2 = QPushButton('密码')
        layout.addWidget(btn2)      # 添加到布局器
        btn3 = QPushButton('确认')
        layout.addWidget(btn3)      # 添加到布局器

        layout.addStretch(2)

        # 应用设置的布局器
        self.setLayout(layout)


if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    w = Windows()       # 创建一个窗口（继承了QWindows,并封装为一个类）
    w.show()            # 展示窗口
    sys.exit(app.exec_())  # 程序进入循环等待，并在退出时关闭应用
```

---


---


## 二、布局器的组合

> 
垂直布局器+水平布局器
关系：套娃
将多个布局器的垂直水平关系在一个大布局器内确认----&gt;然后再分别处理套娃内的布局器
注意：
对于套娃内的套娃---&gt;放在一个组里面，然后设置组的布局
组需要的模块：QGroupBox
水平+垂直器模块：QHBoxLayout, QVBoxLayout
设置组：group1 = QGroupBox()


---


---


## 三、水平布局+垂直布局（套娃）

代码：

```
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton


class Windows(QWidget):
    def __init__(self):
        # 调用父类的__init__方法(并传入子类，或实例)
        super(Windows, self).__init__()
        self.init_ui()

    def init_ui(self):
        # 先定义最外层的垂直布局（水平布局是QHBoxLayout）:垂直布局+水平布局--&gt;垂直关系
        container = QVBoxLayout()       # 最外层布局器（命名为容器）

        #——————————创建第一个组(垂直布局)——————————#
        group1_box = QGroupBox('target')    # 组
        target_layout = QVBoxLayout()   # 布局

        # 控件
        btn1 = QRadioButton('target1')
        btn2 = QRadioButton('target2')
        btn3 = QRadioButton('target3')
        btn4 = QPushButton('确认')

        # 将控件添加到布局中
        target_layout.addWidget(btn1)
        target_layout.addWidget(btn2)
        target_layout.addWidget(btn3)
        target_layout.addWidget(btn4)

        # 将布局设置到组中
        group1_box.setLayout(target_layout)




        # ——————————创建第二个组(水平布局)——————————#
        group2_box = QGroupBox('test')  # 组
        test_layout = QHBoxLayout()   # 布局

        # 控件
        btn1 = QRadioButton('test1')
        btn2 = QRadioButton('test2')
        btn3 = QRadioButton('test3')


        # 将控件添加到布局中
        test_layout.addWidget(btn1)
        test_layout.addWidget(btn2)
        test_layout.addWidget(btn3)

        # 将布局设置到组中
        group2_box.setLayout(test_layout)



        # 将2个组中添加到最外层布局器中
        container.addWidget(group1_box)
        container.addWidget(group2_box)

        # 设置显示最外层布局器 (布局器的应用)
        self.setLayout(container)

        # 窗口设置
        self.resize(700, 500)            # 设置大小
        self.setWindowTitle("pyqt5程序")  # 窗口标题



if __name__ == '__main__':
    app = QApplication(sys.argv)    # 接收参数（仅有一个）
    w = Windows()           # 创建一个窗口（继承了QWindows,并封装为一个类）
    w.show()                # 展示窗口
    sys.exit(app.exec_())   # 程序进入循环等待，并在退出时关闭应用
```
