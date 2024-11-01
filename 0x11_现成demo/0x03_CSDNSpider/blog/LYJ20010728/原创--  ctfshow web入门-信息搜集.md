# 原创
：  ctfshow web入门-信息搜集

# ctfshow web入门-信息搜集

#### ctfshow web入门-信息搜集

## web1

> 
直接`view-source:`查看源码即可


## web2

> 
题目提示我们：js前台拦截 === 无效操作，这种情况下多半是利用率JavaScript函数禁用了部分查看源码的方式，这里依旧直接`view-source:`即可绕过JavaScript前台拦截查看源码


## web3

> 
题目提示我们：没思路的时候抓个包看看，可能会有意外收获；利用burpsuite抓包拦截，在response中发现flag


## web4

> 
题目提示我们：总有人把后台地址写入robots，帮黑阔大佬们引路；访问 `robots.txt`文件


> 
发现flag文件路径，访问即可


## web5

> 
题目提示我们：phps源码泄露有时候能帮上忙；访问 `index.phps` ，得到flag


## web6

> 
题目提示我们：解压源码到当前目录，测试正常，收工；疑似www.zip源码泄露，访问得到www.zip，解压得到flag文件


## web7

> 
题目提示我们：版本控制很重要，但不要部署到生产环境更重要；疑似 `git`代码泄露，直接访问 `.git/index.php`


## web8

> 
题目提示我们：版本控制很重要，但不要部署到生产环境更重要；信息 `svn`泄露，直接访问 `.svn/`


## web9

> 
题目提示我们：发现网页有个错别字？赶紧在生产环境vim改下，不好，死机了；vim缓存信息泄露，直接访问`/index.php.swp`


## web10

> 
题目提示我们：cookie 只是一块饼干，不能存放任何隐私数据；直接查看Cookie信息


## web11

> 
题目提示我们：域名其实也可以隐藏信息，比如ctfshow.com 就隐藏了一条信息；通过dns检查查询flag `https://zijian.aliyun.com/` TXT 记录，一般指为某个主机名或域名设置的说明


## web12

> 
题目提示我们：有时候网站上的公开信息，就是管理员常用密码；查看robots.txt文件，用户名admin，密码在页面的最下方


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623000820816.png#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623000826636.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## web13

> 
题目提示我们：技术文档里面不要出现敏感信息，部署到生产环境后及时修改默认密码；根据题目提示，技术文档在页面下面发现 document，下载发现里面存在后台地址和用户名密码登录成功获得flag


## web14

> 
题目提示我们：有时候源码里面就能不经意间泄露重要(editor)的信息,默认配置害死人；根据提示访问 `/editor`，然后访问 flag的路径


## web15

> 
题目提示我们：公开的信息比如邮箱，可能造成信息泄露，产生严重后果；访问/admin页面 发现有一个忘记密码操作，需要输入地址，在主页面下面看到QQ邮箱，通过QQ号查询邮箱是西安的，修改密码成功，用户名 admin 登录成功获得flag


## web16

> 
题目提示我们：对于测试用的探针，使用完毕后要及时删除，可能会造成信息泄露；url后缀名添加/tz.php 版本是雅黑PHP探针，然后查看phpinfo搜索flag


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623004051147.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623004058410.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## web17

> 
题目提示我们：透过重重缓存，查找到ctfer.com的真实IP，提交flag{IP地址}；直接`ping www.ctfshow.com`获得flag


## web18

> 
题目提示我们：不要着急，休息，休息一会儿，玩101分给你flag；F12查看源码，查看js文件，查看flag的条件，通过uncode解码得到信息访问110.php


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623004811865.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623004820625.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623004826231.png#pic_center"/>

## web19

> 
题目提示我们：密钥什么的，就不要放在前端了；F12查看源代码，提交用户名密码


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210623005247986.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021062300525418.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## web20

> 
题目提示我们：mdb文件是早期asp+access构架的数据库文件，文件泄露相当于数据库被脱裤了；访问/db/db.mdb 下载文件，通过txt打开或者通过EasyAccess.exe打开搜索flag即可

