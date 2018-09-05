def solve(dividend, divisor):
    if dividend < divisor:
        return 0
    if dividend == divisor:
        return 1
    ans = 1
    Divisor = divisor
    while dividend > divisor:
        divisor <<= 1
        ans <<= 1
    divisor >>= 1
    ans >>= 1
    if dividend == divisor:
        return ans
    ans += solve(dividend - divisor, Divisor)
    return ans
class Solution():
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        f = 1
        if dividend < 0:
            f = -1
            dividend = 0 - dividend
        if divisor < 0:
            if f == 1:
                f = -1
            elif f == -1:
                f = 1
            divisor = 0 - divisor
        ans = solve(dividend, divisor)
        if f == -1:
            ans = 0 - ans
        if ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 2 ** 31 - 1
        return ans