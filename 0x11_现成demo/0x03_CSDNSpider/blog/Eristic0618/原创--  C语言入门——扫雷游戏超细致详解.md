# 原创
：  C语言入门——扫雷游戏超细致详解

# C语言入门——扫雷游戏超细致详解

本篇文章面向已经对C语言有了一定了解的同学，需要用到的知识有数组、自定义函数、函数嵌套、各类循环语句和分支语句，srand函数和rand函数、宏定义、自定义头文件等。今天我们将从头开始，对扫雷游戏的基本程序的实现思路作一个细致的了解。

首先我们创建一个.c文件，文件名可以按照自己喜好设定，我这里命名为test.c

我们先对主程序的内容进行构思，先把最基本的部分完成。

```
//test.c
int main()
{
    return 0;
}
```

然后我们使用do-while循环，目的是无论如何程序都至少执行一次。

```
//test.c
int main()
{
    do
    {
        
    } while ();   
    return 0;
}
```

要运行游戏，首先我们得有一个基本的ui，这里我们写一个menu函数来帮助我们实现打印一个游戏ui的功能。因为不需要返回值，所以menu函数的类型应该是void。

```
//test.c
void menu()
{
    printf("**********************\n");
    printf("****    1.play   *****\n");
    printf("****    0.exit   *****\n");
    printf("**********************\n");
}

int main()
{
    do
    {
        menu();
    } while ();   
    return 0;
}
```

打印完游戏ui之后，我们需要输入值来选择开始游戏还是退出游戏，所以要设定一个变量，并输入值。当然在输入值之前我们得提醒使用程序的人此时应该输入一个值。因为输入的值决定了程序是否继续运行，所以在while的条件判断语句中我们应放入这个值。

```
//test.c
void menu()
{
    printf("**********************\n");
    printf("****    1.play   *****\n");
    printf("****    0.exit   *****\n");
    printf("**********************\n");
}

int main()
{
    int input;
    do
    {
        menu();
        printf("请选择:&gt; ");
        scanf("%d", &amp;input);
    } while (input);   
    return 0;
}
```

输入了值之后，我们就要使用分支语句来进行不同情况的程序设计。当输入了1时我们打印“开始游戏”并执行游戏程序，当输入0时我们打印“游戏结束”并终止程序，当输入了其他值的时候我们打印“非法操作，请重新输入”并要求玩家重新输入值。这样我们就完成了所有可能性的程序设计。

```
//test.c
void menu()
{
    printf("**********************\n");
    printf("****    1.play   *****\n");
    printf("****    0.exit   *****\n");
    printf("**********************\n");
}

int main()
{
    int input;
    do
    {
        menu();
        printf("请选择:&gt; ");
        scanf("%d", &amp;input);
        switch (input)
        {
        case 1:
        {
            printf("开始游戏\n");
            game();
            break;
        }
        case 0:
        {
            printf("游戏结束\n");
            break;
        }
        default:
        {
            printf("非法操作，请重新输入\n");
            break;
        }
        }
    } while (input);   
    return 0;
}
```

此时你会发现，case 1中有一个没见过的函数——game，这其实是我们自定义的一个函数，目的是实现游戏的各项功能，现在我们就在menu函数下边完成这个函数。因为不需要返回值所以game函数的类型也是void。

```
//test.c
void menu()
{
    printf("**********************\n");
    printf("****    1.play   *****\n");
    printf("****    0.exit   *****\n");
    printf("**********************\n");
}

void game()
{

}

int main()
{
    int input;
    do
    {
        menu();
        printf("请选择:&gt; ");
        scanf("%d", &amp;input);
        switch (input)
        {
        case 1:
        {
            printf("开始游戏\n");
            game();
            break;
        }
        case 0:
        {
            printf("游戏结束\n");
            break;
        }
        default:
        {
            printf("非法操作，请重新输入\n");
            break;
        }
        }
    } while (input);   
    return 0;
}
```

