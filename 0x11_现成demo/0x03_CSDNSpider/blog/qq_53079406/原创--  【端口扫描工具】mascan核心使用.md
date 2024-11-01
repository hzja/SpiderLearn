# 原创
：  【端口扫描工具】mascan核心使用

# 【端口扫描工具】mascan核心使用

**目录**

[ 端口扫描masscan：](#%C2%A0%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8Fmasscan%EF%BC%9A)

[1.1、基础：](#1.1%E3%80%81%E5%9F%BA%E7%A1%80%EF%BC%9A)

[1.2、单端口扫描：](#1.2%E3%80%81%E5%8D%95%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F%EF%BC%9A)

[1.3、多端口扫描](#1.3%E3%80%81%E5%A4%9A%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F)

[1.4、扫描一系列端口](#1.4%E3%80%81%E6%89%AB%E6%8F%8F%E4%B8%80%E7%B3%BB%E5%88%97%E7%AB%AF%E5%8F%A3)

[1.5、快速扫描](#1.5%E3%80%81%E5%BF%AB%E9%80%9F%E6%89%AB%E6%8F%8F)

[1.6、排除目标](#1.6%E3%80%81%E6%8E%92%E9%99%A4%E7%9B%AE%E6%A0%87)

[1.7、保存结果](#1.7%E3%80%81%E4%BF%9D%E5%AD%98%E7%BB%93%E6%9E%9C)

[1.8、其他命令：](#1.8%E3%80%81%E5%85%B6%E4%BB%96%E5%91%BD%E4%BB%A4%EF%BC%9A)

---


##  端口扫描masscan：

> 
<h3>1.1、基础：</h3>
A类子网掩码255.0.0.0开始
B类子网掩码255.255.0.0开始
B类子网掩码255.255.255.0开始
11.11.0.0(拿的一个美国ip做测试，哈哈哈)


> 
<h3>1.2、单端口扫描：</h3>
扫描80端口的B类子网
**sudo masscan 11.11.0.0/16 -p80**




> 
<h3>1.3、多端口扫描</h3>
扫描80或8888端口的B类子网
**sudo masscan 11.11.0.0/16 -p80,8888**




> 
<h3>1.4、扫描一系列端口</h3>
扫描10到12端口的B类子网
**sudo masscan 11.11.0.0/16 -p10-12**



> 
<h3>1.5、快速扫描</h3>
设置每秒扫描的数据包个数（默认100/s）
--top-ports &lt;number&gt; 扫描&lt;number&gt;个可能开发的端口
--rate &lt;number&gt; 每秒扫描number个数据包
**sudo masscan 11.11.0.0/16 --top-ports 2 --rate 300**




> 
<h3>1.6、排除目标</h3>
--exclude &lt;ip / range&gt;：将IP地址或范围列入黑名单，以防止其被扫描
--excludefile &lt;文件名&gt;：在同一tar中读取排除范围列表得到上面描述的格式
--adapter-ip 指定发包的ip地址
--adapter-port 指定发包源端口
--adapter-mac 指定发包的源MAC地址
--router-mac 指定网关MAC地址
--includefile,-iL 读取一个范围列表进行扫描
--wait 指定发包后的等待时间
**sudo masscan 11.11.0.0/16 --top-ports 100 --excludefile index.txt **


> 
<h3>1.7、保存结果</h3>
**sudo masscan 11.11.0.0/16 --top-ports 5 --rate 300  &gt;  results.txt**

`  ``-oX &lt;文件名&gt;：输出&lt;文件名&gt;以XML格式。`
`  ``-oG &lt;文件名&gt;：输出&lt;文件名&gt;以grepable格式。`
`  ``-oJ &lt;文件名&gt;：输出&lt;文件名&gt;以JSON格式。`


### 1.8、其他命令：

```
&lt;ip / range&gt;：命令行上前缀没有“-”的任何内容是IP地址或范围。
              有三种有效格式。
              第一个，单个IPv4地址，例如“ 11.11.0.0”。
              第二个，范围是“ 10.0.0.1-10.0.0.100”。
              第三个是CIDR地址，eg“ 0.0.0.0/0”。
              指定为多个选项，以空格分隔，逗号分割作为单个选项，例如10.0.0.0/8,192.168.0.1

--range &lt;ip / range&gt;：与上述目标范围规格相同，不同之处在于一个命名参数而不是一个未命名参数。

-p &lt;端口，--ports &lt;端口&gt;：指定要扫描的端口。
                         可以指定单个端口，例如-p80。
                         可以指定端口范围，例如-p10-15。
                         可以指定端口/范围的列表，例如-p80,20-25。
                         UDP端口也可以指定，例如--ports U：161，U：1024-1100。

--banners：指定应抓取横幅，例HTTP服务器版本部分，HTML标题字段等。

--rate &lt;packets-per-second&gt;：指定所需的传输速率包的数量

-c &lt;文件名&gt;，-conf &lt;文件名&gt;：读取配置文件。

--resume &lt;文件名&gt;：与--conf相同，只是一些选项是自动的临时设置，例如--append-output。配置文件 
格式
            
--echo：不运行，而是将当前配置转储到文件中。可以将文件与-c选项一起使用。此输出的格式为在“配置文件”下分析。

-e &lt;ifname&gt;，-adapter &lt;ifname&gt;：使用命名的原始网络接口，例如 “ eth0”或“ dna1”。如果未指定，则找到的第一个网络接口带有将使用默认网关。

--adapter-ip &lt;IP地址&gt;：使用此IP地址发送数据包。如果没有指定确定，则将使用绑定到网络接口的第一个IP地址。可以指定一个范围，而不是一个IP地址。注意：的大小范围必须是2的偶数幂，例如1、2、4、8、16、1024等。

--adapter-port &lt;端口&gt;：使用此端口号作为源发送数据包。如果如果未指定，则会在40000到60000范围内选择一个随机端口。此端口应由主机防火墙（如iptables）过滤，以防止主机网络堆栈不会干扰到达的数据包。代替单端口，可以指定一个范围，例如40000-40003。注意：的大小范围必须是2的偶数幂，例如上面的示例总共4个地址。

--adapter-mac &lt;mac-address&gt;：使用此作为源MAC ad-发送数据包。如果未指定，则绑定到网络的第一个MAC地址位于将使用接口。

--router-mac &lt;mac地址&gt;：将数据包作为destina-发送到此MAC地址tion。如果未指定，则为网络接口的网关地址将被ARPed。

--ping：指示扫描应包括ICMP回显请求。这可能包含在TCP和UDP扫描中。

--exclude &lt;ip / range&gt;：将IP地址或范围列入黑名单，以防止其被扫描。这会覆盖任何目标规范，从而保证该地址/范围不会被扫描。与普通格式相同目标规范。

--excludefile &lt;文件名&gt;：在同一tar中读取排除范围列表得到上面描述的格式。这些范围会覆盖所有目标，从而防止他们被扫描。

--append-output：使输出追加到文件，而不是覆盖文件。

--iflist：列出可用的网络接口，然后退出。

--retries：每隔1秒发送一次的重试次数。注意由于此扫描程序是无状态的，因此无论是否回复，都会发送重试已经收到。

--nmap：打印帮助，而不是这些选项的nmap兼容性替代品。

--pcap-payloads：从libpcap文件中读取包含数据包的数据包，并提取UDP有效负载，并将这些有效负载与目标相关联端口。这些有效负载将在通过以下方式发送UDP数据包时使用匹配目标端口。每个端口仅记住一个有效负载。 Sim‐与--nmap-payloads类似。

--nmap-payloads &lt;文件名&gt;：以与nmap相同的格式读取文件文件nmap-payloads。它包含UDP有效负载，以便我们可以发送有用的UDP包而不是空包。与--pcap-payloads类似。

--http-user-agent &lt;user-agent&gt;：将现有的user-agent字段替换为执行HTTP请求时的指示值。

--open-only：仅报告打开的端口，不报告关闭的端口。

--pcap &lt;文件名&gt;：将收到的数据包（但不传输的数据包）保存到libpcap格式的文件。

--packet-trace：打印发送和接收的那些数据包的摘要。这是在低速率下很有用，例如每秒几个数据包，但会淹没终端机率很高。

--pfring：强制使用PF_RING驱动程序。

--resume-index：扫描中的暂停点。

--resume-count：退出前要发送的最大探测数。这是与--resume-index一起使用可将扫描切碎并分成多个实例，尽管--shards选项可能更好。

--shards &lt;x&gt; / &lt;y&gt;：在实例之间拆分扫描。 x是此扫描的ID，而y是实例总数。例如，--shards 1/2告诉实例发送每个其他数据包，并从索引0开始。--shards 2/2发送其他所有数据包，但从索引1开始，因此它与第一个示例不重叠。

--rotate &lt;时间&gt;：旋转输出文件，将其重命名为当前时间图章，将其移动到单独的目录中。时间以数量指定秒，例如“ 3600”一个小时。或者，可以指定时间单位，例如 “每小时”，“或6小时”或“ 10分钟”。时间在均匀边界上对齐，因此如果指定为“ daily”，则文件将每天在午夜旋转。

--rotate-offset &lt;时间&gt;：时间的偏移量。这是为了适应时间区域。

--rotate-dir &lt;目录&gt;：旋转文件时，这指定哪个目录尝试将文件移动到。一个有用的目录是/ var / log / masscan。

--seed &lt;integer&gt;：整数作为种子随机数生成器的种子。用一个不同的种子将导致数据包以不同的随机顺序发送。在-可以指定字符串时间，而不是整数，使用本地时间戳记，自动生成不同的随机扫描顺序。如果未指定种子，则时间为默认值。

--regress：运行回归测试，成功返回“ 0”，失败返回“ 1”。

--ttl &lt;num&gt;：指定传出数据包的TTL，默认为255。

--wait &lt;seconds&gt;：指定发送完成后的秒数在退出程序之前等待接收数据包。默认值为10秒onds。可以将字符串永久指定为永不终止。

--offline：实际不传输数据包。这对低费率很有用和--packet-trace以查看可能传输了哪些数据包。要么，它与--rate 100000000一起使用以比较快速传输的基准会工作（假设零开销驱动程序）。 PF_RING慢20％比离线模式下的基准测试结果要高。

-sL：不执行扫描，而是创建一个随机地址列表。这对于导入其他工具很有用。选项--shard，--resume-index和--resume-count对于此功能很有用。

--interactive：在控制台上实时显示结果。没有效果如果与--output-format或--output-filename一起使用。

--output-format &lt;fmt&gt;：指示输出文件的格式，可以是xml，二进制，grepable，列表或JSON。选项--output-filename必须指定。

--output-filename &lt;filename&gt;：将结果保存到的文件。如果parameter --output-format未指定，则默认为xml用过的。

-oB &lt;文件名&gt;：将输出格式设置为二进制并将输出保存在给定的文件名。这等效于使用--output-format和--out-put-filename参数。然后可以使用--readscan选项读取二进制文件。二进制文件的大小比其XML等效项小，但是需要一个单独的步骤才能转换回XML或其他可读格式。

-oX &lt;文件名&gt;：将输出格式设置为XML并将输出保存在给定的文件名。这等效于使用--output-format xml和--output-filename参数。

-oG &lt;文件名&gt;：将输出格式设置为grepable并将输出保存在给定的文件名。这等效于使用--output-format grepable和--output-filename参数。

-oJ &lt;文件名&gt;：将输出格式设置为JSON并将输出保存在给定的文件名。这等效于使用--output-format json和--output-filename参数。

-oL &lt;文件名&gt;：将输出格式设置为简单列表格式并保存以给定的文件名输出。这等效于使用--output-formatlist和--output-filename参数。

--readscan &lt;binary-files&gt;：从-oB选项中读取-oB选项创建的文件扫描，然后根据其他格式以其他格式之一输出它们需求线参数。换句话说，它可以采用输出并将其转换为XML或JSON格式。
```
