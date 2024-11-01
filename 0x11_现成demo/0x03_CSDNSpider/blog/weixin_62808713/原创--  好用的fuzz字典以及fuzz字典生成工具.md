# 原创
：  好用的fuzz字典以及fuzz字典生成工具

# 好用的fuzz字典以及fuzz字典生成工具

## 一、fuzz字典下载地址

[https://github.com/fuzzdb-project/fuzzdb](https://github.com/fuzzdb-project/fuzzdb)

[https://github.com/TheKingOfDuck/fuzzDicts](https://github.com/TheKingOfDuck/fuzzDicts)

[https://github.com/TuuuNya/fuzz_dict](https://github.com/TuuuNya/fuzz_dict)

[https://github.com/jas502n/fuzz-wooyun-org](https://github.com/jas502n/fuzz-wooyun-org)

## 二、fuzz字典生成工具

#### 前言

学习xss的时候翻阅资料发现了一个文件上传漏洞fuzz字典生成脚本小工具，试了试还不错，分享一下

#### 配置

需要python2环境

工具地址:[https://github.com/c0ny1/upload-fuzz-dic-builder](https://github.com/c0ny1/upload-fuzz-dic-builder)

#### 使用方法

```
$ python upload-fuzz-dic-builder.py -h
usage: upload-fuzz-dic-builder [-h] [-n] [-a] [-l] [-m] [--os] [-d] [-o]

optional arguments:
  -h, --help            show this help message and exit
  -n , --upload-filename
                        Upload file name
  -a , --allow-suffix   Allowable upload suffix
  -l , --language       Uploaded script language
  -m , --middleware     Middleware used in Web System
  --os                  Target operating system type
  -d, --double-suffix   Is it possible to generate double suffix?
  -o , --output         Output file
```

上传文件名（-n），允许的上传的后缀（-a），后端语言（-l），中间件(-m),操作系统（–os），是否加入双后缀（-d）以及输出的字典文件名（-o）。我们可以根据场景来生成合适的字典，提供的信息越详细，脚本生成的字典越精确。

```
python upload-fuzz-dic-builder.py -l php -m apache --os win
```

然后用burpsuite抓包，放入intreder模块，选择上一步生成的字典，选择枚举的位置。

注意:如图模块不用勾选。

最后:start attack即可，观察跑的结果，进行进一步利用。

#### 最后个人想法

可以自定义中间件，后端语言，系统，来生成fuzz，要是手工测试的会很累，精确的还行，就是跑的还是蛮多的，对服务器还是有影响，我本地跑的，生成了很多的图片，所以肯定没有手工注入准确，最后，这个工具还是很不错的，感觉可以的可以尝试一下。

#### 参考地址

[https://www.bbsmax.com/](https://www.bbsmax.com/)
