# 原创
：  STP生成树协议

# STP生成树协议

**1、配置用户设备**<br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210111232453449.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

**2、配置STP**

```
配置MK-1交换机
&lt;Huawei&gt;sys
[Huawei]sysname MK-1
[MK-1]stp enable 
[MK-1]stp mode stp

配置MK-2交换机
&lt;Huawei&gt;sys
[Huawei]sysname MK-2
[MK-2]stp enable
[MK-2]stp mode stp

```

**3、检验配置**

```
[MK-1]display stp
-------[CIST Global Info][Mode STP]-------
CIST Bridge         :32768.4c1f-cc96-4da7
Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
CIST Root/ERPC      :32768.4c1f-cc96-4da7 / 0
CIST RegRoot/IRPC   :32768.4c1f-cc96-4da7 / 0
CIST RootPortId     :0.0
BPDU-Protection     :Disabled
TC or TCN received  :5
TC count per hello  :0
STP Converge Mode   :Normal 
Time since last TC  :0 days 0h:0m:50s
Number of TC        :10
Last TC occurred    :GigabitEthernet0/0/2
----[Port1(GigabitEthernet0/0/1)][FORWARDING]----
 Port Protocol       :Enabled
 Port Role           :Designated Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :32768.4c1f-cc96-4da7 / 128.1
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
 Port STP Mode       :STP 
 Port Protocol Type  :Config=auto / Active=dot1s
 BPDU Encapsulation  :Config=stp / Active=stp
 PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
 TC or TCN send      :34
 TC or TCN received  :0
 BPDU Sent           :97             
          TCN: 0, Config: 97, RST: 0, MST: 0
 BPDU Received       :0             
          TCN: 0, Config: 0, RST: 0, MST: 0
----[Port2(GigabitEthernet0/0/2)][FORWARDING]----
 Port Protocol       :Enabled
 Port Role           :Designated Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :32768.4c1f-cc96-4da7 / 128.2
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
 Port STP Mode       :STP 
 Port Protocol Type  :Config=auto / Active=dot1s
 BPDU Encapsulation  :Config=stp / Active=stp
 PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
 TC or TCN send      :36
 TC or TCN received  :2
 BPDU Sent           :100             
          TCN: 0, Config: 100, RST: 0, MST: 0
 BPDU Received       :3             
          TCN: 2, Config: 1, RST: 0, MST: 0
----[Port3(GigabitEthernet0/0/3)][FORWARDING]----
 Port Protocol       :Enabled
 Port Role           :Designated Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :32768.4c1f-cc96-4da7 / 128.3
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
 Port STP Mode       :STP 
 Port Protocol Type  :Config=auto / Active=dot1s
 BPDU Encapsulation  :Config=stp / Active=stp
 PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
 TC or TCN send      :35
 TC or TCN received  :0
 BPDU Sent           :101             
          TCN: 0, Config: 101, RST: 0, MST: 0
 ---- More ----

```

**4、修改桥优先级，控制桥根选举**<br/> 在MK-1上修改桥优先级，配置MK-1为根桥<br/> 优先级的范围是0~61400，输入的值必须是4096的倍数

```
[MK-1]stp priority 0
[MK-1]display stp
-------[CIST Global Info][Mode STP]-------
CIST Bridge         :0    .4c1f-cc96-4da7
Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
CIST Root/ERPC      :0    .4c1f-cc96-4da7 / 0
CIST RegRoot/IRPC   :0    .4c1f-cc96-4da7 / 0
CIST RootPortId     :0.0
BPDU-Protection     :Disabled
TC or TCN received  :5
TC count per hello  :0
STP Converge Mode   :Normal 
Time since last TC  :0 days 0h:3m:59s
Number of TC        :10
Last TC occurred    :GigabitEthernet0/0/2
----[Port1(GigabitEthernet0/0/1)][DISCARDING]----
 Port Protocol       :Enabled
 Port Role           :Designated Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :0.4c1f-cc96-4da7 / 128.1
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None

```

**5、修改端口优先级，控制根端口和指定端口的选举**

```
[MK-1]display stp brief 
 MSTID  Port                        Role  STP State     Protection
   0    GigabitEthernet0/0/1        DESI  FORWARDING      NONE
   0    GigabitEthernet0/0/2        DESI  FORWARDING      NONE
   0    GigabitEthernet0/0/3        DESI  FORWARDING      NONE

[MK-2]display stp brief 
 MSTID  Port                        Role  STP State     Protection
   0    GigabitEthernet0/0/1        DESI  FORWARDING      NONE
   0    GigabitEthernet0/0/2        ROOT  FORWARDING      NONE
   0    GigabitEthernet0/0/3        ALTE  DISCARDING      NONE

```

