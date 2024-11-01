# 原创
：  【kali-漏洞利用】（3.2）Metasploit基础（中）:Armitage工具利用过程

# 【kali-漏洞利用】（3.2）Metasploit基础（中）:Armitage工具利用过程

**目录**

[一、常见问题：](#%E4%B8%80%E3%80%81%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%EF%BC%9A)

[ 二、使用步骤：](#%C2%A0%E4%BA%8C%E3%80%81%E4%BD%BF%E7%94%A8%E6%AD%A5%E9%AA%A4%EF%BC%9A)

[第一步：启动ArmItage工具](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E5%90%AF%E5%8A%A8ArmItage%E5%B7%A5%E5%85%B7)

[第二步：配置](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E9%85%8D%E7%BD%AE)

[第三步：扫描完成](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E6%89%AB%E6%8F%8F%E5%AE%8C%E6%88%90)

[第四步：利用模块](#%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E5%88%A9%E7%94%A8%E6%A8%A1%E5%9D%97)

[第五步：Attacks菜单](#%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9AAttacks%E8%8F%9C%E5%8D%95)

[第六步：问题解决](#%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E9%97%AE%E9%A2%98%E8%A7%A3%E5%86%B3)

[第七步：识别系统](#%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E8%AF%86%E5%88%AB%E7%B3%BB%E7%BB%9F)

[ 第八步：检测目标可利用漏洞](#%C2%A0%E7%AC%AC%E5%85%AB%E6%AD%A5%EF%BC%9A%E6%A3%80%E6%B5%8B%E7%9B%AE%E6%A0%87%E5%8F%AF%E5%88%A9%E7%94%A8%E6%BC%8F%E6%B4%9E)

[第九步：利用漏洞 ](#%E7%AC%AC%E4%B9%9D%E6%AD%A5%EF%BC%9A%E5%88%A9%E7%94%A8%E6%BC%8F%E6%B4%9E%C2%A0)

[第十步：分析结果](#%E7%AC%AC%E5%8D%81%E6%AD%A5%EF%BC%9A%E5%88%86%E6%9E%90%E7%BB%93%E6%9E%9C)

[第十一步：获取权限](#%E7%AC%AC%E5%8D%81%E4%B8%80%E6%AD%A5%EF%BC%9A%E8%8E%B7%E5%8F%96%E6%9D%83%E9%99%90)

---


> 
<h3>一、常见问题：</h3>
[【kali-Metasploit】Armitage常见问题：sudo权限、连接不到数据库、service not found<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/126145882?spm=1001.2014.3001.5501](https://blog.csdn.net/qq_53079406/article/details/126145882?spm=1001.2014.3001.5501)


> 
<h3> 二、使用步骤：</h3>
<h4>第一步：启动ArmItage工具</h4>

<hr/>
<h4>第二步：配置</h4>
菜单栏中依次选择Hosts-----NmapScan------Quick Scan

 在输入框中输入要扫描的网络范围， 这里输入的网络范围是192.168.190.0/24。点击“ 确定” 按钮，开始扫描


<hr/>
<h4>第三步：扫描完成</h4>
弹出了一个扫描完成对话框，点击确认



<hr/>
<h4>第四步：利用模块</h4>
在菜单栏中选择Attacks-----FindAttacks命令



<hr/>
<h4>第五步：Attacks菜单</h4>
未出现attacks菜单

<hr/>
<h4>第六步：问题解决</h4>


然后再次执行Attacks-----FindAttacks命令

再次提示完成

 出现attack菜单


<hr/>

<h4>第七步：识别系统</h4>
扫描到的主机屏幕都是黑色， 是因为还没有识别出操作系统的类型
先选中一个主机
然后在菜单栏中选择Hosts-----NmapScan-------Quick Scan (OS detect)命令， 扫描操作系统类型。扫描完成后，将显示操作系统的默认附标


或者输入一个要扫描的主机

 <img alt="" height="605" src="https://img-blog.csdnimg.cn/984fe237807242d784803a9e71824d3e.png" width="793"/>
<hr/>


<h4> 第八步：检测目标可利用漏洞</h4>
在Attack中找到check exploits，自动扫描检查上面所显示的每一个漏洞是否存在及可用


<hr/>
<h4>第九步：利用漏洞 </h4>
在左上的exploit模块中选择Linux，然后填写目标主机等相关信息

最后再点击launch
<hr/>

<h4>第十步：分析结果</h4>
一看就知道是没利用成功
（再换换其他的）


<hr/>
<h4>第十一步：获取权限</h4>
攻击成功后，就可以看到窗口中的靶机图标变成了显眼的红色，且被闪电缠绕，表示这台主机已经被攻下了
右键靶机，依次选择Shell-&gt;Interact，成功获取权限




#### 第一步：启动ArmItage工具

---


#### 第三步：扫描完成

---


#### 第五步：Attacks菜单

---


#### 第七步：识别系统

---


#### 第九步：利用漏洞 

---


#### 第十一步：获取权限
