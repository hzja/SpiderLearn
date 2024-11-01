# 原创
：  【pyqt5界面化工具开发-10】自定义信号+触发事件

# 【pyqt5界面化工具开发-10】自定义信号+触发事件

**目录**

[第一步：触发事件的绑定](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E8%A7%A6%E5%8F%91%E4%BA%8B%E4%BB%B6%E7%9A%84%E7%BB%91%E5%AE%9A)

[第二步：添加逻辑代码+槽](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E6%B7%BB%E5%8A%A0%E9%80%BB%E8%BE%91%E4%BB%A3%E7%A0%81%2B%E6%A7%BD)

---


## 0x00 前言：

> 
自定义槽
需要新增的模块：from PyQt5.QtCore import pyqtSignal
注意：不要将自定义的信号放在某一个自定义函数里面


---


---


## 第一步：触发事件的绑定

1、其实可以先理清楚触发事件要绑定什么逻辑代码（推荐）

2、也可以先写逻辑代码后，再考虑绑定

（绑定逻辑+绑定槽）

就是触发了事件，需要执行的

```
import sys
import time

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication,  QPushButton, QDialog


class MainWindow(QDialog):

# ————————————————————————————————————————
# 自定义的信号

    # 声明一个信号，放在函数外面
    my_signal = pyqtSignal(str)

# ————————————————————————————————————————

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500,400)
        btn = QPushButton("开始检测",self)
        btn.setGeometry(50,100,100,30)

# ————————————————————————————————————
# 绑定的点击事件（绑定逻辑+绑定槽）

        # 绑定按钮的点击事件(check函数)
        btn.clicked.connect(self.check)

        # 绑定信号和槽(自定义的)
        self.my_signal.connect(self.my_slot)


# ————————————————————————————————————————————————



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


## 第二步：添加逻辑代码+槽

完善槽（自定义）+逻辑代码

```
import sys
import time

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication,  QPushButton, QDialog


class MainWindow(QDialog):
    # 声明一个信号，放在函数外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500,400)
        btn = QPushButton("开始检测",self)
        btn.setGeometry(50,100,100,30)


        # 绑定按钮的点击事件(check函数)
        btn.clicked.connect(self.check)

        # 绑定信号和槽(自定义的)
        self.my_signal.connect(self.my_slot)

# ————————————————————————————————————————————————————————————————————————
# 添加槽（自定义的）+逻辑代码


    # 定义槽
    def my_slot(self,msg):
        print("[+]",msg)


    # 点击事件对应的逻辑函数代码
    def check(self):
        # 下面改为自己的漏洞检测事件
        for i,ip in enumerate(["192.168.1.%d" % x for x in range(1,20)]):
            msg = "正在检测 %s 上的漏洞" % ip
            print(msg)
            # 漏洞的判断
            if i % 5 == 0:
                # 发射信号  对象.信号(参数)
                self.my_signal.emit(msg + "[存在漏洞]")
            # else:
            #     self.my_signal.emit("")
            time.sleep(0.1)

# ————————————————————————————————————————————————————————————————————————————


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 根据命名自己改（我每个都以MainWindow就不改了）
    w = MainWindow()
    w.setWindowTitle("对话框")
    w.show()
    sys.exit(app.exec_())
```

运行结果如下：
