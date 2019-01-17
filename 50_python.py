class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pow(x, n):
            if n < 0:
                return 1 / pow(x, -n)
            if n == 1:
                return x
            if n == 0:
                return 1
            if n == 2:
                return x * x
            if n % 2:
                X = pow(x, (n - 1) // 2)
                return X * X * x
            else:
                X = pow(x, n // 2)
                return X * X
        return pow(x, n)