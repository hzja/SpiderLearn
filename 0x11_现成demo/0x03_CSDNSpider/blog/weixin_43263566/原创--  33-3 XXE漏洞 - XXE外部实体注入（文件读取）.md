# 原创
：  33-3 XXE漏洞 - XXE外部实体注入（文件读取）

# 33-3 XXE漏洞 - XXE外部实体注入（文件读取）

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

#### 实验一：文件读取

 <img alt="" height="589" src="https://img-blog.csdnimg.cn/direct/1b60d94395274907ab4ed63d4f6f4a51.png" width="1121"/>

传入一个xml代码，自己构造个标签如：&lt;ff&gt;hello world&lt;/ff&gt;

 上一篇文章我就有介绍过如果我们要进行文件读取就可以利用file协议

##### 利用内部实体进行输入

###### 构造 payload 
