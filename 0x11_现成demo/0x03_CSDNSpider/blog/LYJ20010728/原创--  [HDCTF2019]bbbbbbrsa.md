# 原创
：  [HDCTF2019]bbbbbbrsa

# [HDCTF2019]bbbbbbrsa

[题目地址](https://buuoj.cn/challenges#%5BHDCTF2019%5Dbbbbbbrsa)<br/> 题目给的两个文件：

```
from base64 import b64encode as b32encode
from gmpy2 import invert,gcd,iroot
from Crypto.Util.number import *
from binascii import a2b_hex,b2a_hex
import random

flag = "******************************"

nbit = 128

p = getPrime(nbit)
q = getPrime(nbit)
n = p*q

print p
print n

phi = (p-1)*(q-1)

e = random.randint(50000,70000)

while True:
	if gcd(e,phi) == 1:
		break;
	else:
		e -= 1;

c = pow(int(b2a_hex(flag),16),e,n)

print b32encode(str(c))[::-1]

# 2373740699529364991763589324200093466206785561836101840381622237225512234632


```

```
p = 177077389675257695042507998165006460849
n = 37421829509887796274897162249367329400988647145613325367337968063341372726061
c = ==gMzYDNzIjMxUTNyIzNzIjMyYTM4MDM0gTMwEjNzgTM2UTN4cjNwIjN2QzM5ADMwIDNyMTO4UzM2cTM5kDN2MTOyUTO5YDM0czM3MjM

c = 2373740699529364991763589324200093466206785561836101840381622237225512234632
q = 211330365658290458913359957704294614589

```

这里我先把c和q求出来了<br/> 根据前面的加密过程我们可以知道e是50000-70000中的一个数，我们直接枚举即可：

```
import gmpy2
import binascii
from Crypto.Util.number import *
p = 177077389675257695042507998165006460849
c = 2373740699529364991763589324200093466206785561836101840381622237225512234632
q = 211330365658290458913359957704294614589
n = 37421829509887796274897162249367329400988647145613325367337968063341372726061
phi = (p-1)*(q-1)
for e in range(50000,70000):
    if (gmpy2.gcd(e,phi) == 1):
        d = gmpy2.invert(e,phi)
        flag=str(long_to_bytes(pow(c,d,n)))
        if 'flag' in flag:
            print(flag)

```

这里由于符合条件的e太多了，所以我们直接查找关键词得到最后的flag：`flag{rs4_1s_s1mpl3!#}`
