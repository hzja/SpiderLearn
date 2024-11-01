# 原创
：  33-1 XXE漏洞 - DTD

# 33-1 XXE漏洞 - DTD

#### **一、定义：**

DTD全称为文档类型定义（Document Type Definition），它允许定义合法的XML文档结构。通过一系列合法的元素来描述文档的结构。DTD可以直接嵌入到XML文档中声明，也可以作为外部引用使用。

#### **二、分类：**

##### **1) 内部DTD**

内部DTD是直接嵌入到XML文档中的DTD声明。

**语法：**

```
&lt;!DOCTYPE 内部实体名称(根元素名称) [
  元素声明
]&gt;
```

内部DTD将DTD的声明和实体定义包含在XML文档内部，使得XML文档完全自包含。

示例：

```
&lt;!-- XML声明，它指定了XML版本 --&gt;
&lt;?xml version="1.0"?&gt;
&lt;!-- 文档类型声明（DOCTYPE）,DOCTYPE声明可以引用外部DTD文件，也可以内联DTD定义文档的结构。 --&gt;
&lt;!DOCTYPE note [
    &lt;!-- 定义note元素及其子元素 --&gt;
    &lt;!ELEMENT note (to, from, heading, body)&gt;
    &lt;!-- 定义to元素，其内容为文本数据 --&gt;
    &lt;!ELEMENT to (#PCDATA)&gt;
    &lt;!-- 定义from元素，其内容为文本数据 --&gt;
    &lt;!ELEMENT from (#PCDATA)&gt;
   
```
