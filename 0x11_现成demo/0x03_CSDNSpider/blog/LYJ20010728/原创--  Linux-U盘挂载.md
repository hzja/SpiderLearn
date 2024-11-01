# 原创
：  Linux-U盘挂载

# Linux-U盘挂载

```
连接成功
Activate the web console with: systemctl enable --now cockpit.socket

Last login: Tue Dec 29 15:37:21 2020 from 10.0.0.2
[root@H3rmesk1t ~]# pwd
/root
[root@H3rmesk1t ~]# hostnamectl set-hostname H3rmesk1t
[root@H3rmesk1t ~]# su
[root@H3rmesk1t ~]# uname -r
4.18.0-240.el8.x86_64
[root@H3rmesk1t ~]# cat /etc/redhat-release 
CentOS Linux release 8.3.2011
[root@H3rmesk1t ~]# cd /etc//yum.repos.d/
[root@H3rmesk1t yum.repos.d]# ls
CentOS-Base-repo.bak                 CentOS-Linux-Debuginfo.repo         CentOS-Linux-Media.repo       epel-modular.repo
CentOS-Base.repo                     CentOS-Linux-Devel.repo             CentOS-Linux-Plus.repo        epel-playground.repo
CentOS-Linux-AppStream.repo          CentOS-Linux-Extras.repo            CentOS-Linux-PowerTools.repo  epel-testing-modular.repo
CentOS-Linux-BaseOS.repo             CentOS-Linux-FastTrack.repo         CentOS-Linux-Sources.repo     epel-testing.repo
CentOS-Linux-ContinuousRelease.repo  CentOS-Linux-HighAvailability.repo  docker-ce.repo                epel.repo
[root@H3rmesk1t yum.repos.d]# mkdir bak
[root@H3rmesk1t yum.repos.d]# ls
CentOS-Base-repo.bak                 CentOS-Linux-Debuginfo.repo         CentOS-Linux-Media.repo       docker-ce.repo             epel.repo
CentOS-Base.repo                     CentOS-Linux-Devel.repo             CentOS-Linux-Plus.repo        epel-modular.repo
CentOS-Linux-AppStream.repo          CentOS-Linux-Extras.repo            CentOS-Linux-PowerTools.repo  epel-playground.repo
CentOS-Linux-BaseOS.repo             CentOS-Linux-FastTrack.repo         CentOS-Linux-Sources.repo     epel-testing-modular.repo
CentOS-Linux-ContinuousRelease.repo  CentOS-Linux-HighAvailability.repo  bak                           epel-testing.repo
[root@H3rmesk1t yum.repos.d]# cd
[root@H3rmesk1t ~]# cd /etc/yum.repos.d/
[root@H3rmesk1t yum.repos.d]# pwd
/etc/yum.repos.d
[root@H3rmesk1t yum.repos.d]# dnf makecache
Failed to set locale, defaulting to C.UTF-8
Repository extras is listed more than once in the configuration
CentOS-8 - Base - mirrors.aliyun.com                                                                                     4.4 kB/s | 3.9 kB     00:00    
CentOS-8 - Extras - mirrors.aliyun.com                                                                                   3.4 kB/s | 1.5 kB     00:00    
CentOS-8 - AppStream - mirrors.aliyun.com                                                                                9.1 kB/s | 4.3 kB     00:00    
CentOS Linux 8 - AppStream                                                                                               4.3 kB/s | 4.3 kB     00:01    
CentOS Linux 8 - BaseOS                                                                                                  3.9 kB/s | 3.9 kB     00:00    
Docker CE Stable - x86_64                                                                                                8.8 kB/s | 3.5 kB     00:00    
Extra Packages for Enterprise Linux Modular 8 - x86_64                                                                   677  B/s | 8.8 kB     00:13    
Extra Packages for Enterprise Linux 7 - x86_64                                                                            10 kB/s | 4.7 kB     00:00    
Metadata cache created.
[root@H3rmesk1t yum.repos.d]# cd
[root@H3rmesk1t ~]# rpm qa samba
RPM version 4.14.3
Copyright (C) 1998-2002 - Red Hat, Inc.
This program may be freely redistributed under the terms of the GNU GPL

Usage: rpm [-afgpcdLAlsiv?] [-a|--all] [-f|--file] [-g|--group] [-p|--package] [--pkgid] [--hdrid] [--triggeredby] [--whatconflicts]
        [--whatrequires] [--whatobsoletes] [--whatprovides] [--whatrecommends] [--whatsuggests] [--whatsupplements] [--whatenhances]
        [--nomanifest] [-c|--configfiles] [-d|--docfiles] [-L|--licensefiles] [-A|--artifactfiles] [--dump] [-l|--list]
        [--queryformat=QUERYFORMAT] [-s|--state] [--nofiledigest] [--nofiles] [--nodeps] [--noscript] [--allfiles] [--allmatches] [--badreloc]
        [-e|--erase=&lt;package&gt;+] [--excludedocs] [--excludepath=&lt;path&gt;] [--force] [-F|--freshen=&lt;packagefile&gt;+] [-h|--hash] [--ignorearch]
        [--ignoreos] [--ignoresize] [--noverify] [-i|--install] [--justdb] [--nodeps] [--nofiledigest] [--nocontexts] [--nocaps] [--noorder]
        [--noscripts] [--notriggers] [--oldpackage] [--percent] [--prefix=&lt;dir&gt;] [--relocate=&lt;old&gt;=&lt;new&gt;] [--replacefiles] [--replacepkgs]
        [--test] [-U|--upgrade=&lt;packagefile&gt;+] [--reinstall=&lt;packagefile&gt;+] [-D|--define='MACRO EXPR'] [--undefine=MACRO] [-E|--eval='EXPR']
        [--target=CPU-VENDOR-OS] [--macros=&lt;FILE:...&gt;] [--noplugins] [--nodigest] [--nosignature] [--rcfile=&lt;FILE:...&gt;] [-r|--root=ROOT]
        [--dbpath=DIRECTORY] [--querytags] [--showrc] [--quiet] [-v|--verbose] [--version] [-?|--help] [--usage] [--scripts] [--setperms]
        [--setugids] [--setcaps] [--restore] [--conflicts] [--obsoletes] [--provides] [--requires] [--recommends] [--suggests] [--supplements]
        [--enhances] [--info] [--changelog] [--changes] [--xml] [--triggers] [--filetriggers] [--last] [--dupes] [--filesbypkg] [--fileclass]
        [--filecolor] [--fileprovide] [--filerequire] [--filecaps]
[root@H3rmesk1t ~]# ping g.cn
PING g.cn (203.208.41.34) 56(84) bytes of data.
64 bytes from 203.208.41.34 (203.208.41.34): icmp_seq=1 ttl=128 time=71.3 ms
64 bytes from 203.208.41.34 (203.208.41.34): icmp_seq=2 ttl=128 time=89.3 ms
64 bytes from 203.208.41.34 (203.208.41.34): icmp_seq=3 ttl=128 time=142 ms
64 bytes from 203.208.41.34 (203.208.41.34): icmp_seq=4 ttl=128 time=87.1 ms
64 bytes from 203.208.41.34 (203.208.41.34): icmp_seq=5 ttl=128 time=125 ms
64 bytes from 203.208.41.34 (203.208.41.34): icmp_seq=6 ttl=128 time=119 ms
^C
--- g.cn ping statistics ---
6 packets transmitted, 6 received, 0% packet loss, time 10ms
rtt min/avg/max/mdev = 71.274/105.647/142.068/24.761 ms
[root@H3rmesk1t ~]# dnf install samba -y 
Failed to set locale, defaulting to C.UTF-8
Repository extras is listed more than once in the configuration
Last metadata expiration check: 0:01:53 ago on Tue Dec 29 16:00:45 2020.
Dependencies resolved.
=========================================================================================================================================================
 Package                                    Architecture                   Version                                    Repository                    Size
=========================================================================================================================================================
Installing:
 samba                                      x86_64                         4.12.3-12.el8.3                            base                         840 k
Installing dependencies:
 samba-common-tools                         x86_64                         4.12.3-12.el8.3                            base                         484 k
 samba-libs                                 x86_64                         4.12.3-12.el8.3                            base                         188 k

Transaction Summary
=========================================================================================================================================================
Install  3 Packages

Total download size: 1.5 M
Installed size: 4.0 M
Downloading Packages:
(1/3): samba-libs-4.12.3-12.el8.3.x86_64.rpm                                                                              96 kB/s | 188 kB     00:01    
(2/3): samba-common-tools-4.12.3-12.el8.3.x86_64.rpm                                                                     196 kB/s | 484 kB     00:02    
(3/3): samba-4.12.3-12.el8.3.x86_64.rpm                                                                                  286 kB/s | 840 kB     00:02    
---------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                    513 kB/s | 1.5 MB     00:02     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                 1/1 
  Installing       : samba-libs-4.12.3-12.el8.3.x86_64                                                                                               1/3 
  Installing       : samba-common-tools-4.12.3-12.el8.3.x86_64                                                                                       2/3 
  Installing       : samba-4.12.3-12.el8.3.x86_64                                                                                                    3/3 
  Running scriptlet: samba-4.12.3-12.el8.3.x86_64                                                                                                    3/3 
  Verifying        : samba-4.12.3-12.el8.3.x86_64                                                                                                    1/3 
  Verifying        : samba-common-tools-4.12.3-12.el8.3.x86_64                                                                                       2/3 
  Verifying        : samba-libs-4.12.3-12.el8.3.x86_64                                                                                               3/3 
Installed products updated.

Installed:
  samba-4.12.3-12.el8.3.x86_64                samba-common-tools-4.12.3-12.el8.3.x86_64                samba-libs-4.12.3-12.el8.3.x86_64               

Complete!
[root@H3rmesk1t ~]# rpm -qa samba
samba-4.12.3-12.el8.3.x86_64
[root@H3rmesk1t ~]# fdisk -l
Disk /dev/sda: 40 GiB, 42949672960 bytes, 83886080 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xecf93556

Device     Boot   Start      End  Sectors Size Id Type
/dev/sda1  *       2048  2099199  2097152   1G 83 Linux
/dev/sda2       2099200 83886079 81786880  39G 8e Linux LVM


Disk /dev/mapper/cl-root: 35.1 GiB, 37643878400 bytes, 73523200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/cl-swap: 4 GiB, 4227858432 bytes, 8257536 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/sdb: 28.8 GiB, 30943995904 bytes, 60437492 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x2c8923e0

Device     Boot Start      End  Sectors  Size Id Type
/dev/sdb1  *       63 60435647 60435585 28.8G  b W95 FAT32
[root@H3rmesk1t ~]# cd /dev
[root@H3rmesk1t dev]# cd
[root@H3rmesk1t ~]# dnf -y install netf-3g
Failed to set locale, defaulting to C.UTF-8
Repository extras is listed more than once in the configuration
Last metadata expiration check: 0:17:16 ago on Tue Dec 29 16:00:45 2020.
No match for argument: netf-3g
Error: Unable to find a match: netf-3g
[root@H3rmesk1t ~]# dnf -y install epel
Failed to set locale, defaulting to C.UTF-8
Repository extras is listed more than once in the configuration
Last metadata expiration check: 0:19:31 ago on Tue Dec 29 16:00:45 2020.
No match for argument: epel
Error: Unable to find a match: epel
[root@H3rmesk1t ~]# dnf -y install epel-release
Failed to set locale, defaulting to C.UTF-8
Repository extras is listed more than once in the configuration
Last metadata expiration check: 0:00:44 ago on Tue Dec 29 16:20:35 2020.
Package epel-release-8-10.el8.noarch is already installed.
Dependencies resolved.
Nothing to do.
Complete!
[root@H3rmesk1t ~]# dnf -y install ntfs-3g
Failed to set locale, defaulting to C.UTF-8
Repository extras is listed more than once in the configuration
Last metadata expiration check: 0:01:11 ago on Tue Dec 29 16:20:35 2020.
Dependencies resolved.
=========================================================================================================================================================
 Package                           Architecture                     Version                                         Repository                      Size
=========================================================================================================================================================
Installing:
 ntfs-3g                           x86_64                           2:2017.3.23-11.el7                              epel                           265 k

Transaction Summary
=========================================================================================================================================================
Install  1 Package

Total download size: 265 k
Installed size: 612 k
Downloading Packages:
ntfs-3g-2017.3.23-11.el7.x86_64.rpm                                                                                      147 kB/s | 265 kB     00:01    
---------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                    147 kB/s | 265 kB     00:01     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                 1/1 
  Installing       : ntfs-3g-2:2017.3.23-11.el7.x86_64                                                                                               1/1 
  Running scriptlet: ntfs-3g-2:2017.3.23-11.el7.x86_64                                                                                               1/1 
  Verifying        : ntfs-3g-2:2017.3.23-11.el7.x86_64                                                                                               1/1 
Installed products updated.

Installed:
  ntfs-3g-2:2017.3.23-11.el7.x86_64                                                                                                                      

Complete!
[root@H3rmesk1t ~]# dnf -y install epel-release ntfs-3g
Failed to set locale, defaulting to C.UTF-8
Repository extras is listed more than once in the configuration
Last metadata expiration check: 0:02:36 ago on Tue Dec 29 16:20:35 2020.
Package epel-release-8-10.el8.noarch is already installed.
Package ntfs-3g-2:2017.3.23-11.el7.x86_64 is already installed.
Dependencies resolved.
Nothing to do.
Complete!
[root@H3rmesk1t ~]# fdisk -l
Disk /dev/sda: 40 GiB, 42949672960 bytes, 83886080 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xecf93556

Device     Boot   Start      End  Sectors Size Id Type
/dev/sda1  *       2048  2099199  2097152   1G 83 Linux
/dev/sda2       2099200 83886079 81786880  39G 8e Linux LVM


Disk /dev/mapper/cl-root: 35.1 GiB, 37643878400 bytes, 73523200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/cl-swap: 4 GiB, 4227858432 bytes, 8257536 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/sdb: 28.8 GiB, 30943995904 bytes, 60437492 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x2c8923e0

Device     Boot Start      End  Sectors  Size Id Type
/dev/sdb1  *       63 60435647 60435585 28.8G  b W95 FAT32
[root@H3rmesk1t ~]# mount /dev/sdb /mnt
mount: /mnt: wrong fs type, bad option, bad superblock on /dev/sdb, missing codepage or helper program, or other error.
[root@H3rmesk1t ~]# ntfs-3g /dev/sdb1 /mnt
NTFS signature is missing.
Failed to mount '/dev/sdb1': Invalid argument
The device '/dev/sdb1' doesn't seem to have a valid NTFS.
Maybe the wrong device is used? Or the whole disk instead of a
partition (e.g. /dev/sda, not /dev/sda1)? Or the other way around?
[root@H3rmesk1t ~]# mount /dev/sdb1 /mnt -t exfat
mount: /mnt: unknown filesystem type 'exfat'.
[root@H3rmesk1t ~]# wget http://download1.rpmfusion.org/free/e1/rpmfusion-free-release-7.noarch.rpm
--2020-12-29 16:35:02--  http://download1.rpmfusion.org/free/e1/rpmfusion-free-release-7.noarch.rpm
Resolving download1.rpmfusion.org (download1.rpmfusion.org)... 193.28.235.60, 2001:67c:1740:8005::60
Connecting to download1.rpmfusion.org (download1.rpmfusion.org)|193.28.235.60|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2020-12-29 16:35:03 ERROR 404: Not Found.

[root@H3rmesk1t ~]# ^C
[root@H3rmesk1t ~]# wget http://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
--2020-12-29 16:39:11--  http://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
Resolving download1.rpmfusion.org (download1.rpmfusion.org)... 193.28.235.60, 2001:67c:1740:8005::60
Connecting to download1.rpmfusion.org (download1.rpmfusion.org)|193.28.235.60|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 6448 (6.3K) [application/x-rpm]
Saving to: 'rpmfusion-free-release-7.noarch.rpm'

rpmfusion-free-release-7.noarch.rpm    100%[=========================================================================&gt;]   6.30K  --.-KB/s    in 0s      

2020-12-29 16:39:12 (444 MB/s) - 'rpmfusion-free-release-7.noarch.rpm' saved [6448/6448]

[root@H3rmesk1t ~]# rpm -ivh rpmfusion-free-release-7.noarch.rpm
warning: rpmfusion-free-release-7.noarch.rpm: Header V4 RSA/SHA1 Signature, key ID f5cf6c1e: NOKEY
Verifying...                          ################################# [100%]
Preparing...                          ################################# [100%]
Updating / installing...
   1:rpmfusion-free-release-7-4       ################################# [100%]
[root@H3rmesk1t ~]# yum install fuse-exfat
Failed to set locale, defaulting to C.UTF-8
Repository extras is listed more than once in the configuration
RPM Fusion for EL 7 - Free - Updates                                                                                     109 kB/s | 327 kB     00:02    
Dependencies resolved.
=========================================================================================================================================================
 Package                           Architecture                  Version                             Repository                                     Size
=========================================================================================================================================================
Installing:
 fuse-exfat                        x86_64                        1.3.0-1.el7                         rpmfusion-free-updates                         40 k

Transaction Summary
=========================================================================================================================================================
Install  1 Package

Total download size: 40 k
Installed size: 75 k
Is this ok [y/N]: y
Downloading Packages:
fuse-exfat-1.3.0-1.el7.x86_64.rpm                                                                                         83 kB/s |  40 kB     00:00    
---------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                     23 kB/s |  40 kB     00:01     
warning: /var/cache/dnf/rpmfusion-free-updates-bb4a845bb2222a04/packages/fuse-exfat-1.3.0-1.el7.x86_64.rpm: Header V4 RSA/SHA1 Signature, key ID f5cf6c1e: NOKEY
RPM Fusion for EL 7 - Free - Updates                                                                                     1.6 MB/s | 1.6 kB     00:00    
Importing GPG key 0xF5CF6C1E:
 Userid     : "RPM Fusion free repository for EL (7) &lt;rpmfusion-buildsys@lists.rpmfusion.org&gt;"
 Fingerprint: DB9A 9A57 CAFD 23DA 3A88 792F 758B 3D18 F5CF 6C1E
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-el-7
Is this ok [y/N]: y
Key imported successfully
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                 1/1 
  Installing       : fuse-exfat-1.3.0-1.el7.x86_64                                                                                                   1/1 
  Running scriptlet: fuse-exfat-1.3.0-1.el7.x86_64                                                                                                   1/1 
  Verifying        : fuse-exfat-1.3.0-1.el7.x86_64                                                                                                   1/1 
Installed products updated.

Installed:
  fuse-exfat-1.3.0-1.el7.x86_64                                                                                                                          

Complete!
[root@H3rmesk1t ~]# fdisk -l
Disk /dev/sda: 40 GiB, 42949672960 bytes, 83886080 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xecf93556

Device     Boot   Start      End  Sectors Size Id Type
/dev/sda1  *       2048  2099199  2097152   1G 83 Linux
/dev/sda2       2099200 83886079 81786880  39G 8e Linux LVM


Disk /dev/mapper/cl-root: 35.1 GiB, 37643878400 bytes, 73523200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/cl-swap: 4 GiB, 4227858432 bytes, 8257536 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/sdb: 28.8 GiB, 30943995904 bytes, 60437492 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x2c8923e0

Device     Boot Start      End  Sectors  Size Id Type
/dev/sdb1  *       63 60435647 60435585 28.8G  b W95 FAT32
[root@H3rmesk1t ~]# vim /etc/fstab 
[root@H3rmesk1t ~]# df -h
Filesystem           Size  Used Avail Use% Mounted on
devtmpfs             1.8G     0  1.8G   0% /dev
tmpfs                1.9G     0  1.9G   0% /dev/shm
tmpfs                1.9G   10M  1.9G   1% /run
tmpfs                1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/mapper/cl-root   36G  5.6G   30G  16% /
/dev/sda1           1014M  240M  775M  24% /boot
tmpfs                371M  1.2M  370M   1% /run/user/42
tmpfs                371M  3.5M  368M   1% /run/user/0
/dev/sr0             8.7G  8.7G     0 100% /run/media/root/CentOS-8-3-2011-x86_64-dvd
[root@H3rmesk1t ~]# fdisk -l
Disk /dev/sda: 40 GiB, 42949672960 bytes, 83886080 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xecf93556

Device     Boot   Start      End  Sectors Size Id Type
/dev/sda1  *       2048  2099199  2097152   1G 83 Linux
/dev/sda2       2099200 83886079 81786880  39G 8e Linux LVM


Disk /dev/mapper/cl-root: 35.1 GiB, 37643878400 bytes, 73523200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/cl-swap: 4 GiB, 4227858432 bytes, 8257536 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/sdb: 28.8 GiB, 30943995904 bytes, 60437492 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x2c8923e0

Device     Boot Start      End  Sectors  Size Id Type
/dev/sdb1  *       63 60435647 60435585 28.8G  b W95 FAT32
[root@H3rmesk1t ~]# ls
Desktop    Music     Python-3.6.4      Videos           initial-setup-ks.cfg  rpmfusion-free-release-7.noarch.rpm  turtle-0.0.2         word.zip
Documents  Pictures  Python-3.6.4.tgz  anaconda-ks.cfg  mypackages            screenFetch                          turtle-0.0.2.tar.gz  xt
Downloads  Public    Templates         duola.py         pig.py                test.py                              word.txt             yinghuashu.py
[root@H3rmesk1t ~]# mount /dev/sdb1 /data
mount: /data: mount point does not exist.
[root@H3rmesk1t ~]# mkdir /data
[root@H3rmesk1t ~]# ls
Desktop    Music     Python-3.6.4      Videos           initial-setup-ks.cfg  rpmfusion-free-release-7.noarch.rpm  turtle-0.0.2         word.zip
Documents  Pictures  Python-3.6.4.tgz  anaconda-ks.cfg  mypackages            screenFetch                          turtle-0.0.2.tar.gz  xt
Downloads  Public    Templates         duola.py         pig.py                test.py                              word.txt             yinghuashu.py
[root@H3rmesk1t ~]# mkdir data
[root@H3rmesk1t ~]# ls
Desktop    Pictures          Templates        duola.py              rpmfusion-free-release-7.noarch.rpm  turtle-0.0.2.tar.gz  yinghuashu.py
Documents  Public            Videos           initial-setup-ks.cfg  screenFetch                          word.txt
Downloads  Python-3.6.4      anaconda-ks.cfg  mypackages            test.py                              word.zip
Music      Python-3.6.4.tgz  data             pig.py                turtle-0.0.2                         xt
[root@H3rmesk1t ~]# mount /dev/sdb1 /data
[root@H3rmesk1t ~]# cd /data/
[root@H3rmesk1t data]# ls
'????'      'AWD??'             Data_structure       Dism++                     'System Volume Information'   kali-linux-2020.4-vmware-amd64.7z
'????????'  'AppScan 8.7 ???'   DigitalLicense.exe   Student_Management_System  '_CDUT??????'                 spacesniffer_1_3_0_2
[root@H3rmesk1t data]# cp S
Student_Management_System/ System Volume Information/ 
[root@H3rmesk1t data]# cp Student_Management_System/ ../root/
cp: -r not specified; omitting directory 'Student_Management_System/'
[root@H3rmesk1t data]# cp -r Student_Management_System/ ../root/
[root@H3rmesk1t data]# cd /root/
[root@H3rmesk1t ~]# ls
Desktop    Pictures          Student_Management_System  data                  pig.py                               turtle-0.0.2         xt
Documents  Public            Templates                  duola.py              rpmfusion-free-release-7.noarch.rpm  turtle-0.0.2.tar.gz  yinghuashu.py
Downloads  Python-3.6.4      Videos                     initial-setup-ks.cfg  screenFetch                          word.txt
Music      Python-3.6.4.tgz  anaconda-ks.cfg            mypackages            test.py                              word.zip
[root@H3rmesk1t ~]# vim /etc/fstab 
[root@H3rmesk1t ~]# vim /etc/fstab 
[root@H3rmesk1t ~]# vim /etc/fstab 
[root@H3rmesk1t ~]# df -h
Filesystem           Size  Used Avail Use% Mounted on
devtmpfs             1.8G     0  1.8G   0% /dev
tmpfs                1.9G     0  1.9G   0% /dev/shm
tmpfs                1.9G   10M  1.9G   1% /run
tmpfs                1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/mapper/cl-root   36G  5.6G   30G  16% /
/dev/sda1           1014M  240M  775M  24% /boot
tmpfs                371M  1.2M  370M   1% /run/user/42
tmpfs                371M  3.5M  368M   1% /run/user/0
/dev/sr0             8.7G  8.7G     0 100% /run/media/root/CentOS-8-3-2011-x86_64-dvd
/dev/sdb1             29G   16G   14G  55% /data
[root@H3rmesk1t ~]# fdisk -l
Disk /dev/sda: 40 GiB, 42949672960 bytes, 83886080 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xecf93556

Device     Boot   Start      End  Sectors Size Id Type
/dev/sda1  *       2048  2099199  2097152   1G 83 Linux
/dev/sda2       2099200 83886079 81786880  39G 8e Linux LVM


Disk /dev/mapper/cl-root: 35.1 GiB, 37643878400 bytes, 73523200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/cl-swap: 4 GiB, 4227858432 bytes, 8257536 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
[root@H3rmesk1t ~]# fdisk -l
Disk /dev/sda: 40 GiB, 42949672960 bytes, 83886080 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xecf93556

Device     Boot   Start      End  Sectors Size Id Type
/dev/sda1  *       2048  2099199  2097152   1G 83 Linux
/dev/sda2       2099200 83886079 81786880  39G 8e Linux LVM


Disk /dev/mapper/cl-root: 35.1 GiB, 37643878400 bytes, 73523200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/cl-swap: 4 GiB, 4227858432 bytes, 8257536 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
[root@H3rmesk1t ~]# df -h
Filesystem           Size  Used Avail Use% Mounted on
devtmpfs             1.8G     0  1.8G   0% /dev
tmpfs                1.9G     0  1.9G   0% /dev/shm
tmpfs                1.9G  9.9M  1.9G   1% /run
tmpfs                1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/mapper/cl-root   36G  5.6G   30G  16% /
/dev/sda1           1014M  240M  775M  24% /boot
tmpfs                371M  1.2M  370M   1% /run/user/42
tmpfs                371M  3.5M  368M   1% /run/user/0
/dev/sr0             8.7G  8.7G     0 100% /run/media/root/CentOS-8-3-2011-x86_64-dvd
/dev/sdb1             29G   16G   14G  55% /data
[root@H3rmesk1t ~]# 


```
