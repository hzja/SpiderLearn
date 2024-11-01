# 原创
：  使用Python和Pyecharts制作中国疫情地图可视化教程

# 使用Python和Pyecharts制作中国疫情地图可视化教程

#### 引言 

        前些年新冠病毒疫情肆虐全球，如何更直观地展示全国疫情数据，是每一个数据科学家需要思考的问题。本文将介绍如何使用Python的第三方库Pyecharts制作一张中国疫情地图，并对代码进行详细解释，适合初学者学习。

#### 什么是Pyecharts？

        Pyecharts是一个基于Echarts的Python可视化库，可以用Python语言快速搭建丰富多样的可视化图表。它支持多种常见的可视化类型，包括柱状图、折线图、散点图、饼图、地图等。

本文所做的地图可视化即是基于Pyecharts，通过导入需要用到的模块，再利用类和函数的编程方式，实现了中国疫情地图的可视化效果。

#### 所需模块

在开始写代码之前，我们需要导入以下几个模块：

#### 写代码

在导入必要的模块后，我们可以创建一个名为ChinaEpidemicVisualization的类，在这个类中实现我们需要使用的各种操作。首先，我们需要定义类的初始化函数，传入数据文件路径和编码方式：

```
class ChinaEpidemicVisualization:
    def __init__(self, file_path, file_encoding):
        self.file_path = file_path # 数据文件路径 
        self.file_encoding = file_encoding # 数据
```
