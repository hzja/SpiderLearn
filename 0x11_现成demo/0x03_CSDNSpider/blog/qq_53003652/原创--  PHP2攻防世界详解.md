# 原创
：  PHP2攻防世界详解

# PHP2攻防世界详解

进入题目场景，只有一串没用的提示<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/5e15de79e7f841a8b3cf36d03c41acd6.png"/><br/> 查看网页源代码，也是什么都没有，在URL后加index.php,也是什么都没有，这时，在URL后加index.phps，可以发现有东西出来了<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/09f89abb73a149b4ba8eb8676809b688.png"/><br/> phps文件就是php的源代码文件，通常用于提供给用户（访问者）查看php代码，因为用户无法直接通过Web浏览器看到php文件的内容，所以需要用phps文件代替。其实，只要不用php等已经在服务器中注册过的MIME类型为文件即可，但为了国际通用，所以才用了phps文件类型。<br/> 右键查看网页源代码审计代码<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/f96d6d3ba59b406fb4add87cfe29afb2.png"/><br/> $_GET本身自带一次urldecode，代码里又进行了一次urldecode，所以要对id赋的值admin进行两次url编码，编码后为%25%36%31%25%36%34%25%36%64%25%36%39%25%36%65<br/> 此时即可获取flag<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/202f1bf595ba42ccae2bd0a7b7d04865.png"/><br/> flag：cyberpeace{1326f3a6bffc6d6f1a055ffbad9bb5df}
