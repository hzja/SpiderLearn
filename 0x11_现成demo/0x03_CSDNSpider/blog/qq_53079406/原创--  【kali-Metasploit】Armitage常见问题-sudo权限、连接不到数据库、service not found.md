# 原创
：  【kali-Metasploit】Armitage常见问题：sudo权限、连接不到数据库、service not found

# 【kali-Metasploit】Armitage常见问题：sudo权限、连接不到数据库、service not found

**目录**

[一、问题一：sudo权限、连接不到数据库](#%E4%B8%80%E3%80%81%E9%97%AE%E9%A2%98%E4%B8%80%EF%BC%9Arunning%20nmap%20with%20sudo)

[1.1、示例：](#1.1%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[1.2、错误重现：](#1.2%E3%80%81%E9%94%99%E8%AF%AF%E9%87%8D%E7%8E%B0%EF%BC%9A)

[1.3、问题分析：](#1.3%E3%80%81%E9%97%AE%E9%A2%98%E5%88%86%E6%9E%90%EF%BC%9A)

[1.4、问题解决：](#1.4%E3%80%81%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3%EF%BC%9A)

[方法一：](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9A)

[方法二：](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A)

[方法三：（我使用的）](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A%EF%BC%88%E6%88%91%E4%BD%BF%E7%94%A8%E7%9A%84%EF%BC%89)

[二、问题二：service not found](#%E4%BA%8C%E3%80%81%E9%97%AE%E9%A2%98%E4%BA%8C%EF%BC%9A)

[2.1、错误重现：](#2.1%E3%80%81%E9%94%99%E8%AF%AF%E9%87%8D%E7%8E%B0%EF%BC%9A)

[2.2、分析：](#2.2%E3%80%81%E5%88%86%E6%9E%90%EF%BC%9A)

---


## 一、问题一：sudo权限、连接不到数据库

> 
<h3>1.1、示例：</h3>
从Armitage内部进行 NMap 扫描 - 缺根权限
armitage 提示running nmap with sudo




> 
<h3>1.2、错误重现：</h3>
启动metasploit + armitage
启动 armitage 并单击“Hosts-&gt;Nmap-&gt;快速扫描 （OSdetect）




> 
<h3>1.3、问题分析：</h3>
1、nmap 命令不是由 armitage 启动的，而是由 msfrpcd 启动的，必须确保 msfrpcd 以 root 权限运行
<hr/>
2、如果处于没有root和msfrpcd运行的armitage，armitage 会询问您是否应该启动 msfrpcd，单击“是”后，msfrpcd 在没有 root 的情况下启动，如果退出，msfrpcd 也不会退出，而是继续在后台运行
<hr/>
3、sudo 重新启动了 armitage，但它连接到非 sudo msfrpcd，所以 nmap 提示没有 root
<hr/>
4、要在msf中使用sudo armitage(就能连接到了)


---


> 
<h3>1.4、问题解决：</h3>
<h4>方法一：</h4>
退出 armitage，退出 msfrpcd
使用 sudo 启动 armitage，这将再次询问您是否应该启动 msfrpcd，现在将作为根权限启动


<hr/>
<h4>方法二：</h4>
sudo msfrpcd -U user -P password
sudo armitage
<hr/>
<h4>方法三：（我使用的）</h4>
sudo msfconsole


 sudo armitage<br/><img alt="" height="443" src="https://img-blog.csdnimg.cn/de1f03c61e8d44d3aabbcee9b1863c10.png" width="868"/>

 然后就能扫出来了




#### 方法二：

---


---


---


## 二、问题二：service not found

> 
<h3>2.1、错误重现：</h3>
Failed to start metasploit.service: Unit metasploit.service not found.




> 
<h3>2.2、分析：</h3>
sudo service metasploit start是老命令了
现在直接sudo msfconsole

就启动了 metasploit
再输入db_status查询


