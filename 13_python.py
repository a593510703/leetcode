class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        y = [1, 5, 10, 50, 100, 500, 1000]
        X = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']
        Y = [900, 400, 90, 40, 9, 4]
        Len = len(s)
        ans = 0
        pre = 0
        i = 0
        while True:
            if i >= Len:
                break
            tmp = s[i:i + 2]
            pre = ans
            for j in range(6):
                if tmp == X[j]:
                    ans = ans + Y[j]
            if ans > pre:
                i = i + 2
                continue
            for j in range(7):
                if s[i] == x[j]:
                    ans = ans + y[j]
            i = i + 1
        return ans