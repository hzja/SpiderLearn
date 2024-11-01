# 原创
：  【pyqt5界面化工具开发-13】QtDesigner功能择优使用

# 【pyqt5界面化工具开发-13】QtDesigner功能择优使用

**目录**

[0x00 前言：](#0x00%20%E5%89%8D%E8%A8%80%EF%BC%9A)

[一、完成基本的布局](#%E4%B8%80%E3%80%81%E5%AE%8C%E6%88%90%E5%9F%BA%E6%9C%AC%E7%9A%84%E5%B8%83%E5%B1%80)

[二、其他功能的使用](#%E4%BA%8C%E3%80%81%E5%85%B6%E4%BB%96%E5%8A%9F%E8%83%BD%E7%9A%84%E4%BD%BF%E7%94%A8)

[三、在代码行开发](#%E4%B8%89%E3%80%81%E5%9C%A8%E4%BB%A3%E7%A0%81%E8%A1%8C%E5%BC%80%E5%8F%91)

---


## 0x00 前言：

QtDesigner工具的择优使用：

1、他的界面开发，是我们主要需要使用的功能

2、他的其他功能的使用，有需要就可使用（其他功能我们自己编写自定义的代码会更好）

## 一、完成基本的布局

根据自己的需求，完成界面的布局

优点：界面的布局速度，比我们直接敲代码是要快的

---


---


## 二、其他功能的使用

使用QtDesigner来控制信号出发点逻辑事件

通过下面的选项可以看出，能够触发的逻辑事件都是些基础的（无法自定义的触发）

缺点：所以QtDesigner的其他的功能（信号绑定逻辑操作），不适用我们写自定义的项目

---


---


## 三、在代码行开发

先将ui在py中加载

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
