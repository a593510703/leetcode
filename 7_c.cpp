class Solution {
public:
    int reverse(int x) {
        long long f = 1, ans = 0;
        if (x < 0) {
            f = -1;
            x = -x;
        }
        if (x == 0)
            return 0;
        while (x) {
            ans = ans * 10 + x % 10;
            x /= 10;
        }
        ans *= f;
        if (ans > (1 << 31) - 1 || ans < -(1 << 31))
            return 0;
        return ans;
    }
};
