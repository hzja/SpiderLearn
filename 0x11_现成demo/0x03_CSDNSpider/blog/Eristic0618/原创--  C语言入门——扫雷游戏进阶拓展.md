# 原创
：  C语言入门——扫雷游戏进阶拓展

# C语言入门——扫雷游戏进阶拓展

🎯在上篇文章中我们对扫雷游戏的基础版本已经有了一个详细且全面的了解，但是基础版本的功能十分有限，操作难度大并且游戏体验较差，今天我们来了解如何编写程序实现扫雷游戏的拓展功能，使我们制作出的扫雷程序更加好玩。

### 拓展功能1：展开一片

✨有玩过扫雷的人都知道，当我们的鼠标点击到四周没有地雷的格子时会一下子展开一大片无地雷的空白区域，效果如下：

😍看起来十分的炫酷，并且这种展开一片的效果也可以避免我们游玩自制扫雷程序的时候的大量重复操作，大大的提升了游戏体验。问题来了，怎么实现这种效果呢？

已知在程序运行中我们输入坐标来进行各种操作，首先我们要明确以下几个点：

1.只有当我们输入的坐标位置四周都没有雷（周围8格都是‘0’）时才触发展开效果。

2.已经展开过的坐标不能重复展开。

然后，我们就已经明确了展开效果的触发条件和限制条件了，接着我们开始构思程序该如何实现。为了程序的可读性，实现展开效果的所有程序应该封装在一个函数中，这里我把函数命名为Spread，需要向函数传递一个地雷数组和一个面板数组（一个检测展开条件一个替换字符），还需要传递坐标，不需要返回值所以类型是void，至此我们就完成了函数的命名。

```
void Spread(char arr4[ROWS][LINES], char arr5[ROWS][LINES], int x, int y)
{

}
```

在实现展开一片效果的时候我们容易观察到打开的格子是由第一个坐标辐射向外展开的，这里就需要用到递归的思想。我们先看具体代码。

```
void Spread(char arr4[ROWS][LINES], char arr5[ROWS][LINES], int x, int y)
{
    int count = Traverse_around(arr4, x, y);
    if (count == 0)
    {
        arr5[x][y] = ' ';
        for (int i = x - 1; i &lt;= x + 1; i++)
        {
            for (int j = y - 1; j &lt;= y + 1; j++)
            {
                if (arr5[i][j] == '*' &amp;&amp; x &gt;= 1 &amp;&amp; x &lt;= 9 &amp;&amp; y &gt;= 1 &amp;&amp; y &lt;= 9)
                {
                    Spread(arr4, arr5, i, j); // 通过递归实现展开效果
                }
            }
        }
    }
    else
    {
        arr5[x][y] = count + '0';
    }
    system("cls");
    Print_Array(arr5, ROW, LINE);
}
```

🎃为了更好理解，我们对代码进行逐步讲解。

1.首先计算坐标四周有多少地雷，这里要用到for循环遍历四周坐标，如果周围8格内无地雷，则把‘*’替换成‘ ’，这样就能实现展开一片空白区域的效果，同时也可以作为限制条件避免死递归。

2.当周围8格内无地雷时，就通过递归计算周围8格中每一格四周的坐标并展开。当然前面说过已经展开过的坐标不能重复展开，这里就需要增加一个限定条件

因为只有坐标四周无地雷的时候才进入递归，所以已经被展开过的坐标字符是‘ ’，未被展开过的坐标字符是‘*’，这样就能避免重复展开坐标导致死遍历。

3.当周围8格内有地雷时，就把坐标的字符‘*’替换成地雷数，整型转换成字符的方式在上一篇文章中已经介绍过，这里不再赘述。

4.当空白区域已经全部展开，就无法继续遍历，此时打印面板数组继续游戏。

到这里，我们已经完成了Spread的函数内容，该在哪里去使用这个函数呢？

依旧是根据需求设计代码，我们想要在判断地雷的时候完成展开一片的效果，所以Spread函数应该放置在判断地雷的函数——Identifying_mine里面（这个函数在上篇文章中介绍过）。

但是，前面说过只有当我们输入的坐标位置四周都没有雷（周围8格都是‘0’）时才触发展开效果，所以这里我们需要if语句来设计触发条件，当坐标的字符不为‘0’时（周围有地雷）不触发展开，字符为‘0’时才执行Spread函数。

```
if (arr5[a][b] != '0')
{
    Print_Array(arr5, ROW, LINE);
}
else if (arr5[a][b] == '0')
{
    Spread(arr4, arr5, a, b);
}
```

Print_Array函数上篇文章也介绍过，是用来打印面板二维数组作为游戏ui的，这里不赘述。

但是此时我们又遇到一个问题：现在展开一片的效果基本完成了，但是程序运行的时候游戏胜利的条件似乎和Spread的功能有了一点矛盾。

