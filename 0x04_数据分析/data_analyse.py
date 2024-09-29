import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#画折线图
x=np.linspace(-np.pi,np.pi,256)

cos=np.cos(x)
sin=np.sin(x)

plt.plot(x,cos,'--',linewidth=2)
plt.plot(x,sin)

plt.show

#画饼图
labels = 'cats','dogs','sheep','pigs'
sizes = [30,20,40,10]
explode = (0,0.1,0,0.2)

fig1,ax1 = plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()

# #画直方图
np.random.seed(0)
mu = 200
sigma = 25
x=np.random.normal(mu,sigma,size=100)
fig,(ax0,ax1)=plt.subplots(ncols=2,figsize=(8,4))
ax0.hist(x,20,histtype='stepfilled',facecolor='g',alpha=0.75)
ax0.set_title('stepfilled')

bins = [100, 150, 180, 195, 205, 220, 250, 300]
ax1.hist(x,bins,histtype='bar',rwidth=0.8)
ax1.set_title('unequal bins')

fig.tight_layout()
plt.show()
#画散点图
sns.set(style="darkgrid")

tips = sns.load_dataset("tips")
sns.relplot(x="total_bili",y="tip",data=tips)
plt.show()

#画折线图
fmri = sns.load_dataset("fmri")
sns.replot(x="timepoint",y="signal",hue="event",kind="line",data=fmri);
plt.show()

#画直方图
titanic = sns.load_dataset("titanic")
sns.catplot(x="set",y="survived",hue="class",kind="bar",data=titanic)
plt.show()

from pyecharts.charts import Pie,WordCloud
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts_snapshot.main import make_a_snapshot
from snapshot_selenium import snapshot as driver

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot

#画条形图
bar=(
    Bar()
    .add_xaxis(["衬衫","毛衣","领带","裤子","风衣","高跟鞋","袜子"])
    .add_yaxis("商家A",[114,55,27,101,125,27,105])
    .add_yaxis("商家B",[57,134,137,129,145,60,49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
bar.render()

#画饼状图
def pie_base() -> Pie:
    c = (
        Pie()
        .add("",[list(z) for z in zip(Faker.choose(),Faker.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    )
    return c
make_a_snapshot(driver,pie_base().render(),"pie.png")

#制作词云图
words = [
    ("Sam S Club", 10000),
    ("Macys", 6181),
    ("Amy Schumer", 4386),
    ("Jurassic World", 4055),
    ("Charter Communications", 2467),
    ("Chick Fil A", 2244),
    ("Planet Fitness", 1868),
    ("Pitch Perfect", 1484),
    ("Express", 1112),
    ("Home", 865),
    ("Johnny Depp", 847),
    ("Lena Dunham", 582),
    ("Lewis Hamilton", 555),
    ("KXAN", 550),
    ("Mary Ellen Mark", 462),
    ("Farrah Abraham", 366),
    ("Rita Ora", 360),
    ("Serena Williams", 282),
    ("NCAA baseball tournament", 273),
    ("Point Break", 265),
]

def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
        .add("",words,word_size_range=[20,100])
        .set_global_opts(title_opts=opts.TitleOpts(title="WorldCloud-基本示例"))
    )
    return c

make_snapshot(driver,wordcloud_base().render(),"WorldCloud.png")