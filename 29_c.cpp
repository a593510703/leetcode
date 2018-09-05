long solve(long dividend, long divisor) {
    long ans = 1, Divisor = divisor;
    if (dividend < divisor)
        return 0;
    if (dividend == divisor)
        return 1;
    while (dividend >= divisor) {
        divisor <<= 1;
        ans <<= 1;
    }
    divisor >>= 1;
    ans >>= 1;
    if (divisor == dividend)
        return ans;
    return ans + solve(dividend - divisor, Divisor);
}

class Solution {
public:
    int divide(long dividend, long divisor) {
        long f = 1;
        if (dividend < 0) {
            f = -1;
            dividend = 0 - dividend;
        }
        if (divisor < 0) {
            f = f == 1 ? -1 : 1;
            divisor = 0 - divisor;
        }
        f *= solve(dividend, divisor);
        if (f > 2147483647 || f < -2147483648)
            return 2147483647;
        return f;
    }
};
