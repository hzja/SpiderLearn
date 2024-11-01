# 原创
：  【SpringBlade-权限缺陷】API鉴权逻辑缺陷漏洞

# 【SpringBlade-权限缺陷】API鉴权逻辑缺陷漏洞

**目录**

[一、理论部分](#%E4%B8%80%E3%80%81%E7%90%86%E8%AE%BA%E9%83%A8%E5%88%86)

[简介](#%E7%AE%80%E4%BB%8B)

[如何通过认证](#%E5%A6%82%E4%BD%95%E9%80%9A%E8%BF%87%E8%AE%A4%E8%AF%81)

[API 鉴权](#API%20%E9%89%B4%E6%9D%83)

[配置API放行](#%E9%85%8D%E7%BD%AEAPI%E6%94%BE%E8%A1%8C)

[细颗粒度鉴权配置](#%E7%BB%86%E9%A2%97%E7%B2%92%E5%BA%A6%E9%89%B4%E6%9D%83%E9%85%8D%E7%BD%AE)

[结尾](#%E7%BB%93%E5%B0%BE)

[二、实战部分](#%E4%BA%8C%E3%80%81%E5%AE%9E%E6%88%98%E9%83%A8%E5%88%86)

---


## 一、理论部分

### 简介

---


---


### 如何通过认证
1. 首先需要访问Auth接口，传入账号名密码，获得授权成功后的信息1. 启动`AuthApplication`、`UserApplication`、 `BladeLogApplication`三个服务<img alt="" height="186" src="https://img-blog.csdnimg.cn/67a760ebb79f4cf58231af93c6f1ffc4.png" width="379"/>1. 调用 [http://localhost/blade-auth/token](http://localhost/blade-auth/token) 传入对应参数，如下图所示则说明认证信息获取成功<br/>`（"c3dvcmQ6c3dvcmRfc2VjcmV0"为clientId:clientSecret串转换为的base64编码,这个是可变的）`  
4.从返回的Json中取到 `tokenType` 和 `accessToken`，将他们拼接起来并以逗号隔开

5.设置请求头为`blade-auth`，请求头对应的值为 `tokenType` + `' '` + `accessToken` (后续的所有接口调用都需要带上请求头为 `Authorization` 值为 `c3dvcmQ6c3dvcmRfc2VjcmV0`)

6.再次调用 [http://localhost/blade-demo/api/info?name=Chill](http://localhost/blade-demo/api/info?name=Chill) 发现返回 `Hello, My Name Is: Chill` 说明鉴权成功！

7.理论上看，所有业务API，都需要进行鉴权，这样才能保证整个系统的安全性，但也有个别特例情况，API 不需要认证也可以调用，这里就需要用到 Secure 的 API 放行配置。

8.有些业务 API 鉴权就算成功，也有可能需要根据角色权限来判断是否可以调用，这里就需要用到 Secure更细颗粒度的鉴权配置。

<u>扩展：密码可能会进行二次加密</u>

 如这一个admin就是md5加密后

将得到的Authorization、Blade-Auth填入

（请求参数Params中填name:vulue即可）

---


---


### API 鉴权

#### 配置API放行
1. 若是使用SpringBoot版本，前往对应配置文件，增加接口放行配置
2.若是使用SpringCloud，则打开nacos，找到对应配置文件增加接口放行配置

3.若需要拦截某个api下所有的请求，则可以改为 `/api/**`， 其中 `**` 则代表下层所有请求

4.重启工程，去掉请求头，可以看到，请求成功了，说明 `API 放行` 配置成功

---


---


#### 细颗粒度鉴权配置
1. 鉴权配置用到了 Secure 模块的 `@PreAuth` 注解1. 为了可以起到对比的作用，对 `count` 进行权限放行（只要通过Token认证就可调用API）。
```
@GetMapping("count")
@PreAuth("permitAll()")
public Integer count(Integer cnt) {
   return cnt * 10;
}

```

        3.对 `info`进行权限判断，调用方需要拥有`test`的角色权限才可以调用

```
@GetMapping("info")
@PreAuth("hasRole('test')")
public String info(String name) {
   return "Hello, My Name Is: " + name;
}

```

4.调用 `/api/count` 发现请求成功。

5.调用 `/api/info` 发现又变回了 `请求未授权`，因为我们的`admin`账号没有分配`test`角色

6.尝试改回`admin`权限

```
@GetMapping("info")
@PreAuth("hasRole('administrator')")
public String info(String name) {
   return "Hello, My Name Is: " + name;
}

```

7.调用 `/api/info` 发现请求成功。

---


---


### 结尾

<br/>  

## 二、实战部分

[README.md · 书半生/网络安全知识体系-实战中心 - 码云 - 开源中国 (gitee.com)<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md](https://gitee.com/shubansheng/Treasure_knowledge/blob/master/README.md)

[GitHub - BLACKxZONE/Treasure_knowledge<img alt="icon-default.png?t=N5K3" src="https://csdnimg.cn/release/blog_editor_html/release2.3.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N5K3"/>https://github.com/BLACKxZONE/Treasure_knowledge](https://github.com/BLACKxZONE/Treasure_knowledge)

 更多请参考springBlade开发手册：

[https://www.kancloud.cn/smallchill/blade/](https://www.kancloud.cn/smallchill/blade/913236)
