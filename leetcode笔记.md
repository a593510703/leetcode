### Question 1: Two Sum
[原题链接](https://leetcode-cn.com/problems/two-sum/)
非常裸的Map，不太会用python的map，写了个$n^2$暴力。
python里求某个元素在列表里第一次出现的索引:`列表名.index(元素名)`

### Question 2: Add Two Numbers
[原题链接](https://leetcode-cn.com/problems/add-two-numbers/)
模拟。主要卡在ListNode上，之前一直没用过链表。
c++里`ListNode preHead(0), *p = &preHead;`定义就能存链表的头地址
python里`p = preHead = ListNode(0)`也是一样的道理
知道了这一点之后模拟高精度加法就行了

### Question 3: 无重复字符的最长子串
[原题链接](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)
记一下这个题的滑动窗口思路：枚举滑动窗口的尾部坐标，用Dict存下每个字母**上一次出现**的索引，如果下一个字母已经被用过了，就缩短窗口的大小直至排除上一次出现的字母。

python程序里变量的涵义

- currMax: 当前滑动窗口的长度
- ret: 答案，截止目前滑动窗口长度的最大值
- lastIndex: 记录每个字母上一次出现的索引，用来计算新的currMax的大小

### Question 4: 两个排序数组的中位数
[原题链接](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/)
很裸的归并排序，顺便练了一下vector的使用。vector排序确实非常僵硬。
python里`/`是返回float的除法，写在数组下标里要用`//`

### Question 5: 最长回文子串
[原题链接](https://leetcode-cn.com/problems/longest-palindromic-substring/description/)
Manacher的模板题。用Manacher算出Len数组就行了。
python列表转字符串：`"".join(字符串名)`
python真的好用，爱他

### Question 6: Z字形变换
[原题链接](https://leetcode-cn.com/problems/zigzag-conversion/description/)
没有意义的模拟。不知道为什么c++程序一直re, 就交了个标程。很烦。

### Question 7: 反转整数
[原题链接](https://leetcode-cn.com/problems/reverse-integer/description/)
非常简单，没什么好说的。注意溢出就行。溢出的主语是反转后的整数，所以判断要放在最后而不是一开始

### Question 8: 字符串转整数 (atoi)
[原题链接](https://leetcode-cn.com/problems/string-to-integer-atoi/description/)
非常考验细节的一道题，感觉提交了一百万次。
而且python的bug谜之比c++的bug多，不知道为撒。

### Question 9: 回文数
[原题链接](https://leetcode-cn.com/problems/palindrome-number/description/)
大水题，注意判负就行

### Question 10: 正则表达式匹配
[原题链接](https://leetcode-cn.com/problems/regular-expression-matching/description/)
这个题还是要好好写写的。如果走python的话re模块三行就能搞定
```python3
class Solution:
    def isMatch(self, s, p):
        return s in re.findall(p, s)
        return bool(re.match(p, s)) and re.match(p, s).group(0) == s
```
最后两行随便选一行就行。
走c++或者不用re模块的话这个题就非常困难了。往dp的方向定义dp的意义，要让他没有后效性而且是最优化的，可以这么定义
dp[i][j]: 表示s的前i个字符和p的前j个字符能否匹配，能匹配即为1，反之为0

首先考虑边界，根据定义：`dp[0][0] = 1, dp[0][1] = 0, dp[i][0] = 0(i >= 1)`
注意到`'*'`可以匹配零次，第一个状态转移方程就是`dp[i][j] = dp[i][j - 2] (p[j - 1] = '*')`
再考虑`'*'`匹配多次的情况，如果`p[j - 1] != '*'`，就只需要判断`s[i - 1]`和`p[j - 1]`的关系，即：`dp[i][j] = dp[i - 1][j - 1] (p[j - 1] != '*' && dp[i - 1][j - 1])`
如果`p[j - 1] == '*'`，则又分为两种情况，一种是匹配零次的情况（和之前一样，考虑`dp[i][j - 2]`的值）。另一种是匹配多次的情况，这时候要检查`dp[i - 1][j]`的值和`p[j - 2]`是否匹配。时间复杂度看起来是$O(nm)$。感觉效率不是很高，不知道re模块内部怎么写的（挖个坑以后看看re的代码

### Question 11: 盛最多水的容器
[原题链接](https://leetcode-cn.com/problems/container-with-most-water/description/)
这个题一开始只能想到n^2的解法，1000ms+慢死。
记一下std里一种从两边逼近的方法，遍历容器宽度(从n到0)。left & right指针一开始指向数组的最左和最右，每次循环，对于每一组(left, right)，检查这组(left, right)是否能更新答案。然后更新left和right的值。
如果`height[left] < height[right]`，即现在的容器左低右高，就说明可以尝试将left指针右移，因为向右移可以最大化`min(height[left], height[right])`（？）。或者另一种理解是向右移动指针更有“潜力”。
对于`height[left] >= height[right]`的情况也是一样，尝试将right指针左移就行
[这里](https://leetcode-cn.com/problems/container-with-most-water/solution/)也说了一些关于这个算法的正确性证明

### Question 12: 整数转罗马数字
[原题链接](https://leetcode-cn.com/problems/integer-to-roman/description/)
一个打表题，枚举一下1, 4, 5, 9的情况对应的字符串就行。
表看github吧。

### Question 13: 罗马数字转整数
[原题链接](https://leetcode-cn.com/problems/roman-to-integer/description/)
和上一题一样的打表题，略显麻烦。python的Dict使用的还不熟练
c++中char[]转化成string: `char sub[Maxn], ..., string Sub(sub);`
python中两个列表转化成一个Dict: `dict(zip(list1, list2))`
python中切片: 左闭右开

### Question 14: 最长公共前缀
[原题链接](https://leetcode-cn.com/problems/longest-common-prefix/description/)
停课的时候做过一次这个题。小优化就是预处理算出来最短字符串长度，然后枚举每一位就行。
python真的是太棒了，太接近于自然语言了。没有学过相关的语法随便写一下就能用真是太帅了。
c++ string 在字符串最后加一个字符: `str.push_back('a');`

### Question 15: 三数之和
[原题链接](https://leetcode-cn.com/problems/3sum/description/)
c++ stl大法好！！！！Beats 98.8%卧槽！！！太激动了！！！
基本思路：排序数组。枚举每一个数，在这个数后的切片里用双指针法找 让双指针对应的两个数和为Target的指针。如果两数之和偏大就左移右指针，反之右移左指针。
小优化: 如果`nums[i] > 0`，则肯定找不到对应的解，可以直接`continue`
vector奇技淫巧:

- 排序：`sort(v.begin(), v.end());`
- 去重：`v.erase(unique(v.begin(), v.end()), v.end());`
- 改变大小：`v.resize(n)`

不resize的话leetcode会报出奇怪错误要注意。
这个题一开始的答案要resize一个很大的数，因为可能满足的答案在没有去重之前有很多。

### Question 16: 最接近的三数之和
[原题链接](https://leetcode-cn.com/problems/3sum-closest/description/)
又是这种类型的题...主要有两点优化：如果`nums[i] + nums[left] + nums[left + 1] > target`，因为数组是升序的，所以以后的三数之和一定比target大，没有任何意义。可以直接把这个存入ans数组，不用进行其他操作。`nums[i] + nums[right - 1] + nums[right] < target`也是同理。这两个情况都不满足就只能朴素的求三数之和了。最后在ans数组里找最近的就行。
python找距离target最近的元素: `ans.sort(key=lambda x:abs(x - target));return ans[0]`

### Question 17: 电话号码的字母组合
[原题链接](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/)
c++的话写的bfs, Beats 100%！python可以用自带的字符串拼接方法，Beats 90.57%一样效率不低。python的话代码复杂度很低，c++要上各种stl。
bfs就是写起来麻烦点，思路还是挺简单的
c++ string删除最后一个元素: `s.pop_back();`

### Question 18: 四数之和
[原题链接](https://leetcode-cn.com/problems/4sum/description/)
一个大坑

### Question 19: 删除链表的倒数第N个节点
[原题链接](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/)
练对链表的熟悉程度的题，注意一下删除第一位和链表为空的情况就好。
看了最佳程序，可以不用算出来链表长度。太牛逼了这个。
定义了两个指针，一开始只有end指针移动，移动n次。还要移动len - n次。
移动n次后cur指针和end指针一起移动，当end指针移动到null时，cur指针移动到了len - n，刚好是倒数第n个元素。然后进行操作就行了。太牛逼了这个方法：）我的c++才Beats 4.75%。
自己还是垃圾啊：）

### Question 20: 有效的括号
[原题链接](https://leetcode-cn.com/problems/valid-parentheses/description/)
一道栈的裸题，手写一个栈就行。注意考虑栈空的情况和字符串长度为奇数的情况。

### Question 21: 合并两个有序链表
[原题链接](https://leetcode-cn.com/problems/merge-two-sorted-lists/description/)
又是归并。
leetcode的设计卡了一手我。定义初始化的时候**一定**要用`ListNode *p = new ListNode(-1);`
用`ListNode *p(-1);`会有各种各样的傻逼问题。千万别用这个，用上面那个。

### Question 22: 括号生成
[原题链接](https://leetcode-cn.com/problems/generate-parentheses/description/)
一个dfs。但是一开始只能看出来是dfs不会写...真是废了
dfs枚举的思路，对于每一个状态

- 如果左括号不够，就在最后加上左括号
- 如果右括号少了，就在最后加上右括号

然后递归到下一个状态，直到状态对应的字符串满足要求了(l = r = n)，就记录下这个答案，return之。这样就能相对快速的得出答案了。
相比$O(2^{2n})$的解法剪掉了右括号在左括号之前，和右括号多于左括号的情况。

### Question 23: 合并K个排序链表
[原题链接](https://leetcode-cn.com/problems/merge-k-sorted-lists/description/)
看起来很恐怖，tag里写的堆和分治。但是好像取出来所有元素，然后nlgn排序再塞入元素就好。时间复杂度就是$O(nlogn)$。这么写python还Beats 97%。真是超乎想象的简单。
c++的最快程序用了二分参数，感觉麻烦又神奇。挖个坑之后看。

### Question 24: 两两交换链表中的节点
[原题链接](https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/)
有点像删除节点，思路还是挺简单的，纸上乱画就行了。
c++比较麻烦。一开始用的while，没想到用递归解决问题。while调不出来就去投奔百度了。才反应过来while可以用递归来代替。递归可读性更加强一点，也更加容易理解。
python里一行代码好像是同时进行的，所以不需要设置tmp变量就能完成节点交换。

### Question 25: k个一组翻转链表
[原题链接](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/)
太难了

### Question 26: 删除排序数组中的重复项
[原题链接](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/description/)
c++ stl大法好，两行解决了所有问题还Beats 95.4% ：）爱他
python的话好像只能朴素的算，从前向后找与pre不同的元素，然后更新列表的前一部分和pre就行。就是写起来麻烦点，需要画一画才比较直观

### Question 27: 移除元素
[原题链接](https://leetcode-cn.com/problems/remove-element/description/)
大水题。因为题目奇怪的要求，只能遍历整个vector/list，找到和val相等的数就把他放在最后，然后让返回值大小-1。就能起到erase的作用了。

### Question 28: 实现strStr()
[原题链接](https://leetcode-cn.com/problems/implement-strstr/description/)
纯模拟。好像能算是个kmp的练手题，但是看最优程序用的是模拟而不是kmp。好迷。
能优化的点：如果`sta > haystack.length() - needle.length() + 1`，则肯定不会包含needle。可以直接剪掉这一部分。
注意题目给的特例：`if (needle.empty()) return 0;`
python还可以直接用切片和needle做比较，很牛逼。

### Question 29: 两数相除
[原题链接](https://leetcode-cn.com/problems/divide-two-integers/description/)
想了好久，想到各种方法。特判，暴力，高精度都不能在题目的时限和要求下完成这个问题。所以去舔了题解：）看下面这个连等式感觉一看就能看懂。
$\frac{100}{3} = \frac{100}{6} \times 2^1 = \frac{100}{12} \times 2^2 = \frac{100}{24} \times 2^3= \frac{100}{48} \times 2^4 = \frac{100}{96} \times 2^5$
ban了乘除和mod运算，还有能高效运算的左移右移等一系列二进制运算法则。一开始就直接忽略了，以为只能加减乘除。想到这个公式这个题就简单多了。

### Question 32: 最长有效括号
[原题链接](https://leetcode-cn.com/problems/longest-valid-parentheses/description/)
一开始以为是dp，状态转移方程：
`dp[i][j] = max(dp[i][j], x), x = dp[i][j - 2] + 2 (当j-1, j为一对括号时) / 
dp[i + 2][j] + 2 (当i, i+1为一对括号时) / dp[i + 1][j - 1] + 2 (当i, j为一对括号时)`
但是数据量太大导致不能用$O(n^2)$的算法。之后想了好久的$O(n)$的dp都没有想到。
然后舔了题解，发现一个手写栈就能搞定。思路都被局限在dp上就没有考虑其他的方向。
栈的思路很明显，如果是`'('`就压进去。如果是`')'`就判断一下栈顶元素和次顶元素，对栈做出一些改变就行。想到栈的话就非常好做了。

### Question 33: 搜索旋转排序数组
[原题链接](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/)
题目规定了复杂度。列出题目给的条件：两个数组有序，左边数组最小值>右边数组最大值。
关键点就是怎么用$O(lgn)$的时间找到中间的那个点。想了好久线段树相关，甚至还想了一下状态压缩：）有点太傻逼了。考虑到中间数字的特殊性：左边数字 < 中间数字 > 右边数字和其他数字做比较。就可以基于此进行二分查找。
找到中间点后问题就变得容易了，再有序数组里$O(lgn)$的时间找到特定值是非常简单的。注意一下边界就行了。
