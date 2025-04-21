# 原创
：  【验证码识别专栏】今天不炼丹，用 cv 来秒验证码

# 【验证码识别专栏】今天不炼丹，用 cv 来秒验证码

### 声明

**本文章中所有内容仅供学习交流使用，不用于其他任何目的，不提供完整代码，抓包内容、敏感网址、数据接口等均已做脱敏处理，严禁用于商业用途和非法用途，否则由此产生的一切后果均与作者无关！**

**本文章未经许可禁止转载，禁止任何修改后二次传播，擅自使用本文讲解的技术而导致的任何意外，作者均不负责，若有侵权，请在公众号【K哥爬虫】联系作者立即删除！**

### 前言

最近查看 QQ 群消息，无意间看到了粉丝们关于 opencv 的相关讨论，有热心的群友给出了大致的解决方向。同时也有很多星球伙伴，在星球分享关于验证码识别的相关知识，学习交流的氛围很好。本文就针对提问和已经存在的主题做一期总结与答疑，也是丰富验证码识别类型的相关文章：

### 分析目标

### 初识乾坤

首先我们来分析一下粉丝提到的站点 1，该站的查询接口返回的验证码图片如下：

上图分别是一张缺口图与一张完整的图像，这种类型在滑块中还是比较好处理的，完全可以利用 `absdiff` 来完成。在图像处理和计算机视觉领域，计算图像之间的差异是一项基本的任务。这种差异可以帮助我们识别图像中的变化、运动对象或者进行图像配准等。在 OpenCV 库中，`absdiff` 函数提供了一种高效的方式来计算两个图像之间的绝对差值：

|**特性**|**描述**
|------
|**函数名称**|`cv2.absdiff()`
|**参数**|`src1` 和 `src2`：两张要进行比较的图像，必须具有相同的尺寸和通道数。
|**返回值**|返回一张新的图像，其中每个像素值是 `src1` 和 `src2` 在对应位置的绝对差异。
|**图像类型**|支持灰度图像和彩色图像（RGB）。对于彩色图像，分别计算每个颜色通道的绝对差异。
|**常见用途**|1. 背景减除：检测视频中的运动物体；2. 图像对比：比较两张图像是否相似；3. 图像变化检测：找出图像间的变化。
|**应用场景**|1. 运动检测：通过计算背景和当前帧之间的差异检测前景物体；2. 监控：背景与前景变化检测；3. 图像注册与对比。
|**性能特点**|快速计算两张图像之间的像素差异，适用于图像对比、背景减除等任务。

所以我们先将两张图像转为灰度，然后计算绝对差值，结果如下：

之后，使用 Canny 边缘检测提取边缘，最终使用轮廓查找，找到符合条件的轮廓即可，完整代码如下：

```
import cv2
import numpy as np


def detect_slider_gap_with_canny(original_path, with_hole_path):
    """
    使用 Canny 边缘检测法检测滑块验证码缺口位置，并返回滑块需要移动的 x 坐标值。

    参数:
        original_path (str): 原图路径（无缺口）。
        with_hole_path (str): 带缺口的图片路径。

    返回:
        int: 滑块需要移动的 x 坐标值。
    """
    # 读取图片（灰度模式）
    original = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
    with_hole = cv2.imread(with_hole_path, cv2.IMREAD_GRAYSCALE)

    # 检查两张图片是否大小一致
    if original.shape != with_hole.shape:
        raise ValueError("两张图片的尺寸不一致，请检查输入图片！")

    # 计算绝对差值
    diff = cv2.absdiff(original, with_hole)
    cv2.imshow("diff",diff)
    cv2.waitKey(0)

    # 使用 Canny 边缘检测提取边缘
    edges = cv2.Canny(diff, threshold1=50, threshold2=150)

    cv2.imshow("edges", edges)
    cv2.waitKey(0)

    # 查找边缘图中的轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历轮廓，找到缺口的 x 坐标
    for contour in contours:
        # 获取轮廓的边界矩形
        x, y, w, h = cv2.boundingRect(contour)

        # 假设缺口的宽度和高度有一定限制，筛选可能的缺口
        if 20 &lt; w &lt; 100 and 20 &lt; h &lt; 100:  # 根据具体验证码调整范围
            return x

    # 如果未检测到缺口
    raise ValueError("未能检测到缺口，请检查输入图片！")


# 示例用法
if __name__ == "__main__":
    original_path = "1.png"  # 原图路径
    with_hole_path = "2.png"  # 带缺口的图片路径

    try:
        slider_x = detect_slider_gap_with_canny(original_path, with_hole_path)
        print(f"滑块需要移动的 x 值: {slider_x}")
    except Exception as e:
        print(f"错误: {e}")

```

