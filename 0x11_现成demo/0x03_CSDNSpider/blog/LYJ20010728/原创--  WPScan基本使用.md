# 原创
：  WPScan基本使用

# WPScan基本使用

#### WPScan基本使用

## WPScan 简介

> 



> 
WPScan已经被预安装在以下Linux系统中：



## WPScan 参数

> 
使用`wpscan -h`可以查看各种参数以及定义


> 
常用选项



> 
其他选项



## WPScan 扫描指定站点

> 



```
wpscan --url [wordpress url]

```

> 
例如：`wpscan --url http://192.168.56.103/wordpress`


```
┌──(kali㉿kali)-[~/Desktop]
└─$ wpscan --url http://192.168.56.103/wordpress
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.18
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://192.168.56.103/wordpress/ [192.168.56.103]
[+] Started: Thu Aug  5 11:20:00 2021

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.7 (Ubuntu)
 |  - X-Powered-By: PHP/5.5.9-1ubuntu4.22
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://192.168.56.103/wordpress/xmlrpc.php
 | Found By: Link Tag (Passive Detection)
 | Confidence: 100%
 | Confirmed By: Direct Access (Aggressive Detection), 100% confidence
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://192.168.56.103/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Registration is enabled: http://192.168.56.103/wordpress/wp-login.php?action=register
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.56.103/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.56.103/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 4.8.1 identified (Insecure, released on 2017-08-02).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.56.103/wordpress/?feed=rss2, &lt;generator&gt;https://wordpress.org/?v=4.8.1&lt;/generator&gt;
 |  - http://192.168.56.103/wordpress/?feed=comments-rss2, &lt;generator&gt;https://wordpress.org/?v=4.8.1&lt;/generator&gt;

[+] WordPress theme in use: twentyfifteen
 | Location: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/readme.txt
 | [!] The version is out of date, the latest version is 3.0
 | Style URL: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/style.css?ver=4.8.1
 | Style Name: Twenty Fifteen
 | Style URI: https://wordpress.org/themes/twentyfifteen/
 | Description: Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple, st...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.8 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/style.css?ver=4.8.1, Match: 'Version: 1.8'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:00 &lt;=============================================================================================================================================================&gt; (137 / 137) 100.00% Time: 00:00:00

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Thu Aug  5 11:20:03 2021
[+] Requests Done: 139
[+] Cached Requests: 36
[+] Data Sent: 37.797 KB
[+] Data Received: 19.845 KB
[+] Memory used: 211.109 MB
[+] Elapsed time: 00:00:02


```

## WPScan 扫描指定用户

```
wpscan --url https://www.xxxxxxx.wiki/ --enumerate u

```

## WPScan 扫描插件漏洞

> 



```
wpscan --url https://www.xxxxx.wiki/ --enumerate p
//备注：--url与-u参数相同，下面雷同

```

> 
可以使用下列命令来扫描目标插件中的安全漏洞：


```
wpscan --url https://www.xxxxx.wiki/ --enumerate vp

```

## WPScan 扫描主题漏洞

> 
使用下列命令对主题进行扫描：


```
wpscan --url https://www.xxxxx.wiki --enumerate t

```

> 
例如：`wpscan --url http://192.168.56.103/wordpress --enumerate t`


