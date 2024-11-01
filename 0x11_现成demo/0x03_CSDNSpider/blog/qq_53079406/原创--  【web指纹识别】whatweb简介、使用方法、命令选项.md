# 原创
：  【web指纹识别】whatweb简介、使用方法、命令选项

# 【web指纹识别】whatweb简介、使用方法、命令选项

**目录**

[一、web指纹识别](#%E4%B8%80%E3%80%81web%E6%8C%87%E7%BA%B9%E8%AF%86%E5%88%AB)

[二、whatweb](#%E4%BA%8C%E3%80%81whatweb)

[2.1、简介：](#2.1%E3%80%81%E7%AE%80%E4%BB%8B%EF%BC%9A)

[2.2、下载：](#2.2%E3%80%81%E4%B8%8B%E8%BD%BD%EF%BC%9A)

[2.3、使用方法：](#2.3%E3%80%81%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A)

[2.4、示例用法：](#2.4%E3%80%81%E7%A4%BA%E4%BE%8B%E7%94%A8%E6%B3%95%EF%BC%9A)

[2.5、命令选项](#2.5%E3%80%81%E5%91%BD%E4%BB%A4%E9%80%89%E9%A1%B9)

[2.5.1、目标选择：](#2.5.1%E3%80%81%E7%9B%AE%E6%A0%87%E9%80%89%E6%8B%A9%EF%BC%9A)

[2.5.2、目标修改：](#2.5.2%E3%80%81%E7%9B%AE%E6%A0%87%E4%BF%AE%E6%94%B9%EF%BC%9A)

[2.5.3、侵略：](#2.5.3%E3%80%81%E4%BE%B5%E7%95%A5%EF%BC%9A)

[2.5.4、HTTP选项：](#2.5.4%E3%80%81HTTP%E9%80%89%E9%A1%B9%EF%BC%9A)

[2.5.5、验证：](#2.5.5%E3%80%81%E9%AA%8C%E8%AF%81%EF%BC%9A)

[2.5.6、插件：](#2.5.6%E3%80%81%E6%8F%92%E4%BB%B6%EF%BC%9A)

[2.5.7、输出：](#2.5.7%E3%80%81%E8%BE%93%E5%87%BA%EF%BC%9A)

[2.5.8、性能与稳定性：](#2.5.8%E3%80%81%E6%80%A7%E8%83%BD%E4%B8%8E%E7%A8%B3%E5%AE%9A%E6%80%A7%EF%BC%9A)

[2.5.9、帮助和杂项：](#2.5.9%E3%80%81%E5%B8%AE%E5%8A%A9%E5%92%8C%E6%9D%82%E9%A1%B9%EF%BC%9A)

---


---


 

## 一、web指纹识别

> 
web指纹扫描四大特征：应用名称（版本）、服务器软件（版本）、编程语言（版本）、应用框架（版本）
<hr/>
网站指纹信息包括：应用名、版本、前端框架、后端框架、服务端语言、服务器操作系统、网站容器、内容管理系统和数据库等
<hr/>
设备指纹信息包括：应用名、版本、开放端口、操作系统、服务名、地理位置等


---


## 二、whatweb

> 
<h3>2.1、简介：</h3>
识别网站的详细信息：CMS类型、博客平台、中间件、web框架模块、网站服务器、脚本类型、JavaScript库、IP、cookie等，还标识版本号，电子邮件地址，账户ID，Web框架模块，SQL错误等。
<hr/>
可以隐秘、快速、彻底或缓慢扫描。
支持攻击级别来控制速度和可靠性之间的权衡。


> 
<h3>2.2、下载：</h3>
 kali自带的工具






> 
<h3>2.3、使用方法：</h3>
 whatweb [options] &lt;URLs&gt;
whatweb + 各种选项 + 网址


> 
<h3>2.4、示例用法：</h3>
识别网站
whatweb baidu.com

<hr/>
扫描reddit.com slashdot.org带有详细的插件描述。
whatweb -v reddit.com slashdot.org
<hr/>
wired.com的积极扫描检测到WordPress的确切版本。
whatweb -a 3 www.wired.com
<hr/>
快速扫描本地网络并抑制错误。
 whatweb --no-errors 192.168.0.0/24
<hr/>
扫描HTTPS网站的本地网络
whatweb --no-errors --url-prefix https:// 192.168.0.0/24
<hr/>
扫描Alexa Top 1000中的跨域政策
whatweb -i plugin-development/alexa-top-100.txt \<br/>   --url-suffix /crossdomain.xml -p crossdomain_xml


---


---


<br/>  

> 
<h3>2.5、命令选项</h3>
<h4>2.5.1、目标选择：</h4>
&lt;TARGETs&gt;                    
输入URL，主机名，IP地址，文件名或 IP范围在CIDR，X.X.X-X或X.x.x.x.x-x.x.x.x.x.x 格式
<br/>   --input-file=FILE, -i        
从文件中读取目标。你可以管道 直接使用-i /dev /stdin直接使用主机名或URL。
<hr/>
<h4>2.5.2、目标修改：</h4>
<br/>   --url-prefix                  Add a prefix to target URLs.<br/>   --url-suffix                  Add a suffix to target URLs.<br/>   --url-pattern                 Insert the targets into a URL.<br/>                                 e.g. example.com/%insert%/robots.txt
<hr/>
<h4>2.5.3、侵略：</h4>
<br/> The aggression level controls the trade-off between speed/stealth and<br/> reliability.<br/>   --aggression, -a=LEVEL        Set the aggression level. Default: 1.<br/>   1. Stealthy                   Makes one HTTP request per target and also<br/>                                 follows redirects.<br/>   3. Aggressive                 If a level 1 plugin is matched, additional<br/>                                 requests will be made.<br/>   4. Heavy                      Makes a lot of HTTP requests per target. URLs<br/>                                 from all plugins are attempted.
<hr/>
<h4>2.5.4、HTTP选项：</h4>
<br/>   --user-agent, -U=AGENT        Identify as AGENT instead of WhatWeb/0.5.5.<br/>   --header, -H                  Add an HTTP header. eg "Foo:Bar". Specifying a<br/>                                 default header will replace it. Specifying an<br/>                                 empty value, e.g. "User-Agent:" will remove it.<br/>   --follow-redirect=WHEN        Control when to follow redirects. WHEN may be<br/>                                 `never', `http-only', `meta-only', `same-site',<br/>                                 or `always'. Default: always.<br/>   --max-redirects=NUM           Maximum number of redirects. Default: 10.
<hr/>
<h4>2.5.5、验证：</h4>
<br/>   --user, -u=&lt;user:password&gt;    HTTP basic authentication.<br/>   --cookie, -c=COOKIES          Use cookies, e.g. 'name=value; name2=value2'.<br/>   --cookie-jar=FILE             Read cookies from a file.
PROXY:<br/>   --proxy                       &lt;hostname[:port]&gt; Set proxy hostname and port.<br/>                                 Default: 8080.<br/>   --proxy-user                  &lt;username:password&gt; Set proxy user and password.
<hr/>
<h4>2.5.6、插件：</h4>
<br/>   --list-plugins, -l            List all plugins.<br/>   --info-plugins, -I=[SEARCH]   List all plugins with detailed information.<br/>                                 Optionally search with keywords in a comma<br/>                                 delimited list.<br/>   --search-plugins=STRING       Search plugins for a keyword.<br/>   --plugins, -p=LIST            Select plugins. LIST is a comma delimited set<br/>                                 of selected plugins. Default is all.<br/>                                 Each element can be a directory, file or plugin<br/>                                 name and can optionally have a modifier, +/-.<br/>                                 Examples: +/tmp/moo.rb,+/tmp/foo.rb<br/>                                 title,md5,+./plugins-disabled/<br/>                                 ./plugins-disabled,-md5<br/>                                 -p + is a shortcut for -p +plugins-disabled.<br/>   --grep, -g=STRING|REGEXP      Search for STRING or a Regular Expression. Shows<br/>                                 only the results that match.<br/>                                 Examples: --grep "hello"<br/>                                 --grep "/he[l]*o/"<br/>   --custom-plugin=DEFINITION    Define a custom plugin named Custom-Plugin,<br/>                                 Examples: ":text=&gt;'powered by abc'"<br/>                                 ":version=&gt;/powered[ ]?by ab[0-9]/"<br/>                                 ":ghdb=&gt;'intitle:abc \"powered by abc\"'"<br/>                                 ":md5=&gt;'8666257030b94d3bdb46e05945f60b42'"<br/>                                 "{:text=&gt;'powered by abc'}"<br/>   --dorks=PLUGIN                List Google dorks for the selected plugin.
<hr/>
<h4>2.5.7、输出：</h4>
<br/>   --verbose, -v                 Verbose output includes plugin descriptions.<br/>                                 Use twice for debugging.<br/>   --colour,--color=WHEN         control whether colour is used. WHEN may be<br/>                                 `never', `always', or `auto'.<br/>   --quiet, -q                   Do not display brief logging to STDOUT.<br/>   --no-errors                   Suppress error messages.
LOGGING:<br/>   --log-brief=FILE              Log brief, one-line output.<br/>   --log-verbose=FILE            Log verbose output.<br/>   --log-errors=FILE             Log errors.<br/>   --log-xml=FILE                Log XML format.<br/>   --log-json=FILE               Log JSON format.<br/>   --log-sql=FILE                Log SQL INSERT statements.<br/>   --log-sql-create=FILE         Create SQL database tables.<br/>   --log-json-verbose=FILE       Log JSON Verbose format.<br/>   --log-magictree=FILE          Log MagicTree XML format.<br/>   --log-object=FILE             Log Ruby object inspection format.<br/>   --log-mongo-database          Name of the MongoDB database.<br/>   --log-mongo-collection        Name of the MongoDB collection.<br/>                                 Default: whatweb.<br/>   --log-mongo-host              MongoDB hostname or IP address.<br/>                                 Default: 0.0.0.0.<br/>   --log-mongo-username          MongoDB username. Default: nil.<br/>   --log-mongo-password          MongoDB password. Default: nil.<br/>   --log-elastic-index           Name of the index to store results. Default: whatweb<br/>   --log-elastic-host            Host:port of the elastic http interface. Default: 127.0.0.1:9200
<hr/>
<h4>2.5.8、性能与稳定性：</h4>
<br/>   --max-threads, -t             Number of simultaneous threads. Default: 25.<br/>   --open-timeout                Time in seconds. Default: 15.<br/>   --read-timeout                Time in seconds. Default: 30.<br/>   --wait=SECONDS                Wait SECONDS between connections.<br/>                                 This is useful when using a single thread.
<hr/>
<h4>2.5.9、帮助和杂项：</h4>
<br/>   --short-help                  Short usage help.<br/>   --help, -h                    Complete usage help.<br/>   --debug                       Raise errors in plugins.<br/>   --version                     Display version information.


#### 2.5.1、目标选择：

---


#### 2.5.3、侵略：

---


#### 2.5.5、验证：

---


#### 2.5.7、输出：

---


#### 2.5.9、帮助和杂项：

<br/>  
