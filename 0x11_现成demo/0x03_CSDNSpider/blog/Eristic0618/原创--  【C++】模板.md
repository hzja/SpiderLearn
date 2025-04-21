# 原创
：  【C++】模板

# 【C++】模板

[前言](#%E5%89%8D%E8%A8%80)

[一、泛型编程](#%E4%B8%80%E3%80%81%E6%B3%9B%E5%9E%8B%E7%BC%96%E7%A8%8B)

[二、函数模板](#%E4%BA%8C%E3%80%81%E5%87%BD%E6%95%B0%E6%A8%A1%E6%9D%BF)

[2.1 概念](#2.1%20%E6%A6%82%E5%BF%B5)

[2.2 格式](#2.2%20%E6%A0%BC%E5%BC%8F)

[2.3 函数模板的实例化](#2.3%20%E5%87%BD%E6%95%B0%E6%A8%A1%E6%9D%BF%E7%9A%84%E5%AE%9E%E4%BE%8B%E5%8C%96)

[（1）隐式实例化](#%EF%BC%881%EF%BC%89%E9%9A%90%E5%BC%8F%E5%AE%9E%E4%BE%8B%E5%8C%96)

[2.4 模板参数的匹配原则](#2.4%20%E6%A8%A1%E6%9D%BF%E5%8F%82%E6%95%B0%E7%9A%84%E5%8C%B9%E9%85%8D%E5%8E%9F%E5%88%99)

[三、类模板](#%E4%B8%89%E3%80%81%E7%B1%BB%E6%A8%A1%E6%9D%BF)

[3.1 格式](#3.1%20%E6%A0%BC%E5%BC%8F)

[3.2 成员函数声明和定义分离 ](#3.2%20%E6%88%90%E5%91%98%E5%87%BD%E6%95%B0%E5%A3%B0%E6%98%8E%E5%92%8C%E5%AE%9A%E4%B9%89%E5%88%86%E7%A6%BB%C2%A0)

## 前言

远古时候，文章和诗歌的传播只能靠手抄，既费时又费力。直到印刷术的出现，文字的传播才变得容易起来。

在写C++程序时，我们有时候也会遇到一些大量且重复的问题，例如不同类型的交换函数，虽然我们有了函数重载，但是仍然需要自己一个个的去实现

为了避免这种问题，模板出现了。

---


## 一、泛型编程

上面提到，我们虽然可以用函数重载来实现不同类型的交换函数

```
void Swap(int&amp; left, int&amp; right)
{
	int temp = left;
	left = right;
	right = temp;
}

void Swap(double&amp; left, double&amp; right)
{
	double temp = left;
	left = right;
	right = temp;
}

void Swap(char&amp; left, char&amp; right)
{
	char temp = left;
	left = right;
	right = temp;
}

//...

```

这种方法除了麻烦，还有一些其他的弊端：

如果能有一个模具，只需要填入一个类型，就可以产生一个对应的函数，那不就方便许多了吗

这里引入泛型编程的概念：编写**与类型无关**的通用代码，是代码复用的一种手段。

模板是泛型编程的基础，又分为函数模板和类模板

---


## 二、函数模板

### 2.1 概念

函数模板代表了一个函数家族，与类型无关，在使用时**根据实参类型实例化出特定类型的版本**。

 

### 2.2 格式

> 
template&lt;typename T1, typename T2, ...... , typename Tn&gt;
返回类型 函数名（参数列表）
{
        函数体<br/> }


例如我们实现一个交换函数的模板

```
template&lt;class T&gt; //class也可以用typename
void Swap(T&amp; left, T&amp; right)
{
	T temp = left;
	left = right;
	right = temp;
}
```

typename是用来定义模板参数的**关键字**，也可以用class，但是不能用struct

 

### 2.3 函数模板的实例化

<img alt="" height="403" src="https://i-blog.csdnimg.cn/blog_migrate/75c14bd4e75c3fd275e2bd64803bb207.png" width="503"/> 

这两个调用的是同一个函数吗？

我们打开反汇编： 

<img alt="" height="518" src="https://i-blog.csdnimg.cn/blog_migrate/0e5ec604bf3c46ee23ddd72f60ae1d74.png" width="713"/> 

可以看到调用的并不是同一个函数 

函数模板就像一个蓝图，**本身并不是函数**，而是编译器根据参数产生具体类型函数的模具。

所以使用函数模板就相当于把我们要做的重复的动作交给了编译器完成。

使用函数模板创建不同类型的函数，称为函数模板的实例化，其中又分为隐式实例化和显式实例化

#### （1）隐式实例化

在编译阶段，编译器**根据传入的实参类型来推演实例化函数的对应类型**，称为隐式实例化

像这样，一个参数是int类型，一个是double类型，编译器就无法推演此处到底该将T的类型确定为int还是double而报错

此时有两种处理方式：

例如：

（2）显式实例化

在函数名后面加上&lt;类型&gt;即可指定模板参数的实际类型，例如：

显式实例化，就不需要编译器来推演类型了，直接使用我们指定的类型，和指定类型不同类的参数就进行隐式类型转换

### 2.4 模板参数的匹配原则

**（1）一个非模板函数可以和一个用途相同、名字相同的函数模板同时存在，并且该函数模板可以被实例化为这个非模板函数**

例如我们有一个专门处理int类型的Add函数，和一个通用的Add函数

```
//专门处理int类型
int Add(const int&amp; left, const int&amp; right)
{
	return left + right;
}

//通用
template&lt;class T&gt;
T Add(const T&amp; left, const T&amp; right)
{
	return left + right;
}

int main()
{
	Add(1, 2); //与非模板函数匹配，不需要使用函数模板
	Add&lt;int&gt;(1, 2); //显式实例化指定类型，需要调用函数模板

	return 0;
}
```

**（2）如果用模板函数实例化的条件和调用非模板函数的条件相同，则优先调用非模板函数而不会进行实例化 **

第一个Add中的参数既可以调用非模板，也可以用模板函数实例化，所以直接用非模板函数

如果非要用函数模板，那就显式实例化

我们可以验证一下：

函数模板实例化出的函数与int类型的非模板函数构成重载

---


## 三、类模板

### 3.1 格式

类模板和函数模板类似

> 
template&lt;class T1, class T2, ...... , class Tn&gt;
class 类模板名
{
        类体
};


对于类模板，为什么我们不能像以前C语言一样用typedef呢？

因为typedef只能解决部分问题，遇到下面这种情况就无能为力了：

现在我们可以自己试着定义一个栈的类模板

```
template&lt;class T&gt;
class Stack 
{
public:
	Stack(int capacity = 4)
	{
		_a = new T[capacity];
		_top = 0;
		_capacity = capacity;
	}

    //...

	~Stack()
	{
		delete[] _a;
		_top = _capacity = 0;
	}
private:
	T* _a;
	size_t _top;
	size_t _capacity;
};
```

此时对于栈的类模板，因为构造函数是全缺省，我们不一定要传参，编译器也就无法推演类型

所以需要我们进行显式实例化：

学到这里，一些以前看不到懂的代码也能看懂了，例如：

```
int main()
{
	vector&lt;int&gt; v1;

	for (size_t i = 0; i &lt; v1.size(); ++i)
	{
		cout &lt;&lt; v1[i] &lt;&lt; " ";
	}
	cout &lt;&lt; endl;

	return 0;
}
```

就是实例化出了一个int类型的vector，访问其成员函数size获取数据个数，通过循环迭代和[]运算符重载打印出它的内容

需要提醒的是，vector是类名，vector&lt;int&gt;才是类型

### 3.2 成员函数声明和定义分离 

以我们的动态顺序表为例：

```
template&lt;class T&gt;
class Vector
{
public:
	Vector(size_t capacity = 10)
		: _pData(new T[capacity])
		, _size(0)
		, _capacity(capacity)
	{}

	~Vector(); //我们以析构函数为例，在类内声明类外定义

	void PushBack(const T&amp; data)；
	void PopBack()；
	// ...

private:
	T* _pData;
	size_t _size;
	size_t _capacity;
};

template &lt;class T&gt; //类模板中函数放在类外进行定义时，需要加模板参数列表
Vector&lt;T&gt;::~Vector()
{
	if (_pData)
		delete[] _pData;
	_size = _capacity = 0;
}
```

在类外定义类模板中的函数时，作用域限定符前不能只用类名，而是要用类型，并且加上模板参数和声明

最后，类模板只能在同一个文件上声明和定义。例如分别在.h文件和.cpp文件上声明和定义，会出现链接错误。

如果文章有误，欢迎在评论区指出
