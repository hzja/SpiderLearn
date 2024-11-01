# 原创
：  【pyqt5界面化工具开发-11】界面化显示检测信息

# 【pyqt5界面化工具开发-11】界面化显示检测信息

**目录**

[0x00 前言：](#0x00%20%E5%89%8D%E8%A8%80%EF%BC%9A)

[一、布局的设置](#%E4%B8%80%E3%80%81%E5%B8%83%E5%B1%80%E7%9A%84%E8%AE%BE%E7%BD%AE)

[二、消息的显示](#%E4%BA%8C%E3%80%81%E6%B6%88%E6%81%AF%E7%9A%84%E6%98%BE%E7%A4%BA)

---


## 0x00 前言：

> 
我们在10讲的基础上，需要将其输出到界面上
思路：
1、消息的传递
2、布局的设置
先考虑好消息的传递，再来完善布局
其实先完善布局，再来设置消息的传递也行
（我不是中国人，就是外国人）


---


---


## 一、布局的设置

将布局设置好以后，我们就可以来绑定消息，以及消息的显示

```
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QDialog):
    # 声明一个信号，放在函数外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()       # 用来存放消息

    def init_ui(self):
        self.resize(500,400)
        container = QVBoxLayout()   # 创建一个整体布局
        self.setLayout(container)   # 设置布局器（主入器）

#————————————————————————————————————————————————————————————-————
# 以下为布局的设置

        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        # 创建垂直布局,用来添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 常见水平布局器
        h_layout = QHBoxLayout()
        btn = QPushButton("开始检测",self)
        # 绑定按钮的点击事件
        btn.clicked.connect(self.check)
        h_layout.addStretch(1)  # 伸缩器
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        # 水平+垂直布局 添加到主容器
        container.addLayout(v_layout)
        container.addLayout(h_layout)


#————————————————————————————————————————————————————————————————

    # 定义槽
    def my_slot(self,msg):
        # 更新内容
        print(msg)



    # 点击事件对应的逻辑函数代码
    def check(self):
        # 下面改为自己的漏洞检测事件
        for i,ip in enumerate(["192.168.1.%d" % x for x in range(1,20)]):
            msg = "正在检测 %s 上的漏洞" % ip
            # print(msg)
            # 漏洞的判断
            if i % 5 == 0:
                # 发射信号  对象.信号(参数)
                self.my_signal.emit(msg + "[存在漏洞]")
            # else:
            #     self.my_signal.emit("")
            time.sleep(0.1)


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


## 二、消息的显示

对于消息的布局+消息的更新显示

```
import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QDialog):
    # 声明一个信号，放在函数外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()       # 用来存放消息

    def init_ui(self):
        self.resize(500,400)
        container = QVBoxLayout()   # 创建一个整体布局
        self.setLayout(container)   # 设置布局器（主入器）

#————————————————————————————————————————————————————————
# 消息的显示界面


        # 显示检测到的界面信息
        self.msg = QLabel("")
        self.msg.resize(400,40)
        self.msg.setWordWrap(True)              # 自动换行
        self.msg.setAlignment(Qt.AlignTop)      # 靠上
        # self.msg.setStyleSheet("background-color:yellow;color:black;")


#————————————————————————————————————————————————————————
        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        # 创建垂直布局,用来添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 常见水平布局器
        h_layout = QHBoxLayout()
        btn = QPushButton("开始检测",self)
        # 绑定按钮的点击事件
        btn.clicked.connect(self.check)
        h_layout.addStretch(1)  # 伸缩器
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        # 水平+垂直布局 添加到主容器
        container.addLayout(v_layout)
        container.addLayout(h_layout)




        # 绑定信号和槽(自定义的)
        self.my_signal.connect(self.my_slot)

    # 定义槽
    def my_slot(self,msg):
        # 更新内容
        print(msg)

#————————————————————————————————————————————————————————————————————————————————————
# 消息的更新

        self.msg_history.append(msg)
        self.msg.setText("&lt;br&gt;".join(self.msg_history))
        self.msg.resize(400,self.msg.frameSize().height() + 40)     # 增加的大小，和设置的每一行的宽高一致
        self.msg.repaint()          # 更新内容，不更新会无显示
        # print("[+]",msg)

#————————————————————————————————————————————————————————————————————————————————————


    # 点击事件对应的逻辑函数代码
    def check(self):
        # 下面改为自己的漏洞检测事件
        for i,ip in enumerate(["192.168.1.%d" % x for x in range(1,20)]):
            msg = "正在检测 %s 上的漏洞" % ip
            # print(msg)
            # 漏洞的判断
            if i % 5 == 0:
                # 发射信号  对象.信号(参数)
                self.my_signal.emit(msg + "[存在漏洞]")
            # else:
            #     self.my_signal.emit("")
            time.sleep(0.1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 根据命名自己改（我每个都以MainWindow就不改了）
    w = MainWindow()
    w.setWindowTitle("对话框")
    w.show()
    sys.exit(app.exec_())
```

运行效果：
