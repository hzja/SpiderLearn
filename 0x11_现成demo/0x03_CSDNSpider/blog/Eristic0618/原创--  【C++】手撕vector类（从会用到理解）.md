# 原创
：  【C++】手撕vector类（从会用到理解）

# 【C++】手撕vector类（从会用到理解）

[一、标准库中的vector类](#%E4%B8%80%E3%80%81%E6%A0%87%E5%87%86%E5%BA%93%E4%B8%AD%E7%9A%84vector%E7%B1%BB)

[1.1 vector类介绍](#1.1%20vector%E7%B1%BB%E4%BB%8B%E7%BB%8D)

[1.2 vector的常用接口](#1.2%20vector%E7%9A%84%E5%B8%B8%E7%94%A8%E6%8E%A5%E5%8F%A3)

[1.2.1 常用的构造函数](#1.2.1%20%E5%B8%B8%E7%94%A8%E7%9A%84%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)

[1.2.2 容量操作接口](#1.2.2%20%E5%AE%B9%E9%87%8F%E6%93%8D%E4%BD%9C%E6%8E%A5%E5%8F%A3)

[（1）size](#%EF%BC%881%EF%BC%89size)

[（2）capacity](#%EF%BC%882%EF%BC%89capacity)

[（3）empty](#%EF%BC%883%EF%BC%89empty)

[（4）resize](#%EF%BC%884%EF%BC%89resize)

[（5）reserve](#%EF%BC%885%EF%BC%89reserve)

[1.2.3 访问和遍历](#1.2.3%20%E8%AE%BF%E9%97%AE%E5%92%8C%E9%81%8D%E5%8E%86)

[（1）operator[]](#%EF%BC%881%EF%BC%89operator%5B%5D)

[（2）迭代器](#%EF%BC%882%EF%BC%89%E8%BF%AD%E4%BB%A3%E5%99%A8)

[（3）at](#%EF%BC%883%EF%BC%89at)

[（4）back](#%EF%BC%884%EF%BC%89back)

[（5）front](#%EF%BC%885%EF%BC%89front)

[1.2.4 vector的增删查改](#1.2.4%20vector%E7%9A%84%E5%A2%9E%E5%88%A0%E6%9F%A5%E6%94%B9)

[（1）push_back](#%EF%BC%881%EF%BC%89push_back)

[（2）pop_back](#%EF%BC%882%EF%BC%89pop_back)

[（3）find](#%EF%BC%883%EF%BC%89find)

[（4）insert](#%EF%BC%884%EF%BC%89insert)

[（5）erase](#%EF%BC%885%EF%BC%89erase)

[（6）swap](#%EF%BC%886%EF%BC%89swap)

[（7）assign](#%EF%BC%887%EF%BC%89assign)

[（8）clear](#%EF%BC%888%EF%BC%89clear)

[1.3 迭代器失效](#1.3%20%E8%BF%AD%E4%BB%A3%E5%99%A8%E5%A4%B1%E6%95%88)

[二、模拟实现vector类](#%E4%BA%8C%E3%80%81%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0vector%E7%B1%BB)

---


## 一、标准库中的vector类

### 1.1 vector类介绍

vector用于表示大小可以变化的数组。 

与数组类似，vector也采用连续的存储空间来存储元素，也就是说我们可以和数组一样使用下标对vector进行随机访问。但是相对于不能改变空间大小的数组而言，vector的优势在于它的大小可以动态改变。

前面我们学习了string类，对于同样使用顺序表结构的vector类而言，二者的很多地方是相通的，例如vector也可以进行尾插和尾删等操作。

vector是一个模板类，在使用时我们需要给出元素的类型。

vector类中通常有三个迭代器类型的成员变量，分别指向vector的开头、最后一个有效元素的后一位和vector的结尾

```
iterator _start;
iterator _finish;
iterator _end_of_storage;
```

所以，vector的有效元素个数就等于_finish - _start，容量等于_end_of_storage - _start

我们通过vector类中的接口就能对这三个迭代器进行操作，从而完成增删查改等功能

在使用vector类时，必须包含头文件&lt;vector&gt;和using namespace std;

### 1.2 vector的常用接口

#### 1.2.1 常用的构造函数

> 
**vector();**


vector类的默认构造函数，构造一个没有元素的空容器

例如：

> 
**vector(size_type n, const value_type&amp; val = value_type());**


构造一个vector类对象并用n个val初始化

例如：

> 
**vector(const vector&amp; x);**


vector类的拷贝构造函数

例如：

> 
**Template&lt;class InputIterator&gt;**
**vector(InputIterator first, InputIterator last);**


使用迭代器进行初始化构造

例如：

#### 1.2.2 容量操作接口

##### （1）size

> 
**size_type size() const;**


获取有效元素个数

例如：

##### （2）capacity

> 
**size_type capacity() const;**


获取容量大小

例如：

##### （3）empty

> 
**bool empty() const;**


判断容器是否为空

例如：

##### （4）resize

> 
**void resize(size_type n, value_type val = value_type());**


将有效元素的个数修改为n，并且如果n大于原来的size，多出来的地方用val填充

如果没有给出val，就用0填充

例如：

##### （5）reserve

> 
**void reserve(size_type n);**


改变容量大小

例如：

#### 1.2.3 访问和遍历

##### （1）operator[]

> 
**reference operator[](size_type n);**
**const_reference operator[](size_type n) const;**


用下标访问vector

例如：

##### （2）迭代器

> 
**iterator begin();**
**const_iterator begin() const;**
**iterator end();**
**const_iterator end() const;**


迭代器，用于获取容器中第一个元素的位置和最后一个元素的**下一个位置**

例如：

> 
**reverse_iterator rbegin();**
**const_reverse_iterator rbegin() const;**
**reverse_iterator rend();**
**const_reverse_iterator rend() const;**


反向迭代器，rbegin获取容器中最后一个元素的位置，rend获取容器中的第一个元素的前一个位置

例如：

需要注意，反向迭代器rit也要用++而不是--

##### （3）at

> 
**reference at(size_type n);**
**const_reference at(size_type n) const;**


返回容器中位置n处的元素的引用

例如：

##### （4）back

> 
**reference back();**
**const_reference back() const;**


返回容器中最后一个元素的引用

例如：

##### （5）front

> 
**reference front();**
**const_reference front() const;**


返回容器中第一个元素的引用

例如：

#### 1.2.4 vector的增删查改

##### （1）push_back

> 
**void push_back(const value_type&amp; val);**


从容器尾部插入一个元素

例如：

##### （2）pop_back

> 
**void pop_back();**


从容器尾部删除一个元素

例如：

##### （3）find

> 
**template &lt;class InputIterator, class T&gt;**
**InputIterator find(InputIterator first, InputIterator last, const T&amp; val);**


在两个迭代器区间寻找val并返回其所在处的迭代器

例如：

需要注意的是，该函数**并非vector的成员函数**，是标准库中的函数，多个容器共用该find函数

##### （4）insert

> 
**iterator insert(iterator position, const value_type&amp; val);**
**void insert(iterator position, size_type n, const value_type&amp; val);**


在position位置插入元素

例如：

对于这类可能会修改容量的函数，容易导致迭代器失效的问题，后面我们会详细讲

所以insert函数不仅需要完成插入元素的工作，有时还需要返回新的迭代器

##### （5）erase

> 
**iterator erase(iterator position);**
**iterator erase(iterator first, iterator last);**


删除position位置的元素或者 [first，last) 区间的所有元素

例如：

##### （6）swap

> 
**void swap(vector&amp; x);**


交换两个vector的数据空间

例如：

##### （7）assign

> 
**template &lt;class InputIterator&gt;**
**void assign(InputIterator first, InputIterator last);**
**void assign(size_type n, const value_type&amp; val);**


为vector指定新内容，替换其当前内容并修改size

例如：

##### （8）clear

> 
**void clear();**


从vector中删除所有元素，不改变容量大小

例如：

 

### 1.3 迭代器失效

迭代器的底层实际上就是一个指针或指针的封装，例如vector的迭代器就是一个原生态指针

当迭代器底层的指针指向的空间被销毁时，如果继续在程序中使用该迭代器，就会造成程序崩溃，这就是**迭代器失效**

对于vector，会导致迭代器失效的操作有：

以上函数在使用时都可能会导致vector扩容，在扩容时原空间会被释放，迭代器就会指向一块被释放的空间

假设有迭代器pos，使用pos删除pos对应位置的元素后，该迭代器对应的元素发生改变，属于迭代器失效

如果pos刚好对应最后一个元素，删除后迭代器pos就超出了有效元素范围，可能导致非法访问，属于迭代器失效

迭代器失效后，如果我们需要继续使用迭代器，给迭代器重新赋值即可

---


## 二、模拟实现vector类

知道了vector类中各种常用接口的用法后，我们就可以开始自己手撕一个自己的vector类了

为了不和标准库中的vector类冲突，我们可以开一个自己的命名空间

```
#include &lt;iostream&gt;
#include &lt;assert.h&gt;
#include &lt;string&gt;
using namespace std;

namespace Eristic
{
	template&lt;class T&gt;
	class vector
	{
	public:
		typedef T* iterator;
		typedef const T* const_iterator;

		vector()
			//此处包括下面的初始化列表都可以换用缺省值
			:_start(nullptr)
			,_finish(nullptr)
			,_end_of_storage(nullptr)
		{}

		vector(size_t n, const T&amp; val = T())
			:_start(nullptr)
			, _finish(nullptr)
			, _end_of_storage(nullptr)
		{
			reserve(n);
			for (size_t i = 0; i &lt; n; ++i)
			{
				push_back(val);
			}
		}

		vector(int n, const T&amp; val = T())
			:_start(nullptr)
			, _finish(nullptr)
			, _end_of_storage(nullptr)
		{
			reserve(n);
			for (int i = 0; i &lt; n; ++i)
			{
				push_back(val);
			}
		}

		vector(const vector&lt;T&gt;&amp; v)
			:_start(nullptr)
			, _finish(nullptr)
			, _end_of_storage(nullptr)
		{
			reserve(v.capacity());
			for (size_t i = 0; i &lt; v.size(); ++i)
			{
				_start[i] = v._start[i];
			}
			_finish = _start + v.size();
		}

		template &lt;class InputIterator&gt;
		vector(InputIterator first, InputIterator last)
			:_start(nullptr)
			, _finish(nullptr)
			, _end_of_storage(nullptr)
		{
			while (first != last)
			{
				push_back(*first);
				++first;
			}
		}

		vector&lt;T&gt;&amp; operator=(vector&lt;T&gt;&amp; v)
		{
			if (this != &amp;v)
			{
				reserve(v.capacity());
				for (size_t i = 0; i &lt; v.size(); ++i)
				{
					_start[i] = v._start[i];
				}
				_finish = _start + v.size();
				return *this;
			}
		}

		iterator begin()
		{
			return _start;
		}

		const_iterator cbegin() const
		{
			return _start;
		}

		iterator end()
		{
			return _finish;
		}

		const_iterator cend() const
		{
			return _finish;
		}

		size_t capacity() const
		{
			return _end_of_storage - _start;
		}

		size_t size() const
		{
			return _finish - _start;
		}

		void reserve(size_t n)
		{
			if (n &gt; capacity())
			{
				T* tmp = new T[n];
				size_t sz = size();
				if (_start)
				{
					for (size_t i = 0; i &lt; sz; ++i)
					{
						tmp[i] = _start[i];
					}
					delete[] _start;
				}
				_start = tmp;
				_finish = _start + sz;
				_end_of_storage = _start + n;
			}
		}

		void resize(size_t n, T val = T())
		{
			if (n &lt; size())
			{
				_finish = _start + n;
			}
			if (n &gt; size())
			{
				if (n &gt; capacity())
					reserve(n);
				while (_finish != _start + n)
				{
					*_finish = val;
					++_finish;
				}
			}
		}

		bool empty() const
		{
			return _start == _finish;
		}

		void push_back(const T&amp; x)
		{
			if (_finish == _end_of_storage)
			{
				reserve(capacity() == 0 ? 4 : capacity() * 2);
			}
			*_finish = x;
			++_finish;
		}

		void pop_back()
		{
			assert(!empty());
			--_finish;
		}

		void swap(vector&lt;T&gt;&amp; v)
		{
			std::swap(_start, v._start);
			std::swap(_finish, v._finish);
			std::swap(_end_of_storage, v._end_of_storage);
		}

		iterator insert(iterator pos, const T&amp; val)
		{
			assert(pos &gt;= _start);
			assert(pos &lt;= _finish);
			if (_finish == _end_of_storage)
			{
				size_t range = pos - _start; //在扩容前需要记录相对位置
				//在插入数据时发生了扩容，迭代器的位置会发生改变,叫做迭代器失效
				reserve(capacity() == 0 ? 4 : capacity() * 2);
				pos = _start + range; //将pos也更新到新的位置
			}
			iterator end = _finish;
			while (end &gt; pos)
			{
				*end = *(end - 1);
				--end;
			}
			*pos = val;
			++_finish;
			return pos;
		}

		iterator erase(iterator pos)
		{
			assert(pos &gt;= _start);
			assert(pos &lt; _finish);
			iterator start = pos + 1;
			while (start &lt; _finish)
			{
				*(start - 1) = *start;
				++start;
			}
			--_finish;
			return pos;
		}

		T&amp; front()
		{
			return *_start;
		}

		const T&amp; front() const
		{
			return *_start;
		}

		T&amp; back()
		{
			return *(_finish - 1);
		}

		const T&amp; back() const
		{
			return *(_finish - 1);
		}

		T&amp; operator[](size_t pos)
		{
			assert(pos &lt; size());
			return _start[pos];
		}

		const T&amp; operator[](size_t pos) const
		{
			assert(pos &lt; size());
			return _start[pos];
		}

		~vector()
		{
			delete[] _start;
			_start = _finish = _end_of_storage = nullptr;
		}

	private:
		iterator _start;
		iterator _finish;
		iterator _end_of_storage;
	};
}

```

如有错误，欢迎在评论区指出

完.
