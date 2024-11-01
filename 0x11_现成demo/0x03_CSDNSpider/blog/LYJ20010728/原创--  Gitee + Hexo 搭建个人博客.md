# 原创
：  Gitee + Hexo 搭建个人博客

# Gitee + Hexo 搭建个人博客

#### Gitee + Hexo 搭建个人博客

## 环境安装

> 



```
npm install hexo-cli -g

```

## 本地搭建

### 初始化 Hexo

> 
新建一个空白文件夹用于存放 hexo 资源，在空白文件夹里面打开命令行 ，输入`hexo init`行进行初始化，初始化成功后会在文件夹生成如下图的文件


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/89730531e7604fe8b95b8800b797fade.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c585857c49a04de4bcf0d10383794d16.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### 生成静态页面

```
hexo g

```

### 启动本地服务

```
hexo s

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/79efa02071f94bf9b8e8b3510a2e2e84.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a6846a8f6c99457caac65d62e9cf5863.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 更改主题

### 安装Next

> 



```
git clone https://hub.fastgit.org/theme-next/hexo-theme-next.git

```

### 配置Next

> 
用Sublime打开项目根目录下的 `_config.yml` 配置文件，找到 theme 把原来默认的 landscape 主题名字改成刚刚克隆的主题名字


### 测试Next

> 
重启服务，刷新页面查看新主题


### 发布文章

> 



<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/dc0885d1879c48569f89566b79387c96.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c19f84732e2843279f70c771793e1436.png#pic_center"/>

> 



```
---
title: a
date: 2019-04-14 23:10:17
---

```

> 



```
hexo g

```

### 选择next主题样式

> 
打开主题文件夹下的 `_config.yml` 配置文件，找到 `Schemes` 模块，修改为自己喜欢的风格


## 更改站点属性

> 
在上面的网站界面，打开根目录文件夹下的 `_config.yml` 配置文件，找到 `Site` 可以修改语言、标题等其他参数的设置


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8d20ab1ccba041ee947f536bcff4a334.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c31c7a23f8f1448e88b5b0bcd5c2fa03.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 菜单栏

### 显示更多菜单

> 
在项目根目录下执行命令，新建分类页面，会在项目根目录下的 `source` 文件夹中新建一个 `categories` 文件夹


```
hexo new page categories

```

> 
打开 `categories` 文件夹中的 `index.md` 文件，添加 type 字段，设置为 “categories”


> 
在主题文件夹下的 `_config.yml` 配置文件中找到 `menu` 模块，把 `categories` 的注释给去掉


> 
在项目根目录下执行命令，新建分类页面，会在项目根目录下的 `source` 文件夹中新建一个 `tags` 文件夹


```
hexo new page tags

```

> 
打开 `tags` 文件夹中的 `index.md` 文件，添加 type 字段，设置为 “tags”


> 
在主题文件夹下的 `_config.yml` 配置文件中找到 `menu` 模块，把 `tags` 的注释给去掉


> 
当 `front-matter` 中字段有多个参数的时候，写法为


> 



```
npm install hexo-generator-search --save

```

```
npm install hexo-generator-searchdb --save

```

> 
在项目根目录下的 `_config.yml` 配置文件的文末添加如下代码


```
search:
  path: search.xml
  field: post
  format: html
  limit: 10000

```

> 
编辑主题文件夹的 `_config.yml` 配置文件，设置 Local searchenable 为 ture


> 
重启服务，查看效果


### 图标及内容量显示

> 
打开主题配置文件，找到menu_settings字段，修改


## 一般设置

### 可跳转日志、分类、标签页的链接

> 
打开主题配置文件，找到site_state字段，修改


### 社交信息设置

> 
打开主题配置文件，找到social字段，修改


> 
Next默认给出了一些模板，只要将其中的链接改为自己的链接就可以了，当然也可以自己定义，格式为名字: `链接 || 图标名`，图标必须是[FontAwesome网站](https://fontawesome.dashgame.com/)中能找到的图标名，可以将自己的博客地址添加进去


```
xxxx名字: https://地址xxxxxxx/ || codepen

