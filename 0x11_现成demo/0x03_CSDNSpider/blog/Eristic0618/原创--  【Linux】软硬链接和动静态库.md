# 原创
：  【Linux】软硬链接和动静态库

# 【Linux】软硬链接和动静态库

## 一、软链接和硬链接

### 1.1 软链接

在Linux中，我们可能会看到这种文件：

这就是**软链接**，又称为**符号链接**（Symbolic Link）

说完了表象我们来看本质。可以看到上面的软链接好像是一个文件指向了另一个文件，而实际上也确实是这样的。软链接是一个**独立的文件**，有**独立的inode**，其数据块中存放的是**指向的文件的路径**。

这么一说，你可能会想到什么。没错，我们可以把软链接理解成Windows的**快捷方式**

要创建一个软链接也十分简单，命令为** **ln -s 指向的文件路径 软链接名** **，例如：

可以看到，创建的软链接在相比于普通文件，权限位前面的字符从“-”变成了“l”， 代表软链接

并且，软链接的inode和指向文件的inode是不一样的，这也能说明软链接是一个独立的文件

前面提到，软链接内部存放的是指向文件的路径，那如果我们把指向的文件删除会发生什么呢？

删除指向的文件后软链接仍然存在，但已经是一个无效的软链接了，所以软链接与指向的文件是**从属关系**，指向的文件不存在了，软链接也就无效了

要删除一个软链接也很简单，命令为** **unlink 软链接****

软链接有什么作用呢？显而易见，我们平时使用的快捷方式有什么用，软链接就有什么用

### 1.2 硬链接

相比于软链接是一个独立的文件，我们在创建**硬链接**时**不会生成一个新的文件**，硬链接会与其指向的文件**共用同一个inode**

简单来说，硬链接就是给文件起别名，虽然文件名不同，但硬链接与指向的文件的inode是相同的，即一个inode对应两个或多个不同的文件名

创建一个硬链接的方式与软链接类似，通过命令**** ln 指向的文件路径 硬链接名 ****即可创建硬链接：

可以看到，权限位后的数字也由1变为了2，实际上这个数字就是**硬链接数**，在我们创建了一个指向file.txt的硬链接后，硬链接数也增加了。因为二者的inode是一样的，所以拥有相同的硬链接数

此时我们分别打印file.txt和硬链接的内容，可以看到是一样的

此时我们删除file.txt，会发生什么呢？

可以看到，硬链接依然能够被访问，此时硬链接数重新变为1。所以硬链接和指向的文件是**平等的关系**，删除任何一个都不会影响另一个的访问，且当硬链接数大于0时文件不会被销毁

要理解硬链接的本质也很简单，前面在学习Linux文件系统时我们提到过，目录的数据块中存放的其实是**文件名与inode的映射关系**。所谓的建立硬链接，本质上就是在特定目录的数据块中新增一个文件名与inode的映射即可

我们知道，目录中有两个隐藏目录，分别指向当前目录和上级目录，例如我们创建一个新文件夹

可以看到，里面的两个隐藏目录，“.”指向当前目录，“..”指向上级目录，这两个隐藏目录实际上**也是硬链接**

接着我们返回上级目录，可以看到上级目录中的两个inode和刚刚我们看到的两个隐藏目录的inode是一致的，这也能印证隐藏目录是硬链接的结论

正因如此，我们创建一个新的目录文件时，其硬链接数**天然就是2**，正是因为其内部的两个隐藏目录中有一个指向自己

硬链接通常用于进行路径定位，例如上面的隐藏目录，采用硬链接的方式就可以进行路径间切换

但是我们会发现，Linux并不允许我们**自行对目录建立硬链接**，为什么？

这是因为Linux中的目录结构是一颗多叉树，如果用户擅自对目录建立硬链接容易让结构带环，从而可能在进行查找等操作时导致系统级的bug

你问我隐藏目录难道不也是带环？这是Linux系统自带的，和用户能一样吗

## 二、动态库和静态库

### 2.1 库的概念

库是一种可执行代码的**二进制形式**，是写好的、成熟的、可以复用的代码。库和可执行文件的区别在于，库不是独立程序，而是向其他程序提供服务的代码

就比如，我们写了一段代码可以实现某种功能，如果将其封装成一个库，下次要用到该功能就无需重复写这段代码，直接使用库里的代码即可

根据源代码是否公开，又分为**开源库**和**闭源库**。开源库就是直接将源代码发布出去，别人能够看到代码的具体实现；闭源库则是不公开源代码，而是发布源代码编译后的二进制文件，别人看不到代码的具体实现

闭源库又分为**动态库**和**静态库**，相对的，在与程序链接时也分为**动态链接**和**静态链接**，动态链接只能链接动态库，静态链接只能链接静态库