### 渐入佳境

给粉丝答疑完之后，我们再来看看星球成员最近分享的，稍微复杂点的案例，是关于差异点击类型的验证码。该验证码是基于给定的图像中，选择其中不同类型的图案或文字：

该类型的验证码如下图所示：

主要是利用 PCA 特征降维和余弦计算，关键代码如下：

```
def find_anomalous_image(images):
    # 提取所有图像的特征
    features = [extract_features(img) for img in images]

    # 设置 PCA 的 n_components 为样本数和特征数的最小值
    n_components = min(len(features), len(features[0]))
    pca = PCA(n_components=n_components)
    reduced_features = pca.fit_transform(features)

    # 计算余弦相似度
    similarity_matrix = cosine_similarity(reduced_features)
    average_similarity = np.mean(similarity_matrix, axis=1)

    # 找到平均相似度最低的图像索引
    anomalous_index = np.argmin(average_similarity)
    return anomalous_index

```

那么，借此思路我们同样也可以用其他办法来解决，既然图案有差异，那么我们可以通过模板匹配的结果来计算得分，同样还是遍历每个图案，求自身与其他图案的模板的得分平均值，最终还是利用 `np.argmin` 去得到平均相似度最低的字符索引，即可得到答案：

```
import cv2
import ddddocr
import numpy as np


# 初始化 ddddocr 检测器
det = ddddocr.DdddOcr(det=True, show_ad=False)

def cv_show(img):
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def preprocess_image(image):
    """
    对图像进行预处理：灰度化和二值化。
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return binary

def extract_cropped_regions(image_path):
    """
    从验证码图像中裁剪检测到的字符区域。

    :param image_path: 验证码图像路径
    :return: 裁剪后的字符图像列表和检测框坐标
    """
    original_image = cv2.imread(image_path)
    with open(image_path, 'rb') as f:
        image_data = f.read()
    poses = det.detection(image_data)  # 检测字符位置

    cropped_images = []
    for bbox in poses:
        x_min, y_min, x_max, y_max = bbox
        cropped = original_image[y_min:y_max, x_min:x_max]
        cropped_images.append((cropped, bbox))

    return cropped_images

def match_cropped_regions(cropped_images, threshold=0.8):
    """
    使用模板匹配比较裁剪的字符图像，找到异常字符。

    :param cropped_images: 裁剪的字符图像和其对应的检测框
    :param threshold: 模板匹配的相似度阈值
    :return: 异常字符的索引
    """
    num_images = len(cropped_images)
    similarity_scores = np.zeros((num_images, num_images))

    for i, (img1, _) in enumerate(cropped_images):
        for j, (img2, _) in enumerate(cropped_images):
            if i != j:
                # 预处理图像
                img1_processed = preprocess_image(img1)
                img2_processed = preprocess_image(img2)

                # 计算模板匹配得分
                result = cv2.matchTemplate(img1_processed, img2_processed, cv2.TM_CCOEFF_NORMED)
                # print(result)
                similarity_scores[i, j] = np.max(result)

    # 计算每个字符与其他字符的平均相似度
    print(similarity_scores)
    average_similarity = np.mean(similarity_scores, axis=1)
    print(average_similarity)

    # 找到平均相似度最低的字符索引
    anomalous_index = np.argmin(average_similarity)
    return anomalous_index

def main():
    # 输入验证码图像路径
    captcha_image_path = "1.png"  # 替换为你的验证码路径

    # 裁剪字符区域
    cropped_images = extract_cropped_regions(captcha_image_path)

    # cv_show(cropped_images)

    # 找到异常字符
    anomalous_index = match_cropped_regions(cropped_images)

    # 可视化结果
    original_image = cv2.imread(captcha_image_path)
    for i, (_, bbox) in enumerate(cropped_images):
        x_min, y_min, x_max, y_max = bbox
        color = (0, 255, 0) if i != anomalous_index else (0, 0, 255)  # 异常字符用红框标记
        cv2.rectangle(original_image, (x_min, y_min), (x_max, y_max), color, 2)

    # 保存并显示结果
    output_path = "output.png"
    cv2.imwrite(output_path, original_image)
    print(f"结果已保存到: {output_path}")

    # 显示结果
    cv2.imshow("Matched Result", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

```

