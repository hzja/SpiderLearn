# 原创
：  37-3 编写 Python 脚本以生成特定的 RCE 漏洞证明-of-concept（PoC），针对 Struts2 漏洞 S2-057

# 37-3 编写 Python 脚本以生成特定的 RCE 漏洞证明-of-concept（PoC），针对 Struts2 漏洞 S2-057

环境准备：[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187) 

#### 一、搭建 Struts2 漏洞漏洞环境

非常感谢大佬分享的文章！我花了两天时间在 Vulhub 中按照老师的指导成功搭建了这个靶场，但在测试过程中未发现漏洞。尽管我尝试了很多在网上找到的教程，它们都是基于相同的原理，但依然无法触发漏洞。最终，我终于找到了大佬分享的文章，问题成功解决。这篇文章对我来说真是及时雨，非常感谢！链接在此：[https://www.cnblogs.com/NBeveryday/p/9525654.html](https://www.cnblogs.com/NBeveryday/p/9525654.html)

```
# 从 Docker Hub 上拉取 medicean/vulapps:s_struts2_s2-057 镜像
docker pull medicean/vulapps:s_struts2_s2-057

# 在后台运行一个容器，并将容器的 8080 端口映射到主机的 8083 端口上
docker run -d -p 8083:8080 medicean/vulapps:s_struts2_s2-057

# 关闭防火墙（如果有的话）
systemctl stop firewalld
```
