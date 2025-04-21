# 原创
：  【Linux】进程间通信——System V共享内存

# 【Linux】进程间通信——System V共享内存

**目录**

[一、概念和原理](#%E4%B8%80%E3%80%81%E6%A6%82%E5%BF%B5%E5%92%8C%E5%8E%9F%E7%90%86)

[二、API介绍与使用](#%E4%BA%8C%E3%80%81API%E4%BB%8B%E7%BB%8D%E4%B8%8E%E4%BD%BF%E7%94%A8)

[2.1 shmget](#2.1%20shmget)

[2.2 ftok](#2.2%20ftok)

[2.3 shmat](#2.3%20shmat)

[2.4 shmdt](#2.4%20shmdt)

[2.5 shmctl](#2.5%20shmctl)

[三、开始通信](#%E4%B8%89%E3%80%81%E5%BC%80%E5%A7%8B%E9%80%9A%E4%BF%A1)

---


## 一、概念和原理

之前提到，进程间通信的本质就是**让两个不同的进程能够看到同一份资源**。因为进程具有独立性，不同进程间无法直接的进行数据的传递，需要操作系统提供对应的资源。

前面学习的管道，就是操作系统提供的资源，两个进程打开同一个管道，就能够进行通信。

除了管道，**共享内存**也是进程间通信的一种方式，并且是**最快的方式**。其原理是**将一段物理内存映射到两个进程的地址空间**，这样两个进程就能够共享这段内存，并通过共享内存来进行数据传递，并且不再涉及内核。

进程间数据的传递不再涉及内核，因此进程在传递数据时就无需再执行对应的系统调用进入内核了，直接通过操作共享内存来进行通信，效率大大提高。

（操作系统首先申请一块共享内存，然后通过两个进程的页表将共享内存挂接到进程地址空间上）

共享内存可用于进程间通信，那么物理内存中肯定存在不止一块共享内存。既然共享内存由操作系统提供，那么我们可以猜想：操作系统一定要对这些共享内存进行管理。如何管理？**先描述再组织**

因此内核中也有用于描述共享内存的结构体，操作系统通过对结构体的组织进行共享内存的管理

System V进程间通信方式除了System V共享内存，还有**System V消息队列**和**System V 信号量**，这三种IPC方式的API和实现上都非常相似，包括内核中相似的结构体，和命名、使用方式相似的函数

System V消息队列和System V 信号量在后面的文章中会讲到，这里先贴出System V共享内存的内核结构体，后续大家可以将其与另外两种方式的内核结构体进行对比

```
struct shmid_ds {
	struct ipc_perm shm_perm; /* operation perms */
	int shm_segsz; /* size of segment (bytes) */
	__kernel_time_t shm_atime; /* last attach time */
	__kernel_time_t shm_dtime; /* last detach time */
	__kernel_time_t shm_ctime; /* last change time */
	__kernel_ipc_pid_t shm_cpid; /* pid of creator */
	__kernel_ipc_pid_t shm_lpid; /* pid of last operator */
	unsigned short shm_nattch; /* no. of current attaches */
	unsigned short shm_unused; /* compatibility */
	void* shm_unused2; /* ditto - used by DIPC */
	void* shm_unused3; /* unused */
};
```

其中ipc_perm结构体：

```
struct ipc_perm {
    key_t          __key;    /* Key supplied to shmget(2) */
    uid_t          uid;      /* Effective UID of owner */
    gid_t          gid;      /* Effective GID of owner */
    uid_t          cuid;     /* Effective UID of creator */
    gid_t          cgid;     /* Effective GID of creator */
    unsigned short mode;     /* Permissions + SHM_DEST and
                                       SHM_LOCKED flags */
    unsigned short __seq;    /* Sequence number */
};
```

---


## 二、API介绍与使用

### 2.1 shmget

```
#include &lt;sys/ipc.h&gt;
#include &lt;sys/shm.h&gt;

int shmget(key_t key, size_t size, int shmflg);
```

shmget函数用于创建共享内存，若创建成功会返回**shmid**，即**共享内存标识符**； 创建失败返回-1

其中：

key是一个**整型变量**，在内核中具有唯一性，两个进程**通过key**来访问同一块共享内存。key用于在操作系统中标识一块共享内存的唯一性，而shmid用于用户层的行为，只在进程内标识该共享内存唯一性

用户要创建key，可以使用ftok函数

### 2.2 ftok

```
#include &lt;sys/types.h&gt;
#include &lt;sys/ipc.h&gt;

key_t ftok(const char *pathname, int proj_id);

```

ftok函数用于创建共享内存的key，创建成功返回key，失败返回-1

其中pathname和proj_id由用户自由指定，函数内通过特定的算法对参数进行计算并生成对应的具有唯一性的key。而因为参数都由用户指定，所以用户可以**通过约定对应的pathname和proj_id，实现在两个进程中获取到相同的key**，从而访问到同一块共享内存。

接下来我们实践一下

shared.hpp：

```
//shared.hpp
#include &lt;iostream&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/shm.h&gt;
#include &lt;sys/ipc.h&gt;
#include &lt;string&gt;

using namespace std;

//用户自己约定
const string path = "/home/Eristic";
const int proj_id = 0x1234;

key_t GetKey()
{
    key_t key = ftok(path.c_str(), proj_id); //创建key
    if(key &lt; 0)
    {
        perror("ftok error");
        exit(1);
    }
    printf("create key success, key = %d\n", key); //打印key的值
    return key;
}

int GetSharedMem()
{
    key_t key = GetKey(); //获取key
    int shmid = shmget(key, 4096, IPC_CREAT | IPC_EXCL); //创建共享内存
    if(shmid &lt; 0)
    {
        perror("shmget error");
        exit(1);
    }
    printf("create shared memory success, shmid = %d\n", shmid); //打印shmid的值
    return shmid;
}
```

processa.cc：

```
//processa.cc
#include "shared.hpp"

int main()
{
    int shmid = GetSharedMem();
    return 0;
}
```

编译并运行程序，结果如下：

可以看到我们的key和共享内存已经创建成功了，并且key和shmid是不同的值

再次运行程序，结果变为了：

此时key创建成功，但共享内存创建失败。这是因为我们创建共享内存时权限位设置为IPC_CREAT|IPC_EXCL，如果共享内存存在就出错并返回，说明进程退出后共享内存仍然存在

实际上，**共享内存的生命周期是随内核的**，也就是除非内核重启，共享内存会一直存在直到用户主动关闭 

要查看系统中所有的共享内存，我们可以输入 ****ipcs -m****

要删除共享内存，我们可以输入**** ipcrm -m + shmid **** 

其中perms是共享内存的权限位，nattch是与该共享内存关联的进程数，size是共享内存大小

关于共享内存的大小，建议设置为4096的整数倍，因为操作系统分配内存是按照4KB分配的，即使用户将共享内存的大小设置为4097，实际大小是4096*2（虽然查看共享内存时还是显示4097）

要设置共享内存的权限，我们可以在shmget函数的shmflg参数中加上，例如：

```
int shmid = shmget(key, 4096, IPC_CREAT | IPC_EXCL | 0666);
```

删除原来的共享内存，重新编译并运行程序后，再次查看系统中的共享内存：

可以看到随着我们对shmget函数的修改，perms变为了666

并且会发现每次创建共享内存，key是保持不变的，但shmid会改变

### 2.3 shmat

```
#include &lt;sys/types.h&gt;
#include &lt;sys/shm.h&gt;

void *shmat(int shmid, const void *shmaddr, int shmflg);
```

shmat函数用于将对应的共享内存连接到进程的地址空间，成功会返回一个地址，是共享内存映射的起始地址，失败则返回-1

其中：

同样是得到一块内存空间，同样是返回值为void*，让你想到了什么？

是不是很像malloc，申请一段空间，具体的用途由用户决定，并按照用途来进行类型转换

实践一下：

```
//processa.cc
#include "shared.hpp"

int main()
{
    int shmid = GetSharedMem();
    char *shmaddr = (char *)shmat(shmid, nullptr, 0);
    sleep(10); //便于在程序退出前观测现象
    return 0;
}
```

编译并运行代码，在程序未退出时观测共享内存的nattch：

可以看到此时进程已经与共享内存关联

### 2.4 shmdt

```
#include &lt;sys/types.h&gt;
#include &lt;sys/shm.h&gt;

int shmdt(const void *shmaddr);

```

shmdt函数用于去除进程与共享内存的关联，成功返回0，失败返回-1

我们只需要将关联共享内存时返回的地址传入shmdt函数即可

我们继续在程序中加入shmdt函数，并观察现象：

```
//processa.cc
#include "shared.hpp"

int main()
{
    int shmid = GetSharedMem();
    char *shmaddr = (char *)shmat(shmid, nullptr, 0);
    printf("shmat done\n");
    sleep(5);
    shmdt(shmaddr);
    printf("shmdt done\n");
    sleep(5);
    return 0;
}
```

可以看到shmat函数执行后，共享内存的nattch变为1，shmdt去关联后又变为0

### 2.5 shmctl

```
#include &lt;sys/ipc.h&gt;
#include &lt;sys/shm.h&gt;

int shmctl(int shmid, int cmd, struct shmid_ds *buf);
```

shmctl函数用于控制共享内存，在大部分cmd操作下成功返回0，失败返回-1

其中：

我们继续加入shmctl函数，在去关联后直接删除共享内存，看看现象如何：

```
//processa.cc
#include "shared.hpp"

int main()
{
    int shmid = GetSharedMem();
    char *shmaddr = (char *)shmat(shmid, nullptr, 0);
    printf("shmat done\n");
    sleep(5);
    shmdt(shmaddr);
    printf("shmdt done\n");
    sleep(5);
    shmctl(shmid, IPC_RMID, nullptr);
    printf("shmctl done\n");
    sleep(5);
    return 0;
}
```

可以看到，由于我们选择了IPC_RMID操作，shmctl函数执行完毕后共享内存被删除

---


## 三、开始通信

到目前位置，我们已经初步了解如何创建并关联共享内存了，接下来我们来简单实现两个进程之间的通信

processa.cc：

```
#include "shared.hpp"

int main()
{
    int shmid = CreateSharedMem();
    char *shmaddr = (char *)shmat(shmid, nullptr, 0);

    while(true)
    {
        cout &lt;&lt; "process b say:" &lt;&lt; shmaddr &lt;&lt; endl;
        sleep(1);
    }

    shmdt(shmaddr);
    shmctl(shmid, IPC_RMID, nullptr);
    return 0;
}
```

processb.cc：

```
#include "shared.hpp"

int main()
{
    int shmid = GetSharedMem();
    char *shmaddr = (char *)shmat(shmid, nullptr, 0);

    while(true)
    {
        cout &lt;&lt; "Please enter# ";
        fgets(shmaddr, 4096, stdin);
    }

    shmdt(shmaddr);
    return 0;
}
```

因为创建和删除共享内存的工作在processa.cc中已经完成了，所以processb.cc中只需要获取共享内存即可，无需再进行创建和删除

shared.hpp

```
#include &lt;iostream&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/shm.h&gt;
#include &lt;sys/ipc.h&gt;
#include &lt;string&gt;
#include &lt;unistd.h&gt;

using namespace std;

//用户自己约定
const string path = "/home/Eristic";
const int proj_id = 0x1234;

key_t GetKey()
{
    key_t key = ftok(path.c_str(), proj_id); //创建key
    if(key &lt; 0)
    {
        perror("ftok error");
        exit(1);
    }
    printf("create key success, key = %d\n", key); //打印key的值
    return key;
}

int SharedMem(int flag)
{
    key_t key = GetKey(); //获取key
    int shmid = shmget(key, 4096, flag);
    if(shmid &lt; 0)
    {
        perror("shmget error");
        exit(1);
    }
    printf("create shared memory success, shmid = %d\n", shmid); //打印shmid的值
    return shmid;
}

int CreateSharedMem() //创建全新的共享内存
{
    return SharedMem(IPC_CREAT | IPC_EXCL | 0666);
}

int GetSharedMem() //获取已有的共享内存
{
    return SharedMem(IPC_CREAT);
}

```

编译并运行：

需要注意，共享内存是**没有同步互斥**之类的保护机制的，也就是说如果多个进程同时对共享内存进行读写操作可能导致冲突发生

因此，如果要实现对数据的保护，可以使用锁或者信号量等机制，或者与管道共同结合使用来让共享内存实现同步与互斥

完.
