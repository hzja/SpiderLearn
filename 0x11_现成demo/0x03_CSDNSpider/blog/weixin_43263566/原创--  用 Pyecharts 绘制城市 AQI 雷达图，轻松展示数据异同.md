# 原创
：  用 Pyecharts 绘制城市 AQI 雷达图，轻松展示数据异同

# 用 Pyecharts 绘制城市 AQI 雷达图，轻松展示数据异同

**部分数据来源：**ChatGPT 

#### 准备数据

        假设我们有以下三个城市的 AQI 数据：北京、上海和广州。每个城市对应六项指标：AQI 等级、PM2.5、PM10、SO2、NO2 和 CO。示例数据格式如下：

aqi.json

```
[
  [80, 40, 35, 20, 45, 1],
  [90, 35, 30, 25, 50, 0.8],
  [110, 50, 45, 30, 70, 1.5]
]

```

接下来，我们需要使用 Pyecharts 将这些数据绘制成雷达图。我们可以使用 `Radar()` 类来创建雷达图，并通过多次调用 `add()` 方法来添加每个城市的数据。

#### 具体操作过程如下所示：

#### 1. 导入所需的模块和数据

```
import json
from pyecharts.charts import Radar
from pyecharts import options as opts

with open('aqi.json') as f:
    data = json.load(f)

```

这里先使用 `json.load()` 函数读取示例数据文件 `aqi.json` 并将其赋值给变量 `data`。

#### 2. 创建雷达图对象并设置全局参数

```
radar = (
    Radar()
    .set_global_opts(title_opts=opts.TitleOpts(title="AQI Radar Chart"), 
```
