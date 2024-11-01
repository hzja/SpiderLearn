# 原创
：  Linux虚拟机网卡配置（创建静态ip）

# Linux虚拟机网卡配置（创建静态ip）

```
ip addr
```

```
dhclient
```

```
ip addr
```

```
cp ifcfg-ens33 ifcfg-ens33bf
```

```
vi ifcfg-ens33
```

（注意：配置过程全程使用**英文**输入法）

其中：

```
:wq
```

```
systemctl restart network
```
