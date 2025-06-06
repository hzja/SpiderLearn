# 原创
：  【C++】继承

# 【C++】继承

[一、继承的概念与定义](#%E4%B8%80%E3%80%81%E7%BB%A7%E6%89%BF%E7%9A%84%E6%A6%82%E5%BF%B5%E4%B8%8E%E5%AE%9A%E4%B9%89)

[1.1 继承的概念](#1.1%20%E7%BB%A7%E6%89%BF%E7%9A%84%E6%A6%82%E5%BF%B5)

[1.2 继承的应用 ](#1.2%20%E7%BB%A7%E6%89%BF%E7%9A%84%E5%BA%94%E7%94%A8%C2%A0)

[1.3 继承的定义](#1.3%20%E7%BB%A7%E6%89%BF%E7%9A%84%E5%AE%9A%E4%B9%89)

[1.3.1 格式](#1.3.1%20%E6%A0%BC%E5%BC%8F)

[1.3.2 继承方式和访问限定符](#1.3.2%20%E7%BB%A7%E6%89%BF%E6%96%B9%E5%BC%8F%E5%92%8C%E8%AE%BF%E9%97%AE%E9%99%90%E5%AE%9A%E7%AC%A6)

[二、基类和派生类对象赋值转换](#%E4%BA%8C%E3%80%81%E5%9F%BA%E7%B1%BB%E5%92%8C%E6%B4%BE%E7%94%9F%E7%B1%BB%E5%AF%B9%E8%B1%A1%E8%B5%8B%E5%80%BC%E8%BD%AC%E6%8D%A2)

[三、继承中的作用域](#%E4%B8%89%E3%80%81%E7%BB%A7%E6%89%BF%E4%B8%AD%E7%9A%84%E4%BD%9C%E7%94%A8%E5%9F%9F)

[四、派生类的默认成员函数](#%E5%9B%9B%E3%80%81%E6%B4%BE%E7%94%9F%E7%B1%BB%E7%9A%84%E9%BB%98%E8%AE%A4%E6%88%90%E5%91%98%E5%87%BD%E6%95%B0)

[五、继承与友元](#%E4%BA%94%E3%80%81%E7%BB%A7%E6%89%BF%E4%B8%8E%E5%8F%8B%E5%85%83)

[六、继承与静态成员](#%E5%85%AD%E3%80%81%E7%BB%A7%E6%89%BF%E4%B8%8E%E9%9D%99%E6%80%81%E6%88%90%E5%91%98)

[七、菱形继承与虚继承](#%E4%B8%83%E3%80%81%E8%8F%B1%E5%BD%A2%E7%BB%A7%E6%89%BF%E4%B8%8E%E8%99%9A%E7%BB%A7%E6%89%BF)

[7.1 继承的不同种类 ](#7.1%20%E7%BB%A7%E6%89%BF%E7%9A%84%E4%B8%8D%E5%90%8C%E7%A7%8D%E7%B1%BB%C2%A0)

[7.2 虚继承](#7.2%20%E8%99%9A%E7%BB%A7%E6%89%BF)

[7.3 虚继承的原理](#7.3%20%E8%99%9A%E7%BB%A7%E6%89%BF%E7%9A%84%E5%8E%9F%E7%90%86)

[八、has-a和is-a](#%E5%85%AB%E3%80%81has-a%E5%92%8Cis-a)

---


## 一、继承的概念与定义

### 1.1 继承的概念

> 
继承（inheritance）是面向对象编程中的重要概念，它允许我们创建一个新的派生类，并**从现有的基类中继承成员和特性**。


从生物层面来说，孩子会继承父母的一些特点

从代码层面来说，派生类会继承基类的成员

继承允许我们根据以一个已有类为基础来设计出一个新的类，能够提高代码的可维护性和复用性。

这个已有类被称为基类（父类），新的类被称为派生类（子类）

### 1.2 继承的应用 

例如我们有一个学生类和一个老师类，他们都属于人类，有自己的姓名、电话、性别等基本信息

但是学生有自己的私有信息学号，老师有自己的私有信息工号 

如果我们把这些基本信息在学生类和老师类中都定义一次，就会出现重复的代码，代码复用性低

因此我们可以定义一个Person类，在这个类中定义基本信息，并将其作为基类去创建新的派生类Student和Teacher，例如：

```
class Person //基类
{
public:
	void Print()
	{
		cout &lt;&lt; "Print()" &lt;&lt; endl;
	}
protected:
	string _name; //姓名
	int _age; //年龄
};

class Student : public Person //派生类
{
protected:
	int _stuid; //学号
};

class Teacher : public Person //派生类
{
protected:
	int _jobid; //工号
};
```

像这样，Student类和Teacher类就继承了Person类中的成员，虽然派生类中没有明确的去定义，但是继承来的成员本身就是自身的一部分了

例如我们可以用派生类去调用基类的方法：

### 1.3 继承的定义

#### 1.3.1 格式

通过上面的例子，我们已经可以大概了解到如何去定义继承了

通过在派生类的类名后加上冒号、继承方式和基类名，就可以完成继承的定义。

#### 1.3.2 继承方式和访问限定符

访问限定符分为public访问、protected访问和private访问，而继承方式也分为**public继承、protected继承和private继承**

类成员的访问限制和类的继承方式都会影响最终继承下来的成员的权限大小，具体变化如下：
|**类成员/继承方式**|**public继承**|**protected继承**|**private继承**
|**基类的public成员**|派生类的public成员|派生类的protected成员|派生类的private成员
|**基类的protected成员**|派生类的protected成员|派生类的protected成员|派生类的private成员
|**基类的private成员**|在派生类中不可见|在派生类中不可见|在派生类中不可见

从该表中可以看出，派生类中继承的成员的权限是由**基类成员的权限和继承方式中较小的那个**决定的。

例如基类中的成员如果是public限定，但继承方式是private，那么最终继承到派生类中的成员，权限就是private。

而**基类private成员无论以什么继承方式，在派生类中都是不可见的**。此处的不可见并不代表没有继承，而是即使继承到了派生类中，但是语法上限制了派生类对象**无论在类内还是类外都无法直接访问**到继承的基类private成员，但是可以通过调用基类的公有或保护成员来访问。

如果我们想让继承下来的成员**不能在类外被访问，但是能在派生类中被访问**，此时就应该使用**protected访问限定符**。从这点我们可以看出protected访问限定符是为了继承而生的。

可以看到，用基类中protected限制的两个成员就只能在派生类中访问，而不能在类外访问了。

实际使用中我们一般都用public继承，很少并且也不提倡使用protected/private继承，因为这两种继承方式继承下来的成员都只能在派生类中使用，实际中扩展维护性较弱。

---


## 二、基类和派生类对象赋值转换

派生类其实就是在基类的基础上再添加一些成员，那么二者能否互相赋值转换呢？

派生类对象是可以赋值给基类的对象/指针/引用的，这种操作叫做切片（切割），我们可以看上面的图来帮助理解：Student类赋值给Person类就像把多出来的部分给切掉

在公有继承类中，子类对象被认为是一个特殊的父类对象。 

当派生类对象赋值给基类的指针或引用时，该指针/引用实际上还是指向派生类中的一部分

基类对象则不能赋值给派生类对象。

不过，我们可以通过强制类型转换将基类的指针或者引用赋值给派生类的指针或者引用，这里不作深入了解。

---


## 三、继承中的作用域

在继承体系中，子类和父类都有着独立的作用域。

如果此时子类和父类中出现了同名成员，在子类中将屏蔽对父类同名成员的直接访问，这种情况叫做**隐藏或重定义**，例如：

此时子类和父类中的成员_id同名，构成隐藏，因此如果我们直接访问的话只会访问到子类的_id，如果想要访问父类的_id则需要添加作用域限定符

像这样，子类和父类中的func构成隐藏，而不是重载，因为不在同一个作用域

---


## 四、派生类的默认成员函数

派生类是在基类的基础上形成的一个类，那么在派生类中的默认成员函数是如何工作的呢？

**特别注意：派生类对象的初始化先调用基类再调用派生类，而析构清理先调用派生类再调基类**

在后面要学到的多态中，某些场景下析构函数需要构成重写，编译器会将析构函数名改成destructor()，因此当我们不使用虚继承的情况下，子类的析构函数与父类的析构函数构成隐藏。

虚继承的内容我们后面会讲到

---


## 五、继承与友元

在继承体系中友元关系无法继承，所以基类的友元无法访问派生类的私有和保护成员

例如：

---


## 六、继承与静态成员

在基类中定义一个static静态成员，则在整个继承体系中，无论派生出多少个子类，**该静态成员是唯一的**。

例如：

可以看到，通过子类对该静态成员进行修改，会对整个继承体系产生影响

---


## 七、菱形继承与虚继承

### 7.1 继承的不同种类 

继承分为三种情况：

但是菱形继承有两个致命的缺点：**数据冗余和二义性**

使用菱形继承，此时如果想访问_name这个成员就会产生歧义：你要访问的是哪个_name？

如果显式指定目标的话可以解决该问题，但是依旧无法解决数据冗余的问题。

因此在C++3.0中引入了**虚继承**，算是解决了菱形继承的二义性和数据冗余的问题

### 7.2 虚继承

导致菱形继承产生二义性和数据冗余问题的原因在于，Student类和Teacher类同时是Person类的子类，它们继承了同样的成员

因此在Student类和Teacher类继承Person类时使用虚拟继承，就可以解决问题

如何使用虚拟继承：在继承方式前面加上 virtual 即可

例如：

那么问题来了：虚继承是如何解决菱形继承的数据冗余和二义性的呢？

### 7.3 虚继承的原理

为了研究虚继承的原理，我们首先要创建一个简单的不包含虚继承的菱形继承体系，例如：

```
class A
{
public:
	int _a;
};

class B : public A
{
public:
	int _b;
};

class C : public A
{
public:
	int _c;
};

class D : public B, public C
{
public:
	int _d;
};
```

它们的关系如下：

我们创建一个D类对象，并修改其成员，数值可以随便给

```
int main()
{
	D d;
	d.B::_a = 1;
	d.C::_a = 2;
	d._b = 3;
	d._c = 4;
	d._d = 5;
	return 0;
}
```

运行程序，通过内存窗口我们就可以清晰的看到它的结构

现在我们使用虚继承，再进行观察

可以看到，此时在d的地址处发生了一些变化，B、C和D的位置都不变，但是原本属于A的位置变成了两个类似地址的东西，并且最下面的2看起来应该是A。

通过这些我们可以分析出，在虚继承中把数据冗余的部分给去掉了，此时的A同时属于B和C，并且放到了最下面。 但是B和C如何去找到这个公共的A呢？

我们在内存窗口中输入这两个地址，就会发现两个16进制数字

细心的人可能已经发现了，B和C中存放的两个指针，指向了两个**虚基表**，通过虚基表中存放的偏移量就可以找到下面的A

因此这两个指针也叫做虚基表指针

---


## 八、has-a和is-a

继承关系通常被描述成is-a（是一个）关系，即派生类是基类的一种类型

组合是一种has-a（有一个）关系，也就是一个对象内部有另一个对象

组合和继承都是一种提高代码复用性的方式，但在继承中基类的内部细节对子类可见，一定程度上破坏了基类的封装，如果基类改变，派生类也会跟着改变，派生类与基类的耦合度高；而组合关系中对象之间的内部细节是不可视的，是一种黑箱复用，因此组合间没有很强的关联，耦合度低，利于保持封装。

但不意味着我们就要一味的选择组合，实际运用中灵活选择合适的方式即可。

完.
