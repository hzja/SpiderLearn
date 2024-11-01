# 原创
：  htmlspecialchars函数绕过

# htmlspecialchars函数绕过

#### htmlspecialchars函数绕过

### 定义

> 
把预定义的字符转换为 HTML 实体


### 语法

```
htmlspecialchars(string,flags,character-set,double_encode)

```

### 用法

```
预定义的字符
&amp;：转换为&amp;amp;
"：转换为&amp;quot;
'：转换为成为 '
&lt;：转换为&amp;lt;
&gt;：转换为&amp;gt;

string：必需，规定要转换的字符串
flags ：可选，规定如何处理引号、无效的编码以及使用哪种文档类型
character-set ：可选，一个规定了要使用的字符集的字符串，如：UTF-8（默认）
double_encode ：可选，布尔值，规定了是否编码已存在的 HTML 实体

flags参数可用的引号类型
ENT_COMPAT ：默认仅编码双引号
ENT_QUOTES：编码双引号和单引号
ENT_NOQUOTES：不编码任何引号
注：xss-lab中有些关卡可以利用单引号绕过是因为flags参数默认只编码双引号

double_encode参数布尔值
TRUE：默认，将对每个实体进行转换
FALSE：不会对已存在的 HTML 实体进行编码

```

### 绕过方法

```
默认编码（仅编码双引号）

&lt;?php 
	$name = $_GET["name"];
	$name_new = htmlspecialchars($name);
?&gt;
&lt;input type='text' value='&lt;?php echo $name_new?&gt;'&gt;

利用单引号能够绕过

```
