# 原创
：  Ubuntu20.04挂起再打开时无法上网

# Ubuntu20.04挂起再打开时无法上网

```
(base) root@ubuntu:~/Desktop# ping www.baidu.com
ping: www.baidu.com: Temporary failure in name resolution
(base) root@ubuntu:~/Desktop# dhclient
(base) root@ubuntu:~/Desktop# ping www.baidu.com
PING www.a.shifen.com (39.156.66.14) 56(84) bytes of data.
64 bytes from 39.156.66.14 (39.156.66.14): icmp_seq=1 ttl=128 time=39.4 ms
64 bytes from 39.156.66.14 (39.156.66.14): icmp_seq=2 ttl=128 time=38.6 ms


```
