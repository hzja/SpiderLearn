# 原创
：  7_DH协议

# 7_DH协议

**实验题目**

> 
DH协议


**实验目的和要求**

> 
通过实验熟练掌握DH协议，了解密钥协商协议内涵，提高使用Python语言设计能力


**实验环境**

> 
PyCharm


**实验内容**

> 
进行会话通信的A和B两方，共享生成符合需要的大素数和生成元，而后各自生成随机数，进行发送部分密钥，最后计算协商成功共享密钥


**算法描述**

> 
DH协议描述：<br/> Diffie-Hellman:一种确保共享KEY安全穿越不安全网络的方法，它是OAKLEY的一个组成部分。Whitefield与Martin Hellman在1976年提出了一个奇妙的密钥交换协议，称为Diffie-Hellman密钥交换协议/算法(Diffie-Hellman Key Exchange/Agreement Algorithm).这个机制的巧妙在于需要安全通信的双方可以用这个方法确定对称密钥；然后可以用这个密钥进行加密和解密；但是注意，这个密钥交换协议/算法只能用于密钥的交换，而不能进行消息的加密和解密；双方确定要用的密钥后，要使用其他对称密钥操作加密算法实现加密和解密消息<br/> 实验步骤<br/> 1.生成大素数p和生成元g；<br/> 2.选择随机数x，计算g^x；<br/> 3.选择随机数y，计算g^y；<br/> 4.计算接收方的共享密钥K_B=(g^x )^y；<br/> 5.计算发送方的共享密钥K_A=(g^y )^x；<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021051220075953.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>


**实验代码**

```
# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 19:50
# @Author  : H3rmesk1t
# @FileName: DH协议.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/LYJ20010728/
import math
import random
from Cryptodome.Util.number import *

def judge_prime(p):
    # 素数的判断
    if p &lt;= 1:
        return False
    i = 2
    while i * i &lt;= p:
        if p % i == 0:
            return False
        i += 1
    return True


def get_generator(p):
    # 得到所有的原根
    a = 2
    list = []
    while a &lt; p:
        flag = 1
        while flag != p:
            if (a ** flag) % p == 1:
                break
            flag += 1
        if flag == (p - 1):
            list.append(a)
        a += 1
    return list

def yg(n):		# 这样默认求最小原根
    k=(n-1)//2
    for i in range(2,n-1):
        if multimod(i,k,n)!=1:
            return i

def multimod(a,k,n):    #快速幂取模
    ans=1
    while(k!=0):
        if k%2:         #奇数
            ans=(ans%n)*(a%n)%n
        a=(a%n)*(a%n)%n
        k=k//2          #整除2
    return ans

# A，B得到各自的计算数
def get_calculation(p, a, X):
    Y = (a ** X) % p
    return Y


# A，B得到交换计算数后的密钥
def get_key(X, Y, p):
    key = (Y ** X) % p
    return key


if __name__ == "__main__":
    # 随机得到一个素数
    prime = getPrime(20)
    print(prime)
    # 得到素数的第一个一个原根
    list = yg(prime)
    print(str(prime) + ' 的一个原根为：', end='')
    print(list)
    print('------------------------------------------------------------------------------')

    # 得到A的私钥
    XA = random.randint(0, prime - 1)
    print('A随机生成的私钥为：%d' % XA)

    # 得到B的私钥
    XB = random.randint(0, prime - 1)
    print('B随机生成的私钥为：%d' % XB)
    print('------------------------------------------------------------------------------')

    # 得待A的计算数
    YA = get_calculation(prime, int(list), XA)
    print('A的计算数为：%d' % YA)

    # 得到B的计算数
    YB = get_calculation(prime, int(list), XB)
    print('B的计算数为：%d' % YB)
    print('------------------------------------------------------------------------------')

    # 交换后A的密钥
    key_A = get_key(XA, YB, prime)
    print('A的生成密钥为：%d' % key_A)

    # 交换后B的密钥
    key_B = get_key(XB, YA, prime)
    print('B的生成密钥为：%d' % key_B)
    print('---------------------------True or False------------------------------------')

    print(key_A == key_B)

```
