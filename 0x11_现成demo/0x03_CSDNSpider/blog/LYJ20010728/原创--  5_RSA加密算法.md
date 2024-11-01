# 原创
：  5_RSA加密算法

# 5_RSA加密算法

**实验题目**

> 
RSA加密算法


**实验目的和要求**

> 
熟悉RSA加解密算法的运行过程，使用Python语言编写实现RSA算法程序，加深对素数筛选和使用的理解


**实验环境**

> 
PyCharm


**算法描述**

> 
RSA公开密钥密码体制的原理是：根据数论，寻求两个大素数比较简单，而将它们的乘积进行因式分解却极其困难，因此可以将乘积公开作为加密密钥<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210511125723970.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>


**实验代码**

```
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 12:58
# @Author  : H3rmesk1t
# @FileName: RSA加密.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/LYJ20010728/
import gmpy2
import binascii
from Cryptodome.Util.number import *

# 读取加密前文件
def getFileFront():
    try:
        with open('RSA_IN.txt', 'r', encoding='utf-8') as file_object:
            content = file_object.read()
        print("文件读取成功！")
    except IOError:
        print('文件读取出错！')
    return content

# 读取解密前文件
def getFileLater():
    try:
        with open('RSA_OUT.txt', 'r', encoding='utf-8') as file_object:
            content = file_object.readlines()
        print("文件读取成功！")
    except IOError:
        print("文件读取出错")
    return content

# 保存加密后文件
def saveFileLater(p,q,d,e,c):
    try:
        with open('RSA_OUT.txt', 'w', encoding='utf-8') as file_object:
            file_object.write("p:" + str(p) + '\n')
            file_object.write("q:" + str(q) + '\n')
            file_object.write("d:" + str(d) + '\n')
            file_object.write("e:" + str(e) + '\n')
            file_object.write("c:" + str(c) + '\n')
        print("文件保存成功！")
    except IOError:
        print('文件加解密出错！')

# 保存解密后文件
def saveFileFront(msg):
    try:
        with open('RSA_IN.txt', 'w', encoding='utf-8') as file_object:
            file_object.write(str(msg))
        print("文件保存成功！")
    except IOError:
        print('文件加解密出错！')

# 素数生成
def Prime():
    p = getPrime(512)
    q = getPrime(512)
    print(f"素数生成成功 分别为\n{p}\n{q}")
    return p,q

# 加密操作
def encodeOfRSA(p,q,e,msg):
    hex_msg = binascii.b2a_hex(msg.encode('utf-8'))
    hex_msg = int(hex_msg, 16)
    print(f"明文为：{msg}")
    phi = (p - 1) * (q - 1)
    n = p * q
    d = gmpy2.invert(e, phi)
    c = pow(hex_msg, e, n)
    print(f"加密过程中的公钥n为：{n}")
    print(f"加密过程中的私钥d为：{d}")
    print(f"加密的结果为：{c}")
    saveFileLater(p,q,d,e,c)

# 解密操作
def decodeOfRSA():
    content = []
    for i in getFileLater():
        content.append(int(i[2:len(i) - 1]))
    n = content[0] * content[1]
    msg = pow(content[4], content[2], n)
    msg = binascii.unhexlify(hex(msg)[2:].strip("L"))
    print(f"解密过程中的p为：{content[0]}")
    print(f"解密过程中的q为：{content[1]}")
    print(f"解密过程中的d为：{content[2]}")
    print(f"解密过程中的e为：{content[3]}")
    print(f"解密过程中的c为：{content[4]}")
    print(f"解密的结果为：{msg}")
    saveFileFront(msg)

if __name__ == '__main__':
    while True:
        mode = eval(input("请选择你要进行的操作：1-加密 2-解密\n"))
        if mode == 1:
            p,q = Prime()
            e = eval(input("请输入公钥e；\n"))
            encodeOfRSA(p=p,q=q,e=e,msg=getFileFront())
        elif mode == 2:
            decodeOfRSA()
        else:
            print("操作选择错误，请重试！")
            continue

```
