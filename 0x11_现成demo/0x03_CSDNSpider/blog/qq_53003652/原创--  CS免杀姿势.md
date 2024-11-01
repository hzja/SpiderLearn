# 原创
：  CS免杀姿势

# CS免杀姿势

### 一：环境

1.公网vps一台<br/> 2.Cobalt Strike 4.7<br/> 3.免杀脚本<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/418e0c8a250552f16eb72751586cad27.jpeg"/>

### 二：生成payload

生成一个payload<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/2442adf9de807154653d77fd219db76e.jpeg"/><br/> c格式的x64位payload<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d76d149ce83d742a23f135019a292376.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/5f5fc3a1625338a1049288735effb573.jpeg"/>

### 三：免杀

下载免杀脚本<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/88d36f2b31df83ce70f80989d160fd6d.jpeg"/><br/> .c打开是这样的<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/223080566b66e851d037ad095387fb83.jpeg"/><br/> 把双引号里面的内容复制出来，放到脚本目录下的1.txt<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/35d5aeafd496420134dd5fda36eead6b.jpeg"/><br/> 运行生成器.py<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/f9fef7769411a3e917ecd41b8db3ae9c.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/b6e9b8cd474b1248218a7611da09b6bb.jpeg"/><br/> 将这三个文件上传到服务器<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/355b99a3c7b20f15425028fa53526a47.jpeg"/><br/> 服务器用python开个http服务<br/> `python3 -m http.server 8000`<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/4f64f4e9d2614a0f777c931d0559e055.jpeg"/><br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/68be723592f804df627926ddfa78e4bb.jpeg"/><br/> 回到主机，用pyinstaller把loader.py打包成exe<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/7a8e3eae5eaf7100e36c1332075bf645.jpeg"/><br/> 成功后在dist下生成了一个exe文件<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/d91fb0edd24072d4bdf9c817f9451c7d.jpeg"/><br/> 上线的话还需要在exe同目录下存在kygvseedc.txt文件，内容为空就可以了，目的是为了绕过沙箱<br/> <img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/aa454fa285d0ddf135a026160dc26c3e.jpeg"/>

### 四：免杀测试

<img alt="image.png" src="https://img-blog.csdnimg.cn/img_convert/521af017181be7bd9076a82884f5a474.jpeg"/><br/> 稳

### 五：结语

项目地址<br/> [https://github.com/ChinaRan0/ZhiShanGongFangAVV](https://github.com/ChinaRan0/ZhiShanGongFangAVV)<br/> 大家不要放在云沙箱或者直接用杀软单独扫描，这样很快就会让捕捉到不能免杀了。

### 免责声明：

文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行负
