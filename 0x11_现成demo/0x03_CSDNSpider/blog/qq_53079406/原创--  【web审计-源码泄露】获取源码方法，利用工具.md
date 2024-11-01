# 原创
：  【web审计-源码泄露】获取源码方法，利用工具

# 【web审计-源码泄露】获取源码方法，利用工具

**目录**

[一、备份文件泄露](#%E4%B8%80%E3%80%81%E5%A4%87%E4%BB%BD%E6%96%87%E4%BB%B6%E6%B3%84%E9%9C%B2)

[1.1、简介：](#1.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.2、文本备份文件](#1.2%E3%80%81%E6%96%87%E6%9C%AC%E5%A4%87%E4%BB%BD%E6%96%87%E4%BB%B6)

[1.3、整站源码备份文件](#1.3%E3%80%81%E6%95%B4%E7%AB%99%E6%BA%90%E7%A0%81%E5%A4%87%E4%BB%BD%E6%96%87%E4%BB%B6)

[二、Git泄露](#%E4%BA%8C%E3%80%81Git%E6%B3%84%E9%9C%B2)

[2.1、工具（GitHack）：](#2.1%E3%80%81%E5%B7%A5%E5%85%B7%EF%BC%88GitHack%EF%BC%89%EF%BC%9A)

[2.2、产生：](#2.2%E3%80%81%E4%BA%A7%E7%94%9F%EF%BC%9A)

[2.3、通过特征搜索](#2.3%E3%80%81%E9%80%9A%E8%BF%87%E7%89%B9%E5%BE%81%E6%90%9C%E7%B4%A2)

[2.4、通过.git泄露](#2.4%E3%80%81%E9%80%9A%E8%BF%87.git%E6%B3%84%E9%9C%B2)

[分析源码：](#%E5%88%86%E6%9E%90%E6%BA%90%E7%A0%81%EF%BC%9A)

[文件：](#%E6%96%87%E4%BB%B6%EF%BC%9A)

[自定义函数](#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%87%BD%E6%95%B0)

[三、svn泄露](#%E4%B8%89%E3%80%81svn%E6%B3%84%E9%9C%B2)

[3.1、简介：](#3.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[3.2、产生原因：](#3.2%E3%80%81%E4%BA%A7%E7%94%9F%E5%8E%9F%E5%9B%A0%EF%BC%9A)

[3.3、工具：](#3.3%E3%80%81%E5%B7%A5%E5%85%B7%EF%BC%9A)

[Seay-Svn（简单）](#Seay-Svn%EF%BC%88%E7%AE%80%E5%8D%95%EF%BC%89)

[dvcs-ripper](#dvcs-ripper)

[四、hg、CVS、Bazaar/bzr源码泄漏](#%E5%9B%9B%E3%80%81hg%E3%80%81CVS%E3%80%81Bazaar%2Fbzr%E6%BA%90%E7%A0%81%E6%B3%84%E6%BC%8F)

[4.1、工具：](#4.1%E3%80%81%E5%B7%A5%E5%85%B7%EF%BC%9A)

[dvcs-ripper](#dvcs-ripper)

[五、WEB-INF/web.xml 泄露](#%E4%BA%94%E3%80%81WEB-INF%2Fweb.xml%20%E6%B3%84%E9%9C%B2)

[5.1、简介：](#5.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[5.2、产生原因：](#5.2%E3%80%81%E4%BA%A7%E7%94%9F%E5%8E%9F%E5%9B%A0%EF%BC%9A)

[5.3、WEB-INF 主要包含文件或目录：](#5.3%E3%80%81WEB-INF%20%E4%B8%BB%E8%A6%81%E5%8C%85%E5%90%AB%E6%96%87%E4%BB%B6%E6%88%96%E7%9B%AE%E5%BD%95%EF%BC%9A)

[5.4、利用：](#5.4%E3%80%81%E5%88%A9%E7%94%A8%EF%BC%9A)

[六、DS_Store 文件泄露](#%E5%85%AD%E3%80%81DS_Store%20%E6%96%87%E4%BB%B6%E6%B3%84%E9%9C%B2)

[6.1、简介：](#6.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[6.2、工具：](#6.2%E3%80%81%E5%B7%A5%E5%85%B7%EF%BC%9A)

[ds_store_exp](#ds_store_exp)

[七、利用漏洞泄露](#%E4%B8%83%E3%80%81%E5%88%A9%E7%94%A8%E6%BC%8F%E6%B4%9E%E6%B3%84%E9%9C%B2)

---


## 一、备份文件泄露

> 
<h3>1.1、简介：</h3>
备份文件一般是由于维护人员的疏忽，忘记删除而留在服务器中的文件。
攻击者通过枚举常见备份文件名，来获得对应的路径，并得到关键代码，从而进行源代码的审计
为了能够找到这些备份文件，一般会使用一些敏感文件扫描工具来进行探测。
一般常见备份文件有：文本备份文件、整站源码备份文件
文件后缀：.rar   .zip  .7z   .tar.gz   .bak    .swp   .txt   .sql等


> 
<h3>1.2、文本备份文件</h3>
在Linux系统下会使用诸如vim或gedit等文本编辑器，当编辑器崩溃或因异常退出时会自动备份当前文件；或将实现某功能后的代码备份后再进行后续开发工作。
可能的备份文件（index.php为例）：
.index.php.swp<br/> .index.php.swo<br/> index.php~<br/> index.php.bak<br/> index.php.txt<br/> index.php.old<br/> ...


> 
<h3>1.3、整站源码备份文件</h3>
会将整站源码打包，然后放在网站的根目录下，这时，只要找到这个压缩包就能开始进行源码审计了。
常见的整站备份文件名：
www<br/> wwwdata<br/> wwwroot<br/> web<br/> webroot<br/> backup<br/> dist<br/> ...
<hr/>
各种压缩文件后缀名：
.zip<br/> .tar<br/> .tar.gz<br/> .7z<br/> .rar<br/> ...
还可利用其他可能泄露目录结构或文件名的敏感文件来获取备份文件的位置，如“.xx_xxx”


---


---


## 二、Git泄露

> 
<h3>2.1、工具（GitHack）：</h3>

GitHack是一个.git泄露利用脚本，通过泄露的.git文件夹下的文件，重建还原工程源代码。
渗透测试人员、攻击者，可以进一步审计代码，挖掘：文件上传，SQL注射等web安全漏洞。
[GitHub - lijiejie/GitHack: A `.git` folder disclosure exploit<img alt="icon-default.png?t=M5H6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://github.com/lijiejie/GitHack](https://github.com/lijiejie/GitHack)
使用：
<pre>`python GitHack.py http://www.openssl.org/.git/`</pre>


> 
<h3>2.2、产生：</h3>
web在升级和维护过程中，会对站点文件进行修改，就需要对网站整站或其中一部分进行备份
发布代码的时候，如果没有删除.git目录，就直接发布到服务器，攻击者通过它来恢复源代码
备份文件被放在到 web 服务器可访问的目录下


> 
<h3>2.3、通过特征搜索</h3>
当某个网站存在某个明显特征字符串的时候
就有可能通过GitHub的搜索功能来搜索到该项目


> 
<h3>2.4、通过.git泄露</h3>
每个git项目的根目录下都存在一个.git文件夹，作用就是存储项目的相关信息
工具：GitHack和源码
<hr/>
<h4>分析源码：</h4>
首先在本地建立一个git工程并初始化，然后再commit一次
进入.git目录下，看看目录中文件
确定commit对象，查看对象
输入存在“.git”目录中的url
接着查看HEAD文件获取分支的位置，然后得到分支的hash值
得到hash值后本地初始化一个git，接着通过parseCommit获取全部对象
最后使用reset重设分支，成功将项目重新建立在本地
<hr/>
<h4>文件：</h4>
关键的文件（一部分）：
HEAD：标记当前git在哪个分支中。
refs：标记该项目里的每个分支指向的commit。
objects：git本地仓库存储的所有对象。

git的对象：
commit：标记一个项目的一次提交记录。
tree：标记一个项目的目录或者子目录。
blob：标记一个项目的文件。
tag：命名一次提交。
<hr/>
<h4>自定义函数</h4>
（1）parseCommit函数：
作用：下载commit对象，将其parent一并下载
代码：
function parseCommit {<br/>         echo parseCommit $1<br/>         downloadBlob $1<br/>         tree=$(git cat-file -p $1| sed -n '1p' | awk '{print $2}')<br/>         parseTree $tree<br/>         parent=$(git cat-file -p $1 | sed -n '2p' | awk '{print $2}')<br/>         [ ${#parent} -eq 40 ] &amp;&amp; parseCommit $parent<br/> }
<hr/>
（2）parseTree函数：
作用：下载tree对象，并列出tree下的所有对象，分类为tree或者blob后处理
代码：
function parseTree {<br/>         echo parseTree $1<br/>         downloadBlob $1<br/>         while read line<br/>         do<br/>         type=$(echo $line | awk '{print $2}')<br/>         hash=$(echo $line | awk '{print $3}')<br/>         [ "$type" = "tree" ] &amp;&amp; parseTree $hash || downloadBlob $hash<br/>         done &lt; &lt;(git cat-file -p $1)<br/> }

<hr/>
（3）downloadBlob函数：
作用：下载与hash对应的文件
function downloadBlob {<br/>         echo downloadBlob $1<br/>         mkdir -p ${1:0:2}<br/>         cd $_<br/>         wget -q -nc $domain/.git/objects/${1:0:2}/${1:2}<br/>         cd ..<br/> }


---


#### 文件：

---


---


---


## 三、svn泄露

> 
<h3>3.1、简介：</h3>
Subversion(SVN) 是一个开源的版本控制系統, 也就是说 Subversion 管理着随时间改变的数据。 这些数据放置在一个中央资料档案库(repository) 中。 这个档案库很像一个普通的文件服务器, 不过它会记住每一次文件的变动。 这样你就可以把档案恢复到旧的版本, 或是浏览文件的变动历史。
在使用SVN管理本地代码过程中，会自动生成一个名为.svn的隐藏文件夹，其中包含重要的源代码信息。


> 
<h3>3.2、产生原因：</h3>
网站管理员在发布代码时，没有使用‘导出’功能，而是直接复制代码文件夹到WEB服务器上，这就使.svn隐藏文件夹被暴露于外网环境，可以利用.svn/entries文件，获取到服务器源码。


> 
<h3>3.3、工具：</h3>
<h4>Seay-Svn（简单）</h4>
[http://www.vuln.cn/wp-content/uploads/2015/10/Seay-Svn.rar<img alt="icon-default.png?t=M5H6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>http://www.vuln.cn/wp-content/uploads/2015/10/Seay-Svn.rar](http://www.vuln.cn/wp-content/uploads/2015/10/Seay-Svn.rar)<img alt="" height="607" src="https://img-blog.csdnimg.cn/84e4775aaae843228005f5029b7d5d71.png" width="1127"/>
<hr/>
<h4>dvcs-ripper</h4>
下载地址：
[GitHub - kost/dvcs-ripper: Rip web accessible (distributed) version control systems: SVN/GIT/HG...<img alt="icon-default.png?t=M5H6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://github.com/kost/dvcs-ripper](https://github.com/kost/dvcs-ripper)
‎Rip Web可访问（分布式）版本控制系统：SVN，GIT，Mercurial/hg，bzr，...‎
‎即使目录浏览关闭，它也可以翻录存储库。‎
‎确保将自己置于要下载/克隆存储库的空目录中。‎


#### dvcs-ripper

---


---


## 四、hg、CVS、Bazaar/bzr源码泄漏

> 
<h3>4.1、工具：</h3>
<h4>dvcs-ripper</h4>
下载地址：
[GitHub - kost/dvcs-ripper: Rip web accessible (distributed) version control systems: SVN/GIT/HG...<img alt="icon-default.png?t=M5H6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://github.com/kost/dvcs-ripper](https://github.com/kost/dvcs-ripper)
‎Rip Web可访问（分布式）版本控制系统：SVN，GIT，Mercurial/hg，bzr，...‎
‎即使目录浏览关闭，它也可以翻录存储库。‎
‎确保将自己置于要下载/克隆存储库的空目录中。‎


---


---


## 五、WEB-INF/web.xml 泄露

> 
<h3>5.1、简介：</h3>
WEB-INF是Java的WEB应用的安全目录，客户端无法访问，只有服务端才可以可以访问，如果想在页面中直接访问其中的文件，必须通过web.xml文件对要访问的文件进行相应映射才能访问。


> 
<h3>5.2、产生原因：</h3>
在使用网络架构的时候，对静态资源的目录或文件的映射配置不当，从而引发的安全问题，导致web.xml等文件能够被读取


> 
<h3>5.3、WEB-INF 主要包含文件或目录：</h3>
（1）/WEB-INF/web.xml :
Web应用程序配置文件(描述servlet和其他的应用组件配置及命名规则)
（2）/WEB-INF/database.properties:
数据库配置文件
（3）/WEB-INF/classes/:
存放Java类文件(.class),包含所有的 Servlet 类和其他类文件，类文件所在的目录结构与他们的包名称匹配
（4）/WEB-INF/lib/ :
用来存放打包好的库(.jar),即web应用需要的各种JAR文件
（5）/WEB-INF/src/ :
源码目录，存放源代码(.asp和.php等)


> 
<h3>5.4、利用：</h3>
通过找到 web.xml 文件，推断 class 文件的路径，找到 class 文件，再通过反编译 class 文件，得到网站源码。


---


---


## 六、DS_Store 文件泄露

> 
<h3>6.1、简介：</h3>
.DS_Store是Mac下Finder用来保存如何展示文件/文件夹 的数据文件（即文件夹的显示属性的，和比文件图标的摆放位置），每个文件夹下对应一个
<hr/>
把代码上传的时候，安全正确的操作应该把 .DS_Store 文件删除,如果未删除，.DS_Store将会上传部署到服务器，可能造成文件泄漏（目录结构、备份文件、源代码文件）


> 
<h3>6.2、工具：</h3>
<h4>ds_store_exp</h4>
是一个 .DS_Store 文件泄漏利用脚本，它解析.DS_Store文件并递归地下载文件到本地。
下载地址：
[GitHub - lijiejie/ds_store_exp: A .DS_Store file disclosure exploit. It parses .DS_Store file and downloads files recursively.<img alt="icon-default.png?t=M5H6" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://github.com/lijiejie/ds_store_exp](https://github.com/lijiejie/ds_store_exp)


---


---


> 
<h2>七、利用漏洞泄露</h2>
结合任意文件包含漏洞或者任意文件存在下载漏洞
就可能下载到源码，并对其进行审计

