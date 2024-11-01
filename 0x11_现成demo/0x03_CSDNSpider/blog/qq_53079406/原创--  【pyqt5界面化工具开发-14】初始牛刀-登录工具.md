# 原创
：  【pyqt5界面化工具开发-14】初始牛刀-登录工具

# 【pyqt5界面化工具开发-14】初始牛刀-登录工具

**目录**

[0x00 前言：](#0x00%20%E5%89%8D%E8%A8%80%EF%BC%9A)

[一、准备好ui的加载](#%E4%B8%80%E3%80%81%E5%87%86%E5%A4%87%E5%A5%BDui%E7%9A%84%E5%8A%A0%E8%BD%BD)

[二、获取对应的触发事件](#%E4%BA%8C%E3%80%81%E8%8E%B7%E5%8F%96%E5%AF%B9%E5%BA%94%E7%9A%84%E8%A7%A6%E5%8F%91%E4%BA%8B%E4%BB%B6)

[三、触发事件绑定](#%E4%B8%89%E3%80%81%E8%A7%A6%E5%8F%91%E4%BA%8B%E4%BB%B6%E7%BB%91%E5%AE%9A)

[三、输入内容的调用](#%E4%B8%89%E3%80%81%E8%BE%93%E5%85%A5%E5%86%85%E5%AE%B9%E7%9A%84%E8%B0%83%E7%94%A8)

[三、完善登录逻辑](#%E4%B8%89%E3%80%81%E5%AE%8C%E5%96%84%E7%99%BB%E5%BD%95%E9%80%BB%E8%BE%91)

---


## 0x00 前言：

在逻辑代码的处理添加数据包的请求，返回数据包的判断，就可以完整实现登录检测的一个界面化工具了

---


---


## 一、准备好ui的加载

老演员来了

```
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.ui = uic.loadUi("./my_win.ui")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()       # 展示窗口
    sys.exit(app.exec_())
```

---


---


## 二、获取对应的触发事件

如图所示

此处：self.ui为顶层，然后下面为控件

```
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.ui = uic.loadUi("./my_win.ui")

# ————————————————————————————————————————————————————————————————————
# 与布局中控件相对应

        # 获取对应触发事件
        user_name = self.ui.lineEdit        # 用户名
        password = self.ui.lineEdit_2       # 获取密码
        login_btn = self.ui.pushButton      # 登录按钮
        forget_btn = self.ui.pushButton_2   # 忘记密码
        text_browser = self.ui.textBrowser  # 文本显示区域


# ——————————————————————————————————————————————————————————————-——————

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()       # 展示窗口
    sys.exit(app.exec_())
```

---


---


## 三、触发事件绑定

1、绑定触发事件和对应的逻辑

2、写好逻辑处理函数

```
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.ui = uic.loadUi("./my_win.ui")

        # 获取对应触发事件
        user_name = self.ui.lineEdit        # 用户名
        password = self.ui.lineEdit_2        # 获取密码
        login_btn = self.ui.pushButton      # 登录按钮
        forget_btn = self.ui.pushButton_2    # 忘记密码
        text_browser = self.ui.textBrowser  # 文本显示区域

# —————————————————————————————————————————————————————————————————————
# 新增如下

        # 绑定登陆事件的逻辑
        login_btn.clicked.connect(self.login)

    def login(self):
        # 登录逻辑
        print("正在登录中")


# ———————————————————————————————————————————————————————————————————————



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()       # 展示窗口
    sys.exit(app.exec_())
```

---


---


## 三、输入内容的调用

获取到输入框内内容，并在登录逻辑中调用

（其实能在登录逻辑调用，就可以通过逻辑代码进行检测账号密码是否正确了）

```
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.ui = uic.loadUi("./my_win.ui")

        # 获取对应触发事件

# ————————————————————————————————————————————————————————————————————————
# 获取到用户输入

        self.user_name = self.ui.lineEdit        # 用户名
        self.password = self.ui.lineEdit_2       # 获取密码

# ————————————————————————————————————————————————————————————————————————
        login_btn = self.ui.pushButton      # 登录按钮
        forget_btn = self.ui.pushButton_2   # 忘记密码
        text_browser = self.ui.textBrowser  # 文本显示区域


        # 绑定登陆事件的逻辑
        login_btn.clicked.connect(self.login)

    def login(self):
        # 登录逻辑
        print("正在登录中")

#————————————————————————————————————————————————————————————————————————
# 在其他部分调用（并转换格式）

        print(self.user_name.text())
        print(self.password.text())

#————————————————————————————————————————————————————————————————————————


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()       # 展示窗口
    sys.exit(app.exec_())
```

---


---


## 三、完善登录逻辑

1、完善相关数据的获取

2、完善登录的逻辑代码

```
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.ui = uic.loadUi("./my_win.ui")

# ——————————————————————————————————————————————————————————————————————————
# 完善相关数据的获取

        # 获取对应触发事件
        self.user_name = self.ui.lineEdit        # 用户名
        self.password = self.ui.lineEdit_2       # 获取密码
        self.login_btn = self.ui.pushButton      # 登录按钮
        self.forget_btn = self.ui.pushButton_2   # 忘记密码
        self.text_browser = self.ui.textBrowser  # 文本显示区域

#
# ——————————————————————————————————————————————————————————————————————————


        # 绑定登陆事件的逻辑
        self.login_btn.clicked.connect(self.login)


# ——————————————————————————————————————————————————————————————————————————
# 完善登录逻辑

    def login(self):
        # 登录逻辑
        uname = self.user_name.text()
        pw = self.password.text()
        if uname == "admin" and pw == "123456":
            self.text_browser.setText("欢迎%s回来" % uname)
            self.text_browser.repaint()
        else:
            self.text_browser.setText("%s的用户名或密码错误" % uname)
            self.text_browser.repaint()

#
# ——————————————————————————————————————————————————————————————————————————


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.ui.show()       # 展示窗口
    sys.exit(app.exec_())
```

正确登录

错误登录
