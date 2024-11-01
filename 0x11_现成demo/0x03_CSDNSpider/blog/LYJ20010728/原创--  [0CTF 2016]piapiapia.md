# 原创
：  [0CTF 2016]piapiapia

# [0CTF 2016]piapiapia

#### [0CTF 2016]piapiapia

## 考点

> 
数组绕过、PHP反序列化字符逃逸


## 思路

> 
页面是一个登录框，弱密码爆破试了下没得用，扫描一下网站发现register.php，登录注册<br/> 用python扫描了一下备份文件，发现存在www.zip<br/> 在profile.php文件中有一个很明显的可以读文件的地方`$photo = base64_encode(file_get_contents($profile['photo']));`，并且`$profile`变量是经过反序列化的。那么现在的目标就是要把`$profile['photo']`的值替换成`config.php`，update.php中可以控制`$profile`变量。主要是下面这一段代码：


```
$profile['phone'] = $_POST['phone'];
$profile['email'] = $_POST['email'];
$profile['nickname'] = $_POST['nickname'];
$profile['photo'] = 'upload/' . md5($file['name']);
 
$user-&gt;update_profile($username, serialize($profile));
echo 'Update Profile Success!&lt;a href="profile.php"&gt;Your Profile&lt;/a&gt;';

```

> 
传入了数组中这四个值，然后将数组序列化后带入user类中的update_profile方法中从而更改表信息。然后我们查看内容时会在profile.php中反序列化后返回给我们要看的信息。再去看一下update_profile函数：


```
public function update_profile($username, $new_profile) {
		$username = parent::filter($username);
		$new_profile = parent::filter($new_profile);

		$where = "username = '$username'";
		return parent::update($this-&gt;table, 'profile', $new_profile, $where);
	}

public function filter($string) {
		$escape = array('\'', '\\\\');
		$escape = '/' . implode('|', $escape) . '/';
		$string = preg_replace($escape, '_', $string);

		$safe = array('select', 'insert', 'update', 'delete', 'where');
		$safe = '/' . implode('|', $safe) . '/i';
		return preg_replace($safe, 'hacker', $string);
	}

```

> 
这是一个防止sql注入的方法，其中他将上面五个sql关键字替换为了hacker，看起来没什么问题，但这却是我们最重要的利用点，我们可以利用这个点来实现字符逃逸<br/> 首先我们看一下一个正常的$profile经过序列化后是什么样子：


```
$profile = a:4:{s:5:"phone";s:11:"12345678901";s:5:"email";s:8:"ss@q.com";s:8:"nickname";s:5:"ca01h";s:5:"photo";s:10:"config.php";}s:39:"upload/804f743824c0451b2f60d81b63b6a900";}

```

> 



> 
由于数组绕过长度检测，下面的这个preg_math可以用数组绕过：


```
if(preg_match('/[^a-zA-Z0-9_]/', $_POST['nickname']) || strlen($_POST['nickname']) &gt; 10)
	die('Invalid nickname');

```

## Payload

> 
config.php内容


```
&lt;?php
	$config['hostname'] = '127.0.0.1';
	$config['username'] = 'root';
	$config['password'] = '';
	$config['database'] = '';
	$flag = '';
?&gt;

```

> 
class.php内容


```
&lt;?php
require('config.php');

class user extends mysql{
	private $table = 'users';

	public function is_exists($username) {
		$username = parent::filter($username);

		$where = "username = '$username'";
		return parent::select($this-&gt;table, $where);
	}
	public function register($username, $password) {
		$username = parent::filter($username);
		$password = parent::filter($password);

		$key_list = Array('username', 'password');
		$value_list = Array($username, md5($password));
		return parent::insert($this-&gt;table, $key_list, $value_list);
	}
	public function login($username, $password) {
		$username = parent::filter($username);
		$password = parent::filter($password);

		$where = "username = '$username'";
		$object = parent::select($this-&gt;table, $where);
		if ($object &amp;&amp; $object-&gt;password === md5($password)) {
			return true;
		} else {
			return false;
		}
	}
	public function show_profile($username) {
		$username = parent::filter($username);

		$where = "username = '$username'";
		$object = parent::select($this-&gt;table, $where);
		return $object-&gt;profile;
	}
	public function update_profile($username, $new_profile) {
		$username = parent::filter($username);
		$new_profile = parent::filter($new_profile);

		$where = "username = '$username'";
		return parent::update($this-&gt;table, 'profile', $new_profile, $where);
	}
	public function __tostring() {
		return __class__;
	}
}

class mysql {
	private $link = null;

	public function connect($config) {
		$this-&gt;link = mysql_connect(
			$config['hostname'],
			$config['username'], 
			$config['password']
		);
		mysql_select_db($config['database']);
		mysql_query("SET sql_mode='strict_all_tables'");

		return $this-&gt;link;
	}

	public function select($table, $where, $ret = '*') {
		$sql = "SELECT $ret FROM $table WHERE $where";
		$result = mysql_query($sql, $this-&gt;link);
		return mysql_fetch_object($result);
	}

	public function insert($table, $key_list, $value_list) {
		$key = implode(',', $key_list);
		$value = '\'' . implode('\',\'', $value_list) . '\''; 
		$sql = "INSERT INTO $table ($key) VALUES ($value)";
		return mysql_query($sql);
	}

	public function update($table, $key, $value, $where) {
		$sql = "UPDATE $table SET $key = '$value' WHERE $where";
		return mysql_query($sql);
	}

	public function filter($string) {
		$escape = array('\'', '\\\\');
		$escape = '/' . implode('|', $escape) . '/';
		$string = preg_replace($escape, '_', $string);

		$safe = array('select', 'insert', 'update', 'delete', 'where');
		$safe = '/' . implode('|', $safe) . '/i';
		return preg_replace($safe, 'hacker', $string);
	}
	public function __tostring() {
		return __class__;
	}
}
session_start();
$user = new user();
$user-&gt;connect($config);

```

