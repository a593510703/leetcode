class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0:
            return ""
        minLen = min(len(strs[i]) for i in range(n))
        for Len in range(minLen):
            for i in range(1, n):
                if strs[0][Len] != strs[i][Len]:
                    return strs[0][:Len]
        return strs[0][:minLen]