# 原创
：  upload-labs详解1-19关通关全解（最全最详细一看就会）

# upload-labs详解1-19关通关全解（最全最详细一看就会）

upload-labs是一个使用php语言编写的，专门收集渗透测试过程中遇到的各种上传漏洞的靶场。旨在帮助大家对上传漏洞有一个全面的了解。目前一共19关，每一关都包含着不同上传方式。

1.png:

```
&lt;?php phpinfo();?&gt;

```

### Pass-01

选择一个php文件，发现无法上传。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3e0151fc72c4415ca42ea67fa344342b.png"/><br/> 查看提示说是使用js对不合法文件进行检查，看到是前端验证就很开心了，如同虚设。<br/> **方法一**<br/> 直接禁用js就可以上传了，以火狐浏览器为例，按f12，在‘调试器’面板最右边有个设置按钮，禁用js。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/34ccba663b614d7fb94db736109f8ab1.png"/><br/> 禁用js后上传原先的文件就可以直接上传了,右键图片复制图片链接，成功上传<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f73285daa7304edcab20235c988eb46b.png"/><br/> 不过在实战中直接禁用js插件会导致一些页面无法正常显示，还是存在着一些缺陷，所以这种方法打打靶场就OK了。<br/> **方法二**<br/> 右键查看网页源代码 — 复制全部代码 — 将代码放在一个txt文件中 — 将后缀改为html — 用notepad++打开 — 找到js代码并删除（删除红框里的代码）<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/eac7c9976d0641709b8755ce029f19bd.png"/><br/> 然后在在上面添加一段action，地址是要将图片上传到哪的地址，我们在这加上来（如果不知道这个地址是什么，就回到最开始正常的上传页面，按F12,然后随便上传一个图片，在"网络"模块中可以找到）<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ff7bb4b8b5804635bc246fe4e77237f4.png"/><br/> 然后用浏览器打开这个html文件，直接进行上传操作即可。<br/> **方法三**<br/> 使用burpsuite工具抓包，直接修改后缀名为.php然后点击Forward即可完成上传<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/383d334fcb7849ff9bc29a81dc6e30e1.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9572aef4cd284e73874e9928d181f7cb.png"/>

### Pass-02

查看提示看到是在服务端对数据的MIME进行检查，MIME验证就是验证文件的类型。所以我们的思路就是用burp抓包然后修改文件的类型。<br/> 上传一个1.php文件，用burp抓包。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/14c3bd546c5a4f4187f09920fcbf1ad6.png"/><br/> 抓包后修改红框里的内容，Content-Type就是文件类型，通过关卡查看源码可以看到允许上传的类型有三种：image/jpeg、image/png、image/gif，将红框里的内容改为其中一种就可以成功上传文件<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ebc972d083784facbdb74fa7dcf8ead6.png"/>

### Pass-03

查看源码发现是黑名单验证，禁止上传这四种后缀的文件<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/87fa565b3e2d41e5b506527619c5203b.png"/><br/> 这时候我们就要想办法绕过，在网上查了一下，说黑名单规则不严谨，在某些特定环境中某些特殊后缀仍会被当作php文件解析 php、php2、php3、php4、php5、php6、php7、pht、phtm、phtml。我们这里用.php7试一下，直接上传一个名为1.php5的文件，可以发现直接上传成功<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/32f82d376c574e2a871ebc48325061d1.png"/><br/> 注：有一些使用phpstudy搭建的upload-labs可能无法加载出这个页面，这是因为phpstudy的配置文件需要修改，打开phpstudy的httpd-conf配置文件，修改 `#AddType application/x-httpd-php .php .phtml` 为 `AddType application/x-httpd-php .php .phtml .php5 .php3`，注意前面的#要删除，这时即可正常访问图片地址。

### Pass-04

查看关卡源码，发现黑名单比第三关多了很多<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/31f4416185f941a1bd40d4edf7f3f95f.png"/><br/> 这些后缀的都无法上传，这时候就要用到传说中的.htaccess文件上传了。<br/> 首先创建一个.htaccess文件（文件名就为.htaccess）内容如下

```
AddType application/x-httpd-php .png

```

意思就是如果文件里面有一个后缀为.png的文件，他就会被解析成.php。先上传一个1.png文件，然后上传这个.htaccess，再访问1.png，完美通关。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c95c502e3124422296161ffb8f197267.png"/>

### Pass-05