依此类推，利用孪生 SiameseResNet50 网络，同样也可以不炼丹就解决该类型验证码， ResNet50 已经在大量的图像数据集（如 ImageNet）上训练过，预训练的 ResNet50 能提供非常好的性能，尤其是在图像分类、特征提取和其他计算机视觉任务中：

```
import cv2
import ddddocr

import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models

import numpy as np

# 使用 ddddocr 进行文字检测
det = ddddocr.DdddOcr(det=True, show_ad=False)

# 定义孪生网络模型
class SiameseResNet50(nn.Module):
    def __init__(self):
        super(SiameseResNet50, self).__init__()
        # 加载预训练的ResNet50模型
        resnet50 = models.resnet50(pretrained=True)
        # 去掉最后的全连接层
        self.resnet50 = nn.Sequential(*list(resnet50.children())[:-1])
        self.fc = nn.Sequential(
            nn.Linear(resnet50.fc.in_features, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
        )

    def forward_one(self, x):
        # 提取图像的特征
        x = self.resnet50(x)
        x = x.view(x.size(0), -1)  # Flatten
        x = self.fc(x)
        return x

    def forward(self, x1, x2):
        output1 = self.forward_one(x1)
        output2 = self.forward_one(x2)
        return output1, output2


# 提取图像特征
def extract_features(image, model, transform):
    image = cv2.resize(image, (224, 224))  # 调整为ResNet50的输入大小
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换为RGB格式
    image = transform(image).unsqueeze(0)  # 应用变换并添加batch维度
    model.eval()
    with torch.no_grad():
        feature = model.forward_one(image).numpy()
    return feature


# 找到异常图像
def find_anomalous_image(images, model, transform):
    # 提取所有图像的特征
    features = [extract_features(img, model, transform) for img in images]
    features = np.vstack(features)

    # 计算特征之间的欧几里得距离
    distance_matrix = np.linalg.norm(features[:, np.newaxis] - features[np.newaxis, :], axis=2)
    average_distance = np.mean(distance_matrix, axis=1)
    print(average_distance)

    # 找到具有最大平均距离的图像
    anomalous_index = np.argmax(average_distance)
    return anomalous_index


def main():
    # 加载预训练模型
    model = SiameseResNet50()
    # 定义图像变换
    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),  # Normalize RGB图像
    ])

    # 读取输入图像
    image_path = "1.png"  # 替换为您的图像路径
    original_image = cv2.imread(image_path)
    with open(image_path, 'rb') as f:
        image_data = f.read()
    poses = det.detection(image_data)

    # 裁剪检测到的区域
    cropped_images = []
    for bbox in poses:
        x_min, y_min, x_max, y_max = bbox
        cropped = original_image[y_min:y_max, x_min:x_max]
        cropped_images.append(cropped)

    # 找到最异常的图像
    anomalous_index = find_anomalous_image(cropped_images, model, transform)

    # 输出异常图像的坐标
    print(f"与其他不同的图像坐标为: {poses[anomalous_index]}")

    # 绘制矩形框，跳过最异常的图像
    for i, bbox in enumerate(poses):
        x_min, y_min, x_max, y_max = bbox
        color = (0, 255, 0) if i == anomalous_index else (0, 0, 255)  # 绿色表示异常，红色表示其他
        cv2.rectangle(original_image, (x_min, y_min), (x_max, y_max), color, 2)

    # 保存结果图像
    output_path = "output.png"
    cv2.imwrite(output_path, original_image)
    print(f"结果已保存到: {output_path}")


if __name__ == "__main__":
    main()

```

