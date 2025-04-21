# 原创
：  【Linux】进程信号（上）

# 【Linux】进程信号（上）

**目录**

[一、信号概念](#%E4%B8%80%E3%80%81%E4%BF%A1%E5%8F%B7%E6%A6%82%E5%BF%B5)

[1.1 生活中的信号](#1.1%20%E7%94%9F%E6%B4%BB%E4%B8%AD%E7%9A%84%E4%BF%A1%E5%8F%B7)

[1.2 进程中的信号  ](#1.2%20%E8%BF%9B%E7%A8%8B%E4%B8%AD%E7%9A%84%E4%BF%A1%E5%8F%B7%C2%A0%C2%A0)

[1.3 信号的概念](#1.3%20%E4%BF%A1%E5%8F%B7%E7%9A%84%E6%A6%82%E5%BF%B5)

[二、信号的产生](#%E4%BA%8C%E3%80%81%E4%BF%A1%E5%8F%B7%E7%9A%84%E4%BA%A7%E7%94%9F)

[2.1 通过组合键产生信号](#2.1%C2%A0%E9%80%9A%E8%BF%87%E7%BB%84%E5%90%88%E9%94%AE%E4%BA%A7%E7%94%9F%E4%BF%A1%E5%8F%B7)

[2.2 通过函数发送信号](#2.2%20%E9%80%9A%E8%BF%87%E5%87%BD%E6%95%B0%E5%8F%91%E9%80%81%E4%BF%A1%E5%8F%B7)

[kill命令](#kill%E5%91%BD%E4%BB%A4)

[kill函数](#kill%E5%87%BD%E6%95%B0)

[raise函数 ](#raise%E5%87%BD%E6%95%B0%C2%A0)

[abort函数 ](#abort%E5%87%BD%E6%95%B0%C2%A0)

[Core Dump](#Core%20Dump)

[2.3 特定软件条件下产生信号](#2.3%20%E7%89%B9%E5%AE%9A%E8%BD%AF%E4%BB%B6%E6%9D%A1%E4%BB%B6%E4%B8%8B%E4%BA%A7%E7%94%9F%E4%BF%A1%E5%8F%B7)

---


## 一、信号概念

### 1.1 生活中的信号

在日常生活中，我们的身边处处是信号，例如电话铃、红绿灯、闹钟等等，这些信号的设置是为了提示我们某种信息

又例如，点的外卖到了，我们接收到了外卖员发送的“信号”，知道此时应该对该信号进行处理即取外卖，但可能我们正在做一些重要事情脱不开身，于是过了一会才下楼将外卖取走。这说明**即使我们接收到了信号，也可以选择不同的处理该信号的方式**。

上面的情景说明，通过他人的教导，我们能够**识别某种信号的作用**以及**如何处理该信号**，例如绿灯就应该通行，闹钟响了代表该起床了，这些都是对信号的**默认处理动作**。但同时我们还可以自定义对信号的处理方式，例如闹钟响了但我仍然继续睡觉。

一般在接收到信号后我们有三种处理信号的方式：

### 1.2 进程中的信号  

上面的概念，在进程中也同样适用，进程必须能够识别并用某种方式处理不同的进程信号。

当我们在Shell中启动了一个**前台进程**，并按下ctrl+c，此时进程会直接退出，例如：

这是因为当我们按下ctrl+c后，键盘**产生硬件中断**被操作系统获取，并将我们的操作解释成信号发送给前台进程，进程**收到该信号后执行退出的动作**。

就像你在打游戏的过程中，你妈突然喊你吃饭，此时你就得老老实实关掉游戏去吃饭

前台进程在运行的过程中，用户随时都可能按下ctrl+c产生信号终止进程，因此信号相对于进程的运行流程是**异步的**

### 1.3 信号的概念

进程信号是Linux中用于**进程间通信和控制的一种机制**，是进程之间**事件异步通知**的一种方式，属于软中断。进程信号通常应用于进程间通信、异常处理、线程同步等场景。

进程信号有很多种，我们可以通过**** kill -l ****命令查看

而我们上面输入的ctrl+c，本质上是被解释为了2号信号即SIGINT信号，被进程接收 

其中，1-31号信号为普通信号，34号往后的信号是实时信号。这些不同的信号分别在哪些情况下产生，默认的处理动作是什么，通过**** man 7 signal ****命令可以查看

同时我们也可以通过signal函数来**修改进程对于某个信号的处理动作**

```
#include &lt;signal.h&gt;
typedef void (*sighandler_t)(int);

sighandler_t signal(int signum, sighandler_t handler);
```

其中handler是用户自定义的信号处理动作

例如：

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;
#include &lt;cstdlib&gt;
#include &lt;signal.h&gt;

using namespace std;

void myhandler(int sig)
{
    cout &lt;&lt; "process get a signal: " &lt;&lt; sig &lt;&lt; endl;
    exit(1);
}

int main()
{
    signal(SIGINT, myhandler); 
    while(1)
    {
        cout &lt;&lt; "process running..." &lt;&lt; endl;
        sleep(1);
    }
    return 0;
}
```

我们将SIGINT信号的处理方式修改为了我们的myhandler函数，然后运行代码：

可以看到，在我们输入ctrl+c后，进程收到的信号的确是2号信号 

> 
拓展：我们在键盘上输入的ctrl+c，是怎么被解释为对应信号的呢？


CPU上有很多针脚，通过这些针脚硬件就能向CPU发送硬件中断来告诉CPU，我这个硬件当中已经有数据输入了

同时，电脑当中有很多硬件，要进行区分，每个硬件都有自己**对应的中断号**。接收到对应硬件发送的硬件中断后，操作系统就**根据中断号在中断向量表中查找对应的函数指针指向的方法**，通过该方法来读取硬件当中的数据。

在把硬件中的数据读取到内存前，操作系统会先判断当前的数据是否是组合控制键，例如我们输入的ctrl+c，就会被转化为对应的信号发送给进程。在读取完毕后，硬件又会向CPU发送硬件中断来停止读取

硬件向CPU发送硬件中断，和我们向进程发送不同的信号是不是很类似？实际上我们要学习的信号就是用软件方式对进程模拟硬件中断。

---


## 二、信号的产生

### 2.1 通过组合键产生信号

除了ctrl+c会被解释为2号信号，ctrl+\会被解释为3号信号SIGQUIT，ctrl+z会被解释为19号信号SIGSTOP

### 2.2 通过函数发送信号

#### kill命令

除了组合键，我们还可以通过**** kill -信号 pid ****命令向进程发送信号

不是所有的信号都能够被修改默认处理动作的，否则假设一个进程将所有的信号都忽略，我们如何终止该进程？

接下来测试一下有哪些信号可以被捕捉，哪些信号不能被捕捉

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;
#include &lt;cstdlib&gt;
#include &lt;signal.h&gt;

using namespace std;

void myhandler(int sig)
{
    cout &lt;&lt; "process get a signal: " &lt;&lt; sig &lt;&lt; endl;
}

int main()
{
    for (int i = 1; i &lt;= 31; i++) //修改所有普通信号的默认处理动作
    {
        signal(i, myhandler);
    }
    while (1)
    {
        cout &lt;&lt; "process running..., pid: " &lt;&lt; getpid() &lt;&lt; endl;
        sleep(1);
    }
    return 0;
}
```

像这样，通过测试，我们最后可以发现只有9号信号SIGKILL和19号信号SIGSTOP无法被修改处理动作

#### kill函数

kill命令本质上是调用了kill系统调用实现的

```
#include &lt;sys/types.h&gt;
#include &lt;signal.h&gt;

int kill(pid_t pid, int sig);

```

通过传入pid和信号码sig，就可以向指定进程发送指定信号

用kill函数，我们就可以搭配命令行参数实现我们自己的kill命令了

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;
#include &lt;cstdlib&gt;
#include &lt;sys/types.h&gt;
#include &lt;signal.h&gt;

using namespace std;

void Usage(std::string proc)
{
    std::cout &lt;&lt; "Usage:\n\t" &lt;&lt; proc &lt;&lt; " signo pid" &lt;&lt; std::endl;
}

// ./mykill signo pid
int main(int argc, char* argv[])
{
    if(argc != 3)
    {
        Usage(argv[0]);
        exit(1);
    }

    int signo = atoi(argv[1]);
    pid_t pid = atoi(argv[2]);

    kill(pid, signo);

    return 0;
}
```

#### raise函数 

还有一个函数可以给进程自身发送信号

```
#include &lt;signal.h&gt;

int raise(int sig);

```

因为是给自身发送信号，因此raise函数不需要传入pid，只需要指定信号码

测试：

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;
#include &lt;cstdlib&gt;
#include &lt;signal.h&gt;

using namespace std;

void myhandler(int sig)
{
    cout &lt;&lt; "process get a signal: " &lt;&lt; sig &lt;&lt; endl;
}

int main()
{
    for (int i = 1; i &lt;= 31; i++)
    {
        signal(i, myhandler);
    }
    cout &lt;&lt; "process running..., pid: " &lt;&lt; getpid() &lt;&lt; endl;
    for (int i = 1; i &lt;= 31; i++) //发送1-31号信号
    {
        raise(i);
    }
    return 0;
}
```

可以再次证明，9号信号的处理方式无法被修改，一旦信号收到9号信号就立即被杀死

#### abort函数 

还有一个函数可以让进程立即终止

```
#include &lt;stdlib.h&gt;

void abort(void);

```

测试：

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;
#include &lt;cstdlib&gt;
#include &lt;signal.h&gt;

using namespace std;

void myhandler(int sig)
{
    cout &lt;&lt; "process get a signal: " &lt;&lt; sig &lt;&lt; endl;
}

int main()
{
    for (int i = 1; i &lt;= 31; i++)
    {
        signal(i, myhandler);
    }
    int cnt = 10;
    while (cnt--)
    {
        cout &lt;&lt; "process runnning..., pid: " &lt;&lt; getpid() &lt;&lt; endl;
        if(cnt == 5)
            abort();
        sleep(1);
    }
    return 0;
}
```

可以看到abort函数会向进程发送6号信号SIGABRT，但是我们不是可以对6号信号的处理方式进行修改吗？为什么进程还是会被终止？

这是由abort函数的行为决定的，该函数不止会向进程发送6号信号，还会让进程终止。也就是说导致进程终止的不是abort函数发送的6号信号，所以我们不能用kill函数或raise函数代替abort函数

#### Core Dump

在三个月之前讲如何获取子进程的退出状态的时候，曾经出现过Core Dump这个名词

[【Linux】进程等待-CSDN博客<img alt="icon-default.png?t=O83A" src="https://csdnimg.cn/release/blog_editor_html/release2.3.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=O83A"/>https://blog.csdn.net/Eristic0618/article/details/140667331?spm=1001.2014.3001.5502](https://blog.csdn.net/Eristic0618/article/details/140667331?spm=1001.2014.3001.5502)

当时没有细讲，这里我们来聊聊什么是Core Dump

在signal(7)中，关于默认处理方式：

```
Term   Default action is to terminate the process.
Ign    Default action is to ignore the signal.
Core   Default action is to terminate the process and dump core (see core(5)).
Stop   Default action is to stop the process.
Cont   Default action is to continue the process if it is currently stopped.

```

其中：

然后是不同信号的默认处理方式：

可以看到，不同信号的默认处理方式也可能不同

首先我们来解释一下何为Core Dump。当进程异常终止时，可以选择将进程的用户空间内存数据全部保存到磁盘上，形成一个core文件，这个过程叫做Core Dump

通过调试器检查core文件可以帮助我们查清进程异常终止时的错误原因，这叫做事后调试（Post-mortem Debug）。一个进程能够生成多大的core文件取决于进程的core file size，我们可以通过**** ulimit -a ****命令查看

可以看到此时进程的core file size为0，说明进程不被允许创建core文件。

这是因为生成core文件也并不是那么安全的，一方面是core文件中可能包含某些隐私信息，另一方面是如果默认允许进程生成core文件，假设某个带有自重启功能的服务挂掉了，一瞬间就会产生大量的core文件把磁盘挤爆

我们可以通过**** ulimit -c 大小 ****来修改core file size的数值

而我们之前提到的Core Dump标志位，就是用来标记进程是Term终止还是Core终止。通过位运算我们也可以将该标志位解析出来：

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;
#include &lt;cstdlib&gt;
#include &lt;signal.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/wait.h&gt;

using namespace std;

int main()
{
    pid_t id = fork();
    if(id == 0)
    {
        while(true)
        {
            cout &lt;&lt; "child process running..., pid: " &lt;&lt; getpid() &lt;&lt; endl;
            sleep(1);
        }
        exit(0);
    }

    int status = 0;
    pid_t rid = waitpid(id, &amp;status, 0);
    if(rid == id)
    {
        cout &lt;&lt; "waitpid success, exit code: " &lt;&lt; ((status &gt;&gt; 8) &amp; 0xFF) 
        &lt;&lt; ", exit signal: " &lt;&lt; (status &amp; 0x7F) 
        &lt;&lt; ", core dump: " &lt;&lt; ((status &gt;&gt; 7) &amp; 1) &lt;&lt; endl;
    }

    return 0;
}
```

可以看到，因为2号信号的默认处理方式是Term，因此Core Dump标志位为0且没有core文件生成

而8号信号的默认处理方式为Core，此时Core Dump标志位为1，且生成了core文件

关于core文件的使用，我们运行一段包含除零错误的代码作为例子

用gdb调试我们发生异常的可执行文件

在调试时打开core文件，就可以查看进程异常退出时收到的信号和发生异常的位置

### 2.3 特定软件条件下产生信号

在讲进程间通信时，我们认识了管道，以及管道在读端被关闭时会SIGPIPE信号，这也属于软件条件下产生信号

除此之外，我们通过alarm函数可以向进程发送SIGALRM信号即第14号信号，这也属于在特定软件条件下产生信号

```
#include &lt;unistd.h&gt;

unsigned int alarm(unsigned int seconds);

```

alarm函数的作用是在seconds秒后向进程发送SIGALRM信号，类似一个闹钟，默认动作是终止当前进程

若进程在传入函数的时间准时收到信号，则alarm函数的返回值为0，否则返回闹钟剩余的时间

验证：

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;
#include &lt;cstdlib&gt;
#include &lt;signal.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/wait.h&gt;

using namespace std;

int t;

void myhandler(int sig)
{
    cout &lt;&lt; "process get a signal, signo: " &lt;&lt; sig &lt;&lt; endl;
    t = alarm(30);
    cout &lt;&lt; t &lt;&lt; endl;
}

int main()
{
    for (int i = 1; i &lt;= 31; i++)
    {
        signal(i, myhandler);
    }
    alarm(30);
    while(true)
    {
        cout &lt;&lt; "process running..., pid: " &lt;&lt; getpid() &lt;&lt; endl;
        sleep(1);
    }
    return 0;
}
```

可以看到，当我们手动发送14号信号给进程时，闹钟还剩27秒

有没有想过，死循环运行一秒能循环多少次？

```
#include &lt;iostream&gt;
#include &lt;unistd.h&gt;

using namespace std;

int main()
{
    int cnt = 0;
    alarm(1);
    while(true)
    {
        cout &lt;&lt; "cnt = " &lt;&lt; cnt++ &lt;&lt; endl;
    }
    return 0;
}
```

进程信号（上）完.
