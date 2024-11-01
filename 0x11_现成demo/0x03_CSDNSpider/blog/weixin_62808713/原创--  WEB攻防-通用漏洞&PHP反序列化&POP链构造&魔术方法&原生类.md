# 原创
：  WEB攻防-通用漏洞&PHP反序列化&POP链构造&魔术方法&原生类

# WEB攻防-通用漏洞&amp;PHP反序列化&amp;POP链构造&amp;魔术方法&amp;原生类

**目录**

[一、序列化和反序列化](#%E4%B8%80%E3%80%81%E5%BA%8F%E5%88%97%E5%8C%96%E5%92%8C%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96)

[二、为什么会出现反序列化漏洞](#%E4%BA%8C%E3%80%81%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BC%9A%E5%87%BA%E7%8E%B0%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%8F%E6%B4%9E)

[三、序列化和反序列化演示](#%E4%B8%89%E3%80%81%E5%BA%8F%E5%88%97%E5%8C%96%E5%92%8C%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E6%BC%94%E7%A4%BA)

[&lt;演示一&gt;](#%3C%E6%BC%94%E7%A4%BA%E4%B8%80%3E)

[&lt;演示二&gt;](#%3C%E6%BC%94%E7%A4%BA%E4%BA%8C%3E)

[&lt;演示二&gt;](#%3C%E6%BC%94%E7%A4%BA%E4%BA%8C%3E)

[四、漏洞出现演示](#%E5%9B%9B%E3%80%81%E6%BC%8F%E6%B4%9E%E5%87%BA%E7%8E%B0%E6%BC%94%E7%A4%BA)

[&lt;演示一&gt;](#%3C%E6%BC%94%E7%A4%BA%E4%B8%80%3E)

[&lt;演示二&gt;](#%3C%E6%BC%94%E7%A4%BA%E4%BA%8C%3E)

[四、ctfshow靶场真题实操](#%E5%9B%9B%E3%80%81ctfshow%E9%9D%B6%E5%9C%BA%E7%9C%9F%E9%A2%98%E5%AE%9E%E6%93%8D)

[&lt;真题一&gt;](#%3C%E7%9C%9F%E9%A2%98%E4%B8%80%3E)

[&lt;真题二&gt;](#%3C%E7%9C%9F%E9%A2%98%E4%BA%8C%3E)

[&lt;真题三&gt;](#%3C%E7%9C%9F%E9%A2%98%E4%B8%89%3E)

[&lt;真题四&gt;](#%3C%E7%9C%9F%E9%A2%98%E5%9B%9B%3E)

---


## 一、序列化和反序列化

        serialize()              //将一个对象转换成一个字符串

        unserialize()          //将字符串还原成一个对象

## 二、为什么会出现反序列化漏洞

        在php里有时会存在一些魔术方法，可以控制优先执行什么或者初始化什么，但是如果魔术方法使用不当，就可能会造成反序列化漏洞。

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

## 三、序列化和反序列化演示

### &lt;演示一&gt;

2.先将后两行注释掉，仅让其输出$s，可以看到其内容如下。

3.下面是对其序列化的内容的解释。

4. 将代码修改成下面的样式。

5.将$u输出出来如下图所示。

6.完整的解释如下图所示。

**        总结**：就是一种典型的数据传输方法，可以更好的保证代码的正确性和完整性。

### &lt;演示二&gt;

2.我们首先将代码更改成下面的样式。

 3.此时访问可以可到下面的返回结果。

4.这里我们仅仅创建了一个对象，就将下面的两个函数给调用了，从而输出了对应的内容。

        **总结**：无需函数，创建对象就会调用魔术方法。 

### &lt;演示二&gt;

 2.执行结果如下图所示。

3.我们将代码更改为下面的样式。

 4.将上面序列化后的代码使用参数上传上去。

 5.网页返回下面的结果。 

6.在代码里我们没有进行创建，但是仍然返回的end，是因为我们上传了序列化的内容，此时默认就进行了调用。

7.将代码再次更改。

8.此时再次执行可以发现test()被触发出来了。

         **总结**：传递序列化字符串，就相当于默认实现获取对象里的数据，包括调用里面的函数，也就是说即使不去创建对象，也能够触发对象里的变量以及函数，触发过程就是按照魔术方法的触发逻辑，

## 四、漏洞出现演示

### &lt;演示一&gt;

1.打开下面的代码。

2.创建一个对象，会先调用__construct，然后销毁调用__destruct。运行结果如下图所示。

3.更改代码然后执行，将序列化字符串输出出来然后复制。<img alt="" height="381" src="https://img-blog.csdnimg.cn/e30edadc3cf74781a6b3e83117b3b7a9.png" width="1066"/>

4.将代码更改成下图样式。

5.将序列化的代码当作参数进行上传，之后可以看到页面内依然返回了ipconfig执行结果。相当于此时没有创建对象，只是输入了序列化字符串，就默认调用了__destruct代码。

### &lt;演示二&gt;

1.打开下面的代码。

<img alt="" height="351" src="https://img-blog.csdnimg.cn/bddfb68d2c2145f4a9b3e5db3d934969.png" width="1014"/> 2.此时访问后，会先执行__construct，显示“xiaodisec”，然后回执行__destruct，执行系统命令ipconfig。 <img alt="" height="481" src="https://img-blog.csdnimg.cn/6e9bf3f0365f4b7e9774e618031e1a43.png" width="1200"/>

3.更改代码然后访问，来获取cc的序列化代码。

<img alt="" height="494" src="https://img-blog.csdnimg.cn/b4e5002ecab94d9880ebfb24a3712121.png" width="1200"/>4.将代码更改为下面的样式来接收序列化的代码c。

<img alt="" height="378" src="https://img-blog.csdnimg.cn/3fe3d33b177f4ae3a0f24ca1250475a7.png" width="1137"/>5.将序列化代码c当作参数提交，此时执行了__destruct，没有执行__construct，因为我们这里皆有进行“new”操作。

6.此时我们可以想到更改参数c的内容来执行一些其它的命令，下面进行尝试。

7.将参数里的ipconfig更改为“var”，然后将前面的长度改为“3”，执行后可以得到下面的返回结果，成功执行了“var”命令。

        **这里就是序列化漏洞的核心点，前面讲解的所有都是为这一步做准备！**

        **总结：在反序列化操作里，对象里设置好的一些变量也可以进行修改，这里就是将ipconfig修改成了ver。也就是说，有时只要创建对象，就会调用对象内的魔术方法；或者当类似于unserialize的这种函数出现时，即使没有创建对象，也可以通过控制输入的参数，去让它调用对象里的内容。**

**        这种漏洞一般出现在白盒里，在黑盒里要想发现几乎是不可能的，因为需要看到源代码对源代码的代码逻辑进行分析后才能分析到是否存在反序列化漏洞。**

## 四、ctfshow靶场真题实操

        **靶场地址：[ctf.show](https://ctf.show/)**

### &lt;真题一&gt;

1.找到对应题目进入靶场。 

2.打开靶场。

3.进入靶场。

4.分析代码后得到下面的解题思路：

5.继续分析代码：

 6.开始操作。

```
http://eaece883-4d1b-411b-989d-b09aae68b5df.challenge.ctf.show/?username=xxxxxx&amp;password=xxxxxx
```

7.成功得到了flag。

### &lt;真题二&gt;

1.找到对应题目进入靶场。 

 2.打开靶场。

3.进入靶场。

4.分析代码后可以想到进行下面的操作。

5.将POP链复制下来。

```
O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A8%3A%22password%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D
```

6.打开Hack Firefox访问靶场链接。

7.使用burp抓包。

8.将抓到的数据包发送到Repeater。 

9.根据源代码可以知道它接收的是cookie里的user数据，并且会检测username和password因此对数据包进行下面的修改。

<img alt="" height="987" src="https://img-blog.csdnimg.cn/b5342faaca1440c7a64ff5f763064cec.png" width="1200"/>10.放包后可以看到成功获取到了flag。

### &lt;真题三&gt;

1.找到对应题目进入靶场。 

 2.打开靶场。

 3.进入靶场。

4.分析代码后可以想到进行下面的操作。

 5.将POP链复制下来。

```
O%3A11%3A%22ctfShowUser%22%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A1%3A%22x%22%3Bs%3A8%3A%22password%22%3Bs%3A1%3A%22y%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3B%7D
```

6.打开Hack Firefox访问靶场链接。

7.使用burp抓包。

 8.将抓到的数据包发送到Repeater。 

9.根据源代码可以知道它接收的是cookie里的user数据，并且会检测username和password因此对数据包进行下面的修改，然后放包。

<img alt="" height="985" src="https://img-blog.csdnimg.cn/766a061bc59546f8a5514453bb771174.png" width="1200"/>10.可以看到成功获取到了flag。

### &lt;真题四&gt;

1.找到对应题目进入靶场。 

 2.打开靶场。

3.进入靶场。

4.这关里可以看到有多个class，因此我们就先要看哪个地方能获取到flag，但是我们并没有找到直接和flag相关的操作，但是我们在下面看到了函数eval。

**        补充： eval()函数可以把字符串按照php代码来执行。**

5.因为这里只可能eval会与flag相关，所以我们就判断谁会触发eval。

6.可以看到getInfo会触发eval，__destruct会触发getInfo，而__destruct触发时class='info'，当将'info'修改成backDoor后就可以调用到eval函数了。

7.复制class代码到在线工具内，然后将无用的代码删除后修改，之后执行。 

```
O%3A11%3A%22ctfShouUser%22%3A1%3A%7Bs%3A18%3A%22%00ctfShouUser%00class%22%3BO%3A8%3A%22backDoor%22%3A1%3A%7Bs%3A14%3A%22%00backDoor%00code%22%3Bs%3A17%3A%22system%28%22cat+f%2A%22%29%3B%22%3B%7D%7D
```

8.打开Hack Firefox访问靶场链接。<img alt="" height="1028" src="https://img-blog.csdnimg.cn/47521c509fbc4fdb8845150ecdeaf76d.png" width="1200"/>

9.使用burp抓包。

 10.将抓到的数据包发送到Repeater。  

9.对数据包进行下面的修改然后放包，可以得到flag。

<img alt="" height="694" src="https://img-blog.csdnimg.cn/07b6a4a6251245989f19af0b3a6c26e0.png" width="1077"/>10.成功获取到了flag。
