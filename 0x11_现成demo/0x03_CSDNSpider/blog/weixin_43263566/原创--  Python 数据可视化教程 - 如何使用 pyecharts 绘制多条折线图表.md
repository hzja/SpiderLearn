# 原创
：  Python 数据可视化教程 - 如何使用 pyecharts 绘制多条折线图表

# Python 数据可视化教程 - 如何使用 pyecharts 绘制多条折线图表

**部分数据来源：**ChatGPT  

#### 引言

        本文主要介绍如何使用 Python 中的 pyecharts 库，绘制多条折线图表。在本例中，我们将展示各国的 COVID-19 确诊人数数据。

#### 1、首先，我们需要导入必要的库：

```
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, LabelOpts

```

其中，`json` 库用于解析 JSON 数据，`pyecharts` 库用于绘图，`TitleOpts`、`LegendOpts`、`ToolboxOpts`、`LabelOpts` 则是对绘图的一些设置。

#### 2、接着，我们需要编写一个函数来加载数据：

```
def load_data(file_path):
    """
    加载数据
    参数：
        file_path: 文件路径
    返回值：
        data["data"][0]["trend"]["updateDate"][:314]：日期列表（2020/1/22至今），取前314个字符
        data["data"][0]["trend"]["list"][0]["data"][:314]：确诊
```
