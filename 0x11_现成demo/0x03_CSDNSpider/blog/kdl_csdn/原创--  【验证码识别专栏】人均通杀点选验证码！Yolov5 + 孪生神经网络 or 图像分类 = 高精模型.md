# 原创
：  【验证码识别专栏】人均通杀点选验证码！Yolov5 + 孪生神经网络 or 图像分类 = 高精模型

# 【验证码识别专栏】人均通杀点选验证码！Yolov5 + 孪生神经网络 or 图像分类 = 高精模型

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

近期有群友反馈，不知道如何训练点选验证码，之前也有不少粉丝问过相关问题，众所周知，K哥一向会尽力满足粉丝们的需求，现在特此推出《验证码识别专栏》，今后将输出相关文章，充实知识体系：

### 孪生神经网络简介

简单来说，孪生神经网络（Siamese network）就是“连体的神经网络”，神经网络的“连体”是通过共享权值来实现的，如下图所示 ：

孪生神经网络是一种特殊的神经网络结构，由两个或多个相同的子网络组成，这些子网络共享相同的权重和参数。其设计灵感来源于孪生兄弟或姐妹之间的相似性。孪生神经网络主要用于解决比较和相似性度量的问题。它可以将两个输入进行比较，并输出一个度量值，表示它们之间的相似性或差异程度。通俗来说，就是不同的人写了同一个汉字，将其中随机的二者拿出来进行对比，判断他们写的是不是同一个汉字，原理就是通过一个神经网络进行特征提取再进行比较， 通过 Loss 的计算，评价两个输入的相似度 。大家可以简单了解一下它的大致过程：

#### 孪生网络中的 LOSS 计算

对于孪生神经网络而言，其具有两个输入。

当两个输入指向同一个类型的图片时，此时标签为 1。

当两个输入指向不同类型的图片时，此时标签为 0。

然后将网络的输出结果和真实标签进行交叉熵运算，就可以作为最终的 loss 了。

比如，当我们输入下面俩个的时候，我们希望网络给我们输出 1：

<img alt="7mS0XO.jpg" src="https://i-blog.csdnimg.cn/blog_migrate/d4f281fa2472e03edfce787fc0ff7a52.jpeg"/> <img alt="7mSlmQ.png" src="https://i-blog.csdnimg.cn/blog_migrate/a5ec1dcb3f8dd54b08a8b4bc8035efda.png"/>

当我们输入以下俩个的时候，我们希望网络给我们输出 0：

<img alt="7mSErc.jpg" src="https://i-blog.csdnimg.cn/blog_migrate/9ba9397a796ca3373cf2adbeb16dece6.jpeg"/> <img alt="7mS7hf.png" src="https://i-blog.csdnimg.cn/blog_migrate/0b531a7b414e1d40aa54455bfe4c7e18.png"/>

当输出 0 或者 1 的时候，我们将会与预测结果求交叉熵，进而输出相似度，这便是孪生神经网络的奇妙之处。

### YOLO目标检测

YOLO 是目标检测模型。 目标检测是计算机视觉中比较简单的任务，用来在一张图篇中找到某些特定的物体。附上一张图，让大家直观的感受一下：

YOLO 检测速度非常快。因为检测问题是回归问题，所以不需要复杂的管道。它比 “R-CNN” 快 1000 倍，比 “Fast R-CNN” 快 100 倍。

YOLO 能够处理实时视频，延迟非常小，连 25 毫秒都不到。精度也是以前实时系统的 2 倍多。更为重要的是 YOLO 遵循“端到端深度学习”的实践。

### CNN 图像分类

在计算机视觉中，我们有一个卷积神经网络，它非常适用于计算机视觉任务，例如图像分类、对象检测、图像分割等等。卷积神经网络 (CNN)是一种用于处理图像的神经网络，这种类型的神经网络从图像中获取输入并从图像中提取特征，并提供可学习的参数以有效地进行分类、检测和更多任务。

我们使用称为“过滤器”的东西从图像中提取特征，我们使用不同的过滤器从图像中提取不同的特征。让我们举个例子，你正在构建一个分类模型来检测图像是猫还是非猫。因此，我们有不同的过滤器用于从图像中提取不同的特征，从而识别他是什么。所以大家可以把他理解成 OCR，输入一张图像，返回图像类别。

好了，大家对这 3 个东西相信也有一定的了解了，怎么使用，那我们就用实例来给大家讲解一下他们怎么使用。

### 点选验证码处理思路

我们附上几张，我们常见点选类验证码：

背景图的话千篇一律，没有什么区分，相比而言，对于点选问题，不同站点的验证码是不同的，基本有以下几类，我们通过不同的类别，来浅谈以下不同类型的点选我们应该如何处理。

#### 类型一：yolo+CNN

① 有些网站的题目是在接口中返回 例如 `wordList': ['并', '细', '什']` 这样的话，就很简单，我们把他从数组中取出来，就可以得到问题的答案。现在我们已经拿到了问题，就需要在图片中找到对应文字的坐标。我们这里采用 yolo+CNN（ddddocr），利用 labelimg 标注数据集生成 yolo 格式，labelimg 的安装：

```
pip install labelimg

```

新建 2 个文件夹：一个是存放图片的目录，另一个存放标签 class 的目录。

