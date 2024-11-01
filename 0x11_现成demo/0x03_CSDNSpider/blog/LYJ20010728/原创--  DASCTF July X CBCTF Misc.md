# 原创
：  DASCTF July X CBCTF Misc

# DASCTF July X CBCTF Misc

#### DASCTF July X CBCTF Misc

## 问卷题

> 



## red_vs_blue

> 



```
from pwn import *
context.log_level = 'debug'

num = 0
p = remote('node4.buuoj.cn',27291)
resultsList = ['r' for res in range(66)]

while 1:
    p.recvuntil('choose one [r] Red Team,[b] Blue Team:\n')
    while 1:
        p.sendline(resultsList[num])
        choice = p.recvline()
        result = p.recvline()
        if choice[-9:] == result[-9:]:
            num += 1
            if num == 66:
                print(p.recvline())
                print(p.recvline())
                print(p.recvline())
                print(p.recvline())
                break
            else:
                p.recvuntil('choose one [r] Red Team,[b] Blue Team:\n')
        else:
            resultsList[num] = 'b'
            num = 0
            p.sendline('y')
            break

```

## funny_maze

> 



```
import re
import sys
from pwn import *
context.log_level = 'debug'

sys.setrecursionlimit(10000)

class Point:
    def __init__(self, x, y, _):
        self.x = x
        self.y = y
        self._ = _
        self.sum = 0
        self.next = [x, x, x, x]
        self.next[0] = -1, -1
        self.next[1] = -1, -1
        self.next[2] = -1, -1
        self.next[3] = -1, -1
        self.next_list = [-1, -1, -1, -1]
    # 记录相邻点的相关数据
    def join(self, x, y, s, e, w):
        if self._ == s or self._ == e or self._ == w:
            if x == self.x + 1 and y == self.y:
                self.next_list[self.sum] = 0
                self.next[0] = x, y
                self.sum += 1
                return 1
            if x == self.x - 1 and y == self.y:
                self.next_list[self.sum] = 1
                self.next[1] = x, y
                self.sum += 1
                return 1
            if x == self.x and y == self.y - 1:
                self.next_list[self.sum] = 2
                self.next[2] = x, y
                self.sum += 1
                return 1
            if x == self.x and y == self.y + 1:
                self.next_list[self.sum] = 3
                self.next[3] = x, y
                self.sum += 1
                return 1
        return 0

def load(path, start, end, way):
    x = 0
    y = 0
    startx = -1
    starty = -1
    endx = -1
    endy = -1
    mapy = []
    for lines in path:
        mapx = []
        for c in lines:
            mapx.append(Point(x, y, c))
            if c == start or c == end or c == way:
                if c == start:
                    startx = x
                    starty = y
                if c == end:
                    endx = x
                    endy = y
                if x &gt; 0:
                    if mapx[x - 1].join(x, y, start, end, way) == 1:
                        mapx[x].join(x - 1, y, start, end, way)
                if y &gt; 0:
                    if mapy[y - 1][x].join(x, y, start, end, way) == 1:
                        mapx[x].join(x, y - 1, start, end, way)
            x += 1
        mapy.append(mapx)
        x = 0
        y += 1
    return mapy, startx, starty, endx, endy

def re_find_the_way(x, y, MAP, map1, map2, end):
    map1[y][x] = 1
    if map2[y][x] == '#':
        map2[y][x] = '.'
    if MAP[y][x]._ == end:
        lengh = 0
        for m1 in map1:
            for m2 in m1:
                if m2 == 1:
                    lengh += 1
        return map1, map2, lengh, 1
    for i in range(MAP[y][x].sum):
        xx, yy = MAP[y][x].next[MAP[y][x].next_list[i]]
        if map1[yy][xx] == 0:
            r1, r2, r3, r4 = re_find_the_way(xx, yy, MAP, map1, map2, end)
            if r4 == 1:
                return r1, r2, r3, r4
            else:
                map1[yy][xx] = 0
                map2[yy][xx] = '#'
    return map1, map2, 0, 0

def find_the_way(path, start, end, way):
    MAP, startx, starty, endx, endy = load(path, start, end, way)
    map1 = []
    map2 = []
    for y in MAP:
        map1_ = []
        map2_ = []
        for x in y:
            map1_.append(0)
            map2_.append('#')
        map1.append(map1_)
        map2.append(map2_)
    map2[starty][startx] = start
    map2[endy][endx] = end
    map1, map2, length, r4 = re_find_the_way(startx, starty, MAP, map1, map2, end)
    return length

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python exp.py ip port flag")
        sys.exit()
    p = remote(sys.argv[1], int(sys.argv[2]))
    FLAG = sys.argv[3]
    list1 = []
    while 1:
        a = p.recvuntil('Introduction to this game\n')
        p.sendline('1')
        while 1:
            try:
                p.recvuntil('#')
            except:
                while 1:
                    a = p.recvline().decode().strip('\n')
                    print(a)
                    if 'flag{' in a:
                        flag = re.findall('flag{(.*?)}', a)
                        if flag[0] == FLAG:
                            print('Pass!')
                        else:
                            print('AssertionError!')
                        sys.exit()
            while 1:
                a = p.recvline().decode().strip('\n')
                print(a)
                if a != '#' and a != 'S':
                    pass
                if a != 'Please enter your answer:':
                    list1.append(a)
                    print(list1)
                    continue
                else:
                    length = find_the_way(list1, 'S', 'E', ' ')
                    p.sendline(str(length))
                    print(length)
                    break

```