```

### 博客头像设置

> 
打开主题文件夹下的 `_config.yml` 配置文件，找到 `avatar`，添加一个在线的头像图片地址（这里采用的是聚合图床）


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b482d36ae72d48f3954411cd68e5ee05.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5d1814fb3d364c7eae0a47eac6cd5e94.png#pic_center"/>

> 
打开主题文件夹下的 `_config.yml` 配置文件，找到 `avatar`，开启 rounded 和 rotated 即可设为旋转圆角


### 网站图标设置

> 
图标素材网站：[easyicon](https://www.easyicon.net/)、[iconfont](https://www.iconfont.cn/)


> 



### 建立标签云及效果展示

> 
安装插件，进入Hexo根目录，在`package.json`中添加依赖：`hexo-tag-cloud": "2.1.*`


> 
配置插件，插件的配置需要对应的环境，可以在主题文件夹里找一下，有没有对应的渲染文件，然后根据渲染文件的类型，选择对应的插件配置方法


> 
swig 用户 (Next主题为例)<br/> 在主题文件夹找到文件 `theme/next/layout/_macro/sidebar.swig`, 然后找到`theme.back2top`在其结束行后添加如下代码


```
{% if site.tags.length &gt; 1 %}
&lt;script type="text/javascript" charset="utf-8" src="/js/tagcloud.js"&gt;&lt;/script&gt;
&lt;script type="text/javascript" charset="utf-8" src="/js/tagcanvas.js"&gt;&lt;/script&gt;
&lt;div class="widget-wrap"&gt;
    &lt;h3 class="widget-title"&gt;Tag Cloud&lt;/h3&gt;
    &lt;div id="myCanvasContainer" class="widget tagcloud"&gt;
        &lt;canvas width="250" height="250" id="resCanvas" style="width=100%"&gt;
            {{ list_tags() }}
        &lt;/canvas&gt;
    &lt;/div&gt;
&lt;/div&gt;
{% endif %}

```

> 
ejs的用户 (默认主题landscape为例)<br/> 在主题文件夹找到文件`hexo/themes/landscape/layout/_widget/tagcloud.ejs`，将这个文件修改如下


```
&lt;% if (site.tags.length) { %&gt;
  &lt;script type="text/javascript" charset="utf-8" src="&lt;%- url_for('/js/tagcloud.js') %&gt;"&gt;&lt;/script&gt;
  &lt;script type="text/javascript" charset="utf-8" src="&lt;%- url_for('/js/tagcanvas.js') %&gt;"&gt;&lt;/script&gt;
  &lt;div class="widget-wrap"&gt;
    &lt;h3 class="widget-title"&gt;&lt;%= __('tagcloud') %&gt;&lt;/h3&gt;
    &lt;div id="myCanvasContainer" class="widget tagcloud"&gt;
      &lt;canvas width="250" height="250" id="resCanvas" style="width=100%"&gt;
        &lt;%- tagcloud() %&gt;
      &lt;/canvas&gt;
    &lt;/div&gt;
  &lt;/div&gt;
&lt;% } %&gt;

```

> 
开主题配置，然后在最后添加如下的配置项，可以自定义标签云的字体和颜色，还有突出高亮：


```
# hexo-tag-cloud
tag_cloud:
    textFont: Trebuchet MS, Helvetica
    textColor: '#333'
    textHeight: 25
    outlineColor: '#E2E1D1'
    maxSpeed: 0.1

```

> 
构建：`hexo clean &amp;&amp; hexo g &amp;&amp; hexo d`


### 文章添加阴影、透明效果及代码块样式

> 
打开 `source/_data/styles.styl`，在此样式中加入以下代码


```
// 主页文章添加阴影效果
.post {
   margin-top: 60px;
   margin-bottom: 60px;
   padding: 25px;
   background:rgba(255,255,255,0.9) none repeat scroll !important;
   -webkit-box-shadow: 0 0 5px rgba(202, 203, 203, .5);
   -moz-box-shadow: 0 0 5px rgba(202, 203, 204, .5);
}

```

> 
在站点配置文件中，搜索`highlight`


```
highlight:
      enable: true #是否开启代码高亮
      line_number: false #是否增加代码行号
      auto_detect: true #自动判断代码语言
      tab_replace:

```

> 
代码块背景，打开主题配置，查找`highlight_theme`


### 其他可参考设置

```
toc:
  enable: true #自动生成目录
  # Automatically add list number to toc.
  number: true #自动产生目录编号
  # If true, all words will placed on next lines if header width longer then sidebar width.
  wrap: false #标题过长是否换行
  # If true, all level of TOC in a post will be displayed, rather than the activated part of it.
  expand_all: false # 是否显示所有等级的目录项。
  # Maximum heading depth of generated toc. You can set it in one post through `toc_max_depth` in Front-matter.
  max_depth: 6 #最大标题嵌套个数

sidebar:
  # Sidebar Position.#侧边栏的位置
  position: left
  #position: right

  # Manual define the sidebar width. If commented, will be default for:
  # Muse | Mist: 320
  # Pisces | Gemini: 240
  #width: 300

  # Sidebar Display (only for Muse | Mist), available values:
  # 显示侧边栏的时机
  #  - post    expand on posts automatically. Default.
  #  - always  expand for all pages automatically.
  #  - hide    expand only when click on the sidebar toggle icon.
  #  - remove  totally remove sidebar including sidebar toggle.
  display: post

  # Sidebar offset from top menubar in pixels (only for Pisces | Gemini).
  offset: 12 # 侧边栏相对主菜单的像素距离
  # Enable sidebar on narrow view (only for Muse | Mist).
  onmobile: false #在手机上侧边栏是否显示

# 返回顶部
back2top:
  enable: true 
  # Back to top in sidebar.
  sidebar: false  #侧边栏显示返回顶部信息,默认显示在页面右下方
  # Scroll percent label in b2t button.
  scrollpercent:   #显示百分比,显示当前浏览进度

