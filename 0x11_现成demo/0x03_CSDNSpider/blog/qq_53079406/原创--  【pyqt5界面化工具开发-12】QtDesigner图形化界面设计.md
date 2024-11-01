# 原创
：  【pyqt5界面化工具开发-12】QtDesigner图形化界面设计

# 【pyqt5界面化工具开发-12】QtDesigner图形化界面设计

**目录**

[0x00 前言](#0x00%20%E5%89%8D%E8%A8%80)

[一、启动程序](#%E4%B8%80%E3%80%81%E5%90%AF%E5%8A%A8%E7%A8%8B%E5%BA%8F)

[二、基础的使用](#%E4%BA%8C%E3%80%81%E5%9F%BA%E7%A1%80%E7%9A%84%E4%BD%BF%E7%94%A8)

[三、保存布局文件](#%E4%B8%89%E3%80%81%E4%BF%9D%E5%AD%98%E5%B8%83%E5%B1%80%E6%96%87%E4%BB%B6)

[四、加载UI文件](#%E5%9B%9B%E3%80%81%E5%8A%A0%E8%BD%BDUI%E6%96%87%E4%BB%B6)

---


## 0x00 前言

关于QtDesigner工具的配置等步骤（网上链接也比较多）

下列链接非本人的（如果使用pip 在命令行安装过pyqt5以及tools，那么就可以跳过前面几步了）

[PyCharm安装PyQt5及其工具（Qt Designer、PyUIC、PyRcc）详细教程 - 知乎摘要：Qt是常用的用户界面设计工具，而在Python中则使用PyQt这一工具包，它是Python编程语言和Qt库的成功融合。这篇博文通过图文详细介绍在PyCharm中如何完整优雅地安装配置PyQt5的所有工具包，主要内容包括PyQt5…<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://zhuanlan.zhihu.com/p/469526603](https://zhuanlan.zhihu.com/p/469526603)

---


---


## 一、启动程序

如果是使用的上面的教程，就可以直接在添加的扩展工具里面启动

然后选择对应的窗口进行创建

一些操作的界面展示

（勾选以后就会在界面中进行显示）

---


---


## 二、基础的使用

1、拖动左边的控件到图示上，然后设置好布局

2、然后进行预览

窗口---&gt;预览

预览的界面可以进行点击操作

---


---


## 三、保存布局文件

将其另存为

ui后缀的文件

---


---


## 四、加载UI文件

加载并显示ui文件

```
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *




if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi("./my_win.ui")      # 加载ui文件
    ui.show()                           # 展示窗口

    sys.exit(app.exec_())
```
