class Solution {
public:
    int myAtoi(string str) {
        int i = 0, len = str.length();
        for (; i < len;)
            if (str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
                i++;
            else
                break;
        int f = str[i] == '-' ? -1 : 1;
        long long maxInt = (1 << 31) - 1, minInt = -maxInt - 1, x = 0;
        if ((f == -1 && str[i] == '-' ) || str[i] == '+')
            i++;
        while (str[i] >= '0' && str[i] <= '9' && x <= maxInt && x * f >= minInt && i <= len) {
            x = x * 10 + str[i] - '0';
            i++;
        }
        x = x * f;
        if (x > maxInt)
            return maxInt;
        if (x < minInt)
            return minInt;
        return x;
    }
};