静态库在Linux和Windows下的后缀分别是**.a**和**.lib**，动态库在Linux和Windows下的后缀分别是**.so**和**.dll**

我们回顾一下，将一个程序编译为可执行程序分为四步：预编译、编译、汇编、链接，其中动态库和静态库就在链接阶段通过动态链接、静态链接和其他文件一起链接成一个可执行程序

### 2.2 静态链接和静态库

静态链接是指链接器在链接时**将库的内容全部加入到可执行程序中**的做法，程序在链接完之后本身就拥有了静态库的内容，不再需要二次链接静态库

静态库既然可以与汇编后生成的目标文件一起链接为同一个可执行程序，那么二者的格式必定是类似的。其实，静态库可以简单看作是**一组目标文件（.o/.obj文件）的集合**

要验证这一点也很简单，我们可以自己手动封装一个静态库

首先，我们得先写几个功能，将他们编译为.o文件，例如我们写两个实现了加法和减法的程序：

```
//add.h
int add(int x, int y);
```

```
//add.c
#include "add.h"

int add(int x, int y)
{
    return x + y;
}
```

```
//sub.h
int sub(int x, int y);
```

```
//sub.c
#include "sub.h"

int sub(int x, int y)
{
    return x - y;
}
```

然后在程序中调用这两个库函数：

```
//main.c
#include &lt;stdio.h&gt;
#include "add.h"
#include "sub.h"

int main()
{
    int a = 20;
    int b = 10;
    printf("a + b = %d\n", add(a, b));
    printf("a - b = %d\n", sub(a, b));
    return 0;
}
```

此时我们有了五个文件

要把这两个功能的源代码打包成静态库，还需要进行一些前置工作，即让这两份源代码编译为目标文件

然后通过ar工具输入命令 ****ar -rc 静态库名 目标文件**** 即可将多个.o文件打包成静态库

需要注意，静态库的命名格式要严格遵守** lib+库名+.a **的规范，lib为前缀，中间是静态库名，后缀为.a

封装好静态库后，我们要使用静态库，需要在编译时指定**头文件路径**、**静态库路径**和**静态库名**

因为此处我们的源文件与头文件位于同一目录下，而头文件的检索会默认在当前目录中进行，所以可以不用指定头文件路径，但静态库路径和静态库名还是需要的

其中，-I指定头文件路径，-L指定库路径，-l指定库名

但是如果当我们将main.c移动到当前目录的子目录中，此时源文件与头文件不在同一目录下，如果不带头文件路径就无法成功编译：

但是我们指定了头文件路径后就可以正常编译了

前面提到，在链接静态库后，可执行程序内部包含了静态库的内容，后续使用中就无需再依赖该静态库了。那么我们将静态库删掉，可执行程序还能否正常运行呢？

可以看到，即使静态库被删除，可执行程序依然能够正常运行

有人可能又要问了，为什么我们平时用语言给我们提供的库函数和头文件，不需要带头文件路径、库路径和库名呢？

如果在使用第三方库时不想带头文件路径和库文件路径，则需要把头文件和库文件拷贝到系统路径底下，例如：

像这样，把我们自己的头文件和库文件拷贝到系统的头文件路径和库文件路径下

但是即便这样，在编译时我们还是需要带上库名，这是使用第三方库时的必要条件

将第三方头文件和库文件拷贝到系统路径下的过程，叫做**库的安装**

静态库的**优缺点**都很明显，优点在于目标文件与静态库链接并编译出可执行程序后不再依赖静态库，可以独立于静态库运行；缺点在于因为静态库的代码完整的拷贝到了程序中，称为可执行程序的一部分，所以会导致可执行文件较大，且运行时占用内存多。除了空间浪费，一旦静态库进行更新，所有使用这个静态库的程序都需要重新编译发布

如果把用户运行程序比作上网，那么静态库就是一家卖电脑的数码店，链接静态库就是从这家店买了一台电脑，不管后续这家店是否倒闭，电脑都在我们自己手上，依然可以正常的上网。但是每台电脑都是我们的私人财产，别人要想上网只能再买一台电脑。

### 2.3 动态链接和动态库

前面的比喻放在动态库依然适用，如果说静态库是电脑店，那么动态库就是网吧，用户每次要上网（运行程序）必须跑到网吧（静态库）才能进行，如果网吧倒闭，那么也就上不了网了，但是网吧里面同一台电脑可以让多个人共享使用。

相比静态库，动态库在程序编译时**不会被链接到可执行程序中**，而是在程序**开始运行且调用库函数时才被载入到内存**。

并且，不同的程序如果调用相同的动态库，那么只需要在内存中载入一份动态库的实例，不同的程序再通过页表将动态库映射到自己的**共享区**当中即可访问同一个动态库的内容

