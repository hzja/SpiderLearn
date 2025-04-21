# 原创
：  【算法】spfa最短路径算法

# 【算法】spfa最短路径算法

**目录**

[一、概念](#%E4%B8%80%E3%80%81%E6%A6%82%E5%BF%B5)

[二、思路](#%E4%BA%8C%E3%80%81%E6%80%9D%E8%B7%AF)

[三、spfa求最短路](#%E4%B8%89%E3%80%81spfa%E6%B1%82%E6%9C%80%E7%9F%AD%E8%B7%AF)

---


在阅读本文前请先食用：

[【算法】Bellman-Ford单源最短路径算法（附动图）-CSDN博客文章浏览阅读366次，点赞16次，收藏14次。算法学习笔记之Bellman-Ford单源最短路径算法<img alt="" src="https://g.csdnimg.cn/static/logo/favicon32.ico"/>https://blog.csdn.net/Eristic0618/article/details/143207783](https://blog.csdn.net/Eristic0618/article/details/143207783)

## 一、概念

---


## 二、思路

spfa算法的核心思路：**用被更新的节点去更新其他的节点**

（记好节点编号，后面为了方便展示将节点编号替换为节点的dist值）

首先将**源节点入队**

**当队列不为空时**，取出队头节点并遍历其出边，更新其他节点，并**将被更新的节点入队**

循环上一步

当遍历2号节点的出边时，3号节点被更新，但队列中已经存在3号节点，所以无需再次入队

为了维护队列中节点的唯一性，我们需要一个check数组

当队列为空时得出最优解

---


## 三、spfa求最短路

```
#include &lt;iostream&gt;
#include &lt;algorithm&gt;
#include &lt;cstring&gt;
#include &lt;queue&gt;
using namespace std;

const int N = 100010;

int n, m, dis[N];
int e[N], h[N], w[N], ne[N], idx;
bool check[N]; //维护队列，使队列中节点不重复

int spfa()
{
    //初始化dist数组
    memset(dis, 0x3f, sizeof dis);
    dis[1] = 0;
    queue&lt;int&gt; q; //宽搜核心：队列
    q.push(1); //将源节点加入队列
    
    while(q.size()) //当队列非空
    {
        int t = q.front(); //取出队头节点
        q.pop(); //节点出队
        check[t] = false; //修改check数组
        for(int i = h[t];i != -1;i = ne[i]) //遍历节点所有出边
        {
            int j = e[i]; //j为有向边指向的节点
            if(dis[j] &gt; dis[t] + w[i]) // 更新为更短距离，将对应点入队
            {
                dis[j] = dis[t] + w[i];
                if(!check[j]) //若队列中不存在该节点
                {
                    q.push(j); //节点入队
                    check[j] = true; //修改check数组
                }
            }
        }
    }
    return dis[n];
}

void add(int a, int b, int c) //构建邻接表
{
    e[idx] = b; w[idx] = c; ne[idx] = h[a]; h[a] = idx++;
}

int main()
{
    memset(h, -1, sizeof h);
    cin &gt;&gt; n &gt;&gt; m;
    for(int i = 1;i &lt;= m;i++) //构建邻接表
    {
        int a, b ,c;
        cin &gt;&gt; a &gt;&gt; b &gt;&gt; c;
        add(a, b, c);
    }
    
    int t = spfa(); //spfa算法
    
    if(t == 0x3f3f3f3f) cout &lt;&lt; "impossible";
    else cout &lt;&lt; t;
    return 0;
}
```

完.
