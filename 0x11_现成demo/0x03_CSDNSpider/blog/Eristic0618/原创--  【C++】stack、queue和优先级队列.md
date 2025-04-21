# 原创
：  【C++】stack、queue和优先级队列

# 【C++】stack、queue和优先级队列

[一、前言](#%E4%B8%80%E3%80%81%E5%89%8D%E8%A8%80)

[二、stack类](#%E4%BA%8C%E3%80%81stack%E7%B1%BB)

[2.1 了解stack](#2.1%20%E4%BA%86%E8%A7%A3stack)

[2.2 使用stack](#2.2%20%E4%BD%BF%E7%94%A8stack)

[（1）empty](#%EF%BC%881%EF%BC%89empty)

[（2）size](#%EF%BC%882%EF%BC%89size)

[（3）top](#%EF%BC%883%EF%BC%89top)

[（4）push](#%EF%BC%884%EF%BC%89push)

[（5）pop](#%EF%BC%885%EF%BC%89pop)

[2.3 stack的模拟实现](#2.3%20stack%E7%9A%84%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0)

[三、queue类](#%E4%B8%89%E3%80%81queue%E7%B1%BB)

[3.1 了解queue](#3.1%20%E4%BA%86%E8%A7%A3queue)

[3.2 使用queue](#3.2%20%E4%BD%BF%E7%94%A8queue)

[（1）empty](#%EF%BC%881%EF%BC%89empty)

[（2）size](#%EF%BC%882%EF%BC%89size)

[（3）front](#%EF%BC%883%EF%BC%89front)

[（4）back](#%EF%BC%884%EF%BC%89back)

[（5）push](#%EF%BC%885%EF%BC%89push)

[（6）pop](#%EF%BC%886%EF%BC%89pop)

[3.3 queue的模拟实现](#3.3%20queue%E7%9A%84%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0)

[四、优先级队列](#%E5%9B%9B%E3%80%81%E4%BC%98%E5%85%88%E7%BA%A7%E9%98%9F%E5%88%97)

[4.1 了解优先级队列](#4.1%20%E4%BA%86%E8%A7%A3%E4%BC%98%E5%85%88%E7%BA%A7%E9%98%9F%E5%88%97)

[4.2 使用优先级队列](#4.2%20%E4%BD%BF%E7%94%A8%E4%BC%98%E5%85%88%E7%BA%A7%E9%98%9F%E5%88%97)

[（1）empty](#%EF%BC%881%EF%BC%89empty)

[（2）size](#%EF%BC%882%EF%BC%89size)

[（3）top](#%EF%BC%883%EF%BC%89top)

[（4）push](#%EF%BC%884%EF%BC%89push)

[（5）pop](#%EF%BC%885%EF%BC%89pop)

[4.3 仿函数](#4.3%20%E4%BB%BF%E5%87%BD%E6%95%B0)

[4.4 优先级队列的模拟实现](#4.4%20%E4%BC%98%E5%85%88%E7%BA%A7%E9%98%9F%E5%88%97%E7%9A%84%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0)

[五、deque类（了解）](#%E4%BA%94%E3%80%81deque%E7%B1%BB%EF%BC%88%E4%BA%86%E8%A7%A3%EF%BC%89)

[5.1 关于deque](#5.1%20%E5%85%B3%E4%BA%8Edeque)

[5.2 deque的应用](#5.2%20deque%E7%9A%84%E5%BA%94%E7%94%A8)

## 一、前言

通过前面的学习，我们已经对string、vector和list类有了了解

本文中介绍的stack、queue和优先级队列相比于前面的容器而言接口较少，并且有了前面的基础，在学习这几个容器的使用和模拟实现时会更好上手。

因此，本文仅对接口的使用进行简单介绍，把重点放在优先级队列等部分。

---


## 二、stack类

### 2.1 了解stack

[stack - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://legacy.cplusplus.com/reference/stack/stack/](https://legacy.cplusplus.com/reference/stack/stack/)通过文档，我们可以了解到以下的内容：
1. empty：判空1. size：获取容器有效元素个数1. back：获取容器尾部元素1. push_back：尾插1. pop_back：尾删
### 2.2 使用stack

在实例化与stack类类似的容器适配器时，模板参数除了必须要传入元素类型，还可以选择**传入底层容器的种类**

例如：

#### （1）empty

> 
**bool empty() const;**


检测栈是否为空

#### （2）size

> 
**size_type size() const;**


返回stack中元素的个数

#### （3）top

> 
**value_type&amp; top();**
**const value_type&amp; top(); const**


返回栈顶元素的引用

#### （4）push

> 
**void push(const value_type&amp; val);**


将val压入栈中

#### （5）pop

> 
**void pop();**


将栈顶元素弹出

例如：

### 2.3 stack的模拟实现

前面提到，stack是一个容器适配器，其底层封装了其他的容器，这里我们以vector作为底层容器

```
namespace Eristic
{
	template&lt;class T, class Container = vector&lt;T&gt;&gt; 
    //一个模板参数传入数据类型，一个模板参数传入底层容器   
	class stack
	{
	public:
		void push(const T&amp; val)
		{
			_con.push_back(val); //压栈即在容器尾部插入数据
		}

		void pop()
		{
			_con.pop_back(); //出栈即删除容器尾部的数据
		}

		const T&amp; top()
		{
			return _con.back(); //栈顶元素即容器尾部的元素
		}

		size_t size()
		{
			return _con.size();
		}

		bool empty()
		{
			return _con.empty();
		}

	private:
		Container _con; //对容器进行封装
	};
}

```

---


## 三、queue类

### 3.1 了解queue

[cplusplus.com/reference/queue/queue/<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://cplusplus.com/reference/queue/queue/](https://cplusplus.com/reference/queue/queue/)通过文档，我们可以了解到以下的内容：
1. empty：判空1. size：获取容器有效元素个数1. front：获取容器头部元素1. back：获取容器尾部元素1. push_back：尾插1. pop_front：头删
通过这些操作，我们就可以实现队列的出队和入队等行为。

### 3.2 使用queue

#### （1）empty

> 
**bool empty() const;**


检测队列是否为空

#### （2）size

> 
**size_type size() const;**


返回队列中有效元素的个数

#### （3）front

> 
**value_type&amp; front();**
**const value_type&amp; front(); const**


返回队头元素的引用

#### （4）back

> 
**value_type&amp; back();**
**const value_type&amp; (); const**


#### （5）push

> 
**void push(const value_type&amp; val);**


从队尾将元素val入队列

#### （6）pop

> 
**void pop();**


将队头元素出队列

例如：

### 3.3 queue的模拟实现

因为queue需要头删，如果底层使用vector效率太低，这里我们使用list作为queue的底层容器

```
namespace Eristic
{
	template&lt;class T, class Container = list&lt;T&gt;&gt;
	class queue
	{
	public:
		void push(const T&amp; val)
		{
			_con.push_back(val); //入队列，即从容器尾部插入数据
		}

		void pop()
		{
			_con.pop_front(); //出队列，即从容器头部删除数据
		}

		const T&amp; front()
		{
			return _con.front();
		}

		const T&amp; back()
		{
			return _con.back();
		}

		size_t size()
		{
			return _con.size();
		}

		bool empty()
		{
			return _con.empty();
		}

	private:
		Container _con;
	};
}

```

---


## 四、优先级队列

### 4.1 了解优先级队列

[cplusplus.com/reference/queue/priority_queue/<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://cplusplus.com/reference/queue/priority_queue/](https://cplusplus.com/reference/queue/priority_queue/)

通过文档，我们可以了解到以下的内容：
1. empty：判空1. size：返回容器有效元素个数1. push_back：尾插1. pop_back：尾删
因为优先级队列以堆的方式实现，因此将数据出队列时应按照堆的方式删除数据，也就是首尾数据交换后尾删，并重新建堆。

### 4.2 使用优先级队列

#### （1）empty

> 
**bool empty() const;**


检测优先级队列是否为空

#### （2）size

> 
**size_type size() const;**


返回优先级队列中有效元素个数

#### （3）top

> 
**const value_type&amp; top(); const**


返回优先级队列中优先级最大的元素，即堆顶元素

#### （4）push

> 
**void push(const value_type&amp; val);**


向优先级队列中插入元素val

#### （5）pop

> 
**void pop();**


删除优先级队列中优先级最大的元素，即堆顶元素

### 4.3 仿函数

可以看到，优先级队列相比stack和queue，又多了一个模板参数：仿函数。

首先，**仿函数是一个类，而不是函数**

当我们实例化优先级队列时不传入仿函数，就默认使用仿函数less，其效果为：

如果我们想变为升序，就需要手动传入仿函数greater，需要包含头文件&lt;functional&gt;

传入的仿函数为优先级队列提供了排序的顺序

仿函数在类中重载了括号（），使得我们可以像调用函数一样去调用实例化的类对象（或者匿名对象）。

我们以仿函数greater为例，自己尝试实现一个

```
	template&lt;class T&gt;
	class greater
	{
	public:
		bool operator()(const T&amp; x, const T&amp; y)
		{
			return x &gt; y;
		}
	};
```

像这样，就是一个仿函数，而使用仿函数的方式如下：

可以看到，我们既可以使用仿函数实例化出的对象来调用类中的函数，也可以使用匿名对象调用。

### 4.4 优先级队列的模拟实现

```
namespace Eristic
{
	template&lt;class T&gt;
	class less //也可以用struct，默认公开
	{
	public:
		bool operator()(const T&amp; x, const T&amp; y)
		{
			return x &lt; y;
		}
	};

	template&lt;class T&gt;
	class greater
	{
	public:
		bool operator()(const T&amp; x, const T&amp; y)
		{
			return x &gt; y;
		}
	};

	template&lt;class T, class Container = vector&lt;T&gt;, class Compare = less&lt;T&gt;&gt;
	class priority_queue
	{
	public:
		void adjust_up(int child) //向上调整算法
		{
			Compare com;
			int parent = (child - 1) / 2;
			while (child &gt; 0)
			{
				if (com(_con[parent], _con[child]))
				{
					swap(_con[child], _con[parent]);
					child = parent;
					parent = (child - 1) / 2;
				}
				else
					break;
			}
		}

		void adjust_down(int parent) //向下调整算法
		{
			Compare com;
			int child = parent * 2 + 1;
			while (child &lt; _con.size())
			{
				if (child + 1 &lt; _con.size() &amp;&amp; com(_con[child], _con[child + 1]))
				{
					child++;
				}
				if (com(_con[parent], _con[child]))
				{
					swap(_con[parent], _con[child]);
					parent = child;
					child = parent * 2 + 1;
				}
				else
					break;
			}
		}

		void push(const T&amp; x)
		{
			_con.push_back(x); //队尾插入数据
			adjust_up(_con.size() - 1); //向上调整重新排序
		}

		void pop()
		{
			swap(_con[0], _con[_con.size() - 1]); //交换队头（堆顶）和队尾（堆尾）数据
			_con.pop_back(); //删除队尾数据
			adjust_down(0); //向下调整重新排序
		}

		const T&amp; top()
		{
			return _con[0]; //取出队头（优先级最大）元素
		}

		size_t size()
		{
			return _con.size();
		}

		bool empty()
		{
			return _con.empty();
		}


	private:
		Container _con;
	};
}

```

---


## 五、deque类（了解）

### 5.1 关于deque

deque（双端队列），是一种具有**双向开口的连续线性空间**的数据结构，在头尾插入的时间复杂度为常数，其特点介于vector和list之间。

双端数组的底层是一段假想的连续空间，看似所有元素是顺序排列的，实际上将元素分为了多块，每块元素之间依靠**中控数组**联系

中控数组是一个指针数组，存放了每个空间的指针

deque的整体结构如下：

这种结构相对于vector的优势在于，头插头删的效率和扩容的效率高，不需要移动大量元素，第一个元素会从中控数组的中间开始插入。

相对于list的优势在于，支持随机访问。

但是缺点在于中间的插入删除，如果我们规定指针指向的每个数组不一样大，那么中间插入删除的效率就较高，但是随机访问的效率会变差；如果规定数组一样大，随机访问的效率变高，但是同时会牺牲中间插入删除的效率。

问题又来了：既然deque支持随机访问，其迭代器是如何设计的呢？

其迭代器的设计如下：

其中，cur指向当前的位置，first指向小数组的开头，last指向小数组的结尾，node指向中控数组中指向数组的指针的位置。

当迭代器遍历到小数组的尾部，node走到下一个指针的位置，first和last更新，cur回到数组头部。

在这里引入deque的另一个缺陷：在遍历时，deque的迭代器需要频繁的去检测是否移动到小数组的边界，导致效率低下，而在序列式场景中需要经常的遍历容器。

### 5.2 deque的应用

虽然deque兼具了vector和list的特点，但是并没有做到极致，并且缺点也很明显，无法完全的替代vector和list，因此我们并不常用deque，其主要应用就是作为stack和queue的底层数据结构。

因为stack和queue只需要尾插或头插，并且不需要遍历，所以完美避免了deque的缺点，并且发挥了deque扩容效率和空间利用率高的优点。

完.