扫雷的棋盘有行数和列数，你会发现这和二维数组十分相似，所以我们创建两个二维数组来存储棋盘的数据，一个二维数组用来存放地雷（这里我们用字符‘1’作为地雷，则字符‘0’就是没有地雷），另一个二维数组我们作为游戏ui，所以数组中存放的都是‘*’字符。

因为我们这次只设计初阶扫雷游戏的程序，所以棋盘大小是9*9，但是实际上我们需要定义一个11*11的二维数组，这里我们后续会知道原因。

```
//test.c
void menu()
{
    printf("**********************\n");
    printf("****    1.play   *****\n");
    printf("****    0.exit   *****\n");
    printf("**********************\n");
}

void game()
{
    // 创建一个地雷二维数组和一个面板二维数组
    char mine[ROWS][LINES];
    char show[ROWS][LINES];
}

int main()
{
    int input;
    do
    {
        menu();
        printf("请选择:&gt; ");
        scanf("%d", &amp;input);
        switch (input)
        {
        case 1:
        {
            printf("开始游戏\n");
            game();
            break;
        }
        case 0:
        {
            printf("游戏结束\n");
            break;
        }
        default:
        {
            printf("非法操作，请重新输入\n");
            break;
        }
        }
    } while (input);   
    return 0;
}
```

写到这里，我们不得不创建一个.h文件来开始头文件的自定义了，因为game函数中用到了若干个常量，我们可以在自定义头文件中使用define定义这些常量，并且程序用到的库函数的头文件我们也可以包含在自定义头文件中。这里我把自定义头文件命名为func.h并在test.c中声明。

```
//func.h
#pragma once

#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;time.h&gt;

#define ROW 9  // 游戏棋盘行数
#define LINE 9 // 游戏棋盘列数

#define ROWS ROW + 2   // 实际数组行数
#define LINES LINE + 2 // 实际数组列数

#define MINES 10 //地雷数量
```

自定义完头文件，我们继续在test.c中完成game函数的内容。创建完数组之后，我们就要初始化数组内容，具体操作是将地雷数组的元素全部变成字符'0'，将面板数组的元素全部变成字符'*'。这里我们再写一个函数从而在game函数中实现这个功能。此时我们再创建一个.c文件用来存放我们自定义的函数，这里命名为func.c

我将函数命名为Initialize_Array，不需要返回数值则类型为void，向函数传输的实参分别为数组，ROWS,LINES和用来初始化的字符。

```
//test.c
#include "func.h"
#include "func.c"

void menu()
{
    printf("**********************\n");
    printf("****    1.play   *****\n");
    printf("****    0.exit   *****\n");
    printf("**********************\n");
}

void game()
{
    // 创建一个地雷二维数组和一个面板二维数组
    char mine[ROWS][LINES];
    char show[ROWS][LINES];

    Initialize_Array(mine, ROWS, LINES, '0'); // 初始化地雷二维数组
    Initialize_Array(show, ROWS, LINES, '*'); // 初始化面板二维数组
}

int main()
{
    int input;
    do
    {
        menu();
        printf("请选择:&gt; ");
        scanf("%d", &amp;input);
        switch (input)
        {
        case 1:
        {
            printf("开始游戏\n");
            game();
            break;
        }
        case 0:
        {
            printf("游戏结束\n");
            break;
        }
        default:
        {
            printf("非法操作，请重新输入\n");
            break;
        }
        }
    } while (input);   
    return 0;
}
```

```
//func.c
#include "func.h"

void Initialize_Array(char arr[ROWS][LINES], int x, int y, char var)
{

}
```

 接着我们使用for循环逐步自定义数组元素

```
//func.c
#include "func.h"

void Initialize_Array(char arr[ROWS][LINES], int x, int y, char var)
{
    for (int i = 0; i &lt; x; i++)
    {
        for (int j = 0; j &lt; y; j++)
        {
            arr[i][j] = var;
        }
    }
}
```

这样我们就完成了Initialize_Array函数的自定义，可以正常的初始化二维数组了。

