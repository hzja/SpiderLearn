# 原创
：  3_DES加密算法

# 3_DES加密算法

**实验目的**

> 
通过实验，掌握DES密码的程序实现，熟悉比特串的操作，矩阵变换，提高xxx程序设计能力


**实验环境**

> 
PyCharm


**实验要求**

> 
编写DES密码的加密解密程序，运行并验证<br/> (1) 输入64比特明文和密文，利用DES密码对其加密并输出密文<br/> (2) 输入DES加密的64比特密文和密钥，对其进行解密<br/> (3) 记录调试和验证过程，完成实验报告


**实验内容**

> 
DES算法包括：<br/> (1)：一个初始置换IP：重排明文分组的64比特数据<br/> (2)：相同功能的16轮变换：每轮中都有置换和代换运算，第16轮变换的输出分为左右两半，并被交换次序<br/> (3)：经过一个逆初始置换IP-1(为IP的逆)，最后产生64比特的密文
- 给定的DES如图：<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210511093033556.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>- 每轮的结构如图：<br/> 32比特扩展48位，轮密钥异或；<br/> S盒代换（1，6位合并选行，2-5位合并选列），置换P<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210511093120712.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> 轮密钥生成：<br/> 输入算法的56比特有效密钥：<br/> 首先经过一个置换运算（实际初始密钥共64位，去除8个校验位并且改变顺序），<br/> 然后将置换后的56比特分为各为28比特的C_0和D_0两半<br/> 第i轮C_(i-1)和D_(i-1)，分别左循环移位。得到C_i和和D_i 做为求下一轮子密钥的输入，同时也输入置换选择2<br/> 置换选择2产生的48比特的 ，即为本轮的子密钥，输入函数<br/> 验证操作 ：<br/> 选择进行文件加密，输入长度为8个字符的加解密的密钥，读入明文文件1.txt，加密文件存储在2.txt文件中；<br/> 选择进行文件解密，输入长度为8个字符的加解密的密钥，读入密文文件2.txt，解密文件存储在3.txt文件中


**实验代码**

> 
DES_MAIN


