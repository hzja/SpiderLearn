# 原创
：  爬虫逆向基础，认识 SM1-SM9、ZUC 国密算法

# 爬虫逆向基础，认识 SM1-SM9、ZUC 国密算法

> 
关注微信公众号：K哥爬虫，QQ交流群：808574309，持续分享爬虫进阶、JS/安卓逆向等技术干货！


#### 文章目录

---


### 【01x00】 简介

国密即国家密码局认定的国产加密算法，爬虫工程师在做 JS 逆向的时候，会遇到各种各样的加密算法，其中 RSA、AES、SHA 等算法是最常见的，这些算法都是国外的，在 K 哥以前的文章里也有介绍：[《【爬虫知识】爬虫常见加密解密算法》](https://mp.weixin.qq.com/s/4QTee0M9ukN6olgoR_LMug)

事实上从 2010 年开始，我国国家密码管理局就已经开始陆续发布了一系列国产加密算法，这其中就包括 SM1、SM2、SM3 、SM4、SM7、SM9、ZUC（祖冲之加密算法）等，SM 代表商密，即商业密码，是指用于商业的、不涉及国家秘密的密码技术。**SM1 和 SM7 的算法不公开**，其余算法都已成为 ISO/IEC 国际标准。

在这些国产加密算法中，**SM2、SM3、SM4 三种加密算法是比较常见的**，在爬取部分 gov 网站时，也可能会遇到这些算法，所以作为爬虫工程师是有必要了解一下这些算法的，如下图所示某 gov 网站就使用了 SM2 和 SM4 加密算法：

### 【02x00】算法概述

<th align="center">算法名称</th><th align="center">算法类别</th><th align="center">应用领域</th><th align="center">特点</th>
|------
<td align="center">SM1</td><td align="center">对称（分组）加密算法</td><td align="center">芯片</td><td align="center">分组长度、密钥长度均为 128 比特</td>
<td align="center">SM2</td><td align="center">非对称（基于椭圆曲线 ECC）加密算法</td><td align="center">数据加密</td><td align="center">ECC 椭圆曲线密码机制 256 位，相比 RSA 处理速度快，消耗更少</td>
<td align="center">SM3</td><td align="center">散列（hash）函数算法</td><td align="center">完整性校验</td><td align="center">安全性及效率与 SHA-256 相当，压缩函数更复杂</td>
<td align="center">SM4</td><td align="center">对称（分组）加密算法</td><td align="center">数据加密和局域网产品</td><td align="center">分组长度、密钥长度均为 128 比特，计算轮数多</td>
<td align="center">SM7</td><td align="center">对称（分组）加密算法</td><td align="center">非接触式 IC 卡</td><td align="center">分组长度、密钥长度均为 128 比特</td>
<td align="center">SM9</td><td align="center">标识加密算法（IBE）</td><td align="center">端对端离线安全通讯</td><td align="center">加密强度等同于 3072 位密钥的 RSA 加密算法</td>
<td align="center">ZUC</td><td align="center">对称（序列）加密算法</td><td align="center">移动通信 4G 网络</td><td align="center">流密码</td>

### 【03x00】算法详解

#### 【03x01】SM1 分组加密算法

SM1 为分组加密算法，对称加密，分组长度和密钥长度都为 128 位，故对消息进行加解密时，若消息长度过长，需要进行分组，要消息长度不足，则要进行填充。算法安全保密强度及相关软硬件实现性能与 AES 相当，该算法不公开，仅以 IP 核的形式存在于芯片中，调用该算法时，需要通过加密芯片的接口进行调用，采用该算法已经研制了系列芯片、智能 IC 卡、智能密码钥匙、加密卡、加密机等安全产品，广泛应用于电子政务、电子商务及国民经济的各个应用领域（包括国家政务通、警务通等重要领域），一般了解的人比较少，爬虫工程师也不会遇到这种加密算法。

#### 【03x02】SM2 椭圆曲线公钥加密算法

SM2 为椭圆曲线（ECC）公钥加密算法，非对称加密，SM2 算法和 RSA 算法都是公钥加密算法，SM2 算法是一种更先进安全的算法，在我们国家商用密码体系中被用来替换 RSA 算法，在不少 gov 网站会见到此类加密算法。我国学者对椭圆曲线密码的研究从 20 世纪 80 年代开始，目前已取得不少成果，SM2 椭圆曲线公钥密码算法比 RSA 算法有以下优势：

<th align="center">SM2</th><th align="center">RSA</th>
|------
<td align="center">安全性</td><td align="center">256 位 SM2 强度已超过 RSA-2048</td><td align="center">一般</td>
<td align="center">算法结构</td><td align="center">基本椭圆曲线（ECC）</td><td align="center">基于特殊的可逆模幂运算</td>
<td align="center">计算复杂度</td><td align="center">完全指数级</td><td align="center">亚指数级</td>
<td align="center">存储空间（密钥长度）</td><td align="center">192-256 bit</td><td align="center">2048-4096 bit</td>
<td align="center">秘钥生成速度</td><td align="center">较 RSA 算法快百倍以上</td><td align="center">慢</td>
<td align="center">解密加密速度</td><td align="center">较快</td><td align="center">一般</td>

#### 【03x03】SM3 杂凑算法

SM3 为密码杂凑算法，采用密码散列（hash）函数标准，用于替代 MD5/SHA-1/SHA-2 等国际算法，是在 SHA-256 基础上改进实现的一种算法，消息分组长度为 512 位，摘要值长度为 256 位，其中使用了异或、模、模加、移位、与、或、非运算，由填充、迭代过程、消息扩展和压缩函数所构成。在商用密码体系中，SM3 主要用于数字签名及验证、消息认证码生成及验证、随机数生成等。据国家密码管理局表示，其安全性及效率要高于 MD5 算法和 SHA-1 算法，与 SHA-256 相当。

#### 【03x04】SM4 分组加密算法

SM4 为无线局域网标准的分组加密算法，对称加密，用于替代 DES/AES 等国际算法，SM4 算法与 AES 算法具有相同的密钥长度和分组长度，均为 128 位，故对消息进行加解密时，若消息长度过长，需要进行分组，要消息长度不足，则要进行填充。加密算法与密钥扩展算法都采用 32 轮非线性迭代结构，解密算法与加密算法的结构相同，只是轮密钥的使用顺序相反，解密轮密钥是加密轮密钥的逆序。

|SM4|DES|AES
|------
|计算轮数|32|16（3DES 为 16*3）|10/12/14
|密码部件|S 盒、非线性变换、线性变换、合成变换|标准算术和逻辑运算、先替换后置换，不含线性变换|S 盒、行移位变换、列混合变换、圈密钥加变换（AddRoundKey）

#### 【03x05】SM7 分组加密算法

SM7 为分组加密算法，对称加密，该算法不公开，应用包括身份识别类应用（非接触式 IC 卡、门禁卡、工作证、参赛证等），票务类应用（大型赛事门票、展会门票等），支付与通卡类应用（积分消费卡、校园一卡通、企业一卡通等）。爬虫工程师基本上不会遇到此类算法。

#### 【03x06】SM9 标识加密算法

SM9 为标识加密算法（Identity-Based Cryptography），非对称加密，标识加密将用户的标识（如微信号、邮件地址、手机号码、QQ 号等）作为公钥，省略了交换数字证书和公钥过程，使得安全系统变得易于部署和管理，适用于互联网应用的各种新兴应用的安全保障，如基于云技术的密码服务、电子邮件安全、智能终端保护、物联网安全、云存储安全等等。这些安全应用可采用手机号码或邮件地址作为公钥，实现数据加密、身份认证、通话加密、通道加密等。在商用密码体系中，SM9 主要用于用户的身份认证，据新华网公开报道，SM9 的加密强度等同于 3072 位密钥的 RSA 加密算法。

#### 【03x07】ZUC 祖冲之算法

ZUC 为流密码算法，对称加密，该机密性算法可适用于 3GPP LTE 通信中的加密和解密，该算法包括祖冲之算法（ZUC）、机密性算法（128-EEA3）和完整性算法（128-EIA3）三个部分。已经被国际组织 3GPP 推荐为 4G 无线通信的第三套国际加密和完整性标准的候选算法。

### 【04x00】编程语言实现

#### 【04x01】Python 语言实现

在 Python 里面并没有比较官方的库来实现国密算法，这里仅列出了其中两个较为完善的第三方库，需要注意的是，SM1 和 SM7 算法不公开，目前大多库仅实现了 SM2、SM3、SM4 三种密算法。

其中 gmssl-python 是 gmssl 的改进版，gmssl-python 新增支持了 SM9 算法，不过截止本文编写时，gmssl-python 并未发布 pypi，也未 PR 到 gmssl，使用 `pip install gmssl` 安装的 gmssl 不支持 SM9 算法。若要使用 SM9 算法，可下载 gmssl-python 源码手动安装。

以 gmssl 的 SM2 算法为例，实现如下（其他算法和详细用法可参考其官方文档）：

SM2 加密（encrypt）和解密（decrypt）：

```
from gmssl import sm2


# 16 进制的公钥和私钥
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=private_key)

# 待加密数据和加密后数据为 bytes 类型
data = b"this is the data to be encrypted"
enc_data = sm2_crypt.encrypt(data)
dec_data = sm2_crypt.decrypt(enc_data)

print('enc_data: ', enc_data.hex())
print('dec_data: ', dec_data)

# enc_data:  3cb96dd2e0b6c24df8e22a5da3951d061a6ee6ce99f46a446426feca83e501073288b1553ca8d91fad79054e26696a27c982492466dafb5ed06a573fb09947f2aed8dfae243b095ab88115c584bb6f0814efe2f338a00de42b244c99698e81c7913c1d82b7609557677a36681dd10b646229350ad0261b51ca5ed6030d660947

# dec_data:  b'this is the data to be encrypted'

```

SM2 签名（sign）和校验（verify）：

```
from gmssl import sm2, func


# 16 进制的公钥和私钥
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
sm2_crypt = sm2.CryptSM2(public_key=public_key, private_key=private_key)

# 待签名数据为 bytes 类型
data = b"this is the data to be signed"
random_hex_str = func.random_hex(sm2_crypt.para_len)

#  16 进制
sign = sm2_crypt.sign(data, random_hex_str)
verify = sm2_crypt.verify(sign, data)

print('sign: ', sign)
print('verify: ', verify)

# sign:  45cfe5306b1a87cf5d0034ef6712babdd1d98547e75bcf89a17f3bcb617150a3f111ab05597601bab8c41e2b980754b74ebe9a169a59db37d549569910ae273a

# verify:  True

```

#### 【04x02】JavaScript 语言实现

在 JavaScript 中已有比较成熟的实现库，这里推荐 sm-crypto，目前支持 SM2、SM3 和 SM4，需要注意的是，SM2 非对称加密的结果由 C1、C2、C3 三部分组成，其中 C1 是生成随机数的计算出的椭圆曲线点，C2 是密文数据，C3 是 SM3 的摘要值，最开始的国密标准的结果是按 C1C2C3 顺序的，新标准的是按 C1C3C2 顺序存放的，sm-crypto 支持设置 cipherMode，也就是 C1C2C3 的排列顺序。

sm-crypto：https://www.npmjs.com/package/sm-crypto

以 SM2 算法为例，实现如下（其他算法和详细用法可参考其官方文档）：

SM2 加密（encrypt）和解密（decrypt）：

```
const sm2 = require('sm-crypto').sm2

// 1 - C1C3C2，0 - C1C2C3，默认为1
const cipherMode = 1

// 获取密钥对
let keypair = sm2.generateKeyPairHex()
let publicKey = keypair.publicKey   // 公钥
let privateKey = keypair.privateKey // 私钥

let msgString = "this is the data to be encrypted"
let encryptData = sm2.doEncrypt(msgString, publicKey, cipherMode)    // 加密结果
let decryptData = sm2.doDecrypt(encryptData, privateKey, cipherMode) // 解密结果

console.log("encryptData: ", encryptData)
console.log("decryptData: ", decryptData)

// encryptData:  ddf261103fae06d0efe20ea0fe0d82bcc170e8efd8eeae24e9559b3835993f0ed2acb8ba6782fc21941ee74ca453d77664a5cb7dbb91517e6a3b0c27db7ce587ae7af54f8df48d7fa822b7062e2af66c112aa57de94d12ba28e5ba96bf4439d299b41da4a5282d054696adc64156d248049d1eb1d0af28d76b542fe8a95d427e

// decryptData:  this is the data to be encrypted

```

SM2 签名（sign）和校验（verify）：

```
const sm2 = require('sm-crypto').sm2

// 获取密钥对
let keypair = sm2.generateKeyPairHex()
let publicKey = keypair.publicKey   // 公钥
let privateKey = keypair.privateKey // 私钥

// 纯签名 + 生成椭圆曲线点
let msgString = "this is the data to be signed"
let sigValueHex = sm2.doSignature(msgString, privateKey)                    // 签名
let verifyResult = sm2.doVerifySignature(msgString, sigValueHex, publicKey) // 验签结果

console.log("sigValueHex: ", sigValueHex)
console.log("verifyResult: ", verifyResult)

// sigValueHex:  924cbb9f2b5adb554ef77129ff1e3a00b2da42017ad3ec2f806d824a77646987ba8c8c4fb94576c38bc11ae69cc98ebbb40b5d47715171ec7dcea913dfc6ccc1

// verifyResult:  true

```

#### 【04x03】其他语言实现以及参考资料

### 【05x00】附：GM/T 密码行业标准
