# 原创
：  【算法】Bellman-Ford单源最短路径算法（附动图）

# 【算法】Bellman-Ford单源最短路径算法（附动图）

**目录**

[一、性质](#%E4%B8%80%E3%80%81%E6%80%A7%E8%B4%A8)

[二、思路](#%E4%BA%8C%E3%80%81%E6%80%9D%E8%B7%AF)

[三、有边路限制的最短路](#%E4%B8%89%E3%80%81%E6%9C%89%E8%BE%B9%E8%B7%AF%E9%99%90%E5%88%B6%E7%9A%84%E6%9C%80%E7%9F%AD%E8%B7%AF)

---


## 一、性质

> 
负权回路：图中带环且环中所有边的权重和为负


---


## 二、思路

Bellman-Ford算法的思路十分简单粗暴

与Dijkstra类似的，我们用一个dist数组存放源节点到任意节点的最短路径

首先，在求最短路径前，我们需要将源节点到自己的距离初始化为0，到其他节点的距离初始化为**最大值**

然后，我们遍历所有的边

> 
对于一条边，我们这里可以直接用一个结构体存储其信息，例如：


```
struct edge{
    int a, b, w;
}edges[M];
```

其中a为有向边出发的节点，b为有向边指向的节点，w为边的权重

遍历所有的边，如果 **dist[a]+w &lt; dist[b]** ，则更新最短路径

以同样的方式一共循环n次，我们就能得到源节点到任意节点的最短路径

 <img alt="" height="664" src="https://i-blog.csdnimg.cn/direct/4ec3b1694c7c4871925e5cd716688751.gif" width="1200"/>

有时不一定非要循环n次才能得到最优解，例如上面我们只循环了3次。但**最坏的情况下**，如果我们的图是这样的呢？

有n个节点，但只有n-1条边，我们**至少循环n-1次**才能将所有节点更新

那我们不能只循环n-1次吗？

前面提到，Bellman-Ford算法可用于检测图中是否存在负权回路，具体是如何检测的？靠的就是这多出来的一次循环

首先解释一下为何**路径中存在负权回路则不存在最短路径**，因为我们如果在这个负权回路中一直走，那么路径长度不就一直在变小直到负无穷吗？

可以看到，在上面最坏的情况下，我们也只需要循环n-1次就能将源节点到每个节点的最短路径求出来，而最后一次循环中不会有节点被更新。但如果**存在负权回路**，则**最后一次循环中一定还会有节点被更新**。通过判断我们就可以知道图中是否存在负权回路。

即使每次遍历边的顺序不同也不会影响最后的结果，但每次循环中dist数组中的值可能不同。因为如果遍历边的顺序与边的指向一致，我们可以连续更新多个节点，例如：

可以看到dist的数组更新是**串联**的，即**一个位置更新可能影响到其他位置**，如果我们没有对最短路径的边数进行限制的话就无需多虑，但如果**最短路径有边数限制**，那我们就需要一个额外的**备份数组**来辅助节点更新

---


## 三、有边路限制的最短路

```
#include &lt;iostream&gt;
#include &lt;cstring&gt;
#include &lt;algorithm&gt;
using namespace std;

const int N = 510, M = 10010;

struct edge{
    int a, b, w;
}edges[M];

int n, m, k;
int dist[N], backup[N]; 
//最短路径有边数限制，所以我们还需要一个备份数组

int bellman_ford()
{
    //初始化dist数组
    memset(dist, 0x3f, sizeof dist); 
    dist[1] = 0; 
    
    //最短路径不能超过k条边，因此我们循环k次
    for(int i = 0;i &lt; k;i++) 
    {
        //将上一次循环中dist数组的结果存入backup数组
        memcpy(backup, dist, sizeof dist); 
        for(int j = 0;j &lt; m;j++)
        {
            int a, b, w;
            a = edges[j].a, b = edges[j].b, w = edges[j].w;
            dist[b] = min(dist[b], backup[a] + w); //用backup数组来更新dist数组
        }
    }
    return dist[n];
}

int main()
{
    cin &gt;&gt; n &gt;&gt; m &gt;&gt; k;
    for(int i = 0;i &lt; m;i++)
    {
        int a, b, w;
        cin &gt;&gt; a &gt;&gt; b &gt;&gt; w;
        edges[i] = {a,b,w}; //存边
    }
    
    int ans = bellman_ford(); //Bellman-Ford算法
    
    if(ans &gt; 0x3f3f3f3f / 2) cout &lt;&lt; "impossible"; 
    //返回值过大不符合预期，可以判断不存在满足条件的路径
    else cout &lt;&lt; ans;
    return 0;
}
```

如有错误，欢迎在评论区指出

完.
