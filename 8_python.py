class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        Len = len(str)
        while i < Len:
            if str[i] == ' ' or str[i] == '\t' or str[i] == '\n':
                i = i + 1
            else:
                break
        if Len == i:
            return 0
        f = 1
        flag = 0
        if str[i] == '+' and Len > 1:
            flag = 1
            i = i + 1
        elif str[i] == '+' and Len == 1:
            return 0
        if str[i] == '-' and flag == 0:
            f = -1
            i = i + 1
        elif str[i] == '-' and flag == 1:
            return 0
        maxInt = 2 ** 31 - 1
        minInt = -maxInt - 1
        x = 0
        while i < Len and str[i] >= '0' and str[i] <= '9' and x <= maxInt and x * f >= minInt:
            x = x * 10 + int(str[i])
            i = i + 1
        x = x * f
        if x > maxInt:
            return maxInt
        if x < minInt:
            return minInt
        return x