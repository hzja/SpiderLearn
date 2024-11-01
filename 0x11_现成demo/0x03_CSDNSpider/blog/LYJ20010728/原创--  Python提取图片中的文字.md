# 原创
：  Python提取图片中的文字

# Python提取图片中的文字

#### Python提取图片中的文字

## 相关依赖库安装

```
pip install PIL
pip install pytesseract

```

## OCR工具安装

> 
[下载链接](https://share.weiyun.com/a8ZdP3SP)


> 
修改 pytesseract 源码中的路径，将 `tesseract_cmd` 的值改为安装Tesseract-OCR应用程序路径


<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/44156480a09c4962b66c36346e870729.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/3b174f45c2724723ab76ecf9107197f4.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>

> 
安装识别中文所需依赖库，[下载链接](https://share.weiyun.com/OIhJORlG)<br/> 将下载的中文库放在 Tesseract-OCR 安装目录下的 tessdata 文件夹中


## 识别代码

```
import pytesseract
from PIL import Image
 
img_en = Image.open(r'C:\Users\95235\Downloads\misc1\misc1.png')
img_ch = Image.open(r'C:\Users\95235\Downloads\misc1\misc1.png')
 
print('========识别字母========')
print(pytesseract.image_to_string(img_en))
 
print('========识别中文========')
print(pytesseract.image_to_string(img_ch, lang='chi_sim'))

```

<img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/36a9e8585ac3457093f309987ddd0e5a.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/><br/> <img alt="在这里插入图片描述" src="https://img-blog.csdnimg.cn/ff67fc71b18048dea187b64ae953ab80.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xZSjIwMDEwNzI4,size_16,color_FFFFFF,t_70#pic_center"/>
