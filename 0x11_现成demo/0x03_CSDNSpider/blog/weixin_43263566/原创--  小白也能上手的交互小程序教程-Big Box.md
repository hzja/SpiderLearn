# 原创
：  小白也能上手的交互小程序教程：Big Box

# 小白也能上手的交互小程序教程：Big Box

#### 引言

        本文将带您了解如何使用 HTML、CSS、JavaScript 和基本编程知识，创建一个名为“Big Box”的小程序，可以将一组小盒子收缩成一个中盒子，然后将其恢复为小盒子。

这个小程序将使用 HTML 和 CSS 来创建一个具有 flexbox 布局的容器，并在其中生成大量小盒子。最后，将使用 JavaScript 为小盒子添加事件，使其能够收缩成一个中盒子，并将其恢复为小盒子。

#### 我们来看一下完整的代码实现：

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;

&lt;head&gt;
  &lt;title&gt;Big Box&lt;/title&gt;
  &lt;style&gt;
    /* 样式定义 */
    .container {
      width: 800px;
      height: 900px;
      display: flex;
      flex-wrap: wrap;
      border: 1px solid #ccc;
    }

    .box {
      width: 8.5px;
      height: 44.5px;
      border: 1px solid #ccc;
      margin: -1px;
      /* 确保相邻的两个小盒子之间没有空隙 */
      cursor: pointer;
      transition: width 0.3s, background-color 0.3s;
      display: block;
      /* 将.display样式初始化为block */
    }

    .box.hidden {
      /* visibility: hidden; 用 display: none; 代替*/
      display: none;
    }

    /* 绿色中盒子的样式 */
    .box.middle {
      background-color: #8BC34A;
      width: 136px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: width 0.3s, background-color 0.3s;
    }
  &lt;/style&gt;
&lt;/head&gt;

&lt;body&gt;
  &lt;div class="container"&gt;
    &lt;!-- 生成80x20个小盒子 --&gt;
    &lt;script&gt;
      let boxStates = []; // 记录每个小盒子的初始 display 状态
      for (var i = 0; i &lt; 1600; i++) {
        document.write('&lt;div class="box"&gt;&lt;/div&gt;');
        boxStates[i] = window.getComputedStyle(document.querySelectorAll('.box')[i]).getPropertyValue('display');
      }
    &lt;/script&gt;
  &lt;/div&gt;
  &lt;script&gt;
    // 变量定义
    var boxes = document.querySelectorAll('.box');
    var bigBox = document.querySelector('.container');

    // 给所有小盒子绑定点击事件
    for (var i = 0; i &lt; boxes.length; i++) {
      boxes[i].addEventListener('click', function () {
        // 获取当前点击的小盒子的索引（从0开始）
        var clickedIndex = Array.prototype.indexOf.call(boxes, this);

        // 如果已经是个中盒子，则还原成16个小盒子
        if (this.classList.contains('middle')) {
          // 找到起始隐藏盒子的索引
          var startIndex = clickedIndex - 16;
          // 恢复初始状态
          for (var i = 0; i &lt; 16; i++) {
            // 这里只需要判断当前元素的 .hidden样式即可
            if (boxes[startIndex + i].classList.contains('hidden')) {
              boxes[startIndexi].classList.remove('hidden');
            }
          }
          // 移除中盒子的样式
          this.classList.remove('middle');
        } else {
          // 否则，合并成中盒子
          this.classList.add('middle');
          // 找到起始隐藏盒子的索引
          var startIndex = clickedIndex + 1;
          // 记录更改的状态
          var newBoxStates = [];
          for (var i = 0; i &lt; 16; i++) {
            if (boxes[startIndex + i].classList.contains('hidden')) {
              newBoxStates[i] = 'hidden';
            } else {
              newBoxStates[i] = 'visible';
            }
            boxes[startIndex + i].classList.add('hidden');
          }
          // 记录状态更改
          boxStates.splice(startIndex, 16, ...newBoxStates);
        }
      });
    }
  &lt;/script&gt;
&lt;/body&gt;

&lt;/html&gt;
```

#### 实现步骤 
1. 首先，我们定义了 CSS 样式，用于定义容器和盒子的样式。在容器中，我们使用了 flexbox 布局，并将其设置为具有较大的宽度和高度，以便我们有足够的空间来放置大量的盒子。在盒子中，我们使用了一些简单的样式，例如边框、宽度、高度、左右负边距等，以及初始的 display 属性，并为小盒子和中盒子定义不同的背景色。1. 然后，我们在页面上添加了一个 div 容器，其中包含一个由 JavaScript 生成的 80x20 网格的小盒子。1. 接下来是 JavaScript 部分。首先，我们使用 `querySelectorAll()` 方法选中所有小盒子，并使用 `getComputedStyle()` 方法为每个小盒子记录了其初始的 `display` 属性，以便在将中盒子还原为小盒子时，我们可以恢复每个小盒子的 `display` 属性。1. 其次，我们给所有小盒子绑定了一个 `click` 事件监听器，通过 `Array.prototype.indexOf.call()` 方法计算出小盒子的索引，以便我们可以访问和修改与当前盒子相关的其他盒子的属性。当单击一个小盒子时，我们将会执行一个简单的检查: 如果点击的是中盒子，则将其还原为小盒子并显示所有隐藏的小盒子。否则，我们将合并16个小盒子，将它们转换为一个中盒子。
在上述检查中，我们首先检查当前盒子是否为中盒子。如果是，我们将从数组中检索起始的隐藏盒子的索引，设置一个 for 循环，用于检查每个小盒子的状态是否为隐藏。如果是，我们将移除它们的 `hidden` 类，这样它们就会显示在屏幕上。然后，我们移除中盒子的样式。

如果当前盒子不是中盒子，则执行另一段代码。我们在数组中记录了新的状态，然后将每个隐藏的小盒子的 `hidden` 类添加到其 classList 中。最后，我们更新 `boxStates` 数组中的状态。

在这个小程序中，最关键的部分是如何记录和管理每个小盒子的状态。我们使用 `boxStates` 数组来记录每个小盒子的初始状态（包括文档加载后的初始状态和之后的状态更改）。在合并或分成中盒子后，我们会检查当前小盒子在 `boxStates` 中的最新状态，并根据这个状态来恢复小盒子的初始状态或者隐藏它们。

#### 总结

        总之，这是一个基于 HTML、CSS 和 JavaScript 的小程序，用于创建一个由多个小盒子组成的大盒子，在单击时可以把小盒子收缩成一个中盒子，然后再次单击时展开成小盒子。虽然这个程序看起来简单，但它涵盖了许多基础的编程概念，如选择器、事件监听器和数组的使用。通过这个例子，我们可以学习如何使用 HTML、CSS 和 JavaScript 创建交互性的小程序，并学习如何使用编程技术记录和管理数据状态。