查看源码，和第四关对比，发现这关没有转换大小写的代码<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/54c0808eb0ae4ac2a8e6309b8d2b9447.png"/><br/> 这样我们就可以上传大小写混合的后缀名来进行绕过。上传一个5.Php文件，直接上传成功。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/bdd8c5aeeb414bdc9682d10874662c3a.png"/>

### Pass-06

查看本关源码，对比第四关，发现没有收尾去空。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2eb4b143b0d546df907e82e5e8d8811d.png"/><br/> 思路就是在文件后面加上空格，但由于windows特性，文件名后空格会被直接删除，不能直接上传.php后加空格，所以我们要用burp抓包然后再添加空格。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5fd7fc4819434bf29430e45ab14b204c.png"/><br/> 上传成功<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2822ffd0f043469ca9d8ceec17b6f0da.png"/>

### Pass-07

查看关卡源码，对比第四关，发现少了删除文件末尾的点<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1dafd9e34ba04bc7aaf3e5075c4dd358.png"/><br/> 和第六关一样，windows文件后缀名不能加’.'，一样使用burp抓包然后后缀加一个点。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/9d4a0f8ba7f7429d96ef313c50445469.png"/><br/> 上传成功<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/87312e3afcd945c0aba517427e851eb4.png"/>

### Pass-08

查看关卡源码，对比第四关，发现少了去除字符串,和前面关卡一样，在burp中抓包在文件名后加::$DATA<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/45a1beecad4c423db332e29a622740a7.png"/><br/> 上传成功<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2f7471b36a0041408561bcd774ca8aa6.png"/>

### Pass-09

查看源码，和前几关相比，本关明显不能按前几关的思路来绕过，仔细看了一下代码，发现没有循环验证，也就是说转换大小写去除空格什么的它只验证一次，所以我的思路是想把后缀改为.phP . .,直接开始实验。<br/> 上传一个9.php抓包<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/345fc3031b534c2cb62172ef2534ed73.png"/><br/> 修改为<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7b7670b8c3a64ee58f9468d71572a527.png"/><br/> 果然上传成功<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/1000d0bc70c04871bebc4eca438eec5c.png"/>

### Pass-10

查看第十关源码，不难看出没有了前几关的验证方式，而且是一个黑名单验证，意思是如果上传了它这些后缀的文件，就会把后缀名删除，没了后缀名也就无法正常解析，不过不需要着急，这关同样只验证一次，所以我们只需要把后缀改为.pphphp，它删除掉中间的php后后缀仍然为php，话不多说直接实验。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4281611c27a948b6a3923d890e66b5a6.png"/><br/> 上传一个10.pphphp，直接上传成功，通关。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/89f8d1d9378245d280b0606d20078eb4.png"/>

### **Pass-11**

查看这关源码，很明显是一个白名单上传，它只允许上传它给定的后缀名，关键的代码是这里<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/414ae902379b4a32a5acde117970b56a.png"/><br/> save_path是一个可控的变量，后面还有一个后缀名需要绕过，这个时候需要使用%00截断，不过这个东西已经是旧时代的产物的，所以有使用条件

```
php版本小于5.3.4
php的magic_quotes_gpc为OFF状态

```

满足条件后先上传一个.png文件开始抓包，在save_path这里修改<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/036146b1bf264606a5fa70538a57ce70.png"/><br/> 上传成功！<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4a2271a9892b456cbcff529d3522c428.png"/>

### Pass-12

查看源代码，和第十一关对比，发现接受值变成了post，那么思路就和第十一关一样，不过post方式不会自行解码，所以要对%00进行urldecode编码<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/fa45250f44ea4468b1a9695d733188f7.png"/><br/> burp可以进行快捷编码，选中%00右键convert selection即可进行快速url编码<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0b91e2129b584092b2a81f0d8e56ed66.png"/><br/> 上传成功，通关。

### Pass-13

查看提示，说检查图片内容开头两个字节，所以要想到用图片+php来组成一个图片马，可以直接用notepad打开一个图片在后面添加代码组成图片马，也可以使用cmd命令。

```
copy 13.jpg /b + 13.php /a webshell.jpg

```

意思是将13.php中的代码追加到13.jpg中并重新生成一个叫webshell.php的代码。<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/df85326060bb4dd7b83ec3810659f234.png"/><br/> 然后上传这个文件，因为是文件包含漏洞，地址加上file<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/121c09ee89864f409bd3360a9b4178ee.png"/><br/> 拿下

### Pass-14

