# 原创
：  【web-攻击本地编译性应用程序】(11.3)格式化字符串漏洞

# 【web-攻击本地编译性应用程序】(11.3)格式化字符串漏洞

**目录**

[格式化字符串漏洞](#%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%BC%8F%E6%B4%9E)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、查找格式化字符串漏洞](#1.2%E3%80%81%E6%9F%A5%E6%89%BE%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%BC%8F%E6%B4%9E)

[简述：](#%E7%AE%80%E8%BF%B0%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

---


## 格式化字符串漏洞

> 
<h3>1.1、简介：</h3>
1、如果用户可控制的输入被当做格式化字符串参数提交给一个接受可能被滥用的格式说明符的函数（如C计言中的pcintf系列函数），就会产生格式化字符串漏洞，这些函数接受的参数数量不定，其中可能包含不同的数据类型，如数字和字符串，提交给函数的格式化字符串中包含的说明符告诉函数，变量参数中应包含何种数据，以及这些数据以什么格式表示

2、最危险的格式说明符为%n，这个说明符不会导致什么数据被打印。相反它使已经输出的字节数量被写入到以相关变量参数提交给函数的指针地址中

3、如果格式化字符串中的说明符比提交给函数的变量参数多，而函数又无法探查到这一点，那么它就会继续处理调用栈中的参数

4、如果攻击者能够控制提交给printf之类函数的全部或部分格式化字符串，就可以利用上述行为重写进程内存的重要部分，并最终执行任意代码。由于攻击者控制着格式化字符中，所以他能够控制函数输出的字节数量以及栈上被输入的字节数量重写的指针，这样攻击者就能够重写一个已保存的返回地址或者一个指向异常处理器的指针，进而控制代码执行，就像在栈溢出中一样


> 
<h3>1.2、查找格式化字符串漏洞</h3>
<h4>简述：</h4>
在远程应用程序中探查格式化字符串漏洞的最有效方法是，提交包含各种格式说明符的数据并监控应用程序的任何反常行为。与不受控制地触发缓冲区溢出漏洞可能造成的后果一样，在一个易受攻击的应用程序中探查格式化字符串漏洞可能会导致系统崩溃
<hr/>
<h4>过程：</h4>
1、轮流向每个目标参数提交包含大量格式化说明符%n与%s的字符串
基于安全考虑，一些格式化字符串操作可能会忽略%n说明符。相反提交%s说明符将会使函数废弃栈上的每一个参数，如果应用程序易于受到攻击，就可能会导致非法访问
2、Windows FormatMessage函数以一种不同的方式使用printf系列函数中的说明符。测试调用这个函数是否易于受到攻击
3、将%字符URL编码成%25
4、与查找缓冲区溢出漏洞时一样， 应该监控应用程序响应中出现的反常事件


#### 简述：