## ezSteganography

> 



<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/98e5296a06534c978cbeee46e19b7937.png#pic_center"/><br/> <img alt="请添加图片描述" src="https://img-blog.csdnimg.cn/5e4bc6eb78284fa5b73936f8fbabc360.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBASDNybWVzazF0,size_20,color_FFFFFF,t_70,g_se,x_16"/>

### 非预期解

> 



### 预期解

> 



```
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def extract(delta, y):
    out = []
    for i in (delta / 2 - y % delta):
        if i &gt; 0:
            out.append(1)
        else:
            out.append(0)
    out = np.array(out)
    return out

if __name__ == '__main__':
    imagePath = r'C:\Users\95235\Downloads\ezSteganography-flag.png'
    p = np.array(Image.open(imagePath))
    R, G, B = p[:,:,0], p[:,:,1], p[:,:,2]
    G = G.ravel()
    te_out = extract(20, G)
    plt.imshow(np.array(te_out).reshape(1440,2560))
    plt.show()

```

## Just a GIF

> 



```
import os
from PIL import Image
from tqdm import tqdm

img = Image.open(r'C:\Users\95235\Downloads\gif\Just_a_GIF.gif')
os.mkdir(r'C:\Users\95235\Downloads\gif\png')
for i in range(img.n_frames):
    img.seek(i)
    new = Image.new('RGB', img.size)
    new.paste(img)
    new.save(r'C:\Users\95235\Downloads\gif\png\\' + str(i) + '.png')

os.mkdir(r'C:\Users\95235\Downloads\gif\flag')
path_1 = r'C:\Users\95235\Downloads\gif\flag\\'
path_2 = r'C:\Users\95235\Downloads\gif\png\\'

for i in tqdm(range(11)):
    img = Image.open(path_2 + str(i) + '.png')
    img_1 = Image.new('RGB', (83,83), (255,255,255))
    for h in range(40):
        im = Image.open(path_2 + str((h+1)*11+i) + '.png')
        width, height = img.size
        for j in range(0, width):
            for k in range(0, height):
                tmp = img.getpixel((j,k))
                tmp_1 = im.getpixel((j,k))
                if tmp != tmp_1:
                    img_1.putpixel((j,k), (0,0,0))
    img_1.save(path_1 + str(i+1) + '.png')

```

> 



```
from PIL import Image

a = [7, 1, 6, 9, 3, 4, 5, 2, 8]
f = Image.new("RGB", (83 * 3, 83 * 3))
for i in range(0, 3):
    for j in range(0, 3):
        path = r"C:\Users\95235\Downloads\gif\flag\\" + str(a[i + j * 3]) + ".png"
        x = Image.open(path)
        f.paste(x, (i * 83, j * 83))
f.save(r"C:\Users\95235\Downloads\gif\flag\flag.png")

```

> 



## Nuclear wastewater

> 



```
from PIL import Image

img = Image.open(r"C:\Users\95235\Downloads\Nuclear_wastewater\key.png")
for y in range(img.size[1]):
	list_pix = []
		for x in range(img.size[0]):
			if (y % 10 == 0 and x % 10 == 0):
				list_pix.append(img.getpixel((x,y)))
		if list_pix != []:
			print(list_pix)

```

> 



```
from PIL import Image

pic = Image.open(r'C:\Users\95235\Downloads\Nuclear_wastewater\Nuclear wastewater.png')
w, h = pic.size
list_1 = []

for y in range(0, h, 10):
    for x in range(0, w, 10):
        pixel = pic.getpixel((x, y))
        if pixel == (255, 255, 255):
            continue
        r, g, b = pixel
        list_1.extend([r, g, b])

dict_1 = {}
for i in list_1:
    dict_1[i] = dict_1.get(i, 0) + 1

result = sorted(dict_1.items(), key=lambda x: x[1], reverse=True)
for s in result:
    print(chr(s[0]), end="")

```

> 



> 
发现提示，搜索关键词 “Citrix CTX1” 发现是一种加密方式，继续[在线解密](https://gchq.github.io/CyberChef/)，两次解密即可拿到 Flag

