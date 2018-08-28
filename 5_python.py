def Manacher(s):
    s = '#' + '#'.join(s) + '#'
    RL = [0] * len(s)
    MaxRight = pos = MaxLen = 0
    for i in range(len(s)):
        if i < MaxRight:
            RL[i] = min(RL[2 * pos - i], MaxRight - i)
        else:
            RL[i] = 1
        while i >= RL[i] and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
            RL[i] = RL[i] + 1
        if RL[i] + i - 1 > MaxRight:
            MaxRight = RL[i] + i - 1
            pos = i
        if MaxLen < RL[i]:
            MaxLen = RL[i]
            index = i
    return [MaxLen - 1, index, s]
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        Str = []
        x = y = size = 0
        [x, y, Str] = Manacher(s)
        ret = [0] * x
        for i in range(y - x, x + y):
            if Str[i] == '#':
                continue
            ret[size] = Str[i]
            size = size + 1
        return "".join(ret)