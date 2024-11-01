# 原创
：  PHP基础 - 常量字符串

# PHP基础 - 常量字符串

#### 常量

在PHP中，常量是一个简单值的标识符，定义后默认是全局变量，可以在整个运行的脚本的任何地方使用。常量由英文字母、下划线和数字组成，但数字不能作为首字母出现。

PHP中定义常量的方式是使用`define()`函数，其语法如下：

```
bool define( string $name, mixed $value [, bool $case_insensitive = false] )
```

其中：

下面是一个例子：

```
define("CLname", "国家信息安全");
echo CLname . "\n"; // 输出：国家信息安全
//echo clname; // 产生警告：常量未定义 (默认区分大小写)

define("CL", "常量字符串");
echo CL . "\n"; // 输出：常量字符串
//echo cl; // 产生警告：常量未定义
```
