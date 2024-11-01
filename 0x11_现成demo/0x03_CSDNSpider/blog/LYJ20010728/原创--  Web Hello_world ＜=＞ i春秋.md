# 原创
：  Web Hello_world ＜=＞ i春秋

# Web Hello_world ＜=＞ i春秋

[题目内容](http://106.75.72.168:9999/)<br/> 首先，扫描一下网站看看有没有什么可以利用的信息：

```
python3 dirsearch.py -u "http://106.75.72.168:9999/" -e *

```

```
┌──(root💀kali)-[~/Desktop/dirsearch]
└─# python3 dirsearch.py -u "http://106.75.72.168:9999/" -e*

  _|. _ _  _  _  _ _|_    v0.4.1
 (_||| _) (/_(_|| (_| )

Extensions: php, inc.php, jsp, jsf, asp, aspx, do, action, cgi, pl, html, htm, js, css, json, txt, tar.gz, tgz | HTTP method: GET | Threads: 30
Wordlist size: 17357

Error Log: /root/Desktop/dirsearch/logs/errors-21-02-05_05-48-23.log

Target: http://106.75.72.168:9999/

Output File: /root/Desktop/dirsearch/reports/106.75.72.168/_21-02-05_05-48-23.txt

[05:48:23] Starting: 
[05:48:26] 301 -  319B  - /.git  -&gt;  http://106.75.72.168:9999/.git/                                                                    


```

发现存在.git泄露：

```
python2 git_extract.py http://106.75.72.168:9999/.git/

```

```
┌──(root💀kali)-[~/Desktop/Git_Extract]
└─# python2 git_extract.py http://106.75.72.168:9999/.git/                                                                                               1 ⨯

    ________.__  __    ___________         __                        __                                                                                      
   /  _____/|__|/  |_  \_   _____/__  ____/  |_____________    _____/  |_                                                                                    
  /   \  ___|  \   __\  |    __)_\  \/  /\   __\_  __ \__  \ _/ ___\   __\                                                                                   
  \    \_\  \  ||  |    |        \&gt;    &lt;  |  |  |  | \// __ \\  \___|  |                                                                                     
   \______  /__||__|   /_______  /__/\_ \ |__|  |__|  (____  /\___  &gt;__|                                                                                     
          \/                   \/      \/                  \/     \/                                                                                         
                                                    Author: gakki429                                                                                         
                                                                                                                                                             
[05:50:49] [*] Start Extract
[05:50:49] [*] Target Git: http://106.75.72.168:9999/.git/
[05:50:49] [*] Analyze .git/HEAD
[05:50:49] [+] Extract Ref refs/heads/master 887746
[05:50:49] [*] Clone Commit 887746
[05:50:49] [*] Parse Tree ../ b5dfb5
[05:50:49] [*] Analyze .git/logs/HEAD
[05:50:49] [*] Clone Commit 09e053
[05:50:49] [*] Parse Tree ../ 9ee4dc
[05:50:49] [*] Detect .git/index
[05:50:49] [+] Index index.php                                         
[05:50:49] [*] Extract Done


```

得到内容含有两个flag.js文件，利用diff命令比较一下可以发现他们的差别就是flag内容：

```
┌──(root💀kali)-[~/Desktop/Git_Extract/106.75.72.168_9999]
└─# diff flag.js flag.js.04bb09 
220c220
&lt;           BufferedBlockAlgorithm=o                           .          
---
&gt;           BufferedBlockAlgorithm=f                           .          
256c256
&lt;         c=n/(4*o),c=e                 ?t.ceil(c):       
---
&gt;         c=n/(4*o),c=e                 ?t.cell(c):       
297c297
&lt;         _append                                (t)        
---
&gt;         _ppend                                (t)        
334c334
&lt;         }; return r                  }(Math);(       
---
&gt;         }; return g                  }(Math);(       
377c377
&lt;    (n)                ,-1!=n      &amp;&amp;                  (r=n  
---
&gt;    (n)                ,-1!=n      &amp;&amp;                  {r=n  
410c410
&lt;     (t                                          ,e,   
---
&gt;     (t                                          ,8,   
431c431
&lt;  return(t   &lt;&lt;              o|t &gt;&gt;&gt;32-o             )+e} 
---
&gt;  return(t   &lt;&lt;              o|t &gt;&gt;&gt;3-o             )+e} 
454c454
&lt;    ,s=o                .algo     ,f=                 [],  
---
&gt;    ,s=o                .algo     ,e=                 [],  
490c490
&lt;      ,g=t                                        [o+    
---
&gt;      ,g=t                                        [f+    
516c516
&lt;      ,w                                        ,z,    
---
&gt;      ,c                                        ,z,    
535c535
&lt;  ]) ,D=e             (D,w,z,  C,m,12             ,f[13]) 
---
&gt;  ]) ,D=e             (D,w,z,  C,m,12             ,f[133]) 
541c541
&lt;     z,x                                         ,17    
---
&gt;     z,x                                         ,177    
567c567
&lt;     ]),                                         w=r    
---
&gt;     ]),                                         w=f    
592c592
&lt;     D=i                                          (D,   
---
&gt;     D=1                                          (D,   
595c595
&lt;       ,f                                      [33     
---
&gt;       ,c                                      [33     
621c621
&lt;       z=i                                      (z,     
---
&gt;       z=d                                      (z,     
637c637
&lt;   w,       h,23        ,f[47]   ),w=n     (w,z,C      ,D,c,6 
---
&gt;   w,       h,23        ,f[47]   ),5=n     (w,z,C      ,D,c,6 
678c678
&lt;                   [62]),z=n(z,C,D,w,                 
---
&gt;                   [62]),d=n(z,C,D,w,                 
867c867
&lt;    :1,                _DEC_XFORM_MODE     :2,                 _createHelper  
---
&gt;    :1,                _DEC_XFORM_MODE     :4,                 _createHelper  
970c970
&lt;      &lt;&lt;           16|r           &lt;&lt; 8|r          ,o=[    
---
&gt;      &lt;&lt;           1|r           &lt;&lt; 8|r          ,o=[    
1026c1026
&lt;  _process (!0)             ,t.unpad  (e);              return e 
---
&gt;  _process (!3)             ,t.unpad  (e);              return e 
1051c1051
&lt;  function    (t){    var e=t.  ciphertext    ;t=t      .salt; 
---
&gt;  function    (t){    var e=t.  ciphertext    ;t=6      .salt; 
1102c1102
&lt;   ;        return p.create         ({   ciphertext     :e,key      :r,iv: 
---
&gt;   ;        return p.create         ({   eiphertext     :e,key      :r,iv: 
1181c1181
&lt;  extend    (i);    e=this._parse  (e    ,i.      format);r=i.
---
&gt;  extend    (i);    a=this._parse  (e    ,i.      format);r=i.
1209c1209
&lt;   ,l=0                                            ;256   
---
&gt;   ,l=0                                            ;257   
1229c1229
&lt;     [v],B=d          [S],          m=257          *d[_    
---
&gt;     [v],B=c          [S],          m=257          *d[_    
1239c1239
&lt;     _]=m                                          &lt;&lt;    
---
&gt;     _]=a                                          &lt;&lt;    
1244c1244
&lt;           16|m                            &gt;&gt;&gt;16                     ;u[_            
---
&gt;           16|d                            &gt;&gt;&gt;16                     ;u[_            
1258c1258
&lt;  (var               t=this.  _key,e=t             .words, 
---
&gt;  (var               t=this.  _key,e=c             .words, 
1284c1284
&lt;  :( s=s              &lt;&lt; 8|s   &gt;&gt;&gt;24             ,s=i[s  
---
&gt;  :( s=s              &lt;&lt; 8|d   &gt;&gt;&gt;24             ,s=i[s  
1307c1307
&lt;   s=r       %4?        n[o]:n   [o-     4],e[r      ]=4&gt;r  
---
&gt;   s=r       %4?        n[o]:n   [o-     5],e[r      ]=4&gt;r  
1356c1356
&lt;         2],p=t[e+3]                 ^r[3],d=4,l=1       
---
&gt;         2],p=t[a+3]                 ^r[3],d=4,l=1       
1385c1385
&lt;   [       u&amp;255        ]^r[ d++    ],     f=y,h=g      ,u=_;y= 
---
&gt;   [       u&amp;255        ]^r[ d++    ],     f=y,h=8      ,u=_;y= 
1432c1432
&lt;         :8});t.AES=e                 .       
---
&gt;         :8});t.AES=1                 .       
1458c1458
&lt;         ;i=[function                 (t){ return o       
---
&gt;         ;i=[function                 (t){ return 4       
1484c1484
&lt;         'k.o.B'+                 '(9-1)'+       
---
&gt;         'k.a.B'+                 '(9-1)'+       
1526c1526
&lt;           +                           '0.6.8'          
---
&gt;           +                           '0.2.8'          


```

得到flag：`flag{82efc37f1cd5d4636ea7cadcd5a814a2}`
