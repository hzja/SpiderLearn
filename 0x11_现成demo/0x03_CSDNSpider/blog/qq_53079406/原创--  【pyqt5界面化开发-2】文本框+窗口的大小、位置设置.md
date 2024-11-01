# 原创
：  【pyqt5界面化开发-2】文本框+窗口的大小、位置设置

# 【pyqt5界面化开发-2】文本框+窗口的大小、位置设置

## 一、目标1：新增文本框：

需要模块：QLineEdit

```
# 文本框
    edit = QLineEdit('请输入账号：', w)
    # 设置坐标+大小（x,y,w,h）
    edit.setGeometry(90, 50, 200, 30)
```

代码：

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel, QLineEdit

if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    # 窗口标题
    w.setWindowTitle("pyqt5程序")

    # 按钮(并将按钮放置在窗口w中)
    btn = QPushButton('确认',w)
    # 设置坐标+大小（x,y,w,h）
    btn.setGeometry(300, 50, 60, 30)

    # 文本(并将文本放置在窗口w中)
    label = QLabel('账号：', w)
    # 设置坐标+大小（x,y,w,h）
    label.setGeometry(50,50,60,30)

    # 文本框
    edit = QLineEdit('请输入账号：', w)
    # 设置坐标+大小（x,y,w,h）
    edit.setGeometry(90, 50, 200, 30)

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()
```

---


---


## 二、目标2：新增文本框：

需要模块：QLineEdit

直接加上文字

```
# 文本框
    edit = QLineEdit('请输入账号：', w)
    # 设置坐标+大小（x,y,w,h）
    edit.setGeometry(90, 50, 200, 30)
```

设置浅灰色文字

```
    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号：')   # 使用setPlaceholderText设置的字体是淡灰色
    # 设置坐标+大小（x,y,w,h）
    edit.setGeometry(90, 50, 200, 30)
```

代码：

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel, QLineEdit

if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    # 窗口标题
    w.setWindowTitle("pyqt5程序")

    # 按钮(并将按钮放置在窗口w中)
    btn = QPushButton('确认',w)
    # 设置坐标+大小（x,y,w,h）
    btn.setGeometry(300, 50, 60, 30)

    # 文本(并将文本放置在窗口w中)
    label = QLabel('账号：', w)
    # 设置坐标+大小（x,y,w,h）
    label.setGeometry(50,50,60,30)

    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号：')   # 使用setPlaceholderText设置的字体是淡灰色
    # 设置坐标+大小（x,y,w,h）
    edit.setGeometry(90, 50, 200, 30)

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()
```

---


---


## 三、目标3：窗口大小、位置的设置：

```
    # 创建一个窗口
    w = QWidget()
    w.resize(700,500)   # 窗口大小设置
    w.move(500,250)     # 窗口打开位置设置
    w.setWindowTitle("pyqt5程序")     # 窗口标题
```

代码：

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel, QLineEdit

if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    w.resize(700,500)   # 窗口大小设置
    w.move(500,250)     # 窗口打开位置设置
    w.setWindowTitle("pyqt5程序")     # 窗口标题

    # 按钮(并将按钮放置在窗口w中)
    btn = QPushButton('确认',w)
    # 设置坐标+大小（x,y,w,h）
    btn.setGeometry(300, 50, 60, 30)

    # 文本(并将文本放置在窗口w中)
    label = QLabel('账号：', w)
    # 设置坐标+大小（x,y,w,h）
    label.setGeometry(50,50,60,30)

    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号：')   # 使用setPlaceholderText设置的字体是淡灰色
    # 设置坐标+大小（x,y,w,h）
    edit.setGeometry(90, 50, 200, 30)

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()
```

---


---


方法一：

窗口设置在屏幕正中间

（需要减去窗口的一半大小）

```
    center_pointer = QDesktopWidget().availableGeometry().center()      # 屏幕中点位置的坐标
    x = center_pointer.x()
    y = center_pointer.y()
    w.move(x-350,y-250)     # 减去窗口大小的一半（因为坐标以窗口的左上角为初始点）
```

代码：

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel, QLineEdit, QDesktopWidget

if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    w.setWindowTitle("pyqt5程序")  # 窗口标题
    w.resize(700,500)   # 窗口大小设置
    # w.move(500,250)     # 窗口打开位置设置

    center_pointer = QDesktopWidget().availableGeometry().center()      # 屏幕中点位置的坐标
    x = center_pointer.x()
    y = center_pointer.y()
    w.move(x-350,y-250)     # 减去窗口大小的一半（因为坐标以窗口的左上角为初始点）



    # 按钮(并将按钮放置在窗口w中)
    btn = QPushButton('确认',w)
    # 设置坐标+大小（x,y,w,h）
    btn.setGeometry(300, 50, 60, 30)

    # 文本(并将文本放置在窗口w中)
    label = QLabel('账号：', w)
    # 设置坐标+大小（x,y,w,h）
    label.setGeometry(50,50,60,30)

    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号：')   # 使用setPlaceholderText设置的字体是淡灰色
    # 设置坐标+大小（x,y,w,h）
    edit.setGeometry(90, 50, 200, 30)

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()
```

方法二：

窗口设置在中间

（自动获取窗口的大小，然后减去一半）

```
    center_pointer = QDesktopWidget().availableGeometry().center()  # 屏幕中点位置的坐标
    x = center_pointer.x()
    y = center_pointer.y()
    old_x, old_y, weight, hight = w.frameGeometry().getRect()    # 获取窗口的相关值
    w.move(x - weight/2, y - hight/2)
```

代码

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel, QLineEdit, QDesktopWidget

if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    w.setWindowTitle("pyqt5程序")  # 窗口标题
    w.resize(700,500)   # 窗口大小设置
    # w.move(500,250)     # 窗口打开位置设置

    # center_pointer = QDesktopWidget().availableGeometry().center()      # 屏幕中点位置的坐标
    # x = center_pointer.x()
    # y = center_pointer.y()
    # w.move(x-350,y-250)     # 减去窗口大小的一半（因为坐标以窗口的左上角为初始点）

    center_pointer = QDesktopWidget().availableGeometry().center()  # 屏幕中点位置的坐标
    x = center_pointer.x()
    y = center_pointer.y()
    old_x, old_y, weight, hight = w.frameGeometry().getRect()    # 获取窗口的相关值
    w.move(x - weight/2, y - hight/2)



    # 按钮(并将按钮放置在窗口w中)
    btn = QPushButton('确认',w)
    # 设置坐标+大小（x,y,w,h）
    btn.setGeometry(300, 50, 60, 30)

    # 文本(并将文本放置在窗口w中)
    label = QLabel('账号：', w)
    # 设置坐标+大小（x,y,w,h）
    label.setGeometry(50,50,60,30)

    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号：')   # 使用setPlaceholderText设置的字体是淡灰色
    # 设置坐标+大小（x,y,w,h）
    edit.setGeometry(90, 50, 200, 30)

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()
```

 
