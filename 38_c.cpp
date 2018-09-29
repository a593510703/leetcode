string solve(string x) {
    string ret;
    int len = x.length(), Len;
    char first;
    for (int i = 0; i < len; i++) {
        first = x[i];
        for (Len = 1; ; Len++) {
            if (first != x[i + 1])
                break;
            i++;
        }
        ret.push_back(Len + '0');
        ret.push_back(first);
    }
    return ret;
}
class Solution {
public:
    string countAndSay(int n) {
        n--;
        string tmp = "1";
        while (n --> 0)
            tmp = solve(tmp);
        return tmp;
    }
};
