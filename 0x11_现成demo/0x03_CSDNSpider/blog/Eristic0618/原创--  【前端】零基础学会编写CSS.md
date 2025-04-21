# 原创
：  【前端】零基础学会编写CSS

# 【前端】零基础学会编写CSS

## 一、什么是CSS

**CSS** (Cascading Style Sheets，层叠样式表）是一种是一种用来为结构化文档（如 HTML 文档）**添加样式**（字体、间距和颜色等）的计算机语言，能够对网页中元素位置的排版进行**像素级别的精确控制**，实现**美化页面**的效果。

html决定一个页面的结构，那么css就用来控制页面的展示效果

---


## 二、CSS基本语法 

首先介绍基本的概念，CSS的基本语法由选择器和声明组成

选择器用来决定**修改谁的样式**，声明则决定了**修改成什么样子**，每条声明都是一个键值对

例如这个例子：

```
p {
    color: red; /*设置字体颜色*/
    font-size: 20px; /*设置字体大小*/
}
```

就是将所有&lt;p&gt;元素的文本都设置为红色，字体大小为20px

一个样式可以写在同一行，但是更推荐一个声明一行的风格，显得没那么拥挤

---


## 三、CSS的引入方式

CSS需要以一定的方式才能够插入HTML中

### 3.1 内部样式表

将CSS写在**style标签**中，直接嵌入到HTML内部

例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        p {
            color: red;
            font-size: 20px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    页面内容
&lt;/body&gt;
&lt;/html&gt;
```

这样可以将CSS和HTML合并在一个文件中，一般将style标签放在HTML的head标签中，也能够做到样式与页面结构分离

不过这种方式分离的不够彻底，当CSS内容很多时会显得杂乱

### 3.2 行内样式表

这种方法相比上面的内部样式表，分离程度更低，但优先级较高，且只针对单个标签生效

直接**在某个标签中定义style属性**来指定该标签的样式，但一般只适合写一些简单的样式

例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div style="color: red"&gt;行内样式表&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

行内样式表的优先级较高，会覆盖其他引入方式的样式

### 3.3 外部样式表

另外创建一个CSS文件，并使用link标签在HTML文件中引入该CSS文件，例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;link rel="stylesheet" href="test.css"&gt;
&lt;/head&gt;
&lt;body&gt;
    页面内容
&lt;/body&gt;
&lt;/html&gt;
```

这种方式的分离程度最高，是实际开发中最常用的方式

---


## 四、选择器

前面提到，选择器决定了要对谁的样式进行修改，我们必须选中了目标，才能设置属性。

选择器也有不同的种类

### 4.1 基础选择器

#### （1）标签选择器

前面的例子使用的就是标签选择器，能够快速的**修改同一标签的所有元素**，但无法进行差异化修改

例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        p {
            color: red;
        }
        div {
            color: blue;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    页面内容
&lt;/body&gt;
&lt;/html&gt;
```

#### （2）类选择器

定义某个元素的类名，然后**通过指定类名来修改其样式**

例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test {
            color: red;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;p class="test"&gt;测试&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
```

一些细节需要注意：

例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1 {
            color: red;
        }
        .test2 {
            font-size: 20px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;p class="test1 test2"&gt;测试&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
```

#### （3）id选择器

定义某个元素的id，并**通过指定id来修改其样式**

例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        #test {
            color: red;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;p id="test"&gt;测试&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
```

id选择器和类选择器相似，区别在于：

#### （4）通配符选择器

使用星号 * 来**选取所有的元素**，例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        * {
            color: red;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    页面内容
&lt;/body&gt;
&lt;/html&gt;
```

页面中的所有文字都会被改成红色

### 4.2 复合选择器

#### （1）后代选择器

也叫包含选择器，用于**选择某个父元素的某个子元素**

> 
元素1 元素2 { 声明 }


父子元素间要用空格分隔，前面的是父元素，后面的是子元素，只会修改子元素的样式

多个元素间可以使用不同的基础选择器，例如元素1用类选择器，元素2用标签选择器

例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .parent .child {
            color: red;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;ol class="parent"&gt;
        &lt;li class="child"&gt;1&lt;/li&gt;
        &lt;li&gt;2&lt;/li&gt;
        &lt;li&gt;3&lt;/li&gt;
    &lt;/ol&gt;
&lt;/body&gt;
&lt;/html&gt;
```

元素2不一定非要是子元素，孙子辈的元素也可以

#### （2）并集选择器

用于**同时对多个目标的样式进行修改**，例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1, .test2 {
            color: red;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="test1"&gt;1&lt;/div&gt;
    &lt;div class="test2"&gt;2&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

并集选择器通过逗号分割不同的目标。

任何基础选择器（如上面的类选择器）都可以使用并集选择器

#### （3）伪类选择器

伪类用于**定义元素的特殊状态**

一些网页上的链接，鼠标没放上去的时候是黑色的，但是我们把鼠标放上去后就变为了其他颜色，这是如何做到的呢？

我们可以使用伪类选择器来实现这样的效果，例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        a:link {
            color: black;
        }
        a:visited {
            color: purple;
        }
        a:hover {
            color: blue;
        }
        a:active {
            color: red;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;a href="#"&gt;链接&lt;/a&gt;
&lt;/body&gt;
&lt;/html&gt;
```

其中：

上面的例子中，我们设置的链接未访问时是黑色字体的，将鼠标放在上面就会变为蓝色，按下但不松开时字体则会变为红色，点击链接过后字体变为紫色

> 
在测试上面的例子时，链接被访问后就会一直显示紫色字体
如果我们要将一个被访问过的链接恢复为未访问的状态，则需要用ctrl+shift+delete清空浏览器历史记录


使用伪类选择器时，需要注意按照**link-visited-hover-active**的顺序定义

除了链接我们还可以在其他元素上使用伪类，例如&lt;div&gt;等

 更多伪类可以跳转：

[CSS 伪类 (w3school.com.cn)<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://www.w3school.com.cn/css/css_pseudo_classes.asp](https://www.w3school.com.cn/css/css_pseudo_classes.asp)

---


## 五、常用元素属性

知道该如何选择修改的目标后，我们还需要知道能够修改目标的哪些属性

这里只对部分常用的属性进行介绍，更多属性可以参考文档

[CSS 参考手册 (w3school.com.cn)<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://www.w3school.com.cn/cssref/index.asp](https://www.w3school.com.cn/cssref/index.asp)

### 5.1 设置字体属性

#### （1）字体类型

**font-family**：可以指定目标字体的类型，例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1 {
            font-family: '微软雅黑';
        }
        .test2 {
            font-family: '宋体';
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="test1"&gt;内容1&lt;/div&gt;
    &lt;div class="test2"&gt;内容2&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```

字体名称可以用中文，但是推荐用英文

#### （2）字体大小

**font-size**：指定目标字体的大小，例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1 {
            font-size: 20px;
        }
        .test2 {
            font-size: 40px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="test1"&gt;内容1&lt;/div&gt;
    &lt;div class="test2"&gt;内容2&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

不同浏览器默认字体大小不一样，最好显式定义一个明确值

注意，不要忘记带单位px

#### （3）字体粗细

**font-weight**：指定目标字体的粗细，例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1 {
            font-weight: bolder;
        }
        .test2 {
            font-weight: 400;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="test1"&gt;内容1&lt;/div&gt;
    &lt;div class="test2"&gt;内容2&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

字体粗细既可以用单词表示，从粗到细分别是bolder、bold、normal、lighter

也可以用数字表示，取值范围是100-900，400等同于normal，700等同于bold

#### （4）字体样式

**font-style**：指定目标字体的样式（正常或斜体），例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1 {
            font-style: italic;
        }
        .test2 {
            font-style: normal;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="test1"&gt;内容1&lt;/div&gt;
    &lt;div class="test2"&gt;内容2&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```

### 5.2 设置文本属性

#### （1）文本颜色

我们的显示器是由很多像素构成的，将每个像素视为一个点，这个点就能反映出一个具体的颜色

红绿蓝（RGB）是色光三原色，将三个颜色按照不同的比例混合就能得到不同的颜色

计算机中针对RGB三个分量，分别使用一个字节(8个比特位，范围是 0-255，十六进制范围是00-FF)表示，数值越大，该分量的颜色就越浓。

rgb(255,255,255)表示白色，rgb(0,0,0)表示黑色

在设置文本颜色时，我们也可以通过不同的方式设置，例如：

```
color: rgb(255, 255, 255);
color: white;
color: #ffffff;
```

三者都表示白色

#### （2）文本对齐

**text-align**：控制文本水平方向的对齐，例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1 {
            text-align: center;
        }
        .test2 {
            text-align: left;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="test1"&gt;内容1&lt;/div&gt;
    &lt;div class="test2"&gt;内容2&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```

其中center表示居中对齐，left表示左对齐，right表示右对齐

#### （3）文本装饰

**text-decoration**：给文本加上下划线等装饰，例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1 {
            text-decoration: underline;
        }
        .test2 {
            text-decoration: line-through;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="test1"&gt;内容1&lt;/div&gt;
    &lt;div class="test2"&gt;内容2&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

其中underline代表下划线，none代表什么都不加，overline代表上划线，line-through代表删除线

#### （4）文本缩进

**text-indent**：控制段落的首行缩进，例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1 {
            text-indent: 2em;
        }
        .test2 {
            text-indent: 4em;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="test1"&gt;内容1&lt;/div&gt;
    &lt;div class="test2"&gt;内容2&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```

其中单位可以使用px或em，推荐使用em，1em代表一个当前元素的文字大小

缩进值可以是负数，表示向左缩进

#### （5）行高

**line-height**：控制上下文本行之间的距离，例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .test1 {
            line-height: 10px;
        }
        .test2 {
            line-height: 100px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="test1"&gt;内容1&lt;/div&gt;
    &lt;div class="test2"&gt;内容2&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```

### 5.3 设置背景属性

#### （1）背景颜色

**background-color**：设置元素的背景颜色，例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        body {
            background-color: red;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    
&lt;/body&gt;
&lt;/html&gt;

```

对body的背景设置为红色，整个页面都变成红色了，可以用来设置页面的基调色

背景颜色和前面文本颜色一样也可以用三种不同的方法设置

#### （2）背景图片

**background-image**：将元素的背景设置为某张图片，例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .pic {
            background-image: url(baidu.png);
            height: 300px;
            width: 300px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="pic"&gt;&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

设置背景图片时的url既可以是绝对路径，也可以是相对路径

#### （3）背景重复

**background-repeat**：设置背景图片该以何种方式在元素中填充

其取值如下：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .pic {
            background-image: url(baidu.png);
            height: 600px;
            width: 600px;
            background-repeat: no-repeat;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="pic"&gt;&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

no-repeat比较简单这里就不展示效果了，我们从repeat开始

这是repeat的效果：

这是repeat-x的效果：

这是repeat-y的效果：

#### （4）背景图片位置

**background-position**：修改图片在元素中的位置，例如：

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .pic {
            background-image: url(baidu.png);
            height: 600px;
            width: 600px;
            border: 2px solid black; /*边框*/
            background-repeat: no-repeat; /*图片不重复*/
            background-position: 100px 100px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="pic"&gt;&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
```

为了便于演示所以给div元素加上了边框

background-position的参数有三种风格：

#### （5）背景尺寸

**background-size**：设置背景的尺寸，例如

```
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;页面标题&lt;/title&gt;
    &lt;style&gt;
        .pic {
            background-image: url(baidu.png);
            height: 600px;
            width: 600px;
            border: 2px solid black;
            background-repeat: no-repeat; 
            background-size: 100px 100px; /*背景尺寸*/
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="pic"&gt;&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```

背景尺寸既可以填具体的数值（如20px 40px表示宽度为20px，高度为40px），也可以填百分比

还可以填cover（图像完全覆盖整个背景区域，可能导致图像某些部分超出区域）或contain（图像尺寸扩展到最大但不超出背景区域）等单词

更多元素属性可以参考文档

[CSS 参考手册 (w3school.com.cn)<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://www.w3school.com.cn/cssref/index.asp](https://www.w3school.com.cn/cssref/index.asp)

完.
