# 原创
：  FTP服务的登录方式

# FTP服务的登录方式

#### FTP服务的登录方式

## 匿名用户登录

> 



> 



```
useradd anontest -s /sbin/nologin -d /data/ftp/anontest
chmod 755 /data/ftp/anontest

```

> 



```
# 打开匿名用户模式
anonymous_enable=YES
## 打开本地用户登录
local_enable=YES
## 打开全局写权限
write_enable=YES
## 系统用户新增或上传档案时的umask值
#local_umask=022
# 若是启动这项功能，则使用匿名登入时，不会询问密码。默认值为NO
no_anon_password=YES
# 定义匿名登入的使用者名称。默认值为ftp
ftp_username=anontest
# 使用匿名登入时，所登入的目录。默认值为/var/ftp。注意ftp目录不能是777的权限属性，即匿名用户的家目录不能有777的权限
#anon_root=/data/ftp/anontest
anon_root=/data/ftp
# 如果设为YES，则允许匿名登入者有上传文件（非目录）的权限，只有在write_enable=YES时，此项才有效。当然，匿名用户必须要有对上层目录的写入权。默认值为NO
anon_upload_enable=YES
# 开启匿名用户创建目录的权限
anon_mkdir_write_enable=YES
# 开启匿名用户可以删除目录和文件
# （如果anon_upload_enable=NO，则匿名用户不能上传文件，但可以删除或者重命名已经存在的文件；如果anon_mkdir_write_enable=NO，则匿名用户不能上传或者新建文件夹，但可以删除或者重命名已经存在的文件夹。）
anon_other_write_enable=YES
# 开启匿名用户下载权限
anon_world_readable_only=YES
# 设置匿名用户可以下载自己上传的文件：新建的目录 权限是755，文件的权限是 644
# 设置是否改变匿名用户上传文件（非目录）的属主。默认值为NO
chown_uploads=NO
# 设置匿名用户上传文件（非目录）的属主名。建议不要设置为root
chown_username=anontest
# 设置匿名登入者新增或上传档案时的umask值。
anon_umask=022
# 是否显示目录消息
dirmessage_enable=YES
# 是否让系统自动维护上传和下载的日志文件
xferlog_enable=YES
# 是否启用端口20进行FTP数据连接请求
connect_from_port_20=YES
# 设定系统维护记录FTP服务器上传和下载情况的日志文件
xferlog_file=/var/log/vsftpd.log
# 开启日志功能（记录删除、下载、删除所有动作）
log_ftp_protocol=yes
# 是否以标准xferlog的格式书写传输日志文件
xferlog_std_format=no
xferlog_enable=yes
#standalone模式 (must config)
# 设置vsftpd服务器是否以standalone模式运行。以standalone模式运行是一种较好的方式，此时listen必须设置为YES，此为默认值。建议不要更改，有很多与服务器运行相关的配置命令，需要在此模式下才有效。若设置为NO，则vsftpd不是以独立的服务运行，要受到xinetd服务的管控，功能上会受到限制
# 是否允许监听。如果设置为YES，则vsftpd将以独立模式运行，由vsftpd自己监听和处理IPv4端口的连接请求
listen=YES
listen_port=666
#listen_ipv6=YES
# 被动模式传输
pasv_enable=YES
pasv_promiscuous=YES
pasv_min_port=12351
pasv_max_port=12551
# 列出与vsftpd相关的pam文件
pam_service_name=vsftpd
# 是否启用禁止登录用户名单
userlist_enable=YES
# 是否支持tcp_wrappers
tcp_wrappers=NO
# 设置vsftpd允许的最大连接数，默认值为0，表示不受限制。若设置为100时，则同时允许有100个连接，超出的将被拒绝。只有在standalone模式运行才有效。
max_clients=0
# 设置每个IP允许与FTP服务器同时建立连接的数目。默认值为0，表示不受限制。只有在standalone模式运行才有效
max_per_ip=0
# 设置FTP服务器在指定的IP地址上侦听用户的FTP请求。若不设置，则对服务器绑定的所有IP地址进行侦听。只有在standalone模式运行才有效
#listen_address=IP地址

```

## 系统用户登录

> 



