# 原创
：  渗透测试--JWT攻防（一）

# 渗透测试--JWT攻防（一）

### JWT简介

JWT代表**JSON Web Token**，它是一种用于安全地在不同实体之间传递信息的开放标准（RFC 7519）。JWT通常用于身份验证和授权领域，以及在网络应用程序和服务之间传递声明（claims）信息。<br/> JWT的常见用途包括在身份验证流程中生成令牌，将用户信息传递给Web应用程序，以及在不同的服务之间进行身份验证和授权。由于JWT是自包含的，不需要在服务器端存储会话信息，因此它们适用于分布式系统和微服务架构。

### JWT结构

JWT的结构是一个紧凑的、自包含的文本字符串，它由三个部分组成，这些部分使用点号（.）分隔开来，分别是**Header**、**Payload**和**Signature**

#### 1.Header

头部通常包含了关于令牌的元信息，例如使用的加密算法。这部分使用Base64编码，但未加密。header中有两个指定的字段：**alg**和**typ**

```
{
  "alg": "HS256",
  "typ": "JWT"
}

```

**alg**（Algorithm）：指定用于对JWT进行签名的加密算法。在这里，使用了HS256，它代表HMAC SHA-256算法，一种常见的对称加密算法。<br/> **typ**（Type）：指定令牌的类型，通常设置为"JWT"表示这是一个JSON Web Token。

#### 2.Payload

载荷（Payload）：载荷包含了一些声明（claims），这些声明描述了实体（通常是用户）和其他数据。有三种类型的声明：

```
{
  "sub": "1234567890",
  "name": "tuboshusec",
  "iat": 1697790142
}

```

在这个示例中，JWT的载荷部分是一个JSON对象，包含了一些声明（claims）：

#### 3.Signature

签名（Signature）：签名部分用于验证令牌的完整性和真实性。它使用头部中指定的加密算法（如HMAC SHA256或RSA）对头部和载荷部分进行签名，以确保它们在传输过程中未被篡改。

```
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret
)

```

这个示例使用HMAC SHA-256算法生成JWT的签名，其中：

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6InR1Ym9zaHVzZWMiLCJpYXQiOjE2OTc3OTAxNDJ9.f9B4-JRPyMGMiL2syuhuB9k0mZV4mhTN72MZesAn-tQ

```

这是一个完整的JWT，包括头部、载荷和签名部分。JWT的实际用途是在身份验证和授权流程中传递信息，并确保令牌的完整性和真实性。在实际应用中，密钥将用于生成和验证签名部分。可以看到JWT是base64编码的，并不是加密的，所以JWT可以被解密。

### JWT解密

该网站可进行JWT在线加解密<br/> [https://jwt.io/](https://jwt.io/)<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/782f70ae3d30e5bb9476b202ce0d304c.jpeg"/>

### JWT工作原理

#### 生成令牌：

#### 传输和验证令牌：

JWT的工作原理允许在不同服务之间传递身份验证和授权信息，而无需在服务器端存储会话状态。这使得JWT在分布式系统和微服务架构中非常有用。同时，使用正确的安全实践和保护密钥是确保JWT安全性的关键部分。

#### JAVA

在java中JWT库可以很容易实现JWT签名和验证<br/> 使用JWT库要在Maven或Gradle中添加依赖，在Maven中，可以将以下依赖添加到pom.xml文件中：

```
&lt;dependency&gt;
    &lt;groupId&gt;io.jsonwebtoken&lt;/groupId&gt;
    &lt;artifactId&gt;jjwt&lt;/artifactId&gt;
    &lt;version&gt;0.9.1&lt;/version&gt; &lt;!-- 请根据实际情况更新版本 --&gt;
&lt;/dependency&gt;

```

这是一个简单的JWT签名和验证的示例代码:

```
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.Claims;

public class JwtExample {

    // 密钥，实际应用中应该保护好密钥，不要硬编码在代码中
    private static final String SECRET_KEY = "mySecretKey";

    public static void main(String[] args) {
        // 创建JWT
        String jwt = createJWT("1234567890", "John Doe");

        System.out.println("Generated JWT: " + jwt);

        // 验证JWT
        Claims claims = parseJWT(jwt);
        if (claims != null) {
            System.out.println("Subject: " + claims.getSubject());
            System.out.println("Name: " + claims.get("name"));
        } else {
            System.out.println("JWT verification failed.");
        }
    }

