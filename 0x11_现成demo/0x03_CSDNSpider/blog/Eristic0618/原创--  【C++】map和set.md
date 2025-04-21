# 原创
：  【C++】map和set

# 【C++】map和set

[一、set介绍](#%E4%B8%80%E3%80%81set%E4%BB%8B%E7%BB%8D)

[1.1 概念](#1.1%20%E6%A6%82%E5%BF%B5)

[1.2 常用接口](#1.2%20%E5%B8%B8%E7%94%A8%E6%8E%A5%E5%8F%A3)

[（1）insert](#%EF%BC%881%EF%BC%89insert)

[（2）erase](#%EF%BC%882%EF%BC%89erase)

[（3）swap](#%EF%BC%883%EF%BC%89swap)

[（4）clear](#%EF%BC%884%EF%BC%89clear)

[（5）find](#%EF%BC%885%EF%BC%89find)

[（6）count](#%EF%BC%886%EF%BC%89count)

[（7）size](#%EF%BC%887%EF%BC%89size)

[（8）empty](#%EF%BC%888%EF%BC%89empty)

[1.3 multiset](#1.3%20multiset)

[二、map介绍](#%E4%BA%8C%E3%80%81map%E4%BB%8B%E7%BB%8D)

[三、红黑树改造](#%E4%B8%89%E3%80%81%E7%BA%A2%E9%BB%91%E6%A0%91%E6%94%B9%E9%80%A0)

[四、模拟实现set](#%E5%9B%9B%E3%80%81%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0set)

[五、模拟实现map](#%E4%BA%94%E3%80%81%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0map)

---


## 一、set介绍

### 1.1 概念

set是C++STL库中的一个关联式容器，类似于Python中的集合，其特点是内部的元素是一个值（Key），它们有序且唯一，所以可用于对一个序列的排序和去重。

### 1.2 常用接口

#### （1）insert

> 
**pair&lt;iterator,bool&gt; insert (const value_type&amp; val); **
**pair&lt;iterator,bool&gt; insert (value_type&amp;&amp; val);**


插入一个元素，返回一个pair对象，其中包含一个迭代器和bool值

如果插入成功（set中没有该元素），pair中存放插入位置的迭代器和true

如果插入失败（set中已经存在该元素），pair中存放对应元素的迭代器和false

#### （2）erase

> 
**size_type erase (const value_type&amp; val);**


删除一个元素，返回删除的元素个数

#### （3）swap

> 
**void swap (set&amp; x);**


交换两个set中的元素

#### （4）clear

> 
**void clear() noexcept;**


清除set中的所有元素

#### （5）find

> 
**const_iterator find (const value_type&amp; val) const;**
**iterator find (const value_type&amp; val);**


在set中寻找目标元素并返回其位置的迭代器

如果没有该元素，则返回end()

#### （6）count

> 
**size_type count (const value_type&amp; val) const;**


返回set中值为val的元素个数

因为set的去重性，所以返回值只会是0或1

#### （7）size

> 
**size_type size() const noexcept;**


返回set中的元素个数

#### （8）empty

> 
**bool empty() const noexcept;**


判断set是否为空

### 1.3 multiset

基本与set相同，区别在于multiset可以插入相同的值

---


## 二、map介绍

map也是C++STL库中的一个关联式容器，类似于Python中的字典。

和set不同的是，map中的元素不是单一的key，而是一个key/value模型，也就是键值对。所以map中的元素都是pair对象

在map中，key必须是唯一的，但是value可以重复。排序时根据key进行排序

它可以通过查找key来获取value值。

map的接口使用方法和set差不多，只是把key换成了键值对

map重载了方括号，我们可以像使用下标一样用key来查找value

> 
**mapped_type&amp; operator[] (const key_type&amp; k); **
**mapped_type&amp; operator[] (key_type&amp;&amp; k);**


重载后的方括号可以用于插入元素和查找元素，方括号中传入key，就会返回value

 

---


## 三、红黑树改造

set是key结构，而map是key/value模型，要想让两者底层使用相同的代码，则需要对红黑树进行一定的改造

首先需要改造红黑树的模板参数。set只需要指定key的类型，但是map除了需要指定key的类型还需要指定value的类型，所以原先的模板参数是无法做到通用的，因为你不知道红黑树中存的是key还是pair对象。

因此我们可以设定一个class K接收key的类型，再设定一个class T接收容器内元素的类型。如果是set的话T的类型就是key的类型，如果是map的话T的类型就是一个pair。

但是在容器中我们需要获得key来进行许多操作，例如插入、查找。如果是map，我们可以用.first来拿到key，但是这种方法又不适用于set了。因此我们再设定一个class KeyOfT来接收二者传入的仿函数，用该仿函数来获取key即可。因为我们可以在map和set中个性化定义仿函数的内部细节，所以可以做到代码复用。

其他地方基本不需要做什么改动

完整代码如下：

```
#pragma once

enum Colour
{
	RED,
	BLACK
};

template&lt;class T&gt;
struct RBTreeNode
{
	RBTreeNode&lt;T&gt;* _left;
	RBTreeNode&lt;T&gt;* _right;
	RBTreeNode&lt;T&gt;* _parent;
	T _data;
	Colour _col;

	RBTreeNode(const T&amp; data)
		:_left(nullptr)
		, _right(nullptr)
		, _parent(nullptr)
		, _data(data)
		, _col(RED)
	{}
};

template&lt;class T, class Ref, class Ptr&gt;
struct __TreeIterator
{
	typedef RBTreeNode&lt;T&gt; Node;
	typedef __TreeIterator&lt;T, Ref, Ptr&gt; Self;
	Node* _node;

	__TreeIterator(Node* node)
		:_node(node)
	{}

	Ref operator*()
	{
		return _node-&gt;_data;
	}

	Ptr operator-&gt;()
	{
		return &amp;_node-&gt;_data;
	}

	Self&amp; operator--()
	{
		Node* parent = _node-&gt;_parent;
		if (_node-&gt;_left)
			_node = _node-&gt;_left;
		else if (_node == parent-&gt;_right)
			_node = parent;
		else
		{
			Node* cur = _node;
			while (parent &amp;&amp; cur == parent-&gt;_left)
			{
				cur = parent;
				parent = cur-&gt;_parent;
			}
			_node = parent;
		}
		return *this;
	}

	Self&amp; operator++()
	{
		if (_node-&gt;_right)
		{
			Node* cur = _node-&gt;_right;
			while (cur-&gt;_left)
				cur = cur-&gt;_left;
			_node = cur;
		}
		else
		{
			Node* cur = _node;
			Node* parent = cur-&gt;_parent;
			while (parent &amp;&amp; cur == parent-&gt;_right)
			{
				cur = parent;
				parent = cur-&gt;_parent;
			}
			_node = parent;
		}
		return *this;
	}

	bool operator!=(const Self&amp; s)
	{
		return _node != s._node;
	}
};

//K是key的类型，T是元素的类型（set中的T和K一样，map中T是一个pair类型），KeyOfT是获取key的仿函数
//因为该红黑树是set和map共用的，所以需要作此处理。因为虽然map中的pair类型元素可以直接用.first获取key，但是如果是set的话同样的代码就无法通用了
template&lt;class K, class T, class KeyOfT&gt; 
class RBTree
{
	typedef RBTreeNode&lt;T&gt; Node;
public:
	typedef __TreeIterator&lt;T, T&amp;, T*&gt; iterator;
	typedef __TreeIterator&lt;T, const T&amp;, const T*&gt; const_iterator;
	iterator begin()
	{
		Node* cur = _root;
		while (cur &amp;&amp; cur-&gt;_left)
			cur = cur-&gt;_left;
		return iterator(cur);
	}

	iterator end()
	{
		return iterator(nullptr);
	}

	const_iterator begin() const
	{
		Node* cur = _root;
		while (cur &amp;&amp; cur-&gt;_left)
			cur = cur-&gt;_left;
		return const_iterator(cur);
	}

	const_iterator end() const
	{
		return const_iterator(nullptr);
	}

	pair&lt;Node*, bool&gt; insert(const T&amp; data)
	{
		if (_root == nullptr)
		{
			_root = new Node(data);
			_root-&gt;_col = BLACK;
			return make_pair(_root, true);
		}

		Node* parent = nullptr;
		Node* cur = _root;
		KeyOfT kot;

		while (cur)
		{
			parent = cur;
			if (kot(data) &gt; kot(cur-&gt;_data))
				cur = cur-&gt;_right;
			else if (kot(data) &lt; kot(cur-&gt;_data))
				cur = cur-&gt;_left;
			else
				return make_pair(cur, false);
		}

		cur = new Node(data);
		Node* newnode = cur;
		cur-&gt;_col = RED; //新节点默认为红色
		if (kot(data) &gt; kot(parent-&gt;_data))
		{
			parent-&gt;_right = cur;
			cur-&gt;_parent = parent;
		}
		else
		{
			parent-&gt;_left = cur;
			cur-&gt;_parent = parent;
		}

		while (parent &amp;&amp; parent-&gt;_col == RED) //若父节点不存在说明走到根，若父节点为黑色则不需要处理
		{
			Node* grandfather = parent-&gt;_parent; //记录祖父节点

			if (grandfather-&gt;_left == parent) //父节点在祖父节点左边时
			{
				Node* uncle = grandfather-&gt;_right; //记录叔叔节点

				if (uncle &amp;&amp; uncle-&gt;_col == RED) //如果叔叔节点存在且为红色
				{
					//变色
					parent-&gt;_col = uncle-&gt;_col = BLACK; //将父节点与叔叔节点都变为黑色
					grandfather-&gt;_col = RED; //将祖父节点变为红色
					//继续向上处理
					cur = grandfather;
					parent = cur-&gt;_parent;  
				}
				else //叔叔节点不存在或为黑色
				{
					//需要旋转+变色
					if (parent-&gt;_left == cur) //cur节点在父节点左边，右单旋
					{
						RotateRight(grandfather);
						//变色
						parent-&gt;_col = BLACK;
						grandfather-&gt;_col = RED;
					}
					else //cur节点在父节点右边，左右双旋
					{
						RotateLeft(parent);
						RotateRight(grandfather);
						//变色
						cur-&gt;_col = BLACK;
						grandfather-&gt;_col = RED;
					}
					break;
				}
			}
			else //父节点在祖父节点右边，和上面同理
			{
				Node* uncle = grandfather-&gt;_left;

				if (uncle &amp;&amp; uncle-&gt;_col == RED)
				{
					parent-&gt;_col = uncle-&gt;_col = BLACK;
					grandfather-&gt;_col = RED;

					cur = grandfather;
					parent = cur-&gt;_parent;
				}
				else
				{
					if (parent-&gt;_right == cur)
					{
						RotateLeft(grandfather);
						parent-&gt;_col = BLACK;
						grandfather-&gt;_col = RED;
					}
					else
					{
						RotateRight(parent);
						RotateLeft(grandfather);
						cur-&gt;_col = BLACK;
						grandfather-&gt;_col = RED;
					}
					break;
				}
			}
		}
		_root-&gt;_col = BLACK; //无论如何，都将根变为黑色
		return make_pair(newnode, true);
	}

	void RotateLeft(Node* parent)
	{
		Node* subR = parent-&gt;_right;
		Node* subRL = subR-&gt;_left;

		parent-&gt;_right = subRL;
		if (subRL)
			subRL-&gt;_parent = parent;

		Node* parentParent = parent-&gt;_parent;

		if (parent != _root)
		{
			subR-&gt;_parent = parentParent;
			if (parent == parentParent-&gt;_left)
				parentParent-&gt;_left = subR;
			else
				parentParent-&gt;_right = subR;
		}
		else
		{
			_root = subR;
			subR-&gt;_parent = nullptr;
		}

		subR-&gt;_left = parent;
		parent-&gt;_parent = subR;
	}

	void RotateRight(Node* parent)
	{
		Node* subL = parent-&gt;_left;
		Node* subLR = subL-&gt;_right;

		parent-&gt;_left = subLR;
		if (subLR)
			subLR-&gt;_parent = parent;

		Node* parentParent = parent-&gt;_parent;

		if (parent != _root)
		{
			subL-&gt;_parent = parentParent;
			if (parent == parentParent-&gt;_left)
				parentParent-&gt;_left = subL;
			else
				parentParent-&gt;_right = subL;
		}
		else
		{
			_root = subL;
			subL-&gt;_parent = nullptr;
		}

		subL-&gt;_right = parent;
		parent-&gt;_parent = subL;
	}

	void InOrder()
	{
		_InOrder(_root);
		cout &lt;&lt; endl;
	}

	bool IsBalance()
	{
		if (_root == nullptr)
			return true;
		if (_root-&gt;_col == RED)
		{
			cout &lt;&lt; "异常：根为红色" &lt;&lt; endl;
			return false;
		}
		
		//预先求出某条路径的黑色节点数量
		size_t blackcount = 0;
		Node* cur = _root;
		while (cur)
		{
			if (cur-&gt;_col == BLACK)
				blackcount++;
			cur = cur-&gt;_left;
		}

		size_t k = 0;
		return _IsBalance(_root, k, blackcount);
	}

	iterator Find(const K&amp; key)
	{
		Node* cur = _root;
		KeyOfT kot;
		while (cur)
		{
			if (key &gt; kot(cur-&gt;_data))
				cur = cur-&gt;_right;
			else if (key &lt; kot(cur-&gt;_data))
				cur = cur-&gt;_left;
			else
				return iterator(cur);
		}
		return iterator(nullptr);
	}

	int Height()
	{
		return _Height(_root);
	}

	size_t Size()
	{
		return _Size(_root);
	}
private:
	void _InOrder(Node* root)
	{
		KeyOfT kot;
		if (root == nullptr)
			return;
		_InOrder(root-&gt;_left);
		cout &lt;&lt; kot(root-&gt;_data) &lt;&lt; " ";
		_InOrder(root-&gt;_right);
	}

	bool _IsBalance(Node* root, size_t k, size_t blackcount)
	{
		if (root == nullptr)
		{
			if (k != blackcount)
			{
				cout &lt;&lt; "异常：路径黑节点数目不同" &lt;&lt; endl;
				return false;
			}
			return true;
		}
		if (root-&gt;_col == RED &amp;&amp; root-&gt;_parent-&gt;_col == RED)
		{
			cout &lt;&lt; "异常：出现连续红节点" &lt;&lt; endl;
			return false;
		}
		if (root-&gt;_col == BLACK)
			k++;

		return _IsBalance(root-&gt;_left, k, blackcount)
			&amp;&amp; _IsBalance(root-&gt;_right, k, blackcount);
	}

	int _Height(Node* root)
	{
		if (root == nullptr)
			return 0;
		int higher = max(_Height(root-&gt;_left), _Height(root-&gt;_right));
		return higher + 1;
	}

	size_t _Size(Node* root)
	{
		if (root == nullptr)
			return 0;
		return _Size(root-&gt;_left) + _Size(root-&gt;_right) + 1;
	}
private:
	Node* _root = nullptr;
};
```

---


## 四、模拟实现set

在实现set和map的时候主要把仿函数实现出来就行了，其他接口直接封装红黑树的方法即可

因为红黑树中没有实现删除，所以set和map的删除也不实现了（纯懒）

```
#pragma once
#include "RBTree.h"

namespace Eristic
{
	template&lt;class K&gt;
	class set 
	{
	public:
		struct SetKeyOfT
		{
			const K&amp; operator()(const K&amp; key)
			{
				return key;
			}
		};

		//在set和map中重命名迭代器时不加typename，迭代器运行的时候会报错
		//域作用限定符可以取类型或者静态变量，但是因为变量不能被typedef，所以我们需要用typename告诉编译器是对类型重命名
		typedef typename RBTree&lt;K, K, SetKeyOfT&gt;::const_iterator iterator; 
		typedef typename RBTree&lt;K, K, SetKeyOfT&gt;::const_iterator const_iterator;

		iterator begin() const
		{
			return _t.begin();
		}

		iterator end() const
		{
			return _t.end();
		}

		pair&lt;iterator, bool&gt; insert(const K&amp; key)
		{
			return _t.insert(key);
		}

		void InOrder()
		{
			_t.InOrder();
		}
	private:
		RBTree&lt;K, K, SetKeyOfT&gt; _t;
	};
}
```

---


## 五、模拟实现map

```
#pragma once
#include "RBTree.h"

namespace Eristic
{
	template&lt;class K,class T&gt;
	class map
	{
	public:
		struct MapKeyOfT
		{
			const K&amp; operator()(const pair&lt;K, T&gt;&amp; kv)
			{
				return kv.first;
			}
		};

		typedef typename RBTree&lt;K, pair&lt;const K, T&gt;, MapKeyOfT&gt;::iterator iterator;
		typedef typename RBTree&lt;K, pair&lt;const K, T&gt;, MapKeyOfT&gt;::const_iterator const_iterator;
		
		iterator begin()
		{
			return _t.begin();
		}

		iterator end()
		{
			return _t.end();
		}

		const_iterator begin() const
		{
			return _t.begin();
		}

		const_iterator end() const
		{
			return _t.end();
		}

		pair&lt;iterator, bool&gt; insert(const pair&lt;K, T&gt;&amp; kv)
		{
			return _t.insert(kv);
		}

		void InOrder()
		{
			_t.InOrder();
		}

		T&amp; operator[](const K&amp; key)
		{
			pair&lt;iterator, bool&gt; p = insert(make_pair(key, T()));
			return p.first-&gt;second;
		}
	private:
		RBTree&lt;K, pair&lt;const K, T&gt;, MapKeyOfT&gt; _t;
	};
}
```

完.