上篇文章中，我们使用win &lt; ROW * LINE - MINES作为循环执行的条件，每次检查完一个坐标就win++，当win == ROW * LINE - MINES时游戏就胜利。但是我们现在有了展开一片空白区域之后这个条件就作废了，因为无法计算展开了多少格数，此时我们需要换一个方向来设计循环执行的条件。这里先把代码放出来便于理解。

```
void Identifying_mine(char arr4[ROWS][LINES], char arr5[ROWS][LINES], int x, int y)
{
    int a, b;
    int win = 0;
    int star = 81;
    while (star &gt; MINES)
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
                if (arr5[a][b] != '0')
                {
                    Print_Array(arr5, ROW, LINE);
                }
                else if (arr5[a][b] == '0')
                {
                    Spread(arr4, arr5, a, b);
                }
                star = 0;
                for (int i = 1; i &lt;= 9; i++)
                {
                    for (int j = 1; j &lt;= 9; j++)
                    {
                        if (arr5[i][j] == '*' || arr5[i][j] == '!')
                        {
                            star++; // 每次检测面板数组还剩多少颗星，如果星数和地雷数相等跳出while
                        }
                    }
                }
            }
        }
        else
        {
            printf("非法坐标,请重新输入\n");
        }
    }
    if (star == MINES)
    {
        printf("游戏结束，你通关了!\n");
    }
}
```

首先int star=81（ 不一定非要81，能够满足条件进入while循环的数都可），然后一直到这个部分

当没有达到胜利条件的时候，show数组中的‘*’和‘！’（这里在后续标记地雷功能中会提到）一定大于地雷数，所以循环继续。每次输入坐标排雷时都检测一遍，当字符数=地雷数时说明剩下的坐标全部是地雷，于是游戏胜利。至此我们就完成了展开一篇拓展功能的实现。

### 拓展功能2：标记地雷

这个功能实现的难度不高，话不多说我们先上代码

```
void Choose(char mine[ROWS][LINES], char show[ROWS][LINES]) // 拓展功能：标记地雷
{
    printf("1.扫雷\n");
    printf("2.标记\n");
    printf("3.取消标记\n");
    printf("请选择:&gt;");
    int select;
    scanf("%d", &amp;select);
    switch (select)
    {
    case 1:
    {
        break;
    }
    case 2:
    {
        int flag = 1;
        while (flag)
        {
            int x, y;
            printf("请输入想标记的坐标:&gt;");
            scanf("%d %d", &amp;x, &amp;y);
            if (x &gt;= 1 &amp;&amp; x &lt;= ROW &amp;&amp; y &gt;= 1 &amp;&amp; y &lt;= LINE)
            {
                show[x][y] = '@';
                Print_Array(show, ROW, LINE);
                Choose(mine, show);
                flag = 0;
            }
            else
            {
                printf("非法坐标,请重新输入\n");
            }
        }
        break;
    }
    case 3:
    {
        int flag = 1;
        while (flag)
        {
            int x, y;
            printf("请输入想取消标记的坐标:&gt;");
            scanf("%d %d", &amp;x, &amp;y);
            if (x &gt;= 1 &amp;&amp; x &lt;= ROW &amp;&amp; y &gt;= 1 &amp;&amp; y &lt;= LINE)
            {
                show[x][y] = '*';
                Print_Array(show, ROW, LINE);
                Choose(mine, show);
                flag = 0;
            }
            else
            {
                printf("非法坐标,请重新输入\n");
            }
        }
        break;
    }
    default:
    {
        printf("非法操作，请重新输入\n");
    }
    }
}
```

首先我们创建一个函数用来封装实现标记地雷功能的代码，将函数命名为Choose，不需要返回值所以函数类型为void。

我们设定函数执行时，输入1继续扫雷，输入2转到标记地雷功能，输入3转到取消标记地雷功能，所以这里选择使用switch语句。

case 1中，要继续扫雷，我们直接使用break跳出语句就开始继续执行扫雷程序。

case 2中，要标记地雷，我们需要变量来存贮输入的坐标，然后将对应的坐标的字符替换成自己想要的标记符号（如‘！’或者‘@’都可，按自己喜好来），再打印面板数组即可。但是要保证输入的坐标是有效的，否则就要重新输入。所以我们创建一个flag变量并赋值为1作为while循环的条件，当坐标合法并完成了标记地雷功能后flag赋值为0，循环结束。

case 3与case 2同理，只是把标记符号替换回'*'而已。

Choose函数和Spread函数一样，也是放在Identifying_mine函数中，具体位置在：

很好理解，打印完面板数组或者展开空白区域之后就要紧跟着选择扫雷或者标记，所以Choose函数放在Print_Array函数和Spread函数之后。

🎉至此，我们就完成了两个扫雷的进阶拓展功能的实现，当我们真正上手做时会发现这并不需要什么很高端的知识，只要有心，困难往往迎刃而解。
