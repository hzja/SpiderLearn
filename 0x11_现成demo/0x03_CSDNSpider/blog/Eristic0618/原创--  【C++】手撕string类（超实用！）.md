# 原创
：  【C++】手撕string类（超实用！）

# 【C++】手撕string类（超实用！）

[前言](#%E5%89%8D%E8%A8%80)

[一、标准库中的string类](#%E4%B8%80%E3%80%81%E6%A0%87%E5%87%86%E5%BA%93%E4%B8%AD%E7%9A%84string%E7%B1%BB)

[1.1 string类介绍](#1.1%20string%E7%B1%BB%E4%BB%8B%E7%BB%8D)

[1.2 string的常用接口](#1.2%20string%E7%9A%84%E5%B8%B8%E7%94%A8%E6%8E%A5%E5%8F%A3)

[1.2.1 常用的构造函数](#1.2.1%20%E5%B8%B8%E7%94%A8%E7%9A%84%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0)

[1.2.2 容量操作接口](#1.2.2%20%E5%AE%B9%E9%87%8F%E6%93%8D%E4%BD%9C%E6%8E%A5%E5%8F%A3)

[（1）size](#%EF%BC%881%EF%BC%89size)

[（2）capacity ](#%EF%BC%882%EF%BC%89capacity%C2%A0)

[（3）empty ](#%EF%BC%883%EF%BC%89empty%C2%A0)

[（4）clear ](#%EF%BC%884%EF%BC%89clear%C2%A0)

[（5）reserve ](#%EF%BC%885%EF%BC%89reserve%C2%A0)

[（6）resize ](#%EF%BC%886%EF%BC%89resize%C2%A0)

[1.2.3 访问和遍历](#1.2.3%20%E8%AE%BF%E9%97%AE%E5%92%8C%E9%81%8D%E5%8E%86)

[（1）operator[] ](#%EF%BC%881%EF%BC%89operator%5B%5D%C2%A0)

[（2）迭代器 ](#%EF%BC%882%EF%BC%89%E8%BF%AD%E4%BB%A3%E5%99%A8%C2%A0)

[（3）at ](#%EF%BC%883%EF%BC%89at%C2%A0)

[（4）back](#%EF%BC%884%EF%BC%89back)

[（5）front](#%EF%BC%885%EF%BC%89front)

[（6）find](#%EF%BC%886%EF%BC%89find)

[（7）rfind和npos](#%EF%BC%887%EF%BC%89rfind%E5%92%8Cnpos)

[（8）c_str](#%EF%BC%888%EF%BC%89c_str)

[1.2.4 修改字符串操作](#1.2.4%20%E4%BF%AE%E6%94%B9%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%93%8D%E4%BD%9C)

[（1）operator+=](#%EF%BC%881%EF%BC%89operator%2B%3D)

[（2）push_back](#%EF%BC%882%EF%BC%89push_back)

[（3）append](#%EF%BC%883%EF%BC%89append)

[（4）insert](#%EF%BC%884%EF%BC%89insert)

[（5）erase](#%EF%BC%885%EF%BC%89erase)

[（6）swap](#%EF%BC%886%EF%BC%89swap)

[（7）operator+](#%EF%BC%887%EF%BC%89operator%2B)

[（8）getline](#%EF%BC%888%EF%BC%89getline)

[1.2.5 各种运算符重载函数](#1.2.5%20%E5%90%84%E7%A7%8D%E8%BF%90%E7%AE%97%E7%AC%A6%E9%87%8D%E8%BD%BD%E5%87%BD%E6%95%B0)

[（1）operator&gt;&gt;和operator&lt;&lt;](#%EF%BC%881%EF%BC%89operator%3E%3E%E5%92%8Coperator%3C%3C)

[（2）比较运算符](#%EF%BC%882%EF%BC%89%E6%AF%94%E8%BE%83%E8%BF%90%E7%AE%97%E7%AC%A6)

[二、模拟实现string类](#%E4%BA%8C%E3%80%81%E6%A8%A1%E6%8B%9F%E5%AE%9E%E7%8E%B0string%E7%B1%BB)

---


## 前言

学习string类之前，我们需要对STL库有一个简单的了解

STL（standard template library——标准模板库），是**C++标准库的重要组成部分**，不仅是一个可复用的组件库，还是一个包罗数据结构与算法的软件框架。

STL有六大组件：

---


## 一、标准库中的string类

### 1.1 string类介绍

string类是表示字符串的一个类，内部通常有三个成员变量：指向字符串的指针、字符串的有效元素个数和字符串的容量大小

```
char* _str;
size_t _size;
size_t _capacity;
```

我们通过string类中的成员函数（接口），就能对字符串进行各种操作

在使用string类时，必须包含头文件&lt;string&gt;和using namespace std;

### 1.2 string的常用接口

#### 1.2.1 常用的构造函数

> 

**string();**



默认构造函数，用于构造空的string类对象

例如：

```
void Test()
{
    string s1;
}
```

> 

**string(const char* s);**



用一个常量字符串来构造string类对象

例如：

```
void Test()
{
    string s1("hello");
}
```

> 

**string(const string&amp; s);**



string类的拷贝构造函数

例如：

```
void Test()
{
    string s1("hello");
    string s2(s1);
}

```

#### 1.2.2 容量操作接口

##### （1）size

> 
**size_t size() const;**


返回字符串有效字符长度

string类中还有一个函数length和size的效果一样，最初只有length存在，为了和其他容器相同后面新增了size

例如：

##### （2）capacity 

> 
**size_t capacity() const;**


返回字符串容量

例如：

##### （3）empty 

> 
**bool empty()  const;**


 检测字符串是否为空串，为空返回true，否则返回false

例如：

##### （4）clear 

> 
**void clear();**


用于清空有效字符，不改变字符串容量大小

例如：

##### （5）reserve 

> 
**void reserve(size_t n = 0);**


为字符串预留空间

例如：

如果n比原容量小则不作改变

在vs上常常会开比n更大一些的空间

##### （6）resize 

> 
**void resize(size_t n);**
**void resize(size_t n, char c);**


将有效字符的个数修改为n，并且如果n大于原来的_size，多出来的地方用字符c填充，不改变字符串容量大小

如果没有给出字符c，则用\0填充

例如：

#### 1.2.3 访问和遍历

##### （1）operator[] 

> 
**char&amp; operator[](size_t pos);**
**const char&amp; operator[](size_t pos) const;**


返回字符串中pos位置的字符

例如：

##### （2）迭代器 

> 
**iterator begin();**
**const_iterator begin() const;**
**iterator end();**
**const_iterator end() const;**


迭代器，用于获取字符串第一个字符的位置和最后一个字符的**下一个位置**

例如：

> 
**reverse_iterator rbegin();**
**const_reverse_iterator rbegin() const;**
**reverse_iterator rend();**
**const_reverse_iterator rend() const;**


反向迭代器，rbegin获取字符串最后一个字符的位置，rend获取字符串的第一个字符的前一个位置

例如：

需要注意，这里rit是加加而不是减减

**范围for的底层实际上也是迭代器**

##### （3）at 

> 
**char&amp; at(size_t pos);**
**const char&amp; at(size_t pos) const;**


返回字符串中pos位置的字符的引用

例如：

##### （4）back

> 
**char&amp; back();**
**const char&amp; back() const;**


返回字符串最后一个字符的引用

例如：

##### （5）front

> 
**char&amp; front();**
**const char&amp; front() const;**


返回字符第一个字符串的引用

例如：

##### （6）find

> 
**size_t find(char c, size_t pos = 0) const;**


从字符串的pos位置向后找字符c，返回该字符在字符串中的位置

例如：

##### （7）rfind和npos

> 
**size_t rfind(char c, size_t pos = npos) const;**
**static const size_t nops = -1**


从字符串的pos位置向前找字符c，返回该字符在字符串中的位置

npos是string类中定义的一个静态成员变量，类型为无符号整型，值为-1，因为是无符号转换后变成整型的最大值，也就是4294967295（42亿多），当我们不给pos的值时按照缺省值执行，默认从字符串尾部开始找起

例如：

##### （8）c_str

> 
**const char* c_str() const;**


按照C语言的格式返回字符串

例如：

在hello后面加上\0和字符串world，重载后的流插入操作符函数会按照size的大小来打印字符串

而打印c_str的返回值，会遇到\0就停下

#### 1.2.4 修改字符串操作

##### （1）operator+=

> 
**string&amp; operator+=(const string&amp; str);**
**string&amp; operator+=(const char* s);**
**string&amp; operator+=(char c);**


在字符串后追加一个字符串或字符

例如：

##### （2）push_back

> 
**void push_back(char c);**


在字符串后尾插一个字符c

例如：

##### （3）append

> 
**string&amp; append(const string&amp; str);**
**string&amp; append(const char* s);**
**string&amp; append(const char* s, size_t n);**
**string&amp; append(size_t n, char c);**


用于在字符串后加一个字符串、一个字符串的前n个字符或n个字符c

例如：

##### （4）insert

> 
**string&amp; insert(size_t pos, const string&amp; str);**
**string&amp; insert(size_t pos, const char* s);**
**string&amp; insert(size_t pos, const char* s, size_t n);**
**string&amp; insert(size_t pos, size_t n, char c);**
**iterator insert(iterator p, char c);**


用于在字符串的pos位置插入一个字符串、字符串的前n个字符或n个字符c

还有迭代器版本的insert，用法是在p的位置插入字符c 

例如：

##### （5）erase

> 
**string&amp; erase(size_t pos, size_t len = npos);**
**iterator erase(iterator p);**
**iterator erase(iterator first, iterator last);**


用于在字符串的pos位置删除len个字符

迭代器版本的erase，在p的位置删除一个字符，或者删除 [ first , last ) 内的字符

例如：

##### （6）swap

> 
**void swap(string&amp; str);**


用于交换两个string类对象

string类中的swap函数相比标准库中的swap函数，交换string类对象的效率更高

例如：

##### （7）operator+

> 
**string operator+(const string&amp; lhs, const string&amp; rhs);**
**string operator+(const string&amp; lhs, const char* rhs);**
**string operator+(const char* lhs, const string&amp; rhs);**
**string operator+(const string&amp; lhs, char rhs);**
**string operator+(char lhs, const string&amp; rhs);**


返回一个新构造的string类对象，其值是lhs和rhs的合并

例如：

##### （8）getline

> 
**istream&amp; getline(istream&amp; is, string&amp; str, char delim);**
**istream&amp; getline(istream&amp; is, string&amp; str);**


用于字符串的输入

相比cin遇到空格就停止提取，我们可以给出分隔符delim，遇到delim才停止提取，如果没有给出，则遇到换行停止提取

例如：

#### 1.2.5 各种运算符重载函数

##### （1）operator&gt;&gt;和operator&lt;&lt;

> 
**istream&amp; operator&gt;&gt;(istream&amp; is, string&amp; str);**
**ostream&amp; operator&lt;&lt;(ostream&amp; os, const string&amp; str);**


用于string对象的流提取和流插入

例如：

##### （2）比较运算符

各种比较运算符的重载函数，这里就不赘述了

用于比较两个字符串的对应位置的ASCII码值大小

例如：

---


## 二、模拟实现string类

知道了string类中各种常用接口的用法后，我们就可以开始自己手撕一个自己的string类了

为了不和标准库中的string类冲突，我们可以开一个自己的命名空间

完整代码如下：

```
namespace Eristic
{
	class string
	{
		friend ostream&amp; operator&lt;&lt;(ostream&amp; cout, const string&amp; s);
		friend istream&amp; operator&gt;&gt;(istream&amp; cout, const string&amp; s);
	public:
		typedef char* iterator;
		typedef const char* const_iterator;

		iterator begin()
		{
			return _str;
		}

		iterator end()
		{
			return _str + _size;
		}

		const_iterator begin() const
		{
			return _str;
		}

		const_iterator end() const
		{
			return _str + _size;
		}

		string(const char* str = "")
			:_size(strlen(str))
		{
			_capacity = _size == 0 ? 3 : _size;
			_str = new char[_capacity + 1];
			strcpy(_str, str);
		}

		void reserve(size_t n)
		{
			if (n &gt; _capacity)
			{
				char* tmp = new char[n + 1];
				strcpy(tmp, _str);
				delete[] _str;
				_str = tmp;
				_capacity = n;
			}
		}

		bool empty() const
		{
			size_t len = strlen(_str);
			return !len;
		}

		char&amp; at(size_t pos)
		{
			assert(pos &lt; _size);
			return _str[pos];
		}

		const char&amp; at(size_t pos) const
		{
			assert(pos &lt; _size);
			return _str[pos];
		}

		char&amp; back()
		{
			return at(_size - 1);
		}

		const char&amp; back() const
		{
			return at(_size - 1);
		}

		char&amp; front()
		{
			return at(0);
		}

		const char&amp; front() const
		{
			return at(0);
		}

		void resize(size_t n, char ch = '\0')
		{
			if (n &lt; _size)
			{
				_size = n;
				_str[_size] = '\0';
			}
			else if (n &gt; _size)
			{
				if (n &gt; _capacity)
				{
					reserve(n);
				}
				for (size_t i = _size; i &lt; n; i++)
				{
					_str[i] = ch;
				}
				_size = n;
				_str[_size] = '\0';
			}
		}

		void push_back(char ch)
		{
			if (_size + 2 &gt; _capacity)
			{
				reserve(_capacity * 2);
			}
			_str[_size] = ch;
			_size++;
			_str[_size] = '\0';
			//insert(_size, ch); //或者直接复用
		}

		void push_back(const char* str)
		{
			append(str);
		}

		void append(const char* str)
		{
			int len = strlen(str);
			if (_size + len &gt; _capacity)
			{
				reserve(_size + len);
			}
			strcpy(_str + _size, str);
			_size += len;
		}

		string&amp; insert(size_t pos, char ch)
		{
			assert(pos &lt;= _size);
			if (_size + 1 &gt; _capacity)
			{
				reserve(_capacity * 2);
			}
			size_t end = _size + 1;
			while (end &gt; pos)
			{
				_str[end] = _str[end - 1];
				--end;
			}
			_str[pos] = ch;
			_size++;
			return *this;
		}

		string&amp; insert(size_t pos, const char* str)
		{
			assert(pos &lt;= _size);
			size_t len = strlen(str);
			if (_size + len &gt; _capacity)
			{
				reserve(_size + len);
			}
			size_t end = _size + len;
			while (end &gt; pos + len - 1)
			{
				_str[end] = _str[end - len];
				--end;
			}
			strncpy(_str + pos, str, len);
			_size += len;
			return *this;
		}

		string&amp; erase(size_t pos, size_t len = npos)
		{
			assert(pos &lt; _size);
			if (len &gt;= _size - pos)
			{
				_str[pos] = '\0';
			}
			else
			{
				strcpy(_str + pos, _str + pos + len);
			}
			_size -= len;
			return *this;
		}

		void swap(string&amp; s)
		{
			std::swap(_str, s._str);
			std::swap(_capacity, s._capacity);
			std::swap(_size, s._size);
		}

		void clear()
		{
			_str[0] = '\0';
			_size = 0;
		}

		size_t find(char ch, size_t pos = 0) const
		{
			assert(pos &lt; _size);
			for (size_t i = pos; i &lt; _size; ++i)
			{
				if (_str[i] == ch)
				{
					return i;
				}
			}
			return npos;
		}

		size_t find(const string&amp; s, size_t pos = 0) const
		{
			assert(pos &lt; _size);
			char* p = strstr(_str + pos, s._str);
			if (p == nullptr)
			{
				return npos;
			}
			return p - _str;
		}

		size_t find(const char* str, size_t pos = 0) const
		{
			assert(pos &lt; _size);
			char* p = strstr(_str + pos, str);
			if (p == nullptr)
			{
				return npos;
			}
			return p - _str;
		}

		string&amp; operator+=(const char ch)
		{
			push_back(ch);
			return *this;
		}

		string&amp; operator+=(const string&amp; s)
		{
			push_back(s._str);
			return *this;
		}

		string&amp; operator+=(const char* str)
		{
			push_back(str);
			return *this;
		}

		string&amp; operator=(const string&amp; s)
		{
			if (this != &amp;s)
			{
				char* tmp = new char[s._capacity + 1];
				strcpy(tmp, s._str);
				delete[] _str;
				_str = tmp;
				_size = s._size;
				_capacity = s._capacity;
			}
			return *this;
		}

		const char&amp; operator[](size_t pos) const
		{
			assert(pos &lt; _size);
			return _str[pos];
		}

		char&amp; operator[](size_t pos)
		{
			assert(pos &lt; _size);
			return _str[pos];
		}

		bool operator&gt;(const string&amp; s) const
		{			
			return strcmp(_str, s._str) &gt; 0;
		}

		bool operator==(const string&amp; s) const
		{
			return strcmp(_str, s._str) == 0;
		}

		bool operator&gt;=(const string&amp; s) const
		{
			return	*this &gt; s || *this == s;
		}

		bool operator&lt;(const string&amp; s) const
		{
			return	!(*this &gt;= s);
		}

		bool operator&lt;=(const string&amp; s) const
		{
			return	!(*this &gt; s);
		}

		bool operator!=(const string&amp; s) const
		{
			return	!(*this == s);
		}

		size_t size() const
		{
			return _size;
		}

		size_t capacity() const
		{
			return _capacity;
		}

		const char* c_str() const
		{
			return _str;
		}

		~string()
		{
			delete[] _str;
			_capacity = _size = 0;
		}

	private:
		char* _str;
		size_t _size;
		size_t _capacity;

		static const size_t npos;
	};

	const size_t string::npos = -1;

	ostream&amp; operator&lt;&lt;(ostream&amp; out, const string&amp; s)
	{
		for (auto ch : s)
		{
			out &lt;&lt; ch;
		}
		return out;
	}

	istream&amp; operator&gt;&gt;(istream&amp; in, string&amp; s)
	{
		s.clear();
		char ch = in.get();
		char buff[128];
		size_t i = 0;
		while (ch != ' ' &amp;&amp; ch != '\n')
		{
			buff[i++] = ch;
			if (i == 127)
			{
				buff[i] = '\0';
				s += buff;
				i = 0;
			}
			ch = in.get();
		}
		if (i != 0)
		{
			buff[i] = '\0';
			s += buff;
		}
		return in;
	}
}
```

如有错误，欢迎在评论区指出

完.
