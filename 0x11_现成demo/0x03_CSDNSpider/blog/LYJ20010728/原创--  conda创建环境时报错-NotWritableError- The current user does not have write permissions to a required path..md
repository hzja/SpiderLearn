# 原创
：  conda创建环境时报错：NotWritableError: The current user does not have write permissions to a required path.

# conda创建环境时报错：NotWritableError: The current user does not have write permissions to a required path.

> 
背景：<br/> 在Ubuntu系统上装Anaconda3时，安装完成后无法使用conda命令


> 
原因：<br/> 考虑安装时是否使用的root权限进行安装


> 
解决：<br/> 此处针对安装时使用root权限进行安装的步骤；<br/> 找到anaconda文件夹所在的位置，输入：sudo chown -R xxx anaconda3 #xxx为自己的用户名<br/> 待命令执行完成后即可使用conda命令