cmd 继续输入 labelimg 即可进入标注首页，按照下图片进行设置：<img alt="7m1MOj.png" src="https://i-blog.csdnimg.cn/blog_migrate/40db651dbbdbbbc2824e68076dcf4b78.png"/><br/> <img alt="7m1fi5.png" src="https://i-blog.csdnimg.cn/blog_migrate/d6feb1fc9e50d0d09cca9595fa7ef6b1.png"/>

标注的类名用英文，或者数字，这里我们只需要做文字检测，所以类名都写成 1 就可以了。标注完成会在你新建的目录下生成 class.txt 文件。

yolov5 下载地址：

> 
https://codeload.github.com/ultralytics/yolov5/zip/refs/heads/master


下载好以后，导入 pycharm，打开 train.py，找到 data 这个位置，这是训练集的配置文件，上面显示 data/coco128.yaml：

按照指定要求放我们的数据集，整体的路径框架就是这个样子，保存 yaml 配置文件与数据集存放位置一致就可以了。我们刚刚标注的导出的txt文件夹和原图文件夹按照下图去对应存放就可以，一定要与yaml保持一致

走到这一步，我们的数据准备工作就完成了，接下来我们把我们 yolo 总文件夹打包，然后上传到 Auto 算力云平台（地址：https://www.autodl.com）去租用 gpu 去训练，（也自己本地可以安装 conda，安装 pytorch 去配置环境去训练，如何配置环境网上有教程，但是对电脑性能有一定要求，且很多框架要求必须是 N 卡），这里笔者为了所有人都可以训练，选择算力云平台去训练，这也是笔者平时为了节省效率采用的方式。

##### 模型训练

进入以后，我们选择 T 卡即可，环境配置如下：

选择 1.x 的版本都可以，推荐 1.7.0，创建以后我们进入即可，进入以后选择终端，输入 source /etc/network_turbo 回车进行镜像加速，然后输入指令，`pip install -r requirements.txt` 进行相关库的安装，如果遇上安装不上的，手动安装即可，和 win 的操作基本一致，我们所需的库安装完以后，敲入 python3 train.py 即可开始训练，训练完成会导出 pt 模型。

我们自己编写代码进行预测，这里咱已经贴心的写成接口形式了：

```
# 实例化 flask
app = Flask(__name__)
docr = solve()

# 设置路由和处理函数（异步处理）
@app.route("/ocr", methods=["POST"])
def shibie():
    data = request.get_data().decode("utf-8")
    data = json.loads(data)
    # BASE64 图片
    beijing_data = data["beijing"]

    beijing_bytes = base64.b64decode(beijing_data)
    beijing_image = Image.open(BytesIO(beijing_bytes))

    results = model(beijing_image)
    boxes = results.xyxy[0][:, :4].tolist()
    output = []
    for box in boxes:
        x1, y1, x2, y2 = box
        output.append([int(x1), int(y1), int(x2), int(y2)])

   
    return output


if __name__ == "__main__":
    # 导入 yolov5 模型定义和权重
    # 加载 yolo 模型
    luansheng = Siamese()
    model = torch.hub.load("./", "custom", path="best2.pt", source="local")
    model.conf = 0.5
    app.run(host="0.0.0.0", threaded=True, processes=1)

```

上面代码会给你一组数组，是图片上每个检测对象的左上坐标和左下坐标，你可以用它来求中心坐标~

当然，网上很多人会教你转成 onnx 去运行，下面教大家如何转成 onnx 模型，并且推理：

pt 模型转 onnx 模型代码 1（网传）

```
from ultralytics import YOLO
model = YOLO(r"suixin.pt")
model.export(format="onnx",imgsz=320,simplify=True)

```

pt 模型转 onnx 模型代码 2（本人在用的方式）

yolo 官方其他给我们已经准备好了转换的文件，我们进入我们下载的 yolo5 文件夹中，找到 export.pt：

找到这三个位置，第一个位置一定不陌生，就是我们训练的时候已经配置好的那个文件，第二个就是我们训练结束以后的 pt 模型，第三个是选择导出的类型，我们这里输入 onnx 模型就行。

onnx 模型预测代码 1（网传，自测，大部分人跑不起来，可能第一步用别人的代码转就没转好）：

```
from ultralytics import YOLO
model = YOLO(r"best2.onnx")
res = model.predict(source=r"bg1.jpg",show=False,save=True,imgsz=300)

```

onnx 模型预测代码 2（笔者本人在用的方式）这里如果要接口调用，自己仿照上面的格式去修改即可：

```
import os
import cv2
import time
import numpy as np
import onnxruntime

# coco80 类别
CLASSES = ['1'] 

class YOLOV5:
    def __init__(self,onnxpath):
        self.onnx_session = onnxruntime.InferenceSession(onnxpath)
        self.input_name = self.get_input_name()
        self.output_name = self.get_output_name()
    #-------------------------------------------------------
    #   获取输入输出的名字
    #-------------------------------------------------------
    def get_input_name(self):
        input_name = []
        for node in self.onnx_session.get_inputs():
            input_name.append(node.name)
        return input_name
    def get_output_name(self):
        output_name = []
        for node in self.onnx_session.get_outputs():
            output_name.append(node.&lt;/
```