与创建静态库不同，动态库的创建不需要使用其他工具，**使用编译器**即可创建动态库

创建动态库之前也需要进行一些前置准备，将源文件编译为.o文件

这里需要注意加上编译器选项**-fPIC**，目的是生成**地址无关码**，这里后面会提到

然后生成动态库，命令为**** gcc -shared -o 动态库名 目标文件****

可以看到相比静态库，动态库多了**可执行权限**

这是因为静态库不需要被加载到内存，而动态库在使用时需要被加载到内存中，所以需要可执行权限。动态库虽然没有main函数，但是也具有可执行程序的特征，只是不能单独执行

接着我们进入目录dir，用之前链接静态库的方式编译目标源文件

但是运行生成的可执行程序时，却发现报错了

此时我们查看可执行程序链接的动态库，会发现我们自己的动态库找不到！

为什么加载时系统或语言提供的库就能找到，我们自己的动态库就找不到呢？我不是把路径什么的都告诉编译器了吗？

因为不仅编译时要告诉编译器路径，**在加载时也需要让加载器知道动态库的路径**！

要解决加载时找不到动态库的情况，方法也有很多。系统在加载时会默认在某些路径下搜索动态库，我们可以把动态库通过**拷贝**或在系统默认的库路径**/lib64**或**/usr/lib64**下**创建软链接**的方式让系统在加载时也能够找到我们的动态库，例如：

同时我们也可以看到在该路径下也的确有我们创建的软链接

除此之外，我们还可以将我们动态库所在的路径，添加到系统的环境变量LD_LIBRARY_PATH中

我们还可以在**/ect/ld.so.conf.d**路径下创建一个配置文件，在文件中写入自己的动态库路径，并输入**ldconfig**重新加载配置文件

以上几种方法，都可以让我们在加载时找到动态库的位置

## 三、重谈进程地址空间(地址无关码)

前面提到，动态库在运行时需要被加载到内存中，并且可能同时被多个进程共享。也就是说动态库在加载后可以**被所有进程共享**

至于库中的全局变量也很好理解，当多个进程同时修改一个全局变量时，就会触发写时拷贝

一个程序要用到动态库时，先将动态库加载到内存中，然后通过页表映射到自己进程地址空间的共享区中，并直接从代码段跳转到共享区中执行，执行完后再返回正文代码继续执行即可

实际中，程序编译成指令后，函数名已经变为一个个地址了，每条指令都有属于自己的逻辑地址

并且虽然每条指令的长度都各不相同，只要我们知道了程序的起始地址，和每条指令的长度，就可以一直执行下去，或者跳转到其他函数的位置。

程序的起始地址会被记录在**Entry point address**（入口地址）中，在编译期间就已经形成，所以这个地址只有可能是**逻辑地址**，不可能是物理地址。

CPU中有个**EIP/PC寄存器**，用于存储下一条要读取指令的地址。在运行一个程序时，PCB创建完毕，将入口地址加载到寄存器中，并通过寄存器中的地址在页表中进行查找。如果没有找到说明对应的程序还没有被加载到内存当中，触发**缺页中断**。当程序加载到内存中后，物理地址也就有了，同时页表中也建立了映射，就找到了对应的代码。

寄存器当中的地址不断的增加偏移量，也就一步步找到了后续的指令，这些指令中不仅有代码，还可能有地址（跳转到其他函数），指令中的地址是编译时就固定的，所以也是虚拟地址。虚拟地址只是用于指令间的寻址，最终在内存中执行指令还是得映射为物理地址，所以对于这些虚拟地址我们依旧是通过页表来访问物理内存，如果没有则缺页中断即可。

通过入口地址找到第一条指令，将程序载入内存并建立页表映射，执行指令，读取到地址并访问页表的一套环形逻辑，程序就能顺着这个逻辑一路向下运行。

接下来就是**动态库的加载**，前面提到过函数在编译后，其位置是一个被硬编码的地址，所以在动态库加载到内存中，被映射到地址空间的共享区后，我们依旧需要通过这个地址来找到对应的函数。

但是一个程序的共享区中可能同时加载了多个动态库，这么多的库就无法保证一个库能够刚好保证其函数被加载到对应的位置了，所以我们要让动态库可以**在共享区中任意位置加载**

但是虽然动态库可以在任意位置加载，但函数的位置是被硬编码不能改变的，我们又如何能够找到呢？

实际上，函数被编译后形成的地址不是虚拟地址，而是相对于整个动态库的偏移量。通过这种方式，我们只需要知道动态库的起始地址，通过偏移量就能找到其所有函数的位置了

所以前面提到的，所谓的**地址无关码**，就是**直接用偏移量对库中函数进行编址**

如有错误欢迎在评论区指出

完.
