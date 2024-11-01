# 原创
：  BurpSuite拦截不到127.0.0.1或者localhost的问题

# BurpSuite拦截不到127.0.0.1或者localhost的问题

> 
背景：在本地练习一些web安全靶场的时候需要进行抓包，但是BurpSuite无法进行抓包


> 
BurpSuite工作流程：burp Suite的工作流程是浏览器访问某个站点，先将发送给服务器的请求发送给BurpSuite处理。由Burp Suite来决定是发送这个请求还是修改或者拦截这个请求；BurpSuite默认监听的是本地（localhost或者127.0.0.1）的8080端口（如果端口被占用，可以修改），必须要让浏览器所有的数据包都经过127.0.0.1:8080


> 
解决方案：将127.0.0.1改为本机ip即可

