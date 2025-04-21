# 原创
：  【数据结构】AVL树（万字超详细 附动图）

# 【数据结构】AVL树（万字超详细 附动图）

[一、前言](#%E4%B8%80%E3%80%81%E5%89%8D%E8%A8%80)

[二、AVL树的性质](#%E4%BA%8C%E3%80%81AVL%E6%A0%91%E7%9A%84%E6%80%A7%E8%B4%A8)

[三、AVL树节点的定义](#%E4%B8%89%E3%80%81AVL%E6%A0%91%E8%8A%82%E7%82%B9%E7%9A%84%E5%AE%9A%E4%B9%89)

[四、AVL树的插入](#%E5%9B%9B%E3%80%81AVL%E6%A0%91%E7%9A%84%E6%8F%92%E5%85%A5)

[五、AVL树的平衡调整](#%E4%BA%94%E3%80%81AVL%E6%A0%91%E7%9A%84%E5%B9%B3%E8%A1%A1%E8%B0%83%E6%95%B4)

[六、AVL树的验证](#%E5%85%AD%E3%80%81AVL%E6%A0%91%E7%9A%84%E9%AA%8C%E8%AF%81)

[6.1 验证有序](#6.1%20%E9%AA%8C%E8%AF%81%E6%9C%89%E5%BA%8F)

[6.2 验证平衡](#6.2%20%E9%AA%8C%E8%AF%81%E5%B9%B3%E8%A1%A1)

[七、AVL树的删除](#%E4%B8%83%E3%80%81AVL%E6%A0%91%E7%9A%84%E5%88%A0%E9%99%A4)

[八、AVL树的性能和代码](#%E5%85%AB%E3%80%81AVL%E6%A0%91%E7%9A%84%E6%80%A7%E8%83%BD%E5%92%8C%E4%BB%A3%E7%A0%81)

---


## 一、前言

还没有学习过二叉搜索树的同学可以移步

[【数据结构】二叉搜索树-CSDN博客<img alt="icon-default.png?t=N7T8" src="https://i-blog.csdnimg.cn/blog_migrate/003a2ce7eb50c2e24a8c624c260c5930.png"/>https://blog.csdn.net/Eristic0618/article/details/137919573?spm=1001.2014.3001.5501](https://blog.csdn.net/Eristic0618/article/details/137919573?spm=1001.2014.3001.5501)AVL树，又称为平衡二叉树，它基于二叉搜索树并通过平衡而得到。

在前面的学习中我们提到，二叉搜索树可以提高搜索数据的效率，但在数据有序的情况下会退化为单支树，此时在树中查找元素就得遍历一整个分支，时间复杂度也会退化至O(N)。

如果有一种算法，可以使二叉搜索树时刻保持左右子树的平衡，就可以避免这种最坏情况。

因此，两位俄罗斯的数学家G.M.Adelson-Velskii和E.M.Landis在1962年发明了AVL树，解决了上述问题。

---


## 二、AVL树的性质

当我们向二叉搜索树中插入新节点时，如果能用某种方法时刻保证树中每个节点的**左右子树高度之差**不超过1，就可以降低整棵树的高度，保证每条分支的平衡

AVL树的性质如下：

例如：

---


## 三、AVL树节点的定义

AVL树的左右子树高度差不能超过1，但是如何便捷的去检测该性质是否被打破呢？

我们可以在节点中定义一个**平衡因子**，如果左子树比右子树高一层，那么平衡因子就为-1；如果左右子树一样高，平衡因子就为0；如果右子树比左子树高一层，那么平衡因子就为1，这三种情况下AVL树的性质都没有被打破。

按照这个规则，如果平衡因子为-2、2或其他值，则说明左右子树已经失衡，性质被打破。

在调整失衡的AVL树时，我们需要频繁的访问父节点，所以在AVL树中我们需要使用三叉链，因此AVL树的节点除了包含左右子节点的指针，还需要一个指向父节点的指针

另外需要说明一下，本文中，我们使用key/value模型的AVL树

AVL树节点的定义如下：

```
template&lt;class K,class V&gt;
struct AVLTreeNode
{
	AVLTreeNode&lt;K, V&gt;* _left;
	AVLTreeNode&lt;K, V&gt;* _right;
	AVLTreeNode&lt;K, V&gt;* _parent;
	
	pair&lt;K, V&gt; _kv; //第一个数据存储key，第二个数据存储value
	int _bf; //平衡因子(balance factor)

	AVLTreeNode(const pair&lt;const K, V&gt;&amp; kv)
		:_left(nullptr)
		,_right(nullptr)
		,_parent(nullptr)
		,_kv(kv)
		,_bf(0) //新节点左右都为空，平衡因子为0
	{}
};
```

可能有些同学对pair没有了解，这里简单介绍一下

pair可以将两个数据组成一组元素，因此对于key/value模型这种需要用到两个数据为一组的元素时就可以使用，内部的成员变量为first和second，其主要使用方法为：

```
pair&lt;T1, T2&gt; p1(v1, v2); //输入两个数据创建pair类型变量
make_pair(v1, v2);       //输入两个数据通过函数创建pair类型变量
p1.first                 //访问p1的第一个数据
p1.second                //访问p1的第二个数据
```

---


## 四、AVL树的插入

向AVL树中插入节点与向二叉搜索树中插入节点的过程基本相同，唯一的区别就是AVL树在插入节点后可能存在失衡的情况，需要调整。

我们先按照二叉搜索树的规则将节点插入到AVL树中，并判断插入的节点在父节点的左边还是右边

按照平衡因子的规则，如果新节点插入到了父节点的左侧，那么父节点的平衡因子-1

如果新节点插入到了父节点的右侧，那么父节点的平衡因子+1

以上，便是新增节点的父节点平衡因子可能的变化情况。

**但是！**插入一个节点不但会影响父节点，还可能会**影响到祖先节点**。

我们观察上面的四种可能，其中**左边的两种情况**下，插入节点后以父节点为根的子树高度发生了变化；在**右边的两种情况**下，插入节点后以父节点为根的子树高度没有发生变化。

观察过后可以发现，当父节点的平衡因子从0变为1/-1后，子树高度发生变化；当父节点的平衡因子从1/-1变为0后，子树高度不发生变化 

如果以父节点为根的子树高度没有发生变化，那么就**不会影响**到祖先节点的平衡因子；如果高度变了就**会继续向上影响**到祖先节点的平衡因子

因此，我们可以通过**判断节点的插入位置**来**计算父节点的平衡因子**，进而**判断子树高度是否发生变化**，再进一步**计算对祖先节点平衡因子的影响**，来**判断AVL树是否失衡**。

至此，我们已经可以开始写插入新节点和更新平衡因子的代码了：

```
template&lt;class K, class V&gt;
class AVLTree
{
	typedef AVLTreeNode&lt;K, V&gt; Node;
public:
	bool insert(const pair&lt;const K, V&gt;&amp; kv)
	{
		if (_root == nullptr) //检测为空树的情况
		{
			_root = new Node(kv);
			return true;
		}

		Node* parent = nullptr;
		Node* cur = _root;

		while (cur) //搜索新节点的插入位置
		{
			parent = cur;
			if (kv.first &gt; cur-&gt;_kv.first)
				cur = cur-&gt;_right;
			else if (kv.first &lt; cur-&gt;_kv.first)
				cur = cur-&gt;_left;
			else
				return false;
		}

		cur = new Node(kv);
        //将父节点与新节点链接
        //比较新节点和父节点的key判断插入到左边还是右边
		if (kv.first &gt; parent-&gt;_kv.first) //这里防止有人看不懂再强调一遍，kv是pair类型的对象，kv.first是key，kv.second是value
		{
			parent-&gt;_right = cur;
			cur-&gt;_parent = parent;
		}
		else
		{
			parent-&gt;_left = cur;
			cur-&gt;_parent = parent;
		}

		while (cur != _root)
		{
            //插入节点后除了对父节点造成影响还可能对祖宗节点造成影响
            //因此随着循环进行，这里的cur不一定为新节点，可以理解为高度发生变化的子树的根节点
            //更新父节点的平衡因子
			if (cur == parent-&gt;_left)
				parent-&gt;_bf--;
			else
				parent-&gt;_bf++;

            //更新后检测父节点的平衡因子
			if (parent-&gt;_bf == 0) //平衡因子为0说明没有打破性质，跳出循环
				break;
			else if (parent-&gt;_bf == 1 || parent-&gt;_bf == -1) //更新后平衡因子为1或-1说明高度发生变化，改变cur和parent的指向后继续向上更新
			{
				cur = parent;
				parent = parent-&gt;_parent;
			}
			else if (parent-&gt;_bf == 2 || parent-&gt;_bf == -2) //更新后平衡因子为2或-2.说明已经失衡，需要调整
			{
                //不同情况的调整方法...
				if (parent-&gt;_bf == 2)
				{
					if (cur-&gt;_bf == 1)
					{
						//...
					}
					else if (cur-&gt;_bf == -1)
					{
						//...
					}
				}
				else
				{
					if (cur-&gt;_bf == 1)
					{
						//...
					}
					else if (cur-&gt;_bf == -1)
					{
						//...
					}
				}
				break;
			}
			else //平衡因子出现意外情况，报错
			{
				assert(false);
			}
		}

		return true;
	}

private:
	Node* _root = nullptr;
};
```

---


## 五、AVL树的平衡调整（附动图）

如果在一颗原本平衡的AVL树中插入一个新节点，可能会造成失衡，此时需要调整树的结构使之重新平衡，这种调整方法称为**旋转**。

根据树的原本结构和节点插入位置的不同分为**四种情况**和**四种旋转方式**：

（1）新节点插入**较高左子树**的**左侧**：右单旋

自己做的动图大家有需要自取~这里就不加水印了

问题来了：如何判断插入的新节点的方位呢？

很简单，以上面的情况为例，插入新节点后60的平衡因子变成-2，说明左子树更高，而30的平衡因子变成-1，说明新节点插入到了30的左子树。后面左单旋以及双旋中都同理，我们使用平衡因子就可以判断新节点插入的位置

右单旋代码如下：

```
void RotateRight(Node *parent) //parent为平衡因子发生失衡的节点
{
    Node *subL = parent-&gt;_left; //subL为parent的左子节点
    Node *subLR = subL-&gt;_right; //subLR为subL的右子节点
    //parent，subL和subLR三个节点是旋转中唯三需要进行操作的三个节点

    // 将parent与subLR节点进行链接
    parent-&gt;_left = subLR;
    if (subLR) //subLR可能为空
        subLR-&gt;_parent = parent;

    Node *parentParent = parent-&gt;_parent; //记录parent的父节点

    if (parent != _root)
    {
        subL-&gt;_parent = parentParent; //将subL与parent的父节点链接
        if (parent == parentParent-&gt;_left)
            parentParent-&gt;_left = subL;
        else
            parentParent-&gt;_right = subL;
    }
    else //如果parent为根，旋转后subL成为新的根
    {
        _root = subL;
        subL-&gt;_parent = nullptr;
    }

    //将subL与parent链接
    subL-&gt;_right = parent;
    parent-&gt;_parent = subL;

    parent-&gt;_bf = subL-&gt;_bf = 0; //更新平衡因子
}
```

（2）新节点插入**较高右子树**的**右侧**：左单旋

因为左单旋的原理和右单旋是类似的，只要理解了右单旋，加上动图的配合，左单旋和后面的双旋都是很好理解的 

左单旋代码如下：

```
void RotateLeft(Node *parent)
{
    Node *subR = parent-&gt;_right;
    Node *subRL = subR-&gt;_left;

    parent-&gt;_right = subRL;
    if (subRL)
        subRL-&gt;_parent = parent;

    Node *parentParent = parent-&gt;_parent;

    if (parent != _root)
    {
        subR-&gt;_parent = parentParent;
        if (parent == parentParent-&gt;_left)
            parentParent-&gt;_left = subR;
        else
            parentParent-&gt;_right = subR;
    }
    else
    {
        _root = subR;
        subR-&gt;_parent = nullptr;
    }

    subR-&gt;_left = parent;
    parent-&gt;_parent = subR;

    parent-&gt;_bf = subR-&gt;_bf = 0;
}
```

（3）新节点插入**较高左子树**的**右侧**：先左单旋再右单旋（左右双旋） 

这种情况又可以分为两种情况：

不过这两种情况都属于在较高左子树的右侧插入，处理方式都是相同的，唯一的区别在于最后旋转完成后，更新平衡因子时的值不同。

接下来我们以上面的那个情况为例展示左右双旋的过程：

而下面的情况和上面的情况唯一的区别在于，最后更新的平衡因子不同

如何去决定每个节点更新后的平衡因子呢？可以看到这两种情况中，如果在b下面插入新节点，那么旋转过后30和60的平衡因子更新成0，90的平衡因子更新成1；如果在c下面插入新节点，则是60和90的平衡因子更新成0，30的平衡因子更新成-1

而新节点究竟插入到了b下面还是在c下面，我们可以通过插入节点后60的平衡因子来判断

左右双旋代码如下：

```
void RotateLR(Node *parent)
{
    Node *subL = parent-&gt;_left;
    Node *subLR = subL-&gt;_right;
    int bf = subLR-&gt;_bf; //记录插入节点后subLR的平衡因子

    RotateLeft(subL); //先左单旋
    RotateRight(parent); //再右单旋

    //更新平衡因子
    //通过前面记录的平衡因子判断更新的情况
    if (bf == 0)
    {
        parent-&gt;_bf = subL-&gt;_bf = subLR-&gt;_bf = 0;
    }
    else if (bf == 1)
    {
        subL-&gt;_bf = -1;
        parent-&gt;_bf = subLR-&gt;_bf = 0;
    }
    else if (bf == -1)
    {
        parent-&gt;_bf = 1;
        subL-&gt;_bf = subLR-&gt;_bf = 0;
    }
    else
    {
        assert(false);
    }
}
```

（4）新节点插入**较高右子树**的**左侧**：先右单旋再左单旋（右左双旋）

这种情况和左右双旋的情况原理一样，我们直接上动图和代码

右左双旋的代码如下：

```
void RotateRL(Node *parent)
{
    Node *subR = parent-&gt;_right;
    Node *subRL = subR-&gt;_left;
    int bf = subRL-&gt;_bf;

    RotateRight(subR);
    RotateLeft(parent);

    if (bf == 0)
    {
        parent-&gt;_bf = subR-&gt;_bf = subRL-&gt;_bf = 0;
    }
    else if (bf == 1)
    {
        parent-&gt;_bf = -1;
        subR-&gt;_bf = subRL-&gt;_bf = 0;
    }
    else if (bf == -1)
    {
        subR-&gt;_bf = 1;
        parent-&gt;_bf = subRL-&gt;_bf = 0;
    }
    else
    {
        assert(false);
    }
}
```

现在四个旋转的函数都实现了，完整的插入函数代码如下：

```
bool insert(const pair&lt;const K, V&gt; &amp;kv)
{
    if (_root == nullptr)
    {
        _root = new Node(kv);
        return true;
    }

    Node *parent = nullptr;
    Node *cur = _root;

    while (cur)
    {
        parent = cur;
        if (kv.first &gt; cur-&gt;_kv.first)
            cur = cur-&gt;_right;
        else if (kv.first &lt; cur-&gt;_kv.first)
            cur = cur-&gt;_left;
        else
            return false;
    }

    cur = new Node(kv);
    if (kv.first &gt; parent-&gt;_kv.first)
    {
        parent-&gt;_right = cur;
        cur-&gt;_parent = parent;
    }
    else
    {
        parent-&gt;_left = cur;
        cur-&gt;_parent = parent;
    }

    while (cur != _root)
    {
        if (cur == parent-&gt;_left)
            parent-&gt;_bf--;
        else
            parent-&gt;_bf++;

        if (parent-&gt;_bf == 0)
            break;
        else if (parent-&gt;_bf == 1 || parent-&gt;_bf == -1)
        {
            cur = parent;
            parent = parent-&gt;_parent;
        }
        else if (parent-&gt;_bf == 2 || parent-&gt;_bf == -2)
        {
            if (parent-&gt;_bf == 2) //说明右子树更高
            {
                if (cur-&gt;_bf == 1) //说明新节点插入到了右边，符合在更高右子树的右侧插入的情况
                {
                    RotateLeft(parent); //执行左单旋
                }
                else if (cur-&gt;_bf == -1) //说明新节点插入到了左边，符合在更高右子树的左侧插入的情况
                {
                    RotateRL(parent); //执行右左双旋
                }
            }
            else //左子树更高
            {
                if (cur-&gt;_bf == 1) //说明新节点插入到了右边，符合在更高左子树的右侧插入的情况
                {
                    RotateLR(parent); //执行左右双旋
                }
                else if (cur-&gt;_bf == -1) //说明新节点插入到了左边，符合在更高左子树的左侧插入的情况
                {
                    RotateRight(parent); //执行右单旋
                }
            }
            break;
        }
        else
        {
            assert(false);
        }
    }

    return true;
}
```

---


## 六、AVL树的验证

### 6.1 验证有序

最重要的插入节点部分完成了，不过在验证是否符合AVL树性质前，我们首先需要验证其是否是一棵二叉搜索树

在之前讲解二叉搜索树中提到过，如果中序遍历能够得到一个有序的序列，就说明是二叉搜索树

中序遍历代码如下：

```
void InOrder()
{
    _InOrder(_root);
    cout &lt;&lt; endl;
}

void _InOrder(Node *root)
{
    if (root == nullptr)
        return;
    _InOrder(root-&gt;_left);
    cout &lt;&lt; root-&gt;_kv.first &lt;&lt; " "; // key/value模型，我们只打印key即可
    _InOrder(root-&gt;_right);
}
```

验证：

说明符合二叉搜索树性质

### 6.2 验证平衡

要验证是否符合AVL树性质，只需要检测它的所有节点的子树高度差不超过1即可

需要注意的是，这里不可以直接通过判断平衡因子的绝对值是否大于1来验证平衡，因为平衡因子是不客观的，可以被修改

因此，我们通过递归来得到每棵子树的高度并进行判断即可

代码如下：

```
bool IsBalance()
{
    return _IsBalance(_root);
}

bool _IsBalance(Node *root)
{
    if (root == nullptr)
        return true;
    int leftHeigit = _Height(root-&gt;_left);
    int rightHeight = _Height(root-&gt;_right);
    if (rightHeight - leftHeigit != root-&gt;_bf)
    {
        cout &lt;&lt; root-&gt;_kv.first &lt;&lt; "平衡因子异常" &lt;&lt; endl;
        return false;
    }

    return abs(rightHeight - leftHeigit) &lt;= 1 
        &amp;&amp; _IsBalance(root-&gt;_left) 
        &amp;&amp; _IsBalance(root-&gt;_right);
}

int Height()
{
    return _Height(_root);
}

int _Height(Node *root)
{
    if (root == nullptr)
        return 0;
    int higher = max(_Height(root-&gt;_left), _Height(root-&gt;_right));
    return higher + 1;
}
```

验证：

如果在验证是否是AVL树中需要更多大量的测试用例，我们可以取一些随机数：

```
int main()
{
	const int N = 1000;
	vector&lt;int&gt; v;
	v.reserve(N);
	srand(time(0));

	for (int i = 0; i &lt; N; i++)
	{
		v.push_back(rand() + i);
	}

	AVLTree&lt;int, int&gt; t;
	for (auto i : v)
	{
		t.insert(make_pair(i, 1));
	}
	t.InOrder();
	if (t.IsBalance())
		cout &lt;&lt; "是AVL树" &lt;&lt; endl;
	else
		cout &lt;&lt; "不是AVL树" &lt;&lt; endl;
	return 0;
}
```

 

---


## 七、AVL树的删除

AVL树的删除并不是本文的重点，因为其原理我们在前面已经学习过了

我们只需要按照二叉搜索树的方式来对目标节点进行删除，再判断是否失衡，如果失衡则旋转即可

---


## 八、AVL树的性能和代码

AVL树追求的是严格平衡，因此可以保证查找时高效的时间复杂度O(logN)，但是如果我们需要频繁的对其进行旋转来维护平衡，一定程度上会影响效率，尤其是删除节点时的最差情况下我们可能需要一路旋转到根的位置。

相对于AVL树的严格平衡，红黑树则追求一种相对平衡，因此会略胜一筹，后面的文章中会对红黑树进行讲解。

AVL树的完整代码如下：

```
template&lt;class K,class V&gt;
struct AVLTreeNode
{
	AVLTreeNode&lt;K, V&gt;* _left;
	AVLTreeNode&lt;K, V&gt;* _right;
	AVLTreeNode&lt;K, V&gt;* _parent;
	
	pair&lt;K, V&gt; _kv;
	int _bf; //平衡因子

	AVLTreeNode(const pair&lt;const K, V&gt;&amp; kv)
		:_left(nullptr)
		,_right(nullptr)
		,_parent(nullptr)
		,_kv(kv)
		,_bf(0)
	{}
};

template&lt;class K, class V&gt;
class AVLTree
{
	typedef AVLTreeNode&lt;K, V&gt; Node;
public:
	bool insert(const pair&lt;const K, V&gt;&amp; kv)
	{
		if (_root == nullptr)
		{
			_root = new Node(kv);
			return true;
		}

		Node* parent = nullptr;
		Node* cur = _root;

		while (cur)
		{
			parent = cur;
			if (kv.first &gt; cur-&gt;_kv.first)
				cur = cur-&gt;_right;
			else if (kv.first &lt; cur-&gt;_kv.first)
				cur = cur-&gt;_left;
			else
				return false;
		}

		cur = new Node(kv);
		if (kv.first &gt; parent-&gt;_kv.first)
		{
			parent-&gt;_right = cur;
			cur-&gt;_parent = parent;
		}
		else
		{
			parent-&gt;_left = cur;
			cur-&gt;_parent = parent;
		}

		while (cur != _root)
		{
			if (cur == parent-&gt;_left)
				parent-&gt;_bf--;
			else
				parent-&gt;_bf++;

			if (parent-&gt;_bf == 0)
				break;
			else if (parent-&gt;_bf == 1 || parent-&gt;_bf == -1)
			{
				cur = parent;
				parent = parent-&gt;_parent;
			}
			else if (parent-&gt;_bf == 2 || parent-&gt;_bf == -2)//平衡异常
			{
				if (parent-&gt;_bf == 2)
				{
					if (cur-&gt;_bf == 1)
					{
						RotateLeft(parent);
					}
					else if (cur-&gt;_bf == -1)
					{
						RotateRL(parent);
					}
				}
				else
				{
					if (cur-&gt;_bf == 1)
					{
						RotateLR(parent);
					}
					else if (cur-&gt;_bf == -1)
					{
						RotateRight(parent);
					}
				}
				break;
			}
			else
			{
				assert(false);
			}
		}

		return true;
	}

	void RotateLeft(Node* parent) //新节点插入较高右子树的右侧：左单旋
	{
		Node* subR = parent-&gt;_right;
		Node* subRL = subR-&gt;_left;

		parent-&gt;_right = subRL;
		if(subRL)
			subRL-&gt;_parent = parent;

		Node* parentParent = parent-&gt;_parent;

		if (parent != _root)
		{
			subR-&gt;_parent = parentParent;
			if (parent == parentParent-&gt;_left)
				parentParent-&gt;_left = subR;
			else
				parentParent-&gt;_right = subR;
		}
		else
		{
			_root = subR;
			subR-&gt;_parent = nullptr;
		}

		subR-&gt;_left = parent;
		parent-&gt;_parent = subR;

		parent-&gt;_bf = subR-&gt;_bf = 0;
	}

	void RotateRight(Node* parent) //新节点插入较高左子树的左侧：右单旋
	{
		Node* subL = parent-&gt;_left;
		Node* subLR = subL-&gt;_right;

		parent-&gt;_left = subLR;
		if (subLR)
			subLR-&gt;_parent = parent;

		Node* parentParent = parent-&gt;_parent;

		if (parent != _root)
		{
			subL-&gt;_parent = parentParent;
			if (parent == parentParent-&gt;_left)
				parentParent-&gt;_left = subL;
			else
				parentParent-&gt;_right = subL;
		}
		else
		{
			_root = subL;
			subL-&gt;_parent = nullptr;
		}

		subL-&gt;_right = parent;
		parent-&gt;_parent = subL;

		parent-&gt;_bf = subL-&gt;_bf = 0;
	}

	void RotateRL(Node* parent)
	{
		Node* subR = parent-&gt;_right;
		Node* subRL = subR-&gt;_left;
		int bf = subRL-&gt;_bf;

		RotateRight(subR);
		RotateLeft(parent);

		if (bf == 0)
		{
			parent-&gt;_bf = subR-&gt;_bf = subRL-&gt;_bf = 0;
		}
		else if (bf == 1)
		{
			parent-&gt;_bf = -1;
			subR-&gt;_bf = subRL-&gt;_bf = 0;
		}
		else if (bf == -1)
		{
			subR-&gt;_bf = 1;
			parent-&gt;_bf = subRL-&gt;_bf = 0;
		}
		else
		{
			assert(false);
		}
	}

	void RotateLR(Node* parent)
	{
		Node* subL = parent-&gt;_left;
		Node* subLR = subL-&gt;_right;
		int bf = subLR-&gt;_bf;

		RotateLeft(subL);
		RotateRight(parent);

		if (bf == 0)
		{
			parent-&gt;_bf = subL-&gt;_bf = subLR-&gt;_bf = 0;
		}
		else if (bf == 1)
		{
			subL-&gt;_bf = -1;
			parent-&gt;_bf = subLR-&gt;_bf = 0;
		}
		else if (bf == -1)
		{
			parent-&gt;_bf = 1;
			subL-&gt;_bf = subLR-&gt;_bf = 0;
		}
		else
		{
			assert(false);
		}
	}

	void InOrder()
	{
		_InOrder(_root);
		cout &lt;&lt; endl;
	}

	bool IsBalance()
	{
		return _IsBalance(_root);
	}

	int Height()
	{
		return _Height(_root);
	}

	size_t Size()
	{
		return _Size(_root);
	}

	Node* Find(const K&amp; key)
	{
		Node* cur = _root;
		while (cur)
		{
			if (key &gt; cur-&gt;_kv.first)
				cur = cur-&gt;_right;
			else if (key &lt; cur-&gt;_kv.first)
				cur = cur-&gt;_left;
			else
				return cur;
		}
		return nullptr;
	}
private:
	void _InOrder(Node* root)
	{
		if (root == nullptr)
			return;
		_InOrder(root-&gt;_left);
		cout &lt;&lt; root-&gt;_kv.first &lt;&lt; " ";
		_InOrder(root-&gt;_right);
	}

	bool _IsBalance(Node* root)
	{
		if (root == nullptr)
			return true;
		int leftHeigit = _Height(root-&gt;_left);
		int rightHeight = _Height(root-&gt;_right);
		if (rightHeight - leftHeigit != root-&gt;_bf)
		{
			cout &lt;&lt; root-&gt;_kv.first &lt;&lt; "平衡因子异常" &lt;&lt; endl;
			return false;
		}

		return abs(rightHeight - leftHeigit) &lt;= 1 
			&amp;&amp; _IsBalance(root-&gt;_left)
			&amp;&amp; _IsBalance(root-&gt;_right);
	}

	int _Height(Node* root)
	{
		if (root == nullptr)
			return 0;
		int higher = max(_Height(root-&gt;_left), _Height(root-&gt;_right));
		return higher + 1;
	}

	size_t _Size(Node* root)
	{
		if (root == nullptr)
			return 0;
		return _Size(root-&gt;_left) + _Size(root-&gt;_right) + 1;
	}
private:
	Node* _root = nullptr;
};

```

如果有错误的地方，欢迎在评论区指出

完.
