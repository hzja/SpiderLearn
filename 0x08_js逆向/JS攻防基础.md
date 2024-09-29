## 逆向的目标

+ 逆向的目标:加密数据的加密过程，脱离浏览器后本地运行js同样可获取到数据



+ 能对网站的<code>javascript</code>进行调试
  + 能修改js运行中的一些变量的值，也能输出
  + 能下断点
  + 能批量智能监听一些变量的值



## 断点详解

### 什么是断点

+ DOM断点(浏览器对象断点)
+ DOM事件断点
+ XHR断点
+ 代码行断点，最基础的断点
+ 代码断点，其实就是<code>debugger</code>
+ 全局事件断点(浏览器事件)
+ 异常捕获断点



#### DOM断点

#### Dom事件

~~~ tex
	DOM（文档对象模型，Document Object Model）事件是Web开发中的一个重要概念，它指的是在Web页面的DOM元素上发生的各种动作或行为，比如用户点击按钮、移动鼠标、提交表单等。开发者可以通过JavaScript监听这些事件，并在事件发生时执行特定的代码

以下是一些常见的DOM事件类型：

UI事件：与用户界面交互有关，如load（页面加载完毕）、error（加载资源失败）、resize（浏览器窗口大小改变）等。
鼠标事件：与鼠标操作有关，如click（鼠标点击）、dblclick（鼠标双击）、mouseover（鼠标移动到元素上）、mouseout（鼠标从元素上移开）等。
键盘事件：与键盘操作有关，如keydown（键盘上的一个键被按下）、keyup（键盘上的一个键被释放）等。
焦点事件：与元素获得或失去焦点有关，如focus（元素获得焦点）、blur（元素失去焦点）等。
表单事件：与表单操作有关，如submit（表单提交）、reset（表单重置）、change（表单控件的值改变）等。
触摸事件：与触摸屏操作有关，如touchstart、touchend、touchmove等。
自定义事件：开发者可以创建自己的事件类型，通过new Event('customType')来实现。

DOM事件模型通常包括三个阶段：
捕获阶段：事件从window对象开始，向下传播到目标元素的各个祖先节点。
目标阶段：事件到达目标元素。
冒泡阶段：事件从目标元素开始，向上传播到其祖先节点，直到window对象。

开发者可以通过设置事件监听器来响应事件，如：

// 监听点击事件
element.addEventListener('click', function(event) {
  // 处理点击事件
});

或者使用HTML的on-event属性：

<button onclick="handleClick()">点击我</button>
<script>
function handleClick() {
  // 处理点击事件
}
</script>

DOM事件是Web开发中实现交互性的关键技术之一。
~~~

看到7 js调试_DOM事件和断点一份59秒

