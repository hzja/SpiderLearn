# 原创
：  【音频隐写提取】MP3Stego下载、命令、使用方法

# 【音频隐写提取】MP3Stego下载、命令、使用方法

**目录**

[一、介绍：](#%E4%B8%80%E3%80%81%E4%BB%8B%E7%BB%8D%EF%BC%9A)

[二、下载：](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[2.1、 下载地址：](#2.1%E3%80%81%20%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%EF%BC%9A)

[2.2、官网：](#2.2%E3%80%81%E5%AE%98%E7%BD%91%EF%BC%9A)

[三、命令：](#%E4%B8%89%E3%80%81%E5%91%BD%E4%BB%A4%EF%BC%9A)

[3.1、选项：](#3.1%E3%80%81%E9%80%89%E9%A1%B9%EF%BC%9A)

[四、使用方法：](#%E5%9B%9B%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[4.1、第一步：准备好hidden文件](#4.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%87%86%E5%A4%87%E5%A5%BDhidden%E6%96%87%E4%BB%B6)

[4.2、 第二步：将要提取到文件下](#4.2%E3%80%81%20%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%B0%86%E8%A6%81%E6%8F%90%E5%8F%96%E5%88%B0%E6%96%87%E4%BB%B6%E4%B8%8B)

[4.3、第三步：打开命令提示符，并进入到文件](#4.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%89%93%E5%BC%80%E5%91%BD%E4%BB%A4%E6%8F%90%E7%A4%BA%E7%AC%A6%EF%BC%8C%E5%B9%B6%E8%BF%9B%E5%85%A5%E5%88%B0%E6%96%87%E4%BB%B6)

[4.3.1、方法一：](#4.3.1%E3%80%81%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A)

[4.3.2、方法二：](#4.3.2%E3%80%81%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A)

[ 4.4、第四步：输入提取命令](#%C2%A04.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E8%BE%93%E5%85%A5%E6%8F%90%E5%8F%96%E5%91%BD%E4%BB%A4)

[4.5、第五步：分析结果](#4.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E7%BB%93%E6%9E%9C)

---


 

---


## 一、介绍：

> 
十年前， 音频文件的数据嵌入技术发展缓慢， 即使是现在， 也只有少数几个数据隐藏或隐写工具支待常见的压缩音频文件（如MP3或AAC)数据嵌入。 最著名的就是MP3Stego, 它采用一种特殊的量化方法， 并将数据隐藏在MP3文件的奇偶校验块中。MP3编码器将wav文件和一个要隐藏的载荷文件作为输入， 生成一个新的mp3文件。 这种方法最显著的局限性在于载荷文件不能太大。 例如， 一个6MB的全频谱波形音频文件最多只能嵌入6KB的信息， 嵌入率约为0.1%


## 二、下载：

> 
<h3>2.1、 下载地址：</h3>
[Index of /fabien/software (petitcolas.net)<img alt="icon-default.png?t=M3K6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://www.petitcolas.net/fabien/software/](https://www.petitcolas.net/fabien/software/)
<h3>2.2、官网：</h3>
[MP3Stego (petitcolas.net)<img alt="icon-default.png?t=M3K6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://www.petitcolas.net/steganography/mp3stego/](https://www.petitcolas.net/steganography/mp3stego/)


### 2.2、官网：

## 三、命令：

> 
<h3>3.1、选项：</h3>
         -X        提取隐藏数据<br/>           -P &lt;text&gt;        用密码用于嵌入<br/>           -A        编写AIFF输出PCM声音文件<br/>           -s &lt;sb&gt;        仅在此SB（仅调试）<br/>           inputBS        编码音频的输入位<br/>           outPCM        输出PCM声音文件（DFLT输入+.AIF | .pcm）<br/>           outhidden        输出隐藏的文本文件（dflt inputbs+.txt）


## 四、使用方法：

> 
<h3>4.1、第一步：准备好hidden文件</h3>
（就是将音频文件里面隐藏了东西的音频）
[【音频隐写】S-TOOLS具体使用步骤（准备+载体+分析+hidden+加密+对比）、附下载链接<img alt="icon-default.png?t=M3K6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.0/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M3K6"/>https://blog.csdn.net/qq_53079406/article/details/124677358?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/124677358?spm=1001.2014.3001.5501)




> 
<h3>4.2、 第二步：将要提取到文件下</h3>
 放到和Decode.exe同一目录中





> 
<h3>4.3、第三步：打开命令提示符，并进入到文件</h3>
<h4>4.3.1、方法一：</h4>
右键文件夹里面的空白处选择Open in Windows Terminal

就进入到了Windows PowerShell
（直接在当前目录了）


<hr/>


<h4>4.3.2、方法二：</h4>
win+R  cmd（或直接搜cmd）
直接将路径复制粘贴进去




#### 4.3.2、方法二：

> 
<h3> 4.4、第四步：输入提取命令</h3>
.\Decode.exe -X -P 1111 hidden.WAV
-X是提取隐藏文件
-P是密码
111为文件隐藏时的密码
 hidden.WAV是要提取的文件





> 
<h3>4.5、第五步：分析结果</h3>
Will attempt to extract hidden information（将尝试提取隐藏的信息）
输出为hidden.wav.txt（命名：使用原音频名）


<hr/>

我的没有找出隐藏文件（没有输出对应的txt文件）
我在20M文件里隐藏了一个英文单词，找不到也正常



