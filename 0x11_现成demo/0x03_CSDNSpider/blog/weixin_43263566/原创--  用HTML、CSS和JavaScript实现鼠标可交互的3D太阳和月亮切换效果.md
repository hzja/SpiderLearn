# 原创
：  用HTML、CSS和JavaScript实现鼠标可交互的3D太阳和月亮切换效果

# 用HTML、CSS和JavaScript实现鼠标可交互的3D太阳和月亮切换效果

**部分数据来源：**ChatGPT 

#### 引言

        太阳和月亮对于我们来说是一种常见的对比，这篇文章将介绍一个使用HTML、CSS和JavaScript创建的网页场景，能够把太阳和月亮切换展示给用户。这个场景能够让用户使用鼠标和滚轮与场景互动，带来更多的趣味和体验。

### HTML代码实现部分

这里展示了HTML部分的代码来创建页面结构，包括头部文件声明，以及结构元素body和其中的两个div标签。

```
&lt;!DOCTYPE html&gt;
&lt;html lang="zh-CN"&gt;

&lt;head&gt;
 &lt;meta charset="UTF-8" /&gt;
 &lt;meta name="viewport" content="width=device-width, initial-scale=1.0" /&gt;
 &lt;title&gt;太阳和月亮切换&lt;/title&gt;
 &lt;style&gt;
   /* CSS代码在这里*/
 &lt;/style&gt;
 &lt;link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" /&gt;
&lt;/head&gt;

&lt;body&gt;
  &lt;!-- 页面容器 --&gt;
  &lt;div id="page-container"&gt;
    &lt;!-- 立方体面板 --&gt;
    &lt;div class="face front"&gt;&lt;/div&gt;
    &lt;div class="face back"&gt;&lt;/div&gt;
    &lt;div class="face top"&gt;&lt;/div&gt;
    &lt;div class="face bottom"&gt;&lt;/div&gt;
    &lt;div class="face left"&gt;&lt;/div&gt;
    &lt;div class="face right"&gt;&lt;/div&gt;
  &lt;/div&gt;
  &lt;!-- 太阳和月亮切换按钮 --&gt;
  &lt;div id="sun-moon-toggle" onclick="toggleSunMoon()"&gt;
    &lt;i class="fas fa-moon"&gt;&lt;/i&gt;
    &lt;i class="fas fa-sun"&gt;&lt;/i&gt;
  &lt;/div&gt;

 &lt;script&gt;
   // JavaScript代码在这里
 &lt;/
```

在代码中， `#page-container` 这个元素用来定义一个3D立方体场景，而 `#sun-moon-toggle` 用来表示切换按钮。页面中也链接了一个Font Awesome图标库实现按钮图标的展示。

CSS代码实现部分

下面是CSS代码的具体实现细节，其中包括页面元素的外观（如颜色、大小、位置等）以及3D场景的效果等。

```
   /* 设置 HTML 元素高度为 100% */
    html {
      height: 100%;
    }

    /* 设置 body 元素样式 */
    body {
      margin: 0;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #2d3436;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }

    /* 设置页面容器样式 */
    #page-container {
      width: 500px;
      height: 500px;
      position: relative;
      transform-style: preserve-3d;
      transition: transform 0.3s ease-in-out;
    }

    /* 设置太阳和月亮切换按钮样式 */
    #sun-moon-toggle {
      position: absolute;
      top: 20px;
      right: 0px;
      z-index: 1;
      cursor: pointer;
      width: 60px;
      height: 60px;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 50%;
      background-color: #fff;
      box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.3);
      transition: right 0.3s ease-in-out;
    }

    /* 设置太阳和月亮图标样式 */
    #sun-moon-toggle i {
      font-size: 28px;
      color: #f39c12;
      transition: color 0.3s ease-in-out;
    }

    /* 设置太阳和月亮切换按钮为夜间模式样式 */
    #sun-moon-toggle.sun-shown i.fa-moon {
      color: #f1c40f;
    }

    /* 设置太阳和月亮切换按钮为白天模式样式 */
    #sun-moon-toggle.sun-shown i.fa-sun {
      color: #fdcb6e;
    }

    /* 设置立方体面板样式 */
    .face {
      width: 500px;
      height: 500px;
      position: absolute;
      background-repeat: no-repeat;
      background-size: 100% 100%;
      border: 5px solid #fff;
      box-sizing: border-box;
      transform: translate3d(0, 0, 250px);
    }

    /* 设置前面板样式 */
    .front {
      background-image: url("https://picsum.photos/500");
      transform: rotateY(0deg) translateZ(250px);
    }

    /* 设置后面板样式 */
    .back {
      background-image: url("https://picsum.photos/501");
      transform: rotateY(180deg) translateZ(250px);
    }

    /* 设置上面板样式 */
    .top {
      background-image: url("https://picsum.photos/502");
      transform: rotateX(-90deg) translateZ(250px);
    }

    /* 设置底面板样式 */
    .bottom {
      background-image: url("https://picsum.photos/503");
      transform: rotateX(90deg) translateZ(250px);
    }

    /* 设置左面板样式 */
    .left {
      background-image: url("https://picsum.photos/504");
      transform: rotateY(-90deg) translateZ(250px);
    }

    /* 设置右面板样式 */
    .right {
      background-image: url("https://picsum.photos/505");
      transform: rotateY(90deg) translateZ(250px);
    }
```