### 崭露头角

经过上文几轮介绍，我们已经拿下 2 种类型验证码的识别，这俩种应该算比较简单的，那么对于个别类型的验证码如果单单通过降维来提取主干特征，筛选正确答案，是远远不能满足要求的。比如上文的差异点击升级以后，便是**字体风格**类型验证码的识别，想从主干特征几乎一模一样的字体中筛选出正确答案，我们对特征的提取是需要叠加的，还要考虑文字的字体、笔画以及大小等等因素的影响，该类型的验证码如下图所示：

可以看到，此类验证码对于特征的提取，肯定不是单纯的模板匹配或者直接相似度就能解决的。换汤不换药，我们首先还是将图像转为灰度图，然后创建一个特征容器 features，用来存储特征集合。

#### 提取轮廓面积与周长

```
_, binary_image = cv2.threshold(inverted_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 轮廓面积与周长
if contours:
    largest_contour = max(contours, key=cv2.contourArea)
    contour_area = cv2.contourArea(largest_contour)
    contour_perimeter = cv2.arcLength(largest_contour, True)
    features.extend([contour_area, contour_perimeter])

    # 轮廓宽高比
    _, _, width, height = cv2.boundingRect(largest_contour)
    aspect_ratio = width / height
    features.append(aspect_ratio)
else:
    features.extend([0, 0, 0])  # 如果没有找到轮廓，添加 0

```

#### 笔画宽度提取

这类验证码最重要的特征就是笔画了，主要提取宽度均值和宽度标准差：

```
kernel = np.ones((3, 3), np.uint8)
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)
eroded_image = cv2.erode(binary_image, kernel, iterations=1)
stroke_width_map = dilated_image - eroded_image
stroke_width_mean = np.mean(stroke_width_map)
stroke_width_std = np.std(stroke_width_map)
features.extend([stroke_width_mean, stroke_width_std])

```

### 骨架提取

```
skeleton_image = skeletonize(binary_image &gt; 0)  # 先二值化，再进行骨架化
skeleton_length = np.sum(skeleton_image)
features.append(skeleton_length)

```

### 灰度统计与局部梯度

梯度统计主要用来求边缘强度，不同风格的字体边缘特征有时候有明显差别：

```
# 5. 灰度统计特征
mean_intensity = np.mean(gray_image)  # 灰度均值
std_intensity = np.std(gray_image)  # 灰度标准差
features.extend([mean_intensity, std_intensity])

# 6. 局部梯度分析（提取边缘强度）
gradient_x = cv2.Sobel(inverted_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(inverted_image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
gradient_mean = np.mean(gradient_magnitude)
gradient_std = np.std(gradient_magnitude)
features.extend([gradient_mean, gradient_std])

```

### 局部特征

局部特征主要用来提取字体形状和结构：

```
# 7. 局部特征（将图像分割为网格）
grid_size = 8  # 网格大小
cell_height, cell_width = resized_image.shape[0] // grid_size, resized_image.shape[1] // grid_size
local_grid_features = []

# 遍历每个网格，计算每个小区域的均值
for i in range(grid_size):
    for j in range(grid_size):
        cell = resized_image[i * cell_height:(i + 1) * cell_height, j * cell_width:(j + 1) * cell_width]
        local_grid_features.append(np.mean(cell))  # 计算网格单元的均值
        
features.extend(local_grid_features)

```

最终特征合并，计算相似性矩阵，回归上文相似度计算，继续计算均值，找到平均相似度最低的索引：

```
similarity_matrix = cosine_similarity(features)

# 计算每个图像与其他图像的平均相似度
average_similarity = np.mean(similarity_matrix, axis=1)
print("平均相似度:", average_similarity)

# 找到平均相似度最低的图像索引
anomalous_index = np.argmin(average_similarity)

```

最终效果如下：

### 行云流水

走到这里，已经对 3 种验证码进行了处理，最后我们来用 cv 处理一下旋转验证码，这种方法对于中小型网站，是足够使用的，相反对于 AI 类型的验证码也是一种处理办法，对于 AI 生成的旋转验证码，模型通常没有很好的泛性进行适配，如果模型可以一劳永逸，那么风控频繁的更新将毫无意义：

