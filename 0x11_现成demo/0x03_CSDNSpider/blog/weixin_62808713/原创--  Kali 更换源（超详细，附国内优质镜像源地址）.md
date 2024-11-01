# 原创
：  Kali 更换源（超详细，附国内优质镜像源地址）

# Kali 更换源（超详细，附国内优质镜像源地址）

1.进入管理员下的控制台。

2. 输入密码后点击“授权”。

3.在控制台内输入下面的内容。

```
vim /etc/apt/sources.list
```

4.敲击回车后会进入下面的页面。

5.来到这个页面后的第一部是按键盘上的“i”键，左下角出现“插入”后说明操作正确。

6.使用“#”将原本的源给注释掉。

7. 从下面的源内选择一个复制下来准备粘贴进去（都是优质源，复制哪个都可以）。

```
中科大Kali镜像源

deb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
deb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib
```

```
阿里云Kali镜像源

deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
```

```
清华大学Kali镜像源

deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
```

8.将上面复制的源粘贴到下图所示位置。

9.按键盘上的“ESC”键，左下角的“插入”消失说明操作正确。

10.输入“:wq!”（注意使用英文输入法），这步操作是保存配置并退出。

```
:wq!
```

11. 回车后便成功保存并退出了。

12.之后执行下面的命令更新源。

```
apt-get update
```

13.回车后等待即可，约一分钟，出现下面页面即更新成功了。

14.接下来可以使用下面的命令来对软件进行更新（如果不需要更新则可以忽略下面内容）。

```
命令1：
apt-get upgrade

命令2：
apt-get dist-upgrade

上面两条命令均是用来更新所有软件的，不同的是：
它能识别新版本的依赖关系，
将不要的依赖进行卸载，
将需要升级的依赖进行升级。
```

        在更新软件期间可能会需要确认、配置、显示更新日志等，按照提示操作即可。

15.安装或更新完成后，会遗留一些软件的安装包，会占用部分硬盘空间，可使用下面的命令来对其进行清理。

```
apt-get clean
```
