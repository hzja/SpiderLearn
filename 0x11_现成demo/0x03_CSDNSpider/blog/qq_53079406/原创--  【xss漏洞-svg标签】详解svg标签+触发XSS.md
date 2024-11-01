# 原创
：  【xss漏洞-svg标签】详解svg标签+触发XSS

# 【xss漏洞-svg标签】详解svg标签+触发XSS

**目录**

[一、理论知识](#%E4%B8%80%E3%80%81%E7%90%86%E8%AE%BA%E7%9F%A5%E8%AF%86)

[SVG标签的使用](#SVG%E6%A0%87%E7%AD%BE%E7%9A%84%E4%BD%BF%E7%94%A8)

[二、实战部分](#%E4%BA%8C%E3%80%81%E5%AE%9E%E6%88%98%E9%83%A8%E5%88%86)

---


## 一、理论知识

### SVG标签的使用

代码中的SVG标签和`onload`事件本身并不依赖于其他特定的标签来触发弹窗。无论它们被放置在哪个标签内，只要浏览器解析并加载了这个SVG标签，`onload`事件就会被触发。

注：SVG标签通常是在HTML文档中嵌入使用的，并且可以放置在许多不同的HTML标签内。具体取决于网页的结构和用途。以下是一些常见的情况：

**<u>`&lt;body&gt;`标签：</u>**

SVG标签可以直接放置在`&lt;body&gt;`标签内，这样当整个页面加载完毕时，`onload`事件将触发。

```
&lt;body&gt;
  &lt;svg onload="alert(document.domain)"&gt;
    &lt;!-- SVG内容 --&gt;
  &lt;/svg&gt;
&lt;/body&gt;</code>
</pre>


**<u>`&lt;div&gt;`标签：</u>**
SVG标签可以作为`&lt;div&gt;`标签的子元素，当该`&lt;div&gt;`标签加载完成时，`onload`事件将触发。
<pre><code>&lt;div&gt;
  &lt;svg onload="alert(document.domain)"&gt;
    &lt;!-- SVG内容 --&gt;
  &lt;/svg&gt;
&lt;/div&gt;
```

**<u>`&lt;img&gt;`标签：</u>**

SVG标签也可以作为`&lt;img&gt;`标签的`src`属性值，当图像加载完成时，`onload`事件将触发。

```
&lt;img src="data:image/svg+xml,&lt;svg onload='alert(document.domain)'&gt;"&gt;

```

## 二、实战部分

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[BLACKxZONE/Treasure_knowledge<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)
