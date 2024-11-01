# 原创
：  Github&Hexo 搭建个人博客

# Github&amp;Hexo 搭建个人博客

#### Github&amp;Hexo 搭建个人博客

## 创建Repository

## 配置SSH keys

> 
检查自己电脑上现有的 SSH key


> 
生成新的 SSH Key


> 
添加SSH Key到GitHub<br/> 在本地文件夹找到`id_rsa.pub`文件，看上面的图片第四行的位置告诉你存在哪里了


> 
这个文件复制全部内容到github相应位置


> 
测试一下


> 
设置用户信息


> 
GitHub 也是用这些信息来做权限的处理，输入下面的代码进行个人信息的设置，把名称和邮箱替换成你自己的，名字必须是你的真名，而不是GitHub的昵称


## 博客部署

> 
进入 Github 个人主页中的 Repository，复制新建的独立博客项目的 SSH 码


> 
编辑整站配置文件，把刚刚复制的 SSH 码粘贴到 repo 后面


```
# Deployment
## Docs: https://hexo.io/docs/one-command-deployment
deploy:
  type: git
  repo: git@github.com:H3rmesk1t/H3rmesk1t.github.io.git
  branch: master

```

> 
执行命令


```
hexo g
hexo d

```
