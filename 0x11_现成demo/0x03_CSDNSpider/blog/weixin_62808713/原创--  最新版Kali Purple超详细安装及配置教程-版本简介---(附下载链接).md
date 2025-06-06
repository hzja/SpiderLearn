# 原创
：  最新版Kali Purple超详细安装及配置教程-版本简介---(附下载链接)

# 最新版Kali Purple超详细安装及配置教程-版本简介---(附下载链接)

**目录**

[一、Kali Purple简介](#%E4%B8%80%E3%80%81Kali%20Purple%E7%AE%80%E4%BB%8B)

[二、官网下载Kali Purple映像](#%E4%BA%8C%E3%80%81%E5%AE%98%E7%BD%91%E4%B8%8B%E8%BD%BDKali%20Purple%E6%98%A0%E5%83%8F)

[三、创建Kali Purple虚拟机](#%C2%A0%E4%B8%89%E3%80%81%E5%88%9B%E5%BB%BAKali%20Purple%E8%99%9A%E6%8B%9F%E6%9C%BA)

[四、打开Kali Purple进行内部配置](#%C2%A0%E5%9B%9B%E3%80%81%E6%89%93%E5%BC%80Kali%20Purple%E8%BF%9B%E8%A1%8C%E5%86%85%E9%83%A8%E9%85%8D%E7%BD%AE)

[五、内部展示](#%E4%BA%94%E3%80%81%E5%86%85%E9%83%A8%E5%B1%95%E7%A4%BA)

---


## 一、Kali Purple简介

        Kali Linux在庆祝十周年之际，引入了一个新的Kali Linux风味，称为Kali Purple，重点是防御性安全和终极SOC In-A-Box的参考架构，旨在学习、实践SOC分析和威胁猎取、安全控制设计/测试、Kali间谍与间谍竞赛，以及保护中小型环境。

        Kali Purple配备了100多个防御工具，如Arkime全包捕获和分析、CyberChef网络瑞士军刀、Elastic Security信息和事件管理、GVM漏洞扫描仪、TheHive事件响应平台、Malcolm网络流量分析工具套件，以及Zeek和Suricata入侵检测系统。

        这个版本还包括了新的工具，即Arkime全包捕获和分析、CyberChef网络瑞士军刀、DefectDojo应用漏洞管理关联和安全协调工具、Dscan nmap包装器、用于在预配置的Kubernetes资源中管理Charts的Kubernetes-Helm工具，以及在pentest操作中的Redeye数据管理器。

        Kali Purple还配备了一些最新和最伟大的GNU/Linux技术，包括Xfce 4.18桌面环境、Linux内核6.1 LTS、Python 3.11，以及KDE Plasma 5.27 LTS作为安装Kali Linux时的可选桌面环境。

## 二、官网下载Kali Purple映像

1.进入kali官网（点击下面超链接即可进入）,在官网内找到“Kali Purple”。

        [Get Kali | Kali Linux](https://www.kali.org/get-kali/#kali-installer-images)

 2.点击左侧的下载后耐心等待其下载完成。

 3.下载完成。

## 三、创建Kali Purple虚拟机

1.打开VMware，点击“创建新的虚拟机”。

 2.默认“典型”后点击“下一步”。

 3.默认“安装程序光盘映像文件”后点击“浏览”，按照路径选择刚刚下载的Kali Purple映像文件，然后点击“下一步”。

 4.选择“Linux”后点击“下一步”。

 5.修改“虚拟机名称”以及“位置”后，点击“下一步”。

 6.根据自己情况修改“最大磁盘大小”，然后这里建议选择“将虚拟磁盘拆分成多个文件”，选择后点击“下一步”。

 7.点击“完成”。

 8.点击“编辑虚拟机设置”来到虚拟机设置页面。

 9.首先配置“内存”，我这里内存分配为6GB（6144MB），可以根据自己的电脑情况来选择分配大小。

 10.接下来配置处理器，我这里配置的处理器数量是3，每个处理器的内核数量是2，这里同样可以根据自己的电脑自行选择配置大小。

 11.上述配置均配置完成后点击“确定”即可。

## 四、打开Kali Purple进行内部配置

1.点击“开启此虚拟机”。

 2.如果有图示窗口弹出，点击“确定”即可。

 3.打开后会进入到如下页面，此时将鼠标移入虚拟机点击任意位置一下后，敲击键盘回车键即可。

4.敲击回车后会看到如下界面（大概会出现3至7秒）。

5.出现下面的页面后上拉找到“中文（简体）”并选择后，点击“Continue”（这里根据个人习惯，如果习惯使用英语保持默认即可）。

 6.国家这里默认选择“中国”后，点击“继续”。

 7.这里默认“汉语”，点击“继续”即可。

 8.等待系统进行自动配置（约1分钟）。

 9.系统自动配置完成后会进入到下面的页面，这里主机名默认即可（也可以根据个人想法进行修改），点击“继续”。

10.这里若无特殊要求直接点击“继续”即可（这里设置的用户名就是最终登陆kali系统时所要输入的用户名）。

 11.根据自己情况设置好用户名后点击“继续”。<img alt="" height="1029" src="https://img-blog.csdnimg.cn/2b9056eaa57e46c6964c68cff79b9ca5.png" width="1200"/>

12.这个页面可以不用更改直接点击“继续”。

13.这里对每次登陆kali时使用的密码进行设置（为了方便，可以直接将密码设为“kali”），填写完成后点击“继续”。

 14.再次进入到了系统自动配置，等待其配置完成即可（约30秒）。

 15.保持默认直接点击“继续”即可。

16.点击“继续”。

17.点击“继续”。

 18.点击“继续”。

19. 这里选择“是”后，点击“继续”。

 20.等待系统自行安装基本系统以及软件（约2分钟）。

 21.待其出现下面的页面后，直接点击“继续”。

 22.等待其自动选择、安装并解压软件（快的话约8分钟，慢的话约10至20分钟）。

 23.待其安装完成出现下面的页面后，选择“是”，然后点击“继续”。

 24.选择“/dev/sda”后，点击“继续”。

 25.等待其结束安装进程（约5分钟）。

 26.出现下面的页面后点击“继续”。

 27.等待其继续结束安装进程（约2分钟）。

28. 安装进程彻底结束后，会进入到下面的页面，在此页面内直接敲击键盘上的回车即可。

 29.敲击回车后等待系统启动（约1分钟）。<img alt="" height="1027" src="https://img-blog.csdnimg.cn/80af71ff398d4c199e9639aaa436a750.png" width="1200"/>

 30.进入到了登陆页面，输入前面设置的账号和密码后点击“登陆”。 

31.成功进入了Kali Purple！

---


**                至此Kali Purple就已经成功安装并配置完成了！！！**

---


## 五、内部展示

 
