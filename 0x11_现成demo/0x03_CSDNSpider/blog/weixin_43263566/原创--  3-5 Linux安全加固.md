# 原创
：  3-5 Linux安全加固

# 3-5 Linux安全加固

### 一、检查是否存在空密码账户 

|步骤|描述|命令
|------
|检测步骤|检查是否存在空密码账户|`awk -F: '($2==""){print $1}' /etc/shadow`
|合规性判定|如果步骤1返回值为空，则符合要求；如果步骤1返回值不为空，则存在空密码账户|-
<td colspan="1" rowspan="2">加固步骤</td>|备份`/etc/shadow`文件|`cp /etc/shadow /etc/shadow_bak`
|删除空密码账户|`userdel &lt;用户名&gt;`
|或 为空密码账户设置密码|`passwd &lt;用户名&gt;`

#### 演示&amp;#x
