# 原创
：  14-2 tomcat反序列化

# 14-2 tomcat反序列化

#### 漏洞介绍：

**漏洞名称：**

**影响范围：**

**漏洞描述：**

Apache Tomcat是一个基于Java的Web应用软件容器，用于运行servlet和JSP Web应用。当Tomcat使用了自带session同步功能时，并且未配置安全设置（缺少Encrypt Interceptor加密拦截器），存在反序列化漏洞。攻击者可以通过构造精心设计的数据包来利用这个漏洞，对使用了自带session同步功能的Tomcat服务器进行攻击。

**攻击方式：**

攻击者构造恶意的序列化数据包，然后将其发送给目标Tomcat服务器。当服务器尝试解析并反序列化该数据包时，攻击者可以利用漏洞执行任意代码，从而进一步攻击服务器。

**漏洞利用条件：**

1. 攻击者能够控制服务器上文件的内容和文件名称。
1. 服务器的PersistenceManager配置中使用了Filestore（文件存储）。
1. PersistenceManager中的sessionAttributeValueClassNameFilter被配置为"null"，或者过滤器设置不严格，允许攻击者提供反序列化数据的对象。
1. 攻击者知道使用的Filestore存储位置，并且可以控制文件的相对路径。

** 影响范围**
