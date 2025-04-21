# 原创
：  C语言字符串函数和内存函数全集

# C语言字符串函数和内存函数全集

学习完指针的基础知识后，我们就可以开始学习C语言中的各种字符函数、字符串函数和内存函数了，并且还可以通过所学的知识来模拟实现这些函数

## 一.字符函数

### 1.1 字符分类函数

C语言中有一系列的函数提供给我们用来进行字符判断和转换，这些函数都包含在头文件 &lt;ctype.h&gt; 中

这些函数的使用方法非常类似，我们在这里只挑选一个函数来作简单的讲解

> 
int islower ( int a )


islower 可以根据ASCII码值判断参数部分的字符a是否为小写字母，是小写则返回非0整数，不是小写则返回0.

可以尝试练习一下写一个代码实现将字符串中的小写字母转成大写字母

```
#include &lt;stdio.h&gt;
#include &lt;ctype.h&gt;

int main()
{
    int i = 0;
    char str[] = "HelloWorld.\n";
    char c;
    while (str[i])
    {
        c = str[i];
        if (islower(c))
            c -= 32;
        putchar(c);
        i++;
    }
    return 0;
}
```

### 1.2 字符转换函数

C语言中提供了两个字符转换函数

> 
int tolower ( int a ) //大写字母转小写
int toupper ( int a ) //小写字母转大写


在上面写的代码中，我们使用ASCII码减去32来实现小写转大写的效果。但是使用字符转换函数则可以直接使用函数实现大小写转换 

```
#include &lt;stdio.h&gt;
#include &lt;ctype.h&gt;

int main()
{
    int i = 0;
    char str[] = "HelloWorld.\n";
    char c;
    while (str[i])
    {
        c = str[i];
        if (islower(c))
            c = toupper(c);
        putchar(c);
        i++;
    }
    return 0;
}
```

想要了解更多关于字符分类函数和字符转换函数的知识可以点击下方链接 

