# 原创
：  【Linux】输入输出重定向

# 【Linux】输入输出重定向

**目录**

[一、概念](#%E4%B8%80%E3%80%81%E6%A6%82%E5%BF%B5)

[二、重定向的本质](#%E4%BA%8C%E3%80%81%E9%87%8D%E5%AE%9A%E5%90%91%E7%9A%84%E6%9C%AC%E8%B4%A8)

[三、系统调用接口dup和dup2](#%E4%B8%89%E3%80%81%E7%B3%BB%E7%BB%9F%E8%B0%83%E7%94%A8%E6%8E%A5%E5%8F%A3dup%E5%92%8Cdup2)

[3.1 dup ](#3.1%20dup%C2%A0)

[3.2 dup2](#3.2%20dup2)

---


## 一、概念

在之前对Linux的学习中，我们有接触过一系列的重定向命令，例如 &gt;、&gt;&gt;等

它们可以将一个命令的输出或输入重定向到其他地方，如**echo**命令用来将我们指定的文本打印到终端中，通过输出重定向就可以把原来要打印到终端的文本输出到其他的地方

例如我们可以通过重定向把echo要打印的内容重定向到某个文件中

像这样，**通过控制数据的流向，让数据的目的地发生改变，即为****重定向**

---


## 二、重定向的本质

在学习重定向之前，我们需要先知道什么是文件描述符

[【Linux】文件描述符 fd-CSDN博客<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://blog.csdn.net/Eristic0618/article/details/140838982?spm=1001.2014.3001.5501](https://blog.csdn.net/Eristic0618/article/details/140838982?spm=1001.2014.3001.5501)在前面的学习中，我们已经知道进程是通过**文件描述符**来访问文件的，而进程在打开一个文件时操作系统会给该文件分配一个**当前最小的未使用的**文件描述符。

所以假设我们把标准输出流关闭，那么1号文件描述符此时就是未被使用的状态

如果此时我们再打开一个文件，按理来说这个文件的文件描述符会分配为1

那么我们再向原来的标准输出流打印某些内容，这些内容会跑到哪里呢？

```
#include &lt;stdio.h&gt;
#include &lt;errno.h&gt;
#include &lt;unistd.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;fcntl.h&gt;

int main()
{
    close(1); //关闭标准输出
    int fd = open("file.txt", O_CREAT | O_WRONLY | O_TRUNC, 0666); //打开文件
    if(fd &lt; 0)
    {
        perror("open");
        return 1;
    }
    const char *msg = "hello Linux\n";
    int cnt = 5;
    while(cnt--) //循环5次
    {
        write(1, msg, strlen(msg)); //向原来的标准输出流打印
    }
    close(fd);
    return 0;
}
```

原本当我们向write函数传入1号文件描述符进行写入时会向显示器文件中写入。但现在当我们向1号文件描述符中打印的时候，显示器上什么也没有，而我们写入的内容已经写到了file.txt中。此时，我们就完成了对这些内容的重定向了

所以可以知道：重定向实际上就是**改变某个文件描述符指向的文件**

原本1号文件描述符对应标准输出流，但我们通过关闭标准输出流再创建新文件的方式让1号描述符重新分配给了我们的file.txt，所以向显示器打印的内容就重定向到了我们的file.txt中 

不过这种说法还不够准确，从内核的角度，应该说重定向就是修改文件描述符下标对应的**file*指针**

---


## 三、系统调用接口dup和dup2

dup和dup2都是Linux中用于实现重定向的系统调用接口，使用起来也并没有难度，不过二者之间有一些区别需要注意

### 3.1 dup 

向dup中传入一个文件描述符，会给我们返回一个新的文件描述符，传入的文件描述符和新的文件描述符指向的是同一个文件

例如：

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;fcntl.h&gt;

int main()
{
    int newfd = dup(1);
    const char *msg = "hello Linux\n";
    write(newfd, msg, strlen(msg));
    printf("newfd: %d\n", newfd);
    return 0;
}

```

可以看到，我们向newfd中写入的内容被打印到了终端，说明newfd已经重定向到了标准输出中

### 3.2 dup2

dup2比dup多了一个参数，其中dup2会将newfd重定向到oldfd指向的文件，也就是将oldfd对应的file*指针拷贝到newfd对应的下标位置

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;fcntl.h&gt;

int main()
{
    int fd = open("file.txt", O_CREAT | O_WRONLY | O_TRUNC, 0666);
    dup2(fd, 1);
    const char *msg = "hello Linux\n";
    write(1, msg, strlen(msg));
    close(fd);
}
```

可以看到，因为1号文件描述符被重定向到了fd指向的文件，所以我们原本向标准输出中打印的内容并没有在终端中显示，而是被重定向到了file.txt中

除了对输出流进行重定向，我们也可以对输入流进行重定向，例如我们先向file.txt中写一些内容

然后用dup2将标准输入流重定向到文件对应的文件描述符

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;fcntl.h&gt;

int main()
{
    int fd = open("file.txt", O_RDONLY);
    dup2(fd, 0);
    char buffer[1024];
    ssize_t s = read(0, buffer, sizeof(buffer) - 1);
    if(s &gt; 0)
    {
        buffer[s] = '\0';
        printf("%s", buffer);
    }
    close(fd);
}
```

执行程序，此时虽然从0号文件描述符中读取数据，但因为已经被重定向到了fd指向的文件中，所以read会从文件中读取数据，最后将读取的内容打印出来

如有错误欢迎在评论区指出

完.
