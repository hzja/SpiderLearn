# 原创
：  su: Authentication failure问题

# su: Authentication failure问题

**做题需要挂载文件是遇到的一个问题：**<br/> su命令不能切换root，提示su: Authentication failure，只要你sudo passwd root过一次之后，下次再su的时候只要输入密码就可以成功登录了

```
(base) pwn@ubuntu:~/Desktop/test$ mount abc findme 
mount: only root can do that
(base) pwn@ubuntu:~/Desktop/test$ conda activate pwn
(pwn) pwn@ubuntu:~/Desktop/test$ mount abc findme 
mount: only root can do that
(pwn) pwn@ubuntu:~/Desktop/test$ su root
Password: 
su: Authentication failure
(pwn) pwn@ubuntu:~/Desktop/test$ sudo passwd root
[sudo] password for pwn: 
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
(pwn) pwn@ubuntu:~/Desktop/test$ su
Password: 
root@ubuntu:/home/pwn/Desktop/test# 


```
