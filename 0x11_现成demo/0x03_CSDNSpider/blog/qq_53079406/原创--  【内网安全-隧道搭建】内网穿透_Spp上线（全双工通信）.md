# 原创
：  【内网安全-隧道搭建】内网穿透_Spp上线（全双工通信）

# 【内网安全-隧道搭建】内网穿透_Spp上线（全双工通信）

**目录**

[Spp（特殊协议上线）](#Spp%EF%BC%88%E7%89%B9%E6%AE%8A%E5%8D%8F%E8%AE%AE%E4%B8%8A%E7%BA%BF%EF%BC%89)

[1、简述：](#1%E3%80%81%E7%AE%80%E8%BF%B0%EF%BC%9A)

[2、用法：](#2%E3%80%81%E7%94%A8%E6%B3%95%EF%BC%9A)

[1、准备](#1%E3%80%81%E5%87%86%E5%A4%87)

[2、服务器](#2%E3%80%81%E6%9C%8D%E5%8A%A1%E5%99%A8)

[3、客户机](#3%E3%80%81%E5%AE%A2%E6%88%B7%E6%9C%BA)

[4、cs、msf](#4%E3%80%81cs%E3%80%81msf)

---


## Spp（特殊协议上线）

> 
<h3>1、简述：</h3>
1）支持的协议：tcp、udp、rudp（可靠udp）、ricmp（可靠icmp）、rhttp（可靠http）、kcp、quic
<hr/>
2）支持的类型：双向代理、socks5正向代理、socks5反向代理
<hr/>
3）外部代理协议和内部转发协议可以自由组合
<hr/>
4）支持Shadowsocks插件，spp-shadowsocks-plugin，spp-shadowsocks-plugin-android
[GitHub - esrrhs/spp-shadowsocks-plugin: spp shadowsocks pluginspp shadowsocks plugin. Contribute to esrrhs/spp-shadowsocks-plugin development by creating an account on GitHub.<img alt="" src="https://github.com/fluidicon.png"/>https://github.com/esrrhs/spp-shadowsocks-plugin](https://github.com/esrrhs/spp-shadowsocks-plugin)
<hr/>
5）工具：[Releases · esrrhs/spp (github.com)<img alt="icon-default.png?t=N0U7" src="https://csdnimg.cn/release/blog_editor_html/release2.2.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N0U7"/>https://github.com/esrrhs/spp/releases/](https://github.com/esrrhs/spp/releases/)
<hr/>
6）原理图：

（图片来自GitHub:[Releases · esrrhs/spp (github.com)](https://github.com/esrrhs/spp/releases/)） 
<hr/>
7）个人见解：
使用简单：服务器、客户机各一条命令，就可建立连接
全双工通信：工具没有服务端、客户端之分，直接在命令中指定服务端、客户端


---


---


---


---


---


### 2、用法：

> 
<h4>1、准备</h4>
因为是全双工通信（工具就没有客户端，服务端之分，找服务器和客户机对应的版本即可）




> 
<h4>2、服务器</h4>
1）方法一：启动服务器：
假设服务器IP为 www.server.com，监听端口8888
指定类型为server（服务端），协议为tcp协议，监听端口8888
<pre>`# ./spp -type server -proto tcp -listen :8888`</pre>
<hr/>
2）方法二：自由组合方法：
还可以与其他类型的端口和协议同时侦听
-prto后分别接了3个协议、端口，同时进行监听
<pre>`# ./spp -type server -proto tcp -listen :8888 -proto rudp -listen :9999 -proto ricmp -listen 0.0.0.0`</pre>
<hr/>
3）方法三：其他方法：也可以使用 Docker
（这个就复杂了一点）
<pre>`# docker run --name my-server -d --restart=always --network host esrrhs/spp ./spp -proto tcp -listen :8888`</pre>



---


> 
<h4>3、客户机</h4>
1）方法一：启动TCP转发代理
（正向）将 www.server.com 的8080端口映射到本地8080，使访问本地8080等同于访问 www.server.com 8080
<pre>`# ./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto tcp`</pre>
<hr/>
2）方法二：启动TCP逆向代理
（反向）将本地8080映射到 www.server.com 的8080端口，访问 www.server.com 8080相当于访问本地8080
<pre>`# ./spp -name "test" -type reverse_proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto tcp`</pre>
<hr/>
3）方法三：启动TCP正极Socks5代理
（正向）在本地8080端口开启socks5协议，通过服务器访问服务器中的网络
<pre>`# ./spp -name "test" -type socks5_client -server www.server.com:8888 -fromaddr :8080 -proxyproto tcp`</pre>
<hr/>
4）方法四：启动tcp反向socks5代理
（反向）在www.server.com的8080端口开启socks5协议，通过客户端访问客户端中的网络
<pre>`# ./spp -name "test" -type reverse_socks5_client -server www.server.com:8888 -fromaddr :8080 -proxyproto tcp`</pre>
<hr/>
5）其他代理协议：
只需要修改客户端的proxyProto参数
<pre><code># 代理 UDP协议
./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto udp

# 代理 rudp协议
./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8081 -toaddr :8081 -proxyproto rudp

# 代理 ricmp协议
./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8082 -toaddr :8082 -proxyproto ricmp

# 同时使用UDP、rudp、ricmp协议
./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto udp -fromaddr :8081 -toaddr :8081 -proxyproto rudp -fromaddr :8082 -toaddr :8082 -proxyproto ricmp
</code></pre>
<hr/>
6）客户端和服务器之间的内部通信
也可以修改为其他协议，自动转换外部协议和内部协议
<pre><code># 代理tcp协议，内部用rudp协议转发
./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto tcp -proto rudp


# 代理tcp协议，内部用ricmp协议转发
./spp -name "test" -type proxy_client -server www.server.com -fromaddr :8080 -toaddr :8080 -proxyproto tcp -proto ricmp


# 代理udp协议，内部用tcp协议转发
./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto udp -proto tcp


# 代理udp协议，内部用kcp协议转发
./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto udp -proto kcp


# 代理tcp协议，内部用quic协议转发
./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto tcp -proto quic


# 代理tcp协议，内部用rhttp协议转发
./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto tcp -proto rhttp</code></pre>
<hr/>
7）其他方法：docker
<pre>`# docker run --name my-client -d --restart=always --network host esrrhs/spp ./spp -name "test" -type proxy_client -server www.server.com:8888 -fromaddr :8080 -toaddr :8080 -proxyproto tcp`</pre>



---


---


---


> 
<h4>4、cs、msf</h4>
生成监听后门监听


---


使用方法来源开发者：

[esrrhs/spp：一个简单而强大的代理 (github.com)<img alt="icon-default.png?t=N0U7" src="https://csdnimg.cn/release/blog_editor_html/release2.2.2/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=N0U7"/>https://github.com/esrrhs/spp](https://github.com/esrrhs/spp)