#### JavaScript代码实现部分

下面是JavaScript代码的实现，其中包括：

**完整JavaScript代码如下：**

```
 // 获取DOM元素
    const pageContainer = document.getElementById("page-container");
    const sunMoonToggle = document.getElementById("sun-moon-toggle");
    const moonIcon = document.querySelector("#sun-moon-toggle .fa-moon");
    const sunIcon = document.querySelector("#sun-moon-toggle .fa-sun");

    // 初始化变量
    let isSunShown = false; // 初始状态下显示月亮

    // 为按钮绑定点击事件
    function toggleSunMoon() {
      if (isSunShown) {
        // 从太阳到月亮
        sunMoonToggle.classList.remove("sun-shown");
        moonIcon.style.display = "inline-block";
        sunIcon.style.display = "none";
        document.body.style.backgroundColor = "#2d3436";
      } else {
        // 从月亮到太阳
        sunMoonToggle.classList.add("sun-shown");
        sunIcon.style.display = "inline-block";
        moonIcon.style.display = "none";
        document.body.style.backgroundColor = "#ffeaa7";
      }
      isSunShown = !isSunShown;
    }

    // 鼠标按下事件
    let isMouseDown = false;
    let pageX, pageY;
    document.addEventListener("mousedown", (event) =&gt; {
      isMouseDown = true;
      pageX = event.pageX;
      pageY = event.pageY;
    });

    // 鼠标松开事件
    document.addEventListener("mouseup", () =&gt; {
      isMouseDown = false;
    });

    // 鼠标移动事件
    document.addEventListener("mousemove", (event) =&gt; {
      if (!isMouseDown) return;
      const deltaX = event.pageX - pageX;
      const deltaY = event.pageY - pageY;
      pageContainer.style.transform += `rotateX(${deltaY * 0.5}deg) rotateY(${deltaX * -0.5
        }deg)`;
      pageX = event.pageX;
      pageY = event.pageY;
    });

    // 鼠标滚轮事件
    let scale = 1;
    document.addEventListener("wheel", (event) =&gt; {
      event.preventDefault();
      scale += event.deltaY * -0.01;
      scale = Math.min(Math.max(0.5, scale), 3); // 缩放边界
      pageContainer.style.transform = `rotateX(0deg) rotateY(0deg) scale(${scale})`;
    });
```

        在这个代码片段中， `scale` 变量存储当前页面的缩放比例，当鼠标滚轮事件发生时， `event.deltaY` 用于获取鼠标滚轮的方向（正值表示向上滚动，负值则表示向下滚动），并根据其值更新 `scale` 变量。同时更新页面样式中的transform属性，以实现页面缩放。

#### 完整的HTML、CSS和JavaScript代码如下：

