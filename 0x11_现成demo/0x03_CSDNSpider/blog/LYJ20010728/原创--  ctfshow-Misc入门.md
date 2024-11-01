# 原创
：  ctfshow-Misc入门

# ctfshow-Misc入门

#### ctfshow-Misc入门

## 写在前面

> 
后续提取图片中的flag均为脚本提取，部分flag提取出错需要人工再次核验哈~，[flag提取演示](https://blog.csdn.net/LYJ20010728/article/details/119194101?spm=1001.2014.3001.5501)


## 图片篇(基础操作)

### misc1

> 
flag在下载的图片上


### misc2

> 
将后缀名改为`.png`即可在图片上看到flag


### misc3

> 
推荐一款图片浏览器 `Honeyview`，直接可以查看bpg格式的图片


### misc4

> 
用 HxD 依次查看文件头，将后缀名依次改为 `.png`、`.jpg`、`.bmp`、`.gif`、`.tif`、`.webp`，将内容拼接起来即可得到flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f57fcd273abd47d992f8c0c7556c9f51.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/232b4e043c0a4633b37a6df1786c3320.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 图片篇(信息附加)

### misc5

> 
用 `HxD` 打开，拖到尾部即可发现flag


### misc6

> 
用 `HxD` 打开，搜索关键词 `ctfshow` 即可发现flag


### misc7

> 
用 `HxD` 打开，搜索关键词 `ctfshow` 即可发现flag


### misc8

> 
`binwalk` 查看图片发现隐藏图片，利用 `foremost` 提取出来


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/dadf0a0f700143edafb10f24f52fdcbd.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/cb0f464db19d47fa836a09a10f227773.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc9

> 
用 `zsteg` 查看图片，发现flag


#### zsteg (补充)

> 
zsteg安装方法 (补充)


```
更换RubyGems的源
gem sources --remove https://rubygems.org/
gem sources --add https://gems.ruby-china.com/
gem sources -l
安装zsteg
git clone https://hub.fastgit.org/zed-0xff/zsteg.git 
cd zsteg
gem install zsteg

```

> 
zsteg的使用方法 (常见)


```
查看帮助
zsteg -h

查看LSB信息
zsteg pcat.png

检测zlib
# -b的位数是从1开始的
zsteg zlib.bmp -b 1 -o xy -v

显示细节
zsteg pcat.png -v

尝试所有已知的组合
zsteg pcat.png -a

导出内容
zsteg -E "b1,bgr,lsb,xy" pcat.png &gt; p.exe

更多的使用方法可以查看README.md

```

### misc10

> 
用 `binwalk` 查看图片，分离图片，查看数据块即可发现flag，需要注意的是zlib是PNG IDAT的可选压缩格式


### misc11

> 
binwalk 查看发现两个IDAT数据块，尝试删去第一个数据块，查看图片发现flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/68a80e9171774656ac12ff309393b4a5.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b46fe725b6f642c69e4d0d45e2e77f3f.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/e532c5dda59845feb5712be23c712a26.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc12

> 
zsteg查看图片提示数据块异常


> 
测试后发现需要删掉前8个IDAT块


### misc13

> 
`HxD`查看发现图片尾部存在可疑数据，观察发现`{`前面那一串字符从第一位开始每隔一位选取一个字符，连起来就是ctfshow，编写脚本提取flag


```
s="631A74B96685738668AA6F4B77B07B216114655336A5655433346578612534DD38EF66AB35103195381F628237BA6545347C3254647E373A64E465F136FA66F5341E3107321D665438F1333239E9616C7D"
flag=""
for i in range(0,len(s),4):
    flag += s[i]
    flag += s[i+1]
print(flag)

```

### misc14

> 
`binwalk`查看图片，发现JPEG图片，`foremost`和`binwalk`无法成功提取，用`HxD`打开搜索文件头手动提取<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/fbbbf5dbb2e443f3b4fdd8994ad12c1e.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>


### misc15

> 
用`HxD`打开搜索关键词 `ctfshow` 即可发现flag


### misc16

> 
`binwalk`查看图片，发现额外数据，用`binwalk -e`提取出来，查看提取出来的文件发现flag


### misc17

> 
`binwalk`提取出来的东西解不出，尝试 `zsteg`，根据提示提取信息得到PNG图片，查看图片发现flag


### misc18

> 
用 `exiftool` 查看图片，flag在标题、作者、照相机和镜头型号里


### misc19

> 
用 `exiftool` 查看图片，flag在主机上的文档名里


### misc20

> 
用 `exiftool` 查看图片，flag在评论里


### misc21

> 
用 `exiftool` 查看图片，将序列号`686578285826597329`转字符得到`hex(X&amp;Ys)`，分别将`X/Y Resolution`和`X/Y Position`转成hex，然后拼接起来，flag为`ctfshow{e8a221498d5c073b4084eb51b1a1686d}`


### misc22

> 
直接查看图片没有发现什么，但是用 `Honeyview`浏览缩略图时发现数据


> 
利用 `MagicEXIF` 查看图片，flag为`ctfshow{dbf7d3f84b0125e833dfd3c80820a129}`


### misc23

> 
用`exiftool`看一下发现有好几个历史时间，`History Action`中有提示


> 
将给出的四个时间的时间戳转换出来，分别hex后拼在一起，[转换地址](https://tool.chinaz.com/tools/unixtime.aspx)


### misc41

> 
提示中的`F001`是突破点，`HxD` 查看图片发现有有大量`F001`组成了某种形状


> 
把`F001`出现过的位置中所有十六进制的值单独截取出来，每四位分隔开，把F001替换成0，其他值替换成空格，得到一张含有flag的图片，这里也可以采用`CyberChef`来解决问题，flag为`ctfshow{fcbd427caf4a52f1147ab44346cd1cdd}`


## 图片篇(文件结构)

### misc24

> 
用`HxD`查看一下图片，文件头占了53个字节，文件尾的位置在675053字节处 (后面两个字节是windows的”补0”)，因为每个像素点由3个字节 (十六进制码6位) 表示，每个字节负责控制一种颜色，分别为蓝（Blue）、绿（Green）、红（Red），所以文件真实的像素大小为：`(675053-53)/3=225000`


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ced708b85c2145b6866d5398c5e03249.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6ca3b37807534c03a64fc3be3252630c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
题目给的图片是`900*150=135000`个像素大小


> 
尝试后发现这题的宽度是对的，所以正确的高度是`225000/900=250`，将高度改成


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0a1c52667d4c4b928f3f9bee647e0500.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ec50faf3f2e24181887b2da017317ebc.bmp?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc25

> 
用`TweakPNG`查看图片发现图片的CRC值不对，猜测应该是修改了宽高，用脚本跑一下看看


> 
根据脚本计算出来的值修改宽高，保存后即可看到flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c68d12defa1f4a428157ec9931730a37.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/61a83bd4a86a4a6398e3d1297453ed70.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc26

> 
用`TweakPNG`查看图片发现图片的CRC值不对，和上一题一样用脚本跑一下看看


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3c65333664cd44ddb88bbb43a61081a0.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/49fa416912954d97b376619d56b83f8a.png#pic_center"/>

> 
根据脚本计算出来的值修改宽高，保存后即可看到flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/25f595c7f9d74b9e875beb5fb6c5e2f9.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/6050e89576e646cf8b9c45e9199f1af1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc27

> 
根据提示，猜测依旧是修改图片高度，将高度改高后即可发现flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/116ab84b182f4838b131e260faaa50d3.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b37accd8b35642768195014037185eee.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc28

> 
根据提示，猜测依旧是修改图片高度，将高度改高后即可发现flag，但是需要注意从预览图中能看到flag，但是直接打开看不到，可以使用图片编辑器或者Stegsolve打开


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/35837cf925ab410aa3fb6fea6fe50a6d.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1ab09ce6d1c545e9a04422ac518de9ca.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/8cbb82e5590a48a284aaeaa38808e918.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc29

> 
GIF有很多帧，将每一帧的高度都改高后，用`Stegsolve`查看，在第八帧即可发现flag


### misc30

> 
根据提示修改BMP图片宽度即可发现flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/45f9c68dc4ef460e975a3f07189b9ff1.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/463de4f25fc646fea7e2bc1a5394e690.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc31

> 
根据题给描述，计算正确宽度


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/201eed53c8c0414b8e4bea885d4e8839.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/fda996e4a3f84cd7b88d3ee03747b571.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc32

> 
根据题给描述，计算出正确的高宽


```
import zlib
import struct

# 同时爆破宽度和高度
filename = "misc32.png"
with open(filename, 'rb') as f:
    all_b = f.read()
    data = bytearray(all_b[12:29])
    n = 4095
    for w in range(n):
        width = bytearray(struct.pack('&gt;i', w))
        for h in range(n):
            height = bytearray(struct.pack('&gt;i', h))
            for x in range(4):
                data[x+4] = width[x]
                data[x+8] = height[x]
            crc32result = zlib.crc32(data)
            #替换成图片的crc
            if crc32result == 0xE14A4C0B:
                print("宽为：", end = '')
                print(width, end = ' ')
                print(int.from_bytes(width, byteorder='big'))
                print("高为：", end = '')
                print(height, end = ' ')
                print(int.from_bytes(height, byteorder='big'))


```

> 
修改宽高保存后即可看到flag<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bd8df0e67a2e49b5b1b13ad587e1a22c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d555acfe3e3d488596106c84e9a609bd.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>


### misc33

> 
根据题给描述，计算出正确的高宽


> 
修改宽高保存后即可看到flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3b21ebb00a4b4856b8b51119af80c661.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ced1640e265f4ef7888a712a80ab876c.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc34

> 
利用脚本把生成的所有图片都保存下来了，观察哪个是正常的


```
import zlib
import struct
filename = r"C:\Users\95235\Downloads\misc34\misc34.png"
with open(filename, 'rb') as f:
    all_b = f.read()
    #w = all_b[16:20]
    #h = all_b[20:24]
    for i in range(901,1200):
        name = str(i) + ".png"
        f1 = open(r"C:\Users\95235\Downloads\misc34\\" + name,"wb")
        im = all_b[:16]+struct.pack('&gt;i',i)+all_b[20:]
        f1.write(im)
        f1.close()

```

### misc35

> 
先把图片基础的高度调高一点（高度在600，宽度在993-1000这个范围内都可以得到flag），才能看到flag


```
import zlib
import struct
filename = r"C:\Users\95235\Downloads\misc35\misc35.jpg"
with open(filename, 'rb') as f:
    all_b = f.read()
    #w = all_b[159:161]
    #h = all_b[157:159]
    for i in range(901,1200):
        name = str(i) + ".jpg"
        f1 = open(r"C:\Users\95235\Downloads\misc35\\" + name,"wb")
        im = all_b[:159]+struct.pack('&gt;h',i)+all_b[161:]
        f1.write(im)
        f1.close()

```

### misc36

> 
和上一题一样先把图片基础的高度调高一点，脚本爆破即可，用照片编辑器查看gif文件


```
import zlib
import struct
filename = r"C:\Users\95235\Downloads\misc36\misc36.gif"
with open(filename, 'rb') as f:
    all_b = f.read()
    for i in range(920,951):
        name = str(i) + ".gif"
        f1 = open(r"C:\Users\95235\Downloads\misc36\\" + name,"wb")
        im = all_b[:38]+struct.pack('&gt;h',i)[::-1]+all_b[40:]
        f1.write(im)
        f1.close()

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/41c08ab4455345958fe15f4e45a1f988.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a266a23f5b46402297d989023c885bc7.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc37

> 
用`Stegsolve`查看，flag在`8、14、21、31、34`帧中，拼接起来即可


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ad8606589a7c4ea38c769a65d0ffe4e2.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f80c2d6ba5044cb99a1c3c075475b7a6.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5a8d4c5785be4a118ca62bfb2f282269.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5093da1bc17541b9a9cd55a2a5b778bb.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc38

> 
题目所给的是apng图片，可以使用APNG Disassembler来把每一帧分离出来，`9、17、36、40`帧中藏有flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/726d92cb93ac4f899ab7a2d58d71d520.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/344ebfcff6b14e60a6c247bb329aa8d6.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/504b68bfb20142c6b16f29ede03e0691.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5f4b2d6e50c04e78ac958a9289d658b4.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc39

> 
这里是利用不同帧之间的间隔时间来隐写的，利用`identify`来处理该GIF图片


```
安装命令：
sudo apt-get install imagemagick

```

> 
提取命令：`identify -format "%T " misc39.gif &gt; 1.txt`，得到的一串36和37


> 
把37换成1、36换成0，得到长度为287的二进制字符串，由于无法整除8，考虑7位一组，转换成字符得到flag


### misc40

> 
文件识别为`apng`文件，使用工具`APNG Disassembler`，flag在记录详细信息的txt文件中，用脚本把flag提取出来


### misc42

> 
根据提示，用`tweakpng`打开图片，发现IDAT块的长度很可疑，有一部分IDAT块的长度转换为字符是`ctfshow`，将后面的接着转换成字符即可得到flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1918a998817140d9a43693f6a232e00e.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ce3873df70fd483a9b2eac8d782a8259.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc43

> 
根据题给描述，先用tweakpng打开分析一下图片，发现报了一堆错，使用`pngdebugger`分析，发现所有IDAT块的crc32值都是错误的


> 
将错误的IDAT块的`crc-code`提取出来，拼接起来转字符串即可得到flag


```
import binascii
def hex_to_str(s):
    hex = s.encode('utf-8')
    str_bin = bin
    str_bin = binascii.unhexlify(hex)
    return str_bin.decode('utf-8')

s = 'E59387E593A62E63746673686F777B36656232353839666666663565333930666536623837353034646263303839327D'
hex_to_str(s)

```

### misc44

> 
根据提示，用`PNGDebugger`打开，把信息导入到txt文件中


> 
利用脚本把`CRC OK`的替换成1，`CRC FAILED`替换成0，注意先把前十行的内容删去，再把最后四行删去


### misc45

> 
根据题给描述，猜测是文件转换，测试后发现转成`.bmp`格式后，用`binwalk`提取即可，看大师傅的blog发现考察点是`png和bmp像素点的读取方式`


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/e7bdf6f8e69d4fef8084a75501bd6787.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/b92a1caa7c9248adb94fc4d748a625f0.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### misc46

> 
根据题给描述，搜索后猜测应该是画图之类的，先提取出GIF的详细信息


```
identify misc46.gif &gt; message.txt 

```

> 
观察得到的信息，其中`0+0、174+49、196+47`这些是偏移量，用其来进行画图


```
坐标提取：

f = open(r"C:\Users\95235\Downloads\misc46\message.txt","r")
x = f.readlines()
f.close()

f = open(r"C:\Users\95235\Downloads\misc46\out.txt","w")
for i in x:
    f.write(i.split("+")[1])
    f.write(" ")
    f.write(i.split("+")[2][:2])
    f.write("\n")
f.close()

```

> 
根据得到的点坐标进行绘图


### misc47

> 
测试后发现是apng格式，解题的思路是根据每一个IDAT块前面的一个fcTL块中包含的水平垂直偏移量


```
import struct
from PIL import Image
import matplotlib.pyplot as plt
f = open(r'C:\Users\95235\Downloads\misc47\misc47.png','rb')
c = f.read()
c = c[c.index(bytes.fromhex('6663544C00000001')):]
pp = []
for i in range(1,1124,2):
    start = c.index(bytes.fromhex('6663544C0000')+struct.pack('&gt;h',i))
    fc = c[start:start+30]
    print(fc[18:20],fc[22:24])
    print(struct.unpack('&gt;h',fc[18:20])+struct.unpack('&gt;h',fc[22:24]))
    pp.append(struct.unpack('&gt;h',fc[18:20])+struct.unpack('&gt;h',fc[22:24]))
img = Image.new('RGB',(400,70),(255,255,255))
for i in pp:
    new = Image.new('RGB',(1,1),(0,0,0))
    img.paste(new,i)
plt.imshow(img)
plt.show()

```

### misc48

> 
用`010 editor`打开，发现提示`统计FF的数量再减去1、ctfshow{}中包含32个字符`


> 
因为flag长度是32位，所以只需要统计前32个段就行


```
0 12 11 0 7 10 13 13 9 0 9 13 0 13 6 0 10 9 2 1 0 1 10 8 11 5 12 7 2 2 3 10

```

> 
分别转换成hex即可


```
s = [0,12,11,0,7,10,13,13,9,0,9,13,0,13,6,0,10,9,2,1,0,1,10,8,11,5,12,7,2,2,3,10]
f = '0123456789abcdef'
flag = 'ctfshow{'
for i in range(len(s)):
    flag += f[s[i]]
flag += '}'
print(flag)

```

### misc49

> 
用`010 editor`打开，`FFE`后面的就是flag的值


## 图片篇(颜色通道)

### misc50

> 
由于是颜色通道篇的，很自然想到用`Stegsolve`查看一下，


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/db4a1fb1cb4043e9865a7db0f44c8801.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/34482ae993f8434ab9fdf079bb56ce32.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/57f78f14be394f17b1e1bb949be08820.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
