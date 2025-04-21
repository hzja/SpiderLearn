# 原创
：  【Linux】进程间通信——System V消息队列和信号量

# 【Linux】进程间通信——System V消息队列和信号量

## 一、消息队列

### 1.1 概念

进程间通信的原理是**让不同进程看到同一份资源**，资源种类的不同就决定了通信方式的差异。如果用管道通信，则资源是文件缓冲区；如果用共享内存，则资源是内存块

消息队列是由操作系统提供的资源，其本质就是**内核中存放通信数据块的一个队列**，可供两个进程进行双向通信。

两个要进行通信的进程以数据块的形式发送数据，数据块被链入到消息队列中，并发送给目标进程

如果两个进程的数据块被存放到一个消息队列中，如何区分数据块是自己发送的还是对方进程发给自己的呢？所以**数据块需要有自己的类型**，根据类型来进行区分。

系统中存在这么多进程，因此肯定也有不止一个消息队列。既然消息队列由OS提供，那么OS必定要对消息队列进行管理。所以内核中除了有队列的结构外，一定需要其他的数据结构对消息队列进行描述和组织。

消息队列的内核结构体：

```
struct msqid_ds {
    struct ipc_perm msg_perm;     /* Ownership and permissions */
    time_t          msg_stime;    /* Time of last msgsnd(2) */
    time_t          msg_rtime;    /* Time of last msgrcv(2) */
    time_t          msg_ctime;    /* Time of last change */
    unsigned long   __msg_cbytes; /* Current number of bytes in
                                     queue (nonstandard) */
    msgqnum_t       msg_qnum;     /* Current number of messages
                                     in queue */
    msglen_t        msg_qbytes;   /* Maximum number of bytes
                                     allowed in queue */
    pid_t           msg_lspid;    /* PID of last msgsnd(2) */
    pid_t           msg_lrpid;    /* PID of last msgrcv(2) */
};
```

细心的人可能已经发现了，消息队列的内核结构体，与我们之前讲的共享内存的内核结构体十分类似，特别是**它们都有一个ipc_perm结构体**：

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

其中存放了key等非常重要的信息，说明消息队列和共享内存一样，都有自己的key来标识自己在系统中的唯一性

### 1.2 API介绍和使用

