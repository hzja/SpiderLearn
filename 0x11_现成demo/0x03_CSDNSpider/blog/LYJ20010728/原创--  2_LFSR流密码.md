# 原创
：  2_LFSR流密码

# 2_LFSR流密码

**实验目的**

> 
编程实现简单地线性反馈移位寄存器，理解其工作原理，掌握流密码的算法结构和加解密过程


**实验环境**

> 
PyCharm


**实验要求**

> 
利用Python语言实现LFSR；通过不同初始状态生成相应序列，观察其周期特点；利用生成的序列对文本进行加密和解密运算；完成实验报告


**实验内容**

> 
给定的LFSR结构如图，程序完成功能：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210510232030255.png#pic_center"/><br/> （1）由给定的初始状态序列生成密钥序列<br/> （2）选择进行文件加密还是解密<br/> （3）如果选择文件加密，则从in.txt中读取明文，用密钥流序列进行加密，密文保存于out.txt中；如果选择文件解密，则从out.txt中读取密文，用密钥流序列进行解密，密文保存于in.txt中


**实验代码**

```
# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 23:22
# @Author  : H3rmesk1t
# @FileName: LFSR密码.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/LYJ20010728/
# 读入明文
import numpy as np
# 采用随机数种子，确保随机密钥一致
np.random.seed(209)

# 明文读取
def getFile():
    with open('LFSR密码_In.txt', 'r', encoding='utf-8') as file_object:
        content = file_object.read()
    print('明文读取成功！')
    return content

# 密文保存
def saveFile(ResultString, key):
    filename = 'write_data.txt'
    with open('LFSR密码_Out.txt', 'w', encoding='utf-8') as file_object:
        file_object.write(ResultString + '\n')
        file_object.write(str(key))
    print('密文以及密钥保存成功！')

# 产生随机密钥
def getKey():
    key = list(np.random.randint(0, 2, 5))
    print(f"初始密钥为：{key}")
    for i in range(5,31):
        temp = (key[i-2] + key[i-5]) % 2
        key.append(temp)
    print(f"变换后得到的加解密所用密钥：{key}")
    return key

# LFSR加密
def encodeOfLSFR(content, key):
    m = 0
    encodeResult = []
    for i in content:
        sum = 0
        n = 0
        for j in range(8):
            n = j
            sum += pow(2, 7 - n) * key[(m + n) % 31]
        if (m + n &gt; 32):
            m = (m + n - 1) % 31 + 1
        else:
            m = m + 8
        encodeResult.append(chr(ord(i) ^ sum))
    encodeResultString = ''.join(encodeResult)
    print(f'加密前的内容为：{content}')
    print(f"加密后的内容为：{encodeResultString}")
    saveFile(encodeResultString, key=key)

# LFSR解密
def decodeOfLSFR(content, key):
    m = 0
    decodeResult = []
    for i in content:
        sum = 0
        n = 0
        for j in range(8):
            n = j
            sum += pow(2, 7 - n) * key[(m + n) % 31]
        if (m + n &gt; 32):
            m = (m + n - 1) % 31 + 1
        else:
            m = m + 8
        decodeResult.append(chr(ord(i) ^ sum))
    decodeResultString = ''.join(decodeResult)
    print(f"解密前的内容为：{content}")
    print(f"解密后的内容为：{decodeResultString}")
    saveFile(decodeResultString, key=key)

if __name__ == '__main__':
    # 操作方式选择
    wayOfChoice = eval(input("请选择操作方式：1-加密 2-解密\n"))
    key = getKey()
    if wayOfChoice == 1:
        encodeOfLSFR(content=getFile(), key=key)
    elif wayOfChoice == 2:
        decodeOfLSFR(content=getFile(), key=key)

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210511092251294.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210511092303693.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210511092351565.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210511092401619.png#pic_center"/>
