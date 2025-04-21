# 原创
：  【Linux】进程程序替换

# 【Linux】进程程序替换

**目录**

[一、原理](#%E4%B8%80%E3%80%81%E5%8E%9F%E7%90%86)

[二、程序替换函数](#%E4%BA%8C%E3%80%81%E7%A8%8B%E5%BA%8F%E6%9B%BF%E6%8D%A2%E5%87%BD%E6%95%B0)

[三、模拟实现简易版shell](#%E4%B8%89%E3%80%81%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0%E7%AE%80%E6%98%93%E7%89%88shell)

---


## 一、原理

我们可以通过fork方法创建一个子进程，但是我们为什么要创建子进程呢？

在程序中，我们往往需要子进程帮助我们执行另一个程序，但子进程又只能和父进程共享相同的代码和数据。此时就需要调用一些函数来将子进程的代码和数据**替换为新程序的代码和数据**，即**程序替换**，这些函数我们统称为exec函数

当子进程调用这些函数时，其物理内存中的代码和数据完全被新程序的代码和数据替换（先进行写时拷贝），并**从新程序的启动例程开始执行**。

所以程序替换只是替换了代码和数据，并没有创建新进程，子进程的ID也并不会改变

---


## 二、程序替换函数

一共有六种以exec开头的程序替换函数，它们分别是：

```
#include &lt;unistd.h&gt;

int execl(const char *path, const char *arg, ...);
int execlp(const char *file, const char *arg, ...);
int execle(const char *path, const char *arg, ...,char *const envp[]);
int execv(const char *path, char *const argv[]);
int execvp(const char *file, char *const argv[]);
int execve(const char *path, char *const argv[], char *const envp[]);
```

这些函数如果调用成功则执行替换后的程序，**不再返回**，如果调用出错才会返回-1。所以一旦exec函数有返回值则说明调用出错。

这些函数命名看似混乱，实际有迹可循，我们先对它们的参数进行解释：

所以函数名中的字母分别表示：

我们以execl为例，先来测试一下：

```
#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;

int main()
{
    execl("/usr/bin/ls", "ls", "-l", "-a", NULL); //命令行参数最后一个必须是NULL                                                                                                                              
    return 0;
}

```

执行这段代码，结果如下：

可以看到，我们的程序已经成功被替换为了ls命令

如果将execl函数替换为execlp（会自动在环境变量中查找），则不需要带ls命令的完整路径了，只需要传 "ls" 即可，其他函数同理。

exec系列函数体现了加载器的效果。shell本质也是一个进程，我们用shell运行程序实际上都是通过创建子进程和exec系列函数实现的

之前说过，子进程会继承父进程的环境变量，所以我们可以通过在父进程中添加环境变量的方式向子进程传递环境变量。除了这种方法，我们在execle或execve函数中还可以通过自己维护环境变量表并传参的方式来**彻底覆盖**子进程的环境变量内容。所以向函数中传参实际上并不是对子进程的环境变量进行追加，而是**覆盖**

实际上，这些函数中只有execve是真正的**系统调用**，其他五个函数都是对其的封装。

---


## 三、模拟实现简易版shell

我们汇总以前学过的知识和本文中学到的程序替换，就可以自己实现一个丐版的shell

虽然功能远远比不上真正的shell，但是其原理我们已经掌握了

完整代码：

```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/wait.h&gt;
#include &lt;assert.h&gt;

#define LABLE "#"
#define LINE_SIZE 1024
#define QUIT 0
#define ARGC_SIZE 32
#define EXIT_CODE 4

char commandline[LINE_SIZE];
char* argv[ARGC_SIZE];
int argc;
int last_code;
char pwd[LINE_SIZE];
char myenv[LINE_SIZE];

const char* gethostname() //获取主机名
{
    return getenv("HOSTNAME");
}

const char* getusername() //获取用户名
{
    return getenv("USER");
}

void getpwd() //获取工作路径
{ 
    getcwd(pwd, sizeof(pwd));
}

void printinfo() //打印命令行信息
{
    getpwd();
    printf("[%s@%s %s]"LABLE" ", getusername(), gethostname(), pwd);
}

void getcommand() //获取输入的命令
{
    char* s = fgets(commandline, sizeof(commandline), stdin);
    assert(s != NULL);
    (void)s;
    commandline[strlen(commandline)-1] = '\0'; //去掉\n
}

int parsecommand() //解析命令:将长串字符串切割为一个个选项
{
    int i = 0;
    argv[i++] = strtok(commandline, " \t");
    while(argv[i++] = strtok(NULL, " \t"));
    return i-1;
}

int ExecuteBuiltinCommands() //执行内建命令
{
    if(argc == 2 &amp;&amp; strcmp(argv[0], "cd") == 0) //cd命令
    {
        chdir(argv[1]);
        getpwd();
        sprintf(getenv("PWD"), "%s", pwd);
        return 1;
    }
    else if(argc == 2 &amp;&amp; strcmp(argv[0], "export") == 0) //export命令
    {
        strcpy(myenv, argv[1]);
        putenv(myenv);
        return 1;
    }
    else if(argc == 2 &amp;&amp; strcmp(argv[0], "echo") == 0) //echo命令
    {
        if(strcmp(argv[1], "$?") == 0) //打印上一次的退出码
        {
            printf("%d\n", last_code);
            last_code = 0;
        }
        else if(*argv[1] == '$') //判断是否要输出环境变量
        {
            char* s = getenv(argv[1]+1);
            if(s) printf("%s\n", s);
        }
        else 
            printf("%s\n", argv[1]);
        return 1;
    }
    //...
    if(strcmp(argv[0], "ls") == 0) //特殊处理
    {
        argv[argc++] = "--color"; //给不同文件加上颜色
        argv[argc] = NULL;
    }
    return 0;
}

void ExecuteRegularCommands() //执行普通命令
{
    pid_t id = fork(); //创建子进程执行命令
    if(id &lt; 0)
    {
        perror("fork error");
        return;
    }
    else if(id == 0)
    {
        //程序替换
        execvp(argv[0], argv);
        exit(EXIT_CODE);
    }
    else 
    {
        int status = 0;
        pid_t ret = waitpid(id, &amp;status, 0); //阻塞式等待
        if(ret == id) //等待成功
        {
            last_code = WEXITSTATUS(status); //保留退出码       
        }
    }
}

int main()
{
    while(!QUIT)
    {
        printinfo(); //打印命令行信息
        getcommand(); //获取输入的命令
        argc = parsecommand(); //解析命令
        if(argc == 0) continue;
        int flag = ExecuteBuiltinCommands(); //判断是否为内建命令
        if(!flag) ExecuteRegularCommands(); //执行普通命令
    }
    return 0;
}
```

部分功能测试：

完.
