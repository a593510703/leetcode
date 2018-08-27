class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = 1
        ans = 0
        if x < 0:
            f = -1
            x = -x
        while x != 0:
            k = x % 10
            x = x // 10
            ans = ans * 10 + k
        x = ans * f
        if x > 2 ** 31:
            return 0
        if x < -2 ** 31:
            return 0
        return x