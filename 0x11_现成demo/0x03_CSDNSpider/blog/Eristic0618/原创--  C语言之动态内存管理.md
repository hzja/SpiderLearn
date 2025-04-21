# 原创
：  C语言之动态内存管理

# C语言之动态内存管理

## 一、引言

当我们写了一段程序，创建了一个变量或者一个数组，这些操作都需要在内存中开辟出一块空间。但是我们过去的这些操作有一定的局限性：开辟的空间大小是固定的，并且数组在申明的时候，必须指定数组的长度，数组空间一旦确定大小就无法再调整了。

虽然在某些编译器（例如gcc）中。允许我们使用一个变量来指定数组的大小，但是在大部分编译器中这种变长数组都是不允许的。所以C语言引入了动态内存的开辟方式，让程序员可以自己申请和释放空间，这种方法就比较的灵活了。

---


## 二、malloc函数和free函数

### 2.1 malloc函数

首先明确一点：在使用动态内存管理函数的时候要包含头文件 **&lt;stdlib.h&gt;**

C语言给我们提供了这么一个动态内存开辟的函数：

> 
void* malloc ( size_t size );


这个函数会向内存中申请一块**连续可用**的空间，并且返回指向这块空间的指针

**注意！**

### 2.2 free函数

为什么要把malloc和free放在一起讲呢？当你未来在写代码时使用了malloc函数或者其他动态内存管理函数的时候，就必须要用到free函数，接下来我们具体讲解一下

free函数是C语言专门用来做动态内存的释放和回收的函数，其原型如下：

> 
void free ( void* ptr );


free函数可以用来释放我们通过malloc动态开辟的内存空间，如果一块动态开辟的内存空间没有被free函数释放的话，就会造成内存泄漏

**注意！**

free函数和malloc函数一样要通过&lt;stdlib.h&gt;头文件声明

学会了这两个函数之后，我们就可以开始练习写代码了

```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main()
{
	int *arr = (int *)malloc(sizeof(int) * 10);
	if (arr == NULL)
	{
		perror("malloc fail");
		return 1;
	}
	free(arr);
	arr = NULL; // 为什么要置空?
	return 0;
}
```

上面，指针arr指向了我们动态开辟的一块40个字节的空间，然后我们free掉这一块空间后，又给arr置空了，为什么要这么做呢？

实际上，arr指向的空间被释放掉后就变成了野指针，为了防止错误的操作，我们就对其进行置空防止后续有人错误使用

---


## 三、calloc函数

C语言还提供了calloc函数用来进行动态内存分配，这个函数也和malloc很相似

> 
void* calloc ( size_t num , size_t size );


calloc函数可以为 num 个大小为 size 的元素开辟一块空间，并且把这块空间的每个字节都初始化为0，这也是它和malloc最大的区别

例如：

```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main()
{
	int *arr = (int *)calloc(10, sizeof(int));
	if (arr == NULL)
	{
		perror("calloc fail");
		return 1;
	}
	free(arr);
	arr = NULL;
	return 0;
}
```

输出结果为

所以如果我们需要对动态开辟的内存初始化的话，calloc是更好的选择

---


## 四、realloc函数

动态内存管理就是让我们更加自由的去开辟内存，但是光看上面几个函数似乎还不够自由。这里就引入一个动态内存管理的好帮手：realloc函数。这个函数的出现让动态内存管理更加灵活。

当我们动态开辟内存之后，有时会发现开辟出的空间太小了不够用，有时又会发现开辟出的空间太大了有点浪费。为了合理的使用内存，对内存的大小做灵活的调整，就需要使用realloc函数来对动态开辟的内存大小进行调整。

> 
void* realloc ( void* ptr , size_t size );


其中，ptr 是待调整大小的内存空间的地址，size 是**调整之后的新大小**，返回值是调整后的内存的起始位置地址。

realloc在调整内存空间时存在两种情况：
1. 原空间后面有足够大的空间，可以在原有内存之后直接增加新的空间，原空间的数据不发生变化1. 原空间后面没有足够大的空间，就会在内存的堆区重新找一块能够容纳新空间的位置，同时把旧空间的数据拷贝到新空间，然后对旧空间进行释放并返回新空间的起始地址
这里引入一个问题：下面的代码1和代码2哪个更好呢？

```
//代码1
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main()
{
	int *arr = (int *)malloc(sizeof(int) * 10);
	arr = (int *)realloc(arr, 1000);
	free(arr);
	arr = NULL;
	return 0;
}
```

```
//代码2
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main()
{
	int *arr = (int *)malloc(sizeof(int) * 10);
	int *tmp = (int *)realloc(arr, 1000);
	if(tmp!=NULL)
	{
		arr = tmp;
	}
	free(arr);
	arr = NULL;
	return 0;
}
```

代码2更好。实际上，当我们使用realloc函数调整动态开辟的内存大小的时候，是存在失败的可能的。如果我们直接对指向原空间的指针来进行调整，一旦失败则会返回NULL，指针无法再指向原空间，则原空间就无法被释放，造成内存泄漏

所以在代码2中，我们使用一个tmp指针来进行调整，调整成功后再赋给arr，这样就更保险。

## 五、常见的动态内存管理的错误

### 5.1 对NULL指针的解引用操作

```
void test()
{
	int *arr = (int *)malloc(sizeof(int) * 10);
	*arr = 20;
	free(arr);
}
```

如果malloc开辟失败，则arr的值为NULL，再对其解引用就会造成错误

所以使用malloc、calloc、realloc等函数的时候，最好增加一个检测环节避免对NULL指针错误使用

### 5.2 对动态开辟空间的越界访问

```
void test()
{
	int i = 0;
	int *p = (int *)malloc(10 * sizeof(int));
	if (NULL == p)
	{
		exit(EXIT_FAILURE);
	}
	for (i = 0; i &lt;= 10; i++)
	{
		*(p + i) = i; // 当i是10的时候越界访问
	}
	free(p);
}
```

我们用malloc开辟了一块10个sizeof(int)的空间，但是在循环中却访问了第11个位置，属于越界访问，也是错误的做法

### 5.3 对非动态开辟的内存使用free释放

上面提到过，只有动态开辟的内存才能用free将其释放，如果我们用free释放非动态开辟的内存就会造成错误，如下：

```
void test()
{
	int i = 0;
	int *p = &amp;i;
	free(p);
}
```

### 5.4 使用free不完全释放动态开辟的内存

```
void test()
{
	int *p = (int *)malloc(100);
	p++;
	free(p);
}
```

如上，p++之后不再指向这块动态开辟的空间的起始地址，所以free函数无法对其完全释放。所以当我们使用free函数释放内存的时候需要注意指针是否指向这块内存的起始位置。

### 5.5 对一块动态内存重复释放

```
void test()
{
	int *p = (int *)malloc(100);
	free(p);
	free(p);
}
```

对已经被释放的动态内存进行二次释放也是错误的做法

### 5.6 不释放动态开辟的内存

前面说过当我们动态开辟了一块内存之后，一定要在程序中的某个位置把它free掉，不然就会造成内存泄漏

## 六、柔性数组

在C99中，结构体的最后一个成员允许是位置大小的数组，这个就叫柔性数组成员

例如：

```
typedef struct
{
	int i;
	int a[0];//柔性数组成员
} type_a;
```

当然这么做有些编译器会报错，可以改成

```
typedef struct
{
	int i;
	int a[];
} type_a;
```

柔性数组的特点有：

我们可以看看上面那个结构体的大小是多少

可以看到刚好是第一个成员的大小，不包含下面的柔性数组成员

完.
