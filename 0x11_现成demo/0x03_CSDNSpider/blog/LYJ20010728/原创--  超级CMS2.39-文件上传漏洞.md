# 原创
：  超级CMS2.39-文件上传漏洞

# 超级CMS2.39-文件上传漏洞

#### 超级CMS2.39-文件上传漏洞

## 环境搭建

> 
- 下载超级CMS V2.39，[下载地址](http://www.chaojicms.com/)- 使用phpstudy搭建web环境- 把下载好的源码放到网站根目录下，开启phpstudy，浏览器访问安装后即可


## 漏洞复现

### 上传点一

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621010029483.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621010034844.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621010041484.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### 上传点二

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621010053328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621010058971.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621010104883.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

### 上传点三

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621010135262.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/2021062101014269.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/20210621010147691.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

## 漏洞分析

> 
存在漏洞的位置`file.class.php`文件中的`getFileExtName`方法


```
public function getFileExtName($filename){
	$filename = strtolower($filename);
		$exts = explode('.',$filename);
		$ext = $exts[count($exts)-1];
		if(strpos($ext,'?') &gt;= 0){
			$ext = explode('?',$ext);
			return $ext[0];
		}
		else
		return $ext;
	}

```

> 
取其中一个图片上传模块为例子，利用位于`webset.master.php`文件中的`setweb`方法


```
private function setweb(){
		$Lang=$this-&gt;G-&gt;loadLang();
		if($_SESSION['input_token']!="" &amp;&amp; $_SESSION['input_token']==$_POST['input_token']){
			$_SESSION['input_token']='';
			$dsw =$_POST['dsw'];
			if($dsw){
                if(is_uploaded_file($_FILES['file']['tmp_name'])){
                    $sfile=$_FILES["file"];
                    $dsw['web_logo']=$this-&gt;files-&gt;uploadFile($sfile,UPLOAD_PATH_IMG);
                }
                if(is_uploaded_file($_FILES['file_ewm']['tmp_name'])){
                    $sfile=$_FILES["file_ewm"];
                    $dsw['web_erweima']=$this-&gt;files-&gt;uploadFile($sfile,UPLOAD_PATH_IMG);
                }
				foreach($dsw as $k=&gt;$v){
					$this-&gt;webconfig-&gt;update(array('value'=&gt;$v),array('varname'=&gt;$k));
				}
				$message = array(
					'CodeType' =&gt;300,
					"message" =&gt; $Lang['set']['UpdateSuccess'],
					"callbackType" =&gt; 'forward',
					"forwardUrl" =&gt; ADMIN_URL."webset"	
				);
				$this-&gt;G-&gt;R($message);
			}
		}else{
			$ListAll=$this-&gt;webconfig-&gt;getAll();
			if($ListAll){
				$ListOne=array();
				foreach($ListAll as $k=&gt;$v){
					$ListOne[$v['varname']]=$v['value'];
				}
				$this-&gt;tpl-&gt;assign("FormTitle",$Lang['set']['FormTitle']);
				$this-&gt;tpl-&gt;assign('ListOne',$ListOne);
				$_SESSION['input_token'] = md5(rand(100,1000));
				$this-&gt;tpl-&gt;assign("input_token",$_SESSION['input_token']);
				$this-&gt;tpl-&gt;assign("FormAction",ADMIN_URL."webset-setweb");
				$this-&gt;tpl-&gt;assign("Lang",$Lang);
				$this-&gt;tpl-&gt;display('webset');
			}
		}
	}

```

> 
跟进uploadFile方法


```
public function uploadFile($file,$updir,$sExtension = NULL,$name = NULL){
		if(!$sExtension)$sExtension = $this-&gt;getFileExtName($file['name']);
		if(!$name)$name = time().rand(1000,9999);
		if(!file_exists('.'.$updir))$this-&gt;mdir('.'.$updir);
		$url = $updir.$name.'.'.$sExtension;
		if(file_exists($url))unlink($url);
		move_uploaded_file($file['tmp_name'],'.'.$url);
		if (file_exists($url)){
			$oldumask = umask(0);
			chmod($url,0777);
			umask($oldumask);
		}
		return $url;
	}

```

> 
我们发现，这里调用`getFileExtName`方法获取文件扩展名，但这里并没有做严格的过滤，所以导致可以通过直接上传`1.jpg.php`来达到getshell的目的

