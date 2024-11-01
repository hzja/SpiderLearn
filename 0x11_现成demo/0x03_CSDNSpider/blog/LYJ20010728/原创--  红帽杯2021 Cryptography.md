# 原创
：  红帽杯2021 Cryptography

# 红帽杯2021 Cryptography

#### 红帽杯2021 Cryptography

## primegame

> 
这道题搬了一道原题：[原题链接](https://www.secmem.org/blog/2020/09/20/poka-science-war-hacking/)<br/> 采用的方法为低密度攻击的扩展


```
题目代码:
from decimal import *
import math
import random
import struct
from flag import flag

assert (len(flag) == 48)
msg1 = flag[:24]
msg2 = flag[24:]                        
primes = [2]
for i in range(3, 90):		# 寻找奇数
    f = True
    for j in primes:
        if i * i &lt; j:
            break
        if i % j == 0:
            f = False
            break
    if f:
        primes.append(i)

getcontext().prec = 100		# 设置浮点数精度
keys = []
for i in range(len(msg1)):
    keys.append(Decimal(primes[i]).ln())

sum_ = Decimal(0.0)
for i, c in enumerate(msg1):
    sum_ += c * Decimal(keys[i])

ct = math.floor(sum_ * 2 ** 256)
print(ct)                  

sum_ = Decimal(0.0)
for i, c in enumerate(msg2):
    sum_ += c * Decimal(keys[i])

ct = math.floor(sum_ * 2 ** 256)
print(ct)	 

```

> 
该代码的结构如下：<br/> 查找不超过100的质数<br/> 通过使用flag的前24位与后24位作为随机种子，可以对十进制数组进行混洗<br/> 每个改组的素数都表示为ln到Decimal<br/> 通过将少量ln值乘以标志的每个字节获得的值相加<br/> 题目采用的为背包密码系统，背包加密系统是一种使用0/1背包问题创建的公钥密码系统，流行的攻击方法之一是低密度攻击


```
exp:
import math
from decimal import *
import random


getcontext().prec = int(100)

primes = [2]
for i in range(3, 90):
    f = True
    for j in primes:
        if i * i &lt; j:
            break
        if i % j == 0:
            f = False
            break
    if f:
        primes.append(i)

keys = []
for i in range(len(primes)):
    keys.append(Decimal(int(primes[i])).ln())

arr = []
for v in keys:
    arr.append(int(v * int(16) ** int(64)))

ct = 425985475047781336789963300910446852783032712598571885345660550546372063410589918
# ct = 597952043660446249020184773232983974017780255881942379044454676980646417087515453

def encrypt(res):
    h = Decimal(int(0))
    for i in range(len(keys)):
        h += res[i] * keys[i]

    ct = int(h * int(16)**int(64))
    return ct


def f(N):
    ln = len(arr)
    A = Matrix(ZZ, ln + 1, ln + 1)
    for i in range(ln):
        A[i, i] = 1
        A[i, ln] = arr[i] // N
        A[ln, i] = 64

    A[ln, ln] = ct // N

    res = A.LLL()

    for i in range(ln + 1):
        flag = True
        for j in range(ln):
            if -64 &lt;= res[i][j] &lt; 64:
                continue
            flag = False
            break
        if flag:
            vec = [int(v + 64) for v in res[i][:-1]]
            ret = encrypt(vec)
            if ret == ct:
                print(N, bytes(vec))


for i in range(2, 10000):
    print(i)
    f(i)

```

> 
分贝将out文件中的ct值放入代码中运行得到flag的两段：b’flag{715c39c3-1b46-4c23-‘和b’8006-27b43eba2446}\x00\x00\x00\x00\x00\x00’


flag为`flag{715c39c3-1b46-4c23-8006-27b43eba2446}`

## hpcurve

> 
这道题也是一道原题改过来的：[原题wp链接](https://pwnthem0le.polito.it/2020/12/20/hxpCTF-2020-Hyper-writeup/)<br/> 我们利用原题的exp，将out文件中的数据放进去直接打


```
import struct
p = 10000000000000001119

K = GF(p)
R.&lt;x&gt; = K[]; y=x
f = y + prod(map(eval, 'yyyyyyy'))
C = HyperellipticCurve(f, 0)
J = C.jacobian()

def get_u_from_out(output, known_input):
    res = []
    for i in range(24):
        res.append(output[i]^^known_input[i])
    res = bytes(res)
    u0, u1, u2 = struct.unpack("&lt;QQQ", res)
    u = x^3+x^2*u2+x*u1+u0
    return u

from itertools import product

def get_v_from_u(u):
    Kbar = GF(p^6)
    Rbar.&lt;t&gt; = Kbar["t"]
    u2 = u.change_ring(Rbar)
    roots = [x[0] for x in u2.roots()]
    ys = []
    for root in roots:
        ys.append(f(root).sqrt(0,1))
    res = []
    for perm in product(range(2), repeat=3):
        poly = Rbar.lagrange_polynomial([(roots[i], ys[i][perm[i]]) for i in range(3)])
        if poly[0] in K:
            res.append(R(poly))
    return res

def try_decode(output, u, v):
    rs = [u[0], u[1], u[2], v[0], v[1], v[2]]
    otp = struct.pack("&lt;QQQQQQ", *rs)
    plain = []
    for i in range(len(output)):
        plain.append(output[i]^^otp[i%len(otp)])
    return bytes(plain)


output = bytes.fromhex("66def695b20eeae3141ea80240e9bc7138c8fc5aef20532282944ebbbad76a6e17446e92de5512091fe81255eb34a0e22a86a090e25dbbe3141aff0542f5")

known_input = 20*b"a"+b"flag"
u = get_u_from_out(output, known_input)
vs = get_v_from_u(u)
for v in vs:
    print(try_decode(output,u,v))

```

> 
运行后得到：flag{1b82f60a-43ab-4f18-8ccc-97d120aae6fc}


flag为`flag{1b82f60a-43ab-4f18-8ccc-97d120aae6fc}`
