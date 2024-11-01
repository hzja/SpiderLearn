# 原创
：  Python绘制气泡图示例

# Python绘制气泡图示例

**部分数据来源：**ChatGPT

#### 引言

        在数据可视化领域中，气泡图是一种能够同时展示三维信息的图表类型，常用于表示数据集中的两个变量之间的关系。Python中提供了许多用于绘制气泡图的可视化库，比如pyecharts。在本篇文章中，我们将介绍如何使用pyecharts库绘制一个简单的气泡图，并附上示例数据。

#### 准备示例数据

        首先，我们需要准备一个包含x轴、y轴和气泡大小数据的CSV文件。在本例中，我们设定了一个名为`data.csv`的CSV文件，其中包含了10个整数数据点，示例如下：

```
x_axis,y_axis,bubble_size
1,10,5
2,20,10
3,15,15
4,35,20
5,25,25
6,45,30
7,30,35
8,55,40
9,40,45
10,50,50

```

这里的`x_axis`和`y_axis`分别代表X轴和Y轴的数据，`bubble_size`代表气泡大小的数据。你可以根据你的实际需求来修改数据文件。

#### 绘制气泡图

接下来，我们使用pyecharts库读取之前生成的CSV文件，并绘制一个气泡图。

```
import pandas as pd
from pyecharts.charts import Scatter
from pyecharts import options as opts

# 读取csv文件
df = pd.read_csv('data.csv')

# 获取x轴、y轴和气泡大小数据
x_data = df['x_axis'].values.tolist()
y_data 
```
