# 原创
：  38-4 Web应用防火墙 - WAF的使用及规则

# 38-4 Web应用防火墙 - WAF的使用及规则

准备：[38-3 Web应用防火墙 - 安装配置WAF-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/138380584)

#### WAF的使用

**启动 Nginx**

```
/usr/local/nginx/sbin/nginx
```

为了测试未启动 ModSecurity 时的访问效果，我们可以模拟攻击。要查看当前虚拟机的 IP 地址，可以使用命令 `ifconfig`

浏览器中访问ip，如果要在真实机中访问就需要关闭防火墙

```
systemctl stop firewalld
```

<img alt="" height="530" src="https://img-blog.csdnimg.cn/direct/0164f28016814c1d82dd780b4639632d.png" width="952"/>**测试waf 未拦截效果**

```
/?param=%22/%3E%3C/script%3E%3Cscript
```