```
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 9:26
# @Author  : H3rmesk1t
# @FileName: DES加密.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/LYJ20010728/
from 密码学实验.DES_BOX import *
import re

# 读取文件
def getFile():
    try:
        with open('DES_IN.txt', 'r', encoding='utf-8') as file_object:
            content = file_object.read()
        print("文件读取成功！")
    except IOError:
        print('文件加解密出错！')
    return content

# 保存文件
def saveFile(resultString):
    try:
        with open('DES_OUT.txt', 'w', encoding='utf-8') as file_object:
            file_object.write(resultString)
        print("文件保存成功！")
    except IOError:
        print('文件加解密出错！')

# 字符串转化为二进制
def str2bin(message):
    res = ""
    for i in message:                               # 对每个字符进行二进制转化
        tmp = bin(ord(i))[2:]                       # 字符转成ascii，再转成二进制，并去掉前面的0b
        for j in range(0,8-len(tmp)):               # 补齐8位
            tmp = '0'+ tmp                          # 把输出的b给去掉
        res += tmp
    return res


# 二进制转化为字符串
def bin2str(bin_str):
    res = ""
    tmp = re.findall(r'.{8}',bin_str)               # 每8位表示一个字符
    for i in tmp:
        res += chr(int(i,2))                        # base参数的意思，将该字符串视作2进制转化为10进制
    return res
    # print("未经过编码的加密结果:"+res)
    # print("经过base64编码:"+str(base64.b64encode(res.encode('utf-8')),'utf-8'))


# IP盒处理
def ip_change(bin_str):
    res = ""
    for i in IP_table:
        res += bin_str[i-1]                         # 数组下标i-1
    return res


# IP逆盒处理
def ip_re_change(bin_str):
    res = ""
    for i in IP_re_table:
        res += bin_str[i-1]
    return res

# E盒置换
def e_str(bin_str):
    res = ""
    for i in E:
        res += bin_str[i-1]
    return res


# 字符串异或操作
def str_xor(my_str1,my_str2):                       # str，key
    res = ""
    for i in range(0,len(my_str1)):
        xor_res = int(my_str1[i],10)^int(my_str2[i],10) # 变成10进制是转化成字符串 2进制与10进制异或结果一样，都是1,0
        if xor_res == 1:
            res += '1'
        if xor_res == 0:
            res += '0'

    return res


# 循环左移操作
def left_turn(my_str,num):
    left_res = my_str[num:len(my_str)]
    left_res =  left_res+my_str[0:num]
    return left_res


# 秘钥的PC-1置换
def change_key1(my_key):
    res = ""
    for i in PC_1:                                  # PC_1盒上的元素表示位置，只循环64次
        res += my_key[i-1]                          # 将密钥按照PC_1的位置顺序排列
    return res

# 秘钥的PC-2置换
def change_key2(my_key):
    res  = ""
    for i in PC_2:
        res += my_key[i-1]
    return res


# S盒过程
def s_box(my_str):
    res = ""
    c = 0
    for i in range(0,len(my_str),6):                # 步长为6，6个为一组
        now_str = my_str[i:i+6]                     # 第i个分组
        row = int(now_str[0]+now_str[5],2)          # b1b6 =r   第r行
        col = int(now_str[1:5],2)                   # 第c列
        # 第几个s盒的第row*16+col个位置的元素
        num = bin(S[c][row*16 + col])[2:]           # 利用了bin输出有可能不是4位str类型的值，所以才有下面的循环并且加上字符0
        for gz in range(0,4-len(num)):
            num = '0'+ num
        res += num
        c  += 1
    return res


# P盒置换
def p_box(bin_str):
    res = ""
    for i in  P:
        res += bin_str[i-1]
    return res

# F函数的实现
def fun_f(bin_str,key):
    first_output = e_str(bin_str)                   # 位选择函数将32位待加密str拓展位48位
    second_output = str_xor(first_output,key)       # 将48位结果与子密钥Ki按位模2加    得到的结果分为8组（6*8）
    third_output = s_box(second_output)             # 每组6位缩减位4位   S盒置换
    last_output = p_box(third_output)               # P盒换位处理  得到f函数的最终值
    return last_output

def gen_key(key):
    key_list = []
    divide_output = change_key1(key)
    key_C0 = divide_output[0:28]
    key_D0 = divide_output[28:]
    for i in SHIFT:                                 # shift左移位数
        key_c = left_turn(key_C0,i)
        key_d = left_turn(key_D0,i)
        key_output = change_key2(key_c + key_d)
        key_list.append(key_output)
    return key_list

# 64位二进制加密
def des_encrypt_one(bin_content,bin_key):
    mes_ip_bin = ip_change(bin_content)             # ip转换
    key_lst = gen_key(bin_key)                      # 生成子密钥
    mes_left = mes_ip_bin[0:32]
    mes_right = mes_ip_bin[32:]
    for i in range(0,15):
        mes_tmp = mes_right                         # 暂存右边32位
        f_result = fun_f(mes_tmp,key_lst[i])        # 右32位与k的f函数值
        mes_right = str_xor(f_result,mes_left)      # f函数的结果与左边32位异或   作为下次右边32位
        mes_left = mes_tmp                          # 上一次的右边直接放到左边
    f_result = fun_f(mes_right,key_lst[15])         # 第16次不用换位，故不用暂存右边
    mes_fin_left = str_xor(mes_left,f_result)
    mes_fin_right = mes_right
    fin_message = ip_re_change(mes_fin_left + mes_fin_right)   # ip的逆
    return fin_message                              # 返回单字符的加密结果

# 64位二进制解密，注意秘钥反过来了
def des_decrypt_one(bin_content,bin_key):
    mes_ip_bin = ip_change(bin_content)
    key_lst = gen_key(bin_key)
    lst = range(1,16)                               # 循环15次
    cipher_left = mes_ip_bin[0:32]
    cipher_right = mes_ip_bin[32:]
    for i in lst[::-1]:                             # 表示逆转列表调用
        mes_tmp = cipher_right
        cipher_right = str_xor(cipher_left,fun_f(cipher_right,key_lst[i]))
        cipher_left = mes_tmp
    fin_left = str_xor(cipher_left, fun_f(cipher_right, key_lst[0]))
    fin_right = cipher_right
    fin_output = fin_left + fin_right
    bin_plain = ip_re_change(fin_output)
    res = bin2str(bin_plain)
    return res

# 判断以及处理信息分组
def deal_content(bin_content):
    ans = len(bin_content)
    if ans % 64 != 0:
        for i in range( 64 - (ans%64)):             # 不够64位补充0
            bin_content += '0'
    return bin_content

# 判断秘钥是否为64位
def input_key_judge(bin_key):
    # 密钥长度不满足64位的用0补全
    ans = len(bin_key)
    if len(bin_key) &lt; 64:
        if ans % 64 != 0:
            for i in range(64 - (ans % 64)):        # 不够64位补充0
                bin_key += '0'
    return bin_key

# 加密起始函数
def encodeOfDES(content,key):
    bin_content = deal_content(str2bin(content))    # 得到明文的二进制比特流  64的倍数
    res = ""
    bin_key = input_key_judge(str2bin(key))         # 得到密钥得二进制比特流 64的倍数
    tmp = re.findall(r'.{64}', bin_content)         # 单次加密只能实现8个字符，匹配为每64一组的列表
    for i in tmp:
        res += des_encrypt_one(i,bin_key)           # 将每个字符加密后的结果再连接起来
    return res

# 解密起始函数
def decodeOfDES(content,key):
    bin_content = deal_content(str2bin(content))    # 得到明文的二进制比特流  64的倍数
    res = ""
    bin_key = input_key_judge(str2bin(key))         # 得到密钥得二进制比特流 64的倍数
    tmp = re.findall(r'.{64}', bin_content)         # 单次加密只能实现8个字符，匹配为每64一组的列表
    for i in tmp:
        res += des_decrypt_one(i,bin_key)           # 将每个字符加密后的结果再连接起来
    return res

# DES加解密功能选择
def get_mode():
    mode = eval(input("请选择对应的功能：1.使用DES加密 2.使用DES解密：\n"))
    if mode == 1:
        key = input("请输入8个字符的加密密钥：\n").replace(' ', '')
        encodeOfStrig = encodeOfDES(content=getFile(), key=key)
        out_encodeOfString = bin2str(encodeOfStrig)
        print("加密后的内容:"+ out_encodeOfString)
        saveFile(out_encodeOfString)
    elif mode == 2:
        key = input("请输入8个字符的解密密钥：\n").replace(' ', '')
        out_decodeOfString = decodeOfDES(content=getFile(), key=key)
        print("解密后的内容："+ out_decodeOfString)
        saveFile(out_decodeOfString)
    else:
        print("选择功能错误，请重新选择！")
        get_mode()

if __name__ == '__main__':
    while True:
        get_mode()

```

