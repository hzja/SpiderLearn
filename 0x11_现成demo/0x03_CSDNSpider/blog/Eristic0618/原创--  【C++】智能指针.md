# 原创
：  【C++】智能指针

# 【C++】智能指针

**目录**

[一、为什么需要智能指针](#%E4%B8%80%E3%80%81%E4%B8%BA%E4%BB%80%E4%B9%88%E9%9C%80%E8%A6%81%E6%99%BA%E8%83%BD%E6%8C%87%E9%92%88)

[二、什么是内存泄漏](#%E4%BA%8C%E3%80%81%E4%BB%80%E4%B9%88%E6%98%AF%E5%86%85%E5%AD%98%E6%B3%84%E6%BC%8F)

[三、智能指针](#%E4%B8%89%E3%80%81%E6%99%BA%E8%83%BD%E6%8C%87%E9%92%88)

[3.1 原理](#3.1%20%E5%8E%9F%E7%90%86)

[3.2 auto_ptr](#3.2%20auto_ptr)

[3.3 unique_ptr](#3.3%20unique_ptr)

[3.4 shared_ptr](#3.4%20shared_ptr)

[3.5 weak_ptr](#3.5%20weak_ptr)

[3.6 boost C++库与智能指针](#3.6%C2%A0boost%20C%2B%2B%E5%BA%93%E4%B8%8E%E6%99%BA%E8%83%BD%E6%8C%87%E9%92%88)

---


## 一、为什么需要智能指针

在前面讲C++异常的时候提到过，在代码中抛出异常可能会导致执行流意外跳出函数，而函数中动态分配的空间没有被释放，造成**内存泄漏**

例如：

```
int div()
{
	int a = 1;
	int b = 0;
	if (b == 0)
		throw "Division by zero condition!"; //除零错误
	else
		return a / b;
}

void Func()
{
	int* p1 = new int;
	int* p2 = new int;

	div(); //抛出异常

	cout &lt;&lt; "开始释放动态分配的空间" &lt;&lt; endl;
	delete p1;
	delete p2;
}

int main()
{
	try {
		Func(); 
	}
	catch (const char* errmsg) 
	{
		cout &lt;&lt; "捕获异常：" &lt;&lt; errmsg &lt;&lt; endl;
	}
	catch (...) 
	{
		cout &lt;&lt; "捕获未知异常" &lt;&lt; endl;
	}
	return 0;
}
```

在Func函数中有两个指针指向了动态分配的空间，在函数结束的时候我们也必须要释放它们，否则会造成内存泄漏。但是中间调用div函数的时候会抛出异常，那还能否正常的释放这些空间呢？

可以看到，抛出异常后执行流就直接跳出Func函数，到了main函数中捕获异常的位置了。Func中申请的空间也没有被释放，造成内存泄漏

---


## 二、什么是内存泄漏

像上面这样，在程序中通过malloc/calloc/realloc/new等内存管理函数动态分配的堆内存空间，使用完后没有被free/delete释放，就会造成**堆内存泄露**（Heap leak）。

因为疏忽或错误设计导致程序未能释放已经不再使用的内存的情况就叫做内存泄漏。内存泄漏并不是指内存完全消失，而是程序失去了对这些内存的控制。如果一次性泄露很多内存，我们可能很快就会发现，但有时内存泄漏常常是积少成多的，程序运行着越来越慢，最后导致卡死。

除了堆内存泄漏，程序使用系统分配的资源，如套接字、文件描述符、管道等，使用完后没有通过对应的函数释放，会导致系统资源的浪费，这属于**系统资源泄露**。

要避免内存泄漏，一方面我们要养成良好的编码规范，申请的资源记得释放。但是如果碰上了例如上面这种抛出异常的场景，即使再怎么小心也没有办法解决。

因此，对于这些资源，我们一般采用**RAII思想**来管理

---


## 三、智能指针

### 3.1 原理

**智能指针是RAII思想的一种实现方式**，何为RAII？

RAII（Resource Acquisition Is Initialization，资源获取即初始化），通过将我们获取到的资源的生命周期与某个对象的生命周期绑定在一起，利用这个对象的生命周期来控制程序资源。

通过这种方式，我们只需要在对象的**构造函数中获取资源**，在**析构函数中释放资源**，利用类对象出作用域会自动析构的特点来自动释放资源，就完成了资源管理的托管。

这种方式有两大好处：

根据RAII思想，我们可以设计出一个**管理指针的一个类**，只需要在这个类构造函数中获取指针，并在析构函数中将指针指向的空间释放，就能完成对动态分配的空间的管理，这就是智能指针

既然是智能指针，我们要让其能够像指针一样被使用，所以还需要在类内部重载解引用操作符(*)和箭头操作符(-&gt;)

现在，我们就可以设计一个最简单的智能指针了：

```
template&lt;class T&gt;
class SmartPtr
{
public:
	SmartPtr(T* ptr = nullptr)
		:_ptr(ptr)
	{}

	T&amp; operator*() { return *_ptr; }

	T* operator-&gt;() { return _ptr; }

	~SmartPtr()
	{
		cout &lt;&lt; "~SmartPtr()" &lt;&lt; endl;
		if (_ptr)
			delete _ptr;
	}
private:
	T* _ptr;
};
```

把上面的指针换成智能指针，看看效果如何：

可以看到，智能指针也能够像普通指针一样使用，并且在抛出异常后也会调用自己的析构函数，将资源释放，避免了内存泄漏

总结下来，智能指针的原理其实就两个：

上面我们实现的只是最简单的智能指针，具有智能指针的基础行为，在实际中还需要考虑更多的问题，例如指针的赋值等。为了解决这些问题，在C++的发展史中也曾诞生多个版本的智能指针

### 3.2 auto_ptr

上面我们实现的智能指针，虽然已经能够实现自动释放资源了，但是还有一些问题没有被解决

例如，假设我们将一个智能指针赋值给另外一个智能指针：

```
void Func()
{
	SmartPtr&lt;int&gt; p1(new int);
	SmartPtr&lt;int&gt; p2 = p1;
}

int main()
{
	Func();
	return 0;
}
```

会发生什么呢？

此时，两个智能指针指向了同一块空间，析构时这块空间**被释放了两次**，导致发生错误

C++98的**auto_ptr**，针对这种问题给出了解决方案，即拷贝时将等号右侧的智能指针置为空

```
int main()
{
	auto_ptr&lt;int&gt; p1(new int);
	auto_ptr&lt;int&gt; p2 = p1;
	return 0;
}
```

乍一听好像合理，解决了空间被重复释放的问题，但是指针管理权转移导致智能指针被置空的情况，遇到不熟悉机制的人就容易导致发生空指针错误，例如：

并且，auto_ptr不支持对数组的内存管理

所以，auto_ptr其实是一个失败的设计，被很多人所诟病

要模拟实现auto_ptr也很简单，只需要在拷贝构造和赋值运算符重载函数中进行指针的管理权转移即可

```
namespace Eristic
{
	template&lt;class T&gt;
	class auto_ptr
	{
	public:
		auto_ptr(T* ptr)
			:_ptr(ptr)
		{}

		auto_ptr(auto_ptr&lt;T&gt;&amp; ap)
			:_ptr(ap._ptr)
		{
			ap._ptr = nullptr; //置空
		}

		auto_ptr&lt;T&gt;&amp; operator=(auto_ptr&lt;T&gt;&amp; ap)
		{
			if (this != &amp;ap) //避免自己给自己赋值的情况
			{
				if (_ptr)
					delete _ptr; //释放原有空间
				_ptr = ap._ptr;
				ap._ptr = nullptr;
			}
			return *this;
		}

		T&amp; operator*()
		{
			return *_ptr;
		}

		T* operator-&gt;()
		{
			return _ptr;
		}

		~auto_ptr()
		{
			if (_ptr)
				delete _ptr;
		}

	private:
		T* _ptr;
	};
}
```

智能指针有三个常用的类方法，在这里用auto_ptr演示一下

使用这个函数后，智能指针就不再对自己内部的指针进行管理，申请的资源需要我们手动释放

```
int main()
{
	auto_ptr&lt;int&gt; ap(new int);
	int* p1 = ap.release();
	delete p1;
	return 0;
}
```

### 3.3 unique_ptr

C++11之后，出现了**unique_ptr**，其特点在于直接**禁止**了智能指针的拷贝与赋值

这样，就不会导致智能指针因管理权转移而被置空，造成可能存在的空指针错误 

要实现这一点也很简单，将拷贝构造和赋值重载只声明不实现，并限定为私有，这样就可以避免有人在类外重新实现或调用这两个函数了。或者直接用delete修饰拷贝构造和赋值重载，也可以起到相同效果。

如果只是简单的禁止智能指针的拷贝与赋值，那么其功能要模拟实现也十分简单：

```
namespace Eristic
{
	template&lt;class T&gt;
	class unique_ptr
	{
	public:
		unique_ptr(T* ptr)
			:_ptr(ptr)
		{}

		~unique_ptr()
		{
			if (_ptr)
				delete _ptr;
		}
	
		T&amp; operator*()
		{
			return *_ptr;
		}

		T* operator-&gt;()
		{
			return _ptr;
		}

		unique_ptr(const unique_ptr&lt;T&gt;&amp; sp) = delete;
		unique_ptr&lt;T&gt;&amp; operator=(const unique_ptr&lt;T&gt;&amp; sp) = delete;
	private:
		T* _ptr;
	};
}
```

不过，虽然unique_ptr不能进行左值拷贝赋值操作，但允许move右值拷贝和赋值，例如：

并且，unique_ptr还支持对数组的内存管理

既然unique_ptr能够管理数组的内存空间，那么其内部必须要针对不同情况选择调用delete和delete[]，这又是如何做到的呢？

其实是因为unique_ptr需要支持**自定义删除器**，即我们可以传入一个函数对象，用于智能指针对空间的释放。例如有时候智能指针指向的资源可能不是new出来的，也可能是malloc出来的，这时我们就无法用delete来释放资源了，需要自己定义一个函数对象来释放

不仅unique_ptr，后面的shared_ptr也支持自定义删除器，不过二者有一些不同之处，我们从二者的定义中也能看出来

可以看到，unique_ptr的第二个模板参数是一个缺省参数，在我们使用unique_ptr并传入自定义删除器时需要对该参数进行说明

```
template&lt;class T&gt;
struct DelArray
{
	void operator()(T* ptr)
	{
		delete[] ptr;
	}
};

int main()
{
	unique_ptr&lt;int, DelArray&lt;int&gt;&gt; p1(new int[5], DelArray&lt;int&gt;());
	return 0;
}
```

自定义删除器可以是普通函数，可以是仿函数，也可以是lambda表达式，由用户自己决定

### 3.4 shared_ptr

我们的原生指针是允许多个指针指向同一块空间的，而显然上面的auto_ptr和unique_ptr并没有符合指针的这一性质，因此C++11又提供了一种智能指针：**shared_ptr**

shared_ptr通过**引用计数**的方式来实现多个shared_ptr之间共同管理同一块空间，即shared_ptr赋值或拷贝一次，引用计数加一。直到引用计数为0，管理的空间才会被释放

通过use_count()方法我们可以获取shared_ptr的引用计数，例如：

多个shared_ptr对象指向同一份资源，当其中一个对象被销毁，则引用计数减一，如果销毁后引用计数变为0，则说明该对象是最后一个管理这份资源的对象，需要负责资源的释放；如果不为0，则说明还有别的对象在管理这份资源，不能释放，否则可能造成野指针错误

shared_ptr除了可以用构造函数初始化，也可以用make_shared

要实现shared_ptr的基础版本也很简单，将引用计数引入智能指针即可

```
namespace Eristic
{
	template&lt;class T&gt;
	class shared_ptr
	{
	public:
		shared_ptr(T* ptr = nullptr)
			:_ptr(ptr)
			,_pcount(new int(1))
		{}

		shared_ptr(const shared_ptr&lt;T&gt;&amp; sp)
			:_ptr(sp._ptr)
			,_pcount(sp._pcount)
		{
			++(*_pcount); //增加引用计数
		}

		shared_ptr&lt;T&gt;&amp; operator=(shared_ptr&lt;T&gt;&amp; sp)
		{
			if (_ptr != sp._ptr)
			{
				release(); //shared_ptr改变指向前需要对原来的引用计数减1
				_ptr = sp._ptr;
				_pcount = sp._pcount;
				++(*_pcount); //增加引用计数
			}
			return *this;
		}

		T&amp; operator*() { return *_ptr; }

		T* operator-&gt;() { return _ptr; }

		void release()
		{
			--(*_pcount); //对象被析构，引用计数减1
			if (*_pcount == 0) //引用计数为0时才释放空间
			{
				delete _ptr;
				delete _pcount;
			}
		}

        int use_count()
		{
			return *_pcount;
		}

		~shared_ptr()
		{
			release();
		}
	private:
		T* _ptr;
		int* _pcount; //引用计数
	};
}
```

但是，shared_ptr也有一个缺点，当遇到两个shared_ptr互相指向对方时，可能导致循环引用问题

例如双向链表，节点中存在指针next和prev

```
struct ListNode
{
	int _val;
	Eristic::shared_ptr&lt;ListNode&gt; prev;
	Eristic::shared_ptr&lt;ListNode&gt; next;

	~ListNode()
	{
		cout &lt;&lt; "~ListNode()" &lt;&lt; endl;
	}
};
```

此时让两个节点互相指向，就会导致循环引用，造成内存泄漏

可以看到并没有打印任何东西，说明ListNode的析构函数没有被调用，造成内存泄漏

循环引用是什么？为什么会导致shared_ptr无法释放自己管理的空间？我们用一张图解释

循环引用会导致两个互相指向的shared_ptr在各自析构后，引用计数仍不为0，所以不会释放资源

可以看到，二者的引用计数都是2 

要解决这个问题，还需要使用另一种智能指针：weak_ptr

### 3.5 weak_ptr

weak_ptr设计的目的是为了配合shared_ptr解决循环引用问题，一个weak_ptr对象只能由另一个shared_ptr或weak_ptr构造而来，且不会造成引用计数的增加或减少

可以看到，将ListNode中的shared_ptr换成weak_ptr，就能够正常释放资源了，因为其不会造成引用计数的变化，所以避免了上面的情况

需要注意的是，shared_ptr没有重载解引用操作符和箭头操作符，所以不支持像指针一样使用。但是我们可以通过调用其lock()方法生成一个新的shared_ptr

weak_ptr不支持RAII，它不是一个传统的智能指针

weak_ptr也会使用shared_ptr的引用计数，我们也可以通过调用use_count()来获取其引用计数

另外，我们还可以使用expired函数检测其指向的shared_ptr是否被释放，未释放返回false，已释放返回true

### 3.6 boost C++库与智能指针

C++中的boost库相当于C++标准库的体验服，由boost社区负责开发和发布，开发人员遍布全球，负责开发和收集高质量的库，作为C++标准的补充。boost库中被证实有价值且实用的库则有机会在未来被纳入到C++标准中

scoped_ptr（即现在的unique_ptr）、shared_ptr和weak_ptr都是在boost库中经过了大众的检验，才敢正式使用，以避免当初auto_ptr的糟糕设计

完.
