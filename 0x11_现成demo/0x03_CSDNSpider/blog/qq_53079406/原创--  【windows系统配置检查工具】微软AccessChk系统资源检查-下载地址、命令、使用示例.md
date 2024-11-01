# 原创
：  【windows系统配置检查工具】微软AccessChk系统资源检查：下载地址、命令、使用示例

# 【windows系统配置检查工具】微软AccessChk系统资源检查：下载地址、命令、使用示例

**目录**

[一、简介：](#%E4%B8%80%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[1.1、概述：](#1.1%E3%80%81%E6%A6%82%E8%BF%B0%EF%BC%9A)

[1.2、下载地址（微软）：](#1.2%E3%80%81%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80%EF%BC%88%E5%BE%AE%E8%BD%AF%EF%BC%89%EF%BC%9A)

[二、命令：](#%E4%BA%8C%E3%80%81%E5%91%BD%E4%BB%A4%EF%BC%9A)

[三、使用方法：](#%E4%B8%89%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[3.1、启动：](#3.1%E3%80%81%E5%90%AF%E5%8A%A8%EF%BC%9A)

[3.2、示例：](#3.2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[3.2.1、访问权限](#3.2.1%E3%80%81%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90)

[3.1.2、用户特定权限](#3.1.2%E3%80%81%E7%94%A8%E6%88%B7%E7%89%B9%E5%AE%9A%E6%9D%83%E9%99%90)

[3.1.3、指定用户全部权限](#3.1.3%E3%80%81%E6%8C%87%E5%AE%9A%E7%94%A8%E6%88%B7%E5%85%A8%E9%83%A8%E6%9D%83%E9%99%90)

[3.1.4、指定用户对特定服务权限](#3.1.4%E3%80%81%E6%8C%87%E5%AE%9A%E7%94%A8%E6%88%B7%E5%AF%B9%E7%89%B9%E5%AE%9A%E6%9C%8D%E5%8A%A1%E6%9D%83%E9%99%90)

[3.1.5、查出服务的权限](#3.1.5%E3%80%81%E6%9F%A5%E5%87%BA%E6%9C%8D%E5%8A%A1%E7%9A%84%E6%9D%83%E9%99%90)

[3.1.6、显示无权访问指定注册表对象](#3.1.6%E3%80%81%E6%98%BE%E7%A4%BA%E6%97%A0%E6%9D%83%E8%AE%BF%E9%97%AE%E6%8C%87%E5%AE%9A%E6%B3%A8%E5%86%8C%E8%A1%A8%E5%AF%B9%E8%B1%A1)

[3.1.7、秘钥安全性](#3.1.7%E3%80%81%E7%A7%98%E9%92%A5%E5%AE%89%E5%85%A8%E6%80%A7)

[3.1.8、显示完整性级别的文件](#3.1.8%E3%80%81%E6%98%BE%E7%A4%BA%E5%AE%8C%E6%95%B4%E6%80%A7%E7%BA%A7%E5%88%AB%E7%9A%84%E6%96%87%E4%BB%B6)

[3.1.9、查看可操作的全局对象](#3.1.9%E3%80%81%E6%9F%A5%E7%9C%8B%E5%8F%AF%E6%93%8D%E4%BD%9C%E7%9A%84%E5%85%A8%E5%B1%80%E5%AF%B9%E8%B1%A1)

---


## 一、简介：

> 
<h3>1.1、概述：</h3>
微软提供的一款安全检查工具，是Sysintenals集合中的一款工具，作为确保他们创建安全环境Windows管理员通常需要知道特定用户或组对资源（包括文件、目录、注册表项、全局对象和Windows服务）拥有哪些类型的访问权限。
<hr/>
顾名思义，使用它可以对Windows系统中的一些系统文件、服务、注册表等进行管理和维护排查等功能，可以很直观清晰的发现系统资源存在的缺陷，对其进行提权等利用


> 
<h3>1.2、下载地址（微软）：</h3>
[AccessChk - Windows Sysinternals | Microsoft Docshttps://docs.microsoft.com/zh-cn/sysinternals/downloads/accesschk<img alt="icon-default.png?t=M4AD" src="https://csdnimg.cn/release/blog_editor_html/release2.1.3/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M4AD"/>https://docs.microsoft.com/zh-cn/sysinternals/downloads/accesschk](https://docs.microsoft.com/zh-cn/sysinternals/downloads/accesschk)第一次使用会弹出一个对话框
点击同意


---


---


## 二、命令：

> 
<table><thead>|参数|说明
</thead><tbody>|**-a**|名称是Windows帐户权限。 指定 `"*"` 为显示分配给用户的所有权限的名称。 请注意，指定特定权限时，仅显示直接分配给右侧的组和帐户。
|**-c**|名称是Windows服务，例如。 `ssdpsrv` 指定 `"*"` 为显示所有服务的名称，并 `scmanager` 检查服务控制管理器的安全性。
|**-d**|仅处理目录或顶级密钥
|**-e**|仅显示 (Windows Vista 及更高级别的显式设置完整性级别)
|**-f**|如果如下所示 `-p`，则显示完整的进程令牌信息，包括组和特权。 否则为要从输出中筛选的逗号分隔帐户的列表。
|**-h**|名称是文件或打印机共享。 指定 `"*"` 为显示所有共享的名称。
|**-i**|在转储完全访问控制列表时，仅忽略仅继承 ACE 的对象。
|**-k**|名称是注册表项，例如 `hklm\software`
|**-l**|显示完整的安全描述符。 添加 `-i` 以忽略继承的 ACE。
|**-n**|仅显示没有访问权限的对象
|**-o**|名称是对象管理器命名空间中的对象， (默认值为根) 。 若要查看目录的内容，请使用尾随反斜杠或添加 `-s`指定名称。 添加 `-t` 和对象类型 (，例如节) 仅查看特定类型的对象。
|**-p**|名称是进程名称或 PID，例如 `cmd.exe` ， (指定 `"*"` 为显示所有进程) 的名称。 添加 `-f` 以显示完整的进程令牌信息，包括组和特权。 添加 `-t` 以显示线程。
|**-q**|省略横幅
|**-r**|仅显示具有读取访问权限的对象
|**-s**|Recurse
|**-t**|对象类型筛选器，例如 `"section"`
|**-u**|禁止显示错误
|**-v**|详细 (包括Windows Vista 完整性级别)
|**-w**|仅显示具有写入访问权限的对象
</tbody></table>


---


---


## 三、使用方法：

> 
<h3>3.1、启动：</h3>
（或者使用命令提示符进入）

<pre>`.\accesschk.exe 加上命令`</pre>


> 
<h3>3.2、示例：</h3>
<h4>3.2.1、访问权限</h4>
帐户（指定账户）对指定文件和目录（ `\Windows\System32`）的访问权限：
<pre>`.\accesschk.exe "当前用户名" c:\windows\system32`</pre>

<hr/>

<h4>3.1.2、用户特定权限</h4>
显示用户组成员具有写入访问权限
<pre><code>.\accesschk.exe 指定用户或用户组 -cw *
</code></pre>



<hr/>
<h4>3.1.3、指定用户全部权限</h4>
查看某个用户或用户组对所有服务的权限
<pre>`.\accesschk.exe  administrators -cu *`</pre>

<hr/>
<h4>3.1.4、指定用户对特定服务权限</h4>
查看某个用户或用户组对指定服务（eg:AppXSvc）的权限
<pre>`.\accesschk.exe  administrators -cu AppXSvc`</pre>

<hr/>
<h4>3.1.5、查出服务的权限</h4>
具有写入权限的windows服务 
<pre>`.\accesschk.exe  -cw *`</pre>


<hr/>
<h4>3.1.6、显示无权访问指定注册表对象</h4>
查看特定帐户下的 `HKLM\CurrentUser` 注册表项无权访问：
<pre><code>.\accesschk.exe -kns 特定账户 hklm\software
</code></pre>

<hr/>
<h4>3.1.7、秘钥安全性</h4>
查看 HKLM\Software 密钥的安全性：
<pre><code>.\accesschk.exe -k hklm\software
</code></pre>


<hr/>

<h4>3.1.8、显示完整性级别的文件</h4>
查看具有显式完整性级别的所有文件 `\Users\用户名`
<pre><code>.\accesschk.exe -e -s -u c:\users\用户名
</code></pre>


<hr/>
<h4>3.1.9、查看可操作的全局对象</h4>
查看每个人都可以修改的所有全局对象：
<pre>`.\accesschk.exe  指定用户 -ou \`</pre>





#### 3.2.1、访问权限

---


#### 3.1.3、指定用户全部权限

---


#### 3.1.5、查出服务的权限

---


#### 3.1.7、秘钥安全性

---


#### 3.1.9、查看可操作的全局对象