> 
profile.php内容


```
&lt;?php
	require_once('class.php');
	if($_SESSION['username'] == null) {
		die('Login First');	
	}
	$username = $_SESSION['username'];
	$profile=$user-&gt;show_profile($username);
	if($profile  == null) {
		header('Location: update.php');
	}
	else {
		$profile = unserialize($profile);
		$phone = $profile['phone'];
		$email = $profile['email'];
		$nickname = $profile['nickname'];
		$photo = base64_encode(file_get_contents($profile['photo']));
?&gt;
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
   &lt;title&gt;Profile&lt;/title&gt;
   &lt;link href="static/bootstrap.min.css" rel="stylesheet"&gt;
   &lt;script src="static/jquery.min.js"&gt;&lt;/script&gt;
   &lt;script src="static/bootstrap.min.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
	&lt;div class="container" style="margin-top:100px"&gt;  
		&lt;img src="data:image/gif;base64,&lt;?php echo $photo; ?&gt;" class="img-memeda " style="width:180px;margin:0px auto;"&gt;
		&lt;h3&gt;Hi &lt;?php echo $nickname;?&gt;&lt;/h3&gt;
		&lt;label&gt;Phone: &lt;?php echo $phone;?&gt;&lt;/label&gt;
		&lt;label&gt;Email: &lt;?php echo $email;?&gt;&lt;/label&gt;
	&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
&lt;?php
	}
?&gt;

```

> 
update.php内容


```
&lt;?php
	require_once('class.php');
	if($_SESSION['username'] == null) {
		die('Login First');	
	}
	if($_POST['phone'] &amp;&amp; $_POST['email'] &amp;&amp; $_POST['nickname'] &amp;&amp; $_FILES['photo']) {

		$username = $_SESSION['username'];
		if(!preg_match('/^\d{11}$/', $_POST['phone']))
			die('Invalid phone');

		if(!preg_match('/^[_a-zA-Z0-9]{1,10}@[_a-zA-Z0-9]{1,10}\.[_a-zA-Z0-9]{1,10}$/', $_POST['email']))
			die('Invalid email');
		
		if(preg_match('/[^a-zA-Z0-9_]/', $_POST['nickname']) || strlen($_POST['nickname']) &gt; 10)
			die('Invalid nickname');

		$file = $_FILES['photo'];
		if($file['size'] &lt; 5 or $file['size'] &gt; 1000000)
			die('Photo size error');

		move_uploaded_file($file['tmp_name'], 'upload/' . md5($file['name']));
		$profile['phone'] = $_POST['phone'];
		$profile['email'] = $_POST['email'];
		$profile['nickname'] = $_POST['nickname'];
		$profile['photo'] = 'upload/' . md5($file['name']);

		$user-&gt;update_profile($username, serialize($profile));
		echo 'Update Profile Success!&lt;a href="profile.php"&gt;Your Profile&lt;/a&gt;';
	}
	else {
?&gt;
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
   &lt;title&gt;UPDATE&lt;/title&gt;
   &lt;link href="static/bootstrap.min.css" rel="stylesheet"&gt;
   &lt;script src="static/jquery.min.js"&gt;&lt;/script&gt;
   &lt;script src="static/bootstrap.min.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
	&lt;div class="container" style="margin-top:100px"&gt;  
		&lt;form action="update.php" method="post" enctype="multipart/form-data" class="well" style="width:220px;margin:0px auto;"&gt; 
			&lt;img src="static/piapiapia.gif" class="img-memeda " style="width:180px;margin:0px auto;"&gt;
			&lt;h3&gt;Please Update Your Profile&lt;/h3&gt;
			&lt;label&gt;Phone:&lt;/label&gt;
			&lt;input type="text" name="phone" style="height:30px"class="span3"/&gt;
			&lt;label&gt;Email:&lt;/label&gt;
			&lt;input type="text" name="email" style="height:30px"class="span3"/&gt;
			&lt;label&gt;Nickname:&lt;/label&gt;
			&lt;input type="text" name="nickname" style="height:30px" class="span3"&gt;
			&lt;label for="file"&gt;Photo:&lt;/label&gt;
			&lt;input type="file" name="photo" style="height:30px"class="span3"/&gt;
			&lt;button type="submit" class="btn btn-primary"&gt;UPDATE&lt;/button&gt;
		&lt;/form&gt;
	&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
&lt;?php
	}
?&gt;

```

> 
注册账号登录成功后抓包修改信息


> 
profile.php查看读取的文件


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210525230954990.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210525231048687.png#pic_center"/>
