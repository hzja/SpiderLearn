# 原创
：  【C++】哈希表

# 【C++】哈希表

**目录**

[一、unordered系列关联式容器](#%E4%B8%80%E3%80%81unordered%E7%B3%BB%E5%88%97%E5%85%B3%E8%81%94%E5%BC%8F%E5%AE%B9%E5%99%A8)

[二、哈希](#%E4%BA%8C%E3%80%81%E5%93%88%E5%B8%8C)

[2.1 概念](#2.1%20%E6%A6%82%E5%BF%B5)

[2.2 哈希冲突](#2.2%20%E5%93%88%E5%B8%8C%E5%86%B2%E7%AA%81)

[2.3 哈希函数](#2.3%20%E5%93%88%E5%B8%8C%E5%87%BD%E6%95%B0)

[（1）直接定址法](#%EF%BC%881%EF%BC%89%E7%9B%B4%E6%8E%A5%E5%AE%9A%E5%9D%80%E6%B3%95)

[（2）除留余数法](#%EF%BC%882%EF%BC%89%E9%99%A4%E7%95%99%E4%BD%99%E6%95%B0%E6%B3%95)

[（3）平方取中法](#%EF%BC%883%EF%BC%89%E5%B9%B3%E6%96%B9%E5%8F%96%E4%B8%AD%E6%B3%95)

[（4）折叠法](#%EF%BC%884%EF%BC%89%E6%8A%98%E5%8F%A0%E6%B3%95)

[（5）随机数法](#%EF%BC%885%EF%BC%89%E9%9A%8F%E6%9C%BA%E6%95%B0%E6%B3%95)

[（6）数学分析法](#%EF%BC%886%EF%BC%89%E6%95%B0%E5%AD%A6%E5%88%86%E6%9E%90%E6%B3%95)

[三、哈希冲突解决方案](#%E4%B8%89%E3%80%81%E5%93%88%E5%B8%8C%E5%86%B2%E7%AA%81%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)

[3.1 闭散列](#3.1%20%E9%97%AD%E6%95%A3%E5%88%97)

[3.1.1 线性探测](#3.1.1%20%E7%BA%BF%E6%80%A7%E6%8E%A2%E6%B5%8B)

[（1）处理不同类型的key](#%EF%BC%881%EF%BC%89%E5%A4%84%E7%90%86%E4%B8%8D%E5%90%8C%E7%B1%BB%E5%9E%8B%E7%9A%84key)

[（2）插入元素](#%EF%BC%882%EF%BC%89%E6%8F%92%E5%85%A5%E5%85%83%E7%B4%A0)

[（3）删除元素](#%EF%BC%883%EF%BC%89%E5%88%A0%E9%99%A4%E5%85%83%E7%B4%A0)

[（4）扩容](#%EF%BC%884%EF%BC%89%E6%89%A9%E5%AE%B9)

[（5）总结](#%EF%BC%885%EF%BC%89%E6%80%BB%E7%BB%93)

[3.1.2 线性探测模拟实现闭散列](#3.1.2%20%E7%BA%BF%E6%80%A7%E6%8E%A2%E6%B5%8B%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0%E9%97%AD%E6%95%A3%E5%88%97)

[3.1.3 二次探测](#3.1.3%20%E4%BA%8C%E6%AC%A1%E6%8E%A2%E6%B5%8B)

[3.2 开散列](#3.2%20%E5%BC%80%E6%95%A3%E5%88%97)

[3.2.1 概念 ](#3.2.1%20%E6%A6%82%E5%BF%B5%C2%A0)

[3.2.2 模拟实现开散列](#3.2.2%20%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0%E5%BC%80%E6%95%A3%E5%88%97)

[四、模拟实现哈希表和Unordered系列关联式容器](#%E5%9B%9B%E3%80%81%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0%E5%93%88%E5%B8%8C%E8%A1%A8%E5%92%8CUnordered%E7%B3%BB%E5%88%97%E5%85%B3%E8%81%94%E5%BC%8F%E5%AE%B9%E5%99%A8)

[4.1 HashTable.h](#4.1%20HashTable.h)

[4.2 Unordered_Set.h](#4.2%20Unordered_Set.h)

[4.3 Unordered_Map.h](#4.3%C2%A0Unordered_Map.h)

---


## 一、unordered系列关联式容器

在C++的STL库中，除了底层为红黑树结构的map和set，还有底层为**哈希表**的unordered_map和unordered_set

由于红黑树的性质，我们遍历map和set会得到一个有序的序列

而顾名思义，我们遍历unordered_map和unordered_set得到的是一个**无序**的序列。这两个容器的使用方式与map和set类似，只是底层结构不同，这里就不对二者的使用方式做详细介绍了

---


## 二、哈希

### 2.1 概念

在顺序结构以及平衡树中，元素的**key**和其**存储的位置**之间没有关联，因此在查找某个元素时需要经过多次对key的**比较**。所以搜索的效率取决于搜索过程中的比较次数。在依靠比较的排序算法中，其排序效率也取决于排序过程中元素的比较次数。

是否有一种方法能够不经过任何比较，就能直接知道要查找的元素位置，从而在**O(1)的时间复杂度**内得到要查找的元素呢？

我们可以构造一种存储结构，通过某种**函数**能够使元素的存储位置和它的key之间建立一个**映射关系**，那么在查找该元素时就能直接通过key得到它的存储位置。

这种方法就是**哈希**（Hash），又称为散列。哈希是一个广义的算法，也可以认为是一种思想

哈希算法中使用的将元素的存储位置和key建立映射的函数称为**哈希函数**或散列函数，构造出的结构称为**哈希表**（Hash Table）或**散列表**。

以26个英文字母为例，我们可以用一个大小为26的数组来存储它们，将每一个下标都与一个字母建立映射关系，例如0为a，1为b。这种线性的映射关系适用于key的范围小且连续的情况，称为**直接定址法**，在后面会介绍。

又例如计数排序，就是对哈希直接定址法的变形应用。将每个元素与其存储的位置建立映射关系，然后统计这个元素出现的次数。

### 2.2 哈希冲突

有时，key的范围较大且过于分散，如果此时还使用直接定址法，就会导致空间的浪费。

例如：

此时我们可以使用**除留余数法**，将key除以一个不大于散列表长度的数，将所得的余数作为映射的哈希地址

将key除以散列表的长度，就使一个范围大且分散的集合存储到一个较小的散列表中了

但是此时出现了一个问题：有不同的值映射到相同的位置上了

这就是**哈希冲突**（哈希碰撞），即不同的key通过哈希函数计算出了相同的哈希地址，我们把key不同但哈希地址相同的元素称为**同义词**

### 2.3 哈希函数

哈希函数是一种建立映射关系的方法，我们使用某种特定的方法处理key得到相对应的哈希地址

常见的哈希函数有：

#### （1）直接定址法

key和哈希地址之间是线性的映射关系，适用于key的**范围较小且连续**的情况。key和哈希地址是**一对一**的关系，不存在哈希冲突

#### （2）除留余数法

设散列表的大小为m，取一个不大于m（接近m或等于m）的质数p作为除数，将key除以p后得到的**余数**作为哈希地址。key和哈希地址是**多对一**的关系，存在哈希冲突

#### （3）平方取中法

对key取平方，取其**平方后的中间几位**作为哈希地址

适合不知道key的分布且key的位数不大的情况

#### （4）折叠法

将key从左到右分割成位数相等的几部分，然后将这几部分**叠加求和**，并按散列表长度**取后几位作为哈希地址**

#### （5）随机数法

选择一个随机函数，**取key的随机函数值**作为它的哈希地址

#### （6）数学分析法

找出key中数字的规律，选择**数字差别较大的几位**作为哈希地址

例如不同电话号的前几位容易重复，但后四位不容易重复，所以我们可以取后四位作为哈希地址

---


## 三、哈希冲突解决方案

解决哈希冲突的两种常见方法：**闭散列**和**开散列**

### 3.1 闭散列

闭散列又称开放定址法。当发送哈希冲突时，如果散列表未满，那么就把出现冲突的key存放到冲突位置的**下一个空位置**中

如何寻找下一个空位置呢？

#### 3.1.1 线性探测

线性探测就是**从发生冲突的位置开始依次向后探测**，**直到寻找到下一个空位置**

##### （1）处理不同类型的key

在使用map、set或者unordered_map、unordered_set时，我们可以将字符串或者浮点数作为key

也就是说，我们的**key不一定是整数**。此时就需要在建立映射前对key进行处理。

针对浮点数等非字符串类型的key，我们可以直接**强转为size_t类型**

针对字符串类型的key，我们可以使用**字符串哈希**，也就是把一个字符串映射成一个数

此处我们使用BKDR字符串哈希：

```
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
```

[各种字符串Hash函数比较 (byvoid.com)<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://byvoid.com/zhs/blog/string-hash-compare/](https://byvoid.com/zhs/blog/string-hash-compare/)

##### （2）插入元素

先通过哈希函数获取待插入元素在哈希表中的位置，如果该位置为空则直接插入，如果有元素则使用线性探测找到下一个空位置再插入

举一个除留余数法的例子：

4444通过哈希函数计算哈希地址，应该插入下标为4的位置，但该位置已经有元素了，此时发生哈希冲突。

使用线性探测从下标为4的位置向后寻找空位置，找到第一个空位即下标为6的位置，将4444插入

我们如何保证哈希表中一定有空位置呢？这里引入一个概念，即**负载因子**

**负载因子：哈希表存储元素的个数 / 哈希表大小**

如果**负载因子太大**（相同大小的哈希表中存储更多的key），可以提高空间利用率，但是冲突的概率大大增加，降低效率

如果**负载因子太小**（相同大小的哈希表中存储更少的key），可以降低冲突的概率，但是空间利用率也会降低

我们只要保证哈希表存储元素的个数除以哈希表的大小不超过负载因子，一旦超过负载因子则扩容，就能够确保哈希表中一定有空位置，并且冲突的概率保持在一个合理的范围

##### （3）删除元素

采用闭散列处理哈希冲突时，我们要如何删除哈希表中已有的元素呢？

如果采用置零或者置为-1的方式是行不通的，因为你无法通过该位置的key判断是否是删除后的值还是原本存储的值

我们可以为哈希表的每个位置**设置一个标记**，**空为EMPTY**，**有元素的话标记为EXIST**

这样就行了吗？如果我们把删除后的位置从EXIST重新标记为EMPTY，那么在搜索元素时可能会出现错误判断的情况。我们以上面的情况为例：

删除34后，下标为4的位置被置为EMPTY。当我们搜索4444时，因为下标为4的位置标记为EMPTY，所以判断哈希表中没有4444

实际上4444因为哈希冲突被我们使用线性探测放到了后面

所以只有EMPTY和EXIST两种标记是不够的，我们需要采用**伪删除法**来删除元素，即多增加一个**DELETE标记表示该位置曾经有元素但已被删除**，当搜索的位置标记为DELETE时需要继续向后搜索。

##### （4）扩容

当哈希表存储元素的个数除以哈希表的大小超过了负载因子，就需要进行扩容

但是如果我们用除留余数法，将哈希表长度作为除数时，就不能直接在原地进行resize扩容。因为扩容后长度发送变化，**映射关系也会改变**。

所以在扩容时我们需要**先开一块新空间，重新建立映射关系，再释放旧空间**。

##### （5）总结

线性探测的优点很明显：实现简单

缺点也很明显：容易发生一连串的哈希冲突，与其逐个向后寻找下一个空位置的方式有关

#### 3.1.2 线性探测模拟实现闭散列

```
namespace open_address // 开放定址法
{
	enum Status
	{
		EMPTY, // 空
		EXIST, // 已有值
		DELETE // 曾经存过值但已被删除
	};

	template&lt;class K, class V&gt;
	struct HashData
	{
		pair&lt;K, V&gt; _kv;
		Status _s; // 目标位置的状态
	};

	template&lt;class K&gt;
	struct HashMapping
	{
		size_t operator()(const K&amp; key)
		{
			return (size_t)key; // 把其他类型的key都强转成无符号整形
		}
	};

	template&lt;&gt;
	struct HashMapping&lt;string&gt; // 如果key是string类型的就无法用上面的仿函数来转换了，所以写一个特化版本的
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

	template&lt;class K, class V, class Hash = HashMapping&lt;K&gt;&gt; // key不一定是整型，需要一个仿函数转换key的类型便于建立映射
	class HashTable
	{
	public:
		HashTable()
		{
			_tables.resize(10);
		}

		bool Insert(const pair&lt;K, V&gt;&amp; kv)
		{
			if (Find(kv.first)) return false;
			if (_n * 10 / _tables.size() == 7) // 负载因子到达0.7，扩容
			{
				// 不能直接在原基础上扩容，否则映射关系改变后无法找到原值
				size_t newsize = _tables.size() * 2;
				HashTable&lt;K, V, Hash&gt; newTable;
				newTable._tables.resize(newsize);
				// 遍历旧表，将元素插入新表，重新建立映射
				for (size_t i = 0; i &lt; _tables.size(); i++)
				{
					if (_tables[i]._s == EXIST)
					{
						newTable.Insert(_tables[i]._kv); // 复用原函数
					}
				}
				_tables.swap(newTable._tables); // 新旧表交换
			}

			Hash hf;
			// 线性探测
			size_t hashI = hf(kv.first) % _tables.size(); // 用无符号可以映射负数
			while (_tables[hashI]._s == EXIST)
			{
				hashI++;
				hashI %= _tables.size();
			}

			_tables[hashI]._kv = kv;
			_tables[hashI]._s = EXIST;
			_n++;

			return true;
		}
		
		bool Erase(const K&amp; key)
		{
			HashData&lt;K, V&gt;* ret = Find(key); // 检测目标是否存在
			if (ret)
			{
				ret-&gt;_s = DELETE; // 伪修改：直接修改状态
				--_n;
				return true;
			}
			else return false;
		}

		HashData&lt;K, V&gt;* Find(const K&amp; key)
		{
			Hash hf;
			size_t hashI = hf(key) % _tables.size();
			while (_tables[hashI]._s != EMPTY) // 如果遍历到空位置还没找到则说明目标值不存在
			{
				if (_tables[hashI]._s == EXIST &amp;&amp; _tables[hashI]._kv.first == key) // 找到目标
				{
					return &amp;_tables[hashI];
				}
				hashI++;
				hashI %= _tables.size();
			}
			return nullptr;
		}

		void Print()
		{
			for (size_t i = 0; i &lt; _tables.size(); i++)
			{
				if (_tables[i]._s == EXIST)
					cout &lt;&lt; "[" &lt;&lt; i &lt;&lt; "]-&gt;" &lt;&lt; _tables[i]._kv.first &lt;&lt; ":" &lt;&lt; _tables[i]._kv.second &lt;&lt; endl;
				else if(_tables[i]._s == EMPTY)
					printf("[%d]-&gt;\n", i);
				else
					printf("[%d]-&gt;D\n", i);
			}
		}

	private:
		vector&lt;HashData&lt;K, V&gt;&gt; _tables;
		size_t _n; // 存储关键字个数
	};
}
```

#### 3.1.3 二次探测

线性探测在插入元素时逐个向后查找空位置，步长不变

二次探测相对线性探测的区别在于，在查找空位置时**跳跃式的前后交替查找**，每次的步长都是前一次的二次方

### 3.2 开散列

#### 3.2.1 概念 

**开散列法**又叫**链地址法**，用开散列法实现的哈希表又叫**哈希桶**

在哈希桶中，其**每一个位置都是一个链表**，原本会产生哈希冲突的、具有相同哈希地址的元素归并成一个集合，用链表链接起来，称为一个桶，并将各个链表的**头节点**存储在哈希表中

例如：

可以看到，原本在除留余数法下会发生哈希冲突的元素，此时都被放进了同一个桶中。所以哈希桶能够**完美解决哈希冲突**的问题

所以用开散列法插入元素和删除元素，按照链表的方式进行操作即可。需要注意的是，因为我们采用的是单链表，不好找尾，所以插入元素时应该**头插**

不断向哈希桶插入元素，虽然不会发生哈希冲突，但是可能会导致**某个桶过长**从而影响性能，所以哈希桶在一定条件下也需要进行扩容。

哈希桶的负载因子可以开到1，也就是**平均每个位置都有一个元素**。当达到条件时，首先创建一个新表，重新将每个节点映射到新表中，然后销毁旧表。

#### 3.2.2 模拟实现开散列

```
namespace hash_bucket // 哈希桶:数组加单链表
{
	template&lt;class K, class V&gt;
	struct HashNode
	{
		HashNode(const pair&lt;K, V&gt;&amp; kv)
			:_kv(kv)
			,_next(nullptr)
		{}

		pair&lt;K, V&gt; _kv;
		HashNode* _next;
	};

	template&lt;class K&gt;
	struct HashMapping
	{
		size_t operator()(const K&amp; key)
		{
			return (size_t)key;
		}
	};

	template&lt;&gt;
	struct HashMapping&lt;string&gt;
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

	template&lt;class K, class V, class Hash = HashMapping&lt;K&gt;&gt;
	class HashTable
	{
		typedef HashNode&lt;K, V&gt; Node;
	public:
		HashTable()
		{
			_tables.resize(10);
		}

		~HashTable() // vector可以自己析构，但哈希桶需要我们手动析构
		{
			for (size_t i = 0; i &lt; _tables.size(); i++)
			{
				Node* cur = _tables[i];
				while (cur)
				{
					Node* next = cur-&gt;_next;
					delete cur;
					cur = next;
				}
				_tables[i] = nullptr;
			}
		}

		bool Insert(const pair&lt;K, V&gt; kv)
		{
			if (Find(kv.first)) return false;

			Hash hf;
			if (_n == _tables.size()) // 负载因子为1时扩容
			{
				// 为了避免析构和重新创建节点的消耗，直接把旧表中的节点重新映射至新表
				vector&lt;Node*&gt; new_tables;
				new_tables.resize(_tables.size() * 2);
				// 遍历旧表
				for (size_t i = 0; i &lt; _tables.size(); i++)
				{
					Node* cur = _tables[i];
					while (cur)
					{
						Node* next = cur-&gt;_next; // 头插会改变节点的指向，所以需要保存next

						// 计算新的映射位置
						size_t new_hashi = hf(cur-&gt;_kv.first) % new_tables.size();
						cur-&gt;_next = new_tables[new_hashi];
						new_tables[new_hashi] = cur;

						cur = next;
					}
					_tables[i] = nullptr;
				}
				_tables.swap(new_tables);
			}

			size_t hashi = hf(kv.first) % _tables.size();
			Node* newnode = new Node(kv);
			// 哈希桶头插
			newnode-&gt;_next = _tables[hashi];
			_tables[hashi] = newnode;
			_n++;

			return true;
		}

		bool Erase(const K&amp; key)
		{
			Hash hf;
			size_t hashi = hf(key) % _tables.size();
			Node* prev = nullptr; // 单链表无法找头，需要提前保存
			Node* cur = _tables[hashi];
			while (cur)
			{
				if (cur-&gt;_kv.first == key)
				{
					if (prev == nullptr) // 待删除节点在头部
						_tables[hashi] = cur-&gt;_next;
					else
						prev-&gt;_next = cur-&gt;_next;
					delete cur;
					return true;
				}
				prev = cur;
				cur = cur-&gt;_next;
			}
			return false;
		}

		Node* Find(const K&amp; key)
		{
			Hash hf;
			size_t hashi = hf(key) % _tables.size();
			Node* cur = _tables[hashi];
			while (cur)
			{
				if (cur-&gt;_kv.first == key)
					return cur;
				cur = cur-&gt;_next;
			}
			return nullptr; 
		}

		void Print()
		{
			for (int i = 0; i &lt; _tables.size(); i++)
			{
				cout &lt;&lt; i &lt;&lt; " : ";
				Node* cur = _tables[i];
				while (cur)
				{
					cout &lt;&lt; "[" &lt;&lt; cur-&gt;_kv.first &lt;&lt; "," &lt;&lt; cur-&gt;_kv.second &lt;&lt; "]" &lt;&lt; "-&gt;";
					cur = cur-&gt;_next;
				}
				cout &lt;&lt; endl;
			}
			cout &lt;&lt; endl;
		}

		size_t size()
		{
			return _n;
		}

	private:
		vector&lt;Node*&gt; _tables;
		size_t _n = 0;
	};
}
```

---


## 四、模拟实现哈希表和Unordered系列关联式容器

### 4.1 HashTable.h

```
#pragma once

namespace hash_bucket // 哈希桶:数组加单链表
{
	template&lt;class T&gt;
	struct HashNode
	{
		HashNode(const T&amp; data)
			:_data(data)
			, _next(nullptr)
		{}

		T _data;
		HashNode&lt;T&gt;* _next;
	};

	template&lt;class K&gt;
	struct HashMapping
	{
		size_t operator()(const K&amp; key)
		{
			return (size_t)key;
		}
	};

	template&lt;&gt;
	struct HashMapping&lt;string&gt;
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

	// 迭代器和HashTable相互依赖：前置声明
	template&lt;class K, class T, class KeyOfT, class Hash&gt; //声明时不需要带缺省参数
	class HashTable;

	template&lt;class K, class T, class Ref, class Ptr, class KeyOfT, class Hash&gt;
	struct __HTIterator
	{
		typedef HashNode&lt;T&gt; Node;
		typedef __HTIterator&lt;K, T, Ref, Ptr, KeyOfT, Hash&gt; Self;

		//如果pht不定义为const变量，const版本的end和begin就无法使用构造函数（const this）,否则会发生权限放大
		__HTIterator(Node* node, const HashTable&lt;K, T, KeyOfT, Hash&gt;* pht, size_t hashi)
			:_node(node)
			, _pht(pht)
			, _hashi(hashi)
		{}

		Self&amp; operator++()
		{
			if (_node-&gt;_next)
				_node = _node-&gt;_next;
			else //当前的桶已走到底部
			{
				++_hashi; 
				while (_hashi &lt; _pht-&gt;_tables.size()) //找下一个非空的桶
				{
					if (_pht-&gt;_tables[_hashi])
					{
						_node = _pht-&gt;_tables[_hashi];
						break;
					}
					++_hashi;
				}
			} 

			if (_hashi == _pht-&gt;_tables.size()) //走到结束还没找到非空的桶
				_node = nullptr;

			return *this;
		}

		Ref operator*()
		{
			return _node-&gt;_data;
		}

		Ptr operator-&gt;()
		{
			return &amp;(_node-&gt;_data);
		}
		
		bool operator!=(const Self&amp; s)
		{
			return _node != s._node;
		}

		Node* _node;
		const HashTable&lt;K, T, KeyOfT, Hash&gt;* _pht;
		size_t _hashi;
	};

	template&lt;class K, class T, class KeyOfT, class Hash&gt; //KeyOfT传入仿函数用于取出key，Hash用于将key转化为合适的值
	class HashTable
	{
		template&lt;class K, class T, class Ref, class Ptr, class KeyOfT, class Hash&gt;
		friend struct __HTIterator; //迭代器需要访问私有成员_tables，需要成为HashTable的友元

		typedef HashNode&lt;T&gt; Node;
	public:
		typedef __HTIterator&lt;K, T, T&amp;, T*, KeyOfT, Hash&gt; iterator;
		typedef __HTIterator&lt;K, T, const T&amp;, const T*, KeyOfT, Hash&gt; const_iterator;

		iterator begin()
		{
			for (size_t i = 0; i &lt; _tables.size(); i++) //找到第一个不为空的桶
			{
				if (_tables[i])
					return iterator(_tables[i], this, i);
			}
			return end(); //如果表为空则返回end()
		}

		iterator end()
		{
			return iterator(nullptr, this, -1);
		}

		const_iterator begin() const
		{
			for (size_t i = 0; i &lt; _tables.size(); i++)
			{
				if (_tables[i])
					return const_iterator(_tables[i], this, i);
			}
			return end();
		}

		const_iterator end() const
		{
			return const_iterator(nullptr, this, -1);
		}

		HashTable()
		{
			_tables.resize(10);
		}

		~HashTable() // vector可以自己析构，但哈希桶需要我们手动析构
		{
			for (size_t i = 0; i &lt; _tables.size(); i++)
			{
				Node* cur = _tables[i];
				while (cur)
				{
					Node* next = cur-&gt;_next;
					delete cur;
					cur = next;
				}
				_tables[i] = nullptr;
			}
		}

		pair&lt;iterator, bool&gt; Insert(const T&amp; data)
		{
			KeyOfT kot;
			Hash hf;

			iterator it = Find(kot(data));
			if (it != end()) return make_pair(it, false); //如果data已存在则返回对应位置的迭代器和false

			if (_n == _tables.size()) // 负载因子为1时扩容
			{
				// 为了避免析构和重新创建节点的消耗，直接把旧表中的节点重新映射至新表
				vector&lt;Node*&gt; new_tables;
				new_tables.resize(_tables.size() * 2);
				// 遍历旧表
				for (size_t i = 0; i &lt; _tables.size(); i++)
				{
					Node* cur = _tables[i];
					while (cur)
					{
						Node* next = cur-&gt;_next; // 头插会改变节点的指向，所以需要保存next

						// 计算新的映射位置
						size_t new_hashi = hf(kot(cur-&gt;_data)) % new_tables.size();
						cur-&gt;_next = new_tables[new_hashi];
						new_tables[new_hashi] = cur;

						cur = next;
					}
					_tables[i] = nullptr;
				}
				_tables.swap(new_tables);
			}

			size_t hashi = hf(kot(data)) % _tables.size();
			Node* newnode = new Node(data);
			// 哈希桶头插
			newnode-&gt;_next = _tables[hashi];
			_tables[hashi] = newnode;
			_n++;

			return make_pair(iterator(newnode, this, hashi), true); //返回data插入位置的迭代器和true
		}

		bool Erase(const K&amp; key)
		{
			KeyOfT kot;
			Hash hf;
			size_t hashi = hf(key) % _tables.size();
			Node* prev = nullptr; // 单链表无法找头，需要提前保存
			Node* cur = _tables[hashi];
			while (cur)
			{
				if (kot(cur-&gt;_data) == key)
				{
					if (prev == nullptr) // 待删除节点在头部
						_tables[hashi] = cur-&gt;_next;
					else
						prev-&gt;_next = cur-&gt;_next;
					delete cur;
					return true;
				}
				prev = cur;
				cur = cur-&gt;_next;
			}
			return false;
		}

		iterator Find(const K&amp; key)
		{
			KeyOfT kot;
			Hash hf;
			size_t hashi = hf(key) % _tables.size(); //建立映射
			Node* cur = _tables[hashi];
			while (cur) //在对应的桶中查找
			{
				if (kot(cur-&gt;_data) == key)
					return iterator(cur, this, hashi);
				cur = cur-&gt;_next;
			}
			return end();
		}

		size_t size()
		{
			return _n;
		}

	private:
		vector&lt;Node*&gt; _tables;
		size_t _n = 0;
	};
}
```

### 4.2 Unordered_Set.h

```
#pragma once
#include "HashTable.h"

namespace Eristic
{
	template&lt;class K, class Hash = hash_bucket::HashMapping&lt;K&gt;&gt;
	class unordered_set
	{
		struct Unordered_Set_KeyOfT
		{
			const K&amp; operator()(const K&amp; key)
			{
				return key;
			}
		};

	public:
		//用typename说明此处是对类型重命名
		typedef typename hash_bucket::HashTable&lt;K, K, Unordered_Set_KeyOfT, Hash&gt;::const_iterator iterator; //set禁止修改，所以只有const迭代器
		typedef typename hash_bucket::HashTable&lt;K, K, Unordered_Set_KeyOfT, Hash&gt;::const_iterator const_iterator;

		const_iterator begin() const
		{
			return _ht.begin();
		}

		const_iterator end() const
		{
			return _ht.end();
		}

		pair&lt;iterator, bool&gt; insert(const K&amp; key)
		{
			auto ret = _ht.Insert(key);
			//HashTable中的Insert返回的是普通迭代器，而set中只有const迭代器，需要进行类型转换
			return pair&lt;iterator, bool&gt;(iterator(ret.first._node, ret.first._pht, ret.first._hashi), ret.second);
		}

		iterator find(const K&amp; key)
		{
			return _ht.Find(key);
		}

		bool erase(const K&amp; key)
		{
			return _ht.Erase(key);
		}

	private:
		hash_bucket::HashTable&lt;K, K, Unordered_Set_KeyOfT, Hash&gt; _ht;
	};
}
```

### 4.3 Unordered_Map.h

```
#pragma once
#include "HashTable.h"

namespace Eristic
{
	template&lt;class K, class V, class Hash = hash_bucket::HashMapping&lt;K&gt;&gt;
	class unordered_map
	{
		struct Unordered_Map_KeyOfT
		{
			const K&amp; operator()(const pair&lt;K, V&gt;&amp; kv)
			{
				return kv.first;
			}
		};

	public:
		typedef typename hash_bucket::HashTable&lt;K, pair&lt;const K, V&gt;, Unordered_Map_KeyOfT, Hash&gt;::iterator iterator;
		typedef typename hash_bucket::HashTable&lt;K, pair&lt;const K, V&gt;, Unordered_Map_KeyOfT, Hash&gt;::const_iterator const_iterator;

		iterator begin()
		{
			return _ht.begin();
		}

		iterator end()
		{
			return _ht.end();
		}

		pair&lt;iterator, bool&gt; insert(const pair&lt;K, V&gt;&amp; kv)
		{
			return _ht.Insert(kv);
		}

		iterator find(const K&amp; key)
		{
			return _ht.Find(key);
		}

		bool erase(const K&amp; key)
		{
			return _ht.Erase(key);
		}

		V&amp; operator[](const K&amp; key)
		{
			pair&lt;iterator, bool&gt; ret = _ht.Insert(make_pair(key, V()));
			return ret.first-&gt;second;
		}

	private:
		hash_bucket::HashTable&lt;K, pair&lt;const K, V&gt;, Unordered_Map_KeyOfT, Hash&gt; _ht;
	};
}
```

完.
