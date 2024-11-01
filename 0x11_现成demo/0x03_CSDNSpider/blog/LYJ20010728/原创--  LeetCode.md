# 原创
：  LeetCode

# LeetCode

#### LeetCode

## 53-最大子序和

> 
动态规划转移方程为：f(i)=max{f(i−1)+nums[i],nums[i]}


```
class Solution {
public:
    int maxSubArray(vector&lt;int&gt;&amp; nums) {
        int pre = 0;
        int maxAns = nums[0];
        for (const auto &amp;x: nums) {
            pre = max(pre+x, x);
            maxAns = max(maxAns, pre);
        }
        return maxAns;
    }
};

```

## 66-加一

> 
只有为9的时候才需要对该位前面的数进行操作，否则直接对该一位加一即可，如果该数组里面元素全部为9，则结果一定为1 后面len(digits的长度)个0


```
class Solution {
public:
    vector&lt;int&gt; plusOne(vector&lt;int&gt;&amp; digits) {
        int len = digits.size();
        for (int i = len - 1; i &gt;= 0; --i) {
            if (digits[i] == 9) {
                digits[i] = 0;
            } else {
                digits[i]++;
                return digits;
            }
        }
        vector&lt;int&gt; temp(len+1,0);
        temp[0] = 1;
        return temp;
    }
};

```

## 108-合并两个有序数组

> 
利用双指针，将两个数组看作队列，每次从两个数组头部取出比较小的数字放到结果中


```
class Solution {
public:
    void merge(vector&lt;int&gt;&amp; nums1, int m, vector&lt;int&gt;&amp; nums2, int n) {
        int p1 = 0, p2 = 0;
        int sortedList[m+n];
        int cur;
        while (p1 &lt; m || p2 &lt; n) {
            if (p1 == m) {
                cur = nums2[p2++];
            } else if (p2 == n) {
                cur = nums1[p1++];
            } else if (nums1[p1] &lt; nums2[p2]) {
                cur = nums1[p1++];
            } else {
                cur = nums2[p2++];
            }
            sortedList[p1+p2-1] = cur;
        }
        int temp = m + n;
        while (temp) {
            nums1[temp-1] = sortedList[temp-1];
            --temp;
        }
    }
};

```

## 118-杨辉三角

> 
每个数字等于上一行的左右两个数字之和，可用此性质写出整个杨辉三角


```
class Solution {
public:
    vector&lt;vector&lt;int&gt;&gt; generate(int numRows) {
        vector&lt;vector&lt;int&gt;&gt; temp(numRows);
        for (int i = 0 ; i &lt; numRows; ++i) {
            temp[i].resize(i+1);
            temp[i][0] = temp[i][i] = 1;
            for (int j = 1; j &lt; i; ++j) {
                temp[i][j] = temp[i-1][j] + temp[i-1][j-1];
            }
        }
        return temp;
    }
};

```

## 119-杨辉三角 II

> 
使用滚动数组的思想优化空间复杂度


```
class Solution {
public:
    vector&lt;int&gt; getRow(int rowIndex) {
        vector&lt;int&gt; cur,pre;
        for (int i = 0; i &lt;= rowIndex; ++i) {
            cur.resize(i+1);
            cur[0] = cur[i] = 1;
            for (int j = 1; j &lt; i; ++j) {
                cur[j] = pre[j-1] + pre[j];
            }
            pre = cur;
        }
        return pre;
    }
};

```
