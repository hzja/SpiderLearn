# 原创
：  前端项目部署到服务器出现的问题：前端项目用的history模式，刷新会404，该怎么解决呢？

# 前端项目部署到服务器出现的问题：前端项目用的history模式，刷新会404，该怎么解决呢？

**部分数据来源：**ChatGPT

#### 引言

        在使用history模式时，可能会遇到刷新页面出现404的情况，这是因为服务器没有正确地处理路由请求。

### 解决这个问题的方法有两种：

#### 1. 配置服务器

        在使用history模式时，需要配置服务器以支持路由。具体来说，需要在服务器上配置一个重定向规则，将所有路由请求都指向index.html文件。例如，如果你使用的是Apache服务器，可以在.htaccess文件中添加以下规则：

```
&lt;IfModule mod_rewrite.c&gt;
  RewriteEngine On

  RewriteBase /
  RewriteRule ^index\.html$ - [L]
  RewriteCond %{REQUEST_FILENAME} !-f
  RewriteCond %{REQUEST_FILENAME} !-d
  RewriteRule . /index.html [L]
&lt;/IfModule&gt;

```

这个规则会将所有非文件和目录的请求都重定向到/index.html文件，从而让前端路由能够正常工作。

#### 2. 改用hash模式

        另一种解决方法是放弃使用history模式，改用hash模式。在hash模式下，需要在URL中添加一个#号，这个#号后面的内容将被当作前端路由的一部分处理，而服务器不会对这个#号后面的内容进行处理。因此，在使用hash模式时即使刷新页面也不会出现404错误。

具体来说，可以通过在vue-router的配置中将mode属性设置为hash来启用hash模式。

```
const router = new VueRouter({
  mode: 'hash',
  routes: [...]
})

```

以上两种方法都可以解决前端路由刷新时出现404错误的问题。具体方法选择可以根据实际情况来决定。

希望这篇文章能帮助到出现类似问题的读者。
