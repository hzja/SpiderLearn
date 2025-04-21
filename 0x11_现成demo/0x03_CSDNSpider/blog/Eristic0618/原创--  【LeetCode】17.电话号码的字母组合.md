# 原创
：  【LeetCode】17.电话号码的字母组合

# 【LeetCode】17.电话号码的字母组合

##  题目

链接：[17. 电话号码的字母组合 - 力扣（LeetCode）](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/)

> 
给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按**任意顺序**返回
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


> 
示例1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]


> 
示例2：
输入：digits = ""
输出：[]


> 
示例3：
输入：digits = "2"
输出：["a","b","c"]


提示：

> 
0 &lt;= digits.length &lt;= 4
digits[i]是范围['2','9']的一个数字


## 思路

本文中的代码使用C++实现，但是思路是共通的

### （1）数字映射字符串

我们需要一个数组保存每个数字对应的字符串，这样digits中的每个数字就能和字符串对应

将字符串在数组中的位置和数字一一对应，我们就可以通过下标访问到对应的字符串

```
vector&lt;string&gt; letter= {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
```

### （2）递归

按照digits中数字找到对应的字符串，将字符串中每个字符进行排列组合即可。

这题不适合使用循环解决，因为digits中数字个数不确定，每个数字也可能对应3或4长度的字符串，所以我们确定大思路：使用递归

因为函数中还有其他的变量，我们需要一个**子函数**来执行递归的程序

在递归中，我们需要记录递归的层数，通过递归的层数来确定返回的条件和选定的数字，例如：

当进入第一层递归，获取digits[0]，并通过这个数字找到其对应的字符串"abc"

使用循环来遍历这个字符串，并在循环中进入下一层递归

进入第二层递归，获取digits[1]，并通过这个数字找到其对应的字符串"ghi"

使用循环来遍历这个字符串，并在循环中进入下一层递归

进入第三层递归，获取digits[2]，并通过这个数字找到其对应的字符串"pqrs"

使用循环来遍历这个字符串，并在循环中进入下一层递归

满足返回条件，自此我们已经获取到了第一个字符组合"agp"

至于如何保存这个字符组合呢？我们需要一个临时的字符串来在递归中保存经过的路径上的字符，并且在最后返回时保存到数组中

将获取到的字符组合保存进数组中，返回到第三层递归，通过循环遍历到下一个字符

到这里，我相信大家已经对递归部分有思路了吧，接下来的步骤就不赘述了，直接展示代码

```
void _letterCombinations(string &amp;digits, vector&lt;string&gt; &amp;ret, string tmp, size_t pile)
    {
        if (pile == digits.size())
        {
            ret.push_back(tmp);
            return;
        }
        int n = digits[pile] - '0';
        string str = letter[n];
        for (auto ch : str)
        {
            _letterCombinations(digits, ret, tmp + ch, pile + 1);
        }
    }
```

其中，ret是我们最后要返回的数组，tmp用来保存字符组合并插入到ret中，pile记录递归层数

### （3）函数主体

在函数主体中只需要对空字符串进行额外的判断即可

```
vector&lt;string&gt; letterCombinations(string digits)
    {
        vector&lt;string&gt; ret;
        if (digits.size() == 0)
        {
            return ret;
        }
        _letterCombinations(digits, ret, "", 0);
        return ret;
    }
```

## 完整代码

```
class Solution
{
    vector&lt;string&gt; letter = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
public:
    void _letterCombinations(string &amp;digits, vector&lt;string&gt; &amp;ret, string tmp, size_t pile)
    {
        if (pile == digits.size())
        {
            ret.push_back(tmp);
            return;
        }
        int n = digits[pile] - '0';
        string str = letter[n];
        for (auto ch : str)
        {
            _letterCombinations(digits, ret, tmp + ch, pile + 1);
        }
    }

    vector&lt;string&gt; letterCombinations(string digits)
    {
        vector&lt;string&gt; ret;
        if (digits.size() == 0)
        {
            return ret;
        }
        _letterCombinations(digits, ret, "", 0);
        return ret;
    }
};

```
