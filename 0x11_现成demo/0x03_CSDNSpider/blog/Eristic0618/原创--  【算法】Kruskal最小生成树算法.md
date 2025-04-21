# 原创
：  【算法】Kruskal最小生成树算法

# 【算法】Kruskal最小生成树算法

**目录**

[一、最小生成树](#%E4%B8%80%E3%80%81%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91)

[二、Kruskal算法求最小生成树](#%E4%BA%8C%E3%80%81Kruskal%E7%AE%97%E6%B3%95%E6%B1%82%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91)

[三、代码](#%E4%B8%89%E3%80%81%E4%BB%A3%E7%A0%81)

---


## 一、最小生成树

什么是最小生成树？ 

对于一个n个节点的带权图，从中选出**n-1条边**（保持每个节点的联通）构成一棵树（不能带环），使得所有边的权值和最小，即为最小生成树

要点：

---


## 二、Kruskal算法求最小生成树

Kruskal算法适用于**稀疏图**，因为其过程基于边的选择，如果图中的边过多可能导致效率变低

其思路如下：

例如：

这是我们的原图

去掉所有的边

按照权重从小到大回填边

此时发现有两条权重为4的边，选择哪条都可以，这也说明我们的最小生成树并不是唯一的，但最小权重和一定是唯一的

此时有两条权重为5的边，但如果我们把V1和V4之间的边回填的话，就带环了，这是不符合要求的，因此我们选择V2和V3之间的边

此时已经选择了n-1条边，我们的最小生成树就为

---


## 三、代码

Kruskal算法的思想很容易理解，但代码实现还是有些难度的

例如我们该如何判断图中是否带环呢？其实很简单，如果在回填某条边时，边两端的节点位于同一个集合中就说明带环。我们可以使用**并查集**来判断

关于并查集，可以阅读：

[【算法】并查集-CSDN博客<img alt="icon-default.png?t=O83A" src="https://csdnimg.cn/release/blog_editor_html/release2.3.7/ckeditor/plugins/CsdnLink/icons/icon-default.png?t=O83A"/>https://blog.csdn.net/Eristic0618/article/details/138584962](https://blog.csdn.net/Eristic0618/article/details/138584962)接下来写一道例题练练手

[P3366 【模板】最小生成树 - 洛谷 | 计算机科学教育新生态](https://www.luogu.com.cn/problem/P3366)

```
#include &lt;bits/stdc++.h&gt;
#define int long long
#define endl '\n'
#define debug(x) cout &lt;&lt; #x &lt;&lt; " = " &lt;&lt; x &lt;&lt; '\n'
#define INF 0x3f3f3f3f
using namespace std;

#define N 5050
#define M 200020

int n, m;
int f[N]; //并查集 

struct edge
{
	int a, b, w;
}e[M];

int cmp(struct edge a, struct edge b)
{
	return a.w &lt; b.w;
}

int check(int num) //查询某个节点所在集合的根 
{
	if(f[num] != num) return f[num] = check(f[num]); 
	//压缩路径：将路径上每个节点的父亲都修改为根节点 
	return num;
}

void merge(int a, int b) //合并两个节点所在集合
{
	if(a == b) //a,b相同 
		return;
	f[a] = b; //a的父节点置为b 
} 

bool same(int a, int b) //判断两个节点是否在同一集合 
{
	if(f[a] == f[b]) return true; //a,b父节点相同，说明在同一集合 
	else return false;
}

int Kruskal()
{
	for(int i = 1; i &lt;= n; i++) //初始化并查集 
	{
		f[i] = i;
	}
	sort(e, e+m, cmp); //按照边权升序排序 
	int cnt = 0; //统计当前选择了多少条边 
	int ans = 0; //最小生成树边权和 
	for(int i = 0;i &lt; m; i++) //遍历所有边 
	{
		int a = e[i].a, b = e[i].b, w = e[i].w;
		a = check(a), b = check(b);
		if(same(a, b)) //a与b处于同一连通分量
			continue;
		//a与b不处于同一连通分量
		ans += w; //选择该条边
		merge(a, b); //将a，b所在连通分量合并 
		cnt++;
		if(cnt == n-1) //已选择n-1条边 
			break;
	} 
	if(cnt &lt; n-1) //边数不足
		return -1;
	return ans; 
}

void solve()
{
	cin &gt;&gt; n &gt;&gt; m;
	for(int i = 0;i &lt; m; i++)
	{
		int x, y, z;
		cin &gt;&gt; x &gt;&gt; y &gt;&gt; z;
		e[i] = {x, y, z}; //存边 
	}
	
	int ans = Kruskal(); //Kruskal算法
	if(ans == -1) //不连通 
		cout &lt;&lt; "orz" &lt;&lt; endl;
	else
		cout &lt;&lt; ans &lt;&lt; endl;
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
