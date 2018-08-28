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

dp[i][j]
:   表示s的前i个字符和p的前j个字符能否匹配，能匹配即为1，反之为0

首先考虑边界，根据定义：`dp[0][0] = 1, dp[0][1] = 0, dp[i][0] = 0(i >= 1)`
注意到'*'可以匹配零次，第一个状态转移方程就是`dp[i][j] = dp[i][j - 2] (p[j - 1] = '*')`
再考虑'*'匹配多次的情况，如果`p[j - 1] != '*'`，就只需要判断s[i - 1]和p[j - 1]的关系，即：`dp[i][j] = dp[i - 1][j - 1] (p[j - 1] != '*' && dp[i - 1][j - 1])`
如果`p[j - 1] == '*'`，则又分为两种情况，一种是匹配零次的情况（和之前一样，考虑dp[i][j - 2]的值）。另一种是匹配多次的情况，这时候要检查dp[i - 1][j]的值和p[j - 2]是否匹配。时间复杂度看起来是O(nm)。感觉效率不是很高，不知道re模块内部怎么写的（挖个坑以后看看re的代码
