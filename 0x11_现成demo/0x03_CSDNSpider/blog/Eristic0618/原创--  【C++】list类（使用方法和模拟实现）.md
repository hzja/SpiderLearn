# 原创
：  【C++】list类（使用方法和模拟实现）

# 【C++】list类（使用方法和模拟实现）

[一、标准库中的list类](#%E4%B8%80%E3%80%81%E6%A0%87%E5%87%86%E5%BA%93%E4%B8%AD%E7%9A%84list%E7%B1%BB)

[1.1 list类介绍](#1.1%20list%E7%B1%BB%E4%BB%8B%E7%BB%8D)

[1.2 list的常用接口](#1.2%20list%E7%9A%84%E5%B8%B8%E7%94%A8%E6%8E%A5%E5%8F%A3)

[1.2.1 常用的构造函数](#1.2.1%20%E5%B8%B8%E7%94%A8%E7%9A%84%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)

[1.2.2 容量操作接口](#1.2.2%20%E5%AE%B9%E9%87%8F%E6%93%8D%E4%BD%9C%E6%8E%A5%E5%8F%A3)

[（1）size](#%EF%BC%881%EF%BC%89size)

[（2）empty](#%EF%BC%882%EF%BC%89empty)

[（3）resize](#%EF%BC%883%EF%BC%89resize)

[1.2.3 访问和遍历](#1.2.3%20%E8%AE%BF%E9%97%AE%E5%92%8C%E9%81%8D%E5%8E%86)

[（1）迭代器](#%EF%BC%882%EF%BC%89%E8%BF%AD%E4%BB%A3%E5%99%A8)

[（2）反向迭代器](#%EF%BC%882%EF%BC%89%E5%8F%8D%E5%90%91%E8%BF%AD%E4%BB%A3%E5%99%A8)

[（3）back](#%EF%BC%883%EF%BC%89back)

[（4）front](#%EF%BC%884%EF%BC%89front)

[1.2.4 list的增删查改](#1.2.4%20list%E7%9A%84%E5%A2%9E%E5%88%A0%E6%9F%A5%E6%94%B9)

[（1）push_front](#%EF%BC%881%EF%BC%89push_front)

[（2）pop_front](#%EF%BC%882%EF%BC%89pop_front)

[（3）push_back](#%EF%BC%883%EF%BC%89push_back)

[（4）pop_back](#%EF%BC%884%EF%BC%89pop_back)

[（5）find](#%EF%BC%885%EF%BC%89find)

[（6）insert](#%EF%BC%886%EF%BC%89insert)

[（7）erase](#%EF%BC%887%EF%BC%89erase)

[（8）swap](#%EF%BC%888%EF%BC%89swap)

[（9）assign](#%EF%BC%889%EF%BC%89assign)

[（10）clear](#%EF%BC%8810%EF%BC%89clear)

[1.2.5 list的顺序修改接口](#1.2.5%20list%E7%9A%84%E9%A1%BA%E5%BA%8F%E4%BF%AE%E6%94%B9%E6%8E%A5%E5%8F%A3)

[（1）sort](#%EF%BC%881%EF%BC%89sort)

[（2）reverse](#%EF%BC%882%EF%BC%89reverse)

[二、模拟实现list类](#%E4%BA%8C%E3%80%81%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0list%E7%B1%BB)

---


## 一、标准库中的list类

### 1.1 list类介绍

list是一个模板类，在使用的时候我们需要给出元素的类型

使用list类时，需要包含头文件&lt;list&gt;

### 1.2 list的常用接口

#### 1.2.1 常用的构造函数

> 
**list();**


list类的默认构造函数，构造一个空链表

例如：

> 
**list(size_type n, const value_type&amp; val =  value_type());**


构造一个list对象并用n个val初始化

例如：

> 
**list(const list&amp; x);** 


list类的拷贝构造函数

例如：

> 
**Template&lt;class InputIterator&gt;**
**list(InputIterator first, InputIterator last);**


使用迭代器进行初始化构造

例如：

#### 1.2.2 容量操作接口

##### （1）size

> 
**size_type size() const;**


获取链表节点个数

例如：

##### （2）empty

> 
**bool empty() const;**


判断链表是否为空

例如：

##### （3）resize

> 
**void resize(size_type n, value_type val = value_type());**


缩减或增加节点个数为n

如果没有给出val，就用0作为元素

例如：

#### 1.2.3 访问和遍历

##### （1）迭代器

> 
**iterator begin();**
**const_iterator begin() const;**
**iterator end();**
**const_iterator end() const;**


迭代器，用于获取链表中第一个节点的位置和最后一个节点的**下一个位置（即哨兵位）**

例如：

##### （2）反向迭代器

> 
**reverse_iterator rbegin();**
**const_reverse_iterator rbegin() const;**
**reverse_iterator rend();**
**const_reverse_iterator rend() const;**


反向迭代器，rbegin获取容器中最后一个节点的位置，rend获取容器中哨兵位的位置

例如：

需要注意，反向迭代器rit也要用++而不是--

##### （3）back

> 
**reference back();**
**const_reference back() const;**


返回链表中最后一个节点存储的数据的引用

例如：

##### （4）front

> 
**reference front();**
**const_reference front() const;**


返回链表中第一个节点存储的数据的引用

例如：

#### 1.2.4 list的增删查改

##### （1）push_front

> 
**void push_front(const value_type&amp; val);**


从链表头部插入一个元素

例如：

##### （2）pop_front

> 
**void pop_front();**


从链表头部删除一个元素

例如：

##### （3）push_back

> 
**void push_back(const value_type&amp; val);**


从链表尾部插入一个元素

例如：

##### （4）pop_back

> 
**void pop_back();**


从链表尾部删除一个元素

例如：

##### （5）find

> 
**template &lt;class InputIterator, class T&gt;**
**InputIterator find(InputIterator first, InputIterator last, const T&amp; val);**


在两个迭代器区间寻找val并返回其所在处的迭代器

例如：

需要注意的是，该函数**并非list的成员函数**，是标准库中的函数，多个容器共用该find函数

可以看到，我们可以直接对list的迭代器进行解引用并修改其内容，但是迭代器不应该指向节点吗？为什么对其解引用能修改数据呢？

实际上list的迭代器并不是用原生态指针进行模拟实现的，需要进行底层的封装，这里会在list的模拟实现的源代码中体现。

##### （6）insert

> 
**iterator insert(iterator position, const value_type&amp; val);**
**void insert(iterator position, size_type n, const value_type&amp; val);**
**————————————————————————————————————————**
**template&lt;class InputIterator&gt;**
**void insert(iterator position, InputIterator first, InputIterator last);**


在position位置的前面插入一个或多个元素

例如：

细心的读者可能已经发现了，list的insert操作是**不会导致迭代器失效**的，因为pos指向的节点不变，相对位置也不变。

但是list的删除操作一定会导致迭代器失效，并且失效的只是指向被删除节点的迭代器，其他迭代器不会受到影响。

##### （7）erase

> 
**iterator erase(iterator position);**
**iterator erase(iterator first, iterator last);**


删除position位置的元素或者 [first，last) 区间的所有元素

例如：

##### （8）swap

> 
**void swap(vector&amp; x);**


交换两个list对象

例如：

##### （9）assign

> 

**template &lt;class InputIterator&gt;**
**void assign(InputIterator first, InputIterator last);**
**void assign(size_type n, const value_type&amp; val);**


为list指定新内容，替换其当前内容并修改节点个数

例如：

##### （10）clear

> 
**void clear();**


删除链表所有节点

例如：

#### 1.2.5 list的顺序修改接口

##### （1）sort

> 
**void sort();**
**template&lt;class Compare&gt;**
**void sort(Compare comp);**


list由于结构的特殊性，是无法使用标准库中的sort函数的，因为迭代器无法进行相减的操作

并且在C++文档中，我们可以看到标准库中的sort也限定了迭代器的类型必须是可以进行随机访问（RandomAccess）的

迭代器有几个功能分类：

但是list的sort函数也是没什么必要的，因为直接对链表排序的效率比拷贝到vector进行排序再拷贝回链表要慢的多

##### （2）reverse

> 
**void reverse();**


对链表进行逆置

例如：

---


## 二、模拟实现list类

学习了list类中各种常用接口的用法后，我们就可以开始自己手撕一个自己的list类了

为了不和标准库中的list类冲突，我们可以开一个自己的命名空间

```
#include &lt;iostream&gt;
#include &lt;assert.h&gt;
using namespace std;

namespace Eristic
{
	template&lt;class T&gt;
	struct list_node
	{
		list_node&lt;T&gt;* _next;
		list_node&lt;T&gt;* _prev;
		T _data;

		list_node(const T&amp; x = T()) //匿名对象作为缺省值，变为默认构造函数
			:_next(nullptr)
			,_prev(nullptr)
			,_data(x)
		{}
	};
	 
	template&lt;class T, class Ref, class Ptr&gt; 
    //通过模板参数实现const迭代器和普通迭代器版本的复用
    //和list类中迭代器的typedef配合阅读会较好理解
	struct __list_iterator //重点：迭代器的底层封装
	{
		typedef list_node&lt;T&gt; node;
		typedef __list_iterator&lt;T, Ref, Ptr&gt; self;
		node* _node;
        //node*本身不支持解引用等操作，对其进行封装就可以模仿原生态指针的行为

		__list_iterator(node* n)
			:_node(n)
		{}

		Ref&amp; operator*()
		{ 
			return _node-&gt;_data;
		}

		Ptr operator-&gt;() //误区：在使用箭头运算符的时候，为什么只需要一个箭头而不是两个？
        //答：为了可读性，编译器会帮助我们省略一个箭头
		{
			 return &amp;_node-&gt;_data;
		}

		self&amp; operator++()
		{
			_node = _node-&gt;_next;
			return *this;
		}

		self operator++(int)
		{
			self tmp(*this);
			_node = _node-&gt;_next;
			return tmp;
		}

		self&amp; operator--()
		{
			_node = _node-&gt;_prev;
			return *this;
		}

		self operator--(int)
		{
			self tmp(*this);
			_node = _node-&gt;_prev;
			return tmp;
		}

		bool operator!=(const self&amp; s)
		{
			return _node != s._node;
		}

		bool operator==(const self&amp; s)
		{
			return _node == s._node;
		}
		//不需要写拷贝构造，因为我们用默认生成的进行浅拷贝就能完成需求
		//析构函数也不需要写，释放节点是list的事，与迭代器无关
	};

	template&lt;class T&gt;
	class list
	{
		typedef list_node&lt;T&gt; node;
	public:
		typedef __list_iterator&lt;T, T&amp;, T*&gt; iterator;
		typedef __list_iterator&lt;T, const T&amp;, const T*&gt; const_iterator;
        //对应上面的多个模板参数

		void list_init()
		{
			_head = new node;
			_head-&gt;_next = _head;
			_head-&gt;_prev = _head;
		}

		list()
		{
			list_init();
		}

		list(int n, const T&amp; x = T())
		{
			list_init();
			for (int i = 0; i &lt; n; i++)
				push_back(x);
		}

		template&lt;class iterator&gt;
		list(iterator first, iterator last)
		{
			list_init();
			while (first != last)
			{
				push_back(*first);
				++first;
			}
		}

		list(const list&lt;T&gt;&amp; lt)
		{
			list_init();
			list&lt;T&gt; tmp(lt.begin(), lt.end());
			swap(tmp);
		}

		~list()
		{
			clear();
			delete _head;
			_head = nullptr;
		}

		list&lt;T&gt;&amp; operator=(const list&lt;T&gt; lt)
		{
			swap(lt);
			return *this;
		}

		int size()
		{
			iterator it = begin();
			int count = 0;
			while (it != end())
			{
				++it;
				++count;
			}
			return count;
		}

		void resize(size_t n, const T&amp; x = T())
		{
			if (n &lt; size())
				while (n &lt; size())
					pop_back();
			else if (n &gt; size())
				while (n &gt; size())
					push_back(x);
		}

		void swap(list&lt;T&gt;&amp; lt)
		{
			std::swap(_head, lt._head);
		}

		T&amp; front()
		{
			return _head-&gt;_next-&gt;_data;
		}

		const T&amp; front() const
		{
			return _head-&gt;_next-&gt;_data;
		}

		T&amp; back()
		{
			return _head-&gt;_prev-&gt;_data;
		}

		const T&amp; back() const
		{
			return _head-&gt;_prev-&gt;_data;
		}

		void push_back(const T&amp; x)
		{
			insert(end(), x);
		}

		void push_front(const T&amp; x)
		{
			insert(begin(), x);
		}

		void pop_back()
		{
			erase(--end());
		}

		void pop_front()
		{
			erase(begin());
		}

		void insert(iterator pos, const T&amp; x)
		{
			node* cur = pos._node;
			node* prev = cur-&gt;_prev;

			node* newnode = new node(x);

			cur-&gt;_prev = newnode;
			newnode-&gt;_next = cur;
			prev-&gt;_next = newnode;
			newnode-&gt;_prev = prev;
		}

		iterator erase(iterator pos)
		{
			assert(pos != end()); //哨兵位不能删
			node* prev = pos._node-&gt;_prev;
			node* next = pos._node-&gt;_next;

			prev-&gt;_next = next;
			next-&gt;_prev = prev;

			delete pos._node;

			return iterator(next);
		}

		iterator begin()
		{
			return iterator(_head-&gt;_next);
		}

		const_iterator begin() const
		{
			return const_iterator(_head-&gt;_next);
		}

		iterator end()
		{
			return iterator(_head);
		}

		const_iterator end() const
		{
			return const_iterator(_head);
		}

		void clear()
		{
			iterator it = begin();
			while (it != end())
			{
				erase(it++);
			}
		}

	private:
		node* _head;
	};
}
```

如有错误，欢迎在评论区指出

完.
