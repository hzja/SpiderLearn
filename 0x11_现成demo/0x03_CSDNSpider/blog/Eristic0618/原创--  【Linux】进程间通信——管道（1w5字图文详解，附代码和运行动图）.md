# 原创
：  【Linux】进程间通信——管道（1w5字图文详解，附代码和运行动图）

# 【Linux】进程间通信——管道（1w5字图文详解，附代码和运行动图）

**目录**

[一、进程间通信](#%E4%B8%80%E3%80%81%E8%BF%9B%E7%A8%8B%E9%97%B4%E9%80%9A%E4%BF%A1)

[1.1 概念](#1.1%20%E6%A6%82%E5%BF%B5)

[1.2 手段](#1.2%20%E6%89%8B%E6%AE%B5)

[二、管道](#%E4%BA%8C%E3%80%81%E7%AE%A1%E9%81%93)

[2.1 概念](#2.1%20%E6%A6%82%E5%BF%B5)

[2.2 匿名管道](#2.2%20%E5%8C%BF%E5%90%8D%E7%AE%A1%E9%81%93)

[2.3 管道的特征](#2.3%20%E7%AE%A1%E9%81%93%E7%9A%84%E7%89%B9%E5%BE%81)

[2.4 管道的读写规则](#2.4%20%E7%AE%A1%E9%81%93%E7%9A%84%E8%AF%BB%E5%86%99%E8%A7%84%E5%88%99)

[2.5 管道的应用场景](#2.5%20%E7%AE%A1%E9%81%93%E7%9A%84%E5%BA%94%E7%94%A8%E5%9C%BA%E6%99%AF)

[三、命名管道](#%E4%B8%89%E3%80%81%E5%91%BD%E5%90%8D%E7%AE%A1%E9%81%93)

[3.1 创建命名管道](#3.1%20%E5%88%9B%E5%BB%BA%E5%91%BD%E5%90%8D%E7%AE%A1%E9%81%93)

[3.2 使用命名管道](#3.2%20%E4%BD%BF%E7%94%A8%E5%91%BD%E5%90%8D%E7%AE%A1%E9%81%93)

[3.3 命名管道的读写规则](#3.3%20%E5%91%BD%E5%90%8D%E7%AE%A1%E9%81%93%E7%9A%84%E8%AF%BB%E5%86%99%E8%A7%84%E5%88%99)

---


## 一、进程间通信

### 1.1 概念

**进程间通信****（Inter-Process Communication，IPC）**是指在不同的进程之间共享信息或数据，实现数据层面的交互。

我们知道，**进程具有独立性**，默认情况下两个进程是无法进行信息交流的，因此我们需要某些技术手段来让不同进程之间能够共享信息

进程间通信的本质，就是让两个进程能够看到同一份“资源”，这份资源一般由操作系统提供，因此进程访问这份资源进行通信，本质上就是在访问操作系统，所以要实现进程间通信，我们需要调用对应的系统调用接口。

操作系统中的两大IPC模块定制标准：System V和Posix，为我们提供了一系列进程间通信方法

### 1.2 手段

常见的进程间通信手段主要有：

---


## 二、管道

### 2.1 概念

管道是Linux中的一种进程间通信方式

我们可以把管道想象成连接两个进程间的一条管子，一个进程的数据流就能通过这个管子流向另一个进程。

管道分为**匿名管道pipe**和**命名管道FIFO**两种，通常我们所说的管道指匿名管道，二者除了创建、使用等方式不同，原理是相同的，都是通过内核的一块缓冲区实现数据传输

### 2.2 匿名管道

匿名管道（pipe）是一个临时创建的对象

站在**文件描述符**角度来看，我们可以把两个进程的文件描述符分别指向管道的读端和写端，一个进程向管道中写，另一个进程从管道中读，就实现了进程间通信。

站在**内核**角度来看，管道的本质就是两个file结构体（一个用于写一个用于读）、一个临时创建的inode节点加上一个内存的物理页。进程向管道中写入时，数据被写入到了这个共享数据页中；进程从管道中读取时，数据又从这个页中被拷贝出来

理解了管道的本质，我们就理解了为什么管道只能进行单向通信

创建匿名管道的接口：

```
#include &lt;unistd.h&gt;
int pipe(int fd[2]);
```

该函数的参数是一个输出型参数，我们需要向函数内传入一个大小为2，元素类型为int的数组。匿名管道创建完毕后，传入的数组内部会存放读端和写端的文件描述符，其中fd[0]为读端，fd[1]为写端

创建匿名管道成功，函数会返回0，创建失败返回-1并设置errno

我们可以用一段简单的代码来验证一下：

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;

using namespace std;

int main()
{
    int fd[2] = {0};
    int n = pipe(fd);
    if(n &lt; 0)
        return 1;
    cout &lt;&lt; "fd[0]=" &lt;&lt; fd[0] &lt;&lt; " fd[1]=" &lt;&lt; fd[1] &lt;&lt; endl;
    return 0;
}
```

运行结果：

我们知道，进程的前三个文件描述符分别被标准输入流、标准输出流和标准错误流占用，所以创建匿名管道时文件描述符只能从3开始，符合预期

但匿名管道又是如何实现**父子进程间通信**的呢？

通过fork创建子进程后，子进程会继承父进程的各种信息，其中就包括文件描述符表，因此父进程如果在创建子进程时就已经创建了匿名管道，后续子进程的文件描述符也会与该管道对应

 

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;

using namespace std;

int main()
{
    int fd[2] = {0};
    int n = pipe(fd); //父进程建立匿名管道
    if(n &lt; 0)
        return 1;
    pid_t id = fork(); //创建子进程
    if(id &lt; 0)
        return 2;
    return 0;
}
```

父进程向子进程通信的情况，再将父进程指向**管道读端**的文件描述符关闭，子进程指向**管道写端**的文件描述符关闭。如果要实现子进程向父进程通信，则反过来即可

```
#include &lt;iostream&gt;
#include &lt;cstdlib&gt;
#include &lt;unistd.h&gt;

using namespace std;

int main()
{
    int fd[2] = {0};
    int n = pipe(fd); //父进程建立匿名管道
    if(n &lt; 0)
        return 1;
    pid_t id = fork(); //创建子进程
    if(id &lt; 0)
        return 2;
    if(id == 0) //子进程
    {
        close(fd[1]); //关闭写端
        //开始通信
        //...
        close(fd[0]); //通信完毕
        exit(0);
    }
    //父进程
    close(fd[0]); //关闭读端
    //开始通信
    //...
    close(fd[1]); //通信完毕
    return 0;
}
```

所以，通过匿名管道实现进程间通信的前提，是两个进程间**有血缘关系**（文件描述符可被继承）

匿名管道不需要将数据拷贝到磁盘中，属于内存级文件，没有路径、文件名和inode，因此而得名

以上就是使用匿名管道实现进程间通信的前置操作——建立通信信道，接下来我们才开始真正的进程间通信

文件描述符也有了，我们只需要让父子进程一个向管道写入内容，一个从管道读取内容，就可以完成通信了。这里用一段简单的代码来验证：

```
#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;cstring&gt;
#include &lt;cstdio&gt;
#include &lt;cstdlib&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/wait.h&gt;
#include &lt;sys/types.h&gt;

using namespace std;

void Writer(int wfd)
{
    //随便准备一些用于通信的内容
    string s = "hello, I am father";
    pid_t self = getpid();

    char buffer[1024];
    while(true)
    {
        buffer[0] = 0; //清空字符串
        snprintf(buffer, sizeof(buffer), "%s, pid:%d", s.c_str(), self); //将内容格式化输入到目标字符串中
        write(wfd, buffer, strlen(buffer)); //将字符串写入管道
        sleep(1);
    }
}

void Reader(int rfd)
{
    char buffer[1024];
    while(true)
    {
        buffer[0] = 0;
        ssize_t n = read(rfd, buffer, sizeof(buffer)); //从管道读取内容
        if(n &gt; 0)
        {
            buffer[n] = 0; //这里的0相当于'\0'
            cout &lt;&lt; "child get a massage[" &lt;&lt; getpid() &lt;&lt; "]#" &lt;&lt; buffer &lt;&lt; endl; //打印读取到的内容
        }
    }
}

int main()
{
    int fd[2] = {0};
    int n = pipe(fd); //父进程建立匿名管道
    if(n &lt; 0)
        return 1;
    pid_t id = fork(); //创建子进程
    if(id &lt; 0)
        return 2;
    if(id == 0) //子进程
    {
        close(fd[1]); //关闭写端
        //向管道读取
        Reader(fd[0]);
        close(fd[0]); // 通信完毕
        exit(0);
    }
    //父进程
    close(fd[0]); //关闭读端
    //向管道写入
    Writer(fd[1]);
    //等待子进程
    pid_t rid = waitpid(id, nullptr, 0);
    if(rid &lt; 0)
        return -1;
    close(fd[1]); // 通信完毕
    return 0;
}
```

运行结果：

可以看到，子进程确实完整的接收到了父进程发送的内容

但是，我把字符串定义为全局的，子进程不是也能访问到吗？实际上进程间通信的内容并不只是传输静态的数据，一些动态变化的数据只能依靠进程间通信来传输

### 2.3 管道的特征

**（1）大小固定**

前面提到，匿名管道是通过数据页完成数据的交互的，所以管道是有其固定的大小的

我们可以通过**** ulimit -a ****命令来查看系统资源的设置

其中：

可以看到，管道的大小为512字节*8=4KB，和页的大小一致

但是实际上管道是否真的是4KB呢？我们可以让写端不停的写，一次只写一个字符，并计算写端写入了多少次，而读端10秒后才开始读取，看看结果如何：

```
#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;cstring&gt;
#include &lt;cstdio&gt;
#include &lt;cstdlib&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/wait.h&gt;
#include &lt;sys/types.h&gt;

using namespace std;

void Writer(int wfd)
{
    int number = 1; 
    while(true)
    {
        char c = 'a'; 
        write(wfd, &amp;c, 1); //一次只写一个字符
        cout &lt;&lt; number++ &lt;&lt; endl; //用于说明写端写了几次
    }
}

void Reader(int rfd)
{
    char buffer[1024]; 
    while(true)
    {
        sleep(10); //10秒后才开始读取
        buffer[0] = 0;
        ssize_t n = read(rfd, buffer, sizeof(buffer)); //从管道读取内容
        if(n &gt; 0)
        {
            buffer[n] = 0; //这里的0相当于'\0'
            cout &lt;&lt; "child get a massage[" &lt;&lt; getpid() &lt;&lt; "]#" &lt;&lt; buffer &lt;&lt; endl; //打印读取到的内容
        }
    }
}

int main()
{
    int fd[2] = {0};
    int n = pipe(fd); //父进程建立匿名管道
    if(n &lt; 0)
        return 1;
    pid_t id = fork(); //创建子进程
    if(id &lt; 0)
        return 2;
    if(id == 0) //子进程
    {
        close(fd[1]); //关闭写端
        //向管道读取
        Reader(fd[0]);
        close(fd[0]); // 通信完毕
        exit(0);
    }
    //父进程
    close(fd[0]); //关闭读端
    //向管道写入
    Writer(fd[1]);
    //等待子进程
    pid_t rid = waitpid(id, nullptr, 0);
    if(rid &lt; 0)
        return -1;
    close(fd[1]); // 通信完毕
    return 0;
}
```

运行结果：

 <img alt="" height="215" src="https://i-blog.csdnimg.cn/direct/0fa88ccb610d4a3e9b5cdf13622f9b25.png" width="343"/>

可以看到写端写入了65536次，也就是最多写入了65536个字符即65536字节，换算为64KB，这和我们说好的可不一样啊！

实际上管道在不同的内核里，大小可能是不同的。在Linux 2.6.11之前管道大小和页大小一样（4KB），后面变为64KB

**（2）血缘限制**

创建匿名管道后，管道的读写端与进程的文件描述符关联，要想让另一个进程也拿到与管道关联的文件描述符，就需要通过血缘关系继承的方式

**（3）单向通信**

管道的结构注定其只能进行**单向通信**，如果要实现双向通信则需要两个管道

**（4）同步与互斥**

通信的进程间会保持进程协同，当读写的内容大小小于4KB时可保证读写的**原子性**，这一点在后面管道的读写规则部分会讲到

**（5）面向字节流**

管道是面向字节流的，这一点在后面管道的读写规则部分会讲到

**（6）基于文件**

管道是基于文件的，而文件的生命周期是随进程的，所以其实在代码最后也不一定要把读写端关闭，进程退出后，操作系统会自动回收

### 2.4 管道的读写规则

**（1）未设置O_NONBLOCK**，**读写端正常，管道如果为空，读端就要阻塞**

例如上面的代码，我们让父进程向管道写入时，限定一秒写一次，而子进程读取数据也是一秒读一次，说明当管道为空时，读端没有内容可以读取，于是阻塞

**（2）未设置O_NONBLOCK**，**读写端正常，管道如果为满，写端就要阻塞**

我们可以修改一下上面的代码，让写端不停写，而读端隔一会才读一次，看看效果如何

```
#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;cstring&gt;
#include &lt;cstdio&gt;
#include &lt;cstdlib&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/wait.h&gt;
#include &lt;sys/types.h&gt;

using namespace std;

void Writer(int wfd)
{
    //随便准备一些用于通信的内容
    string s = "hello, I am father";
    pid_t self = getpid();
    int number = 0; 

    char buffer[1024];
    while(true)
    {
        buffer[0] = 0; //清空字符串
        snprintf(buffer, sizeof(buffer), "%s, pid:%d", s.c_str(), self); //将内容格式化输入到目标字符串中
        write(wfd, buffer, strlen(buffer)); //将字符串写入管道
        cout &lt;&lt; number++ &lt;&lt; endl; //用于说明写端写了几次
    }
}

void Reader(int rfd)
{
    char buffer[1024];
    while(true)
    {
        sleep(5); //隔5秒读一次
        buffer[0] = 0;
        ssize_t n = read(rfd, buffer, sizeof(buffer)); //从管道读取内容
        if(n &gt; 0)
        {
            buffer[n] = 0; //这里的0相当于'\0'
            cout &lt;&lt; "child get a massage[" &lt;&lt; getpid() &lt;&lt; "]#" &lt;&lt; buffer &lt;&lt; endl; //打印读取到的内容
        }
    }
}

int main()
{
    int fd[2] = {0};
    int n = pipe(fd); //父进程建立匿名管道
    if(n &lt; 0)
        return 1;
    pid_t id = fork(); //创建子进程
    if(id &lt; 0)
        return 2;
    if(id == 0) //子进程
    {
        close(fd[1]); //关闭写端
        //向管道读取
        Reader(fd[0]);
        close(fd[0]); // 通信完毕
        exit(0);
    }
    //父进程
    close(fd[0]); //关闭读端
    //向管道写入
    Writer(fd[1]);
    //等待子进程
    pid_t rid = waitpid(id, nullptr, 0);
    if(rid &lt; 0)
        return -1;
    close(fd[1]); // 通信完毕
    return 0;
}
```

运行效果：

可以看到，父进程一下就写了两千多次，把管道写满了，而子进程5秒才读一次，所以父进程无法继续写入，于是阻塞

我们发现子进程第一次读取时，由于其缓冲区大小限制，并没有完整的把管道中的所有数据读完，但读取后管道中空出来了部分空间，而父进程并没有继续进行写入。这是因为管道的读写具有**原子性**（前提是写入的内容小于管道大小），其内部的数据必须被读端完整读取完毕后才会继续进行写入，可以保证数据安全

如果写入的内容大于管道大小，那么当管道被写满就无法再写入了，只能一次写一部分，也就无法保证原子性了

但是，明明我们父进程是一行行写的，怎么子进程读取的时候一次读取了一大块呢？

因为管道是**面向字节流**的，它不会区分读取的内容是字符串还是什么，只负责读取内容，至于后续对内容的处理是用户需要考虑的事情

我们可以对写端写入的内容作一个规定，让其按照某种格式或方式写入，读端在读取内容后就可以按照规定的方式来处理这些内容，于是诞生了**协议**。关于协议在网络部分会提到

**（3）设置了O_NONBLOCK， 读写端正常，管道如果为空，读端返回-1，并设置errno值为EAGAIN**

**（4）设置了O_NONBLOCK， 读写端正常，管道如果为满，写端返回-1，并设置errno值为EAGAIN**

**（5）读端正常，写端被关闭，读端不会被阻塞，且读取的返回值始终为0，表示读取到文件结尾**

要验证这一点，我们就得修改一下之前的代码，让子进程写入，父进程读取

```
#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;cstring&gt;
#include &lt;cstdio&gt;
#include &lt;cstdlib&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/wait.h&gt;
#include &lt;sys/types.h&gt;

using namespace std;

void Writer(int wfd)
{
    string s = "hello, I am child";

    char buffer[1024];
    int cnt = 3;
    while (cnt--) //只写入三次
    {
        buffer[0] = 0; //清空字符串
        snprintf(buffer, sizeof(buffer), "%s", s.c_str()); //将内容格式化输入到目标字符串中
        write(wfd, buffer, strlen(buffer)); //将字符串写入管道
        cout &lt;&lt; "child write: " &lt;&lt; s &lt;&lt; endl;
        sleep(1);
    }
}

void Reader(int rfd)
{
    char buffer[1024]; 
    while(true)
    {
        buffer[0] = 0;
        ssize_t n = read(rfd, buffer, sizeof(buffer)); //从管道读取内容
        if(n &gt; 0)
        {
            buffer[n] = 0; //这里的0相当于'\0'
            cout &lt;&lt; "father read: " &lt;&lt; buffer &lt;&lt; endl; //打印读取到的内容
        }
        cout &lt;&lt; "n=" &lt;&lt; n &lt;&lt; endl; //打印read返回值
    }
}

int main()
{
    int fd[2] = {0};
    int n = pipe(fd); //父进程建立匿名管道
    if(n &lt; 0)
        return 1;
    pid_t id = fork(); //创建子进程
    if(id &lt; 0)
        return 2;
    if(id == 0) //子进程
    {
        close(fd[0]); //关闭读端
        //向管道写入
        Writer(fd[1]);
        close(fd[1]); // 通信完毕
        exit(0);
    }
    //父进程
    close(fd[1]); //关闭写端
    //向管道读取
    Reader(fd[0]);
    //等待子进程
    pid_t rid = waitpid(id, nullptr, 0);
    if(rid &lt; 0)
        return -1;
    close(fd[0]); // 通信完毕
    return 0;
}
```

运行效果：

可以看到，子进程每秒写入一个字符串，父进程读取一个字符串，n为读取到的字节数

而子进程写入3次后就退出，写端被关闭，读端虽然不停的读，但是也没有内容可读了，所以n为0

**（6）写端正常，读端被关闭，操作系统会通过发送信号杀掉正在写入的进程**

操作系统是不会做任何低效浪费的工作的，当管道的读端被关闭，继续写入也就没有任何意义了，所以操作系统会直接杀掉正在写入的进程 

我们可以让父进程读取几次后就将读端关闭，然后通过进程等待来获取子进程的退出信息，查看子进程是否真的收到了信号

```
#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;cstring&gt;
#include &lt;cstdio&gt;
#include &lt;cstdlib&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/wait.h&gt;
#include &lt;sys/types.h&gt;

using namespace std;

void Writer(int wfd)
{
    string s = "hello, I am child";

    char buffer[1024];
    while (true)
    {
        buffer[0] = 0; //清空字符串
        snprintf(buffer, sizeof(buffer), "%s", s.c_str()); //将内容格式化输入到目标字符串中
        write(wfd, buffer, strlen(buffer)); //将字符串写入管道
        cout &lt;&lt; "child write: " &lt;&lt; s &lt;&lt; endl;
        sleep(1);
    }
}

void Reader(int rfd)
{
    char buffer[1024];
    int cnt = 3;
    while(cnt--) //读3次就退出
    {
        buffer[0] = 0;
        ssize_t n = read(rfd, buffer, sizeof(buffer)); //从管道读取内容
        if(n &gt; 0)
        {
            buffer[n] = 0; //这里的0相当于'\0'
            cout &lt;&lt; "father read: " &lt;&lt; buffer &lt;&lt; endl; //打印读取到的内容
        }
        cout &lt;&lt; "n=" &lt;&lt; n &lt;&lt; endl; //打印read返回值
    }
}

int main()
{
    int fd[2] = {0};
    int n = pipe(fd); //父进程建立匿名管道
    if(n &lt; 0)
        return 1;
    pid_t id = fork(); //创建子进程
    if(id &lt; 0)
        return 2;
    if(id == 0) //子进程
    {
        close(fd[0]); //关闭读端
        //向管道写入
        Writer(fd[1]);
        close(fd[1]); // 关闭写端
        exit(0);
    }
    //父进程
    close(fd[1]); //关闭写端
    //向管道读取
    Reader(fd[0]);
    cout &lt;&lt; "read over, close read fd" &lt;&lt; endl;
    close(fd[0]); // 关闭读端
    // 等待子进程
    int status = 0; //获取子进程退出信息
    pid_t rid = waitpid(id, &amp;status, 0); 
    if(rid &lt; 0)
        return -1;
    cout &lt;&lt; "child process exit signal: " &lt;&lt; (status &amp; 0x7F) &lt;&lt; endl; //打印子进程退出信号
    return 0;
}
```

运行结果：

可以看到子进程确实收到了13号信号 

我们可以输入**** kill -l ****命令，查看是哪个信号

### 2.5 管道的应用场景

我们在shell中输入指令时，使用的管道 “|” ，其底层就是匿名管道

我们还可以用管道来实现一个简易的进程池，通过管道实现父进程向子进程派发任务

既然是派发任务，那么我们需要设计一些自定义的任务内容

```
//Task.hpp
#pragma once

#include &lt;iostream&gt;
#include &lt;vector&gt;

typedef void(*task_t)();

void task1()
{
    std::cout &lt;&lt; "task1" &lt;&lt; std::endl;
}

void task2()
{
    std::cout &lt;&lt; "task2" &lt;&lt; std::endl;
}

void task3()
{
    std::cout &lt;&lt; "task3" &lt;&lt; std::endl;
}

void task4()
{
    std::cout &lt;&lt; "task4" &lt;&lt; std::endl;
}

void LoadTask(std::vector&lt;task_t&gt; *tasks) //将任务加载到任务队列
{
    tasks-&gt;push_back(task1);
    tasks-&gt;push_back(task2);
    tasks-&gt;push_back(task3);
    tasks-&gt;push_back(task4);
}

```

接下来就是进程池的设计了，我们依旧是通过父进程创建匿名管道，然后创建子进程继承文件描述符，然后关闭对应的文件描述符来建立通信信道

具体代码如下：

```
#include &lt;iostream&gt;
#include &lt;cstdlib&gt;
#include &lt;unistd.h&gt;
#include &lt;string&gt;
#include &lt;vector&gt;
#include &lt;cassert&gt;
#include &lt;ctime&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/wait.h&gt;
#include &lt;sys/stat.h&gt;
#include "Task.hpp"

#define processnum 5       // 子进程数量
std::vector&lt;task_t&gt; tasks; // 任务队列

class channel // 描述信道信息
{
public:
    channel(int cmdfd, int slaverid, const std::string &amp;processname)
        : _cmdfd(cmdfd), _slaverid(slaverid), _processname(processname)
    {
    }

public:
    int _cmdfd;               // 子进程对应的父进程写端fd
    int _slaverid;            // 子进程pid
    std::string _processname; // 子进程名称
};

void worker() // 子进程工作内容
{
    while (true)
    {
        int cmdcode = 0;
        int n = read(0, &amp;cmdcode, sizeof(int)); // 从管道读入工作码
        if (n == sizeof(int))
        {
            std::cout &lt;&lt; "child-" &lt;&lt; getpid() &lt;&lt; " : get cmdcode: " &lt;&lt; cmdcode &lt;&lt; std::endl; // test
            if (cmdcode &gt;= 0 &amp;&amp; cmdcode &lt; tasks.size())
                tasks[cmdcode](); // 执行任务
        }
        if (n == 0) // 一旦写端关闭，n为0
            break; // n == 0时直接退出
    }
}

void InitProcessPool(std::vector&lt;channel&gt; *channels)
{
    for (int i = 0; i &lt; processnum; i++)
    {
        int pipefd[2];
        int n = pipe(pipefd); // 建立管道
        assert(!n);

        pid_t id = fork(); // 创建子进程
        if (id == 0)       // 子进程
        {
            close(pipefd[1]);   // 关闭写端
            dup2(pipefd[0], 0); // 将管道重定向到标准输入，子进程可以直接从0号文件描述符读取内容
            close(pipefd[0]);
            worker(); // 开始工作

            std::cout &lt;&lt; "子进程:" &lt;&lt; getpid() &lt;&lt; "退出" &lt;&lt; std::endl;
            exit(0);
        }
        // 父进程
        close(pipefd[0]); // 关闭读端
        std::string name = "process-" + std::to_string(i);
        channels-&gt;push_back(channel(pipefd[1], id, name)); // 初始化信道
    }
}

void Debug(const std::vector&lt;channel&gt; &amp;channels) // 测试代码
{
    for (const auto &amp;it : channels) // 测试进程池是否正确初始化
    {
        std::cout &lt;&lt; it._cmdfd &lt;&lt; " " &lt;&lt; it._slaverid &lt;&lt; " " &lt;&lt; it._processname &lt;&lt; std::endl;
    }
}

void CtrlWorker(std::vector&lt;channel&gt; &amp;channels)
{
    int which = 0;
    int cnt = 5;
    while (cnt--) //派发5次就结束
    {
        int cmdcode = rand() % tasks.size(); // 任务码（模拟随机任务）
        //除了随机方式，还可以设计界面并让用户自行选择任务

        std::cout &lt;&lt; "father: " &lt;&lt; "cmdcode-" &lt;&lt; cmdcode &lt;&lt; " has send to "
                  &lt;&lt; channels[which]._processname &lt;&lt; std::endl; // test

        write(channels[which]._cmdfd, &amp;cmdcode, sizeof(cmdcode)); // 向管道写入任务码

        which++; // 顺序选择进程
        which %= channels.size();

        sleep(1);
    }
}

void QuitProcess(const std::vector&lt;channel&gt; &amp;channels)
{
    for (const auto &amp;c : channels)
        close(c._cmdfd); // 关闭对应父进程写端
    for (const auto &amp;c : channels)
        waitpid(c._slaverid, nullptr, 0); // 回收子进程
}

int main()
{
    LoadTask(&amp;tasks); // 初始化任务队列

    srand(time(0));

    std::vector&lt;channel&gt; channels; // 信道列表
    InitProcessPool(&amp;channels);    // 初始化进程池
    // Debug(channels);

    CtrlWorker(channels); // 派发任务并选择进程

    QuitProcess(channels); // 退出子进程
    return 0;
}
```

其中有些思路或许需要说明一下

代码运行结果：

可以看到，父进程传输给子进程的任务码都能够被正确接收，且对应的任务也被执行 

当然，代码中还存在一个小bug，虽然不影响程序的运行

我们会发现，最后子进程退出的时候，是所有子进程一起退出的。但我们最后关闭父进程写端的时候，可是用循环一个个关闭的，难道子进程不应该也是一个个退出的吗？

实际上有一个非常容易被忽略的点，就是父进程在创建完第一个子进程后，其写端fd指向了第一个管道。**而这个写端fd也是会被后面创建的子进程继承的！**

也就是说，后面每一个子进程，都会指向前面所有管道的写端

这就导致后续我们通过关闭写端让子进程退出的时候，前面的n-1次关闭都是无效的，因为始终会有其他的子进程指向管道写端，既然还有进程指向写端，那么对应的读端就不会读到0，而是**保持阻塞**

直到关闭了最后一个管道的写端，由于后续没有子进程指向，只有父进程唯一一个写端，此时关闭才是有效的。

最后一个管道的写端被关闭，导致最后被创建出来的子进程退出，释放所有的文件描述符。这些文件描述符中就有部分指向了前面管道的写端，这样就又导致第n-1个子进程退出...就像**多米诺骨牌**一样，最后一个倒下了，前面的都会一个个倒下

因此我们也可以从后往前关闭写端，这样就能实现子进程一个个退出的效果了

当然，我们也可以用一个数组保存历史上创建的写端fd，每次创建一个新的子进程就遍历一遍数组，把每个继承的写端fd都关闭即可

---


## 三、命名管道

匿名管道限制了只能在具有亲缘关系的进程进行通信时使用，如果我们想让两个没有关联的进程进行通信，则需要使用另一种管道——**命名管道**

命名管道也称为FIFO文件，相较于匿名管道存在于系统内核中，命名管道作为一种特殊的文件存放在文件系统中

### 3.1 创建命名管道

我们可以通过**mkfifo**命令创建命名管道，例如：

也可以通过函数创建命名管道

```
#include &lt;sys/types.h&gt;
#include &lt;sys/stat.h&gt;

int mkfifo(const char* pathname, mode_t mode);
```

其中：

创建命名管道成功，函数返回0，失败则返回-1

既然能用函数创建命名管道，那么也能用函数删除命名管道

```
#include &lt;unistd.h&gt;

int unlink(const char* path);
```

删除成功返回0，失败返回-1 

### 3.2 使用命名管道

既然命名管道也是文件，数据先写入文件再被其他进程读取，为什么我们不使用普通文件进行进程间通信呢？

虽然命名管道存放在文件系统中，但是它并**不会将数据刷新到磁盘**上，是一个内存级文件。如果使用普通文件，还多了一个刷盘的操作，因此我们不使用普通文件。

命名管道有独立的inode、路径和文件名，通过这些我们就能保证两个不同的进程能够打开同一个命名管道

具体如何使用命名管道：我们只需要像使用普通文件一样使用命名管道即可

既然命名管道可用于两个不相关的进程，那么我们就写两份简单的代码，来模拟客户端与服务端之间最基础的通信场景

因为两份代码间可能有较多的重复代码，例如头文件等内容，所以我们可以把这部分的重复代码拆分出来，减少代码的重复性

首先是 shared.hpp，内容主要是两份代码重复的部分：

```
//shared.hpp
#pragma once

#include &lt;iostream&gt;
#include &lt;cerrno&gt;
#include &lt;cstring&gt;
#include &lt;cstdlib&gt;
#include &lt;cstdio&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;fcntl.h&gt;

#define FIFO_FILE "./myfifo" //命名管道路径
#define MODE 0664 //命名管道权限位

enum //退出码，代表不同错误
{
    FIFO_CREATE_ERR = 1,
    FIFO_DELETE_ERR,
    FIFO_OPEN_ERR
};
```

然后是 server.cc，代表服务端

```
//server.cc
//服务端
#include "shared.hpp"
using namespace std;

int main()
{
    int n = mkfifo(FIFO_FILE, MODE); //创建命名管道
    if(n == -1) //创建失败
    {
        perror("mkfifo");
        exit(FIFO_CREATE_ERR);
    }

    int fd = open(FIFO_FILE, O_RDONLY); //读方式打开命名管道
    if(fd &lt; 0) //打开管道失败
    {
        perror("open");
        exit(FIFO_OPEN_ERR);
    }

    while(true) //开始通信
    {
        char buffer[1024] = {0};
        int x = read(fd, buffer, sizeof(buffer)); //从命名管道中读
        if(x &gt; 0)
        {
            buffer[x] = 0;
            cout &lt;&lt; "The server receives a message from the client: " &lt;&lt; buffer &lt;&lt; endl;
        }
    }

    close(fd); //关闭fd

    int m = unlink(FIFO_FILE); //删除命名管道
    if(m == -1) //删除管道失败
    {
        perror("unlink");
        exit(FIFO_DELETE_ERR);
    }
    return 0;
}
```

最后是 client.cc，代表客户端

```
//client.cc
//客户端
#include "shared.hpp"
using namespace std;

int main()
{
    //服务端已经创建管道了，客户端无需再创建
    int fd = open(FIFO_FILE, O_WRONLY); //写方式打开命名管道
    if(fd &lt; 0) //打开失败
    {
        perror("open");
        exit(FIFO_OPEN_ERR);
    }

    string message;
    while(true)
    {
        cout &lt;&lt; "Please enter# " &lt;&lt; endl; //用户输入内容
        cin &gt;&gt; message;

        write(fd, message.c_str(), message.size()); //将内容写入命名管道
    }

    close(fd); //关闭fd
    return 0;
}
```

运行效果如下：

需要注意，先启动server程序再启动client程序，否则命名管道没有被创建会导致打开文件失败

可以看到两个进程间已经能够完成基础的通信了，我们可以在原代码的基础上进行一些修改，让客户端退出时服务端也跟着退出，这里就不做额外的展示了

### 3.3 命名管道的读写规则

需要注意的是，从命名管道读取内容的一方在打开管道时不是马上就打开的，而是会等待写入方打开管道。如果要验证这一点，我们只需要在两份代码中的open函数后打印一些内容，就能观察到了

这里直接给出运行效果：

可以看到server先运行，但是没有打印内容。直到client也开始运行，二者才一起打印

命名管道的读写规则如下：

所以是否设置O_NONBLOCK，就决定了读端或写端在没有另一半的时候是否会阻塞等待

如有错误，欢迎在评论区指出

完.
