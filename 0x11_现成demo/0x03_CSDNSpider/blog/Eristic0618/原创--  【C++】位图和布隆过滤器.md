# 原创
：  【C++】位图和布隆过滤器

# 【C++】位图和布隆过滤器

在前面的学习中，我们已经对哈希有了一定的了解。如果还有不认识哈希的可以移步

[【C++】哈希表-CSDN博客<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://blog.csdn.net/Eristic0618/article/details/140054885?spm=1001.2014.3001.5501](https://blog.csdn.net/Eristic0618/article/details/140054885?spm=1001.2014.3001.5501)今天我们来介绍两个基于哈希思想的数据结构——位图和布隆过滤器

## 一、位图

位图和哈希的直接定址法很相似，我们先来看一道面试题

> 
有40亿个未排序的不重复的无符号整数，如何快速判断一个数是否在这40亿个数中？


方法1：遍历，时间复杂度为O(N)

方法2：排序后二分查找，时间复杂度为O(N*logN)

这两个方法的时间复杂度看上去都还能接受，但是我们不能用这两个办法，为什么？

限制我们的其实不是时间，而是**空间**。40亿个整型需要的空间**高达14.9G**，我们的内存根本开不出这么大的连续空间

如果用红黑树、哈希表，需要的空间那就更多了

因此，我们需要一个**空间友好型**的结构来解决这个问题，而**位图**可以完美解决我们的需求。

### 1.1 概念

我们可以把位图理解为一个**位（bit）组成的数组**，每个位置只有0或1

实际上位图的确是一个类型为int的数组，不过我们可以把一个int**拆分为32个bit位**（int类型大小为4字节，也就是32bit）。拆分过后，相同大小的位图能够存储的信息就比数组多了很多。

### 1.2 思想

例如上面的面试题，首先我们要知道**无符号整数的范围为0~4294967295**，40亿个无符号整数就分布在这个范围区间内。因此我们不能只开40亿个位的位图，而是要开**4294967295**个位的位图。

此时有两种情况：一个数在这40亿个数所在的集合中、一个数不在这40亿个数所在的集合中。

我们用这个数在位图中对应的位来判断其状态，如果为0说明不在，为1说明在

位图开好后，我们只需要**将存在的数所在的位从0置为1**，在查找的时候就可以快速的确定某个数是否包含在这40亿个数所在的集合中。例如整数4在这个集合，那我们就把位图的第5位（第1位对应数字0）从0置为1。

用这种方法，我们所需要的空间就大大减少了，4294967295个bit换算后只有**约0.5G**的大小。

### 1.3 实现

了解了位图的概念和思想后，接下来就是如何实现位图了。

前面提到过，我们可以用一个int类型的数组来实现位图，1个int就是32bit

接下来挡在我们面前的唯一阻碍，就是各种位运算操作了（其实并不复杂）

#### （1）数与位图的映射

要对位图进行操作，首先我们得先找到某个数x**在位图中对应的位置**

一个int是32bit，所以我们用**** i = x / 32 ****就可以找到这个数对应数组的第 i+1 个整型（下标为 i ）

找到了对应的整型后，我们用** j = **x % 32 ****就可以找到这个数对应该整型的第 j 个bit

例如我们要找34在位图中对应的位置，34 / 32 == 1，即对应数组下标为1处的整型

34 % 32 == 2，即对应该整型的第2位

#### （2）将0变为1

成功找到了一个数在位图中对应的位置后，我们要知道如何把该位置的0变为1

我们可以使用按位或的特性：**有1则为1**。例如：

所以要将某个位置的0变为1，我们只需要找到该位置所属的整型，然后用一个**"其他位置全为0、该位置为1"**的二进制数来按位或这个整型即可

如何得到这个"其他位置全为0、该位置为1"的二进制数呢？通过移位操作即可，例如：

（32位太长了，这里只写出前8位） 

需要注意，大端机和小端机中高位和低位在地址中的位置可能不同，但**按位左移**一定是**向高位移动**，**按位右移**一定是**向低位移动**

前面我们已经知道了该位置是整型中的第 j 位，所以只需要左移 j 位即可

代码：

```
void set(size_t x)
{
	size_t i = x / 32;
	size_t j = x % 32;
	_bits[i] |= (1 &lt;&lt; j);
}
```

#### （3）将1变为0

有些情况下我们需要将已经为1的位置变为0，该如何操作呢？

和前面的方法极为相似，不过这一步我们要使用的是按位或：**有0则为0**

要将某个位置的0变为1，我们只需要找到该位置所属的整型，然后用一个**"其他位置全为1、该位置为0"**的二进制数来按位与这个整型即可，和上面刚好相反

还是先通过移位操作来得到一个二进制数，然后将其按位取反，才是我们所需要的二进制数

"~"是按位取反的符号不要忘记了

然后将这个二进制数按位与上对应的整型，就能把对应的bit置为0了

代码：

```
void reset(size_t x)
{
	size_t i = x / 32;
	size_t j = x % 32;
	_bits[i] &amp;= ~(1 &lt;&lt; j);
}
```

#### （4）查询

学会了对位图的操作，我们还需要知道如何查询一个数对应的位置是否为1

和将1变为0的操作类似，先移位，再按位与（不需要按位取反）

如果得到的数为0说明对应位置为0，如果得到的数不为0则说明对应位置为1

代码：

```
bool test(size_t x)
{
	size_t i = x / 32;
	size_t j = x % 32;
	return _bits[i] &amp; (1 &lt;&lt; j);
}
```

#### （5）完整代码

```
namespace Eristic
{
	template&lt;size_t N&gt;
	class bitset
	{
	public:
		bitset()
		{
			_bits.resize(N / 32 + 1, 0);
		}

		void set(size_t x)
		{
			if (x &gt; N) return;
			size_t i = x / 32;
			size_t j = x % 32;
			_bits[i] |= (1 &lt;&lt; j);
		}
		
		void reset(size_t x)
		{
			if (x &gt; N) return;
			size_t i = x / 32;
			size_t j = x % 32;
			_bits[i] &amp;= ~(1 &lt;&lt; j);
		}

		bool test(size_t x)
		{
			if (x &gt; N) return;
			size_t i = x / 32;
			size_t j = x % 32;
			return _bits[i] &amp; (1 &lt;&lt; j);
		}

	private:
		vector&lt;int&gt; _bits;
	};
}
```

## 二、布隆过滤器

位图一般只能处理整型数据，如果遇到字符串类型的数据就束手无策了

面对字符串，我们可以使用**布隆过滤器**

### 2.1 概念

布隆过滤器（Bloom Filter）是1970年由布隆提出的。它实际上由一个很长的**二进制向量**和一系列**哈希函数**组成。布隆过滤器可以用于检索一个元素是否在一个集合中。它的优点是空间效率和查询时间都比一般的算法要好的多，缺点是有一定的误识别率和删除困难。

简单来说，布隆过滤器就是将字符串哈希与位图结合。

### 2.2 思想

既然位图无法处理字符串类型的数据，那我们能否通过某种方式**将字符串变为整型**呢？

实际上这就是布隆过滤器的核心思想，我们可以使用**字符串哈希**将字符串变为整型，然后映射到位图中，例如BKDR字符串哈希：

```
struct BKDRHash
{
	size_t operator()(const string&amp; key)
	{
		// BKDR字符串哈希
		size_t ret = 0;
		for (auto i : key)
		{
			ret *= 31;
			ret += i;
		}
		return ret;
	}
};
```

但是这种方式也会带来问题：不同的字符串通过哈希函数可能会得到相同的整型，造成哈希冲突！

如果不同的字符串映射的位置相同，在查找时可能会出现一个字符串本来不存在，但因为另一个字符串和其映射的位置相同导致判断错误。所以布隆过滤器实际上是有概率**误判**的。

布隆过滤器的误判**无法完全消除**，我们只能想办法尽量减少误判率，即**多增加几个不同的哈希函数**，让一个字符串**同时映射多个位置**，就可以有效减少误判的概率

假设有三个哈希函数，一个字符串映射三个位置：

<img alt="" height="577" src="https://i-blog.csdnimg.cn/direct/412ca6495faa4629bb0b310aa835d043.png" width="1194"/>​​​​​​​

即使字符串1和字符串2有两个位置都产生了哈希冲突，但第三个位置不同，避免了误判

映射的位置越多，同时冲突的概率就越小。但是也不能无休止的增加映射位置，我们可以尽可能地在合理范围内减小误判概率 。

同时，因为存在映射重合的情况，删除一个字符串可能导致另一个字符串无法被查找到，所以布隆过滤器**不支持删除操作**。不过布隆过滤器的变种Counting Bloom filter支持元素删除，可以参考[Counting Bloom Filter 的原理和实现-腾讯云开发者社区-腾讯云 (tencent.com)<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://cloud.tencent.com/developer/article/1136056](https://cloud.tencent.com/developer/article/1136056)

布隆过滤器判断一个元素**不存在**的情况是准确的，只有在判断一个元素存在的时候可能会误判。

哈希函数的个数和布隆过滤器的长度同时影响着误判率，其关系如下：

### 2.3 实现

```
//三个哈希函数
struct BKDRHash
{
	size_t operator()(const string&amp; key)
	{
		// BKDR字符串哈希
		size_t ret = 0;
		for (auto i : key)
		{
			ret *= 31;
			ret += i;
		}
		return ret;
	}
};

struct APHash
{
	size_t operator()(const string&amp; key)
	{
		size_t hash = 0;
		for (size_t i = 0; i &lt; key.size(); i++)
		{
			char ch = key[i];
			if ((i &amp; 1) == 0)
			{
				hash ^= ((hash &lt;&lt; 7) ^ ch ^ (hash &gt;&gt; 3));
			}
			else
			{
				hash ^= (~((hash &lt;&lt; 11) ^ ch ^ (hash &gt;&gt; 5)));
			}
		}
		return hash;
	}
};

struct DJBHash
{
	size_t operator()(const string&amp; key)
	{
		size_t hash = 5381;
		for (auto ch : key)
		{
			hash += (hash &lt;&lt; 5) + ch;
		}
		return hash;
	}
};


template&lt;size_t N, class K = string, class HashFunc1 = BKDRHash, class HashFunc2 = APHash, class HashFunc3 = DJBHash&gt; //3个哈希函数
class BloomFilter
{
public:
	void set(const K&amp; key)
	{
        //每个字符串映射三个位置
		size_t hash1 = HashFunc1()(key) % N;
		size_t hash2 = HashFunc2()(key) % N;
		size_t hash3 = HashFunc3()(key) % N;

		_bs.set(hash1);
		_bs.set(hash2);
		_bs.set(hash3);
	}

	bool test(const K&amp; key)
	{
		size_t hash1 = HashFunc1()(key) % N;
		if (_bs.test(hash1) == false)
			return false;

		size_t hash2 = HashFunc2()(key) % N;
		if (_bs.test(hash2) == false)
			return false;

		size_t hash3 = HashFunc3()(key) % N;
		if (_bs.test(hash3) == false)
			return false;

		return true; //存在误判概率
	}
private:
	bitset&lt;N&gt; _bs;
};

void Test_BF() //测试布隆过滤器长度对误判率的影响
{
	srand(time(0));
	const size_t N = 100;
	BloomFilter&lt;N * 5&gt; bf;

	std::vector&lt;std::string&gt; v1;
	std::string url = "https://blog.csdn.net/Eristic0618?spm=1000.2115.3001.5343";

	for (size_t i = 0; i &lt; N; i++)
	{
		v1.push_back(url + std::to_string(i));
	}
	for (auto&amp; str : v1)
	{
		bf.set(str);
	}

	std::vector&lt;std::string&gt; v2;
	//相同前缀不同后缀的相似串
	for (size_t i = 0; i &lt; N; i++)
	{
		std::string urlstr = url;
		urlstr += std::to_string(9999999 + i);
		v2.push_back(urlstr);
	}

	size_t n2 = 0;
	for (auto&amp; str : v2)
	{
		if (bf.test(str))
		{
			n2++; //误判
		}
	}
	cout &lt;&lt; "相似字符串误判率: " &lt;&lt; (double)n2 / (double)N &lt;&lt; endl;

	//不同前缀不同后缀的不相似串
	std::vector&lt;std::string&gt; v3;
	for (size_t i = 0; i &lt; N; i++)
	{
		string url = "baidu.com";
		url += std::to_string(i + rand());
		v3.push_back(url);
	}

	size_t n3 = 0;
	for (auto&amp; str : v3)
	{
		if (bf.test(str))
		{
			n3++; //误判
		}
	}
	cout &lt;&lt; "不相似字符串误判率: " &lt;&lt; (double)n3 / (double)N &lt;&lt; endl;
}
```

### 2.4 应用

布隆过滤器主要用于可以接受一定程度误判的场景，例如取名系统

所有已经有人使用过的昵称存储在服务器的数据库中，如果每次用户取名都要从数据库中查找该昵称是否被使用的话效率较低。

于是我们可以使用布隆过滤器，如果某个昵称没有被使用过，布隆过滤器的结果是准确的，那么就可以把结果直接返回给用户而不用访问数据库。

如果某个昵称判断已经被使用过了，这种情况存在误判的概率，那我们就继续在数据库中查找，以保证结果的准确性。

布隆过滤器的价值在于，其可以**过滤掉所有准确的情况，只针对可能存在的误判进行二次的确认**。

完.
