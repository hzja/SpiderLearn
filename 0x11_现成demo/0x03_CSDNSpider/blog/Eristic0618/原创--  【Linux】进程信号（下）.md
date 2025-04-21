# 原创
：  【Linux】进程信号（下）

# 【Linux】进程信号（下）

**目录**

[一、信号的阻塞](#%E4%B8%80%E3%80%81%E4%BF%A1%E5%8F%B7%E7%9A%84%E9%98%BB%E5%A1%9E)

[1.1 信号在内核中的保存方式](#1.1%20%E4%BF%A1%E5%8F%B7%E5%9C%A8%E5%86%85%E6%A0%B8%E4%B8%AD%E7%9A%84%E4%BF%9D%E5%AD%98%E6%96%B9%E5%BC%8F)

[1.2 sigset_t信号集](#1.2%20sigset_t%E4%BF%A1%E5%8F%B7%E9%9B%86)

[（1）信号集操作](#%EF%BC%881%EF%BC%89%E4%BF%A1%E5%8F%B7%E9%9B%86%E6%93%8D%E4%BD%9C)

[（2）sigprocmask函数](#%EF%BC%882%EF%BC%89sigprocmask%E5%87%BD%E6%95%B0)

[（3）sigpending函数](#%EF%BC%883%EF%BC%89sigpending%E5%87%BD%E6%95%B0)

[二、信号的处理](#%E4%BA%8C%E3%80%81%E4%BF%A1%E5%8F%B7%E7%9A%84%E5%A4%84%E7%90%86)

[2.1 用户态和内核态](#2.1%20%E7%94%A8%E6%88%B7%E6%80%81%E5%92%8C%E5%86%85%E6%A0%B8%E6%80%81)

[2.2 重谈进程地址空间](#2.2%20%E9%87%8D%E8%B0%88%E8%BF%9B%E7%A8%8B%E5%9C%B0%E5%9D%80%E7%A9%BA%E9%97%B4)

[三、信号的捕捉](#%E4%B8%89%E3%80%81%E4%BF%A1%E5%8F%B7%E7%9A%84%E6%8D%95%E6%8D%89)

[sigaction函数](#sigaction%E5%87%BD%E6%95%B0)

前文： 

[【Linux】进程信号（上）-CSDN博客文章浏览阅读729次，点赞29次，收藏27次。本篇文章围绕Linux中的进程信号展开讲解，包含信号的概念、信号的产生等内容<img alt="" src="https://g.csdnimg.cn/static/logo/favicon32.ico"/>https://blog.csdn.net/Eristic0618/article/details/142900955](https://blog.csdn.net/Eristic0618/article/details/142900955)

---


## 一、信号的阻塞

### 1.1 信号在内核中的保存方式

前面提到，进程在接收到**普通信号**时，并不是立即进行处理的

假设一个信号被阻塞，则这个信号将一直保持未决的状态，直到进程解除对该信号的阻塞才能执行递达动作

进程的阻塞和信号的阻塞是两回事，信号阻塞类似于屏蔽了某个信号

信号的阻塞与忽略也是不同的，信号被阻塞后会一直存在，而忽略是对信号的一种处理动作

进程的PCB中有三个表，分别是block表、pending表和handler表，其中：

三个表一起看，就能知道一个信号**是否被屏蔽**，**是否被收到**，**处理方法是什么**

我们通过signal函数捕捉某个信号，实际上就是把用户提供的函数指针**覆盖**到handler表的对应位置

信号的处理方式类型为__sighandler_t，实际定义为：

```
typedef void(*__sighandler_t)(int);
```

系统中还定义了一些信号的默认处理方法：

```
#define SIG_DFL ((__sighandler_t) 0)
#define SIG_IGN ((__sighandler_t) 1)
```

其中SIG_DFL表示收到信号后终止进程，SIG_IGN表示忽略某个信号

### 1.2 sigset_t信号集

#### （1）信号集操作

sigset_t是一个数据类型，称为信号集，本质上是一个位图

我们的block表和pending表的类型都是sigset_t，其每一位对应一个信号，值为1或0则表示是否未决或被阻塞

要对一个信号集进行修改，只能通过特定函数：

```
#include &lt;signal.h&gt;

int sigemptyset(sigset_t *set);
int sigfillset(sigset_t *set);
int sigaddset(sigset_t *set, int signum);
int sigdelset(sigset_t *set, int signum);
int sigismember(const sigset_t *set, int signum);
```

其中：

通过这几个函数，我们就能对一个信号集进行初始化或修改等操作了

#### （2）sigprocmask函数

```
#include &lt;signal.h&gt;

int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
```

sigprocmask函数可以读取或修改进程的信号屏蔽字（阻塞信号集），成功返回0，出错返回-1

其中：

若set和oset都为非空，则先读取再修改

#### （3）sigpending函数

```
#include &lt;signal.h&gt;

int sigpending(sigset_t *set);
```

sigpending函数可以通过set参数读取当前进程的未决信号集，成功返回0，出错返回-1

例如：

```
#include &lt;iostream&gt;
#include &lt;signal.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;

using namespace std;

void PrintSigset(sigset_t *set) //打印信号集
{
    for (int i = 1;i &lt; 32; i++) //遍历所有普通信号
    {
        if(sigismember(set, i)) //判断当前信号在信号集中是否有效
            cout &lt;&lt; 1;
        else
            cout &lt;&lt; 0;
    }
    cout &lt;&lt; endl;
}

int main()
{
    sigset_t set, p;
    sigemptyset(&amp;set);
    sigaddset(&amp;set, 1); //向信号集中添加1号信号
    sigprocmask(SIG_BLOCK, &amp;set, NULL); //将set中的有效信号添加到信号屏蔽字中
    while(true)
    {
        cout &lt;&lt; "process running...,pid: " &lt;&lt; getpid() &lt;&lt; ", pending: ";
        sigpending(&amp;p); //取出未决信号集
        PrintSigset(&amp;p); //打印未决信号集
        sleep(1);
    }
    return 0;
}
```

运行结果： 

在代码中，我们将1号信号添加到了进程的信号屏蔽字中，所以如果进程接收到1号信号后不会对其进行处理 

通过运行结果可以发现，在我们向进程发送1号信号后，未决信号集的第一位由0变为1，说明此时1号信号处于未决状态，没有被处理。如果过段时间后再对1号信号解除阻塞，那么进程就会在合适的时候处理信号

当然，和信号的捕捉一样，9和19号信号也是无法被阻塞的。试想一下，如果一个进程将所有的信号都阻塞了，那是不是变得刀枪不入了？

---


## 二、信号的处理

### 2.1 用户态和内核态

我们一直说进程会在合适的时候处理信号，具体是什么时候呢？

进程要知道自己是否收到了信号或是否需要对信号进行处理，就需要访问自己的pending表、block表和handler表。但这三张表都是内核中的数据结构，说明进程一定要处在一种**内核状态**才能对信号进行处理

首先搞清楚什么是内核态，和与其对应的用户态：

> 
这里直接给出结论：我们的进程在**从内核态返回到用户态**的时候，进行信号的检测与处理


关于进程在用户态和内核态之间的切换，还有一些内容需要我们了解 

例如进程在执行一些封装了系统调用的库函数时，就需要从用户态陷入到内核态，其中是通过一条汇编指令 "int 0x80" 实现的

### 2.2 重谈进程地址空间

Linux的进程地址空间大小为4GB，其中位于**较高地址**的1GB为**内核空间**，通过**内核级页表**映射了**操作系统的代码和数据**；**较低地址**的3GB为用户空间，供进程使用，通过用户级页表映射到物理内存中进程自己的代码和数据。

操作系统中有几个进程就有几个用户级页表，但内核级页表在操作系统中只有一份，可以被所有进程看到，所以每个进程的内核空间映射的内容都是一样的

> 
既然内核空间是进程地址空间的一部分，而内核空间又映射了操作系统的代码和数据，那么我们在调用系统调用接口的时候，难道不就是在进程自己的地址空间中调用吗？


站在进程的视角，调用系统调用接口，就相当于我们从用户空间的正文代码中跳转到内核空间，执行完毕后再返回到用户空间

但是操作系统肯定不会允许我们进程随心所欲的访问内核空间的内容，只有进程处于内核态时才拥有访问内核空间的权限。如何判断一个进程是处于用户态还是内核态呢？

既然内核态的权限那么大，那处于内核态的进程能否执行用户空间的代码呢？**不行！**

依旧是为了操作系统的安全，OS不会执行任何用户所写的代码（避免用户的代码中包含非法操作等情况），因此进程需要从内核态再重新返回用户态执行用户的代码

我们回到信号的话题，看看进程遇到异常收到信号时是如何进行用户态和内核态的切换的

---


## 三、信号的捕捉

### sigaction函数

除了signal函数，我们还可以通过sigaction函数捕捉一个信号（包括实时信号）

```
#include &lt;signal.h&gt;

int sigaction(int signo, const struct sigaction *act, struct sigaction *oact);
```

sigaction函数用于修改特定信号的处理动作，成功返回0，失败返回-1并设置错误码

其中：

```
struct sigaction {
    void     (*sa_handler)(int);
    void     (*sa_sigaction)(int, siginfo_t *, void *);
    sigset_t   sa_mask;
    int        sa_flags;
    void     (*sa_restorer)(void);
};
```

如果要捕捉的是普通信号，我们主要关注结构体中的**sa_handler**就行，这是我们捕捉信号的自定义处理方法。sa_sigaction是实时信号的处理方法，我们不深入了解

关于sa_mask字段：

> 
在捕捉某个信号时内核会暂时性的将该信号屏蔽，直到将当前信号处理完毕后才会解除屏蔽，避免同样的信号被重复捕捉
如果在处理信号时除了屏蔽当前信号，还希望额外暂时性屏蔽一些其他信号，则通过sa_mask字段进行说明


完.
