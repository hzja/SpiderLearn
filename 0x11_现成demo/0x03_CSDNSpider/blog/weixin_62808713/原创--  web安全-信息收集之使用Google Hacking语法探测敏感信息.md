# 原创
：  web安全-信息收集之使用Google Hacking语法探测敏感信息

# web安全-信息收集之使用Google Hacking语法探测敏感信息

**目录**

[一、介绍](#%E4%B8%80%E3%80%81%E4%BB%8B%E7%BB%8D)

[二、逻辑运算符](#%E4%BA%8C%E3%80%81%E9%80%BB%E8%BE%91%E8%BF%90%E7%AE%97%E7%AC%A6)

[+](#%2B)

[-](#-)

[~](#~)

[.](#.)

[*](#*)

[" "](#%22%20%22)

[|或OR](#%7C%E6%88%96OR)

[三、基本语法](#%E4%B8%89%E3%80%81%E5%9F%BA%E6%9C%AC%E8%AF%AD%E6%B3%95)

[intext:key](#intext%3Akey)

[allintext:key](#allintext%3Akey)

[intitle:key](#intitle%3Akey)

[allintitle:key](#allintitle%3Akey)

[cache:url](#cache%3Aurl)

[filetype:](#filetype%3A)

[info:](#info%3A)

[inurl:](#inurl%3A)

[site:](#site%3A)

[related:url](#related%3Aurl)

[四、高级案例](#%E5%9B%9B%E3%80%81%E9%AB%98%E7%BA%A7%E6%A1%88%E4%BE%8B)

[intitle:管理登录 filetype:php](#intitle%3A%E7%AE%A1%E7%90%86%E7%99%BB%E5%BD%95%20filetype%3Aphp)

[site:baidu.com](#site%3Abaidu.com)

[site:baidu.com intitle:登陆](#site%3Abaidu.com%20intitle%3A%E7%99%BB%E9%99%86)

[intitle:"index of " "shell.txt"](#intitle%3A%22index%20of%20%22%20%22shell.txt%22)

[site:baidu.com inurl:/login](#site%3Abaidu.com%20inurl%3A%2Flogin)

[site:36.110.213.* ](#site%3A36.110.213.*%C2%A0)

[五、Google Hacking语法收集网站](#%E4%BA%94%E3%80%81Google%20Hacking%E8%AF%AD%E6%B3%95%E6%94%B6%E9%9B%86%E7%BD%91%E7%AB%99)

[六、小知识：网络蜘蛛](#%E5%85%AD%E3%80%81%E5%B0%8F%E7%9F%A5%E8%AF%86%EF%BC%9A%E7%BD%91%E7%BB%9C%E8%9C%98%E8%9B%9B)

---


## 一、介绍

        使用Google搜索引擎或其它Google应用程序通过特定于法来查找网站配置或代码中的安全漏洞。

        可以Google Hacking语法搜索Web信息、登陆后台、特定文件、漏洞页面、错误信息等等。

## 二、逻辑运算符

        强制搜索其最后的一个单词。

        把某个关键字忽略掉。

        同意词识别，将有同意词的页面也一起搜索出来。

        单一通配符。

        通配符，可以代表多个字母。

        精确查询，只查询完整连续的关键词，不讲输入的关键词进行拆分。

        将只要符合多个关键字中的任意一个的结果予以显示。

## 三、基本语法

        搜索网页页面内带有关键字的页面。

        功能与intext相似，但是可以接多个关键字。

        搜素网页标题中带有关键字的网页。

        功能与allintext相似，可以接多个关键字，但是不能与别的关键字连用。

        查看指定URL快照。

        搜素指定类型的文件。

        搜素输入URL的摘要信息和其它相关信息，不能与其它关键词混用。

        搜素输入字符是否存在与URL中，可以与site结合来找后台。

        搜素指定网站或者子域名或c段地址。

        搜素与该url相关的，同类的页面。

## 四、高级案例

## 五、Google Hacking语法收集网站

        在这个网站内存在许多Google Hacking语法的高级用法，如果自己对Google Hacking语法使用不熟练，可以来到这个网站内进行借鉴和学习。

        [Google Hacking Database (GHDB) - Google Dorks, OSINT, Recon](https://www.exploit-db.com/google-hacking-database)

## 六、小知识：网络蜘蛛

        蜘蛛在爬行时，会爬行整个网站，网站内所有的链接都会被一一提交到 Google 的数据库中。

        那么如何完全隐藏网站的敏感信息呢?

        从开发人员的角度来讲，一定要保证敏感信息不被外部引用。如果在一些对外暴露的页面中引用一些敏感目录，那么 Google 的蜘蛛就会顺藤摸瓜找到地址。同时，也要保证敏感信息的名字很复杂，否则很有可能被攻击者扫描出地址。

        Google 也不是万能的，它只能查询出蜘蛛爬行过的网页，而蜘蛛遵照网站根目录robots.txt的约定进行爬行，如果一些敏感目录不希望蜘蛛进行爬行，则可以写在网站根目录robots.txt 中。虽然这样不会被蜘蛛爬行到，但是攻击者可以直接访问robots.txt。
