# 原创
：  【算法】Dijkstra求最短路算法

# 【算法】Dijkstra求最短路算法

**TOP提示：Dijkstra算法只适用于不含负权边的情况 **

Dijkstra算法是一个基于贪心，广搜和动态规划 求图中某点到其他所有点的最短路径的算法 

## 一、步骤

首先我们先总结Dijkstra算法的完整步骤

我们需要一个dis数组存储从起点到达其他节点的最短距离，一个check数组判断从起点到某点的最短距离是否已确定，一个path二维数组存储图中从点 i 到点 j 的距离

一共循环n次（n个节点），起初将从起点到其他所有节点的距离（dis[i]）初始化为最大值。

每次循环从dis数组中**未确定最短路径的所有点**中找出最小值的下标mini（第一次循环时最小值为起点dis[1]，因为起点到自己的距离为0，其他的都初始化为了最大值），**此时该最小值即为起点到该点的最短路径**，在check数组中标记该点，然后计算**从该点出发到达其他节点的距离**，如果比原来的值更小则更新dis数组。

## 二、原理

贪心是其中的重要思想，为什么每次找出的最小值就是起点到该点的最短路径呢？

这就要提到为什么Dijkstra不适用于含负权边的情况了，当边的权值全部为正时，从起点经过其他的点到达最小值点的路径长度**必定会大于原来的这个最小值！**

例如你从起点到A点的最短路径是100，到B点的最短路径是200，那么你从起点经过B点到达A点的距离可能会比直接从起点到A点的距离短吗？除非从B点到A点的距离为负数。 

所以当我们每次扫描未确定最短路径中的所有点，找出其中的最小值，该最小值就是起点到达该点的最短路径。经过n次循环，我们就能找出起点到达所有点的最短路径 

我们以下面这道题为例实战一下：

完整代码：

```
#include &lt;iostream&gt;
#include &lt;algorithm&gt;
#include &lt;cstring&gt;
using namespace std;

const int N = 510;

int n, m, dis[N];
int path[N][N];
bool check[N];

int dijkstra()
{
    memset(dis, 0x3f, sizeof dis); //将起点到其他点的路径初始化为最大值
    dis[1] = 0; //起点到自己的距离为0
    for(int i = 1;i &lt;= n;i++) //n次循环
    {
        int mini = -1; 
        for(int j = 1; j &lt;= n;j++)
        {
            if(!check[j] &amp;&amp; (mini == -1 || dis[mini] &gt; dis[j]))
            //从未确定最短距离的点中取出最小值
                mini = j;
        }
        
        check[mini] = true; //标记该点为已确定
        
        for(int j = 1;j &lt;= n;j++)
        {
            //以该点为基础更新其他所有点的最短距离
            dis[j] = min(dis[j], dis[mini] + path[mini][j]);
        }
    }
    if(dis[n] == 0x3f3f3f3f) return -1; //如果n号点的距离还是为最大值，说明无法到达
    return dis[n];
}

int main()
{
    //题目中说可能存在重边，所以将边的权值初始化为最大值便于比较
    memset(path, 0x3f, sizeof path);
    cin &gt;&gt; n &gt;&gt; m;
    for(int i = 1;i &lt;= m;i++)
    {
        int a, b ,c;
        cin &gt;&gt; a &gt;&gt; b &gt;&gt; c;
        path[a][b] = min(path[a][b], c); //如果重边，取最小值
    }
    
    int t = dijkstra(); //Dijkstra算法
    
    cout &lt;&lt; t &lt;&lt; endl;
    return 0;
}
```
