# 原创
：  【pyqt5界面化工具开发-1】运行界面程序框架+按钮+文本+位置的设置

# 【pyqt5界面化工具开发-1】运行界面程序框架+按钮+文本+位置的设置

**目录**

[一、运行界面化框架](#%E4%B8%80%E3%80%81%E8%BF%90%E8%A1%8C%E7%95%8C%E9%9D%A2%E5%8C%96%E6%A1%86%E6%9E%B6)

[二、基础控件](#%E4%BA%8C%E3%80%81%E5%9F%BA%E7%A1%80%E6%8E%A7%E4%BB%B6)

[目标1：新增按钮](#%E7%9B%AE%E6%A0%871%EF%BC%9A%E6%96%B0%E5%A2%9E%E6%8C%89%E9%92%AE)

[目标2：新增文本：](#%E7%9B%AE%E6%A0%872%EF%BC%9A%E6%96%B0%E5%A2%9E%E6%96%87%E6%9C%AC%EF%BC%9A)

[目标3：设置位置](#%E7%9B%AE%E6%A0%873%EF%BC%9A%E8%AE%BE%E7%BD%AE%E4%BD%8D%E7%BD%AE)

---


## 一、运行界面化框架

```
import sys

from PyQt5.QtWidgets import QApplication,QWidget



if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()

    # 窗口标题
    w.setWindowTitle("pyqt5程序")

    # 展示窗口
    w.show()

    # 程序进入循环等待
    app.exec_()


```

---


---


## 二、基础控件

### 目标1：新增按钮

需要模块：QPushButton

```
 # 按钮
    btn = QPushButton('按钮')
    # 将按钮放置在窗口中
    btn.setParent(w)
```

代码：

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    # 窗口标题
    w.setWindowTitle("pyqt5程序")

    # 按钮
    btn = QPushButton('按钮')
    # 将按钮放置在窗口中
    btn.setParent(w)

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()



```

方法二：

```
    # 按钮(并将按钮放置在窗口w中)
    btn = QPushButton('按钮',w)
```

代码：

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    # 窗口标题
    w.setWindowTitle("pyqt5程序")

    # 按钮(并将按钮放置在窗口w中)
    btn = QPushButton('按钮',w)

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()
```

---


### 目标2：新增文本：

需要模块：QLabel

```
# 文本(并将文本放置在窗口w中)
    label = QPushButton('账号：', w)
```

代码：

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel

if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    # 窗口标题
    w.setWindowTitle("pyqt5程序")

    # 按钮(并将按钮放置在窗口w中)
    btn = QPushButton('按钮',w)

    # 文本(并将文本放置在窗口w中)
    label = QLabel('账号：', w)

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()
```

图示可以看见，组件叠加在一起了（接下来需要设置他的位置）

---


### 目标3：设置位置

```
label.setGeometry(60,60,60,30)
```

代码：

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel

if __name__ == '__main__':
    # 接收参数（仅有一个）
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()
    # 窗口标题
    w.setWindowTitle("pyqt5程序")

    # 按钮(并将按钮放置在窗口w中)
    btn = QPushButton('按钮',w)

    # 文本(并将文本放置在窗口w中)
    label = QLabel('账号：', w)
    # 设置坐标+大小（x,y,w,h）
    label.setGeometry(60,60,60,30)

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()
```

最后美化一下的代码

```
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel

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

    # 展示窗口
    w.show()
    # 程序进入循环等待
    app.exec_()
```
