# 原创
：  【Windows漏洞分析工具】wesng下载、命令选项、示例、使用方法

# 【Windows漏洞分析工具】wesng下载、命令选项、示例、使用方法

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[二、下载：](#%E4%BA%8C%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[2.1、GitHub：](#2.1%E3%80%81GitHub%EF%BC%9A)

[三、命令选项](#%E4%B8%89%E3%80%81%E5%91%BD%E4%BB%A4%E9%80%89%E9%A1%B9)

[四、示例：](#%E5%9B%9B%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[五、使用方法：](#%E4%BA%94%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[5.1、第一步：收集系统补丁 ](#5.1%E3%80%81%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%9A%E6%94%B6%E9%9B%86%E7%B3%BB%E7%BB%9F%E8%A1%A5%E4%B8%81%C2%A0)

[5.2、第二步：将收集的文件放到文件下](#5.2%E3%80%81%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%9A%E5%B0%86%E6%94%B6%E9%9B%86%E7%9A%84%E6%96%87%E4%BB%B6%E6%94%BE%E5%88%B0%E6%96%87%E4%BB%B6%E4%B8%8B)

[5.3、第三步：进入Windows powershell](#5.3%E3%80%81%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%9A%E8%BF%9B%E5%85%A5Windows%20powershell)

[5.4、第四步：检查更新](#5.4%E3%80%81%E7%AC%AC%E5%9B%9B%E6%AD%A5%EF%BC%9A%E6%A3%80%E6%9F%A5%E6%9B%B4%E6%96%B0)

[5.5、第五步：检测缺少的补丁](#5.5%E3%80%81%E7%AC%AC%E4%BA%94%E6%AD%A5%EF%BC%9A%E6%A3%80%E6%B5%8B%E7%BC%BA%E5%B0%91%E7%9A%84%E8%A1%A5%E4%B8%81)

[5.6、第六步：仅显示一定影响的脆弱性](#5.6%E3%80%81%E7%AC%AC%E5%85%AD%E6%AD%A5%EF%BC%9A%E4%BB%85%E6%98%BE%E7%A4%BA%E4%B8%80%E5%AE%9A%E5%BD%B1%E5%93%8D%E7%9A%84%E8%84%86%E5%BC%B1%E6%80%A7)

[5.7、第七步：仅显示已知利用的漏洞](#5.7%E3%80%81%E7%AC%AC%E4%B8%83%E6%AD%A5%EF%BC%9A%E4%BB%85%E6%98%BE%E7%A4%BA%E5%B7%B2%E7%9F%A5%E5%88%A9%E7%94%A8%E7%9A%84%E6%BC%8F%E6%B4%9E)

[5.8、第八步：结果输出到文件中](#5.8%E3%80%81%E7%AC%AC%E5%85%AB%E6%AD%A5%EF%BC%9A%E7%BB%93%E6%9E%9C%E8%BE%93%E5%87%BA%E5%88%B0%E6%96%87%E4%BB%B6%E4%B8%AD)

---


---


 

## 一、简介：

> 
WES-NG是一个基于Windows实用程序输出的工具，它提供了操作系统易受攻击的漏洞列表，包括对这些漏洞的任何攻击。支持Windows XP和Windows 11之间的每个Windows操作系统，包括其Windows Server对应操作系统。


---


---


## 二、下载：

> 
<h3>2.1、GitHub：</h3>
[bitsadmin/wesng: Windows Exploit Suggester - Next Generation (github.com)<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://github.com/bitsadmin/wesng](https://github.com/bitsadmin/wesng)Windows的话就直接下载压缩文件

 Linux就在命令行git


---


---


## 三、命令选项

> 
下载CVE的最新列表
-u, --update
<hr/>
定义zip文件（默认：defacitions.zip）
--definitions [DEFINITIONS]
<hr/>
除了SystemInfo.txt文件中列出的内容外，手动指定已安装的补丁程序
-p INSTALLEDPATCH [INSTALLEDPATCH ...]
--patches INSTALLEDPATCH [INSTALLEDPATCH ...]      
<hr/>
过滤出在最新KB发布日期之前发布的KBS的漏洞安装
-d, --usekbdate      
<hr/>
仅显示已知利用的漏洞
-e, --exploits-only  
<hr/>
隐藏例如Adobe Flash Player和Microsoft Edge的漏洞
--hide HIDDENVULN [HIDDENVULN ...]
<hr/>
仅显示具有给定影响的漏洞
 -i IMPACTS [IMPACTS ...], --impact IMPACTS [IMPACTS ...]  
<hr/>
仅显示给定严重性的漏洞
-s SEVERITIES [SEVERITIES ...], --severity SEVERITIES [SEVERITIES ...]
<hr/>
将结果存储在文件中
-o [OUTPUTFILE], --output [OUTPUTFILE]
<hr/>
隐藏漏洞，如果在Microsoft Update目录中列出了安装的HotFix，则取代原始Bulletinkb
--muc-lookup          
<hr/>
在没有此参数的情况下运行时，指定操作系统或ID
--os [OPERATING_SYSTEM]
<hr/>
显示颜色的控制台输出（需要TermColor库）
-c, --color          
<hr/>
显示此帮助消息和退出
-h, --help            
<hr/>
下载最新版本的wes.py<br/>   --update-wes          


---


---


---


---


---


---


---


---


## 四、示例：

> 
下载最新定义<br/>   wes.py --update<br/>   wes.py -u
<hr/>
确定漏洞<br/>   wes.py systeminfo.txt
<hr/>
使用QFE文件确定漏洞。首先在没有-os参数的情况下列出OS<br/>   wes.py --qfe qfe.txt --os 'Windows 10 Version 20H2 for x64-based Systems'<br/>   wes.py -q qfe.txt --os 9
<hr/>
确定漏洞和输出以归档<br/>   wes.py systeminfo.txt --output vulns.csv<br/>   wes.py systeminfo.txt -o vulns.csv
<hr/>
确定明确指定KB的漏洞以减少假阳性<br/>   wes.py systeminfo.txt --patches KB4345421 KB4487017<br/>   wes.py systeminfo.txt -p KB4345421 KB4487017
<hr/>
确定漏洞过滤出来的KB的漏洞，这些漏洞已发布在最新KB的发布日期之前已发布<br/>   wes.py systeminfo.txt --usekbdate<br/>   wes.py systeminfo.txt -d
<hr/>
确定明确指定定义文件的漏洞<br/>   wes.py systeminfo.txt --definitions C:\tmp\mydefs.zip
<hr/>
仅列出具有漏洞利用的漏洞，不包括IE，Edge和Flash<br/>   wes.py systeminfo.txt --exploits-only --hide "Internet Explorer" Edge Flash<br/>   wes.py systeminfo.txt -e --hide "Internet Explorer" Edge Flash
<hr/>
仅显示一定影响的脆弱性<br/>   wes.py systeminfo.txt --impact "Remote Code Execution"<br/>   wes.py systeminfo.txt -i "Remote Code Execution"
<hr/>
仅显示一定严重性的脆弱性<br/>   wes.py systeminfo.txt --severity critical<br/>   wes.py systeminfo.txt -s critical
<hr/>
 根据缺失的补丁显示漏洞<br/>   wes.py --missing missing.txt<br/>   wes.py -m missing.txt
<hr/>
根据指定操作系统的缺失补丁显示漏洞<br/>   wes.py --missing missing.txt --os "Windows 10 Version 1809 for x64-based Systems"<br/>   wes.py -m missing.txt --os 2
<hr/>
验证取代微软的在线更新目录
wes.py systeminfo.txt --muc-lookup
<hr/>
显示彩色输出
wes.py systeminfo.txt --color<br/> wes.py systeminfo.txt -c
<hr/>
下载最新版本的WES
wes.py --update-wes


---


---


---


---


---


---


---


---


---


## 五、使用方法：

> 
<h3>5.1、第一步：收集系统补丁 </h3>
打开命令提示符（win+R  cmd）
收集‎‎操作系统‎‎版本和缺少的补丁到使用 ‎‎WES-NG‎‎ 识别缺少的补丁，包括使用一些描述的过滤器和 csv 输出选项。
systeminfo &gt; systeminfo.txt




 <img alt="" height="73" src="https://img-blog.csdnimg.cn/1d8c34ab3c6b40be836c0592d939f8d0.png" width="560"/>
 <img alt="" height="888" src="https://img-blog.csdnimg.cn/5d3efa6b30df47b0b7ee71ed18819c42.png" width="1016"/>





> 
<h3>5.2、第二步：将收集的文件放到文件下</h3>






> 
<h3>5.3、第三步：进入Windows powershell</h3>
在文件夹内打开Windows powershell（或者命令提示符进入文件夹内）

 右键（或者按住shift再右键）




> 
<h3>5.4、第四步：检查更新</h3>
python wes.py --update

 使用的是20220512


> 
<h3>5.5、第五步：检测缺少的补丁</h3>
python wes.py systeminfo.txt



缺少补丁：3




> 
<h3>5.6、第六步：仅显示一定影响的脆弱性</h3>
python wes.py systeminfo.txt --impact "Remote Code Execution"

Missing patches: 3
缺少补丁：3
 Done. Displaying 13 of the 65 vulnerabilities found.
完毕。显示发现的65个漏洞中的13个。




> 
<h3>5.7、第七步：仅显示已知利用的漏洞</h3>
python wes.py systeminfo.txt --impact "Remote Code Execution" -e

 Done. No vulnerabilities found
完毕。找不到漏洞



> 
<h3>5.8、第八步：结果输出到文件中</h3>
python wes.py systeminfo.txt --impact "Remote Code Execution" -e -o rce.csv

 我这里没有可利用漏洞，所以就输出不了


notepad rce.csv
（使用记事本打开）

 记事本会直接弹出rce.csv文件

