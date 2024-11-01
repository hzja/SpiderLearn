# 原创
：  33-5 XXE漏洞 - xxe外部实体注入相关工具

# 33-5 XXE漏洞 - xxe外部实体注入相关工具

##### 1）[xxe.sh || OOB XXE tool](https://www.xxe.sh/)：一个方便的网站，可以输入您的域名并生成OOB XXE PoC。适用于盲注Out-of-band攻击。（主要）

##### 2）[staaldraad/xxeserv](https://github.com/staaldraad/xxeserv?tab=readme-ov-file) ：简化FTP服务器的设置，以通过FTP接收OOB XXE攻击

以下是 `./xxeserv` 命令的使用说明： 

```
Usage of ./xxeserv:
  -o string
        记录日志的文件位置
  -p int
        监听的端口号 (默认为 2121)
  -uno int
        全局监听的端口号 (默认为 5000)
  -w    设置用于DTD的Web服务器
  -wd string
        从中提供DTD(s)的文件夹位置 (默认为 "./")
  -wp int
        用于提供DTD的端口号 (默认为 212
```
