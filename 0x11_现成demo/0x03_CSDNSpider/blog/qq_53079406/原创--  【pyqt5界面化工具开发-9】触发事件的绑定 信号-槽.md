# 原创
：  【pyqt5界面化工具开发-9】触发事件的绑定 信号-槽

# 【pyqt5界面化工具开发-9】触发事件的绑定 信号-槽

**目录**

[0x00 前言：](#0x00%20%E5%89%8D%E8%A8%80%EF%BC%9A)

[一、基础代码布局](#%E4%B8%80%E3%80%81%E5%9F%BA%E7%A1%80%E4%BB%A3%E7%A0%81%E5%B8%83%E5%B1%80)

[二、添加逻辑代码](#%E4%BA%8C%E3%80%81%E6%B7%BB%E5%8A%A0%E9%80%BB%E8%BE%91%E4%BB%A3%E7%A0%81)

[三、触发事件绑定逻辑代码](#%E4%B8%89%E3%80%81%E8%A7%A6%E5%8F%91%E4%BA%8B%E4%BB%B6%E7%BB%91%E5%AE%9A%E9%80%BB%E8%BE%91%E4%BB%A3%E7%A0%81)

---


## <br/>0x00 前言：

> 
1.信号(signal)<br/> 事件(点击、关闭等状态发生改变的触发事件)
<br/> 2.槽( slot)<br/> 捕获信号后---&gt;执行相应的逻辑代码
<br/> 3.信号-槽 链接<br/> 为实现：触发事件---&gt;执行对应的逻辑
需要把信号 和 槽函数 绑定到一起操作

方法：<br/> 对象.信号.connect(槽函数)


## 一、基础代码布局

拿前面的QDialog对话框代码为例

下面已经有点击事件了

（我们还需要加上逻辑代码，然后将点击事件与对应的逻辑代码相绑定）

```
import sys
from PyQt5.QtWidgets import QApplication,  QPushButton, QDialog

# 对话框（多运用于弹窗）

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_btn = QPushButton("确定",self)
        ok_btn.setGeometry(50,100,100,30)

        no_btn = QPushButton("取消", self)
        no_btn.setGeometry(300, 100, 100, 30)



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


## 二、添加逻辑代码

加上需要与触发事件对应的逻辑代码

（写好逻辑代码后，就只需要将他们相绑定）

```
import sys
from PyQt5.QtWidgets import QApplication,  QPushButton, QDialog

# 对话框（多运用于弹窗）

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_btn = QPushButton("确定",self)
        ok_btn.setGeometry(50,100,100,30)

        no_btn = QPushButton("取消", self)
        no_btn.setGeometry(300, 100, 100, 30)


#————————————————————————————————————————
# 逻辑代码如下

    # 点击事件对应的逻辑函数代码
    def ok_clicked(self,arg):
        print("点击了ok")

    def no_clicked(self,arg):
        print("点击了取消")

# ————————————————————————————————————————

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


## 三、触发事件绑定逻辑代码

方法：

对象.信号.connect(槽函数)

```
import sys
from PyQt5.QtWidgets import QApplication,  QPushButton, QDialog

# 对话框（多运用于弹窗）

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_btn = QPushButton("确定",self)
        ok_btn.setGeometry(50,100,100,30)

        no_btn = QPushButton("取消", self)
        no_btn.setGeometry(300, 100, 100, 30)

# ————————————————————————————————————————————————————————————————————
# 绑定如下

        # 绑定按钮的点击事件
        ok_btn.clicked.connect(self.ok_clicked)
        no_btn.clicked.connect(self.no_clicked)
# —————————————————————————————————————————————————————————————————————


    # 点击事件对应的逻辑函数代码
    def ok_clicked(self,arg):
        print("点击了ok")

    def no_clicked(self,arg):
        print("点击了取消")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 根据命名自己改（我每个都以MainWindow就不改了）
    w = MainWindow()
    w.setWindowTitle("对话框")
    w.show()
    sys.exit(app.exec_())
```

可以看见触发了对应的逻辑代码