接下来我们自定义一个函数帮助我们打印数组，一是可以作为游戏ui，二是方便调试程序是否正常运行。这里我将函数命名为Print_Array，不返回数值所以类型还是void，传输的实参分别为数组，ROW和LINE（注意辨别ROW、ROWS和LINE、LINES）

```
//test.c
#include "func.h"
#include "func.c"

void menu()
{
    printf("**********************\n");
    printf("****    1.play   *****\n");
    printf("****    0.exit   *****\n");
    printf("**********************\n");
}

void game()
{
    // 创建一个地雷二维数组和一个面板二维数组
    char mine[ROWS][LINES];
    char show[ROWS][LINES];

    Initialize_Array(mine, ROWS, LINES, '0'); // 初始化地雷二维数组
    Initialize_Array(show, ROWS, LINES, '*'); // 初始化面板二维数组

    Print_Array(mine, ROW, LINE); // 打印地雷二维数组
    Print_Array(show, ROW, LINE); // 打印面板二维数组
}

int main()
{
    int input;
    do
    {
        menu();
        printf("请选择:&gt; ");
        scanf("%d", &amp;input);
        switch (input)
        {
        case 1:
        {
            printf("开始游戏\n");
            game();
            break;
        }
        case 0:
        {
            printf("游戏结束\n");
            break;
        }
        default:
        {
            printf("非法操作，请重新输入\n");
            break;
        }
        }
    } while (input);   
    return 0;
}
```

```
//func.c
#include "func.h"

void Initialize_Array(char arr[ROWS][LINES], int x, int y, char var)
{
    for (int i = 0; i &lt; x; i++)
    {
        for (int j = 0; j &lt; y; j++)
        {
            arr[i][j] = var;
        }
    }
}

void Print_Array(char arr1[ROWS][LINES], int x, int y)
{

}
```

因为在扫雷游戏中，如果有行数和列数的指引我们会更好地判断坐标（效果如下）

所以首先在第一行打印出列数，接着后面每一行都打印出行数，这个程序很好实现这里就不再赘述了 

```
//func.c
#include "func.h"

void Initialize_Array(char arr[ROWS][LINES], int x, int y, char var)
{
    for (int i = 0; i &lt; x; i++)
    {
        for (int j = 0; j &lt; y; j++)
        {
            arr[i][j] = var;
        }
    }
}

void Print_Array(char arr1[ROWS][LINES], int x, int y)
{
    for (int n = 0; n &lt;= x; n++)
    {
        printf("%d ", n);
    }
    printf("\n");
    for (int i = 1; i &lt;= x; i++)
    {
        printf("%d ", i);
        for (int j = 1; j &lt;= y; j++)
        {
            printf("%c ", arr1[i][j]);
        }
        printf("\n");
    }
}
```

在这里我们就可以运行一下代码，通过打印出的内容来判断程序是否出现bug了。不过在此之前需要在func.h中声明刚刚我们在func.c中创建的函数才能正常使用函数。

```
//func.h
#pragma once

#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;time.h&gt;

#define ROW 9  // 游戏棋盘行数
#define LINE 9 // 游戏棋盘列数

#define ROWS ROW + 2   // 实际数组行数
#define LINES LINE + 2 // 实际数组列数

#define MINES 10 //地雷数量

void Initialize_Array(char arr[ROWS][LINES], int x, int y, char var);

void Print_Array(char arr1[ROWS][LINES], int x, int y);
```

运行完代码，没有出现问题，那么我们就可以开始随机设置地雷了。这里我们依旧是创建一个函数实现这个功能，这里我将函数命名为Set_mine，仍然不需要返回数值所以类型为void，传递的实参有数组，ROW和LINE。

因为前面说过，我们将字符'1'作为有地雷的标志，所以随机设置地雷的实现手段就是随机挑选若干个数组元素，将字符‘0’替换成字符‘1’即可。其中我们需要使用srand函数和rand函数来获取1-9的随机数（游戏中的行列范围也是1-9），并将地雷数作为替换字符的次数。明白这些后设计程序便是信手拈来了。

首先我们在test.c中使用srand函数并用时间戳作为种子。

