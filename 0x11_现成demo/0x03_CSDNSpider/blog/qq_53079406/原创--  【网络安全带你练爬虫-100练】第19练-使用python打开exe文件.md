# 原创
：  【网络安全带你练爬虫-100练】第19练：使用python打开exe文件

# 【网络安全带你练爬虫-100练】第19练：使用python打开exe文件

**目录**

[一、目标1：调用exe文件](#%E4%B8%80%E3%80%81%E7%9B%AE%E6%A0%871%EF%BC%9A%E8%B0%83%E7%94%A8exe%E6%96%87%E4%BB%B6)

[二、目标2：调用exe打开文件](#%E4%BA%8C%E3%80%81%E7%9B%AE%E6%A0%872%EF%BC%9A%E8%B0%83%E7%94%A8exe%E6%89%93%E5%BC%80%E6%96%87%E4%BB%B6)

---


## 一、目标1：调用exe文件

> 
1、subprocess 模块允许在 Python 中启动一个新的进程，并与其进行交互
2、subprocess.run() 函数来启动exe文件
3、subprocess.run(["文件路径"],check=True/)
4、check：如果程序返回一个非零的退出码，subprocess.run() 函数就会抛出一个 CalledProcessError 异常


```
import subprocess

# 启动 notepad.exe 程序，并等待程序运行结束后再继续执行 Python 代码
subprocess.run(["D:\\渗透工具\\010\\010Editor.exe"], check=True)
```

> 
注：
1、Python 会尝试将字符串中类似于 \Uxxxxxxxx 的转义序列转换为对应的 Unicode 字符
2、在 Python 中，反斜杠 \ 是用来表示转义字符的，比如 \n 表示换行符，\t 表示制表符。这里要在字符串中使用反斜杠 \ 字符本身，需要使用双反斜杠 \\ 来表示


---


---


## 二、目标2：调用exe打开文件

> 
1、首先指定要打开的文件名 filename。
2、使用 subprocess.run() 函数启动 exe 程序，并将文件名作为参数传递给程序
3、exe 程序启动后，它会尝试打开指定的文件


```
import subprocess

filename = "D:\\1.png"

# 启动 exe 程序，并将文件名作为参数传递给程序
subprocess.run(["D:\\渗透工具\\010\\010Editor.exe", filename])
```
