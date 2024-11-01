# 原创
：  【PHP特性-变量覆盖】函数的使用不当、配置不当、代码逻辑漏洞

# 【PHP特性-变量覆盖】函数的使用不当、配置不当、代码逻辑漏洞

 **目录**

[一、总述](#%E4%B8%80%E3%80%81%E6%80%BB%E8%BF%B0)

[发现方法：](#%E5%8F%91%E7%8E%B0%E6%96%B9%E6%B3%95%EF%BC%9A)

[产生原因：](#%E4%BA%A7%E7%94%9F%E5%8E%9F%E5%9B%A0%EF%BC%9A)

[利用：](#%E5%88%A9%E7%94%A8%EF%BC%9A)

[使用场景：](#%E4%BD%BF%E7%94%A8%E5%9C%BA%E6%99%AF%EF%BC%9A)

[二、extract函数](#%E4%BA%8C%E3%80%81extract%E5%87%BD%E6%95%B0)

[语法：](#%E8%AF%AD%E6%B3%95%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[三、parse_str函数](#%E4%B8%89%E3%80%81parse_str%E5%87%BD%E6%95%B0)

[语法：](#%E8%AF%AD%E6%B3%95%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[四、import_request_variables函数](#%E5%9B%9B%E3%80%81import_request_variables%E5%87%BD%E6%95%B0)

[语法：](#%E8%AF%AD%E6%B3%95%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[五、配置不当](#%E4%BA%94%E3%80%81%E9%85%8D%E7%BD%AE%E4%B8%8D%E5%BD%93)

[前提：](#%E5%89%8D%E6%8F%90%EF%BC%9A)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

[六、代码逻辑漏洞](#%E5%85%AD%E3%80%81%E4%BB%A3%E7%A0%81%E9%80%BB%E8%BE%91%E6%BC%8F%E6%B4%9E)

[$$导致的变量覆盖](#%24%24%E5%AF%BC%E8%87%B4%E7%9A%84%E5%8F%98%E9%87%8F%E8%A6%86%E7%9B%96)

[示例：](#%E7%A4%BA%E4%BE%8B%EF%BC%9A)

---


> 
<h2>一、总述</h2>
<h3>发现方法：</h3>
代码审计
<hr/>
<h3>产生原因：</h3>
函数的使用不当、配置不当、代码逻辑漏洞
<hr/>
<h3>利用：</h3>
通过前端传入的值去覆盖程序中的局部变量或全局变量，从而达到变量覆盖
<hr/>
<h3>使用场景：</h3>
$$ 使用不当
extract() 、parse_str() 函数使用不当
import_request_variables() 使用不当，开启了全局变量注册(PHP 4 &gt;= 4.1.0, PHP 5 &lt; 5.4.0)
……


### 产生原因：

---


### 使用场景：

---


---


## 二、extract函数

> 
<h3>语法：</h3>
extract(**array**,**extract_rules**,**prefix**)
<table border="1" cellpadding="1" cellspacing="1"><tbody>|参数|描述
|**array**|必需。规定要使用的数组。
<tr>|**extract_rules**<td> 可选。extract() 函数将检查每个键名是否为合法的变量名，同时也检查和符号表中已存在的变量名是否冲突。对不合法和冲突的键名的处理将根据此参数决定。 可能的值：
</td></tr>|**prefix**| 可选。请注意 **prefix** 仅在 **extract_type** 的值是 EXTR_PREFIX_SAME，EXTR_PREFIX_ALL，EXTR_PREFIX_INVALID 或 EXTR_PREFIX_IF_EXISTS 时需要。如果附加了前缀后的结果不是合法的变量名，将不会导入到符号表中。 前缀和数组键名之间会自动加上一个下划线。 
</tbody></table>
<hr/>
<h3>示例：</h3>
&lt;?php<br/>         $a = false;<br/>         extract($_GET);<br/>         if ($a) {<br/>         echo "flag{...}";<br/>         } else {<br/>         echo "……";<br/>         }<br/> ?&gt;
extract函数将GET传入的数据转换为变量名和变量的值<br/> 输入?a=1可将$a的值变为true-----&gt;获得flag


### 示例：

---


---


## 三、parse_str函数

> 
<h3>语法：</h3>
parse_str(**string**,**array**)
<table border="1" cellpadding="1" cellspacing="1"><tbody>|参数|描述
|**string**|必需。规定要解析的字符串。
|**array**|可选。规定存储变量的数组的名称。该参数指示变量将被存储到数组中。
</tbody></table>
未设置 array 参数，由该函数设置的变量将覆盖已存在的同名变量
parse_str函数的作用是解析字符串并注册成变量
在注册变量之前不会验证当前变量是否存在，直接覆盖掉已有变量
也就是把输入的字符串变成变量
<hr/>
<h3>示例：</h3>
&lt;?php<br/>         $a = false;<br/>         parse_str($_SERVER['QUERY_STRING']);<br/>         if ($a) {<br/>         echo "flag{...}";<br/>         } else {<br/>         echo "……";<br/>         }<br/> ?&gt;

输入?a=1


### 示例：

---


---


## 四、import_request_variables函数

> 
<h3>语法：</h3>
bool import_request_variables ( string $types [, string $prefix ] )
<table border="1" cellpadding="1" cellspacing="1"><tbody>|参数|描述
|**$types**|指定需要导入的变量，可以用**字母 G、P 和 C 分别表示 GET、POST 和 Cookie**，这些字母不区分大小写，所以你可以使用 g 、 p 和 c 的任何组合。POST 包含了通过 POST 方法上传的文件信息。**注意这些字母的顺序，当使用 gp 时，POST 变量将使用相同的名字覆盖 GET 变量**。任何 GPC 以外的字母都将被忽略
|**$prefix**|变量名的前缀，置于所有被导入到全局作用域的变量之前。所以如果你有个名为 userid 的 GET 变量，同时提供了 pref_ 作为前缀，那么你将获得一个名为 $pref_userid 的全局变量。虽然 prefix 参数是可选的，但如果不指定前缀，或者指定一个空字符串作为前缀，你将获得一个 E_NOTICE 级别的错误
</tbody></table>

PHP 4 &gt;= 4.1.0, PHP 5 &lt; 5.4.0
<hr/>
<h3>示例：</h3>
&lt;?php<br/>         $a = false;<br/>         import_request_variables('G');<br/>         if ($a) {<br/>         echo "flag{...}";<br/>         } else {<br/>         echo "……";<br/>         }<br/> ?&gt;

排在前面的会覆盖排在后面的字符传入参数的值，若为“GP”，且GET和POST同时传入了a参数，则POST传入的a会被忽略


### 示例：

---


---


## 五、配置不当

> 
<h3>前提：</h3>
当PHP配置register_globals=ON时，利用register_globals的特性，复现全局变量覆盖漏洞
<hr/>
<h3>示例：</h3>
&lt;?php<br/>         if ($a) {<br/>         echo "flag{...}";<br/>         } else {<br/>         echo "……";<br/>         }<br/> ?&gt;

用户传入参数auth=1即可进入if语句块
如果在if语句前初始化$a变量，就不会触发了


### 示例：

---


---


## 六、代码逻辑漏洞

> 
<h3>$$导致的变量覆盖</h3>
$$（可变变量）
一个变量的变量名可以动态的设置和使用
这个可变变量获取了一个普通变量的值作为这个可变变量的变量名

&lt;?php<br/> $a="hello";
        //赋值
$$a="everybody";
        //使a变量的值作为变量名
echo "$a ${$a}";
        //输出：hello everybody
echo "$a $hello";
        //同样输出：hello everybody<br/> ?&gt;
<hr/>
<h3>示例：</h3>
&lt;?php<br/>         $a = false;<br/>         foreach($_GET as $key =&gt; $value){<br/>         $$key = $value;<br/>         }<br/>         if ($a) {<br/>         echo "flag{...}";<br/>         } else {<br/>         echo "……";<br/>         }<br/> ?&gt;

通过foreach循环遍历数组（如，$_GET、$_POST等），这里将GET传入的参数注册为变量，用户输入“?auth=1”就又成功绕过了判断，获得了flag


### 示例：
