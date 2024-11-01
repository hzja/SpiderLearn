# 原创
：  PHP反序列化&魔术方法详细解析及实例&公私有属性对比

# PHP反序列化&amp;魔术方法详细解析及实例&amp;公私有属性对比

**目录**

[一、魔术方法利用点分析](#%E4%B8%80%E3%80%81%E5%BA%8F%E5%88%97%E5%8C%96%E5%92%8C%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96)

[&lt;__construct&amp;__destruct&gt;](#%3C__construct%28%29%26__destruct%28%29%3E)

[&lt;__toString&gt;](#%3C__toString%3E)

[&lt;__call&gt;](#%3C__call%3E)

[&lt;__get&gt;](#%3C__get%3E)

[ &lt;__set&gt;](#%C2%A0%3C__set%3E)

[&lt;__sleep&gt;](#%3C__sleep%3E)

[&lt;__wakeup&gt;](#%3C__wakeup%3E)

[&lt;__isset&gt;](#%3C__isset%3E)

[&lt;__unset&gt;](#%3C__unset%3E)

[&lt;__invoke&gt;](#%3C__invoke%3E)

[&lt;总结&gt;](#%3C%E6%80%BB%E7%BB%93%3E)

[二、对象变量属性及序列化数据显示](#%E4%BA%8C%E3%80%81%E5%AF%B9%E8%B1%A1%E5%8F%98%E9%87%8F%E5%B1%9E%E6%80%A7)

[对象变量属性](#%E5%AF%B9%E8%B1%A1%E5%8F%98%E9%87%8F%E5%B1%9E%E6%80%A7)

[序列化数据显示](#%E5%BA%8F%E5%88%97%E5%8C%96%E6%95%B0%E6%8D%AE%E6%98%BE%E7%A4%BA)

[演示](#%E6%BC%94%E7%A4%BA)

[三、反序列化利用的分类](#%E4%B8%89%E3%80%81%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E5%88%A9%E7%94%A8%E7%9A%84%E5%88%86%E7%B1%BB)

---


## 一、魔术方法利用点分析

### &lt;__construct&amp;__destruct&gt;

```
__construct()     //构造函数，当对象 new 的时候会自动调用
__destruct()      //析构函数当对象被销毁时会被自动调用
```

1.实验代码部分如下。

2.将代码执行后可以看到下面的执行结果。

### &lt;__toString&gt;

```
__toString()        //在对象当做字符串的时候会被调用
```

1.实验代码部分如下。

 2.将代码执行后可以看到下面的执行结果。

### &lt;__call&gt;

```
__call()     //在对象上下文中调用不可访问的方法时触发
```

1.实验代码部分如下。

 2.将代码执行后可以看到下面的执行结果。

 <img alt="" height="281" src="https://img-blog.csdnimg.cn/de7dc414a18242f8ae85f608e329c83e.png" width="602"/>

### &lt;__get&gt;

```
__get()     //用于从不可访问的属性读取数据
```

1.实验代码部分如下。

 2.将代码执行后可以看到下面的执行结果。

 <img alt="" height="260" src="https://img-blog.csdnimg.cn/5263aa9ad0034a4f9d4daf80dccfefdd.png" width="604"/>

###  &lt;__set&gt;

```
__set()     //用于将数据写入不可访问的属性
```

1.实验代码部分如下。

 2.将代码执行后可以看到下面的执行结果。

### &lt;__sleep&gt;

```
__sleep()     //serialize之前被调用，可以指定要序列化的对象属性
```

1.实验代码部分如下。

 2.将代码执行后可以看到下面的执行结果。

 <img alt="" height="235" src="https://img-blog.csdnimg.cn/6954f7a0514443d38c9e9f92ee272db1.png" width="604"/>

### &lt;__wakeup&gt;

```
__wakeup()       //unserialize()时会被自动调用
```

1.实验代码部分如下。

 2.将代码执行后可以看到下面的执行结果。

 <img alt="" height="257" src="https://img-blog.csdnimg.cn/b5d1eb8497644fcba501f9a817d838df.png" width="696"/>

### &lt;__isset&gt;

```
__isset()     //检测对象的某个属性是否存在时执行此函数
```

1.实验代码部分如下。

 2.将代码执行后可以看到下面的执行结果。

 <img alt="" height="217" src="https://img-blog.csdnimg.cn/8f78dd1964f24408b893422c81974791.png" width="599"/>

### &lt;__unset&gt;

```
__unset()     //在不可访问的属性上使用unset()时触发，销毁对象的某个属性时执行此函数
```

1.实验代码部分如下。

 2.将代码执行后可以看到下面的执行结果。

 <img alt="" height="220" src="https://img-blog.csdnimg.cn/bc0409b0df5f485ebffe82160bd61cad.png" width="474"/>

### &lt;__invoke&gt;

```
__invoke()     //将对象当做函数来使用时执行此方法，通常不推荐这样做
```

1.实验代码部分如下。

 2.将代码执行后可以看到下面的执行结果。 

### **&lt;总结&gt;**

```
触发：unserialize 函数的变量可控，文件中存在可利用的类，类中有魔术方法：
__construct():     //构造函数，当对象 new 的时候会自动调用
__destruct()：    //析构函数当对象被销毁时会被自动调用
__wakeup():     //unserialize()时会被自动调用
__invoke():     //当尝试以调用函数的方法调用一个对象时，会被自动调用
__call():     //在对象上下文中调用不可访问的方法时触发
__callStatci():     //在静态上下文中调用不可访问的方法时触发
__get():     //用于从不可访问的属性读取数据
__set():     //用于将数据写入不可访问的属性
__isset():     //在不可访问的属性上调用 isset()或 empty()触发
__unset():     //在不可访问的属性上使用 unset()时触发
__toString():     //把类当作字符串使用时触发
__sleep():     //serialize()函数会检查类中是否存在一个魔术方法__sleep()，如果存在，该方法会被优先调用
```

## 二、对象变量属性及序列化数据显示

### 对象变量属性

### 序列化数据显示

### 演示

## 三、反序列化利用的分类
