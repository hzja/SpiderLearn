# 原创
：  19-4 burpsuite 爆破

# 19-4 burpsuite 爆破

**靶场搭建：**[phpstudy的安装与靶场搭建 - junlin623 - 博客园 (cnblogs.com)](https://www.cnblogs.com/junlin623/p/17202920.html)

**账号字典：**[XXTK: 一些弱口令、fuzz字典 (gitee.com)](https://gitee.com/jjhoc/XXTK?_from=gitee_search)

网盘链接：https://pan.baidu.com/s/1v5pAwaTwoeCnJgkUXf3iLQ?pwd=mllm <br/> 提取码：mllm <br/> --来自百度网盘超级会员V2的分享 

### 一、暴力破解 - 基于表单的暴力破解

#### 1）先抓包

在bp中找到登录请求

 <img alt="" height="724" src="https://img-blog.csdnimg.cn/direct/9eb452f16ee44f4abf9d36cececdeac8.png" width="1011"/>

#### 2）设置爆破变量