```

## 页面美化设置

### 鼠标左键点击红心

#### 普通小红心

> 
打开 `themes/next/souce/js` 文件夹，新建 `clicklove.js` 内容如下


```
!function(e,t,a){function n(){c(".heart{width: 10px;height: 10px;position: fixed;background: #f00;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);}.heart:after,.heart:before{content: '';width: inherit;height: inherit;background: inherit;border-radius: 50%;-webkit-border-radius: 50%;-moz-border-radius: 50%;position: fixed;}.heart:after{top: -5px;}.heart:before{left: -5px;}"),o(),r()}function r(){for(var e=0;e&lt;d.length;e++)d[e].alpha&lt;=0?(t.body.removeChild(d[e].el),d.splice(e,1)):(d[e].y--,d[e].scale+=.004,d[e].alpha-=.013,d[e].el.style.cssText="left:"+d[e].x+"px;top:"+d[e].y+"px;opacity:"+d[e].alpha+";transform:scale("+d[e].scale+","+d[e].scale+") rotate(45deg);background:"+d[e].color+";z-index:99999");requestAnimationFrame(r)}function o(){var t="function"==typeof e.onclick&amp;&amp;e.onclick;e.onclick=function(e){t&amp;&amp;t(),i(e)}}function i(e){var a=t.createElement("div");a.className="heart",d.push({el:a,x:e.clientX-5,y:e.clientY-5,scale:1,alpha:1,color:s()}),t.body.appendChild(a)}function c(e){var a=t.createElement("style");a.type="text/css";try{a.appendChild(t.createTextNode(e))}catch(t){a.styleSheet.cssText=e}t.getElementsByTagName("head")[0].appendChild(a)}function s(){return"rgb("+~~(255*Math.random())+","+~~(255*Math.random())+","+~~(255*Math.random())+")"}var d=[];e.requestAnimationFrame=function(){return e.requestAnimationFrame||e.webkitRequestAnimationFrame||e.mozRequestAnimationFrame||e.oRequestAnimationFrame||e.msRequestAnimationFrame||function(e){setTimeout(e,1e3/60)}}(),n()}(window,document);

```

> 
在 `themes/next/layout/_layout.swig` 文件末尾添加


```
&lt;!-- 页面点击小红心 --&gt;
{% if theme.clicklove %}
      &lt;script type="text/javascript" src="/js/clicklove.js"&gt;&lt;/script&gt;
{% endif %}