```
#允许匿名访问
anonymous_enable=NO
#允许本地用户登录
local_enable=YES
#设置本地用户登录后所在的目录。默认配置文件中没有设置该项，此时用户登录FTP服务器后，所在的目录为该用户的主目录
local_root=/data/ftp
#是否允许登陆用户有写权限
write_enable=YES
#设置本地用户的文件掩码022
local_umask=022

#是否允许匿名用户上传。
#anon_upload_enable=YES
#是否允许匿名用户建立目录。
#anon_mkdir_write_enable=YES

#是否显示目录消息
dirmessage_enable=YES
#是否让系统自动维护上传和下载的日志文件
xferlog_enable=YES
#是否启用端口20进行FTP数据连接请求
connect_from_port_20=NO

#设定系统维护记录FTP服务器上传和下载情况的日志文件
xferlog_file=/var/log/vsftpd.log

#开启日志功能（记录删除、下载、删除所有动作）
log_ftp_protocol=yes
#是否以标准xferlog的格式书写传输日志文件
xferlog_std_format=no
xferlog_enable=yes

#禁止域名反向解析，解决登录慢的问题
reverse_lookup_enable=NO
#是否允许监听。如果设置为YES，则vsftpd将以独立模式运行，由vsftpd自己监听和处理IPv4端口的连接请求
listen=YES
#修改默认端口21，提高安全性
listen_port=666
 
#被动模式传送
pasv_enable=YES
pasv_promiscuous=YES
#设定在PASV模式下，建立数据传输所可以使用port范围的下界和上界，0 表示任意，设置50000-60000，将有助于安全性的提高
pasv_min_port=12351
pasv_max_port=12551
 
#虚拟用户使用PAM认证方式；设置PAM使用的名称，默认值为/etc/pam.d/vsftpd
pam_service_name=vsftpd
 
#(用户的访问控制可以通过user_list和ftpusers(ftpuser不受任何配制项的影响！它总是有效，它是一个黑名单)文件来实现)
#控制用户访问FTP的文件，里面写着用户名称。一个用户名称一行
userlist_file=/etc/vsftpd/user_list

#userlist_enable和userlist_deny两个选项联合起来针对的是：本地全体用户（除去ftpusers中的用户）和出现在user_list文件中的用户以及不在在user_list文件中的用户这三类用户集合进行的设置。
#当且仅当userlist_enable=YES时：userlist_deny项的配置才有效，user_list文件才会被使用；当其为NO时，无论userlist_deny项为何值都是无效的，本地全体用户（除去ftpusers中的用户）都可以登入FTP
#当userlist_enable=YES时，userlist_deny=YES时：user_list是一个黑名单，即：所有出现在名单中的用户都会被拒绝登入；
#当userlist_enable=YES时，userlist_deny=NO时：user_list是一个白名单，即：只有出现在名单中的用户才会被准许登入(user_list之外的用户都被拒绝登入)；另外需要特别提醒的是：使用白名单后，匿名用户将无法登入！除非显式在user_list中加入一行：anonymous
# 是否使userlist这个文件生效
userlist_enable=YES
#设置是否阻扯user_list文件中的用户登录FTP服务器
userlist_deny=YES
 
#是否使用tcp_wrappers作为主机访问控制方式。
tcp_wrappers=NO
 
#指定用户独立的配置文件存放目录
user_config_dir=/etc/vsftpd/vusers_dir

#匿名/本地用户传输速率（单位：K/S）
anon_max_rate=30000000
local_max_rate=30000000
use_localtime=YES

#是否将所有用户限制在主目录,YES为启用 NO禁用.(该项默认值是NO,即在安装vsftpd后不做配置的话，ftp用户是可以向上切换到主目录之外的)
chroot_local_user=NO

#是否启动限制用户的名单 YES为启用 NO禁用(包括注释掉也为禁用)
chroot_list_enable=YES
#是否限制在主目录下的用户名单，至于是限制名单还是排除名单，这取决于chroot_local_user的值，我们可以这样记忆： chroot_local_user总是一个全局性的设定，其为YES时，全部用户被锁定于主目录，其为NO时，全部用户不被锁定于主目录。那么我们势必需要在全局设定下能做出一些“微调”，即，我们总是需要一种“例外机制"，所以当chroot_list_enable=YES时，表示我们“需要例外”。而”例外“的含义总是有一个上下文的，即，当”全部用户被锁定于主目录“时（即chroot_local_user=YES），"例外"就是：不被锁定的用户是哪些；当"全部用户不被锁定于主目录"时（即chroot_local_user=NO），"例外"“就是：要被锁定的用户是哪些。这样解释和记忆两者之间的关系就很清晰了！
chroot_list_file=/etc/vsftpd/vsftpd.chroot_list

#从2.3.5之后，vsftpd增强了安全检查，如果用户被限定在了其主目录下，则该用户的主目录不能再具有写权限了！如果检查发现还有写权限，就会报该错误#要修复这个错误可以用命令chmod a-w 去除主目录写权限，或者你可以在vsftpd的配置文件中增加下列两项中的一项
allow_writeable_chroot=YES

#禁用反向域名解析
reverse_lookup_enable=NO
 
#每个来源IP可建立多少ftp连接
max_per_ip=0
 
##最多允许100个人同时使用FTP服务器
max_clients=100
 
##设置客户端/数据连接超时时间
idle_session_timeout=600
data_connection_timeout=120

```

