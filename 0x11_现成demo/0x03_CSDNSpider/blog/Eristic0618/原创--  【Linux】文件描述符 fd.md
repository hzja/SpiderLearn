# 原创
：  【Linux】文件描述符 fd

# 【Linux】文件描述符 fd

**目录**

[一、C语言文件操作](#%E4%B8%80%E3%80%81C%E8%AF%AD%E8%A8%80%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C)

[1.1 fopen和fclose](#1.1%20fopen%E5%92%8Cfclose)

[1.2 fwrite和fread](#1.2%20fwrite%E5%92%8Cfread)

[1.3 C语言中的输入输出流](#1.3%20C%E8%AF%AD%E8%A8%80%E4%B8%AD%E7%9A%84%E8%BE%93%E5%85%A5%E8%BE%93%E5%87%BA%E6%B5%81)

[二、Linux的文件系统调用](#%E4%BA%8C%E3%80%81Linux%E7%9A%84%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F%E8%B0%83%E7%94%A8)

[2.1 open和文件描述符](#2.1%20open%E5%92%8C%E6%96%87%E4%BB%B6%E6%8F%8F%E8%BF%B0%E7%AC%A6)

[2.2 close](#2.2%20close)

[2.3 read](#2.3%20read)

[2.4 write](#2.4%20write)

[三、Linux内核数据结构与文件描述符](#%E4%B8%89%E3%80%81Linux%E5%86%85%E6%A0%B8%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E6%96%87%E4%BB%B6%E6%8F%8F%E8%BF%B0%E7%AC%A6)

---


## 一、C语言文件操作

在C语言中我们想要打开一个文件并对其进行读取写入等各种操作，需要依赖于fopen、fread、fwrite等函数。我们先来回顾一下这些函数

### 1.1 fopen和fclose

其中：

文件的打开模式中，r表示只读，w表示只写，a表示追加，还有很多模式相信对大家来说都不陌生

fopen如果打开文件成功，会返回一个FILE*指针，其中FILE结构体是C库自己封装的结构体，内部封装了文件的各种属性

一个文件被打开后，如果我们不需要使用该文件了，就需要使用fclose关闭它，向函数传入先前从fopen接收到的FILE*指针即可。

### 1.2 fwrite和fread

其中：

所以读取或写入的字节总数为size*nmemb

我们可以用fwrite对一个文件进行写入，例如：

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;

int main()
{
    FILE *fp = fopen("myfile", "w");
    if(!fp)
    {
        printf("fopen error!\n");
    }
    const char *str = "hello Linux\n";
    fwrite(str, strlen(str), 1, fp); 
    fclose(fp);
    return 0;                                                                                                                                                                                                 
}            
```

运行代码，可以看到已经写入成功了

我们还可以用fread读取一个文件的内容，例如：

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;string.h&gt;

int main()
{
    FILE *fp = fopen("myfile", "r");                                                                                                                                                                          
    if(!fp)
    {
        printf("fopen error!\n");
    }
    char buf[1024];
    ssize_t s = fread(buf, 1, sizeof(buf), fp);
    if(s)
    {
        buf[s] = '\0';
        printf("%s", buf);
    }
    fclose(fp);
    return 0;
}

```

fread如果读取成功，会返回读取的元素总数，与nmemb个数相同

运行代码，可以发现之前写入到myfile文件中的内容已经被读取出来了

除了以上的这些接口，C语言还有很多的文件操作接口，这里不是重点不作过多赘述

### 1.3 C语言中的输入输出流

在Linux中**一切皆文件**，显示器也是文件，我们也可以对其进行写入操作

如何对其进行写入呢？这里介绍C语言中的三个输入输出流

其中**stdin**是**标准输入流**，对应我们的**键盘**；**stdout**是**标准输出流**，**stderr**是**标准错误流**，这两个流对应我们的**显示器**。这三个输入输出流是C语言程序在启动时**默认会给我们打开的**

不止是C语言，其他语言也会默认打开这三个流，不过名称不同。C++中分别是cin、cout和cerr 

进程将从标准输入流中得到输入数据，将正常输出数据输出到标准输出流，而将错误信息送到标准错误流中

可以看到，这三个流的类型都是FILE*，也就是说我们自己也可以通过fread从标准输入流中读取键盘输入的内容，通过fwrite向标准输出流或标准错误流即显示器文件写入我们的内容。

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;string.h&gt;

int main()
{
    const char* str = "hello Linux\n";
    fwrite(str, 1, strlen(str), stdout);
    return 0;                                                                                                                                                                                                 
}

```

运行程序，可以看到我们已经把内容写入到显示器文件中了

---


## 二、Linux的文件系统调用

在前面了解操作系统的时候就提到，操作系统是有自己的系统调用接口的。

而语言中涉及到操作系统内核部分的函数，实际上都是**封装了操作系统的系统调用接口**，包括C语言的文件操作接口也是封装了操作系统的文件系统调用接口

所以我们先来了解一下Linux中的文件系统调用接口

### 2.1 open和文件描述符

open是Linux系统中用来打开文件的一个系统调用接口，其中：

flag参数是**文件访问权限标志位**，其中：

我们在使用open函数时必须包含以上三种中的一种标志位，除了这些还有其他的可选标志位，这里列出常用的三种：

标志位可以通过位运算的方式同时选中多种，例如：

像上面这样，就是以只写方式打开文件、以追加方式写入、如果文件不存在则创建

其中如果选中了O_CREAT，一般都要对mode参数进行设置，该参数用来设置新创建的文件权限

关于文件权限，我在前面的文章中有讲过

[【Linux】常用指令、热键与权限管理-CSDN博客<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://blog.csdn.net/Eristic0618/article/details/138795212?spm=1001.2014.3001.5501](https://blog.csdn.net/Eristic0618/article/details/138795212?spm=1001.2014.3001.5501)接下来我们看看open函数的返回值

可以看到，成功打开文件后open函数会返回一个**file descriptor**，即所谓的**文件描述符（fd）**

文件描述符是一个整型，从0开始向后分配，系统在给文件分配文件描述符时会分配当前没有被使用的最小的文件描述符 

关于文件描述符的本质，在后面会详细提到，目前只需要知道**进程是通过文件描述符来访问文件的**

### 2.2 close

close是Linux系统中关闭文件的系统调用接口，其参数就是一个文件描述符，传入文件对应的文件描述符即可关闭该文件

### 2.3 read

read函数将从fd对应的文件中读取count个字节到buf指向的内存块中

成功则返回读取到的字节数，失败则返回-1，若调用read时文件已达末尾则返回0

### 2.4 write

write函数将把buf指向的内存块中的内容写入count个字节到fd对应的文件中

成功则返回写入的字节数，失败则返回-1

---


## 三、Linux内核数据结构与文件描述符

到这里，相信大家已经学会如何使用Linux中的文件系统调用接口了，接下来我们深入探讨一下访问文件的本质

一个文件由**内容**和**属性**两部分构成，没打开的文件存储在磁盘中，本文重点不在于未打开的文件所以不作过多探讨。而我们如果要打开一个文件，就先得**将其加载到内存**中，这是由冯·诺依曼体系结构决定的。

所以在操作系统内部一定存在着大量的被打开的文件，操作系统也自然要对这些文件进行管理，即**先描述再组织**。操作系统内部使用**file结构体****（与C语言的FILE结构体不同）**来描述一个被打开文件的信息，其中包括该文件的基本属性、权限、大小、内核缓冲区信息等等，将这些结构体用数据结构组织起来，就可以完成对被打开文件的管理了。

而一个进程可以同时打开多个文件，所以进程和文件是一对多的关系。要把一个进程打开的所有文件管理起来，我们就要使用一个**files_struct结构体**。

我们知道操作系统通过PCB描述进程，而在进程的PCB中就有这么一个类型为 **struct files_struct*** 的指针files指向了进程的files_struct结构体，其定义如下

```
struct files_struct {
    atomic_t count;
    struct fdtable *fdt;
    struct fdtable  fdtab;
   
    int next_fd;
    struct embedded_fd_set close_on_exec_init;
    struct embedded_fd_set open_fds_init;
    struct file * fd_array[NR_OPEN_DEFAULT];
};

```

其中的fd_array数组，就指向了进程打开的一个个文件的file结构体。很多人称files_struct是文件描述符表，但我认为这个fd_array数组才是更准确的**文件描述符表**，因为所谓的文件描述符，其实就是文件在这个表中存储位置的**下标**！

前面提到，程序在启动时会默认打开三个标准输入输出流，所以文件描述符表中的前三个位置是默认被使用的。对应的，**标准输入流的文件描述符为0，标准输出流的文件描述符为1，标准错误流的文件描述符为2**

如何验证？在C语言中文件的属性被封装在FILE结构体中，结构体中的_fileno就是文件的文件描述符，我们只需要把三个标准流的文件描述符打印出来就能验证了

```
int main()
{
    printf("stdin:%d\n", stdin-&gt;_fileno);
    printf("stdout:%d\n", stdout-&gt;_fileno);
    printf("stderr:%d\n", stderr-&gt;_fileno);                                                                                                                                                                   
    return 0;
}

```

可以看到三个标准流对应的文件描述符就是0、1、2

如果此时我们在打印前close(1)，会发生什么呢？

```
int main()
{
    close(1);
    printf("stdin:%d\n", stdin-&gt;_fileno);
    printf("stdout:%d\n", stdout-&gt;_fileno);
    printf("stderr:%d\n", stderr-&gt;_fileno);                                                                                                                                                                   
    return 0;
}

```

什么也不会打印，因为标准输出流即显示器文件在打印前已经被关闭了

我们可以在程序中打开多个文件，看看它们的文件描述符是什么

```
int main()
{
    int fd1 = open("file1", O_WRONLY|O_TRUNC|O_CREAT, 0666);
    int fd2 = open("file2", O_WRONLY|O_TRUNC|O_CREAT, 0666);
    int fd3 = open("file3", O_WRONLY|O_TRUNC|O_CREAT, 0666);
    int fd4 = open("file4", O_WRONLY|O_TRUNC|O_CREAT, 0666);
    printf("fd1:%d\n", fd1);
    printf("fd2:%d\n", fd2);
    printf("fd3:%d\n", fd3);
    printf("fd4:%d\n", fd4);                                                                                                                                                                                  
    return 0;
}
```

可以看到，系统会给文件分配当前未被使用的最小的文件描述符

一个文件可以被多个进程打开，那么是不是一个进程将该文件关闭了，该文件对应的资源就要被系统回收呢？

不是的，在file结构体中有该文件的**引用计数**，用来计算该文件被多少个进程打开了。如果一个进程将该文件对应的fd关闭则减少对应的引用计数，只有当引用计数为0时文件才会被真正的关闭

完.
