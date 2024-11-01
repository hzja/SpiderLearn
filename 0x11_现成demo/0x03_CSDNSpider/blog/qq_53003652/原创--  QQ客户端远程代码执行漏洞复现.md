# 原创
：  QQ客户端远程代码执行漏洞复现

# QQ客户端远程代码执行漏洞复现

今天网传了一个QQ的0day，“QQ桌面客户端远程执行的漏洞，攻击者可以利用该漏洞在QQ客户端上进行无需用户确认文件下载执行行为，当用户点击消息链接时，QQ客户端会自动下载并打开文件，最终实现远程代码执行的目的。建议谨慎点击任何消息链接。”现在就来复现一下。<br/> 漏洞原理：<br/> 该漏洞为逻辑漏洞，腾讯QQ windows 客户端的“文件传输消息”在经过“回复<br/> 消息”功能处理后，该文件会变为无需任何弹窗确认，点击消息文本后即可自动下载并打开文件的处理方式。<br/> 1.本地创建一个txt，里面可以写上你想执行的cmd命令，比如写上calc，就是弹出计算器，然后重命名保存为.bat批处理文件。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4c13bb50af124992864a92889616ff2b.png"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/997ff6d4283a48dba00055ea2f9946f9.png"/><br/> 2.然后先转发给自己小号

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4571812c63d4473d8b8635cd8d48f1fe.png"/><br/> 然后右击该消息选择回复，随便输入点内容，继续发送给小号<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4845e1de2d5b4f90b7261a1d9a5b4fb9.png"/><br/> 3.将回复了的消息右击转发给好友。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/c9802a84439341c18a640d2cc74f0156.png"/><br/> 当好友点击剪头指向的区域时，这个文件会自动下载并运行。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f191d4d8d1e6458aae7b3ddc8b940618.png"/><br/> 直接弹出计算器来。<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/e9166c779c35496eac42d5241cfc1f82.png"/><br/> 注：严禁使用该漏洞于真实聊天环境，这种行为只能在合法的安全测试环境中进行，且仅限于授权的活动。
