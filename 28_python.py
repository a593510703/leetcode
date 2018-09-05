class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len1 = len(haystack)
        len2 = len(needle)
        if len2 == 0:
            return 0
        if len1 == len2 and haystack != needle:
            return -1
        for sta in range(len1 - len2 + 1):
            cnt = 0
            for i in range(len2):
                if haystack[sta + i] == needle[i]:
                    cnt += 1
            if cnt == len2:
                return sta
        return -1