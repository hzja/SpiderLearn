# 原创
：  20-3 xss-labs（6-9）

# 20-3 xss-labs（6-9）

#### level6：[欢迎来到level6](http://127.0.0.1/xss-labs-master/level6.php?keyword=break%20it%20out!)

老规矩还是先看看输入框的闭合情况 

尝试事件函数绕过

```
test" onclick="alert('欢迎来钓鱼')
```

既然事件函数被转义了，那就使用我们第二关用过的绕过方法插入标签看看

```
test"&gt;&lt;script&gt;alert('欢迎来钓鱼')&lt;/script&gt;//
```

按照之前讲的第五关绕过思路，使用a标签触发al
