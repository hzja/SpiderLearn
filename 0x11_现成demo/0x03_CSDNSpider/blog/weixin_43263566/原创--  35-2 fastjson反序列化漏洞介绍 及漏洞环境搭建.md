# 原创
：  35-2 fastjson反序列化漏洞介绍 及漏洞环境搭建

# 35-2 fastjson反序列化漏洞介绍 及漏洞环境搭建

#### **一、Fastjson 简介：**

        Fastjson 是一个用于 Java 的库，用于实现 Java 对象与 JSON 格式之间的相互转换。它不仅能够将 Java 对象转换为 JSON 字符串，还能够将 JSON 字符串转换为 Java 对象。与此同时，Fastjson 还具备操作任何 Java 对象的能力，即使是一些没有源码的预先存在的对象。

#### **二、Fastjson 漏洞原理：**

        Fastjson 提供了 autotype 功能，允许用户在反序列化数据中通过 `@type` 指定反序列化的类型。其次，Fastjson 的自定义反序列化机制会调用指定类中的 setter 方法及部分 getter 方法。因此，当组件开启了 autotype 功能，并且反序列化不可信数据时，攻击者可以构造数据，使目标应用的代码执行流程进入特定类的特定 setter 或 getter 方法中。若指定类的指定方法中存在可被恶意利用的逻辑，则可能导致严重的安全问题。

#### 三、漏洞靶场搭建

 搭建 vmihub 靶场：[vulhub靶场搭建与使用_剁椒鱼头没剁椒的博客-CSDN博客](https://blog.csdn.net/weixin_44268918/article/details/128055553)

**运行 **

```
# 这里要改成自己的 /vulhub-master 存放目录
cd ./vulhub/vulhub/fastjson/1.2.47-rce
 
# 关闭防火墙（如果有的话）
```
