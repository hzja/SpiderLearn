# 原创
：  6_SHA1算法

# 6_SHA1算法

**实验题目**

> 
SHA-1算法


**实验目的和要求**

> 
熟悉SHA-1算法的运行过程，使用C++\Python语言编写实现SHA-1算法程序，增加对摘要函数的理解


**实验环境**

> 
VS2019、PyCharm


**实验内容**

> 
- 屏幕输入一句英文，单词之间用下划线间隔；- 输出哈希值


**算法描述**

> 
SHA1是一种密码散列函数，由美国国家安全局设计，主要适用于数字签名标准里面定义的数字签名算法。对于长度小于2^64位的消息，SHA1会产生一个160位的消息摘要。当接收到消息的时候，这个消息摘要可以用来验证数据的完整性。在传输的过程中，数据很可能会发生变化，那么这时候就会产生不同的消息摘要。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210512185905332.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210512185914658.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210512185921721.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210512185929180.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>


**实验代码**

> 
C++


```
#include &lt;iostream&gt;
#include &lt;string&gt;
using namespace std;
#define LL long long 

// 字符转换,string转int
void trans(string In, int* input)
{
	int i, j;
	int len = In.length();
	for (i = 0, j = 0; i &lt; len; i++)
	{
		if (i != 0 &amp;&amp; i % 4 == 0)
		{
			j++;
		}
		input[j] = (input[j] &lt;&lt; 8) + int(In[i]);
	}
	if (In.length() % 4 == 1)
	{
		input[j] = input[j] &lt;&lt; 24;
	}
	else if (In.length() % 4 == 2)
	{
		input[j] = input[j] &lt;&lt; 16;
	}
	else if (In.length() % 4 == 3)
	{
		input[j] = input[j] &lt;&lt; 8;
	}
}

// 补位及补长度
void supplement(LL len, int* input)
{
	if (len % 4 == 0)
	{
		input[len / 4] += 0x80000000;
	}
	else if (len % 4 == 1)
	{
		input[len / 4] += 0x00800000;
	}
	else if (len % 4 == 2)
	{
		input[len / 4] += 0x00008000;
	}
	else if (len % 4 == 3)
	{
		input[len / 4] += 0x00000080;
	} input[14] = ((8 * len) &amp; 0xffffffff00000000) &gt;&gt; 8;
	input[15] = (8 * len) &amp; 0x00000000ffffffff;
}

// 循环左移n位
int ROL(int a, int n)
{
	// 注意强制类型转换为无符号整数
	a = ((unsigned)a &gt;&gt; (32 - n)) + ((unsigned)a &lt;&lt; n);
	return a;
}

// 函数ft(B,C,D) 
int Ft(int i, int* HH)
{
	int result;
	if (i &gt;= 0 &amp;&amp; i &lt;= 19)
	{
		result = (HH[1] &amp; HH[2]) | ((~HH[1]) &amp; HH[3]);
	}
	else if (i &gt;= 20 &amp;&amp; i &lt;= 39)
	{
		result = HH[1] ^ HH[2] ^ HH[3];
	}
	else if (i &gt;= 40 &amp;&amp; i &lt;= 59)
	{
		result = (HH[1] &amp; HH[2]) | (HH[1] &amp; HH[3]) | (HH[2] &amp; HH[3]);
	}
	else if (i &gt;= 60 &amp;&amp; i &lt;= 79)
	{
		result = HH[1] ^ HH[2] ^ HH[3];
	}
	return result;
}

// 常量Kt
int KT(int i)
{
	int Kt[4], result;
	Kt[0] = 0x5A827999;
	Kt[1] = 0x6ED9EBA1;
	Kt[2] = 0x8F1BBCDC;
	Kt[3] = 0xCA62C1D6;
	if (i &gt;= 0 &amp;&amp; i &lt;= 19)
	{
		result = Kt[0];
	}
	else if (i &gt;= 20 &amp;&amp; i &lt;= 39)
	{
		result = Kt[1];
	}
	else if (i &gt;= 40 &amp;&amp; i &lt;= 59)
	{
		result = Kt[2];
	}
	else if (i &gt;= 60 &amp;&amp; i &lt;= 79)
	{
		result = Kt[3];
	}
	return result;
}

// 生成消息Wt
void WT(int i, int* Wt, int* input)
{
	if (i &gt;= 0 &amp;&amp; i &lt;= 15)
	{
		Wt[i] = input[i];
	}
	else
	{
		Wt[i] = ROL(Wt[i - 3] ^ Wt[i - 8] ^ Wt[i - 14] ^ Wt[i - 16], 1);
	}
	return;
}

// 对散列块进行处理
void deal(int* HH, int* input, int* H)
{
	int Wt[80];
	for (int i = 0; i &lt; 80; i++)
	{
		int ft, kt, temp; // 计算函数Ft(B,C,D) ft = Ft(i, HH);
		ft = Ft(i, HH);
		// 对应Kt
		kt = KT(i);
		// 计算wt
		WT(i, Wt, input);
		int aaaa = ROL(HH[0], 5);
		int bbbb = Wt[i];
		// 循环左移5位
		temp = ROL(HH[0], 5) + ft + HH[4] + kt + Wt[i]; // 跟新ABCDE五个寄存器
		HH[4] = HH[3];
		HH[3] = HH[2];
		HH[2] = ROL(HH[1], 30);
		HH[1] = HH[0];
		HH[0] = temp; //printf("%x %x %x %x %x\n", HH[0], HH[1], HH[2], HH[3], HH[4]);
	}
	// 分别与H0,H1,H2,H3,H4相加
	for (int i = 0; i &lt; 5; i++)
	{
		H[i] += HH[i];
	}
}

int main()
{
	cout &lt;&lt; "\n请输入待散列的数据：";
	string In;
	cin &gt;&gt; In;
	/*char ch = '_';
	string::iterator it;
	// 删除输入字符串中的下划线
	for (it = In.begin(); it &lt; In.end(); it++)
	{
		if (*it == ch)
		{
			In.erase(it);
			it--;
		}
	}*/
	cout &lt;&lt; "\n\n*****************************" &lt;&lt; endl;
	cout &lt;&lt; "***  SHA-1散列算法计算中  ***" &lt;&lt; endl;
	cout &lt;&lt; "*****************************\n\n" &lt;&lt; endl;

	int input[16];
	memset(input, 0, sizeof(input));
	// 字符转换
	trans(In, input);
	// 补位以及补长度
	supplement(In.length(), input);

	// HH为ABCDE寄存器
	int HH[5] = { 0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0 };
	// H为初始数据块
	int H[5] = { 0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476,0xC3D2E1F0 };
	//对散列块进行处理
	deal(HH, input, H);

	// 输出哈希结果
	cout &lt;&lt; In &lt;&lt; "的散列值为：";
	for (int i = 0; i &lt; 5; i++)
	{
		// 16进制输出
		cout &lt;&lt; hex &lt;&lt; H[i];
	}
	cout &lt;&lt; endl &lt;&lt; endl &lt;&lt; endl;
	return 0;
}

```

> 
Python


```
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 22:34
# @Author  : H3rmesk1t
# @FileName: SHA-1.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/LYJ20010728/
import hashlib

# SHA_1运算
def encodeOfHSA_1(s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    strOfSHA_1 = input("请输入需要进行SHA_1算法操作的英文句子：\n")
    print(f"{strOfSHA_1}进过SHA_1操作后的结果为{encodeOfHSA_1(s=strOfSHA_1)}")

```