> 



```
useradd local_one -s /sbin/nologin -d /data/ftp/local_one
chmod 755 /data/ftp/local_one

```

> 



```
如果使用系统用户登录，当用户数大于1时，通过默认vsftpd.conf来管理、限制用户权限的方法显然有些力不从心；因此通过配置文件参数--user_config_dir，将每个用户配置独立化可以解决上述问题

```

```
例如，指定用户独立的配置文件存放目录：user_config_dir=/etc/vsftpd/vusers_dir

mkdir -p /etc/vsftpd/vusers_dir
touch  /etc/vsftpd/vusers_dir/local_one
cat  &gt;/etc/vsftpd/vusers_dir/local_one&lt;&lt;EOF
#指定该用户的登陆目录
local_root=/data/ftp/local_one
EOF

```

> 



```
touch /etc/vsftpd/vsftpd.chroot_list

```

## 虚拟用户登录

> 



```
#允许匿名访问
anonymous_enable=NO
#允许本地用户登录
local_enable=YES
#设置本地用户登录后所在的目录。默认配置文件中没有设置该项，此时用户登录FTP服务器后，所在的目录为该用户的主目录
local_root=/data/ftp
#是否允许登陆用户有写权限
write_enable=YES
#设置本地用户的文件掩码022
local_umask=022

#是否允许匿名用户上传。
#anon_upload_enable=YES
#是否允许匿名用户建立目录。
#anon_mkdir_write_enable=YES

#是否显示目录消息
dirmessage_enable=YES
#是否让系统自动维护上传和下载的日志文件
xferlog_enable=YES
#是否启用端口20进行FTP数据连接请求
connect_from_port_20=NO

#设定系统维护记录FTP服务器上传和下载情况的日志文件
xferlog_file=/var/log/vsftpd.log

#开启日志功能（记录删除、下载、删除所有动作）
log_ftp_protocol=yes
#是否以标准xferlog的格式书写传输日志文件
xferlog_std_format=no
xferlog_enable=yes

#禁止域名反向解析，解决登录慢的问题
reverse_lookup_enable=NO
#是否允许监听。如果设置为YES，则vsftpd将以独立模式运行，由vsftpd自己监听和处理IPv4端口的连接请求
listen=YES
#修改默认端口21，提高安全性
listen_port=666
 
#被动模式传送
pasv_enable=YES
pasv_promiscuous=YES
#设定在PASV模式下，建立数据传输所可以使用port范围的下界和上界，0 表示任意，设置50000-60000，将有助于安全性的提高
pasv_min_port=12351
pasv_max_port=12551
 
#虚拟用户使用PAM认证方式；设置PAM使用的名称，默认值为/etc/pam.d/vsftpd
pam_service_name=vsftpd
 
#(用户的访问控制可以通过user_list和ftpusers(ftpuser不受任何配制项的影响！它总是有效，它是一个黑名单)文件来实现)
#控制用户访问FTP的文件，里面写着用户名称。一个用户名称一行
userlist_file=/etc/vsftpd/user_list

#userlist_enable和userlist_deny两个选项联合起来针对的是：本地全体用户（除去ftpusers中的用户）和出现在user_list文件中的用户以及不在在user_list文件中的用户这三类用户集合进行的设置。
#当且仅当userlist_enable=YES时：userlist_deny项的配置才有效，user_list文件才会被使用；当其为NO时，无论userlist_deny项为何值都是无效的，本地全体用户（除去ftpusers中的用户）都可以登入FTP
#当userlist_enable=YES时，userlist_deny=YES时：user_list是一个黑名单，即：所有出现在名单中的用户都会被拒绝登入；
#当userlist_enable=YES时，userlist_deny=NO时：user_list是一个白名单，即：只有出现在名单中的用户才会被准许登入(user_list之外的用户都被拒绝登入)；另外需要特别提醒的是：使用白名单后，匿名用户将无法登入！除非显式在user_list中加入一行：anonymous
# 是否使userlist这个文件生效
userlist_enable=YES
#设置是否阻扯user_list文件中的用户登录FTP服务器
userlist_deny=YES
 
#是否使用tcp_wrappers作为主机访问控制方式。
tcp_wrappers=NO
 
#启用虚拟用户。默认值为NO
guest_enable=YES
 
#这里用来映射虚拟用户。默认值为ftp。
#guest_username=vsftpd
guest_username=virtual
 
#指定用户独立的配置文件存放目录
user_config_dir=/etc/vsftpd/vusers_dir

#匿名/本地用户传输速率（单位：K/S）
anon_max_rate=30000000
local_max_rate=30000000
use_localtime=YES

#是否将所有用户限制在主目录,YES为启用 NO禁用.(该项默认值是NO,即在安装vsftpd后不做配置的话，ftp用户是可以向上切换到主目录之外的)
chroot_local_user=NO

#是否启动限制用户的名单 YES为启用 NO禁用(包括注释掉也为禁用)
chroot_list_enable=YES
#是否限制在主目录下的用户名单，至于是限制名单还是排除名单，这取决于chroot_local_user的值，我们可以这样记忆： chroot_local_user总是一个全局性的设定，其为YES时，全部用户被锁定于主目录，其为NO时，全部用户不被锁定于主目录。那么我们势必需要在全局设定下能做出一些“微调”，即，我们总是需要一种“例外机制"，所以当chroot_list_enable=YES时，表示我们“需要例外”。而”例外“的含义总是有一个上下文的，即，当”全部用户被锁定于主目录“时（即chroot_local_user=YES），"例外"就是：不被锁定的用户是哪些；当"全部用户不被锁定于主目录"时（即chroot_local_user=NO），"例外"“就是：要被锁定的用户是哪些。这样解释和记忆两者之间的关系就很清晰了！
chroot_list_file=/etc/vsftpd/vsftpd.chroot_list

#从2.3.5之后，vsftpd增强了安全检查，如果用户被限定在了其主目录下，则该用户的主目录不能再具有写权限了！如果检查发现还有写权限，就会报该错误#要修复这个错误可以用命令chmod a-w 去除主目录写权限，或者你可以在vsftpd的配置文件中增加下列两项中的一项
allow_writeable_chroot=YES

#禁用反向域名解析
reverse_lookup_enable=NO
 
#每个来源IP可建立多少ftp连接
max_per_ip=0
 
##最多允许100个人同时使用FTP服务器
max_clients=100
 
##设置客户端/数据连接超时时间
idle_session_timeout=600
data_connection_timeout=120

```