```
//test.c
#include "func.h"
#include "func.c"

void menu()
{
    printf("**********************\n");
    printf("****    1.play   *****\n");
    printf("****    0.exit   *****\n");
    printf("**********************\n");
}

void game()
{
    // 创建一个地雷二维数组和一个面板二维数组
    char mine[ROWS][LINES];
    char show[ROWS][LINES];

    Initialize_Array(mine, ROWS, LINES, '0'); // 初始化地雷二维数组
    Initialize_Array(show, ROWS, LINES, '*'); // 初始化面板二维数组

    Print_Array(mine, ROW, LINE); // 打印地雷二维数组
    Print_Array(show, ROW, LINE); // 打印面板二维数组
}

int main()
{
    int input;
    srand((unsigned int)time(NULL));
    do
    {
        menu();
        printf("请选择:&gt; ");
        scanf("%d", &amp;input);
        switch (input)
        {
        case 1:
        {
            printf("开始游戏\n");
            game();
            break;
        }
        case 0:
        {
            printf("游戏结束\n");
            break;
        }
        default:
        {
            printf("非法操作，请重新输入\n");
            break;
        }
        }
    } while (input);   
    return 0;
}
```

 然后在func.c中设计函数内容

```
//func.c
#include "func.h"

void Initialize_Array(char arr[ROWS][LINES], int x, int y, char var)
{
    for (int i = 0; i &lt; x; i++)
    {
        for (int j = 0; j &lt; y; j++)
        {
            arr[i][j] = var;
        }
    }
}

void Print_Array(char arr1[ROWS][LINES], int x, int y)
{
    for (int n = 0; n &lt;= x; n++)
    {
        printf("%d ", n);
    }
    printf("\n");
    for (int i = 1; i &lt;= x; i++)
    {
        printf("%d ", i);
        for (int j = 1; j &lt;= y; j++)
        {
            printf("%c ", arr1[i][j]);
        }
        printf("\n");
    }
}

void Set_mine(char arr2[ROWS][LINES], int x, int y)
{
    int count = MINES;
    while (count)
    {
        int j = rand() % ROW + 1;
        int n = rand() % LINE + 1;
        if (arr2[j][n] == '0')
        {
            arr2[j][n] = '1';
            count--;
        }
    }
}
```

可以看到，这里我们定义了一个变量count并将MINES（地雷数量）赋值给它，当count不为0时开始随机数的生成和字符替换（设置地雷），每次设置地雷成功就count--，当count为0是即地雷布置完毕，Set_mine函数就不再运行。

地雷也设置完了，我们就可以开始判断地雷部分的功能实现了。先明确自己的目的，当输入一个坐标时判断这个坐标是否为地雷，如果是地雷游戏结束，如果不是地雷则显示这个坐标周围八个坐标的地雷数。

但是棋盘最边缘的一圈，周围最多只有5个坐标，怎么进行判断呢？事实上这就是前面我们将数组大小设置为11*11的原因，在实际的数组中红框框住的部分外圈其实还有元素，它们都是字符'0'，这样就能保证进行地雷判断的时候每个坐标周围都有8个坐标可以判断。

这里我们将判断地雷的函数定义为Identifying_mine，不返回数值则类型为void，传递的实参有数组mine，数组show，ROW和LINE

```
//func.c
//...
void Identifying_mine(char arr4[ROWS][LINES], char arr5[ROWS][LINES], int x, int y)
{

}
```

因为棋盘有9*9=81个位置，地雷有10个，所以实际上我们重复Identifying_mine函数81-10=71次时，就获得了游戏的胜利。并且我们要保证输入的坐标是正确的，所以这里我们使用while循环时就能很容易的设定各种条件表达式了

```
void Identifying_mine(char arr4[ROWS][LINES], char arr5[ROWS][LINES], int x, int y)
{
    int a, b;
    int win = 0;
    while (win &lt; ROW * LINE - MINES)
    {
        printf("请输入行列:&gt; ");
        scanf("%d %d", &amp;a, &amp;b);
        if (a &gt;= 1 &amp;&amp; a &lt;= ROW &amp;&amp; b &gt;= 1 &amp;&amp; b &lt;= LINE)
        {
            //...
        }
        else
        {
            printf("非法坐标,请重新输入\n");
        }
    if (win == ROW * LINE - MINES)
    {
        printf("游戏结束，你通关了!\n");
    }
}
```

