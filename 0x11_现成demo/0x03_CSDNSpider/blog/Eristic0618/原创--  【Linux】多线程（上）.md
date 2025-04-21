# 原创
：  【Linux】多线程（上）

# 【Linux】多线程（上）

**目录**

[一、概念](#%E4%B8%80%E3%80%81%E6%A6%82%E5%BF%B5)

[1.1 线程的概念](#1.1%20%E7%BA%BF%E7%A8%8B%E7%9A%84%E6%A6%82%E5%BF%B5)

[1.2 线程周边概念](#1.2%20%E7%BA%BF%E7%A8%8B%E5%91%A8%E8%BE%B9%E6%A6%82%E5%BF%B5)

[二、线程的优缺点](#%E4%BA%8C%E3%80%81%E7%BA%BF%E7%A8%8B%E7%9A%84%E4%BC%98%E7%BC%BA%E7%82%B9)

[2.1 优点](#2.1%20%E4%BC%98%E7%82%B9)

[2.2 缺点](#2.2%20%E7%BC%BA%E7%82%B9)

[三、线程与进程](#%E4%B8%89%E3%80%81%E7%BA%BF%E7%A8%8B%E4%B8%8E%E8%BF%9B%E7%A8%8B)

[四、线程控制](#%E5%9B%9B%E3%80%81%E7%BA%BF%E7%A8%8B%E6%8E%A7%E5%88%B6)

[4.1 POSIX线程库](#4.1%20POSIX%E7%BA%BF%E7%A8%8B%E5%BA%93)

[4.2 线程创建](#4.2%20%E7%BA%BF%E7%A8%8B%E5%88%9B%E5%BB%BA)

[pthread_create](#pthread_create)

[pthread_t及地址空间的布局](#pthread_t%E5%8F%8A%E5%9C%B0%E5%9D%80%E7%A9%BA%E9%97%B4%E7%9A%84%E5%B8%83%E5%B1%80)

[4.3 线程终止](#4.3%20%E7%BA%BF%E7%A8%8B%E7%BB%88%E6%AD%A2)

[pthread_exit](#pthread_exit)

[pthread_cancel](#pthread_cancel)

[4.4 线程等待](#4.4%20%E7%BA%BF%E7%A8%8B%E7%AD%89%E5%BE%85)

[pthread_join](#pthread_join)

[4.5 线程分离](#4.5%20%E7%BA%BF%E7%A8%8B%E5%88%86%E7%A6%BB)

[pthread_detach](#pthread_detach)

[pthread_self](#pthread_self)

---


## 一、概念

### 1.1 线程的概念

不同操作系统对线程的实现方案可能是不一样的。在部分其他的操作系统中，线程有自己独立的线程控制模块TCB（Thread Control Block），但是这样就要为进程单独重新设计各种调度算法

而Linux中选择直接复用进程的数据结构和管理算法来实现线程，即Linux中的线程是由进程模拟的线程，所以认为Linux没有真正意义上的线程，又称为**轻量级进程**（LWP）。这也是为何上面说线程也要创建PCB，因为复用了进程的结构 

进程与线程是1：n的关系，因此操作系统中线程的数量一定比进程要多

进程与线程的关系可以类比为家庭与家人的关系，家庭中的家人可以共享家庭内的资源，并且各司其职维持家庭的运行，家庭中至少存在一个家人

我们过去学习的进程，实际上就是只有一个线程执行流的进程

### 1.2 线程周边概念

说线程是轻量级进程，首先在于线程的创建与释放更加轻量化。线程在创建时只需要创建新的PCB，不需要创建新的地址空间和页表，释放时也只需要释放PCB

其次，线程的切换也更加轻量化

---


## 二、线程的优缺点

### 2.1 优点

### 2.2 缺点

---


## 三、线程与进程

> 
线程需要自己独立的一批寄存器存放线程的上下文
线程有自己独立的栈结构以避免线程之间出现错乱，不同线程之间的栈不共享！这与我们过去的认知有些区别


---


## 四、线程控制

### 4.1 POSIX线程库

Linux中没有明确的线程的概念，因此内核没有给我们提供线程的系统调用，只有轻量级进程的系统调用

但我们用户又需要线程的接口，因此开发者在应用层对轻量级进程的接口进行了封装，为用户提供了许多线程的接口——pthread线程库。几乎所有的Linux平台都默认自带这个第三方库，而我们在编写多线程代码时也需要使用这个库

要使用pthread线程库，需要引入头文件&lt;pthread.h&gt;，并且在编译链接时需要带-lpthread选项

### 4.2 线程创建

#### pthread_create

```
#include &lt;pthread.h&gt;

int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                   void *(*start_routine) (void *), void *arg);
```

pthread_create函数用于创建一个新进程，成功返回0，失败返回错误码

其中：

例子：

```
#include &lt;iostream&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
#include &lt;pthread.h&gt;

using namespace std;

void* threadRoutine(void* arg) //新线程的例程
{
    while(true)
    {
        cout &lt;&lt; "new thread, pid:" &lt;&lt; getpid() &lt;&lt; endl;
        sleep(2);
    }
    return nullptr;
}

int main()
{
    pthread_t tid;
    pthread_create(&amp;tid, nullptr, threadRoutine, nullptr); //创建线程
    while(true) //主线程
    {
        cout &lt;&lt; "main thread, pid:" &lt;&lt; getpid() &lt;&lt; endl;
        sleep(2);
    }
    return 0;
}
```

运行结果： 

可以看到主线程和新线程的PID是一样的，操作系统怎么区分呢？

运行程序，输入 ****ps -aL**** 可以看到当前所有线程的信息

可以看到同一进程内的线程虽然PID相同，但LWP是不同的，操作系统根据LWP对线程进行调度

主线程的PID与LWP相同

#### pthread_t及地址空间的布局

需要额外一提，pthread_t所说的线程ID与我们前面指的线程ID不是一回事，前面提到的线程ID属于**线程调度**的范畴，用于表示线程的唯一性。而pthread_t类型的参数指向一个虚拟内存单元，该内存单元的地址即为新创建线程的线程ID

线程是如何在进程地址空间中布局的？

我们的线程库需要被加载到内存中，线程库也需要维护我们创建的线程，因此在线程库中就需要对线程进行管理。因此，我们创建的线程，在线程库中还有库级别的TCB，其起始地址就是线程的tid

线程的独立栈结构是在线程库内部进行维护的，线程库是动态库，需要被加载到共享区

线程需要有自己独立的栈结构，因为每个线程都有自己独立的调用链。除了主线程，其他所有线程的独立栈结构都在共享区——准确来说是在pthread库中tid指向的用户TCB内部

### 4.3 线程终止

前面提到，线程如果被异常终止，那整个进程也会随之崩溃，那如何正常的使线程终止呢？

我们先来看pthread_exit函数

#### pthread_exit

```
#include &lt;pthread.h&gt;

void pthread_exit(void *retval);
```

retval是一个输出型参数，用于带出线程例程的返回值，pthread_exit函数本身无返回值

注意，调用pthread_exit时，retval指向的内存单元一定得是**全局的**或者是**用malloc分配的**，而不能是线程例程中的一个局部变量，否则线程终止后变量被销毁，retval就变成一个野指针了

包括如果我们在线程的例程中return了一个指针，这个指针指向的内存单元也必须符合上面的要求

例子：

```
#include &lt;iostream&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
#include &lt;pthread.h&gt;

using namespace std;

void* threadRoutine(void* arg) //新线程的例程
{
    int cnt = 0;
    while(true)
    {
        if(cnt == 3)
        {
            cout &lt;&lt; "new thread exit!" &lt;&lt; endl;
            pthread_exit(nullptr);
        }
        cout &lt;&lt; "new thread, pid:" &lt;&lt; getpid() &lt;&lt; endl;
        cnt++;
        sleep(1);
    }
    return nullptr;
}

int main()
{
    pthread_t tid;
    pthread_create(&amp;tid, nullptr, threadRoutine, nullptr); //创建线程
    while (true) // 主线程
    {
        cout &lt;&lt; "main thread, pid:" &lt;&lt; getpid() &lt;&lt; endl;
        sleep(1);
    }
    return 0;
}
```

运行结果：

#### pthread_cancel

```
#include &lt;pthread.h&gt;

int pthread_cancel(pthread_t thread);
```

pthread_cancel函数用于取消一个执行中的线程，成功返回0，失败返回错误码，参数thread传入指定线程的ID

被取消的线程本身在例程中会返回**PTHREAD_CANCELED**的宏，其内容是(void*)-1

例子：

```
#include &lt;iostream&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
#include &lt;pthread.h&gt;

using namespace std;

void* threadRoutine(void* arg) //新线程的例程
{
    while(true)
    {
        cout &lt;&lt; "new thread, pid:" &lt;&lt; getpid() &lt;&lt; endl;
        sleep(1);
    }
    return nullptr;
}

int main()
{
    pthread_t tid;
    pthread_create(&amp;tid, nullptr, threadRoutine, nullptr); //创建线程
    int cnt = 0;
    while (true) // 主线程
    {
        if(cnt == 3)
        {
            int n = pthread_cancel(tid);
            cout &lt;&lt; "new thread cancel!" &lt;&lt; endl;
            break;
        }
        cout &lt;&lt; "main thread, pid:" &lt;&lt; getpid() &lt;&lt; endl;
        cnt++;
        sleep(1);
    }
    return 0;
}
```

运行结果：

### 4.4 线程等待

#### pthread_join

```
#include &lt;pthread.h&gt;

int pthread_join(pthread_t thread, void **retval);
```

pthread_join函数用于阻塞式等待一个线程的结束，成功返回0，失败返回错误码

其中：

pthread_join函数等待的线程必须是joinable的，即等待的线程不能已经分离（后面会提到）

调用该函数的线程将会阻塞式等待目标线程退出，其中又分为以下几种情况：

例子：

```
#include &lt;iostream&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
#include &lt;pthread.h&gt;

using namespace std;

int cnt = 0;

void* threadRoutine(void* arg) //新线程的例程
{
    while(true)
    {
        if(cnt == 3)
        {
            cout &lt;&lt; "new thread exit!" &lt;&lt; endl;
            pthread_exit(&amp;cnt);
        }
        cout &lt;&lt; "new thread, pid:" &lt;&lt; getpid() &lt;&lt; endl;
        cnt++;
        sleep(1);
    }
    return nullptr;
}

int main()
{
    pthread_t tid;
    pthread_create(&amp;tid, nullptr, threadRoutine, nullptr); //创建线程
    int *retval;
    pthread_join(tid, (void**)&amp;retval);
    cout &lt;&lt; *retval &lt;&lt; endl;
    return 0;
}
```

运行结果：

### 4.5 线程分离

#### pthread_detach

如果一个线程终止，而我们又没有对其进行线程等待，那么其资源没有被释放就会造成系统泄露。

有的时候，我们可能不需要线程返回一个值，或者不关注线程的返回值，那么对其进行线程等待是一种负担。此时我们就可以选择让线程分离，即线程退出时自己释放线程资源

```
#include &lt;pthread.h&gt;

int pthread_detach(pthread_t thread);
```

pthread_detach函数成功返回0，失败返回错误码，参数thread传入线程ID

可以是线程自己让自己分离，也可以是线程组内的其他线程对目标线程进行分离。问题：如果线程自己让自己分离，它怎么知道自己的线程ID呢？

#### pthread_self

```
#include &lt;pthread.h&gt;

pthread_t pthread_self(void);
```

pthread_self函数会返回调用该函数的线程的ID，搭配pthread_detach函数使用就能让线程自己分离

一个线程不能既是joinable的又是分离的，即线程如果分离就不能再被线程等待

例子：

```
#include &lt;iostream&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
#include &lt;pthread.h&gt;

using namespace std;

void* threadRoutine(void* arg) //新线程的例程
{
    pthread_detach(pthread_self());
    int cnt = 0;
    while(true)
    {
        if(cnt == 3)
        {
            cout &lt;&lt; "new thread exit!" &lt;&lt; endl;
            pthread_exit(&amp;cnt);
        }
        cout &lt;&lt; "new thread, pid:" &lt;&lt; getpid() &lt;&lt; endl;
        cnt++;
        sleep(1);
    }
    return nullptr;
}

int main()
{
    pthread_t tid;
    pthread_create(&amp;tid, nullptr, threadRoutine, nullptr); //创建线程
    sleep(1);
    if(pthread_join(tid, nullptr) == 0)
        cout &lt;&lt; "wait thread success" &lt;&lt; endl;
    else
        cout &lt;&lt; "wait thread failed" &lt;&lt; endl;
    return 0;
}
```

运行结果：

如有错误，欢迎在评论区指出

【Linux】多线程（上）完.