> 



```
touch  /etc/vsftpd/vftpuser.txt

加入用户的用户名和口令信息，格式很简单："奇数行用户名，偶数行口令"

hyywnobody
123456

```

> 



```
使用db_load命令用HASH算法生成FTP用户数据库文件vftpuser.db

\db_load -T -t hash -f /etc/vsftpd/vftpuser.txt /etc/vsftpd/vftpuser.db
chmod 600 /etc/vsftpd/vftpuser.db

```

> 



```
为保证其他用户可以访问，给予rwxr-xr-x权限

useradd virtual -s /sbin/nologin
mkdir -p /data/ftp/
chmod -Rf 755 /data/ftp

```

> 



```
mv /etc/pam.d/vsftpd /etc/pam.d/vsftpd.back
cat /etc/pam.d/vsftpd

参数db用于指向刚刚生成的vftpuser.db文件，但不要写后缀

centos7系列：
auth       required     pam_userdb.so db=/etc/vsftpd/vftpuser
account    required     pam_userdb.so db=/etc/vsftpd/vftpuser

centos6系列：
auth required /lib64/security/pam_userdb.so db=/etc/vsftpd/vftpuser
account required /lib64/security/pam_userdb.so db=/etc/vsftpd/vftpuser

```

> 



```
虚拟用户的权限默认不能上传、创建、修改文件
如果希望用户能够访问或管理FTP内的资料，就需要让FTP程序支持独立的用户权限配置文件了

首先，编辑vsftpd.conf中的配置指定用户独立的配置文件存放目录：
user_config_dir=/etc/vsftpd/vusers_dir

创建用户配置文件存放目录
mkdir -p /etc/vsftpd/vusers_dir

创建以用户名命名的配置文件
touch /etc/vsftpd/vusers_dir/hyywnobody

配置用户权限，常用组合：
(1) 浏览+上传+下载
#指定该用户的登陆目录
local_root=/data/ftp/hyywnobody
anon_umask=022
#yes=禁止浏览；no=只读，下载
anon_world_readable_only=no
#是否开启写权限
write_enable=yes
#是否可上传
anon_upload_enable=yes

#是否可以创建目录
anon_mkdir_write_enable=yes
#是否可删除
anon_other_write_enable=yes

(2) 浏览+下载
local_root=/data/ftp/hyywnobody
anon_world_readable_only=no

(3) 可上传
local_root=/data/ftp/hyywnobody
write_enable=yes
anon_upload_enable=yes
根据虚拟用户配置文件中设置的local_root，创建虚拟用户主目录并更改权限

mkdir -p /data/ftp/hyywnobody
chown virtual.virtual /data/ftp/hyywnobody

```
