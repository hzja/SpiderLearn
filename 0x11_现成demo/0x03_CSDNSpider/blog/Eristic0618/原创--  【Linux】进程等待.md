# 原创
：  【Linux】进程等待

# 【Linux】进程等待

**目录**

[一、进程终止](#%E4%B8%80%E3%80%81%E8%BF%9B%E7%A8%8B%E7%BB%88%E6%AD%A2)

[1.1 程序正常终止](#1.1%20%E7%A8%8B%E5%BA%8F%E6%AD%A3%E5%B8%B8%E7%BB%88%E6%AD%A2)

[1.2 程序异常终止](#1.2%20%E7%A8%8B%E5%BA%8F%E5%BC%82%E5%B8%B8%E7%BB%88%E6%AD%A2)

[1.3 exit和_exit](#1.3%20exit%E5%92%8C_exit)

[二、进程等待](#%E4%BA%8C%E3%80%81%E8%BF%9B%E7%A8%8B%E7%AD%89%E5%BE%85)

[2.1 进程等待的方法](#2.1%20%E8%BF%9B%E7%A8%8B%E7%AD%89%E5%BE%85%E7%9A%84%E6%96%B9%E6%B3%95)

[（1）wait](#%EF%BC%881%EF%BC%89wait)

[（2）waitpid](#%EF%BC%882%EF%BC%89waitpid)

[2.2 获取子进程退出状态](#2.2%20%E8%8E%B7%E5%8F%96%E5%AD%90%E8%BF%9B%E7%A8%8B%E9%80%80%E5%87%BA%E7%8A%B6%E6%80%81)

---


## 一、进程终止

一个进程在退出的时候，有以下三种情况：

### 1.1 程序正常终止

我们可以通过在main函数中return、调用exit或_exit函数让一个进程正常终止，进程正常结束后会返回一个**退出码**。不同的退出码可以代表不同的错误原因，用于告诉用户程序是否发生错误、发生了什么错误。

例如return 0就是返回一个为0的退出码，表示程序成功运行

我们可以通过** **echo $? ****命令来查看上个进程的退出码，例如：

```
#include &lt;stdio.h&gt;

int main()
{
    return 12;
}     
```

这个程序将会返回退出码12，我们运行该程序后输入上面的命令

问题来了：我怎么知道有哪些退出码，什么退出码又对应哪些错误原因呢？

我们可以用strerror函数来观察，向该函数传入退出码后会返回该退出码对应的错误信息

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;

int main()
{
    for(int i = 0;i &lt; 200;i++)
    {
        printf("%d: %s\n", i, strerror(i));
    }
    return 0;                                                                                                                                                                                                 
}                       
```

### 1.2 程序异常终止

有时候运行代码时会遇到一些**严重错误**导致**程序异常终止**，此时我们就不用关心退出码了

就好比你考试考差了，原因是身体不舒服。但是如果你作弊，直接无法完成考试，别人也不会关心其他的原因了。所以如果程序异常终止或运行结果不正确，我们都要先检查是否出现异常，再检查退出码

程序发生异常后，对应的异常会被系统转化为**信号**的形式发送给父进程

在程序中将一个变量除以0，或者使用野指针都会导致异常。我们可以尝试一下：

可以看到除0错误在编译时就已经出现了警告，运行程序后直接发生Floating point exception即浮点数溢出的异常

而野指针错误在编译时虽然不会发出警告，但是运行程序后也会发生Segmentation fault即段错误的异常

实际上，每种异常也都有自己的编号，我们可以使用命令** kill -l **来查看

其中Floating point exception对应的编号为8，Segmentation fault对应的编号为11

我们甚至还可以通过** kill -编号 pid **的方式给一个进程发送信号将其终止，例如：

所以确认有没有发生异常，只需要检测是否收到信号即可。如果没收到信号则说明代码运行完毕，此时再检测退出码

### 1.3 exit和_exit

前面提到，除了遇到return让程序正常终止，我们还可以在程序中调用exit或_exit函数来让程序正常终止。这三者之间有什么区别呢？

return就像**函数的出口**，一个函数遇到return只会结束该函数，如果是main函数的话程序才会终止

exit和_exit就像**程序的出口**，无论在哪个函数中遇到它都会让程序直接终止。这两个函数的参数就是程序的退出码。

那么，这两个函数之间又有什么区别呢？

首先，_exit属于一个系统调用接口，而exit是C语言库中的函数。其次，exit在退出时会先对**缓冲区**进行刷新，然后才结束进程；而_exit只会直接结束进程

问题又来了，何为缓冲区？

实际上我们在对一个文件进行写入时**并不是直接写入到文件中**的，而是先写入到缓冲区，缓冲区再根据不同的方式将其内容刷新到文件中

缓冲区有三种刷新方式：

一般我们在向显示器文件进行写入时采用的策略是行缓冲，即遇到\n就打印一行；而对于普通文件系统则采用全缓冲策略。缓冲区的存在能够减少消耗，提高效率。

知道缓冲区是什么后，我们如何证明exit在退出时会刷新缓冲区，而_exit不会呢？

前面提到，我们在程序中打印内容（向显示器文件中写入）是行缓冲，那么我们可以多打印一些不带\n的内容，这些内容都会堆积在缓冲区中。然后再用exit和_exit终止程序，看看是否会进行打印

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;

int main()
{
    for(int i = 0;i &lt; 10;i++)                                                                                                                                                                                 
    {
        printf("hello Linux");
    }
    //exit(0);
    _exit(0);
}

```

运行代码后可以看到，如果用_exit函数终止程序，缓冲区不会被刷新；而用exit函数终止程序时缓冲区被刷新，显示器上也能够显示内容

实际上我们在前面说的缓冲区是**语言层面的缓冲区**，内核中还存在着其他的缓冲区，这些是后面才会提到的内容

---


## 二、进程等待

之前提到过，子进程退出如果没有被父进程回收，就会变成僵尸进程造成内存泄漏。而且我们需要知道子进程是否完成了我们给的任务，所以进程等待就显得很有必要了

进程等待即父进程通过wait或waitpid函数回收子进程的资源，并且获取子进程的退出信息

### 2.1 进程等待的方法

#### （1）wait

```
#include&lt;sys/types.h&gt;
#include&lt;sys/wait.h&gt;

pid_t wait(int* status);
```

wait函数成功执行会返回被等待进程的pid，如果失败返回-1

其参数是一个输出型参数，我们可以通过这个参数拿到子进程的退出码等信息，如果不需要获取退出状态则设置为NULL即可

我们可以通过下面这段代码测试一下wait函数：

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/wait.h&gt;

int main()
{
    pid_t id = fork();
    if(id &lt; 0)
    {
        perror("fork error");
        return 1;
    }
    else if(id == 0) //子进程
    {
        int cnt = 3;
        while(cnt) //循环3次
        {
            printf("I am child, pid:%d, ppid:%d, cnt=%d\n", getpid(), getppid(), cnt);
            cnt--;
            sleep(1);
        }
        exit(0); //子进程先退出
    }
    else //父进程
    {
        int cnt = 5;
        while(cnt) //循环五次
        {
            printf("I am parent, pid:%d, cnt=%d\n", getpid(), cnt);
            cnt--;
            sleep(1);
        }
        pid_t ret = wait(NULL); //等待子进程
        if(ret == id)
        {
            printf("wait success, ret=%d\n", ret); //等待成功
        }
        sleep(5);                                                                                                                                                                                             
    }                                                                      
    return 0;                                                              
}     
```

运行代码，子进程先退出，然后被父进程回收

wait函数采用**阻塞式等待**，即如果父进程在执行到wait的时候子进程还没结束，那么父进程停止继续运行，wait函数一直不返回，直到子进程退出

#### （2）waitpid

```
#include&lt;sys/types.h&gt;
#include&lt;sys/wait.h&gt;

pid_t waitpid(pid_t pid, int* status, int options);
```

waitpid函数比wait又多了两个参数，其中pid参数用于设置要等待的进程，设置为-1则等待任意一个进程，如果传入子进程ID则只会等待该进程结束

options参数可以设置为**WNOHANG**，即**非阻塞等待**。此时若指定的进程未结束则返回0，否则返回该子进程ID。设置为0则默认阻塞式等待

waitpid成功调用后返回被等待子进程ID，如果设置了非阻塞等待且调用时子进程未结束则返回0，如果调用中出错则返回-1（如等待了一个不属于自己的子进程）

我们可以用下面这段代码测试一下waitpid：

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/wait.h&gt;

int main()
{
    pid_t id = fork();
    if(id &lt; 0)
    {
        perror("fork error");
        return 1;
    }
    else if(id == 0) //子进程
    {
        while(1) //死循环 
        {
            printf("I am child, pid:%d, ppid:%d\n", getpid(), getppid());
            sleep(100);
        }
    }
    else //父进程
    {
        int cnt = 5;
        while(cnt) //循环五次
        {
            printf("I am parent, pid:%d, cnt=%d\n", getpid(), cnt);
            cnt--;
            sleep(1);
        }
        pid_t ret = waitpid(id, NULL, WNOHANG); //非阻塞等待子进程 
        if(ret == id)
        {
            printf("wait success, ret=%d\n", ret); //等待成功
        }
        else if(ret == 0)  
        {                      
            printf("子进程未退出");
        }                                                                                                                                                                                              
    }                                                                      
    return 0;                                                              
}     
```

运行代码，子进程一直不退出，而waitpid中options设置为WNOHANG即非阻塞等待

此时父进程不再阻塞式等待，如果调用waitpid时子进程还没退出则直接返回0

### 2.2 获取子进程退出状态

前面提到，wait和waitpid中都有个输出型参数status，我们可以通过它获取子进程的退出状态

用下面这段代码测试是否真的能获取子进程的退出码等信息

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/wait.h&gt;

int main()
{
    pid_t id = fork();
    if(id &lt; 0)
    {
        perror("fork error");
        return 1;
    }
    else if(id == 0) //子进程
    {
        int cnt = 3;
        while(cnt) //循环3次
        {
            printf("I am child, pid:%d, ppid:%d, cnt=%d\n", getpid(), getppid(), cnt);
            cnt--;
            sleep(1);
        }
        exit(0); //子进程先退出，这里将退出码设置为1
    }
    else //父进程
    {
        int cnt = 5;
        while(cnt) //循环五次
        {
            printf("I am parent, pid:%d, cnt=%d\n", getpid(), cnt);
            cnt--;
            sleep(1);
        }
        int status = 0;
        pid_t ret = waitpid(id, &amp;status, 0); //阻塞式等待子进程
        if(ret == id)
        {
            printf("wait success, ret=%d, status=%d\n", ret, status); //等待成功，打印status
        }                                                                                                                                                                                      
    }                                                                      
    return 0;                                                              
}     
```

运行代码

可以看到子进程的退出码明明是1，但是这里打印status的值竟然是256，为什么？

前面提到，一个进程在退出的时候有三种情况，即正常终止结果正确、正常终止结果不正确和异常终止，所以status不仅要获取进程的退出码，还要获取进程的异常信息。因此status实际上并不是以整型为单位来存储信息的，而是将int整型的前16位分成几个区，一个区包含多个位

其中，16位中的低7位存储异常的终止信号，高8位存储程序的退出状态码

我们可以通过位运算来打印出信号和退出码，如：

<img alt="" height="227" src="https://i-blog.csdnimg.cn/direct/96a2138eabc44ea59436270e72c90334.png" width="556"/> 

除了位运算，还有两个宏也可以帮助我们解析status

除了阻塞式等待和非阻塞等待，还有一种方式叫做**非阻塞轮询**

非阻塞轮询：非阻塞等待+循环式询问

例如你要找一个人，给他打电话时他在忙，于是你过一段时间就打一次电话问他忙完没，这是非阻塞轮询；如果你和他打电话并一直不挂断，直到他忙完，这是阻塞式等待

完.
