# 原创
：  35-3 使用dnslog探测fastjson漏洞

# 35-3 使用dnslog探测fastjson漏洞

环境准备：[35-2 fastjson反序列化漏洞介绍 及漏洞环境搭建-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/137605174) 

#### 一、DNSLog 原理

        DNSLog是一种记录在DNS上的域名相关信息的机制，类似于日志文件，记录了对域名或IP的访问信息。了解多级域名的概念对理解DNSLog至关重要。因特网采用树状结构的命名方法，按照组织结构划分域，每个域都是名字空间中被管理的一个划分，可以进一步划分为子域。域名可以被分为多级，如一级域名、二级域名、三级域名等。从右到左，域名地址依次是顶级域名、二级域名、三级域名。

        举例来说，假设有一个域名kxsy.work，将其解析设置为对应的IP地址2.2.2.2。当向DNS服务器发起kxsy.work的解析请求时，DNSLog会记录下此次解析，包括解析的域名和对应的IP地址。我们可以利用这些记录来进行漏洞测试，这个过程就是DNSLog。

#### 二、在线的 DNSLog 平台

之前的文章有讲过这两个平台的使用这里就不多说了

####  三、利用 dnslog 测试是否有漏洞

**payloa**
