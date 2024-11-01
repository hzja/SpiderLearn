# 原创
：  11-5 Apache基线检查

# 11-5 Apache基线检查

#### 一、确保对OS根目录禁用覆盖

        当 `AllowOverride` 指令设置为 `None` 时，Apache 将禁止在该目录下使用 `.htaccess` 文件来覆盖任何配置项。这意味着，除非您在主配置文件中显式地指定，否则该目录下的任何 `.htaccess` 文件都将被忽略。

        禁用 `.htaccess` 文件可以提高服务器的安全性，因为这样可以防止恶意用户通过 `.htaccess` 文件来修改 Apache 的配置或执行其他潜在的攻击。

##### 操作方法:

        使用 Vim 或其他文本编辑器打开 Apache 的主配置文件，路径为您的主配置文件的绝对路径。如果主配置文件中包含 `include &lt;path&gt;` 这样的语句，则需要找到 `&lt;path&gt;` 指定的文件并进行编辑。

配置示例：

```
# 打开配置文件
vim /etc/httpd/conf/httpd.conf
```

在配置文件中找到&lt;Directory /&gt; 开头的配置项

```
&lt;Directory /&gt;
    ...
    AllowOverride none
    ...
&lt;/Directory&gt;


```

 保存配置文件并重新启动 Apache 服务器以使更改生效。

#### 二、确保默认情况下拒绝访问OS根目录

        当使用 