##### 感知哈希 (pHash) + 汉明距离

以某度验证码为例，图库有限的情况下，这不疑也是一种解决办法，处理思路就是通过将图片的主干特征提取出来，计算平均值，生成二进制哈希值，代码如下：

```
def phash(image):
    resized = cv2.resize(image, (32, 32), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    dct = cv2.dct(np.float32(gray))
    dct_low = dct[:8, :8]  # 提取左上角低频部分
    mean_val = np.mean(dct_low)
    hash_str = ''.join(['1' if x &gt; mean_val else '0' for x in dct_low.flatten()])
    return hash_str

```

通过读取转正的图像，将哈希值以列表的形式读出，最终存储在序列化文件中，格式如下：

```
['1010100001000000101000000010000010000000100000001000000000000000', '1011101000110010111000001010010010000001000000001000000000100010', '1010101100000000111010001000000010000000000000000000000000000000', '1110100000001100101000001000000010000000100000000000000000010000', '1010001010100010101000000000001000000010000010001000001000001000', '1110001100110000101110001100000010000000000000101000000000000000']

```

那么哈希值的对比就需要用到汉明距离了。

##### 汉明距离的基本原理

汉明距离是用于衡量两个等长字符串之间的相似程度的指标，它表示两个字符串对应位上不同字符的个数。用于计算两个哈希值的相似性。距离越小，图像越相似，反之则差异越大：

```
from scipy.spatial.distance import hamming

hash1 = "1100101011110000"
hash2 = "1100101011010000"
distance = hamming(list(hash1), list(hash2))  # 汉明距离
print(f"汉明距离: {distance}")

```

最终通过将待旋转的图片经过 360 度旋转计算哈希值，最后找到最相似的角度，即可完成旋转验证码的识别：

```
import cv2
import numpy as np

def rotate_image(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))

def find_best_angle(target_image, reference_image, step=1):
    target_hash = phash(target_image)
    best_angle, min_distance = 0, float('inf')
    for angle in range(0, 360, step):
        rotated = rotate_image(reference_image, angle)
        rotated_hash = phash(rotated)
        distance = hamming(list(target_hash), list(rotated_hash))
        if distance &lt; min_distance:
            best_angle, min_distance = angle, distance
    return best_angle

```

个别角度可能顺时针、逆时针不同，需要用 `360 - 计算出来的角度`。

更详细的代码可以参考热心网友已经整理好的 GitHub，方法大同小异：

> 
相关链接：https://github.com/decodecaptcha/Rotate-Captcha-Angle-Prediction


#### SIFT 特征匹配 + 仿射变换

##### SIFT 的基本原理

SIFT 是一种经典的特征提取算法，能提取图像的关键点及其局部特征，具有**旋转不变性**和**尺度不变性**，适用于旋转验证码中图像特征的匹配。

在标注阶段，首先需要准备一些已知的正确图像（即“转正”图像），这些图像的旋转角度是已知的。然后，通过计算这些图像的直方图特征，并将其保存到 **pkl 文件** 中，以便在后续的预测阶段使用：

```
import cv2
import pickle
import numpy as np

def calculate_histogram(image):
    # 计算图像的灰度直方图
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([grayscale_image], [0], None, [256], [0, 256])
    # 归一化直方图
    cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    return hist

def save_histograms(images, output_file):
    histograms = {'baidu': {}, 'allimg': {}}

    for idx, img_path in enumerate(images):
        img = cv2.imread(img_path)  # 读取图像
        hist = calculate_histogram(img)  # 计算图像的灰度直方图
        histograms['baidu'][f"image_{idx}"] = hist  # 将直方图保存到 'baidu' 键下
        histograms['allimg'][f"image_{idx}"] = img  # 将图像数据存储到 'allimg' 键下

    # 将数据保存到 pkl 文件
    with open(output_file, 'wb') as file:
        pickle.dump(histograms, file)

    print(f"saved to {output_file}")

# 示例：保存直方图数据和图像集合
image_paths = ['5_288.jpeg', '6_268.jpeg']  # 示例图片路径
output_file = 'baidu.pkl'  # 输出文件路径
save_histograms(image_paths, output_file)

```

