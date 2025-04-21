# 原创
：  C语言之文件操作

# C语言之文件操作

**目录**

[一、文件是什么](#%E4%B8%80%E3%80%81%E6%96%87%E4%BB%B6%E6%98%AF%E4%BB%80%E4%B9%88)

[1.1 程序文件](#1.1%20%E7%A8%8B%E5%BA%8F%E6%96%87%E4%BB%B6)

[1.2 数据文件 ](#1.2%20%E6%95%B0%E6%8D%AE%E6%96%87%E4%BB%B6%C2%A0)

[1.3 文件名](#1.3%20%E6%96%87%E4%BB%B6%E5%90%8D)

[二、文件的作用](#%E4%BA%8C%E3%80%81%E6%96%87%E4%BB%B6%E7%9A%84%E4%BD%9C%E7%94%A8)

[三、二进制文件和文本文件](#%E4%B8%89%E3%80%81%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6%E5%92%8C%E6%96%87%E6%9C%AC%E6%96%87%E4%BB%B6)

[四、文件的打开和关闭](#%E5%9B%9B%E3%80%81%E6%96%87%E4%BB%B6%E7%9A%84%E6%89%93%E5%BC%80%E5%92%8C%E5%85%B3%E9%97%AD)

[4.1 流和标准流](#4.1%20%E6%B5%81%E5%92%8C%E6%A0%87%E5%87%86%E6%B5%81)

[（1）流](#%EF%BC%881%EF%BC%89%E6%B5%81)

[（2）标准流](#%EF%BC%882%EF%BC%89%E6%A0%87%E5%87%86%E6%B5%81)

[4.2 文件指针](#4.2%20%E6%96%87%E4%BB%B6%E6%8C%87%E9%92%88)

[4.3 文件的打开和关闭](#4.3%20%E6%96%87%E4%BB%B6%E7%9A%84%E6%89%93%E5%BC%80%E5%92%8C%E5%85%B3%E9%97%AD)

[（1）fopen函数](#%EF%BC%881%EF%BC%89fopen%E5%87%BD%E6%95%B0)

[（2）fclose函数](#%EF%BC%882%EF%BC%89fclose%E5%87%BD%E6%95%B0)

[（3）文件的打开模式](#%EF%BC%883%EF%BC%89%E6%96%87%E4%BB%B6%E7%9A%84%E6%89%93%E5%BC%80%E6%A8%A1%E5%BC%8F)

[五、文件的顺序读写函数介绍](#%E4%BA%94%E3%80%81%E6%96%87%E4%BB%B6%E7%9A%84%E9%A1%BA%E5%BA%8F%E8%AF%BB%E5%86%99%E5%87%BD%E6%95%B0%E4%BB%8B%E7%BB%8D)

[（1）fgetc函数](#%EF%BC%881%EF%BC%89fgetc%E5%87%BD%E6%95%B0)

[（2）fputc函数](#%EF%BC%882%EF%BC%89fputc%E5%87%BD%E6%95%B0)

[（3）fgets函数](#%EF%BC%883%EF%BC%89fgets%E5%87%BD%E6%95%B0)

[（4）fputs函数](#%EF%BC%884%EF%BC%89fputs%E5%87%BD%E6%95%B0)

[（5）fscanf函数](#%EF%BC%885%EF%BC%89fscanf%E5%87%BD%E6%95%B0)

[（6）fprintf函数](#%EF%BC%886%EF%BC%89fprintf%E5%87%BD%E6%95%B0)

[（7）fread函数](#%EF%BC%887%EF%BC%89fread%E5%87%BD%E6%95%B0)

[（8）fwrite函数](#%EF%BC%888%EF%BC%89fwrite%E5%87%BD%E6%95%B0)

[六、文件的随机读写](#%E5%85%AD%E3%80%81%E6%96%87%E4%BB%B6%E7%9A%84%E9%9A%8F%E6%9C%BA%E8%AF%BB%E5%86%99)

[6.1 fseek函数](#6.1%20fseek%E5%87%BD%E6%95%B0)

[6.2 ftell函数](#6.2%20ftell%E5%87%BD%E6%95%B0)

[6.3 rewind函数](#6.3%20rewind%E5%87%BD%E6%95%B0)

[七、文件的其他函数](#%E4%B8%83%E3%80%81%E6%96%87%E4%BB%B6%E7%9A%84%E5%85%B6%E4%BB%96%E5%87%BD%E6%95%B0)

[7.1 feof函数](#7.1%20feof%E5%87%BD%E6%95%B0)

[7.2 clearerr函数](#7.2%C2%A0clearerr%E5%87%BD%E6%95%B0)

[7.3 rename函数](#7.3%20rename%E5%87%BD%E6%95%B0)

---


## 一、文件是什么

文件是以计算机硬盘为载体，以单个名称在计算机上存储的**信息集合**。

在程序设计中，我们一般说的文件有两种：程序文件和数据文件        

### 1.1 程序文件

程序文件包括源程序文件（后缀为.c），目标文件（windows环境后缀为.obj ），可执行程序（windows环境后缀为.exe）

### 1.2 数据文件 

在本文中，我们主要讨论数据文件。

文件的内容不一定是程序，有时是**程序运行时读写的数据**，比如程序运行时需要从中读取数据或者输出内容的文件。

以前我们对数据的输入和输出都是以终端为对象的，也就是从终端的键盘输入数据，把运行的结果显示到显示器上。

但实际上我们有时候也会把信息输出到磁盘上，当需要的时候再从磁盘上读取数据到内存中使用，这里处理的就是磁盘上的数据文件。

### 1.3 文件名

一个文件要有一个唯一的文件标识，也被称为文件名，以便用户识别和引用。

文件名包含三部分：文件路径+文件名主干+文件后缀，例如：

> 
C：\ code \ 2023 \ test.txt


---


## 二、文件的作用

如果没有文件，我们写的程序的数据只能存储在电脑的内存中，如果程序退出，内存被回收，数据就丢失了。如果要将数据进行**持久化的保存**，就需要使用文件。

---


## 三、二进制文件和文本文件

根据数据的转换形式，数据文件也被称为**文本文件**或者**二进制文件**。

我们知道，数据在内存中是以二进制的形式存储的，如果对其不加转换的以二进制形式输出到文件，就是二进制文件。

如果将数据转换成ASCII码的形式存储到文件中，就是文本文件。

举个例子，如果将存储在内存中的整数10000以ASCII码的形式输出到磁盘，就是文本文件，此时磁盘中占用5个字节（每个字符的ASCII码值占一个字节）；以二进制形式输出到磁盘，就是二进制文件，在磁盘上只占4个字节。如图：

---


## 四、文件的打开和关闭

### 4.1 流和标准流

#### （1）流

程序的数据需要输出到各种外部设备，也需要从外部设备读取数据，不同的外部设备的输入输出操作各不相同，为了方便程序员对各种设备进行方便的操作，就抽象出了“**流**”的概念，我们可以把流想象成一条流淌着数据的河。

C语言针对文件、画面、键盘等的数据输入输出操作都要经过流。一般情况下，我们想读写数据，也要先打开流之后才能操作。

#### （2）标准流

但是，似乎我们平时从键盘输入数据，或者向屏幕上输出数据时并没有打开流，怎么个事呢？

这是因为C语言程序在启动的时候默认会打开3个流：

默认打开的这三个流，我们通过使用scanf、printf等函数就可以直接进行输入输出操作

这三个流的类型为 FILE* ，通常我们称为文件指针

### 4.2 文件指针

每个被使用的文件都在内存中开辟了一个相应的**文件信息区**，用来存放文件的相关信息（如文件的名字、文件状态、文件当前的位置等）。这些信息是保存在一个结构体变量中的，而该结构体变量的类型是由系统声明的，取名为**FILE**。

例如，在vs2013编译环境提供的&lt;stdio.h&gt;头文件中有以下的文件类型声明：

```
struct _iobuf {
	char* _ptr;
	int _cnt;
	char* _base;
	int _flag;
	int _file;
	int _charbuf;
	int _bufsiz;
	char* _tmpfname;
};
typedef struct _iobuf FILE;
```

不同的C语言编译器的FLIE类型包含的内容不完全相同，但大同小异。

下面我们可以尝试创建一个FILE*类型的指针变量

```
FILE* pf；//文件指针变量
```

我们定义pf是一个指向 FILE 类型数据的指针变量，可以使pf指向某个文件的文件信息区（FILE结构体变量）。通过该文件信息区中的信息就可以访问该文件，也就是说，**通过文件指针变量能够间接找到与它相关联的文件**。

### 4.3 文件的打开和关闭

#### （1）fopen函数

编写程序的时候，我们在程序中读写文件之前应该先打开文件，在使用结束之后应该关闭文件。

ANSIC规定，使用 fopen 函数来打开文件，使用 fclose 函数来关闭文件。

> 

FILE * 
fopen
 ( 
const char
 * filename, 
const char
 * mode );



fopen函数在使用后会返回一个FILE*类型的指针变量指向该文件，相当于建立了指针和文件的关系。其参数 filename 表示文件名，mode 表示文件的打开模式，这里会在后面讲

想了解更多关于fopen函数的内容请点击下方链接

[fopen - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fopen/](https://legacy.cplusplus.com/reference/cstdio/fopen/)

#### （2）fclose函数

> 

int 
fclose
 ( FILE * stream ); 



使用fclose函数后，如果文件关闭成功则返回0，如果失败则返回EOF。其参数 stream 应该为指向要关闭的文件的文件指针

想了解更多关于fclose函数的内容请点击下方链接

[fclose - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fclose/?kw=fclose](https://legacy.cplusplus.com/reference/cstdio/fclose/?kw=fclose)

#### （3）文件的打开模式

上面提到，mode表示文件的打开模式，以下都是文件的打开模式

|文件使用方式|含义|如果指定文件不存在
|------
|“r”（只读）|为了输入数据，打开一个已经存在的文本文件|出错
|“w”（只写）|为了输出数据，打开一个文本文件|建立一个新的文件
|“a”（追加）|向文本文件尾部添加数据|建立一个新的文件
|“rb”（只读）|为了输入数据，打开一个二进制文件|出错
|“wb”（只写）|为了输出数据，打开一个二进制文件|建立一个新的文件
|“ab”（追加）|向一个二进制文件尾部添加数据|建立一个新的文件
|“r+”（读写）|为读写，打开一个文本文件|出错
|“w+”（读写）|为读写，建立一个新的文件|建立一个新的文件
|“a+”（读写）|为读写打开一个文本文件，并在文件尾进行写入|建立一个新的文件
|“rb+”（读写）|为读写打开一个二进制文件|出错
|“wb+”（读写）|为读写新建一个二进制文件|建立一个新的文件
|“ab+”（读写）|为读写打开一个二进制文件，并在文件尾进行写入|建立一个新的文件

cplusplus网站中的实例代码：

```
/* fopen fclose example */
#include &lt;stdio.h&gt;
int main()
{
    FILE *pFile;
    // 打开⽂件
    pFile = fopen("myfile.txt", "w");
    // ⽂件操作
    if (pFile != NULL)
    {
        fputs("fopen example", pFile);
        // 关闭⽂件
        fclose(pFile);
    }
    return 0;
}
```

我们这里可以试着用fopen打开一个不存在的指定文件（只读模式），看看效果

---


## 五、文件的顺序读写函数介绍

|函数名|功能|适用于
|------
|fgetc|字符输入函数 |所有输入流
|fputc|字符输出函数  |所有输出流
|fgets|⽂本⾏输入函数 |所有输入流
|fputs|⽂本⾏输出函数 |所有输出流
|fscanf|格式化输出函数|所有输入流
|fprintf|格式化输入函数 |所有输出流
|fread|⼆进制输入 |文件输入流
|fwrite|⼆进制输出 |文件输出流

 上面说的适用于所有输入流一般指适用于标准输入流和其他输入流（如文件输入流）；所有输出流一般指适用于标准输出流和其他输出流（如文件输出流）。

#### （1）fgetc函数

> 
int fgetc (FILE* stream);


```
/* fgetc example: money counter */
#include &lt;stdio.h&gt;
int main()
{
    FILE *pFile;
    int c;
    int n = 0;
    pFile = fopen("myfile.txt", "r");
    if (pFile == NULL)
        perror("Error opening file");
    else
    {
        do
        {
            c = fgetc(pFile);
            if (c == '$')
                n++;
        } while (c != EOF);
        fclose(pFile);
        printf("The file contains %d dollar sign characters ($).\n", n);
    }
    return 0;
}
```

作用是从流中读取一个字符

想要了解更多关于fgetc函数的内容请点击下方链接

[fgetc - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fgetc/?kw=fgetc](https://legacy.cplusplus.com/reference/cstdio/fgetc/?kw=fgetc)

#### （2）fputc函数

> 
int fputc ( int character, FILE* stream);


```
/* fputc example: alphabet writer */
#include &lt;stdio.h&gt;

int main()
{
    FILE *pFile;
    char c;

    pFile = fopen("alphabet.txt", "w");
    if (pFile != NULL)
    {
        for (c = 'A'; c &lt;= 'Z'; c++)
            fputc(c, pFile);

        fclose(pFile);
    }
    return 0;
}
```

作用是从流中写入一个字符

想要了解更多关于fputc函数的内容请点击下方链接

[fputc - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fputc/](https://legacy.cplusplus.com/reference/cstdio/fputc/)

#### （3）fgets函数

> 
char* fgets ( char* str, int num, FILE* stream);


```
/* fgets example */
#include &lt;stdio.h&gt;

int main()
{
    FILE *pFile;
    char mystring[100];

    pFile = fopen("myfile.txt", "r");
    if (pFile == NULL)
        perror("Error opening file");
    else
    {
        if (fgets(mystring, 100, pFile) != NULL)
            puts(mystring);
        fclose(pFile);
    }
    return 0;
}
```

作用是从流中读取一个字符串

想要了解更多关于fgets函数的内容请点击下方链接

[fgets - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fgets/?kw=fgets](https://legacy.cplusplus.com/reference/cstdio/fgets/?kw=fgets)

#### （4）fputs函数

> 
int fputs ( const char* str, FILE* stream);


```
/* fputs example */
#include &lt;stdio.h&gt;

int main()
{
    FILE *pFile;
    char sentence[256];

    printf("Enter sentence to append: ");
    fgets(sentence, 256, stdin);
    pFile = fopen("mylog.txt", "a");
    fputs(sentence, pFile);
    fclose(pFile);
    return 0;
}
```

作用是从流中写入一个字符串

想要了解更多关于fputs函数的内容请点击下方链接

[fputs - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fputs/?kw=fputs](https://legacy.cplusplus.com/reference/cstdio/fputs/?kw=fputs)

#### （5）fscanf函数

> 
int fscanf ( FILE* stream , const char* format , ... );


实际上，fscanf就比scanf多了一个stream参数而已，作用是相似的

```
/* fscanf example */
#include &lt;stdio.h&gt;

int main()
{
    char str[80];
    float f;
    FILE *pFile;

    pFile = fopen("myfile.txt", "w+");
    fprintf(pFile, "%f %s", 3.1416, "PI");
    rewind(pFile);
    fscanf(pFile, "%f", &amp;f);
    fscanf(pFile, "%s", str);
    fclose(pFile);
    printf("I have read: %f and %s \n", f, str);
    return 0;
}
```

作用是格式化的读取数据

想要了解更多关于fscanf函数的内容请点击下方链接

[fscanf - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fscanf/?kw=fscanf](https://legacy.cplusplus.com/reference/cstdio/fscanf/?kw=fscanf)

#### （6）fprintf函数

> 
int fprintf ( FILE* stream , const char* format , ... );


同上，也只是比printf多了一个stream参数 

```
/* fprintf example */
#include &lt;stdio.h&gt;

int main()
{
    FILE *pFile;
    int n;
    char name[100];

    pFile = fopen("myfile.txt", "w");
    for (n = 0; n &lt; 3; n++)
    {
        puts("please, enter a name: ");
        gets(name);
        fprintf(pFile, "Name %d [%-10.10s]\n", n + 1, name);
    }
    fclose(pFile);
    return 0;
}
```

作用是写入格式化的数据

想要了解更多关于fprintf函数的内容请点击下方链接

[fprintf - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fprintf/](https://legacy.cplusplus.com/reference/cstdio/fprintf/)

#### （7）fread函数

> 
size_t fread ( void * ptr, size_t size, size_t count, FILE * stream );


想要了解更多关于fread函数的内容请点击下方链接

[fread - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fread/?kw=fread](https://legacy.cplusplus.com/reference/cstdio/fread/?kw=fread)

#### （8）fwrite函数

> 
size_t fwrite ( void * ptr, size_t size, size_t count, FILE * stream );


与上面同理，就不赘述了

想要了解更多关于fwrite函数的内容请点击下方链接

[fwrite - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fwrite/](https://legacy.cplusplus.com/reference/cstdio/fwrite/)

---


## 六、文件的随机读写

文件的随机读写并不是随机数那种随机，而是指可以从任意地方开始读写文件，这里就要引入几个函数了

### 6.1 fseek函数

 可以根据文件指针的位置和偏移量来定位文件指针

> 
int fseek ( FILE* stream , long int offset , int origin);


```
/* fseek example */
#include &lt;stdio.h&gt;

int main()
{
    FILE *pFile;
    pFile = fopen("example.txt", "wb");
    fputs("This is an apple.", pFile);
    fseek(pFile, 9, SEEK_SET);
    fputs(" sam", pFile);
    fclose(pFile);
    return 0;
}
```

 想要了解更多关于fseek函数的内容请点击下方链接

[fseek - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/fseek/?kw=fseek](https://legacy.cplusplus.com/reference/cstdio/fseek/?kw=fseek)

### 6.2 ftell函数

返回文件指针相对于起始位置的偏移量

> 
long int ftell ( FILE* stream);


```
/* ftell example : getting size of a file */
#include &lt;stdio.h&gt;

int main()
{
    FILE *pFile;
    long size;

    pFile = fopen("myfile.txt", "rb");
    if (pFile == NULL)
        perror("Error opening file");
    else
    {
        fseek(pFile, 0, SEEK_END); // non-portable
        size = ftell(pFile);
        fclose(pFile);
        printf("Size of myfile.txt: %ld bytes.\n", size);
    }
    return 0;
}
```

想要了解更多关于ftell函数的内容请点击下方链接

[ftell - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/ftell/?kw=ftell](https://legacy.cplusplus.com/reference/cstdio/ftell/?kw=ftell)

### 6.3 rewind函数

让文件指针的位置回到文件的起始位置

> 
void rewind ( FILE* stream);


```
/* rewind example */
#include &lt;stdio.h&gt;

int main()
{
    int n;
    FILE *pFile;
    char buffer[27];

    pFile = fopen("myfile.txt", "w+");
    for (n = 'A'; n &lt;= 'Z'; n++)
        fputc(n, pFile);
    rewind(pFile);
    fread(buffer, 1, 26, pFile);
    fclose(pFile);
    buffer[26] = '\0';
    puts(buffer);
    return 0;
}
```

想要了解更多关于rewind函数的内容请点击下方链接

[rewind - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/rewind/?kw=rewind](https://legacy.cplusplus.com/reference/cstdio/rewind/?kw=rewind)

---


## 七、文件的其他函数

### 7.1 feof函数

判断文件流是否读取到了文件尾

> 
int feof( FILE *stream );


```
/* feof example: byte counter */
#include &lt;stdio.h&gt;

int main()
{
    FILE *pFile;
    int n = 0;
    pFile = fopen("myfile.txt", "rb");
    if (pFile == NULL)
        perror("Error opening file");
    else
    {
        while (fgetc(pFile) != EOF)
        {
            ++n;
        }
        if (feof(pFile))
        {
            puts("End-of-File reached.");
            printf("Total number of bytes read: %d\n", n);
        }
        else
            puts("End-of-File was not reached.");
        fclose(pFile);
    }
    return 0;
}
```

想要了解更多关于feof函数的内容请点击下方链接

[feof - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/feof/?kw=feof](https://legacy.cplusplus.com/reference/cstdio/feof/?kw=feof)

### 7.2 clearerr函数

清除文件错误标志

> 
void clearerr( FILE *stream );


```
/* writing errors */
#include &lt;stdio.h&gt;
int main()
{
    FILE *pFile;
    pFile = fopen("myfile.txt", "r");
    if (pFile == NULL)
        perror("Error opening file");
    else
    {
        fputc('x', pFile);
        if (ferror(pFile))
        {
            printf("Error Writing to myfile.txt\n");
            clearerr(pFile);
        }
        fgetc(pFile);
        if (!ferror(pFile))
            printf("No errors reading myfile.txt\n");
        fclose(pFile);
    }
    return 0;
}
```

 想要了解更多关于clearerr函数的内容请点击下方链接

[clearerr - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/clearerr/?kw=clearerr](https://legacy.cplusplus.com/reference/cstdio/clearerr/?kw=clearerr)

### 7.3 rename函数

重命名文件

> 
int rename ( const char * oldname, const char * newname );


```
/* rename example */
#include &lt;stdio.h&gt;

int main()
{
    int result;
    char oldname[] = "oldname.txt";
    char newname[] = "newname.txt";
    result = rename(oldname, newname);
    if (result == 0)
        puts("File successfully renamed");
    else
        perror("Error renaming file");
    return 0;
}
```

想要了解更多关于rename函数的内容请点击下方链接

[rename - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://csdnimg.cn/release/blog_editor_html/release2.3.6/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N7T8"/>https://legacy.cplusplus.com/reference/cstdio/rename/?kw=rename](https://legacy.cplusplus.com/reference/cstdio/rename/?kw=rename)

完. 
