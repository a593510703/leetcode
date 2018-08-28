class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = []
        if x < 0:
            return False
        while x:
            s.append(x % 10)
            x = x // 10
        size = len(s) - 1
        for i in range(size):
            if s[i] != s[size - i]:
                return False
        return True