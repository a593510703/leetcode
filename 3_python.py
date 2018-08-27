class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastIndex = {}
        currIndex = ret = 0
        for i in range(len(s)):
            if s[i] in lastIndex and i - lastIndex[s[i]] - 1 <= currIndex:
                if ret < currIndex:
                    ret = currIndex
                currIndex = i - lastIndex[s[i]] - 1
            currIndex = currIndex + 1
            lastIndex[s[i]] = i
        if ret < currIndex:
            ret = currIndex
        return ret