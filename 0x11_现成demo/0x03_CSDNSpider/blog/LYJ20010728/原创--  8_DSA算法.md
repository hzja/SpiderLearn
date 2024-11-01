# 原创
：  8_DSA算法

# 8_DSA算法

**实验题目**

> 
DSA算法


**实验目的和要求**

> 
熟悉MPIR大数库的用法，理解和学会DSA数字签名算法，提高一般数字签名算法的设计能力<br/> **实验环境**<br/> PyCharm


**实验内容**

> 
生成满足要求公私钥，随机选取消息，生成DSA签名


**算法描述**

> 
实验步骤<br/> 1.生成公钥的各个部分pubkey-&gt;alpha，pubkey-&gt;p，pubkey-&gt;q，pubkey-&gt;y；<br/> 2.生成私钥prikey；<br/> 3.随机生成消息m；<br/> 4.生成签名的各个部分<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210512213050902.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>


**实验代码**

```
# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 20:12
# @Author  : H3rmesk1t
# @FileName: DSA算法.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/LYJ20010728/
#encoding utf-8
from Cryptodome.Random import random
from Cryptodome.PublicKey import DSA
from Cryptodome.Hash import SHA256
from Cryptodome.Signature import DSS

# Create a new DSA key
def getPublicKey():
    key = DSA.generate(2048)
    f = open("public_key.pem", "wb+")
    f.write(key.publickey().export_key())
    f.close()
    return key

# Sign a message
def signMessage(message,key):
    hash_obj = SHA256.new(message)
    signer = DSS.new(key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature

# Load the public key
def loadPublicKey(message):
    f = open("public_key.pem", "r")
    hash_obj = SHA256.new(message)
    pub_key = DSA.import_key(f.read())
    verifier = DSS.new(pub_key, 'fips-186-3')
    return hash_obj,verifier

# Verify the authenticity of the message
def verifyAuthenticityOfMessage(hash_obj,verifier,signature):
    try:
        verifier.verify(hash_obj, signature)
        print("ResultOfVerify：The message is authentic.")
    except ValueError:
        print("ResultOfVerify：The message is not authentic.")

# print parameter we got
def printParameter(message,key,hash_obj,verifier,signature):
    print(f"Message is {message}")
    print(f"Key is {key}")
    print(f"Hash_obj is {hash_obj}")
    print(f"Verifier is {verifier}")
    print(f"Signature is {signature}")

if __name__ == '__main__':
    message = b"H3rmesk1t_is_a_cool_boy"
    key = getPublicKey()
    signature = signMessage(message=message, key=key)
    hash_obj, verifier = loadPublicKey(message=message)
    printParameter(message=message, key=key, hash_obj=hash_obj, verifier=verifier, signature=signature)
    verifyAuthenticityOfMessage(hash_obj=hash_obj, verifier=verifier, signature=signature)

```