> 
DES_BOX


```
# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 9:40
# @Author  : H3rmesk1t
# @FileName: DES_BOX.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/LYJ20010728/
IP_table = [58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]

IP_re_table = [40,8, 48, 16, 56, 24, 64, 32, 39,
             7, 47, 15, 55, 23, 63, 31, 38, 6,
             46, 14, 54, 22, 62, 30, 37,5, 45,
             13, 53, 21, 61, 29, 36, 4, 44, 12,
             52, 20, 60, 28, 35, 3, 43, 11, 51,
             19, 59, 27, 34, 2, 42, 10, 50, 18,
             58, 26, 33, 1, 41,9, 49, 17, 57, 25]

E  = [32, 1,  2,  3,  4,  5,  4,  5,
       6, 7,  8,  9,  8,  9, 10, 11,
      12,13, 12, 13, 14, 15, 16, 17,
      16,17, 18, 19, 20, 21, 20, 21,
      22, 23, 24, 25,24, 25, 26, 27,
      28, 29,28, 29, 30, 31, 32,  1]

P = [16,  7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26,  5, 18, 31, 10,
     2,  8, 24, 14, 32, 27,  3,  9,
     19, 13, 30, 6, 22, 11,  4,  25]

S = [[14, 4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
     0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
     4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
     15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13 ],

    [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
     3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
     0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
     13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9],

    [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
     13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
     13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
     1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12 ],

    [7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11,  12,  4, 15,
     13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,9,
     10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
     3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14],

    [2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
     14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
     4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
     11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3],

    [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
     10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
     9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
     4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13],

    [4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
     13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
     1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
     6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12],

    [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
     1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
     7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
     2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]

#key
PC_1 = [57, 49, 41, 33, 25, 17,9,
       1, 58, 50, 42, 34, 26, 18,
      10,  2, 59, 51, 43, 35, 27,
      19, 11,  3, 60, 52, 44, 36,
      63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
      14,  6, 61, 53, 45, 37, 29,
      21, 13,  5, 28, 20, 12, 4]

PC_2 = [14, 17, 11, 24,  1,  5,  3, 28,
      15,  6, 21, 10, 23, 19, 12,  4,
      26,  8, 16,  7, 27, 20, 13,  2,
      41, 52, 31, 37, 47, 55, 30, 40,
      51, 45, 33, 48, 44, 49, 39, 56,
      34, 53, 46, 42, 50, 36, 29, 32]

#秘钥左移的位数
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

```
