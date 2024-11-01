# 原创
：  Ubuntu 20.0.4 安装 Docker

# Ubuntu 20.0.4 安装 Docker

#### Ubuntu 20.0.4 安装 Docker

## 卸载旧版本 Docker

```
sudo apt-get remove docker docker-engine docker.io containerd runc

```

## 配置软件源

### 更新软件源并安装依赖包

```
sudo apt-get update
sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common

```

### 添加 Docker 官方软件包密钥

```
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

```

> 
验证密钥是否安装成功


```
toor@toor:~/Desktop$ sudo apt-key fingerprint 0EBFCD88
pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid           [ unknown] Docker Release (CE deb) &lt;docker@docker.com&gt;
sub   rsa4096 2017-02-22 [S]

```

### 添加软件源

> 
查询当前系统所基于的 Debian 版本，得到以下回显


```
toor@toor:~/Desktop$ cat /proc/version
Linux version 5.8.0-63-generic (buildd@lgw01-amd64-035) (gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0, GNU ld (GNU Binutils for Ubuntu) 2.34) #71~20.04.1-Ubuntu SMP Thu Jul 15 17:46:08 UTC 2021

```

> 
通过查询得知 Debian 9 对应的代号为 stretch ，之后执行以下命令写入 docker 软件源


```
echo 'deb https://download.docker.com/linux/debian stretch stable' | sudo tee -a /etc/apt/sources.list.d/docker.list 

```

> 
正常写入回显


```
toor@toor:~/Desktop$ echo 'deb https://download.docker.com/linux/debian stretch stable' | sudo tee -a /etc/apt/sources.list.d/docker.list 
[sudo] password for toor: 
deb https://download.docker.com/linux/debian stretch stable

```

## 安装 Docker

```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

```

> 
安装之后可以配置一下 Docker 镜像加速


```
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json &lt;&lt;-'EOF'
{
  "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

```

> 
配置好后执行以下命令进行测试


```
sudo docker run hello-world

```

> 
得到以下回显显示为正常


```
toor@toor:~/Desktop$ sudo docker run hello-world
[sudo] password for toor: 
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b8dfde127a29: Pull complete 
Digest: sha256:df5f5184104426b65967e016ff2ac0bfcd44ad7899ca3bbcf8e44e4461491a9e
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

## 卸载 Docker

### 卸载软件

```
sudo apt-get purge docker-ce docker-ce-cli containerd.io 

```

### 删除镜像、容器、自定义配置等文件

```
sudo rm -rf /var/lib/docker 

```

## 安装 Docker-Compose

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose -v

```

> 
回显版本号则安装成功


## 卸载 Docker-Compose

```
sudo rm /usr/local/bin/docker-compose 

```
