# 原创
：  【C++】反向迭代器

# 【C++】反向迭代器

## 一、前言

在前面对vector等容器的学习中，我们学会了如何去使用正向迭代器并模拟实现

但是我们没有去模拟实现反向迭代器，这篇文章中我们就来了解反向迭代器的底层并实现它，把之前的坑给填上。

---


## 二、反向迭代器

反向迭代器的底层设计十分精妙，当你真正了解了它的实现方式，一定会拍案叫绝

我们先以list类为例，来实现它的反向迭代器。

list类的正向迭代器中，begin和end的位置如下：

之前我们实现的list类的正向迭代器是这样的：

```
	template&lt;class T, class Ref, class Ptr&gt;
	struct __list_iterator 
	{
		typedef list_node&lt;T&gt; node;
		typedef __list_iterator&lt;T, Ref, Ptr&gt; self;
		node* _node;

		__list_iterator(node* n)
			:_node(n)
		{}

		Ref&amp; operator*()
		{ 
			return _node-&gt;_data;
		}

		Ptr operator-&gt;()
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
	};
```

### 2.1 修改正向迭代器 

有些人就认为，反向迭代器直接把正向迭代器修改一下不就可以了吗？把向前走改成向后走，向后走改成向前，例如：

```
	template&lt;class T, class Ref, class Ptr&gt;
	struct __list_reverse_iterator
	{
		typedef list_node&lt;T&gt; node;
		typedef __list_reverse_iterator&lt;T, Ref, Ptr&gt; self;
		node* _node;

		__list_reverse_iterator(node* n)
			:_node(n)
		{}

		Ref&amp; operator*()
		{
			return _node-&gt;_data;
		}

		Ptr operator-&gt;()
		{
			return &amp;_node-&gt;_data;
		}

		self&amp; operator++()
		{
			_node = _node-&gt;_prev;
			return *this;
		}

		self operator++(int)
		{
			self tmp(*this);
			_node = _node-&gt;_prev;
			return tmp;
		}

		self&amp; operator--()
		{
			_node = _node-&gt;_next;
			return *this;
		}

		self operator--(int)
		{
			self tmp(*this);
			_node = _node-&gt;_next;
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
	};
```

这种方式实现的反向迭代器， rbegin和rend的位置如下：

用正向迭代器修改得到的反向迭代器，也能正常的完成我们需要的功能。

但是这种方式的代码复用率太低，并不是一个好的方法。

### 2.2 封装正向迭代器

我们可以看看标准库中的反向迭代器是如何实现的

[reverse_iterator - C++ Reference (cplusplus.com)<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://legacy.cplusplus.com/reference/iterator/reverse_iterator/](https://legacy.cplusplus.com/reference/iterator/reverse_iterator/)具体是如何实现的呢？我们直接放出模拟实现的代码：

```
template&lt;class Iterator, class Ref, class Ptr&gt;
struct __list_reverse_iterator
{
	typedef __list_reverse_iterator&lt;Iterator, Ref, Ptr&gt; self;
	Iterator _cur;

	__list_reverse_iterator(Iterator it)
		:_cur(it)
	{}

	Ref operator*()
	{
		Iterator tmp = _cur;
		--tmp;
		return *tmp;
	}

	self&amp; operator++()
	{
		--_cur;
		return *this;
	}

	self&amp; operator--()
	{
		++_cur;
		return *this;
	}

	bool operator!=(const self&amp; s)
	{
		return _cur != s._cur;
	}

	bool operator==(const self&amp; s)
	{
		return _cur == s._cur;
	}
};

template&lt;class T&gt;
class list
{
	typedef list_node&lt;T&gt; node;
public:
	typedef __list_iterator&lt;T, T&amp;, T*&gt; iterator;
	typedef __list_iterator&lt;T, const T&amp;, const T*&gt; const_iterator;
	typedef __list_reverse_iterator&lt;iterator, T&amp;, T*&gt; reverse_iterator;
	typedef __list_reverse_iterator&lt;const_iterator, const T&amp;, const T*&gt; const_reverse_iterator;

    //...

	reverse_iterator rbegin()
	{
		return reverse_iterator(end()); //end和begin都会返回一个正向迭代器，用这个正向迭代器来构造反向迭代器
	}

	const_reverse_iterator rbegin() const
	{
		return const_reverse_iterator(end());
	}

    reverse_iterator rend()
	{
		return reverse_iterator(begin());
	}

	const_reverse_iterator rend() const
	{
		return const_reverse_iterator(begin());
	}

    //...
}
```

简单来说，标准库中的反向迭代器，实际上是一个**对正向迭代器的封装**！

> 
当--反向迭代器时，实际上就是对内部封装的正向迭代器进行++操作；
而++反向迭代器时，实际上就是对内部封装的正向迭代器进行--操作。


通过模拟实现的代码，我们会发现： 

在对反向迭代器解引用时，实际上解引用的是其前面的位置

例如，假设反向迭代器此时在哨兵位，对其解引用时，实际上解引用的是5的位置

所以反向迭代器实际上也是一个**适配器**，通过提供特定的函数**对内部封装的正向迭代器进行操作**，来实现反向迭代器的功能。

这种实现反向迭代器的方式，rbegin和rend的位置如下：

这样就刚好和正向迭代器的begin和end对齐

进行测试，可以正常的实现功能

为什么我们选择用封装正向迭代器的方式来实现反向迭代器呢？这种方式感觉反而更麻烦了

实际上，其最大的优点在于，**用适配器的形式来实现反向迭代器，就可以适用于任何一个容器了**

当然前提是这个容器需要有双向迭代器，毕竟需要用到++和--。

例如我们把上面写的反向迭代器放到一个头文件中，并换成vector来使用它

我们知道，相比list的正向迭代器是对指针的封装，vector的正向迭代器是一个原生态指针

但是因为反向迭代器是一个适配器，所以不需要关心正向迭代器的底层如何，只需要能够符合需求，能够完成对应的操作，就可以封装进反向迭代器

例如：

到这里，我们知道**反向迭代器的底层实际上就是一个正向迭代器**，对其进行了封装来实现反向迭代器的功能，通过这种实现反向迭代器的方式就可以适用于所有支持双向迭代器和随机迭代器的容器

如果有错误的地方，欢迎在评论区指出

完.