```

> 
注：此时需要先查看自己站点配置文件，搜索 `root:**` 查看路径是否为默认 `/` 否则在添加 `js**` 路径的时候需要加上此路径


#### 爆炸红心特效

> 
打开 `themes/next/souce/js` 文件夹，新建一个 fireworks.js 内容如下


```
"use strict";function updateCoords(e){pointerX=(e.clientX||e.touches[0].clientX)-canvasEl.getBoundingClientRect().left,pointerY=e.clientY||e.touches[0].clientY-canvasEl.getBoundingClientRect().top}function setParticuleDirection(e){var t=anime.random(0,360)*Math.PI/180,a=anime.random(50,180),n=[-1,1][anime.random(0,1)]*a;return{x:e.x+n*Math.cos(t),y:e.y+n*Math.sin(t)}}function createParticule(e,t){var a={};return a.x=e,a.y=t,a.color=colors[anime.random(0,colors.length-1)],a.radius=anime.random(16,32),a.endPos=setParticuleDirection(a),a.draw=function(){ctx.beginPath(),ctx.arc(a.x,a.y,a.radius,0,2*Math.PI,!0),ctx.fillStyle=a.color,ctx.fill()},a}function createCircle(e,t){var a={};return a.x=e,a.y=t,a.color="#F00",a.radius=0.1,a.alpha=0.5,a.lineWidth=6,a.draw=function(){ctx.globalAlpha=a.alpha,ctx.beginPath(),ctx.arc(a.x,a.y,a.radius,0,2*Math.PI,!0),ctx.lineWidth=a.lineWidth,ctx.strokeStyle=a.color,ctx.stroke(),ctx.globalAlpha=1},a}function renderParticule(e){for(var t=0;t&lt;e.animatables.length;t++){e.animatables[t].target.draw()}}function animateParticules(e,t){for(var a=createCircle(e,t),n=[],i=0;i&lt;numberOfParticules;i++){n.push(createParticule(e,t))}anime.timeline().add({targets:n,x:function(e){return e.endPos.x},y:function(e){return e.endPos.y},radius:0.1,duration:anime.random(1200,1800),easing:"easeOutExpo",update:renderParticule}).add({targets:a,radius:anime.random(80,160),lineWidth:0,alpha:{value:0,easing:"linear",duration:anime.random(600,800)},duration:anime.random(1200,1800),easing:"easeOutExpo",update:renderParticule,offset:0})}function debounce(e,t){var a;return function(){var n=this,i=arguments;clearTimeout(a),a=setTimeout(function(){e.apply(n,i)},t)}}var canvasEl=document.querySelector(".fireworks");if(canvasEl){var ctx=canvasEl.getContext("2d"),numberOfParticules=30,pointerX=0,pointerY=0,tap="mousedown",colors=["#FF1461","#18FF92","#5A87FF","#FBF38C"],setCanvasSize=debounce(function(){canvasEl.width=2*window.innerWidth,canvasEl.height=2*window.innerHeight,canvasEl.style.width=window.innerWidth+"px",canvasEl.style.height=window.innerHeight+"px",canvasEl.getContext("2d").scale(2,2)},500),render=anime({duration:1/0,update:function(){ctx.clearRect(0,0,canvasEl.width,canvasEl.height)}});document.addEventListener(tap,function(e){"sidebar"!==e.target.id&amp;&amp;"toggle-sidebar"!==e.target.id&amp;&amp;"A"!==e.target.nodeName&amp;&amp;"IMG"!==e.target.nodeName&amp;&amp;(render.play(),updateCoords(e),animateParticules(pointerX,pointerY))},!1),setCanvasSize(),window.addEventListener("resize",setCanvasSize,!1)}"use strict";function updateCoords(e){pointerX=(e.clientX||e.touches[0].clientX)-canvasEl.getBoundingClientRect().left,pointerY=e.clientY||e.touches[0].clientY-canvasEl.getBoundingClientRect().top}function setParticuleDirection(e){var t=anime.random(0,360)*Math.PI/180,a=anime.random(50,180),n=[-1,1][anime.random(0,1)]*a;return{x:e.x+n*Math.cos(t),y:e.y+n*Math.sin(t)}}function createParticule(e,t){var a={};return a.x=e,a.y=t,a.color=colors[anime.random(0,colors.length-1)],a.radius=anime.random(16,32),a.endPos=setParticuleDirection(a),a.draw=function(){ctx.beginPath(),ctx.arc(a.x,a.y,a.radius,0,2*Math.PI,!0),ctx.fillStyle=a.color,ctx.fill()},a}function createCircle(e,t){var a={};return a.x=e,a.y=t,a.color="#F00",a.radius=0.1,a.alpha=0.5,a.lineWidth=6,a.draw=function(){ctx.globalAlpha=a.alpha,ctx.beginPath(),ctx.arc(a.x,a.y,a.radius,0,2*Math.PI,!0),ctx.lineWidth=a.lineWidth,ctx.strokeStyle=a.color,ctx.stroke(),ctx.globalAlpha=1},a}function renderParticule(e){for(var t=0;t&lt;e.animatables.length;t++){e.animatables[t].target.draw()}}function animateParticules(e,t){for(var a=createCircle(e,t),n=[],i=0;i&lt;numberOfParticules;i++){n.push(createParticule(e,t))}anime.timeline().add({targets:n,x:function(e){return e.endPos.x},y:function(e){return e.endPos.y},radius:0.1,duration:anime.random(1200,1800),easing:"easeOutExpo",update:renderParticule}).add({targets:a,radius:anime.random(80,160),lineWidth:0,alpha:{value:0,easing:"linear",duration:anime.random(600,800)},duration:anime.random(1200,1800),easing:"easeOutExpo",update:renderParticule,offset:0})}function debounce(e,t){var a;return function(){var n=this,i=arguments;clearTimeout(a),a=setTimeout(function(){e.apply(n,i)},t)}}var canvasEl=document.querySelector(".fireworks");if(canvasEl){var ctx=canvasEl.getContext("2d"),numberOfParticules=30,pointerX=0,pointerY=0,tap="mousedown",colors=["#FF1461","#18FF92","#5A87FF","#FBF38C"],setCanvasSize=debounce(function(){canvasEl.width=2*window.innerWidth,canvasEl.height=2*window.innerHeight,canvasEl.style.width=window.innerWidth+"px",canvasEl.style.height=window.innerHeight+"px",canvasEl.getContext("2d").scale(2,2)},500),render=anime({duration:1/0,update:function(){ctx.clearRect(0,0,canvasEl.width,canvasEl.height)}});document.addEventListener(tap,function(e){"sidebar"!==e.target.id&amp;&amp;"toggle-sidebar"!==e.target.id&amp;&amp;"A"!==e.target.nodeName&amp;&amp;"IMG"!==e.target.nodeName&amp;&amp;(render.play(),updateCoords(e),animateParticules(pointerX,pointerY))},!1),setCanvasSize(),window.addEventListener("resize",setCanvasSize,!1)};

```

> 
打开 `themes/next/layout/_layout.swig`，在上面写下如下代码（注意和上面的对齐）


```
{% if theme.fireworks %}
   &lt;canvas class="fireworks" style="position: fixed;left: 0;top: 0;z-index: 1; pointer-events: none;" &gt;&lt;/canvas&gt; 
   &lt;script type="text/javascript" src="//cdn.bootcss.com/animejs/2.2.0/anime.min.js"&gt;&lt;/script&gt; 
   &lt;script type="text/javascript" src="/js/src/fireworks.js"&gt;&lt;/script&gt;
{% endif %}

