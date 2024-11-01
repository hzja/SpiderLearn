# 原创
：  记一次有趣的tp5代码执行

# 记一次有趣的tp5代码执行

**目录**

[0x00 前言](#toc-0)

[0x01 基础信息](#toc-1)

[0x02 突破](#toc-2)

[base64编码与php://filter伪协议](#toc-3)

[tp 5 method代码执行的细节](#toc-4)

[0x03 总结](#toc-5)

[免费领取安全学习资料包！（私聊进群一起学习，共同进步）​编辑](#%E5%85%8D%E8%B4%B9%E9%A2%86%E5%8F%96%E5%AE%89%E5%85%A8%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99%E5%8C%85%EF%BC%81%EF%BC%88%E7%A7%81%E8%81%8A%E8%BF%9B%E7%BE%A4%E4%B8%80%E8%B5%B7%E5%AD%A6%E4%B9%A0%EF%BC%8C%E5%85%B1%E5%90%8C%E8%BF%9B%E6%AD%A5%EF%BC%89%E2%80%8B%E7%BC%96%E8%BE%91)

---


### 0x00 前言

朋友之前给了个站，拿了很久终于拿下，简单记录一下。

### 0x01 基础信息

### 0x02 突破

现在tp 5 method代码执行开发出来的一些思路，不外乎如下两种：

1，写日志，包含日志 getshell 。payload如下：

2，写session，包含session getshell。payload如下：

而这两种方式在这里都不可用，因为waf对`&lt;?php`等关键字进行了拦截，还有其他办法吗？

#### base64编码与php://filter伪协议

倘若能够对关键字进行变形或者编码就好了，比如base64编码:

假如我们的session 文件为`/tmp/sess_kking`，内容如下

因为最终的利用是通过`inlcude`方法进行包含，其实很容易想到可以利用`php://filter/read=convert.base64-decode/resource=/tmp/sess_kking`的方式进行解码

最终执行类似如下：

但是session里面是会有其他字符的

如何让`php://filter`正确的解码呢?<br/> p神的[谈一谈php://filter的妙用](https://www.leavesongs.com/PENETRATION/php-filter-magic.html)文章有谈到如何巧妙用`php://filter`与`base64`编码绕过死亡`exit`

那么这里也一样，我们只要构造合适的字符，使得我们的webshell能够正确被base64解码即可。

本地测试

第一步，设置session

(注意：这里的+号需要用`urlencode`编码为%2b，不然会在写入`session`的时候被urldecode为空格，导致编码解码失败)。

疑问点1：为什么不用`PD9waHAgQGV2YWwoJF9HRVRbJ3InXSk7Pz4= (&lt;?php @eval($_GET['r']);?&gt;)`而是`PD9waHAgQGV2YWwoJF9HRVRbJ3InXSk7Oz8+ (&lt;?php @eval($_GET['r']);;?&gt;)` 呢，

答：是因为直接使用前者无论怎么拼凑字符，都没法正常解码。

疑问点2：为什么`payload`前后会有两个`ab`？

答：是为了让`shell payload` 的前后两串字符串满足base64解码的长度，使其能正常解码。

第二步，包含，成功执行代码：

本地测试如此，但是在目标测试会发现执行不了，因为我们的payload使用了`php://filter`的协议包含了`php://`关键字

怎么让才能让其没有关键字呢？

#### tp 5 method代码执行的细节

让我们仔细观察代码执行的`Request.php`的`filterValue`方法是如何执行代码的。

我们注意到`filter`其实是可以传递多个的，同时参数为参数引用。

那么其实我们就可以传递多个`filter`来对`value`进行多次传递处理。如先`base64_decode`后将解码后的值传递给`include`进行包含。

但在线上这个waf是对`base64_decode`这个函数进行了过滤的，经过测试发现可以使用`strrev`反转函数突破。考虑到waf的问题，我们使用的`shell payload`加多一层base64编码。

同样道理这里的payload为什么要多几个分号就不需要再解释了

回到我们的`getshell`步骤，在目标上执行

1，设置`session`：

(`payload`前后两个`ab`同样是为了`base64`解码凑字符的原因)

2，文件包含

最终成功绕过防火墙`getshell`。

### 0x03 总结

总的来说挺有趣的，搞了很久，最终成功`getshell`也是非常的爽。（好在没放弃：）<br/> 不妥之处，烦请指出~

## **免费领取安全学习资料包！（私聊进群一起学习，共同进步）**<img alt="" height="768" src="https://img-blog.csdnimg.cn/8462eeecfe8c4816b8a09a92a423a812.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/68782e85fc394fae9907be94ab5bfc90.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/02fb390c760945fbba1a0453dd793bbd.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/f306a7a13f234b4a9454d8c0ea0a2d92.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/5f739586d9f74927bd439876029b617b.png" width="665"/>

应急响应笔记

学习路线