之后读取未转正的图像，计算直方图，找到已经储存到 pkl 文件中最合适的图像，可以用 `cv2.compareHist()` 方法来计算图像之间的直方图相似度，找到相似的图像以后利用 SIFT 进行特征匹配和仿射变换来计算旋转角度。

流程如下：

```
import cv2
import time
import pickle
import numpy as np


# 从文件加载直方图模型
def load_histograms_from_file(file_path):
    with open(file_path, 'rb') as file:
        histograms_data = pickle.load(file)
    return histograms_data

# 特征匹配计算图像的旋转角度
def compute_rotation_angle_by_features(reference_img, query_img):
    # 将图像转换为灰度图
    query_gray = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
    reference_gray = cv2.cvtColor(reference_img, cv2.COLOR_BGR2GRAY)

    # 使用 ORB 特征提取器代替 SIFT（ORB 更加高效）
    orb = cv2.ORB_create()

    # 提取特征点和描述符
    kp1, des1 = orb.detectAndCompute(query_gray, None)
    kp2, des2 = orb.detectAndCompute(reference_gray, None)

    # 使用暴力匹配器进行特征点匹配
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # 提取匹配点
    src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    # 计算变换矩阵，这里使用 RANSAC 方法剔除错误匹配
    matrix, _ = cv2.estimateAffinePartial2D(src_pts, dst_pts, method=cv2.RANSAC, ransacReprojThreshold=5.0)

    if matrix is not None:
        # 提取旋转角度
        angle = np.arctan2(matrix[0, 1], matrix[0, 0]) * (180 / np.pi)
    else:
        angle = None
        print("未能估计变换矩阵。")

    return angle

# 根据旋转角度旋转图像
def rotate_image(img, angle):
    height, width = img.shape[:2]
    # 计算旋转矩阵
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # 进行旋转变换
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height), flags=cv2.INTER_CUBIC)
    return rotated_img

# 使用直方图匹配估计图像的旋转角度
def estimate_image_angle(histograms, image_collection, query_img):
    start_time = time.time()

    # 计算查询图像的灰度直方图
    query_gray = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
    query_hist = cv2.calcHist([query_gray], [0], None, [256], [0, 256])
    cv2.normalize(query_hist, query_hist, 0, 1, cv2.NORM_MINMAX)

    best_match_score = -1
    best_match_key = None

    # 查找与查询图像最相似的图像
    for key, hist in histograms.items():
        similarity = cv2.compareHist(query_hist, hist, cv2.HISTCMP_CORREL)
        if similarity &gt; best_match_score:
            best_match_score = similarity
            best_match_key = key

    print(f"找到最匹配的图像: {best_match_key}")

    # 使用 'best_match_key' 作为索引，从 'image_collection' 字典中获取图像
    best_match_image = image_collection[best_match_key]

    # 计算最佳匹配图像与查询图像之间的旋转角度
    rotation_angle = compute_rotation_angle_by_features(best_match_image, query_img)
    end_time = time.time()

    print(f"执行时间: {end_time - start_time:.2f} 秒，旋转角度: {rotation_angle:.2f} 度。")

    # 显示最匹配的图像
    cv2.imshow("Best Match Image", best_match_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return rotation_angle


# 加载直方图模型和图像集合
histograms_data = load_histograms_from_file('baidu.pkl')
histogram_model = histograms_data['baidu']
image_dataset = histograms_data['allimg']
query_image_path = '5.jpeg'  # 示例查询图像路径

query_img = cv2.imread(query_image_path)

# 估计查询图像的旋转角度
estimated_angle = estimate_image_angle(histogram_model, image_dataset, query_img)

```

最终结果如下：

更细致的处理方法还可以创建掩码，将中心图抠出来，这样会更加准确，可以根据这个思路去设计标注工具，基本很快就能完成对抗，持续对抗是一个不错的选择。这部分标注好的数据集大概 5000 个，后续我会上传到知识星球中，仅供学习交流。