    // 创建JWT
    private static String createJWT(String subject, String name) {
        return Jwts.builder()
                .setSubject(subject)
                .claim("name", name)
                .signWith(SignatureAlgorithm.HS256, SECRET_KEY)
                .compact();
    }

    // 验证JWT
    private static Claims parseJWT(String jwt) {
        try {
            return Jwts.parser()
                    .setSigningKey(SECRET_KEY)
                    .parseClaimsJws(jwt)
                    .getBody();
        } catch (Exception e) {
            // 验证失败
            return null;
        }
    }
}

```

在上面的示例代码中使用jwt库进行JWT的签名和验证，首先构建了一个JWT，然后将其分离为Header、Payload和Signature三部分，使用parseClaimsJws函数对JWT进行解析和验证，从而获取其中的Payload中的信息并进行验证.

### JWT攻击思路

#### 一：伪造令牌

我们这里用burpsuite的靶场进行学习：<br/> 靶场地址：[https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature)<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/feca2aba1cd144d46cf6d989f51ba061.jpeg"/><br/> 这是提示，告诉我们要做什么<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/96a560e5f23588276a0c1edab90ac3fb.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/963f3f4323c634a48fb2359b0c7e94de.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/413ebc18e36271ec65de070e6c8c3a52.jpeg"/><br/> 账号密码为wiener/peter<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/22c30fb3c3b03d5d569aafa25c99bb3f.jpeg"/><br/> 登录<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/37182790765b7d17c8f897319ee3bc63.jpeg"/><br/> bp里有这样的数据包<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/00e5a13f4b8ea71817e53bfc34625829.jpeg"/><br/> 可以看到session是一个标准的JWT形式，直接解密看看<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b329b990ac10bca9761765155bb6bfce.jpeg"/><br/> 我们把中间紫色部分即payload部分sub用户改成administrator，然后编码一下替换原版的payload部分，注意编码的时候别有空格哦<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/8402c3a78d2cfe4dac2a4452ca245f3f.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/15866dfd9e159fc57ed7ec2db2ead2da.jpeg"/><br/> 题目要求访问/admin路径<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e330e675dca820556facd9d2c5086c7d.jpeg"/><br/> 有两个删除用户的接口，进行删除操作<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ac4540aabb5e998df039b3244d869feb.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/054143d64229295de2bbf0d061fcbc17.jpeg"/><br/> 删除成功，这道题就是我们利用JWT可以被解密的特性，伪造了administrator用户的JWT，实现从普通用户到administrator权限的一个越权操作。

#### 二：签名用None

靶场地址：<br/> [https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification)<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/cac1c4d4869e1f9984feaa1ea7fc26e6.jpeg"/><br/> 还是一样的要求，要删除carlos用户，和上一题一样的操作，登录进来先<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/1d47bfddc17994e53094de6dd8f644c6.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/996fc116c0e5973abcf6e5e9f57b12d1.jpeg"/><br/> 看似和上题一样的数据包，尝试替换administrator的payload，伪造JWT去请求/admin<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/ca521691a93eeb41d89656291a32540f.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d25793e620e8103153118643a825b88f.jpeg"/><br/> 这里返回了401，这里就是和上一题不一样的地方，解决方法也很简单。去解密一下JWT的第一部分即header部分<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/03503856ca22fd6b971f208c80c08262.jpeg"/><br/> 将alg至为none再进行编码替换<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/9bfd2a82e43fdc6d5d1d5b58b6441ce9.jpeg"/><br/> 再进行一步URL编码<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/06f59eb397a774067c28882e45739a1e.jpeg"/><br/> 此时再替换header，并将SIGNATURE签名去掉，只留下header和payload部分<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/e217a7887feaf2842dfd10476d030e57.jpeg"/><br/> 这时返回200，也返回了删除用户的接口，拿着伪造后的JWT访问接口<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/509d45777f78bbc9c6e95e81fd51b93d.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/6c88134dc4a5dc1f691ca7161bff1110.jpeg"/><br/> 成功通关，这一关是利用了如果"alg"字段设为"None"，则标识不签名，这样一来任何token都是有效的，设定该功能的最初目的是为了方便调试，但是若不在生产环境中关闭该功能，攻击者可以通过将alg字段设置为"None"来伪造他们想要的任何token，接着便可以使用伪造的token冒充任意用户登陆网站

***************未完待续