当我们输入的坐标是地雷时（数组元素为‘1’时）被“炸死”了，游戏失败，这里我们可以打印出地雷数组让玩家知道所有地雷的位置。如果不是地雷则将‘0’替换成代表周围地雷数的相应字符，这又要如何实现呢？

我们都知道，字符在Ascll码表中是有对应数字的，我们可以利用这一点来将字符转换成数值，例如‘0’-‘0’=‘0’；‘1’-‘0’=1；‘2’-‘0’=2；‘3’-‘0’=3......这里我们再创建一个名为Traverse_around的函数，因为要返回周围地雷的数量所以类型为int，传递的实参为地雷数组和行列坐标。

在函数中我们将字符转换成数值，但是我们需要字符来存储进数组中打印在屏幕上，所以出了函数之后我们还需要将转换出的数值再转换成字符，具体如下

```
//func.c
//...
int Traverse_around(char arr3[ROWS][LINES], int x, int y)
{
    return arr3[x - 1][y - 1] + arr3[x - 1][y] + arr3[x - 1][y + 1] + arr3[x][y - 1] + arr3[x][y + 1] + arr3[x + 1][y - 1] + arr3[x + 1][y] + arr3[x + 1][y + 1] - 8 * '0';
}

void Identifying_mine(char arr4[ROWS][LINES], char arr5[ROWS][LINES], int x, int y)
{
    int a, b;
    int win = 0;
    while (win &lt; ROW * LINE - MINES)
    {
        printf("请输入行列:&gt; ");
        scanf("%d %d", &amp;a, &amp;b);
        if (a &gt;= 1 &amp;&amp; a &lt;= ROW &amp;&amp; b &gt;= 1 &amp;&amp; b &lt;= LINE)
        {
            if (arr4[a][b] == '1')
            {
                printf("你被炸死了\n");
                Print_Array(arr4, ROW, LINE);
                break;
            }
            else if (arr4[a][b] == '0')
            {
                char count = Traverse_around(arr4, a, b) + '0';
                arr5[a][b] = count;
                Print_Array(arr5, ROW, LINE);
                win++;
            }
        }
        else
        {
            printf("非法坐标,请重新输入\n");
        }
    if (win == ROW * LINE - MINES)
    {
        printf("游戏结束，你通关了!\n");
    }
}
```

到这里，程序的设计基本就完成了，接下来我们把函数声明在头文件中，并完善一下test.c，就可以宣告成功了。所有的代码如下:

```
//func.h
#pragma once

#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;time.h&gt;
#include &lt;windows.h&gt;
#include &lt;string.h&gt;

#define ROW 9  // 游戏棋盘行数
#define LINE 9 // 游戏棋盘列数

#define ROWS ROW + 2   // 实际数组行数
#define LINES LINE + 2 // 实际数组列数

#define MINES 10 //地雷数量

void Initialize_Array(char arr[ROWS][LINES], int x, int y, char var);

void Print_Array(char arr1[ROWS][LINES], int x, int y);

void Set_mine(char arr2[ROWS][LINES], int x, int y);

void Identifying_mine(char arr4[ROWS][LINES], char arr5[ROWS][LINES], int x, int y);
```