查看源码，关键函数是这个getimagesize<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c936898ae99a486baba59d4cae549dec.png"/><br/> getimagesize函数会对目标的十六进制的前几个字符串进行读取。比如GIF的文件头问GIF89a，png的文件头为塒NG。所以这关和第十三关一样，我们只需要用notepad打开图片马，在前面加上GIF89A，保存为webshell.gif<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/eff8410b0b4740348953a4b6777d96d9.png"/><br/> 然后直接上传成功。用文件包含漏洞打开图片<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a1ffbfe09f5c4643b0b0d8fbbd698374.png"/>

### Pass-15

查看源码，看到这个函数，exif_imagetype() 读取一个图像的第一个字节并检查其签名。过程和13,14关一样，不过需要打开php_exif<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/abf982dc65244077bd47bfbc93143edf.png"/>通关。

### Pass-16

查看提示发现有重新渲染，查看源码<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/828be07d3ef247c5ac541c9c943ffe00.png"/><br/> imagecreatefromjpeg（）函数，二次渲染是由Gif文件或 URL 创建一个新图象。成功则返回一图像标识符/图像资源，失败则返回false，导致图片马的数据丢失，上传图片马失败。<br/> 按照前几关的方式上传，可以上传，但是包含漏洞无法解析。原因就是二次渲染将图片马里面的php代码删了。接下来把原图和修改后的图片进行比较，看哪里没有被渲染，在这里插入php代码。推荐使用[beyond compare](https://www.beyondcomparepro.com/download)。为了方便大家测试，这里再推荐网上大佬的二次渲染专用图片`https://wwe.lanzoui.com/iFSwwn53jaf`<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0d86f77e877f43bf8a9cf86ad5c993c8.png"/><br/> 把上传的图片在右键保存本地，看没有被渲染的地方，加入php代码<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4e9079490dc74395854c7a6e2ffc4215.png"/><br/> 再重新上传<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/7c3f679e9c444d91ab1fe9068eb96be4.png"/><br/> 通关

### Pass-17

打开提示，让我进行代码审计？看来和前面都不一样，答案藏在源码中。来看看代码<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d60ecbe6f0324ec99fcc44ad6c7a33ec.png"/><br/> 发现如果上传的符合它的白名单，那就进行重命名，如果不符合，直接删除！解析的机会都没有，这让我想到了条件竞争，如果我在它删除之前就访问这个文件，他就不会删除了。接下来直接实验<br/> 上传一个php文件，然后burp抓包发到爆破模块<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/479097ec42944a47b66ad7a558f449ce.png"/><br/> 如图进行修改<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/0f95aa8ba5b34e459a42987fb8296282.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/aa4ed550523944919a61163f84c9922e.png"/><br/> start attack发包，然后用浏览器一直访问1.php，按F5一直刷新，如果在上传的瞬间访问到了，它就无法删除。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f6bb79216cab48308812ae6dc954777f.png"/><br/> 通关

### Pass-18

这关不知道是作者的什么原因，导致这里有个错误。上传的图片放不到upload下，这里进行一个小小的改动。打开18关的myupload.php<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3a4c98de66454ed4ad490a97cf0c07ff.png"/><br/> 修改为这样然后保存重启靶场就OK了<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3f6810a42629488e8b48851ae8e9b723.png"/><br/> 继续来通关，查看代码，发现和第17关的差距是，这关还检测了后缀名，不能直接上传php文件，所以这关要上传图片马，其他步骤和17关类似。访问图片时使用文件包含。<br/> 上传22.gif然后抓包<br/> 和17关一样的过程，进行start attack。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/967fe135a71c43d79d42e9ea7da977dd.png"/><br/> 完美通关

### Pass-19

看到19关的页面，明显比前面的多了点东西，多了一个保存名称，没有对上传的文件做判断，只对用户输入的文件名做判断。查看源码，有move_uploaded_file()这样一个函数，它有一个特性，会忽略到文件末尾的/.<br/> 直接上传1.png，抓包，在末尾加上/.<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/fcbddcb07a174567be7c883a7289f683.png"/><br/> 直接放包，上传成功<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/a5c7b0ba78434f0292a9f7f954222580.png"/><br/> 注:move_uploaded_file()函数中的img_path是由post参数save_name控制的，所以这一关还可以在save_name利用%00截断，这个方法前面已经说过了不再赘述，注意php版本要小于5.3

以上就是upload-labs靶场19关全部的通关技巧，我还看到别人的有二十多关，不过我找到的只有19关，不论有多少关，方法都大差不多，在实战中没有代码只能做黑盒测试，只能使用这些办法去一个个测试，希望能帮助到大家的学习，才学疏浅，如果有错误还请多多指正。