```
┌──(kali㉿kali)-[~/Desktop]
└─$ wpscan --url http://192.168.56.103/wordpress --enumerate t                                                                                                                                                                          1 ⨯
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.18
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://192.168.56.103/wordpress/ [192.168.56.103]
[+] Started: Thu Aug  5 11:21:49 2021

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.7 (Ubuntu)
 |  - X-Powered-By: PHP/5.5.9-1ubuntu4.22
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://192.168.56.103/wordpress/xmlrpc.php
 | Found By: Link Tag (Passive Detection)
 | Confidence: 100%
 | Confirmed By: Direct Access (Aggressive Detection), 100% confidence
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://192.168.56.103/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Registration is enabled: http://192.168.56.103/wordpress/wp-login.php?action=register
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.56.103/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.56.103/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 4.8.1 identified (Insecure, released on 2017-08-02).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.56.103/wordpress/?feed=rss2, &lt;generator&gt;https://wordpress.org/?v=4.8.1&lt;/generator&gt;
 |  - http://192.168.56.103/wordpress/?feed=comments-rss2, &lt;generator&gt;https://wordpress.org/?v=4.8.1&lt;/generator&gt;

[+] WordPress theme in use: twentyfifteen
 | Location: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/readme.txt
 | [!] The version is out of date, the latest version is 3.0
 | Style URL: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/style.css?ver=4.8.1
 | Style Name: Twenty Fifteen
 | Style URI: https://wordpress.org/themes/twentyfifteen/
 | Description: Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple, st...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.8 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/style.css?ver=4.8.1, Match: 'Version: 1.8'

[+] Enumerating Most Popular Themes (via Passive and Aggressive Methods)
 Checking Known Locations - Time: 00:00:00 &lt;============================================================================================================================================================&gt; (400 / 400) 100.00% Time: 00:00:00
[+] Checking Theme Versions (via Passive and Aggressive Methods)

[i] Theme(s) Identified:

[+] twentyfifteen
 | Location: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/readme.txt
 | [!] The version is out of date, the latest version is 3.0
 | Style URL: http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/style.css
 | Style Name: Twenty Fifteen
 | Style URI: https://wordpress.org/themes/twentyfifteen/
 | Description: Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple, st...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Known Locations (Aggressive Detection)
 |  - http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/, status: 500
 |
 | Version: 1.8 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.56.103/wordpress/wp-content/themes/twentyfifteen/style.css, Match: 'Version: 1.8'

[+] twentyseventeen
 | Location: http://192.168.56.103/wordpress/wp-content/themes/twentyseventeen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://192.168.56.103/wordpress/wp-content/themes/twentyseventeen/README.txt
 | [!] The version is out of date, the latest version is 2.8
 | Style URL: http://192.168.56.103/wordpress/wp-content/themes/twentyseventeen/style.css
 | Style Name: Twenty Seventeen
 | Style URI: https://wordpress.org/themes/twentyseventeen/
 | Description: Twenty Seventeen brings your site to life with header video and immersive featured images. With a fo...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://192.168.56.103/wordpress/wp-content/themes/twentyseventeen/, status: 500
 |
 | Version: 1.3 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.56.103/wordpress/wp-content/themes/twentyseventeen/style.css, Match: 'Version: 1.3'

[+] twentysixteen
 | Location: http://192.168.56.103/wordpress/wp-content/themes/twentysixteen/
 | Last Updated: 2021-07-22T00:00:00.000Z
 | Readme: http://192.168.56.103/wordpress/wp-content/themes/twentysixteen/readme.txt
 | [!] The version is out of date, the latest version is 2.5
 | Style URL: http://192.168.56.103/wordpress/wp-content/themes/twentysixteen/style.css
 | Style Name: Twenty Sixteen
 | Style URI: https://wordpress.org/themes/twentysixteen/
 | Description: Twenty Sixteen is a modernized take on an ever-popular WordPress layout — the horizontal masthead ...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://192.168.56.103/wordpress/wp-content/themes/twentysixteen/, status: 500
 |
 | Version: 1.3 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.56.103/wordpress/wp-content/themes/twentysixteen/style.css, Match: 'Version: 1.3'

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Thu Aug  5 11:21:50 2021
[+] Requests Done: 411
[+] Cached Requests: 46
[+] Data Sent: 116.627 KB
[+] Data Received: 206.266 KB
[+] Memory used: 167.32 MB
[+] Elapsed time: 00:00:01               

```

> 
使用下列命令扫描主题中存在的漏洞：


```
wpscan --url https://www.xxxxxx.wiki --enumerate vt

```

## WPScan 更新数据漏洞库

```
wpscan --update

```

## WPScan 暴力破解得到密码

> 
在暴力破解之前，需要提供一个字典文件


```
wpscan --url  https://www.xxxxx.wiki/  -e  u --wordlist 字典文件路径

```

## WPScan TimThumbs文件漏洞扫描

```
wpscan -u https://www.xxxxxx.wiki/ -enumerate tt

```

## WordPress 防护措施

> 
关于密码爆出防护措施



> 
如何防范扫描插件、主题、TimThumb文件


