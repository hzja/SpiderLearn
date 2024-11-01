# 原创
：  Bootstrap垂直表单

# Bootstrap垂直表单

**Index.html**

```
&lt;!DOCTYPE html&gt;
&lt;html lang="zh-cn"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;垂直表单&lt;/title&gt;
    &lt;link rel="stylesheet" href="css/bootstrap.css"&gt;
    &lt;link href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" rel="stylesheet"&gt;
    &lt;style&gt;
        .div2{
            width: 540px;
            height: 620px;
            margin: 10px 20px;
            padding: 10px 20px;
            border: #930;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container"&gt;
        &lt;div class="div2"&gt;
            &lt;h1 style="color: burlywood"&gt;登录框&lt;/h1&gt;
            &lt;form action="#" role="form"&gt;
                &lt;div class="form-group"&gt;
                    &lt;label for="uname" class="control-label"&gt;用户名&lt;/label&gt;
                    &lt;input type="text" id="uname" class="form-control" placeholder="请输入用户名"&gt;
                &lt;/div&gt;
                &lt;div class="form-group"&gt;
                    &lt;label for="upwd" class="control-label"&gt;密码&lt;/label&gt;
                    &lt;input type="password" id="upwd" class="form-control" placeholder="请输入密码"&gt;
                &lt;/div&gt;
                &lt;div class="form-group"&gt;
                    &lt;div class="checkbox"&gt;
                        &lt;label&gt;&lt;input type="checkbox"&gt;七天免费登录&lt;/label&gt;
                    &lt;/div&gt;
                &lt;/div&gt;
                &lt;div class="form-group"&gt;
                    &lt;input type="button" id="login" value="登录" class="btnbtn-success"&gt;
                    &lt;input type="button" id="logout" value="取消" class="btnbtn-danger"&gt;
                &lt;/div&gt;
            &lt;/form&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;

```
