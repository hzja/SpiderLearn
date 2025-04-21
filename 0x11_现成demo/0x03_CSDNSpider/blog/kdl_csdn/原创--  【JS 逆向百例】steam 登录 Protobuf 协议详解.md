# 原创
：  【JS 逆向百例】steam 登录 Protobuf 协议详解

# 【JS 逆向百例】steam 登录 Protobuf 协议详解

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 目标

目标：steam 登录协议逆向分析

网址：`aHR0cHM6Ly9zdG9yZS5zdGVhbXBvd2VyZWQuY29tL2xvZ2luLw==`

### 逆向分析

输入账密后点击登录，首先看接口 `GetPasswordRSAPublicKey/v1`，看接口命名可以了解到这个这个接口应该是返回 `RSA` 加密的公钥信息，先不管这些，观察参数 ，很明显加密参数为 `input_protobuf_encoded` ：

这里直接全局搜索，可以定位到两处：

可以看到 `input_protobuf_encoded` 的值为 `a` ，而 `a` 的值为 `r.JQ(o)` ：

先看参数 `o` 的值，为 `n.SerializeBody()` ，其中 `n` 是一个对象，包含我们输入的账号信息：

这里 `n` 是一个实例对象，这里可以直接通过原型进到它的构造函数中：

进到构造函数中后，在 `super` 位置下断：

可以发现实例化的时候传了一个类：

进到这个类 `c` 中，这里需要清下缓存重新下断：

这里可以看到，在初始化的时候，会检查当前实例的 `account_name` 属性，很明显这个是有关于账号的属性，如果不存在（这里可以理解为首次实例化）则会调用 ` c.M()` 方法创建一个对象，格式如下：

```
{
    proto: c,
    fields: {
        account_name: {
            n: 1,
            br: n.FE.readString,
            bw: n.Xc.writeString
        }
    }
}

```

到这里无论是从 `n.aR` 方法入手，还是从 `account_name` 的几个属性以及这几个类统一的父类 `o`入手，都会进入到一个新的文件中，到这就可以引出本期的主角 `protobuf` 协议了：

### Protocol Buffers

从第一点可以了解到， `protobuf` 协议根据特定的语法来定义数据结构。我们发送数据以及接收数据都需要讲数据字段约定好才能进行生成与解析。

### 字段定义

初步了解 `protobuf` 协议后就能理解上文中的代码了，上文中的类正是对 `account_name` 字段进行定义。

那么我们就可以根据 `JS` 代码中的格式来编写我们自己的 `proto` 文件：

```
account_name: {
    n: 1,
    br: n.FE.readString,
    bw: n.Xc.writeString
}

```

`protobuf ` 常见的数据类型有以下几种：

|**数据类型**|**描述**
|------
|`int32`|`int64`
|`uint32 `|`uint64`
|`sint32 `|`sint64`
|`fixed32 `|`fixed64`
|`sfixed32 `|`sfixed64`
|`float`|单精度浮点数
|`double`|双精度浮点数
|`bool`|布尔值
|`string`|字符串
|`bytes`|二进制数据
|`enum`|枚举类型，表示一组命名整数值
|`message`|消息类型，可以包含其他数据类型的字段，用于嵌套结构
|`map`|映射类型，用于定义键值对的映射关系
|`Any`|用于包装任意类型的消息
|`repeated`|表示一个字段可以包含多个值，类似于数组或列表
|`Timestamp`|表示时间戳，用于表示一个特定时间点
|`Duration`|表示时间间隔，用于表示一段时间的持续
|`Struct`|`Value`

除了上述数据类型，还支持自定义类型。

这里我们新建一个 `proto` 文件（需配置环境），定义 `account_name` 字段：

```
syntax = "proto3";

message CAuthenticationGetPasswordRsaPublicKeyRequest {
    string account_name = 1;
}

```

执行命令 `protoc --python_out=. xx.proto` 将 `proto` 文件转为 `python` 代码。

转成的 `py` 文件格式如下：

使用起来也很简单：

```
from loguru import logger

from steam_pb2 import (
    CAuthenticationGetPasswordRsaPublicKeyRequest
)


def get_rsa_public_key(username):
    message = CAuthenticationGetPasswordRsaPublicKeyRequest(
        account_name=username
    )
    logger.info(message.SerializeToString())
    logger.info(type(message))


if __name__ == '__main__':
    get_rsa_public_key("a123456789")
"""
OUTPUT:
b'\n\na123456789'
&lt;class 'steam_pb2.CAuthenticationGetPasswordRsaPublicKeyRequest'&gt;
"""

```

那么回到逆向流程中，我们已经知道了 `o` 的生成方式，那么还剩 `r.JQ` 方法，这里很简单，直接扣下来即可，根据经验也可以看出这是 `base64` 编码：

```
o = n.SerializeBody()
a = r.JQ(o);

```

到这就生成了 `input_protobuf_encoded` 的值，那么还需要解决接口返回值。

### 响应信息解析

这里推荐下 `xhr` 断点，断在请求发送的地方。一路往下跟直到看到响应信息解析的地方：

这里 `l.data` 就是响应信息，`u.At` 主要就是对响应信息格式进行处理，并且声明一些方法，做一些读写操作等。`s.BinaryReader` 也是类似，都是对响应信息做了一些预处理。

关键看 `r.deserializeBinaryFromReader` ，单步跟，会进入到一个 `MBF` 静态方法中：