```
&lt;!DOCTYPE html&gt;
&lt;html lang="zh-CN"&gt;

&lt;head&gt;
  &lt;meta charset="UTF-8" /&gt;
  &lt;meta name="viewport" content="width=device-width, initial-scale=1.0" /&gt;
  &lt;title&gt;太阳和月亮切换&lt;/title&gt;
  &lt;style&gt;
    /* 设置 HTML 元素高度为 100% */
    html {
      height: 100%;
    }

    /* 设置 body 元素样式 */
    body {
      margin: 0;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: #2d3436;
      font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }

    /* 设置页面容器样式 */
    #page-container {
      width: 500px;
      height: 500px;
      position: relative;
      transform-style: preserve-3d;
      transition: transform 0.3s ease-in-out;
    }

    /* 设置太阳和月亮切换按钮样式 */
    #sun-moon-toggle {
      position: absolute;
      top: 20px;
      right: 0px;
      z-index: 1;
      cursor: pointer;
      width: 60px;
      height: 60px;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 50%;
      background-color: #fff;
      box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.3);
      transition: right 0.3s ease-in-out;
    }

    /* 设置太阳和月亮图标样式 */
    #sun-moon-toggle i {
      font-size: 28px;
      color: #f39c12;
      transition: color 0.3s ease-in-out;
    }

    /* 设置太阳和月亮切换按钮为夜间模式样式 */
    #sun-moon-toggle.sun-shown i.fa-moon {
      color: #f1c40f;
    }

    /* 设置太阳和月亮切换按钮为白天模式样式 */
    #sun-moon-toggle.sun-shown i.fa-sun {
      color: #fdcb6e;
    }

    /* 设置立方体面板样式 */
    .face {
      width: 500px;
      height: 500px;
      position: absolute;
      background-repeat: no-repeat;
      background-size: 100% 100%;
      border: 5px solid #fff;
      box-sizing: border-box;
      transform: translate3d(0, 0, 250px);
    }

    /* 设置前面板样式 */
    .front {
      background-image: url("https://picsum.photos/500");
      transform: rotateY(0deg) translateZ(250px);
    }

    /* 设置后面板样式 */
    .back {
      background-image: url("https://picsum.photos/501");
      transform: rotateY(180deg) translateZ(250px);
    }

    /* 设置上面板样式 */
    .top {
      background-image: url("https://picsum.photos/502");
      transform: rotateX(-90deg) translateZ(250px);
    }

    /* 设置底面板样式 */
    .bottom {
      background-image: url("https://picsum.photos/503");
      transform: rotateX(90deg) translateZ(250px);
    }

    /* 设置左面板样式 */
    .left {
      background-image: url("https://picsum.photos/504");
      transform: rotateY(-90deg) translateZ(250px);
    }

    /* 设置右面板样式 */
    .right {
      background-image: url("https://picsum.photos/505");
      transform: rotateY(90deg) translateZ(250px);
    }
  &lt;/style&gt;
  &lt;!-- 引入 font-awesome 图标库的 CSS 文件 --&gt;
  &lt;link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" /&gt;
&lt;/head&gt;

&lt;body&gt;
  &lt;!-- 页面容器 --&gt;
  &lt;div id="page-container"&gt;
    &lt;!-- 立方体面板 --&gt;
    &lt;div class="face front"&gt;&lt;/div&gt;
    &lt;div class="face back"&gt;&lt;/div&gt;
    &lt;div class="face top"&gt;&lt;/div&gt;
    &lt;div class="face bottom"&gt;&lt;/div&gt;
    &lt;div class="face left"&gt;&lt;/div&gt;
    &lt;div class="face right"&gt;&lt;/div&gt;
  &lt;/div&gt;
  &lt;!-- 太阳和月亮切换按钮 --&gt;
  &lt;div id="sun-moon-toggle" onclick="toggleSunMoon()"&gt;
    &lt;i class="fas fa-moon"&gt;&lt;/i&gt;
    &lt;i class="fas fa-sun"&gt;&lt;/i&gt;
  &lt;/div&gt;

  &lt;script&gt;
    // 获取DOM元素
    const pageContainer = document.getElementById("page-container");
    const sunMoonToggle = document.getElementById("sun-moon-toggle");
    const moonIcon = document.querySelector("#sun-moon-toggle .fa-moon");
    const sunIcon = document.querySelector("#sun-moon-toggle .fa-sun");

    // 初始化变量
    let isSunShown = false; // 初始状态下显示月亮

    // 为按钮绑定点击事件
    function toggleSunMoon() {
      if (isSunShown) {
        // 从太阳到月亮
        sunMoonToggle.classList.remove("sun-shown");
        moonIcon.style.display = "inline-block";
        sunIcon.style.display = "none";
        document.body.style.backgroundColor = "#2d3436";
      } else {
        // 从月亮到太阳
        sunMoonToggle.classList.add("sun-shown");
        sunIcon.style.display = "inline-block";
        moonIcon.style.display = "none";
        document.body.style.backgroundColor = "#ffeaa7";
      }
      isSunShown = !isSunShown;
    }

    // 鼠标按下事件
    let isMouseDown = false;
    let pageX, pageY;
    document.addEventListener("mousedown", (event) =&gt; {
      isMouseDown = true;
      pageX = event.pageX;
      pageY = event.pageY;
    });

    // 鼠标松开事件
    document.addEventListener("mouseup", () =&gt; {
      isMouseDown = false;
    });

    // 鼠标移动事件
    document.addEventListener("mousemove", (event) =&gt; {
      if (!isMouseDown) return;
      const deltaX = event.pageX - pageX;
      const deltaY = event.pageY - pageY;
      pageContainer.style.transform += `rotateX(${deltaY * 0.5}deg) rotateY(${deltaX * -0.5
        }deg)`;
      pageX = event.pageX;
      pageY = event.pageY;
    });

    // 鼠标滚轮事件
    let scale = 1;
    document.addEventListener("wheel", (event) =&gt; {
      event.preventDefault();
      scale += event.deltaY * -0.01;
      scale = Math.min(Math.max(0.5, scale), 3); // 缩放边界
      pageContainer.style.transform = `rotateX(0deg) rotateY(0deg) scale(${scale})`;
    });
  &lt;/script&gt;
&lt;/body&gt;

&lt;/html&gt;
```

这段代码段通过HTML、CSS、JavaScript实现了一个太阳和月亮切换的3D动画效果，实现了用户可鼠标观看的效果，兼具技术性和美观性。

#### 效果图

**鼠标长按可以旋转 **

**按钮切换背景 **

**鼠标滑轮滚动可以缩放**

 
