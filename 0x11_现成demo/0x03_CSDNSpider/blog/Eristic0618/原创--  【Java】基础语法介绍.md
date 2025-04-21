# 原创
：  【Java】基础语法介绍

# 【Java】基础语法介绍

**目录**

[一、注释](#%E4%B8%80%E3%80%81%E6%B3%A8%E9%87%8A)

[二、标识符与关键字](#%E4%BA%8C%E3%80%81%E6%A0%87%E8%AF%86%E7%AC%A6%E4%B8%8E%E5%85%B3%E9%94%AE%E5%AD%97)

[三、输入和输出](#%E4%B8%89%E3%80%81%E8%BE%93%E5%85%A5%E5%92%8C%E8%BE%93%E5%87%BA)

[3.1 输出](#3.1%20%E8%BE%93%E5%87%BA)

[3.2 输入](#3.2%20%E8%BE%93%E5%85%A5)

[四、数据类型](#%E5%9B%9B%E3%80%81%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)

[3.1 基本数据类型](#3.1%20%E5%9F%BA%E6%9C%AC%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)

[3.2 引用数据类型](#3.2%20%E5%BC%95%E7%94%A8%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)

[3.3 var关键字](#3.3%20var%E5%85%B3%E9%94%AE%E5%AD%97)

[五、运算符](#%E4%BA%94%E3%80%81%E8%BF%90%E7%AE%97%E7%AC%A6)

[六、分支和循环](#%E5%85%AD%E3%80%81%E5%88%86%E6%94%AF%E5%92%8C%E5%BE%AA%E7%8E%AF)

[5.1 分支](#5.1%20%E5%88%86%E6%94%AF)

[5.2 循环](#5.2%20%E5%BE%AA%E7%8E%AF)

[七、类和对象](#%E4%B8%83%E3%80%81%E7%B1%BB%E5%92%8C%E5%AF%B9%E8%B1%A1)

[6.1 类的定义与对象的创建](#6.1%20%E7%B1%BB%E7%9A%84%E5%AE%9A%E4%B9%89%E4%B8%8E%E5%AF%B9%E8%B1%A1%E7%9A%84%E5%88%9B%E5%BB%BA)

[6.2 空对象](#6.2%20%E7%A9%BA%E5%AF%B9%E8%B1%A1)

[6.3 类的属性](#6.3%20%E7%B1%BB%E7%9A%84%E5%B1%9E%E6%80%A7)

[6.4 类的方法](#6.4%20%E7%B1%BB%E7%9A%84%E6%96%B9%E6%B3%95)

[6.5 静态](#6.5%20%E9%9D%99%E6%80%81)

[（1）静态属性和静态方法](#%EF%BC%881%EF%BC%89%E9%9D%99%E6%80%81%E5%B1%9E%E6%80%A7%E5%92%8C%E9%9D%99%E6%80%81%E6%96%B9%E6%B3%95)

[（2）静态代码块](#%EF%BC%882%EF%BC%89%E9%9D%99%E6%80%81%E4%BB%A3%E7%A0%81%E5%9D%97)

[6.6 继承](#6.6%20%E7%BB%A7%E6%89%BF)

[6.7 包和import](#6.7%20%E5%8C%85%E5%92%8Cimport)

[6.8 访问权限修饰符](#6.8%20%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90%E4%BF%AE%E9%A5%B0%E7%AC%A6)

[6.9 内部类](#6.9%20%E5%86%85%E9%83%A8%E7%B1%BB)

[6.10 抽象类和抽象方法](#6.10%20%E6%8A%BD%E8%B1%A1%E7%B1%BB%E5%92%8C%E6%8A%BD%E8%B1%A1%E6%96%B9%E6%B3%95)

[6.11 枚举](#6.11%20%E6%9E%9A%E4%B8%BE)

[6.12 匿名类](#6.12%20%E5%8C%BF%E5%90%8D%E7%B1%BB)

[八、final ](#%E5%85%AB%E3%80%81final%C2%A0)

[九、接口](#%E4%B9%9D%E3%80%81%E6%8E%A5%E5%8F%A3)

[十、数组](#%E5%8D%81%E3%80%81%E6%95%B0%E7%BB%84)

[9.1 定义](#9.1%20%E5%AE%9A%E4%B9%89)

[9.2 常用属性和方法](#9.2%20%E5%B8%B8%E7%94%A8%E5%B1%9E%E6%80%A7%E5%92%8C%E6%96%B9%E6%B3%95)

---


> 
提示：本文适合已经有编程基础的读者阅读，仅罗列Java中的语法，不对基础概念作讲解


## 一、注释

Java的注释和C/C++一样

单行注释：以//开头，例如

```
// 这是单行注释
```

多行注释：

```
/*
这是多行注释
*/
```

---


## 二、标识符与关键字

**标识符**，即**变量、方法、对象等的名字**，由用户自己定义

**关键字**，又称为保留字，是一个计算机语言中的预定义保留标识符

截止至Java17，已有67个关键字，它们分别是：
|abstract|continue|for|new|switch|assert|default
|if|package|synchronized|boolean|do|goto|private
|this|break|double|implements|protected|throw|byte
|else|import|public|throws|case|enum|instanceof
|return|transient|catch|extends|int|short|try
|char|final|interface|static|void|class|finally
|long|strictfp|volatile|const|float|native|super
|while|_ **(underscore)**|exports|opens|requires|uses|module
|permits|sealed|var|non-sealed|provides|to|with
|open|record|transitive|yield

---


## 三、输入和输出

### 3.1 输出

**System.out.print()**：不换行输出

**System.out.println()**：换行输出

### 3.2 输入

Java的输入可以通过创建Scanner对象，调用对象方法实现

```
Scanner scanner = new Scanner(System.in);
```

**（1）next()**：读取内容，以空格为分隔符

**（2）nextLine()**：一次读取一行内容

**（3）nextInt()**：读取一个整型

**（4）nextFloat()**：读取一个浮点数

剩余方法可自行阅读文档

---


## 四、数据类型

### 3.1 基本数据类型

基本数据类型都存储在**栈**中 

**（1）整数类型**：byte、short、int、long（按存储范围排序）

其中存储范围小的类型可以通过隐式类型转换赋值给范围更大的类型，但范围大的类型只能通过强制类型转换才能赋值给范围小的类型

**（2）浮点类型**：float、double

需要注意，在用小数给float类型的变量进行初始化时，由于带小数点的数据会被认为是双精度浮点数，所以会造成类型不匹配，此时需要在小数后加上f或F，例如：

**（3）字符类型**：char

**（4）布尔类型**：boolean

### 3.2 引用数据类型

引用数据类型都存储在**堆**中

**（1）类**

我们定义字符串使用的String，或者其他的类，例如Object等

**（2）接口**

**（3）数组**

### 3.3 var关键字

类似C++的auto关键字，var可以让我们在定义变量时不用显式指定变量的类型

```
var a = 1;
var b = 1.1;
var c = "hello";
var d = false;
```

---


## 五、运算符

Java的运算符用法和C/C++一样

**运算符**就是**参与运算的符号**，由Java提供。运算符与数据组合形成的代码称为**表达式**。

**（1）二元运算符**：+、-、*、/、%

二元运算符需要两个数据参与运算

需要注意的是，在二元运算中表达式的结果取决于类型范围最大的那个，且类型最小为int

也就是说，如果两个byte类型的数据进行运算，由于运算的类型最小为int，所以其结果不是byte类型而是int类型，所以无法赋值给byte的变量，需要进行强制类型转换

**（2）一元运算符**：++、--

**（3）赋值运算符**：=、+=、-=、*=、/=、%=

**（4）关系运算符**：==、!=、&gt;、&gt;=、 &lt;、&lt;=

**（5）逻辑运算符**：&amp;、|、^、!、&amp;&amp;、||

**（6）三元运算符**：exp1 ？ exp2 ： exp3

---


## 六、分支和循环

Java的分支和循环语法也与C/C++相同，这里不作过多赘述

### 5.1 分支

（1）if分支：if、else、else if

```
if(表达式){
            
}
else if(表达式){
            
}
else{
            
}
```

（2）switch分支：switch、case、default、break

```
switch(标识符){
    case 常量1:
        ...
        break;
    case 常量2:
        ...
        break;
    ...
    default:
        ...
}
```

### 5.2 循环

（1）while循环

```
while(表达式){
    ...
}
```

（2）do while循环

```
do{
    ...
}while(表达式);
```

（3）for循环

```
for(初始化表达式; 条件表达式; 更新表达式){
    ...
}
```

---


## 七、类和对象

### 6.1 类的定义与对象的创建

类的定义： 

```
class 类名{
    ...
}
```

不同于C++，Java在创建类时大括号后面不需要跟分号

对象的创建：

```
类名 对象名 = new 类名();
```

### 6.2 空对象

例如：

```
String s = null;
```

当我们暂时不想给一个变量创建空间时，可以使用空对象null，表示这个变量只被声明但未创建对象

### 6.3 类的属性

在类内定义类的属性和平时定义变量的方式一致，我们在定义类的属性时可以选择只声明，也可以选择声明的同时进行初始化

```
class Person1
{
    String name;
}

class Person2
{
    String name = "Peter";
}

```

与平时定义变量不同的是，变量在使用前必须初始化，但类的属性即使用户不进行初始化，也会被设置为默认值

其中整数类型会被默认初始化为0，浮点类型为0.0，布尔类型为false，字符类型为'\u0000'，引用数据类型为null

### 6.4 类的方法

在类内定义类的方法和平时定义函数的方式一致，且Java中定义函数的语法和C/C++的大致相同，这里不再介绍

例如：

```
public class test {
    public static void main(String[] args) {
        Person p = new Person();
        String name = "zhangsan";
        p.Who(name);
    }
}
class Person {
    void Who(String name) {
        System.out.println(name);
    }
}
```

像这样，我们就在Person类中定义了一个Who方法，且在main函数中创建了一个Person类对象并调用了Who方法

当参数的数量不确定时，可采用Java的可变参数，方式为参数类型后加省略号

### 6.5 静态

#### （1）静态属性和静态方法

与对象无关，只和类有关的属性和方法可以用**static**声明为静态，例如：

```
class Person 
{
    String name1;
    static String name2; //静态属性

    void test1() 
    {
        System.out.println("void test1()");
    }
    static void test2() //静态方法
    {
        System.out.println("static void test2()");
    }
}
```

可以在成员方法中调用静态方法或静态属性，但不能在静态方法中调用成员方法和成员属性

#### （2）静态代码块

我们可以在类中只使用static和大括号，定义一个静态代码块：

静态代码块在类的信息加载完后就会被自动调用，因此一个类的静态代码块只会被调用一次，即使我们创建了多个类对象

去掉static后，静态代码块失去了静态属性，在每次创建类对象时都会被调用：

### 6.6 继承

Java的继承通过**extends关键字**实现，例如：

```
class Parent
{
    //...
}
class child extends Parent
{
    //...
}
```

另外，如果子类中定义了和父类中同名的成员属性，也会导致覆盖

可以用super和this关键字来分别访问父类和子类的同名属性，例如：

Java的类无法同时继承多个父类

### 6.7 包和import

**包（package）**用于更好的组织类。可以把功能相似或相关的类或接口组织在同一个包中，方便查找和使用

例如我们使用的String类，就是包含在java.lang这个包里面的

一般我们在使用Java核心类库时基本都要在类的前面加上包名（java.lang除外，这个包是Java的核心包，一般JVM会自动给我们导入），例如：

```
java.util.Scanner scanner = new java.util.Scanner(System.in);
```

但是带着一长串包名太复杂了，因此我们也可以通过**import关键字**引入某个类：

```
import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
    }
}
```

有点类似于C++的using关键字

### 6.8 访问权限修饰符

需要注意，一份Java源码中**只能有一个公共外部类**，且必须与源码文件名相同

main方法也应该用public修饰，使得JVM在调用main方法时不用考虑权限问题

若一个成员变量或方法用private修饰，则只能够在类内调用，无法在类外被访问

Java不允许外部类使用private修饰

被protected修饰的成员变量或方法可在子类中被调用

Java也不允许外部类使用protected修饰

### 6.9 内部类

在类中声明的类——内部类

内部类可以当成是外部类的属性来使用

定义和使用：

```
public class test {
    public static void main(String[] args) {
        OutClass outer = new OutClass(); //创建一个外部类对象
        OutClass.InnerClass innerClass = outer.new InnerClass(); //创建一个内部类对象
    }
}

class OutClass{
    public class InnerClass{
        //...
    }
}
```

### 6.10 抽象类和抽象方法

只有声明而没有实现的方法称为抽象方法，用**abstract关键字**声明

但是会发现abstract下有红色波浪线，说明有错误

这是因为如果一个类含有抽象方法，那么这个类就是抽象类，而抽象方法只能在抽象类中声明：

但抽象类中不是一定只有抽象方法的，可以有普通的成员方法 

抽象类是无法直接构造对象的，因为抽象类是一个不完整的类。但抽象类可以被其他类继承，通过子类来间接构造对象

如果抽象类中含有抽象方法，那么子类在继承抽象类时必须重写抽象方法

### 6.11 枚举

在Java中，枚举是一个特殊的类，使用**enum关键字**声明

```
enum name{
    //...
}
```

枚举类无法在外部创建对象，将其对象在类内声明后会自行创建，例如：

```
enum City{
    BEIJING, SHANGHAI, GUANGZHOU, SHENZHEN
}
```

枚举类中可以自定义构造方法，来对内部的对象进行初始化。因为枚举会将对象放置在最前面，所以如果后面还有其他语法，则对象要和后面的语法用分号分开：

枚举类也是用普通的类实现的，所有的枚举值的属性为 public static final

### 6.12 匿名类

没有名字的类称为匿名类

当我们不关心类名、不想重复创建多个类时，我们可以通过匿名类来实现一个抽象类或接口

例如：

还可以这样用： 

像这样，我们直接在匿名类中实现了抽象类中的抽象方法，不需要提供额外的类名

匿名类除了可以用于实现抽象类，也可以对普通的类中的方法进行重写或实现某个接口

---


## 八、final 

Java中的**final关键字**，可以用于修饰变量使该变量无法被修改（对标C/C++的const）、禁止某个成员方法被子类重写或禁止某个类被继承。

C++中也有final，也可以用于禁止某个成员方法被子类重写或禁止某个类被继承。但不同的是Java把final放在方法和类之前，C++放在函数和类的最后

被final修饰的变量具有常性，**一旦初始化后无法被修改**

需要注意，final修饰成员属性后，JVM无法对该属性进行初始化，必须我们手动初始化

类内的final属性除了在声明的同时初始化，还可以在构造方法中进行初始化

和C/C++不同的是，Java中用final修饰的变量可以声明和初始化分离，例如：

但是C/C++中是不行的

除了用于修饰变量使变量具有常性，final还可修饰成员方法（除了构造方法），用于让其无法被子类重写

何为重写？即子类中继承了父类的方法声明，但对其内容进行了重写

final还可以让一个类无法被继承：

另外，final不能和abstract连用，因为如果一个抽象方法/抽象类被final修饰了，那么它就无法被子类重写/继承，也就无法实例化对象了

---


## 九、接口

接口是一个抽象类型，是**一系列抽象方法的集合**，用**interface关键字**来声明

```
interface interfaceName{
    //...
}
```

接口与类比较相似，但二者是不同的概念。接口因为包含了抽象方法，因此无法实例化对象

接口有以下特征：

接口内的每个方法会被隐式的指定为**public abstract**方法， 变量会被隐式指定为**public static final**变量

类实现接口需要用到**implements关键字**。当一个非抽象类实现了某个接口，这个类需要实现接口中的所有抽象方法

实例：

```
public class test {
    public static void main(String[] args) {
        powerBank p = new powerBank();
        iPhone ip1 = new iPhone();
        p.usb1 = ip1;
        iPhone ip2 = new iPhone();
        p.usb2 = ip2;
        p.powerSupply();
    }
}

interface USB{
}

interface USBdischarge extends USB{
    public void powerSupply();
}

interface USBcharge extends USB{
    public void powerReceive();
}

class powerBank implements USBdischarge{
    public USBcharge usb1;
    public USBcharge usb2;

    @Override
    public void powerSupply() {
        System.out.println("充电宝放电");
        usb1.powerReceive();
        usb2.powerReceive();
    }
}

class iPhone implements USBcharge{
    @Override
    public void powerReceive() {
        System.out.println("手机充电");
    }
}
```

运行结果：

一个类可以同时实现多个接口

---


## 十、数组

### 9.1 定义

一维数组的声明方式：类型[] 数组名

```
String[] names;
int[] arr;
```

一维数组的定义方式：类型[] 数组名 = new 类型[容量]

```
String[] names = new String[3];
//或者
int[] arr = {1, 2, 3, 4, 5};
```

二维数组的声明和定义方式：

```
int[][] arr = new int[5][3];
//或
int[][] arr = new int[5][];
arr[0] = new int[5];
arr[1] = new int[2];
arr[2] = new int[3];
arr[3] = new int[7];
arr[4] = new int[1];
//每个一维数组的长度不定
//或
int[][] arr = {{1, 2, 3}, {2, 3, 4},{3, 4, 5, 6}};
```

### 9.2 常用属性和方法

**（1）length**：返回数组的长度

**（2）Arrays.toString()**：将数组转成字符串

**（3）clone()**：将原数组复制一份并返回

**（4）equals()**：判断两个数组是否相等（是否指向同一个地址）

可以看到虽然arr1和arr2的值相同，但是它们没有指向同一个地址，所以为false

**（5）Arrays.fill()**：将数组所有元素赋值为指定值

**（6）Arrays.sort()**：将数组元素排序

**（7）Arrays.binarySearch()**：二分查找，返回下标

**（8）Arrays.copyOfRange()**： 拷贝目标数组的某个返回到指定数组中（范围前闭后开）

本文也是个人的学习笔记，如有错误，欢迎在评论区指出

完.