```

> 
打开主题配置文件 themes/next/ 下的 _config.yml，在文件末尾添加


```
# Fireworks
fireworks: true

```

### 背景设置

#### 动态背景设置

> 
打开主题文件夹下的 `layout` 文件夹中的 `_layout.swig` 文件，在文末加上如下的代码


```
&lt;!-- 动态背景 --&gt;
&lt;script type="text/javascript" src="//cdn.bootcss.com/canvas-nest.js/1.0.0/canvas-nest.min.js"&gt;&lt;/script&gt;

```

#### 背景图片设置

> 
修改主题配置文件 `_config.yml`，找到 `custom_file_path`，取消注释 `style` 其中这个 source 目录指的是博客所在文件夹的根目录下的 source 文件夹，也就是存储 _post 文件夹的目录


> 
打开 `source/_data/styles.styl`，在此样式中加入


```
body {
  background:url(yourself); //图片地址
  //background-size: cover;
  background-repeat: no-repeat; //是否重复出现
  background-attachment: fixed; //定义背景图片随滚动轴的移动方式
  background-position: center; //设置背景图像的起始位置
}
//博客内容透明化
//文章内容的透明度设置
.content-wrap {
  opacity: 0.85;
}

//侧边框的透明度设置
.sidebar {
  opacity: 0.85;
}
//菜单栏的透明度设置
.header-inner {
  background: rgba(255,255,255,0.85);
}
//搜索框（local-search）的透明度设置
.popup {
  opacity: 0.85;
}

```

### 背景动画

> 



```
git clone https://hub.fastgit.org/theme-next/theme-next-canvas-nest.git source/lib/canvas-nest

```

> 
打开 `themes/next/_config.yml` 文件，搜索 `Canvas-nest`，将 canvas_nest 的中 enable 值改为 true 即可


```
# Canvas-nest
# Dependencies: https://github.com/theme-next/theme-next-canvas-nest
canvas_nest:
  enable: true
  onmobile: true # display on mobile or not
  color: "0,0,255" # RGB values, use ',' to separate
  opacity: 0.5 # the opacity of line: 0~1
  zIndex: -1 # z-index property of the background
  count: 99 # the number of lines

```

> 
如果选择 `JavaScript 3D library` 风格，进入 `theme/next` 目录，执行命令


```
git clone https://hub.fastgit.org/theme-next/theme-next-three.git source/lib/three

```

> 
打开 `themes/next/_config.yml` 文件，搜索 `theme-next-three`，将值改为 true 即可


```
# three_waves
three_waves: false
# canvas_lines
canvas_lines: true
# canvas_sphere
canvas_sphere: false

```

> 
补充说明三种参考配置，想用哪种就将该项的 enable 设为 true


```
# 设置动态背景
# Canvas-nest
# Dependencies: https://github.com/theme-next/theme-next-canvas-nest
canvas_nest:
  enable: true
  onmobile: true # display on mobile or not
  color: "0,0,255" # RGB values, use `,` to separate
  opacity: 0.5 # the opacity of line: 0~1
  zIndex: -1 # z-index property of the background
  count: 170 # the number of lines

# JavaScript 3D library.
# Dependencies: https://github.com/theme-next/theme-next-three
three:
  enable: false
  delay: false # Set true to further delay loading
  three_waves: true
  canvas_lines: false
  canvas_sphere: false

# Canvas-ribbon
# Dependencies: https://github.com/theme-next/theme-next-canvas-ribbon
canvas_ribbon:
  enable: false
  size: 300 # The width of the ribbon
  alpha: 0.6 # The transparency of the ribbon
  zIndex: -1 # The display level of the ribbon

```

### 显示busuanzi博客访客/访问次数统计

> 
不蒜子统计功能，打开`themes/next/_config.yml`，修改内容


### Github标识

> 
打开themes/next/下的`_config.yml`，修改内容


### 主题样式调色

> 
打开`\themes\next\source\css\_variables\base.styl`


> 
原配色


```
$whitesmoke   = #f5f5f5;
$gainsboro    = #eee;
$grey-lighter = #ddd;
$grey-light   = #ccc;
$grey         = #bbb;
$grey-dark    = #999;
$grey-dim     = #666;
$black-light  = #555;
$black-dim    = #333;
$black-deep   = #222;
$red          = #ff2a2a;
$blue-bright  = #87daff;
$blue         = #0684bd;
$blue-deep    = #262a30;
$orange       = #fc6423;

```

> 
修改后配色


```
$whitesmoke   = #daa5ff; // 菜单栏当前菜单，归档线条
$gainsboro    = #e3c6f0; // 菜单栏头像边框，分割线。单行代码块
$gray-lighter = #cccedd; // 菜单栏子标题
$grey-light   = #ab2acc; // 菜单栏文章计数器
$grey         = #6a2dbb; // 时间节点
$grey-dark    = #67439a; // 菜单栏博主卡片区文字【描述|日志|分类|标签】
$grey-dim     = #9059bf;
$black-light  = #3d155a;  // 文章正文颜色
$black-dim    = #5b2293;
$black-deep   = #6947bb;  // 菜单栏背景
$red          = #ff2a2a;
$blue-bright  = #87daff;
$blue         = #0684bd;
$blue-deep    = #262a30;
$orange       = #fc6423;

