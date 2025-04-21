# 原创
：  【JS 逆向百例】房天下登录接口参数逆向

# 【JS 逆向百例】房天下登录接口参数逆向

### 声明

本文章中所有内容仅供学习交流，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关，若有侵权，请联系我立即删除！

### 逆向目标

### 逆向过程

#### 抓包分析

随便输入一个账号密码，点击登陆，抓包定位到登录接口为 https://passport.fang.com/login.api ，POST 请求，Form Data 里，密码 pwd 被加密处理了。

#### 参数逆向

加密参数只有一个 pwd，直接全局搜索，出现一个 loginbypassword.js，很明显就是加密的 JS，这个 JS 贴心的写上了中文注释，直接来到登录模块，埋下断点：

```
uid: that.username.val(),
pwd: encryptedString(key_to_encode, that.password.val()),
Service: that.service.val(),
AutoLogin: that.autoLogin.val()

```

`encryptedString` 这个函数可以看到在一个叫做 `RSA.min.js` 的加密 JS 里，很明显的 RSA 加密，直接 copy 下来就好了，`key_to_encode` 这个参数可以直接在首页搜到，可以看到是向 `RSAKeyPair` 函数传入参数得到的：

### 完整代码

**以下只演示部分关键代码**，完整代码可在 GitHub 下载：https://github.com/kuaidaili/crawler/tree/main/passport_fang_com

#### fang_encrypt.js

```
function setMaxDigits(n) {}

function BigInt(n) {}

function biFromDecimal(n) {}

// 此处省略 N 个函数

function twoDigit(n) {}

function encryptedString(n, t) {}

function decryptedString(n, t) {}

var biRadixBase = 2, biRadixBits = 16, bitsPerDigit = biRadixBits, biRadix = 65536, biHalfRadix = biRadix &gt;&gt;&gt; 1,
    biRadixSquared = biRadix * biRadix, maxDigitVal = biRadix - 1, maxInteger = 9999999999999998, maxDigits, ZERO_ARRAY,
    bigZero, bigOne, dpl10, lr10, hexatrigesimalToChar, hexToChar, highBitMasks, lowBitMasks;
setMaxDigits(20);
dpl10 = 15;
lr10 = biFromNumber(1e15);
hexatrigesimalToChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
hexToChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"];
highBitMasks = [0, 32768, 49152, 57344, 61440, 63488, 64512, 65024, 65280, 65408, 65472, 65504, 65520, 65528, 65532, 65534, 65535];
lowBitMasks = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535];
setMaxDigits(129);

function getEncryptedPassword(pwd, n, i, t) {
    var key_to_encode = new RSAKeyPair(n, i, t);
    return encryptedString(key_to_encode, pwd)
}

// 测试样例
// console.log(getEncryptedPassword("16521689404", "010001", "", "978C0A92D2173439707498F0944AA476B1B62595877DD6FA87F6E2AC6DCB3D0BF0B82857439C99B5091192BC134889DFF60C562EC54EFBA4FF2F9D55ADBCCEA4A2FBA80CB398ED501280A007C83AF30C3D1A142D6133C63012B90AB26AC60C898FB66EDC3192C3EC4FF66925A64003B72496099F4F09A9FB72A2CF9E4D770C41"))

```

#### fang_login.py

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

import execjs
import requests


index_url = 'https://passport.fang.com/'
login_url = 'https://passport.fang.com/login.api'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
session = requests.session()


def get_key_to_encode():
    headers = {'User-Agent': user_agent}
    response = session.get(url=index_url, headers=headers)
    key_to_encode = re.findall(r'RSAKeyPair\((.*)\);', response.text)[0].replace('"', '').split(', ')
    return key_to_encode


def get_encrypted_password(key_to_encode, pwd):
    n, i, t = key_to_encode[0], key_to_encode[1], key_to_encode[2]
    with open('fang_encrypt.js', 'r', encoding='utf-8') as f:
        fang_js = f.read()
    encrypted_pwd = execjs.compile(fang_js).call('getEncryptedPassword', pwd, n, i, t)
    return encrypted_pwd


def login(encrypted_password, uid):
    headers = {
        'User-Agent': user_agent,
        'X-Requested-With': 'XMLHttpRequest',
        'Host': 'passport.fang.com',
        'Origin': 'https://passport.fang.com',
        'Referer': 'https://passport.fang.com/?backurl=http%3a%2f%2fmy.fang.com%2f',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    data = {
        'uid': uid,
        'pwd': encrypted_password,
        'Service': 'soufun-passport-web',
        'AutoLogin': 1
    }
    response = session.post(url=login_url, data=data, headers=headers)
    print(response.json())


def main():
    # 16521689404
    uid = input('请输入登录账号：')
    pwd = input('请输入登录密码：')
    rsa_key = get_key_to_encode()
    encrypted_pwd = get_encrypted_password(rsa_key, pwd)
    login(encrypted_pwd, uid)


if __name__ == '__main__':
    main()

```