如果有读者阅读过我前面讲共享内存的文章 [【Linux】进程间通信——System V共享内存_共享内存进程间通信-CSDN博客](https://blog.csdn.net/Eristic0618/article/details/142183129)

本文讲的消息队列和信号量与前面提到的共享内存同属于System V进程间通信方式，其内核结构体、API定义和使用方式都十分相似，大家可以对比一下

#### （1）msgget

```
#include &lt;sys/types.h&gt;
#include &lt;sys/ipc.h&gt;
#include &lt;sys/msg.h&gt;

int msgget(key_t key, int msgflg);

```

msgget函数用于创建消息队列，若创建成功会返回**msqid**，即**消息队列标识符**； 创建失败返回-1

其中：

在前面讲共享内存时，用于创建共享内存的函数shmget中也有参数key和权限位flg，而用于创建消息队列的函数中也有这两个参数，并且用法也是相同的。都有系统中标识唯一性的key，都返回用户层标识唯一性的标识符。

而这里的key，也是通过ftok函数生成的，关于ftok函数我们在讲共享内存时已经讲过了。

可以看出，消息队列的接口和共享内存的接口是非常类似的，很多概念都是共通的

#### （2）msgctl

```
#include &lt;sys/types.h&gt;
#include &lt;sys/ipc.h&gt;
#include &lt;sys/msg.h&gt;

int msgctl(int msqid, int cmd, struct msqid_ds *buf);

```

msgctl函数用于控制消息队列，和共享内存的shmctl函数也是非常类似，类似到我甚至可以直接把讲共享内存时的原话修改一下放到这篇文章中

其中：

#### （3）msgsnd

```
#include &lt;sys/types.h&gt;
#include &lt;sys/ipc.h&gt;
#include &lt;sys/msg.h&gt;

int msgsnd(int msqid, const void *msgp, size_t msgsz, int msgflg);
```

这里开始就与共享内存有所不同了，共享内存需要挂接到进程的地址空间上，不用时再去掉关联；而消息队列则是**向指定消息队列中发送数据块或接收数据块**

其中：

但是说了这么多，这数据块到底长啥样？我们怎么创建一个数据块？

```
struct msgbuf {
    long mtype;       /* message type, must be &gt; 0 */
    char mtext[1];    /* message data */
};

```

这就是我们的数据块结构体，其中mtype是**数据块的类型**（必须大于0），mtext是**消息的内容**

但是为什么字符数组mtext大小只有1呢？实际上在使用时，这个结构体是需要用户自己定义的，只需要保证第一个字段是long类型第二个字段是消息内容即可，消息的大小由用户决定

所以未来我们想用消息队列发一个消息，只需要定义一个数据块结构体，然后创建对象，填充对应字段，并向msgsnd函数中传入该对象的指针即可。

#### （4）msgrcv

```
#include &lt;sys/types.h&gt;
#include &lt;sys/ipc.h&gt;
#include &lt;sys/msg.h&gt;

ssize_t msgrcv(int msqid, void *msgp, size_t msgsz, long msgtyp, int msgflg);

```

有发就有收，msgrcv函数用于从消息队列中读取数据块

其中：

#### （5）查看系统中的消息队列

通过命令 ****ipcs -q**** 查看当前所有消息队列

通过命令 ****ipcrm -q msgid**** 删除指定消息队列

## 二、信号量

### 2.1 概念

前文提到，共享内存不具有任何的保护机制，也就是说如果我们不加保护，当一个进程没有完整的把内容写入时，另一方就开始读取，可能会导致数据的收发方出现**数据不一致问题**

像这种类似的不被保护的共享资源，被多个执行流同时访问时，都可能会出现这类问题。例如我们过年抢回家的车票时，车票的余量也是共享资源，如果不加以保护，则可能会导致余票变为负数的情况（抢到车票后车票余量需要减少，这两步是分开的，所以可能导致同时抢到票的用户数量大于车票的余量，但仍然判断抢票成功）

其中一个解决方案是通过**加锁**来实现对共享资源的**互斥访问**，即**任何时刻只允许一个执行流访问共享资源**。

对于这类被多个执行流共享的，**但通过某种方式保证其互斥访问的共享资源**称为**临界资源**。例如管道也是一种临界资源。在整个程序的所有代码中，可能只有一小部分的代码访问了临界资源，这部分代码就称为**临界区**。

说了这么多，到底什么是信号量呢？

信号量（Semaphore）本质就是一个**计数器**，用于**记录临界资源中资源的数量**。临界资源能被分为多少份，则信号量为几。

> 
例如我们要看电影，自然需要先买票，只有买了票，我们才能够拥有使用电影院座位的资格。而电影院的剩余票数需要用一个计数器记录，每卖出一张票，则计数器减一，当计数器为0时就说明票已经卖光了。


电影院中的座位就是许多共享资源，而买票就是对这些座位的**预定机制**。也就是说，要具有访问共享资源的权限，首先就得申请计数器。但申请了计数器，并不代表一定访问共享资源，就像我只是买了电影票，我已经有了使用该座位的资格，不管我去不去看电影这个座位都是我的。计数器可以**有效保证进入共享资源的执行流的数量**，申请计数器就等同于“买票”。

而这个计数器，**就叫做信号量！**

有了信号量，我们就可以保证共享资源不会同时被多个执行流同时访问，避免了数据不一致问题

假设我们的**信号量初始值为1**，也就是将共享资源看作一个整体，则说明**同一时间内只有一个执行流能够申请到信号量并具有访问共享资源的资格**，实际上我们就实现了互斥。这种值只可能为1或0的信号量叫做**二元信号量**，其本质上就相当于一把锁。

到这里，大家可能还有一些疑惑。信号量既然是一个计数器，那和进程间通信又有什么关系呢？实际上进程间通信**并不仅仅是进行数据的来往**，**进程间的协同也是进程间通信的一部分**。

问题又来了，既然进程要申请信号量，信号量不也是共享资源吗？既然信号量要保证共享资源的安全，首先得保证自己是安全的。因此信号量的**申请（P）**和**释放（V）**操作都是**原子的**，即只有没做和做完了两种状态，不存在“正在做”的情况。

> 
拓展：我们能否用一个变量来代替信号量完成计数操作呢？不行！因为减少变量的值，这个操作并不是安全的。
在编程语言层面，看上去我们可以用一条语句完成减操作，但是变成汇编后则有多条语句。进程在执行这些汇编语句的过程中随时可能会被切换，存在风险
更多细节可以阅读：[Linux下信号量的P.V操作如何保证其原子性_51CTO博客_信号量 Linux](https://blog.51cto.com/ab3813/1764509)


我们来看看信号量的内核结构体：

```
struct semid_ds {
    struct ipc_perm sem_perm;  /* Ownership and permissions */
    time_t          sem_otime; /* Last semop time */
    time_t          sem_ctime; /* Last change time */
    unsigned long   sem_nsems; /* No. of semaphores in set */
};
```

同样，其内部也包含了ipc_perm结构体，这说明什么？信号量也有自己的key。也再次证明，同为System V进程间通信方式，共享内存、消息队列和信号量具有很多相似之处

### 2.2 API介绍和使用

#### （1）semget

```
#include &lt;sys/types.h&gt;
#include &lt;sys/ipc.h&gt;
#include &lt;sys/sem.h&gt;

int semget(key_t key, int nsems, int semflg);
```

semget函数用于创建一个信号量（集），如果成功将会返回该信号量集的semid，失败返回-1并设置错误码

其中：

#### （2）semctl

```
#include &lt;sys/types.h&gt;
#include &lt;sys/ipc.h&gt;
#include &lt;sys/sem.h&gt;

int semctl(int semid, int semnum, int cmd, ...);

```

semctl函数用于控制信号量集，成功会根据cmd返回一个非负值，失败返回-1并设置错误码 

如果需要，第四个参数通常被设置为union semun arg，其结构如下：

```
union semun {
    int              val;    /* SETVAL的值 */
    struct semid_ds *buf;    /* 用于IPC_STAT, IPC_SET的缓冲区 */
    unsigned short  *array;  /* 用于GETALL, SETALL的数组 */
    struct seminfo  *__buf;  /* IPC_INFO的缓冲区(Linux特有) */
};

```

 其中：

#### （3）semop

```
#include &lt;sys/types.h&gt;
#include &lt;sys/ipc.h&gt;
#include &lt;sys/sem.h&gt;

int semop(int semid, struct sembuf *sops, unsigned nsops);

```

semop函数用于设置信号量的值，成功返回0，失败返回-1并设置错误码

关于sops参数，struct sembuf的结构如下：

```
struct sembuf{
    unsigned short sem_num;  /* semaphore number */
    short          sem_op;   /* semaphore operation */
    short          sem_flg;  /* operation flags */
};
```

其中：

nsops参数指定了需要修改的信号量个数，即sops数组中的元素个数，一般我们只需要对一个信号量进行设置，所以设置为1即可

完.