```

### 底部隐藏由Hexo强力驱动、主题–NexT.Mist

> 
在主题文件夹下，打开 `layout/_partials/footer.swig` 文件，注释掉相关代码如下所示，位置是文末


### 博客底部布局

> 
打开themes/next/下的`_config.yml`


```
footer:
  # Specify the date when the site was setup. If not defined, current year will be used.
  since: 2021

  # Icon between year and copyright info.
  icon:
    # Icon name in Font Awesome. See: https://fontawesome.com/icons
    name: fa fa-heart
    # If you want to animate the icon, set it to true.
    animated: true
    # Change the color of icon, using Hex Code.
    color: "#808080"

  # If not defined, `author` from Hexo `_config.yml` will be used.
  copyright: H3rmesk1t

  # Powered by Hexo &amp; NexT
  powered: true

  # Beian ICP and gongan information for Chinese users. See: https://beian.miit.gov.cn, http://www.beian.gov.cn
  beian:
    enable: false
    icp:
    # The digit in the num of gongan beian.
    gongan_id:
    # The full num of gongan beian.
    gongan_num:
    # The icon for gongan beian. See: http://www.beian.gov.cn/portal/download
    gongan_icon_url:

```

### 添加lazyload图片懒加载

> 
懒加载，简言之就是在html加载的时候，若果img标签的src是有内容的，在加载的过程中，img标签就回去请求这个图片，直到加载完，我们的浏览器的刷新那个图标才会停止转动，也就是才算请求完，懒加载能够在你鼠标不动的时候只加载目前电脑窗口内需要展示的图片，电脑屏幕内部需要展示的图片就暂时不加载，从而达到加快访问网站速度的效果


> 
在主目录下执行命令：


```
npm install hexo-lazyload-image --save

```

> 
在站点配置文件`_config.yml`任意位置添加配置


```
# 图片懒加载
lazyload:
  enable: true 
  onlypost: false 
  loadingImg: /images/loading.gif 

```

### 接入网易云播放器

> 
先在网易云音乐网页版搜索到想播放的音乐，点击生成外链播放器，得到外链的html代码，然后我们将代码粘贴到一个合适的位置，建议在侧边栏，对应的文件是`themes/next/layout/_macro/sidebar.swig` ，不同的位置效果呈现的效果不同


## 文章内容相关

### 文章加密(hexo-blog-encrypt)

> 
安装，[hexo-blog-encrypt参考文档](https://github.com/D0n9X1n/hexo-blog-encrypt/blob/master/ReadMe.zh.md)


```
npm install --save hexo-blog-encrypt

```

> 
设置站点配置文件：


```

# Security
encrypt: # hexo-blog-encrypt
  abstract: 有东西被加密了, 请输入密码查看.
  message: 您好, 这里需要密码.
  tags:
  - {name: tagName, password: 密码A}
  - {name: tagName, password: 密码B}
  wrong_pass_message: 抱歉, 这个密码看着不太对, 请再试试.
  wrong_hash_message: 抱歉, 这个文章不能被校验, 不过您还是能看看解密后的内容.

```

> 
然后在文章的头部添加上对应的字段，如 password, abstract, message等


```
---
title: Hello World
date: 2016-03-30 21:12:21
tags:
- 作为日记加密
password: 123456
default-abstract: 这是一篇加密文章，内容可能是个人情感宣泄或者收费技术。如果你确实想看，请与我联系。
default-message: 输入密码，查看文章。
wrong_pass_message: 抱歉, 这个密码看着不太对, 请再试试.
wrong_hash_message: 抱歉, 这个文章不能被校验, 不过您还是能看看解密后的内容.
---

```

> 



> 
这些信息可以直接配置到站点的配置文件中，如果不配置则每篇文档都需要单独配置


#### 对 TOC 进行加密

> 
如果你有一篇文章使用了 TOC，你需要修改模板的部分代码，这里用 landscape 作为例子


> 
可以在 `hexo/themes/landscape/layout/_partial/article.ejs` 找到 `article.ejs`,然后找到 `&lt;% post.content %&gt;` 这段代码，使用如下的代码来替代它


```
&lt;% if(post.toc == true){ %&gt;
  &lt;div id="toc-div" class="toc-article" &lt;% if (post.encrypt == true) { %&gt;style="display:none" &lt;% } %&gt;&gt;
    &lt;strong class="toc-title"&gt;Index&lt;/strong&gt;
      &lt;% if (post.encrypt == true) { %&gt;
        &lt;%- toc(post.origin, {list_number: true}) %&gt;
      &lt;% } else { %&gt;
        &lt;%- toc(post.content, {list_number: true}) %&gt;
      &lt;% } %&gt;
  &lt;/div&gt;
&lt;% } %&gt;
&lt;%- post.content %&gt;

