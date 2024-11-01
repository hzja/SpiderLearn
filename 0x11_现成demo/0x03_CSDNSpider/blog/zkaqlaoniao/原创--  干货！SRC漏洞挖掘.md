# 原创
：  干货！SRC漏洞挖掘

# 干货！SRC漏洞挖掘

**目录**

[一、hunter上搜索web.title=”nacos”，查找中国境内的资产，定位到两个地址。](#%E4%B8%80%E3%80%81hunter%E4%B8%8A%E6%90%9C%E7%B4%A2web.title%3D%E2%80%9Dnacos%E2%80%9D%EF%BC%8C%E6%9F%A5%E6%89%BE%E4%B8%AD%E5%9B%BD%E5%A2%83%E5%86%85%E7%9A%84%E8%B5%84%E4%BA%A7%EF%BC%8C%E5%AE%9A%E4%BD%8D%E5%88%B0%E4%B8%A4%E4%B8%AA%E5%9C%B0%E5%9D%80%E3%80%82)

[二、访问一下8086端口，界面很明显是nacos，直接抓包，创建用户。](#%E4%BA%8C%E3%80%81%E8%AE%BF%E9%97%AE%E4%B8%80%E4%B8%8B8086%E7%AB%AF%E5%8F%A3%EF%BC%8C%E7%95%8C%E9%9D%A2%E5%BE%88%E6%98%8E%E6%98%BE%E6%98%AFnacos%EF%BC%8C%E7%9B%B4%E6%8E%A5%E6%8A%93%E5%8C%85%EF%BC%8C%E5%88%9B%E5%BB%BA%E7%94%A8%E6%88%B7%E3%80%82)

[三、登录网站，里面看到配置管理。](#%E4%B8%89%E3%80%81%E7%99%BB%E5%BD%95%E7%BD%91%E7%AB%99%EF%BC%8C%E9%87%8C%E9%9D%A2%E7%9C%8B%E5%88%B0%E9%85%8D%E7%BD%AE%E7%AE%A1%E7%90%86%E3%80%82)

[四、查看下redis.yml的详情。](#%E5%9B%9B%E3%80%81%E6%9F%A5%E7%9C%8B%E4%B8%8Bredis.yml%E7%9A%84%E8%AF%A6%E6%83%85%E3%80%82)

[五、查看mysql.yml的详情。](#%E4%BA%94%E3%80%81%E6%9F%A5%E7%9C%8Bmysql.yml%E7%9A%84%E8%AF%A6%E6%83%85%E3%80%82)

[六、跟第一个网站一样，创建用户登录。](#%E5%85%AD%E3%80%81%E8%B7%9F%E7%AC%AC%E4%B8%80%E4%B8%AA%E7%BD%91%E7%AB%99%E4%B8%80%E6%A0%B7%EF%BC%8C%E5%88%9B%E5%BB%BA%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E3%80%82)

---


前言：第一次挖到洞，有点小激动。因为前几天刚做过nacos未授权访问的靶场，所以今天心血来潮去搜索了一下相关资产，没想到还真找到了。

### 一、hunter上搜索web.title=”nacos”，查找中国境内的资产，定位到两个地址。

以下是第一个网站的测试

### 二、访问一下8086端口，界面很明显是nacos，直接抓包，创建用户。

### 三、登录网站，里面看到配置管理。

### 四、查看下redis.yml的详情。

<br/> 里面泄露出了主机地址，端口号和密码。

### 五、查看mysql.yml的详情。

<br/> 泄漏出了数据库的连接地址，用户名和密码。

以下是第二个网站的测试

### 六、跟第一个网站一样，创建用户登录。

<br/> 这里面的资产就更多了，还有很多云资产，喔嚯。<br/>  

附言：终于有进度了，继续加油

**没看够~？欢迎关注！**

** **<img alt="" height="567" src="https://img-blog.csdnimg.cn/d89b5fd1e8b24bb0a88152b3995f9ebd.jpeg" width="1015"/>

 渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/f333a24647774be5b99b00fb7019d620.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/3e579b7d7a164889a57771c035775069.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/a601ca2e0eb040bd911477a4f54fef8e.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/04beeeb6757b422a83ca0900a349a544.png" width="665"/>
