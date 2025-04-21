# 原创
：  【算法】Prim最小生成树算法

# 【算法】Prim最小生成树算法

**目录**

[一、思想](#%E4%B8%80%E3%80%81%E6%80%9D%E6%83%B3)

[二、代码](#%E4%BA%8C%E3%80%81%E4%BB%A3%E7%A0%81)

---


在阅读本文前推荐优先食用：

[【算法】Kruskal最小生成树算法-CSDN博客<img alt="icon-default.png?t=O83A" src="https://csdnimg.cn/release/blog_editor_html/release2.3.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=O83A"/>https://blog.csdn.net/Eristic0618/article/details/143312482?spm=1001.2014.3001.5501](https://blog.csdn.net/Eristic0618/article/details/143312482?spm=1001.2014.3001.5501)

## 一、思想

Kruskal算法基于边的选择，因此更适用于稀疏图。而对于**基于选择节点**的Prim最小生成树算法，其更适用于边数量远大于节点数量的**稠密图**

Prim算法的思想如下：

例如下面这个图：

我们以1号节点作为起始节点加入连通块，其他所有节点距离连通块的距离初始化为最大值

更新其他节点距离连通块的最短距离

从所有没有被加入连通块的节点中，找出离连通块距离最短的节点（此处为V3），加入连通块

更新其他节点距离连通块的最短距离，因为V3是新加入连通块的节点，所以实际上只需要判断其他未加入节点距离V3的距离是否小于自己原来的最短距离即可

继续找距离最短节点，此处V4和V6距离连通块的距离都为4，说明最小生成树不一定是唯一的。此处我们选择V4，将其加入连通块并更新距离

V6距离连通块最近，将V6加入连通块并更新距离

V2最近，将V2加入连通块并更新距离

最后是V5

所有节点都被加入连通块后，我们就得到了图中的最小生成树

---


## 二、代码

```
#include &lt;bits/stdc++.h&gt;
#define int long long
#define endl '\n'
#define debug(x) cout &lt;&lt; #x &lt;&lt; " = " &lt;&lt; x &lt;&lt; '\n'
#define INF 0x3f3f3f3f
using namespace std;

#define N 510
#define M 1000010

int	n, m;
int dist[N]; //节点到连通块的最短距离 
int g[N][N]; //邻接矩阵
bool st[N];  //判断某节点是否在连通块中 

int Prim()
{
	memset(dist, 0x3f, sizeof dist); //初始化dist数组 
	dist[1] = 0;
	
	int res = 0; //最小生成树边权和 
	for(int i = 0; i &lt; n; i++) //起始节点已加入连通块，遍历剩余n-1个节点
	{
		int t = -1; //标记当前遍历中与连通块距离最小的节点编号 
		for(int j = 1; j &lt;= n; j++) //遍历所有节点 
		{
			if(!st[j] &amp;&amp; (t == -1 || dist[t] &gt; dist[j])) //节点j不在连通块中 且 当前未选择节点或节点j距离比节点t更短
				t = j; //更新t 
		}
		//经过循环，此时节点t就是 剩余所有不属于连通块中的节点 中 距离连通块最短的节点 
		if(dist[t] &gt; INF / 2) return INF; // dist[t]仍为最大值，说明剩余节点不与连通块相连
		
		res += dist[t]; //将t距离连通块的距离加入边权和 
		
		for(int j = 1; j &lt;= n; j++)
		{
			dist[j] = min(dist[j], g[t][j]); //更新剩余节点到连通块的最短距离 
		}
		
		st[t] = true; //将节点t加入连通块 
	}
	return res;
}

void solve()
{
	cin &gt;&gt; n &gt;&gt; m;
	
	memset(g, 0x3f, sizeof g); //所有权重全部初始化为最大值 
	for(int i = 0;i &lt; m; i++)
	{
		int a, b, w;
		cin &gt;&gt; a &gt;&gt; b &gt;&gt; w;
		g[a][b] = g[b][a] = min(g[a][b], w); //无向图and可能存在重边 
	}
	
	int ret = Prim();
	
	if(ret == INF) cout &lt;&lt; "impossible" &lt;&lt; endl;
	else cout &lt;&lt; ret &lt;&lt; endl;
}

signed main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    //cin &gt;&gt; t;
    while(t--)
        solve();
    return 0;
}
```

完.
