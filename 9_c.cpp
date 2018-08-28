class Solution {
public:
    bool isPalindrome(int x) {
        int s[1000], size = 0;
        memset(s, 0, sizeof(s));
        if (x < 0)
            return false;
        while (x) {
            s[++size] = x % 10;
            x /= 10;
        }
        for (int i = 1; i <= size / 2 + 1; i++)
            if (s[i] != s[size - i + 1])
                return false;
        return true;
    }
};
