# 原创
：  【kali-信息收集】枚举——DNS枚举：DNSenum、fierce

# 【kali-信息收集】枚举——DNS枚举：DNSenum、fierce

**目录**

[一、DNS 枚举](#%E4%B8%80%E3%80%81DNS%20%E6%9E%9A%E4%B8%BE)

[二、DNS枚举工具](#%E4%BA%8C%E3%80%81DNS%E6%9E%9A%E4%B8%BE%E5%B7%A5%E5%85%B7)

[2.1、DNSenum](#2.1%E3%80%81DNSenum)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[查看命令：](#%E6%9F%A5%E7%9C%8B%E5%91%BD%E4%BB%A4%EF%BC%9A)

[测试：](#%E6%B5%8B%E8%AF%95%EF%BC%9A)

[2.2、fierce](#2.2%E3%80%81fierce)

[简介：](#%E7%AE%80%E4%BB%8B%EF%BC%9A)

[查看命令：](#%E6%9F%A5%E7%9C%8B%E5%91%BD%E4%BB%A4%EF%BC%9A)

[测试：](#%E6%B5%8B%E8%AF%95%EF%BC%9A)

---


## 一、DNS 枚举

> 
帮助用户收集目标组织的关键信息， 如用户名 、 计算机名和IP地址等


---


---


## 二、DNS枚举工具

> 
<h3>2.1、DNSenum</h3>
<h4>简介：</h4>
是一款非常强人的域名信息收集工具。它能够通过谷歌或者字典文件猜测可 能存在的域名， 并对一个网段进行反向查询。 它不仅可以查询网站的主机地址信息、 域名 服务器和邮件交换记录， 还可以在域名服务器上执行axfr请求， 然后通过谷歌脚木得到扩展域名信息 ， 提取子域名并查询， 最后计算C类地址并执行wbois查询 ， 执行反向查询 ，把地址段写入文件。本小节将介绍使用DNSenum工具检查DNS枚举。
<hr/>
<h4>查看命令：</h4>
在终端执行命令：
dnsenum -h
直接搜应用：

<pre><code>Usage: dnsenum [Options] &lt;domain&gt;
[Options]:
Note: If no -f tag supplied will default to /usr/share/dnsenum/dns.txt or
the dns.txt file in the same directory as dnsenum.pl
GENERAL OPTIONS:
  --dnsserver   &lt;server&gt;
                        Use this DNS server for A, NS and MX queries.
  --enum                Shortcut option equivalent to --threads 5 -s 15 -w.
  -h, --help            Print this help message.
  --noreverse           Skip the reverse lookup operations.
  --nocolor             Disable ANSIColor output.
  --private             Show and save private ips at the end of the file domain_ips.txt.
  --subfile &lt;file&gt;      Write all valid subdomains to this file.
  -t, --timeout &lt;value&gt; The tcp and udp timeout values in seconds (default: 10s).
  --threads &lt;value&gt;     The number of threads that will perform different queries.
  -v, --verbose         Be verbose: show all the progress and all the error messages.
GOOGLE SCRAPING OPTIONS:
  -p, --pages &lt;value&gt;   The number of google search pages to process when scraping names,
                        the default is 5 pages, the -s switch must be specified.
  -s, --scrap &lt;value&gt;   The maximum number of subdomains that will be scraped from Google (default 15).
BRUTE FORCE OPTIONS:
  -f, --file &lt;file&gt;     Read subdomains from this file to perform brute force. (Takes priority over default dns.txt)
  -u, --update  &lt;a|g|r|z&gt;
                        Update the file specified with the -f switch with valid subdomains.
        a (all)         Update using all results.
        g               Update using only google scraping results.
        r               Update using only reverse lookup results.
        z               Update using only zonetransfer results.
  -r, --recursion       Recursion on subdomains, brute force all discovered subdomains that have an NS record.
WHOIS NETRANGE OPTIONS:
  -d, --delay &lt;value&gt;   The maximum value of seconds to wait between whois queries, the value is defined randomly, default: 3s.
  -w, --whois           Perform the whois queries on c class network ranges.
                         **Warning**: this can generate very large netranges and it will take lot of time to perform reverse lookups.
REVERSE LOOKUP OPTIONS:
  -e, --exclude &lt;regexp&gt;
                        Exclude PTR records that match the regexp expression from reverse lookup results, useful on invalid hostnames.
OUTPUT OPTIONS:
  -o --output &lt;file&gt;    Output in XML format. Can be imported in MagicTree (www.gremwell.com)
</code></pre>
命令：dnsenum -enum ip
附加选项
--threads [number]： 设胃用户同时运行多个进程数。<br/> -r: 允许用户启用递归查询。<br/> -d: 允许用户设置WHOIS请求之间时间延迟数（单钓为秒） 。
-0: 允许用户指定输出位置。<br/> -w： 允许用户启用WHOIS请求。
<hr/>
<h4>测试：</h4>
以百度为例（baidu.com）

输入命令dnsenum -enum baidu.com 
 <img alt="" height="734" src="https://img-blog.csdnimg.cn/97f5f620fc004affb7045e5bbef2e624.png" width="1121"/>

输出的信息显示了DNS服务的详细信息。
包括主机地址、域名服务地址和邮件 服务地址。 （运气好，可以看到区域传输）



#### 查看命令：

---


 

> 
<h3>2.2、fierce</h3>
<h4>简介：</h4>
fierce主要是对子域名进行扫描和收共信息的
<hr/>
<h4>查看命令：</h4>
在终端执行命令：
fierce -h
直接搜应用：



<pre><code>usage: fierce [-h] [--domain DOMAIN] [--connect] [--wide] [--traverse TRAVERSE] [--search SEARCH [SEARCH ...]] [--range RANGE]
              [--delay DELAY] [--subdomains SUBDOMAINS [SUBDOMAINS ...] | --subdomain-file SUBDOMAIN_FILE]
              [--dns-servers DNS_SERVERS [DNS_SERVERS ...] | --dns-file DNS_FILE] [--tcp]

        A DNS reconnaissance tool for locating non-contiguous IP space.
        

optional arguments:
  -h, --help            show this help message and exit
  --domain DOMAIN       domain name to test
  --connect             attempt HTTP connection to non-RFC 1918 hosts
  --wide                scan entire class c of discovered records
  --traverse TRAVERSE   scan IPs near discovered records, this won't enter adjacent class c's
  --search SEARCH [SEARCH ...]
                        filter on these domains when expanding lookup
  --range RANGE         scan an internal IP range, use cidr notation
  --delay DELAY         time to wait between lookups
  --subdomains SUBDOMAINS [SUBDOMAINS ...]
                        use these subdomains
  --subdomain-file SUBDOMAIN_FILE
                        use subdomains specified in this file (one per line)
  --dns-servers DNS_SERVERS [DNS_SERVERS ...]
                        use these dns servers for reverse lookups
  --dns-file DNS_FILE   use dns servers specified in this file for reverse lookups (one per line)
  --tcp                 use TCP instead of UDP
</code></pre>
<hr/>
<h4>测试：</h4>
使用fierce工具获取一个目标主机上子域名
fierce --domain baidu.com

……


#### 查看命令：

---

