# 原创
：  简单易懂！Python中如何用Pyecharts制作散点图 | 实例教程

# 简单易懂！Python中如何用Pyecharts制作散点图 | 实例教程

**部分数据来源：**ChatGPT 

### 引言

        在数据可视化领域中，散点图是一种常见的图表类型，用于表示两个数值变量之间的关系。Python中提供了诸多绘图库，其中包括了强大而易于上手的pyecharts库。在本篇文章中，我们将介绍如何使用pyecharts库在Python中绘制一个简单的散点图，并附上示例数据。

### 准备示例数据

首先，我们需要准备一个包含x轴和y轴数据的CSV文件。在本例中，我们设定了一个名为`data.csv`的CSV文件，其中包含了10个数据点，示例如下：

```
x_axis,y_axis
1,10
2,20
3,15
4,35
5,25
6,45
7,30
8,55
9,40
10,50

```

这里的`x_axis`代表X轴的数据，`y_axis`代表Y轴的数据，你可以根据你自己的实际需求来修改数据。

### 绘制散点图

接下来，我们使用pyecharts库读取之前生成的CSV文件，并绘制一个散点图。

```
import pandas as pd
from pyecharts.charts import Scatter
from pyecharts import options as opts

# 读取csv文件
df = pd.read_csv('data.csv')

# 获取x轴和y轴数据
x_data = df['x_axis'].values.tolist()
y_data = df['y_axis'].values.tolist()

# 绘制散点图
scatter = (
    Scatter()
    
```
