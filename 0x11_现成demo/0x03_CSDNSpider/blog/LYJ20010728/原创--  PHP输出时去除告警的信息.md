# 原创
：  PHP输出时去除告警的信息

# PHP输出时去除告警的信息

> 
有时候在PHP代码运行时总会遇到告警的提示显得很难受<br/> 我们只需要在对应执行的代码中加入


```
error_reporting(E_ALL^E_NOTICE^E_WARNING);

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210528182822499.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210528182828626.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