修改MK-1上端口的优先级，让MK-2的G0/0/3端口成为根端口。在MK-1上有两种方法可以调整：将G0/0/3端口的优先级调小；或将G0/0/2的端口优先级调大。

```
（1）将G0/0/3端口调小。原来端口的优先级默认为128，端口的优先级需要按16的倍数调整，比如将G0/0/3端口的优先级调为32
[MK-1]interface g0/0/3
[MK-1-GigabitEthernet0/0/3]stp port priority 32
[MK-2]display stp brief
 MSTID  Port                        Role  STP State     Protection
   0    GigabitEthernet0/0/1        DESI  FORWARDING      NONE
   0    GigabitEthernet0/0/2        ALTE  DISCARDING      NONE
   0    GigabitEthernet0/0/3        ROOT  FORWARDING      NONE

（2）将G0/0/2端口优先级调大，调整为144
[MK-1]interface g0/0/3
[MK-1-GigabitEthernet0/0/3]stp port priority 128
[MK-2]display stp brief
 MSTID  Port                        Role  STP State     Protection
   0    GigabitEthernet0/0/1        DESI  FORWARDING      NONE
   0    GigabitEthernet0/0/2        ROOT  LEARNING        NONE
   0    GigabitEthernet0/0/3        ALTE  DISCARDING      NONE
   
[MK-1]interface g0/0/2
[MK-1-GigabitEthernet0/0/2]stp port priority 144
[MK-2]display stp brief
 MSTID  Port                        Role  STP State     Protection
   0    GigabitEthernet0/0/1        DESI  FORWARDING      NONE
   0    GigabitEthernet0/0/2        ALTE  DISCARDING      NONE
   0    GigabitEthernet0/0/3        ROOT  DISCARDING      NONE

```

**6、修改端口开销、控制根端口和指定端口的选举**<br/> 在MK-2上修改端口开销，让MK-2的G0/0/3端口成为根端口。