```

#### 对博文禁用 Tag 加密

```
---
title: Callback Test
date: 2019-12-21 11:54:07
tags:
    - A Tag should be encrypted
password: ""
---

Use a "" to diable tag encryption.

```

#### 配置优先级

> 
文章信息头 &gt; _config.yml (站点根目录下的) &gt; 默认配置


#### 关于 Callback 函数

```
---
title: Callback Test
date: 2019-12-21 11:54:07
tags:
    - Encrypted
---

这是测试回调功能的博客。 您只需要在帖子的最后添加代码，如下所示：
博客解密后将调用它。
&lt;script&gt;
    // 添加一个 script tag 与代码在文章末尾.
    alert("Hello World");
&lt;/script&gt;

```

#### 自定义默认信息

> 
如果你对默认的主题不满意，或者希望修改默认的提示和摘要内容，你可以添加如下配置在`_config.yml`中


```
# 文章加密
encrypt: # hexo-blog-encrypt
  enable: true
  default-abstract: 有东西被加密了, 请输入密码查看.
  default-message: 您好, 这里需要密码.
 tags:
  - {name: tagName, password: 密码A}
  - {name: tagName, password: 密码B}
  template: &lt;div id="hexo-blog-encrypt" data-wpm="{{hbeWrongPassMessage}}" data-whm="{{hbeWrongHashMessage}}"&gt;&lt;div class="hbe-input-container"&gt;&lt;input type="password" id="hbePass" placeholder="{{hbeMessage}}" /&gt;&lt;label&gt;{{hbeMessage}}&lt;/label&gt;&lt;div class="bottom-line"&gt;&lt;/div&gt;&lt;/div&gt;&lt;script id="hbeData" type="hbeData" data-hmacdigest="{{hbeHmacDigest}}"&gt;{{hbeEncryptedData}}&lt;/script&gt;&lt;/div&gt;
  wrong_pass_message: 抱歉, 这个密码看着不太对, 请再试试.
  wrong_hash_message: 抱歉, 这个文章不能被校验, 不过您还是能看看解密后的内容.

```

#### 禁用 LOG

> 
如果你想要禁止使用 Log, 你可以在 `_config.yml` 中增加一个 silent 属性, 并将其设置为 true


```
# Security
encrypt: # hexo-blog-encrypt
  silent: true

```

> 
这样就会禁止如 INFO hexo-blog-encrypt: encrypting “{Blog Name}” based on Tag: “EncryptedTag”. 的日志


#### 存在问题

> 



### Front-matter

> 
[Front-matter](https://hexo.io/zh-cn/docs/front-matter.html)是md文件最上方以 —分隔的区域，用于指定个别文件的变量,只有文章支持分类和标签，可以在Front-matter中设置


```
categories:
- Diary
- Life

```

> 
分类具有顺序性和层次性，而标签没有顺序和层次，会使分类Life成为Diary的子分类，而不是并列分类，因此有必要为文章选择尽可能准确的分类


> 
如果为文章添加多个分类，可以尝试以下 list 中的方法


```
categories:
 - [Diary, PlayStation]
 - [Diary, Games]
 - [Life]

```

> 
此时这篇文章同时包括三个分类：PlayStation 和 Games 分别都是父分类 Diary 的子分类，同时 Life 是一个没有子分类的分类


> 
可以修改scaffolds下的post.md、page.md、draft.md，在最顶部加上


```
---
title: {{ title }}
author: 
date: {{ date }}
summary: # 文章摘要
top: true
cover: true
abbrlink: 213245 # 自己可随意设置
img: 'https://img-blog.csdnimg.cn/20200309120551356.png'  # 设置文章背景图，设置为外链图片，访问快
mathjax: true
tags: # 标签
 - 算法
 - 计算机知识
categories: # 分类
 - 算法
password:  # 设置密码（yml中开启相应功能）
coverImg:  # 轮播图片
---

```

> 
打开Git Bash输入命令


```
hexo new post "xxx"
hexo new page "xxx"
hexo new draft "xxx"

```

> 
随后生成的md就会有Front-matter信息


### 文章摘要显示（显示阅读全文按钮）

> 
打开主题配置文件，修改内容如下


```
auto_excerpt:
  enable: true  
  length: 150 # 截取的内容长度
  
# Read more button
# If true, the read more button would be displayed in excerpt section.
read_more_btn: true # 是否显示阅读全文按钮

```

### 代码块设置

```
# 代码块设置
codeblock:
  # Code Highlight theme
  # Available values: normal | night | night eighties | night blue | night bright
  # See: https://github.com/chriskempson/tomorrow-theme
  # 代码块主题, 可选的值为 normal; night; night eighties; night blue; night bright
  highlight_theme: night
  # Add copy_button on codeblock
  # 显示复制按钮
  copy_button:
    enable: true
    # Show text copy result.
    show_result: true
    # Available values: default | flat | mac
    style:  # 按钮显示格式