[cplusplus.com/reference/cctype/?kw=ctype.h<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://cplusplus.com/reference/cctype/?kw=ctype.h](https://cplusplus.com/reference/cctype/?kw=ctype.h)

---


## 二.字符串函数 

### 2.1 strlen的使用和模拟实现

```
size_t strlen (const char* str)
```

strlen函数的模拟实现：

```
#include &lt;stdio.h&gt;
#include &lt;assert.h&gt;

int My_strlen(char *str)
{
    assert(str);
    int i = 0;
    while (*(str + i))
    {
        i++;
    }
    return i;
}

int main()
{
    char str[20] = "hello";
    int len = My_strlen(str);
    printf("%d", len);
    return 0;
}
```

输出：5 

###  2.2 strcpy的使用和模拟实现

```
char* strcpy(char* destination, const char* source );
```

strcpy函数的模拟实现

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;assert.h&gt;

char *My_strcpy(char *str1, const char *str2)
{
    char *ret = str1;
    assert(str1 &amp;&amp; str2);
    while (*str2 != '\0')
    {
        *str1 = *str2;
        str1++;
        str2++;
    }
    *str1 = *str2;
    return ret;
}

int main()
{
    char arr1[20] = {0};
    char arr2[] = {"hello"};
    My_strcpy(arr1, arr2);
    printf("%s", arr1);
    return 0;
}
```

输出：hello 

### 2.3 strcat的使用和模拟实现

```
char* strcat(char* destination, const char* source );
```

strcat函数的模拟实现

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;assert.h&gt;

char *My_strcat(char *str1, const char *str2)
{
    assert(str1 &amp;&amp; str2);
    char *ret = str1;
    while (*str1)
    {
        str1++;
    }
    while (*str2)
    {
        *str1++ = *str2++;
    }
    return ret;
}

int main()
{
    char arr1[20] = {"hello "};
    char arr2[] = {"world"};
    char *p = My_strcat(arr1, arr2);
    printf("%s", p);
    return 0;
}
```

输出：hello world

### 2.4 strcmp的使用和模拟实现

```
int strcmp (const char* str1, const char* str2)
```

strcmp函数的模拟实现

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;assert.h&gt;

int My_strcmp(const char *str1, const char *str2)
{
    assert(str1 &amp;&amp; str2);
    while (*str1 == *str2)
    {
        if (*str1 == '\0')
            return 0;
        str1++;
        str2++;
    }
    return *str1 - *str2;
}

int main()
{
    char arr1[] = {"abcdefg"};
    char arr2[] = {"abcdevg"};
    int ret = My_strcmp(arr1, arr2);
    printf("%d\n", ret);
    return 0;
}
```

输出：-16

### 2.5 strncpy函数的使用和模拟实现

```
char* strncpy(char* destination, const char* source, size_t num);
```

strncpy函数的模拟实现

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;assert.h&gt;

char *My_strncpy(char *p1, const char *p2, size_t num)
{
    assert(p1 &amp;&amp; p2);
    char *pret = p1;
    size_t cmp = strlen(p2);
    if (cmp &lt; num)
    {
        for (int i = 0; i &lt; cmp; i++)
        {
            *(pret + i) = *(p2 + i);
        }
        for (int j = cmp; j &lt; num; j++)
        {
            *(pret + j) = '\0';
        }
    }
    else
    {
        for (int i = 0; i &lt; num;i++)
        {
            *(pret + i) = *(p2 + i);
        }
    }
    return pret;
}

int main()
{
    char arr1[] = "helloworld";
    char arr2[20] = "xxxxxxxxxxxxxxxx";
    char *p1 = My_strncpy(arr2, arr1, 7);
    printf("%s", p1);
    return 0;
}
```

输出：hellowoxxxxxxxxx

### 2.6 strncat函数的使用和模拟实现

```
char* strncat(char* destination, const char* source, size_t num);
```

strncat函数的模拟实现

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;assert.h&gt;

char *My_strncat(char *str1, const char *str2, size_t num)
{
    assert(str1 &amp;&amp; str2);
    size_t a = strlen(str2);
    char *p1 = str1;
    while (*p1)
    {
        p1++;
    }
    if (num &gt; a)
    {
        for (int i = 0; i &lt; a; i++)
        {
            *p1++ = *str2++;
        }
        *p1 = '\0';
    }
    else
    {
        for (int i = 0; i &lt; num; i++)
        {
            *p1++ = *str2++;
        }
        *p1 = '\0';
    }
    return str1;
}

int main()
{
    char arr1[] = "hello\0xxxxxxxxxxxxx";
    char arr2[] = "world";
    char *pc = My_strncat(arr1, arr2, 3);
    printf("%s", pc);
    return 0;
}
```

输出：hellowor

### 2.7 strncmp函数的使用

```
int strncmp(const char* str1, const char* str2, size_t num);
```

同上，只比较两个字符串的前num个字符，这里就不过多赘述了

### 2.8 strstr函数的使用和模拟实现

```
char* strstr(const char* str1, const char* str2);
```

例如：

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;

int main()
{
    char str[] = "Hello world";
    char *pi;
    pi = strstr(str, "o");
    printf("%s\n", pi);
    return 0;
}
```

其中，字符串“Hello world”中有两个'o'，但是strstr只会返回第一个'o'出现的位置，所以输出：

strstr函数的模拟实现：

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;assert.h&gt;

char *My_strstr(const char *str1, const char *str2)
{
    assert(str1 &amp;&amp; str2);
    while (*str1)
    {
        const char *p1 = str1;
        const char *p2 = str2;
        while (*p1 &amp;&amp; *p2 &amp;&amp; *p1 == *p2)
        {
            p1++;
            p2++;
        }
        if (*p2 == '\0')
        {
            return (char *)str1;
        }
        str1++;
    }
    return NULL;
}

int main()
{
    char arr1[] = {"Hello world"};
    char arr2[] = {"o"};
    char *p = My_strstr(arr1, arr2);
    if (p != NULL)
        printf("%s", p);
    else
        printf("找不到");
    return 0;
}
```

### 2.9 strtok函数的使用

```
char* strtok (char* str, const char* sep);
```

例如：

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;

int main()
{
    char arr[] = "192.168.6.111";
    char *sep = ".";
    char *str = NULL;
    for (str = strtok(arr, sep); str != NULL; str = strtok(NULL, sep))
    {
        printf("%s\n", str);
    }
    return 0;
}
```

输出：

---


## 三.内存函数

### 3.1 memcpy函数的使用和模拟实现

```
void* memcpy (void* destination, const void* source, size_t num);
```

memcpy函数的模拟实现：

```
#include &lt;stdio.h&gt;
#include &lt;assert.h&gt;

void *My_memcpy(void *dest, const void *sour, size_t num)
{
    assert(dest &amp;&amp; sour);
    void *pd = dest;
    for (int i = 0; i &lt; num; i++)
    {
        *(char *)pd = *(char *)sour;
        (char *)pd++;
        (char *)sour++;
    }
    return dest;
}

int main()
{
    int arr2[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int arr1[20] = {0};
    int *pi = My_memcpy(arr1, arr2, 20);
    for (int i = 0; i &lt; 10; i++)
    {
        printf("%d ", *(pi + i));
    }
    return 0;
}
```

因为只复制20个字节，也就是5个整型，所以输出：

### 3.2 memmove函数的使用和模拟实现

```
void* memmove(void* destination, const void* source, size_t num);
```

例如我们要在arr数组中，从首元素开始复制20个字节也就是5个整型到目标空间，但是目标空间的地址指向arr+2的位置：

此时两个内存空间出现重叠，如果我们使用memcpy函数，会输出错误的结果：

因为我们在修改destination指向的内存空间的时候，source指向的空间内容也被修改了，就会导致冲突，所以使用memmove会避免冲突

memmove函数的模拟实现：

```
#include &lt;stdio.h&gt;
#include &lt;assert.h&gt;

void *My_memmove(void *dest, const void *sour, size_t num)
{
    assert(dest &amp;&amp; sour);
    void *ret = dest;
    if (dest &gt; sour)
    {
        for (int i = num - 1; i &gt;= 0; i--)
        {
            *((char *)dest + i) = *((char *)sour + i);
        }
    }
    else
    {
        for (int i = 0; i &lt; num; i++)
        {
            *((char *)dest + i) = *((char *)sour + i);
        }
    }
    return ret;
}

int main()
{
    int arr1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int *pi = My_memmove(arr1 + 2, arr1, 20);
    for (int i = 0; i &lt; 10; i++)
    {
        printf("%d ", arr1[i]);
    }
    return 0;
}
```

输出：

### 3.3 memset函数的使用和模拟实现

```
void* memset(void* ptr, int value, size_t num);
```

memset函数可以将ptr指向的内存空间中的num个字节修改为value

例如：

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;

int main()
{
    char str[] = "Hello world";
    memset(str, 'x', 6);
    printf(str);
    return 0;
}
```

输出结果：

### 3.4 memcpy函数的使用

```
int memcmp(const void* ptr1, const void* ptr2, size_t num);
```

memcpy函数用来比较ptr1指向的位置和ptr2指向的位置开始向后的num个字节

例如：

```
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;

int main()
{
    char buffer1[] = "DWgaOtP12df0";
    char buffer2[] = "DWGAOTP12DF0";
    int n;
    n = memcmp(buffer1, buffer2, sizeof(buffer1));
    if (n &gt; 0)
        printf("'%s' is greater than '%s'.\n", buffer1, buffer2);
    else if (n &lt; 0)
        printf("'%s' is less than '%s'.\n", buffer1, buffer2);
    else
        printf("'%s' is the same as '%s'.\n", buffer1, buffer2);
    return 0;
}
```

输出结果：

完.
