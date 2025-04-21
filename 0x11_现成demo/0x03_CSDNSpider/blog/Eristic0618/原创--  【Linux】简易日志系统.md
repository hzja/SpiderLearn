# 原创
：  【Linux】简易日志系统

# 【Linux】简易日志系统

**目录**

[一、概念](#%E4%B8%80%E3%80%81%E6%A6%82%E5%BF%B5)

[二、可变参数](#%E4%BA%8C%E3%80%81%E5%8F%AF%E5%8F%98%E5%8F%82%E6%95%B0)

[三、日志系统](#%E4%B8%89%E3%80%81%E6%97%A5%E5%BF%97%E7%B3%BB%E7%BB%9F)

---


## 一、概念

一个正在运行的程序或系统就像一个哑巴，一旦开始运行我们很难知晓其内部的运行状态。

但有时在程序运行过程中，我们想知道其内部不同时刻的运行结果如何，这时一个日志系统可以有效的帮助我们监控程序的运行状态。

如果系统或程序发生了错误或存在bug，通过日志的内容我们也可以很快的知道故障的原因并定位错误的位置

一个成熟的日志至少需要包含以下信息：

根据情况可将日志划分为不同的等级，例如常规信息、警告信息、严重错误、致命错误、调试信息

---


## 二、可变参数

日志的内容需要我们指定格式并传参，而参数的个数是不确定的。因此在学习编写日志系统之前，我们先了解一下可变参数的用法

以下是对可变参数进行操作时需要用到的函数/宏

```
#include &lt;stdarg.h&gt;

void va_start(va_list ap, last);
type va_arg(va_list ap, type);
void va_end(va_list ap);

```

我们以一个可以同时累加多个变量的函数为例：

```
int sum(int n, ...)
{}
```

形参在实例化时会从右向左进行压栈，也就是说多个参数在函数栈帧中是连续的，因此我们可以通过地址的偏移来依次访问到所有的参数

首先：

```
int sum(int n, ...)
{
    va_list s;
    va_start(s, n);
}
```

其中va_list实际上就是char*， 而va_start可以让s指向参数n的下一个参数，也就是可变参数的第一个参数的位置。此时我们就有了获取第一个参数内容的前提

这也是为什么printf等支持可变参数的函数中必须至少要有一个确定的参数，有了该参数才能找到可变参数的起始地址

```
int sum(int n, ...)
{
    va_list s;
    va_start(s, n);

    int sum = 0;
    while(n--)
    {
        sum += va_arg(s, int);
    }
    va_end(s);
    return sum;
}

```

其中，va_arg传入s和可变参数的类型，用于提取s指向的参数，并且移动s到下一个参数的位置

va_end将s置为空

测试效果：

拓展问题：如果可变参数中，不同参数有不同的类型怎么办？

这也是为什么printf的第一个参数需要传入一个用于控制格式的字符串，通过遍历字符串就能知道可变参数中有哪些类型了

---


## 三、日志系统

本文实现的日志系统具备以下功能： 

如果要让日志包含文件名和行号，则可以通过宏定义__FILE__和__LINE__获取文件名和行号

接下来是完整代码（附注释）

```
#pragma once

#include &lt;iostream&gt;
#include &lt;time.h&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;fcntl.h&gt;
#include &lt;stdarg.h&gt;

// 日志等级
#define Info 0
#define Debug 1
#define Warning 2
#define Error 3
#define Fatal 4

#define SIZE 1024 // 缓冲区大小

// 日志的输出方式
#define Screen 1    // 输出到显示器
#define Same_file 2 // 输出到同一文件
#define Diff_file 3 // 按照等级输出到不同文件

#define Filename "log.txt"

class Log
{
public:
    Log()
    {
        _method = Screen; // 默认输出到显示器
    }

    void output(int method) // 更改输出方式
    {
        _method = method;
    }

    std::string level2string(int level) // 日志等级转换字符串
    {
        switch (level)
        {
        case Info:
            return "Info";
        case Debug:
            return "Debug";
        case Warning:
            return "Warning";
        case Error:
            return "Error";
        case Fatal:
            return "Fatal";
        default:
            return "None";
        }
    }

    void operator()(int level, const char *format, ...)
    {
        va_list s;
        va_start(s, format); // s指向可变参数
        messagehandle(level, format, s);
    }

    void messagehandle(int level, const char *format, va_list s) // 整合日志字符串
    {
        time_t t = time(nullptr);         // 获取时间戳
        struct tm *ctime = localtime(&amp;t); // 将时间戳转换为时间
        char levelAndtime[SIZE];          // 日志等级和时间部分
        snprintf(levelAndtime, sizeof(levelAndtime), "[%s][%d-%d-%d %02d:%02d:%02d]", level2string(level).c_str(),
                 ctime-&gt;tm_year + 1900, ctime-&gt;tm_mon + 1, ctime-&gt;tm_mday, ctime-&gt;tm_hour, ctime-&gt;tm_min, ctime-&gt;tm_sec);

        char content[SIZE]; // 用户自定义的内容部分
        vsnprintf(content, sizeof(content), format, s);
        va_end(s);

        char message[SIZE * 2]; // 整合所有部分
        snprintf(message, sizeof(message), "%s %s\n", levelAndtime, content);

        OutputLog(level, message); // 将整合后的日志输出
    }

    void OutputLog(int level, const std::string &amp;logmessage)
    {
        switch (_method) // 根据输出方式进行调整
        {
        case Screen: // 输出到显示器
            std::cout &lt;&lt; logmessage &lt;&lt; std::endl;
            break;
        case Same_file: // 输出到同一文件
            SamefileOutput(Filename, logmessage);
            break;
        case Diff_file: // 输出到不同文件
            DiffileOutput(level, logmessage);
            break;
        default:
            break;
        }
    }

    void SamefileOutput(const std::string &amp;filename, const std::string &amp;logmessage)
    {
        int fd = open(filename.c_str(), O_WRONLY | O_CREAT | O_APPEND, 0666); //打开文件
        if(fd &lt; 0) //打开失败
            return;
        write(fd, logmessage.c_str(), logmessage.size()); //写入日志
        close(fd); //关闭文件描述符
    }

    void DiffileOutput(int level, const std::string &amp;logmessage)
    {
        std::string filename = Filename;
        filename += ".";
        filename += level2string(level); //根据日志等级调整文件名
        SamefileOutput(filename, logmessage); //复用SamefileOutput函数
    }

    ~Log()
    {}

private:
    int _method; // 输出方式
};
```

测试：

向显示器输出日志（n%5用于模拟不同日志等级）

向同一文件中输出日志

向不同文件中输出日志

完.