```

> 
代码块样式的具体内容可以查看[官方文档](http://theme-next.iissnan.com/theme-settings.html#syntax-highlight-scheme)


### 添加文章结束提示语

> 
在`themes/next/layout/_macro/` 新建 `post-end-text.swig` 文件，将下面的代码添加进去


```
&lt;div&gt;
    {% if not is_index %}
        &lt;div style="text-align:center;color: #ccc;font-size:14px;"&gt;
            ------------- 本文结束 &lt;i class="fa fa-heart-o"&gt;&lt;/i&gt; 感谢您的阅读-------------
    	&lt;/div&gt;
    {% endif %}
&lt;/div&gt;

```

> 
然后我们修改`themes/next/layout/_macro/post.swig`文件


```
{#####################}
{### END POST BODY ###}
{#####################}
&lt;!--文章结束标语--&gt;
&lt;div&gt;
    {% if not is_index %}
    {% include 'post_end_text.swig' %}
    {% endif %}
&lt;/div&gt;

```

> 
然后，在主题配置文件末尾添加如下配置，就可以在这里将其设为 true 或 false 来控制其显示


```
# 文章结束提示语
post_end_text: true
# 或者
passage_end_tag:
	enabled: true

```

### 添加博客字数和阅读时间统计功能

> 
首先在站点根目录下配置依赖


```
npm install hexo-symbols-count-time --save

```

> 
然后再站点配置文件中加入以下内容


```
symbols_count_time:
  symbols: true #是否统计字数
  time: true #是否统计阅读时长
  total_symbols: true #是否统计总字数
  total_time: true #是否统计总阅读时长

```

> 
最后在主题配置文件中修改为以下内容


```
# 字数及访问时间统计
symbols_count_time:
  separated_meta: true  #分隔线
  item_text_post: true  #文章中的显示是否显示文本
  item_text_total: true       #网页底部的显示是否显示文本
  awl: 2 #平均每个字符的长度
  wpm: 275 # 设定每分钟可阅读的字符数

```

### 修改tag图标及文章加入图片

> 
默认的 tag 样式为 # 不带图标，只要在主题配置文件中修改


```
# Use icon instead of the symbol # to indicate the tag at the bottom of the post
# 使用标签图标
tag_icon: true

```

> 
文章加入图片，可以将图片放到[Cloudinary](https://cloudinary.com/)复制图片链接使用


### 添加打赏及版权信息

> 
打开`themes/next/_config.yml`，查找Reward (Donate)


```
# Reward (Donate)
# 打赏设置
reward_settings:
  # If true, reward would be displayed in every article by default.
  # You can show or hide reward in a specific article throuth `reward: true | false` in Front-matter.
  enable: true # 功能开关
  animation: true # 动画
  #comment: Donate comment here.

reward:
  #wechatpay: /images/wechatpay.png # 微信捐赠二维码图片
  #alipay: /images/alipay.png # 支付宝捐赠二维码图片
  #bitcoin: /images/bitcoin.png # 比特币

```

> 
打开`themes/next/_config.yml`，查找creative_commons


```
# Creative Commons 4.0 International License.
# See: https://creativecommons.org/share-your-work/licensing-types-examples
# Available values of license: by | by-nc | by-nc-nd | by-nc-sa | by-nd | by-sa | zero
# You can set a language value if you prefer a translated version of CC license, e.g. deed.zh
# CC licenses are available in 39 languages, you can find the specific and correct abbreviation you need on 
# https://creativecommons.org
creative_commons:
  license: by-nc-sa # 许可协议
  sidebar: true # 侧边栏显示
  post: true # 文章底部显示，将false改为true即可显示版权信息
  language:

```

## 对接码云的远程仓库

> 
在码云上创建一个公有仓库，并把公有仓库的链接保存下来


> 
打开项目根目录下的 _config.yml 配置文件，修改 deploy 的值，tpye 设置为 git，repo 则设置为刚刚新建的远程仓库链接


```
# Deployment
## Docs: https://hexo.io/docs/one-command-deployment
deploy:
  type: git
  repo: https://gitee.com/h3rmesk1t/blog.git
  branch: master

```

> 
在项目根目录下，打开 Git Bash，配置码云的用户和邮箱


```
git config --global user.name空格+你的码云的名字
git config --global user.email空格+你的码云的邮箱

```

> 
安装`hexo-deployer-git`


```
npm install hexo-deployer-git --save

```

> 
部署到远程仓库


```
hexo g
hexo deploy

```

> 
回到刚刚新建的远程仓库，刷新页面，可以发现本地博客的相关文件已经全部部署到远程仓库上了


> 
配置免费域名：项目首页 -&gt; 服务 -&gt; Gitee Pages


> 
点击 Gitee Pages 生成的网站地址，即可远程访问自己的个人博客，但发现博客上的样式都没有


> 
打开项目根目录下的 _config.yml 文件，修改 URL 部分的参数。<br/> url 字段的值修改为远程访问连接<br/> root 字段的值修改 /+远程仓库的名称


> 
重新部署


```
hexo clean
hexo g
hexo d

```
