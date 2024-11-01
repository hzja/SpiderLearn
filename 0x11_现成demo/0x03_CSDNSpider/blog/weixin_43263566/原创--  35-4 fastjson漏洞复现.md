# 原创
：  35-4 fastjson漏洞复现

# 35-4 fastjson漏洞复现

 环境准备：[35-2 fastjson反序列化漏洞介绍 及漏洞环境搭建-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/137605174) 

fastjson_tool.jar下载：[fastjson_rce_tool: fastjson命令执行自动化利用工具， remote code execute，JNDI服务利用工具 RMI/LDAP (gitee.com)](https://gitee.com/zhao-yuanadmin/fastjson_rce_tool?_from=gitee_search)

#### 一、攻击机kali开启nc监听6666端口（或其他端口也行，只要不重复就行）

```
nc -lvvp 6666
```

具体解释如下：