```
//func.c
#include "func.h"

void Initialize_Array(char arr[ROWS][LINES], int x, int y, char var)
{
    for (int i = 0; i &lt; x; i++)
    {
        for (int j = 0; j &lt; y; j++)
        {
            arr[i][j] = var;
        }
    }
}

void Print_Array(char arr1[ROWS][LINES], int x, int y)
{
    for (int n = 0; n &lt;= x; n++)
    {
        printf("%d ", n);
    }
    printf("\n");
    for (int i = 1; i &lt;= x; i++)
    {
        printf("%d ", i);
        for (int j = 1; j &lt;= y; j++)
        {
            printf("%c ", arr1[i][j]);
        }
        printf("\n");
    }
}

void Set_mine(char arr2[ROWS][LINES], int x, int y)
{
    int count = MINES;
    while (count)
    {
        int j = rand() % ROW + 1;
        int n = rand() % LINE + 1;
        if (arr2[j][n] == '0')
        {
            arr2[j][n] = '1';
            count--;
        }
    }
}

int Traverse_around(char arr3[ROWS][LINES], int x, int y)
{
    return arr3[x - 1][y - 1] + arr3[x - 1][y] + arr3[x - 1][y + 1] + arr3[x][y - 1] + arr3[x][y + 1] + arr3[x + 1][y - 1] + arr3[x + 1][y] + arr3[x + 1][y + 1] - 8 * '0';
}

void Identifying_mine(char arr4[ROWS][LINES], char arr5[ROWS][LINES], int x, int y)
{
    int a, b;
    int win = 0;
    while (win &lt; ROW * LINE - MINES)
    {
        printf("请输入行列:&gt; ");
        scanf("%d %d", &amp;a, &amp;b);
        if (a &gt;= 1 &amp;&amp; a &lt;= ROW &amp;&amp; b &gt;= 1 &amp;&amp; b &lt;= LINE)
        {
            if (arr4[a][b] == '1')
            {
                printf("你被炸死了\n");
                Print_Array(arr4, ROW, LINE);
                break;
            }
            else if (arr4[a][b] == '0')
            {
                system("cls");
                char count = Traverse_around(arr4, a, b) + '0';
                arr5[a][b] = count;
                Print_Array(arr5, ROW, LINE);
                win++;
            }
        }
        else
        {
            printf("非法坐标,请重新输入\n");
        }
    }
    if (win == ROW * LINE - MINES)
    {
        printf("游戏结束，你通关了!\n");
    }
}
```

```
//test.c
#include "func.h"
#include "func.c"

void menu()
{
    printf("**********************\n");
    printf("****    1.play   *****\n");
    printf("****    0.exit   *****\n");
    printf("**********************\n");
}

void game()
{
    // 创建一个地雷二维数组和一个面板二维数组
    char mine[ROWS][LINES];
    char show[ROWS][LINES];

    Initialize_Array(mine, ROWS, LINES, '0'); // 初始化地雷二维数组
    Initialize_Array(show, ROWS, LINES, '*'); // 初始化面板二维数组

    Set_mine(mine, ROW, LINE); //随机设置地雷

    // Print_Array(mine, ROW, LINE); // 打印地雷二维数组
    Print_Array(show, ROW, LINE); // 打印面板二维数组

    Identifying_mine(mine,show,ROW,LINE); //判断地雷
}

int main()
{
    int input;
    srand((unsigned int)time(NULL));
    do
    {
        menu();
        printf("请选择:&gt; ");
        scanf("%d", &amp;input);
        switch (input)
        {
        case 1:
        {
            printf("开始游戏\n");
            game();
            break;
        }
        case 0:
        {
            printf("游戏结束\n");
            break;
        }
        default:
        {
            printf("非法操作，请重新输入\n");
            break;
        }
        }
    } while (input);
    return 0;
}
```

当然，游戏过程中我们会发现打印了很多的棋盘，虽然不影响程序的运行，但是很不美观，如果想在每次判断完地雷后清理屏幕怎么实现呢？

在func.h中加入以下头文件

```
#include &lt;windows.h&gt;
```

在Identifying_mine函数中插入这段代码

就可以实现清屏功能了。

**个人感悟：写代码急于求成是大忌，在程序的设计中面对复杂的情况应该化繁为简，将不同功能的需求拆分并逐个击破，首先明确自己写代码的目的，要实现什么功能，然后思考能够达成目的的方法。当代码量比较长时应该写一点调试一次，能够很好的了解bug出现的位置，避免洋洋洒洒写了一大段发现bug比代码行数还多的情况或者找半天也发现不了bug的情况。**
