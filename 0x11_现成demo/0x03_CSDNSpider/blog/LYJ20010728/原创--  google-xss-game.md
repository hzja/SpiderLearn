# 原创
：  google-xss-game

# google-xss-game

[题目链接](https://xss-game.appspot.com/)<br/> **level1-未过滤的字符串输入**<br/> 没有任何过滤，最基本的操作：`&lt;script&gt;alert(1)&lt;/script&gt;`<br/> **level2-服务端存储漏洞**<br/> 查看网页源码，我们在用户字段输入的文字被外部标签`&lt;blockquote&gt;`标签包裹，尝试level1中的操作，发现无法弹窗。在`&lt;script&gt;`标签无法触发的时候，尝试用另一个标记来触发javascript，考虑到数据是永久存储在对方服务器上的，所以可以这样输入：`&lt;img src="x" onerror="javascript:alert(1)"/&gt;`，成功触发弹窗<br/> **level3-隐藏的未过滤字段**<br/> 查看网页的源码，发现图片的加载实际上是由window.location.hash决定的，它决定包括#号和它后面跟的东西。利用`'&gt;&lt;script&gt;alert(1);&lt;/script&gt;`进行绕过(替换#后面跟的东西)<br/> **level4-就近原则绕过检查**<br/> 首先分析网页主体元素，当在输入栏输入某个秒数后，观察url的变化。尝试alert弹窗，再次观看url地址栏的变化,地址栏直接输出了，但是奇怪的是下面的计时器脚本仍然被执行了，想到应该是设置了默认值。查看网页源码，看名识代码，这个函数和计时器息息相关。看到了确实有个默认值等于3秒，这就是之前直接alert弹窗失败的原因。尝试`1');alert('1`，成功触发弹窗<br/> **level5-逃脱过滤字符**<br/> 发现&lt; a href&gt;标签，这种payload直接java伪协议，然后点击触发`javascript:alert(1)`，成功触发弹窗<br/> **level6-针对动态JavaScript加载**<br/> 利用data伪协议：`data:text/plain,alert('xss')`