```
//查看MK-2 STP端口状态
[MK-2]display stp brief
 MSTID  Port                        Role  STP State     Protection
   0    GigabitEthernet0/0/1        DESI  FORWARDING      NONE
   0    GigabitEthernet0/0/2        ROOT  DISCARDING      NONE
   0    GigabitEthernet0/0/3        ALTE  DISCARDING      NONE

//（1）将G0/0/2端口开销调大，选举G0/0/3为根端口
[MK-2]display stp interface g0/0/2
-------[CIST Global Info][Mode STP]-------
CIST Bridge         :32768.4c1f-ccb9-45c8
Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
CIST Root/ERPC      :0    .4c1f-cc96-4da7 / 20000
CIST RegRoot/IRPC   :32768.4c1f-ccb9-45c8 / 0
CIST RootPortId     :128.2
BPDU-Protection     :Disabled
TC or TCN received  :219
TC count per hello  :0
STP Converge Mode   :Normal 
Time since last TC  :0 days 0h:3m:0s
Number of TC        :17
Last TC occurred    :GigabitEthernet0/0/2
----[Port2(GigabitEthernet0/0/2)][FORWARDING]----
 Port Protocol       :Enabled
 Port Role           :Root Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :0.4c1f-cc96-4da7 / 128.2
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
  ---- More ----
 
 
 [MK-2]display stp interface g0/0/3
-------[CIST Global Info][Mode STP]-------
CIST Bridge         :32768.4c1f-ccb9-45c8
Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
CIST Root/ERPC      :0    .4c1f-cc96-4da7 / 20000
CIST RegRoot/IRPC   :32768.4c1f-ccb9-45c8 / 0
CIST RootPortId     :128.2
BPDU-Protection     :Disabled
TC or TCN received  :219
TC count per hello  :0
STP Converge Mode   :Normal 
Time since last TC  :0 days 0h:3m:27s
Number of TC        :17
Last TC occurred    :GigabitEthernet0/0/2
----[Port3(GigabitEthernet0/0/3)][DISCARDING]----
 Port Protocol       :Enabled
 Port Role           :Alternate Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :0.4c1f-cc96-4da7 / 128.3
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
  ---- More ----

//上面显示G0/0/2和G0/0/3端口开销都是20000，由于桥ID一样，从G0/0/2端口收到的BPDU包的端口ID较小，所以G0/0/2端口被选举被根端口。在MK-2的G0/0/2端口下修改开销为50000，大于G0/0/3端口开销，G0/0/3端口被选举为根端口
[MK-2]interface g0/0/2
[MK-2-GigabitEthernet0/0/2]stp cost 50000
[MK-2-GigabitEthernet0/0/2]q
[MK-2]display stp
-------[CIST Global Info][Mode STP]-------
CIST Bridge         :32768.4c1f-ccb9-45c8
Config Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
Active Times        :Hello 2s MaxAge 20s FwDly 15s MaxHop 20
CIST Root/ERPC      :0    .4c1f-cc96-4da7 / 20000
CIST RegRoot/IRPC   :32768.4c1f-ccb9-45c8 / 0
CIST RootPortId     :128.3
BPDU-Protection     :Disabled
TC or TCN received  :219
TC count per hello  :0
STP Converge Mode   :Normal 
Time since last TC  :0 days 0h:7m:4s
Number of TC        :17
Last TC occurred    :GigabitEthernet0/0/2
----[Port1(GigabitEthernet0/0/1)][FORWARDING]----
 Port Protocol       :Enabled
 Port Role           :Designated Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :32768.4c1f-ccb9-45c8 / 128.1
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
 Port STP Mode       :STP 
 Port Protocol Type  :Config=auto / Active=dot1s
 BPDU Encapsulation  :Config=stp / Active=stp
 PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 20
 TC or TCN send      :118
 TC or TCN received  :0
 BPDU Sent           :767             
          TCN: 0, Config: 767, RST: 0, MST: 0
 BPDU Received       :0             
          TCN: 0, Config: 0, RST: 0, MST: 0
----[Port2(GigabitEthernet0/0/2)][DISCARDING]----
 Port Protocol       :Enabled
 Port Role           :Alternate Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=50000 / Active=50000
 Designated Bridge/Port   :0.4c1f-cc96-4da7 / 128.2
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
 Port STP Mode       :STP 
 Port Protocol Type  :Config=auto / Active=dot1s
 BPDU Encapsulation  :Config=stp / Active=stp
 PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 0
 TC or TCN send      :5
 TC or TCN received  :104
 BPDU Sent           :6             
          TCN: 5, Config: 1, RST: 0, MST: 0
 BPDU Received       :777             
          TCN: 0, Config: 777, RST: 0, MST: 0
----[Port3(GigabitEthernet0/0/3)][FORWARDING]----
 Port Protocol       :Enabled
 Port Role           :Root Port
 Port Priority       :128
 Port Cost(Dot1T )   :Config=auto / Active=20000
 Designated Bridge/Port   :0.4c1f-cc96-4da7 / 128.3
 Port Edged          :Config=default / Active=disabled
 Point-to-point      :Config=auto / Active=true
 Transit Limit       :147 packets/hello-time
 Protection Type     :None
 Port STP Mode       :STP 
 Port Protocol Type  :Config=auto / Active=dot1s
 BPDU Encapsulation  :Config=stp / Active=stp
 PortTimes           :Hello 2s MaxAge 20s FwDly 15s RemHop 0
 TC or TCN send      :4
 TC or TCN received  :106
 BPDU Sent           :6             
          TCN: 4, Config: 2, RST: 0, MST: 0
  ---- More ----
 //修改后G0/0/3被选举为根端口

//（2）将G0/0/3端口开销调小，调至10000，选举G0/0/3成为根端口
[MK-2]interface g0/0/2
[MK-2-GigabitEthernet0/0/2]stp cost 20000
[MK-2]display stp brief
 MSTID  Port                        Role  STP State     Protection
   0    GigabitEthernet0/0/1        DESI  FORWARDING      NONE
   0    GigabitEthernet0/0/2        ROOT  LEARNING        NONE
   0    GigabitEthernet0/0/3        ALTE  DISCARDING      NONE

[MK-2]interface g0/0/3
[MK-2-GigabitEthernet0/0/3]stp cost 10000
[MK-2]display stp brief 
 MSTID  Port                        Role  STP State     Protection
   0    GigabitEthernet0/0/1        DESI  DISCARDING      NONE
   0    GigabitEthernet0/0/2        ALTE  DISCARDING      NONE
   0    GigabitEthernet0/0/3        ROOT  DISCARDING      NONE

```
