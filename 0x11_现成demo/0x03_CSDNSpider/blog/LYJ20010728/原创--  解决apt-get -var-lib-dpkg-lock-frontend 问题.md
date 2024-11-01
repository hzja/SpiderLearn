# 原创
：  解决apt-get /var/lib/dpkg/lock-frontend 问题

# 解决apt-get /var/lib/dpkg/lock-frontend 问题

#### 解决apt-get /var/lib/dpkg/lock-frontend 问题

> 
当Ubuntu进行apt-get操作产生如下报错时


```
E: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 4127 (aptd)
N: Be aware that removing the lock file is not a solution and may break your system.
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), is another process using it?

```

> 
采取以下命令来解决该问题


```
sudo rm /var/lib/dpkg/lock-frontend

```
