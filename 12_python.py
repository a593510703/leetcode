class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        x = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        y = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ret = ''
        for i in range(len(x)):
            while num // x[i] > 0:
                num = num - x[i]
                ret += y[i]
        return ret