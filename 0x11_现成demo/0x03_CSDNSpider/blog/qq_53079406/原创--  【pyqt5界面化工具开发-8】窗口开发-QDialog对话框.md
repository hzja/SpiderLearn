# 原创
：  【pyqt5界面化工具开发-8】窗口开发-QDialog对话框

# 【pyqt5界面化工具开发-8】窗口开发-QDialog对话框

**目录**

[一、调用父类的菜单](#%E4%B8%80%E3%80%81%E8%B0%83%E7%94%A8%E7%88%B6%E7%B1%BB%E7%9A%84%E8%8F%9C%E5%8D%95)

[二、添加更多的布局在对话框内](#%E4%BA%8C%E3%80%81%E6%B7%BB%E5%8A%A0%E6%9B%B4%E5%A4%9A%E7%9A%84%E5%B8%83%E5%B1%80%E5%9C%A8%E5%AF%B9%E8%AF%9D%E6%A1%86%E5%86%85)

---


## 一、调用父类的菜单

和前面Qwedget一样的结构（不做过多介绍）

可以参考代码中的注释

```
import sys
from PyQt5.QtWidgets import QApplication,  QPushButton, QDialog

# 对话框（多运用于弹窗）

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

"""
中间为对话框内的内容布局

"""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 根据命名自己改（我每个都以MainWindow就不改了）
    w = MainWindow()
    w.setWindowTitle("对话框")
    w.show()
    sys.exit(app.exec_())
```

---


---


## 二、添加更多的布局在对话框内

这和前面讲的Qwedget窗口布局基本上一样了

```
import sys
from PyQt5.QtWidgets import QApplication,  QPushButton, QDialog

# 对话框（多运用于弹窗）

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

# ——————————————————————————————————————————
# 新增的布局

        ok_btn = QPushButton("确定",self)
        ok_btn.setGeometry(50,100,100,30)

        no_btn = QPushButton("取消", self)
        no_btn.setGeometry(300, 100, 100, 30)

# ———————————————————————————————————————————

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 根据命名自己改（我每个都以MainWindow就不改了）
    w = MainWindow()
    w.setWindowTitle("对话框")
    w.show()
    sys.exit(app.exec_())
```

运行结果：
