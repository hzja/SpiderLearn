# 原创
：  【pyqt5界面化工具开发-7】窗口开发-菜单栏窗口QMainWindow

# 【pyqt5界面化工具开发-7】窗口开发-菜单栏窗口QMainWindow

**目录**

[0x00 前言：](#0x00%20%E5%89%8D%E8%A8%80%EF%BC%9A)

[一、调用父类的菜单](#%E4%B8%80%E3%80%81%E8%B0%83%E7%94%A8%E7%88%B6%E7%B1%BB%E7%9A%84%E8%8F%9C%E5%8D%95)

[二、添加菜单内选项](#%E4%BA%8C%E3%80%81%E6%B7%BB%E5%8A%A0%E8%8F%9C%E5%8D%95%E5%86%85%E9%80%89%E9%A1%B9)

---


## 0x00 前言：

> 
QWedget
控件和窗口的父类，自由度高(什么都东西都没有)，没有划分菜单、工具栏、状态栏、主窗口 等区域


QMainWindow
是 QWwidget 的子类，包含菜单栏，工具栏，状态栏，标题栏等，中间部分则为主窗口区域


QDialog
对话框窗口的基类


---


---


## 一、调用父类的菜单

和前面Qwedget一样的结构（不做过多介绍）

可以参考代码中的注释

```
import sys
from PyQt5.QtWidgets import QApplication,  QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        lable = QLabel("文字内容")          # 最后会设置相关的显示方法
        lable.setStyleSheet("font-size:30px;color:red")

        # 调用父类的menuBar，对菜单栏进行操作
        menu = self.menuBar()
        # mac需要额外配置像windows一样显示菜单栏
        # menu.setNativeMenuBar(False)

"""
————————————————————————

中间将添加具体的菜单选项

————————————————————————
"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("QMainWindow")
    w.show()
    sys.exit(app.exec_())
```

---


---


## 二、添加菜单内选项

添加一些子菜单选项在里面

```
import sys
from PyQt5.QtWidgets import QApplication,  QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        lable = QLabel("文字内容")          # 最后会设置相关的显示方法
        lable.setStyleSheet("font-size:30px;color:red")

        # 调用父类的menuBar，对菜单栏进行操作
        menu = self.menuBar()
        # mac需要额外配置像windows一样显示菜单栏
        # menu.setNativeMenuBar(False)


#——————————————————————————————————
# 如下为菜单中添加相关内容

        # 向菜单栏添加内容1
        file_menu = menu.addMenu("文件")
        # 内容子键的添加
        file_menu.addAction("新建")
        file_menu.addAction("打开")
        file_menu.addAction("保存")


        # 向菜单栏添加内容2
        edit_menu = menu.addMenu("编辑")
        # 内容子键的添加
        edit_menu.addAction("剪切")
        edit_menu.addAction("复制")
        edit_menu.addAction("粘贴")


# ——————————————————————————————————


        # 设置内容的显示
        self.setCentralWidget(lable)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("QMainWindow")
    w.show()
    sys.exit(app.exec_())
```

运行效果如下图所示：
