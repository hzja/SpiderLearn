# 原创
：  【pyqt5界面化开发-5】网格布局（九宫格）界面

# 【pyqt5界面化开发-5】网格布局（九宫格）界面

## 一、网格布局

需要模块：QGridLayout

代码

```
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QGridLayout



class Windows(QWidget):
    def __init__(self):
        # 调用父类的__init__方法(并传入子类，或实例)
        super(Windows, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('计算器')
        # 先定义最外层的垂直布局（水平布局是QHBoxLayout）
        container = QVBoxLayout()               # 最外层布局器（命名为容器）

        # 输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")
        container.addWidget(edit)               # 添加进目标内

        # 网格布局
        grid = QGridLayout()
        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", ")"],
            2: ["1", "2", "3", "*", "&lt;-"],
            3: ["0", ".", "=", "/", "C"]
        }

        # line_num 是行数，line_data 是行数据
        for line_num, line_data in data.items():
            # col_num是列数 date是数据
            for col_num, col_data in enumerate(line_data):
                btn = QPushButton(col_data)
                grid.addWidget(btn, line_num, col_num)      # 添加到网格布局



        container.addLayout(grid)       # 把网格布局放入容器
        self.setLayout(container)      # 设置显示最外层布局器 (布局器的应用)




if __name__ == '__main__':
    app = QApplication(sys.argv)    # 接收参数（仅有一个）
    w = Windows()           # 创建一个窗口（继承了QWindows,并封装为一个类）
    w.show()                # 展示窗口
    sys.exit(app.exec_())   # 程序进入循环等待，并在退出时关闭应用
```
