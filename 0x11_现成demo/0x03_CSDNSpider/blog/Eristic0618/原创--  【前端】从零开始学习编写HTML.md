# 原创
：  【前端】从零开始学习编写HTML

# 【前端】从零开始学习编写HTML

**目录**

[一、什么是前端](#%E4%B8%80%E3%80%81%E4%BB%80%E4%B9%88%E6%98%AF%E5%89%8D%E7%AB%AF)

[二、什么是HTML](#%E4%BA%8C%E3%80%81%E4%BB%80%E4%B9%88%E6%98%AFHTML)

[三、HTML文件的基本结构](#%E4%B8%89%E3%80%81HTML%E6%96%87%E4%BB%B6%E7%9A%84%E5%9F%BA%E6%9C%AC%E7%BB%93%E6%9E%84)

[四、HTML常见标签](#%E5%9B%9B%E3%80%81HTML%E5%B8%B8%E8%A7%81%E6%A0%87%E7%AD%BE)

[4.1 注释标签](#4.1%20%E6%B3%A8%E9%87%8A%E6%A0%87%E7%AD%BE)

[4.2 标题标签](#4.2%20%E6%A0%87%E9%A2%98%E6%A0%87%E7%AD%BE)

[4.3 段落标签](#4.3%20%E6%AE%B5%E8%90%BD%E6%A0%87%E7%AD%BE)

[4.4 换行标签](#4.4%20%E6%8D%A2%E8%A1%8C%E6%A0%87%E7%AD%BE)

[4.5 格式化标签](#4.5%20%E6%A0%BC%E5%BC%8F%E5%8C%96%E6%A0%87%E7%AD%BE)

[4.6 图片标签](#4.6%20%E5%9B%BE%E7%89%87%E6%A0%87%E7%AD%BE)

[4.7 超链接标签](#4.7%20%E8%B6%85%E9%93%BE%E6%8E%A5%E6%A0%87%E7%AD%BE)

[4.8 表格标签](#4.8%20%E8%A1%A8%E6%A0%BC%E6%A0%87%E7%AD%BE)

[4.9 列表标签](#4.9%20%E5%88%97%E8%A1%A8%E6%A0%87%E7%AD%BE)

[4.10 表单标签](#4.10%20%E8%A1%A8%E5%8D%95%E6%A0%87%E7%AD%BE)

[（1）form标签](#%EF%BC%881%EF%BC%89form%E6%A0%87%E7%AD%BE)

[（2）input标签](#%EF%BC%882%EF%BC%89input%E6%A0%87%E7%AD%BE)

[（3）label标签](#%EF%BC%883%EF%BC%89label%E6%A0%87%E7%AD%BE)

[（4）select标签](#%EF%BC%884%EF%BC%89select%E6%A0%87%E7%AD%BE)

[（5）textarea标签](#%EF%BC%885%EF%BC%89textarea%E6%A0%87%E7%AD%BE)

[4.11 无语义标签](#4.11%20%E6%97%A0%E8%AF%AD%E4%B9%89%E6%A0%87%E7%AD%BE)

[五、实现简单的简历展示网页](#%E4%BA%94%E3%80%81%E5%AE%9E%E7%8E%B0%E7%AE%80%E5%8D%95%E7%9A%84%E7%AE%80%E5%8E%86%E5%B1%95%E7%A4%BA%E7%BD%91%E9%A1%B5)

[六、实现简单的简历填写页面](#%E5%85%AD%E3%80%81%E5%AE%9E%E7%8E%B0%E7%AE%80%E5%8D%95%E7%9A%84%E7%AE%80%E5%8E%86%E5%A1%AB%E5%86%99%E9%A1%B5%E9%9D%A2)

---


## 一、什么是前端

前端开发是**创建Web页面或APP等前端界面呈现给用户的过程**，负责把界面更好的呈现给用户

相对于后端主要负责用户看不见的数据处理，前端是指用户**可以看到和操作的部分**，例如网页页面，PC端程序页面或移动端APP页面。

 

---


## 二、什么是HTML

HTML（**H**yper**T**ext **M**arkup **L**anguage）是**超文本标记语言**的简称，是一种用于创建网页的标准标记语言。

 

---


## 三、HTML文档的基本结构

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        页面内容
    &lt;/body&gt;
&lt;/html&gt;
```

如上：

其中被尖括号包括的就是**HTML标签**，不同标签之间分为**父子关系**和**兄弟关系**

我们可以通过上面不同标签的缩进程度来观察它们的关系，例如head和body是html的子标签，title是head的子标签，head和body之间是兄弟关系

不同标签之间的结构关系就构成了一棵**DOM树**

 

---


## 四、HTML常见标签

HTML标签又分为**单标签**和**双标签**

单标签只会单独出现，用法：&lt;标签名/&gt;

双标签成对出现，用法：&lt;标签名&gt;&lt;/标签名&gt;

### 4.1 注释标签

```
&lt;!-- 我是注释 --&gt;
```

像这样，用尖括号、感叹号和横杠组成注释标签，其中填写自己需要的注释

注释不会显示在网页界面上，主要用于提高代码的可读性

 

### 4.2 标题标签

就像CSDN的富文本编辑器中提供了六级标题，HTML的标题标签也有六个，**从h1到h6逐级变小**

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h1&gt;这是一级标题&lt;/h1&gt;
        &lt;h2&gt;这是二级标题&lt;/h2&gt;
        &lt;h3&gt;这是三级标题&lt;/h3&gt;
        &lt;h4&gt;这是四级标题&lt;/h4&gt;
        &lt;h5&gt;这是五级标题&lt;/h5&gt;
        &lt;h6&gt;这是六级标题&lt;/h6&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

 

### 4.3 段落标签

我们在开发工具中编写HTML文档，将一长段文字分成多段，但是在网页中并不会显示分成多段的效果，仍然是一长段，例如：

在浏览器中运行：

在HTML中直接输入回车并不能真正的实现分段，而是相当于一个空格

如果我们要进行分段，需要用到**段落标签p**，具体用法如下：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;p&gt;1111111111111111111&lt;/p&gt;
        &lt;p&gt;2222222222222222222&lt;/p&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

再次运行：

会发现成功分成了两段，段落之间有一定的间隙

段落标签p是一个**双标签**，在开始标签和结束标签之间填写自己想要的内容

当然，标签不限制只能在同一行，像这样也是正确的用法：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;p&gt;
            1111111111111111111
        &lt;/p&gt;
        &lt;p&gt;
            2222222222222222222
        &lt;/p&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

 

### 4.4 换行标签

**换行标签br**是break的缩写，是一个单标签，规范写法是&lt;br/&gt;，不建议写成&lt;br&gt;

区别于段落标签p，用br标签只会进行分行，不会产生空隙

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        hello&lt;br/&gt;world
    &lt;/body&gt;
&lt;/html&gt;
```

在浏览器中运行：

 

### 4.5 格式化标签

HTML中还有一些标签可以改变字体格式：

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;strong&gt;加粗&lt;/strong&gt;
        &lt;b&gt;加粗&lt;/b&gt;
        &lt;em&gt;倾斜&lt;/em&gt;
        &lt;i&gt;倾斜&lt;/i&gt;
        &lt;del&gt;删除线&lt;/del&gt;
        &lt;s&gt;删除线&lt;/s&gt;
        &lt;ins&gt;下划线&lt;/ins&gt;
        &lt;u&gt;下划线&lt;/u&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

在浏览器中运行：

 

### 4.6 图片标签

要在网页中显示图片，就需要用到**图片标签img**

img标签中必须带有**src属性**，用于说明图片的路径，用法：&lt;img src="图片路径"&gt;

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;img src="html.png"&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

在浏览器中运行：

除了保存在本地的图片，网络路径也可以使用，例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;img src="https://tgi12.jia.com/114/936/14936926.jpg"&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

在浏览器中运行：

除了src属性，img标签还有其他属性：

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;img src="html.png" alt="HTML" title="这是HTML图标" width="1000px" border="2px"&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

属性之间不分先后顺序，按照键值对的格式表示

 

### 4.7 超链接标签

要实现在网页中跳转到其他地方，就需要**超链接标签a**

超链接标签也有必须具备的**属性href**，用来说明点击后要跳转到哪个页面

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;a href="https://www.baidu.com/"&gt;百度&lt;/a&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

在浏览器中运行：

点击蓝紫色带下划线的“百度”，就可以跳转到对应的页面

属性href的值有多种形式：

例如：

```
&lt;a href="#"&gt;空链接&lt;/a&gt;
```

例如：

```
&lt;a href="test.zip"&gt;下载文件&lt;/a&gt;
```

例如：

```
&lt;a href="https://www.baidu.com/"&gt;
    &lt;img src="baidu.png"&gt;
&lt;/a&gt;
```

点击该图片就会跳转到百度首页

例如：

```
&lt;a href="#one"&gt;第一章&lt;/a&gt;
&lt;a href="#two"&gt;第二章&lt;/a&gt;
&lt;p id="one"&gt;
    第一章内容
&lt;/p&gt;
&lt;p id="two"&gt;
    第二章内容
&lt;/p&gt;
```

 

### 4.8 表格标签

要在网页中显示一个表格，就需要使用**表格标签table**

table有一些**子标签**：

其中td和th又是tr的子标签

我们举一个例子：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;table&gt;
            &lt;tr&gt;
                &lt;th&gt;姓名&lt;/th&gt;
                &lt;th&gt;性别&lt;/th&gt;
                &lt;th&gt;年龄&lt;/th&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;张三&lt;/td&gt;
                &lt;td&gt;男&lt;/td&gt;
                &lt;td&gt;18&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;李四&lt;/td&gt;
                &lt;td&gt;男&lt;/td&gt;
                &lt;td&gt;19&lt;/td&gt;
            &lt;/tr&gt;
        &lt;/table&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

在浏览器中运行：

我们发现这个表格怎么没有边框？事实上，表格标签table包含一些属性，其中边框也是属性之一，需要进行设置

table的属性有：

实际设置中我们可能会发现表格的边框有两条线，这是因为单元格之间有距离，如果将cellspacing设置为0边框就变为了单线。大家可以自己设置一下看看

我们还可以对单元格标签td设置**合并单元格**：

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;table align="center" border="1" cellpadding="5" cellspacing="0" width="500px" height="500px"&gt;
            &lt;tr&gt;
                &lt;th&gt;姓名&lt;/th&gt;
                &lt;th&gt;性别&lt;/th&gt;
                &lt;th&gt;年龄&lt;/th&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;张三&lt;/td&gt;
                &lt;td rowspan="2"&gt;男&lt;/td&gt;
                &lt;td&gt;18&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;李四&lt;/td&gt;
                &lt;td&gt;19&lt;/td&gt;
            &lt;/tr&gt;
        &lt;/table&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

在浏览器中运行：

 

### 4.9 列表标签

列表标签又分为**有序列表、无序列表和自定义列表**：

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h3&gt;无序列表&lt;/h3&gt;
        &lt;ul&gt;
            &lt;li&gt;第一列&lt;/li&gt;
            &lt;li&gt;第二列&lt;/li&gt;
            &lt;li&gt;第三列&lt;/li&gt;
        &lt;/ul&gt;
        &lt;h3&gt;有序列表&lt;/h3&gt;
        &lt;ol&gt;
            &lt;li&gt;第一列&lt;/li&gt;
            &lt;li&gt;第二列&lt;/li&gt;
            &lt;li&gt;第三列&lt;/li&gt;
        &lt;/ol&gt;
        &lt;h3&gt;自定义列表&lt;/h3&gt;
        &lt;dl&gt;
            &lt;dt&gt;小标题&lt;/dt&gt;
            &lt;dd&gt;第一列&lt;/dd&gt;
            &lt;dd&gt;第二列&lt;/dd&gt;
            &lt;dd&gt;第三列&lt;/dd&gt;
        &lt;/dl&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

在浏览器中运行：

无序列表中，每一列前面的实心圆可以改成**方块**或**空心圆**。可以通过ul标签的**type属性**修改，默认值为**disc**（实心圆），还有**square**（实心方块）和**circle**（空心圆），例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h3&gt;无序列表&lt;/h3&gt;
        &lt;ul type="circle"&gt;
            &lt;li&gt;第一列&lt;/li&gt;
            &lt;li&gt;第二列&lt;/li&gt;
            &lt;li&gt;第三列&lt;/li&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

有序列表中每一列前面的数字也可以改成英文字母或罗马数字，也是通过修改ol标签的type属性。

有序序列还可以通过修改ol标签的start属性来改变列表起始的数字

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;h3&gt;有序列表&lt;/h3&gt;
        &lt;ol type="I" start="2"&gt;
            &lt;li&gt;第一列&lt;/li&gt;
            &lt;li&gt;第二列&lt;/li&gt;
            &lt;li&gt;第三列&lt;/li&gt;
        &lt;/ol&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

 

### 4.10 表单标签

要想让用户**通过页面输入信息**，就需要用到**表单标签**

#### （1）form标签

用于**创建表单**，将用户输入的数据提交到服务器

其中**action属性**负责定义表单数据提交的目标URL，**method属性**定义提交数据的HTTP方法

例如：

这里就涉及到一定的服务器和网络编程相关知识了

 

#### （2）input标签

用于创建各种**输入控件**，如文本框、按钮、单选框和复选框

input的**type属性**用于定义输入控件的类型，是**必须要显式定义的属性**

输入控件有：

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            输入姓名&lt;input type="text"&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            输入密码&lt;input type="password"&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            性别&lt;input type="radio" name="sex"&gt;男&lt;input type="radio" name="sex"&gt;女
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

**注意！**两个构成单选关系的单选框，name属性的值必须相同才可以实现多选一的效果

如果我们想让某个选项作为默认选择项，可以设置其checked属性，例如：

再次运行，此时男选项就被默认选择了

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            &lt;input type="checkbox"&gt;选项1&lt;input type="checkbox"&gt;选项2&lt;input type="checkbox"&gt;选项3
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            &lt;input type="button" value="点击"&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

当前我们写出的按钮点击后没有响应，需要搭配JS使用，例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            &lt;input type="button" value="点击" onclick="alert('hello')"&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            输入姓名&lt;input type="text" name="username"&gt;
            &lt;input type="submit" value="提交"&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

页面如下：

在文本框中输入zhangsan后点击提交：

此时输入的数据就作为参数提交给服务器了

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form action="1.html"&gt;
            输入姓名&lt;input type="text" name="username"&gt;
            &lt;input type="reset" value="清空"&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

在文本框中进行输入后点击清空按钮，即可清空输入的内容

例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            &lt;input type="file"&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

 

#### （3）label标签

搭配input标签使用，可以**与表单控件相关联**，当用户点击label标签的内容时，会自动将焦点跳到相关联的表单控件上，能够提高用户体验

例如我们想实现点击选框对应的文字就能选择该选项的功能：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            &lt;input type="radio" name="sex" id="male"&gt;
            &lt;label for="male"&gt;男&lt;/label&gt;
            &lt;input type="radio" name="sex" id="female"&gt;
            &lt;label for="female"&gt;女&lt;/label&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

此时即使我们不点击选框，点击"男"或"女"也可以实现选择的功能

注意：要将label和表单控件相关联，必须要**保证表单控件的id属性值和label标签的for属性值对应**

 

#### （4）select标签

select用于实现**下拉菜单**，其子标签option作为菜单的每一行，例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            &lt;select&gt;
                &lt;option&gt;北京&lt;/option&gt;
                &lt;option&gt;上海&lt;/option&gt;
                &lt;option&gt;广州&lt;/option&gt;
                &lt;option&gt;深圳&lt;/option&gt;
            &lt;/select&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

如果在option中定义**selected="selected"**则表示该选项默认选中，例如：

此时就会默认选中广州

 

#### （5）textarea标签

可以定义一个**多行的文本输入控件**，例如：

```
&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;页面标题&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt; 
        &lt;form&gt;
            &lt;textarea rows="5" cols="20"&gt;

            &lt;/textarea&gt;
        &lt;/form&gt;
    &lt;/body&gt;
&lt;/html&gt;
```

其中rows属性和cols属性表示一次能够显示几行几列

 

### 4.11 无语义标签

顾名思义，就是**没有语义的标签**，不需要考虑其内容，区别于前面的通过标签名就可以知道标签用途的语义化标签

无语义标签中有**div标签**和**span标签**：

这两个标签主要用于**网页布局**

 

---


## 五、实现简单的简历展示网页

接下来是练习时间，尝试根据前面的知识来实现下面的网页吧！

源码如下：

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;个人简历&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;某某某&lt;/h1&gt;
    &lt;div&gt;
        &lt;h2&gt;基本信息&lt;/h2&gt;
        &lt;img src="https://pic.616pic.com/ys_bnew_img/00/24/50/zLfQibcVrw.jpg" width="300px"&gt;
        &lt;p&gt;&lt;span&gt;求职意向：&lt;/span&gt;C++开发工程师&lt;/p&gt;
        &lt;p&gt;&lt;span&gt;联系电话：&lt;/span&gt;XXX-XXXX-XXXX&lt;/p&gt;
        &lt;p&gt;&lt;span&gt;邮箱：&lt;/span&gt;xxx@qq.com&lt;/p&gt;
        &lt;p&gt;&lt;a href="https://github.com/"&gt;我的 github&lt;/a&gt;&lt;/p&gt;
        &lt;p&gt;&lt;a href="https://blog.csdn.net/"&gt;我的 博客&lt;/a&gt;&lt;/p&gt;
    &lt;/div&gt;

    &lt;div&gt;
        &lt;h2&gt;教育背景&lt;/h2&gt;
        &lt;ol&gt;
            &lt;li&gt;xxx小学&lt;/li&gt;
            &lt;li&gt;xxx初中&lt;/li&gt;
            &lt;li&gt;xxx高中&lt;/li&gt;
            &lt;li&gt;xxx大学&lt;/li&gt;
        &lt;/ol&gt;
    &lt;/div&gt;

    &lt;div&gt;
        &lt;h2&gt;专业技能&lt;/h2&gt;
        &lt;ul&gt;
            &lt;li&gt;熟练掌握C++&lt;/li&gt;
            &lt;li&gt;能够实现并熟练运用常见数据结构&lt;/li&gt;
            &lt;li&gt;熟知计算机网络理论&lt;/li&gt;
            &lt;li&gt;掌握Web开发能力&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/div&gt;

    &lt;div&gt;
        &lt;h2&gt;我的项目&lt;/h2&gt;
        &lt;ol&gt;
            &lt;li&gt;&lt;h3&gt;树洞&lt;/h3&gt;&lt;/li&gt;
            &lt;p&gt;开发时间：xxxx-xxxx&lt;/p&gt;
            &lt;p&gt;功能介绍：&lt;/p&gt;
            &lt;ul&gt;
                &lt;li&gt;功能1&lt;/li&gt;
                &lt;li&gt;功能2&lt;/li&gt;
            &lt;/ul&gt;
            &lt;li&gt;&lt;h3&gt;个人博客网站&lt;/h3&gt;&lt;/li&gt;
            &lt;p&gt;开发时间：xxxx-xxxx&lt;/p&gt;
            &lt;p&gt;功能介绍：&lt;/p&gt;
            &lt;ul&gt;
                &lt;li&gt;功能1&lt;/li&gt;
                &lt;li&gt;功能2&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/ol&gt;    
    &lt;/div&gt;

    &lt;div&gt;
        &lt;h2&gt;个人评价&lt;/h2&gt;
        &lt;p&gt;在校期间学习优良，绩点名列前茅，多次获得奖学金&lt;/p&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

 

---


## 六、实现简单的简历填写页面

接下来是第二个练习，尝试根据前面的知识来实现下面的网页吧！

源码如下：

```
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;简历填写页面&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;table cellspacing="0" width="600px"&gt;
        &lt;thead&gt;&lt;h3&gt;请填写简历信息&lt;/h3&gt;&lt;/thead&gt;
        &lt;tbody&gt;
            &lt;tr&gt;
                &lt;td&gt;姓名&lt;/td&gt;
                &lt;td&gt;&lt;input type="text"&gt;&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;性别&lt;/td&gt;
                &lt;td&gt;
                    &lt;input type="radio" name="sex" id="male"&gt;
                    &lt;label for="male"&gt;男&lt;/label&gt;
                    &lt;input type="radio" name="sex" id="female"&gt;
                    &lt;label for="female"&gt;女&lt;/label&gt;
                &lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;出生年份&lt;/td&gt;
                &lt;td&gt;
                    &lt;select&gt;
                        &lt;option&gt;--请选择年份--&lt;/option&gt;
                        &lt;option&gt;--2000--&lt;/option&gt;
                        &lt;option&gt;--2001--&lt;/option&gt;
                        &lt;option&gt;--2002--&lt;/option&gt;
                        &lt;option&gt;--2003--&lt;/option&gt;
                        &lt;option&gt;--2004--&lt;/option&gt;
                        &lt;option&gt;--2005--&lt;/option&gt;
                    &lt;/select&gt;
                &lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;就读学校&lt;/td&gt;
                &lt;td&gt;&lt;input type="text"&gt;&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;应聘岗位&lt;/td&gt;
                &lt;td&gt;
                    &lt;input type="checkbox" id="fe"&gt;&lt;label for="fe"&gt;前端开发&lt;/label&gt;
                    &lt;input type="checkbox" id="be"&gt;&lt;label for="be"&gt;后端开发&lt;/label&gt;
                    &lt;input type="checkbox" id="qa"&gt;&lt;label for="qa"&gt;测试开发&lt;/label&gt;
                    &lt;input type="checkbox" id="op"&gt;&lt;label for="op"&gt;运维开发&lt;/label&gt;
                &lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;掌握的技能&lt;/td&gt;
                &lt;td&gt;&lt;textarea rows="7" cols="20"&gt;&lt;/textarea&gt;&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;项目经历&lt;/td&gt;
                &lt;td&gt;&lt;textarea rows="7" cols="20"&gt;&lt;/textarea&gt;&lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;&lt;/td&gt;
                &lt;td&gt;
                    &lt;input type="checkbox" id="read"&gt;
                    &lt;label for="read"&gt;我已仔细阅读过公司的招聘要求&lt;/label&gt;
                &lt;/td&gt;
            &lt;/tr&gt;
            &lt;tr&gt;
                &lt;td&gt;&lt;/td&gt;
                &lt;td&gt;
                    &lt;h3&gt;请应聘者确认：&lt;/h3&gt;
                    &lt;ol&gt;
                        &lt;li&gt;以上信息真实有效&lt;/li&gt;
                        &lt;li&gt;能够随时上岗&lt;/li&gt;
                    &lt;/ol&gt;
                &lt;/td&gt;
            &lt;/tr&gt;
        &lt;/tbody&gt;
    &lt;/table&gt;
&lt;/body&gt;
&lt;/html&gt;
```

完.

 