这个很像上文中类 `c` 构造方法中的一段代码，都是判断 `protobuf` 数据格式是否定义，如果没有定义的话会进行定义，那么这里与上文也一样，进到 `l.M()` 中就可以看到定义的字段：

```
static M() {
    return l.sm_m || (l.sm_m = {
        proto: l,
        fields: {
            publickey_mod: {
                n: 1,
                br: n.FE.readString,
                bw: n.Xc.writeString
            	},
            publickey_exp: {
                n: 2,
                br: n.FE.readString,
                bw: n.Xc.writeString
           	 	},
            timestamp: {
                n: 3,
                br: n.FE.readUint64String,
                bw: n.Xc.writeUint64String
               }
            }
        }),
    l.sm_m
    }

```

那么又显而易见了，按照 `JS` 代码中的字段与类型进行定义即可：

```
message CAuthenticationGetPasswordRsaPublicKeyResponse {
    string publickey_mod = 1;
    string publickey_exp = 2;
    uint64 timestamp = 3;
}

```

完整请求代码：

```
import base64
import requests

from steam_pb2 import (
    CAuthenticationGetPasswordRsaPublicKeyRequest,
    CAuthenticationGetPasswordRsaPublicKeyResponse
)

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def get_rsa_public_key(username):
    origin = 'https://steamcommunity.com'
    message = CAuthenticationGetPasswordRsaPublicKeyRequest(
        account_name=username
    )
    protobuf = base64.b64encode(message.SerializeToString()).decode()
    url = f'https://api.steampowered.com/IAuthenticationService/GetPasswordRSAPublicKey/v1'
    params = {
        "origin": origin,
        "input_protobuf_encoded": protobuf
    }

    response = requests.get(url, params=params, headers=headers, timeout=3)
    # 解析响应信息
    response = CAuthenticationGetPasswordRsaPublicKeyResponse.FromString(response.content)
    print(response)


if __name__ == '__main__':
    get_rsa_public_key("a123456789")
"""
OUTPUT:
publickey_mod: "a2fdc8f523c87c6c27e904c89c91ecb56c1199dfcfa2c0fc34c4977c3582aa0f49a3f8fe33cffbd780cc71cfc61d3b7a6f98efc8a14d21174792ef47a8e0b8a6a21c35271ebe384196e60d5d26f010e2539db9b8112873e2bfd08fe73d27f0f15457028ad5da27db4fffb4e17702191f1a7d7f96e60d172835333fea40daf707b38e2030f143b518173453bb5c9e9bf1cbe946e2b4b00d037c9691c2ae9608c4f63263306663f2d8066674d870eb2f142e7c9819416d0499cdc1cc76d47b689ae753648a29cd4d82f6c8f18374ab38c6cb2338652ef5214d620e986e8e7c399e4ef6739485eaccd8cea56d14d61dcd7e8e4f51be82803cea77c7be522e2cfebd"
publickey_exp: "010001"
timestamp: 127222000000
"""

```

到这里第一个接口的请求参数与响应信息我们就都搞定了，这里返回了三个参数：`publickey_mod` ，`publickey_exp`，`timestamp`，很明显是用于进行 `RSA` 加密的，那么看下一个接口：

这个接口为登录接口，会返回账号的登录结果信息。该接口参数只有一个 `input_protobuf_encoded`，那么依旧在老地方下断，根据 `t` 值来判断接口：

那么还是一样的操作，找到约定字段的地方进行改写：

```
fields: {
    device_friendly_name: {
        n: 1,
        br: n.FE.readString,
        bw: n.Xc.writeString
    },
    account_name: {
        n: 2,
        br: n.FE.readString,
        bw: n.Xc.writeString
    },
    encrypted_password: {
        n: 3,
        br: n.FE.readString,
        bw: n.Xc.writeString
    },
    encryption_timestamp: {
        n: 4,
        br: n.FE.readUint64String,
        bw: n.Xc.writeUint64String
    },
    remember_login: {
        n: 5,
        br: n.FE.readBool,
        bw: n.Xc.writeBool
    },
    platform_type: {
        n: 6,
        br: n.FE.readEnum,
        bw: n.Xc.writeEnum
    },
    persistence: {
        n: 7,
        d: 1,
        br: n.FE.readEnum,
        bw: n.Xc.writeEnum
    },
    website_id: {
        n: 8,
        d: "Unknown",
        br: n.FE.readString,
        bw: n.Xc.writeString
    },
    device_details: {
        n: 9,
        c: u
    },
    guard_data: {
        n: 10,
        br: n.FE.readString,
        bw: n.Xc.writeString
    },
    language: {
        n: 11,
        br: n.FE.readUint32,
        bw: n.Xc.writeUint32
    },
    qos_level: {
        n: 12,
        d: 2,
        br: n.FE.readInt32,
        bw: n.Xc.writeInt32
    }
}

```

这里需要注意的是 `device_details` ，可以看到这里这个字段并没有声明类型，这种就属于自定义类型，`u` 就是它的类型：

结构定义好后可以继续往下跟，找到传输的数据字段：

这里密码是被加密过的，加密方法为 `h.IC(a, t)`，这里根据上一个接口的明文规范可以直接推断出为 `RSA` 加密。`publickey_exp` 和 `publickey_mod` 为模数与指数，用于生成公钥：

密码生成后，登录接口 `BeginAuthSessionViaCredentials/v1` 的参数就解决了。至于响应数据的解析依旧是按上文中的方法，这里就不再赘述。

至此，整个逆向流程就结束了。

### 结果验证
