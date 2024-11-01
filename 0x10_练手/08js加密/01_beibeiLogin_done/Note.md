## time模块

~~~ shell
import time
time.time()
~~~

~~~ tex
	返回以浮点数表示的从 epoch 开始的秒数形式的时间, 对 leap seconds 的处理取决于具体平台。 在 Windows 和大多数 Unix 系统中，闰秒不会被计入从 epoch 开始的秒数形式的时间中。 这通常被称为 Unix 时间。

epoch 是起始的时间点，即 time.gmtime(0) 的返回值。 这在所有平台上都是 1970-01-01, 00:00:00 (UTC)。
~~~



## hex语句

~~~ tex
HEX、DEC、OCT 和 BIN含义如下：
    HEX，英文全称 Hexadecimal，表示十六进制。
    DEC，英文全称 Decimal，表示十进制。
    OCT，英文全称 Octal，表示八进制。
    BIN，英文全称 Binary，表示二进制。
~~~



## encode()方法

~~~ tex
描述: Python encode() 方法以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
~~~

~~~ shell
str.encode(encoding='UTF-8',errors='strict')

参数
	encoding -- 要使用的编码，如"UTF-8"。
	errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 		'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
	
返回值
	该方法返回编码后的字符串。
~~~



## hashlib模块

~~~ tex
hashlib.md5(string)模块返回使用md5算法加密的string

哈希对象具有下列方法:
	hash.update(data):用 bytes-like object 来更新哈希对象。 重复调用相当于单次调用并传入所有参数的拼接结果: m.update(a); m.update(b) 等价于 m.update(a+b)。

	hash.digest():返回当前已传给 update() 方法的数据摘要。 这是一个大小为 digest_size 的字节串对象，字节串中可包含 0 至 255 的完整取值范围。

	hash.hexdigest():类似于 digest() 但摘要会以两倍长度字符串对象的形式返回，其中仅包含十六进制数码。 这可以被用于在电子邮件或其他非二进制环境中安全地交换数据值。

	hash.copy():返回哈希对象的副本（“克隆”）。 这可被用来高效地计算共享相同初始子串的数据的摘要。
~~~



## hmac模块

~~~ tex
hmac.new(key, msg=None, digestmod)
	返回一个新的 hmac 对象。 key 是一个指定密钥的 bytes 或 bytearray 对象。 如果提供了 msg，将会调用 update(msg) 方法。 digestmod 为 HMAC 对象所用的摘要名称、摘要构造器或模块。 它可以是适用于 hashlib.new() 的任何名称。 虽然该参数位置靠后，但它却是必须的。
~~~

