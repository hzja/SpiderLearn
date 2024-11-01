# 原创
：  26-4 SQL注入攻击 - 不同数据库系统利用dnslog姿势

# 26-4 SQL注入攻击 - 不同数据库系统利用dnslog姿势

 环境准备：[SQL注入攻击 - SQL注入无回显，盲注又被封怎么办？-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/136631963) <br/><br/>[构建完善的安全渗透测试环境：推荐工具、资源和下载链接_渗透测试靶机下载-CSDN博客](https://blog.csdn.net/weixin_43263566/article/details/129031187)

#### 一、MySQL

在 MySQL 数据库管理系统中，可以利用 `load_file` 函数来执行文件读取操作，并通过注入恶意代码来触发 DNS 解析以传输数据到 DNSLog 平台。以下是针对 Windows 操作系统中 MySQL 的示例：

<li> 需要设置 `secure_file_priv` 为空：
</li>
<li> 使用 `load_file` 函数注入恶意代码：
</li>
