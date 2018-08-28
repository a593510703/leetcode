class Solution {
public:
    string longestPalindrome(string s) {
        string st;
        int len = s.length();
        st[0] = '#';
        for (int i = 1; i <= len * 2; i += 2) {
            st[i] = '#';
            st[i + 1] = s[i / 2];
        }
        st[2 * len + 1] = '#';
        st[2 * len + 2] = '$';
        st[2 * len + 3] = '\0';
        len = len * 2 + 2;
        int mx = 0, ans = 0, po = 0, Len[1001], pos;
        memset(Len, 0, sizeof(Len));
        for (int i = 1; i <= len; i++) {
            if (mx > i)
                Len[i] = min(Len[2 * po - i], mx - i);
            else
                Len[i] = 1;
            while (st[i - Len[i]] == st[i + Len[i]])
                Len[i]++;
            if (Len[i] + i > mx) {
                mx = Len[i] + i;
                po = i;
            }
            if (ans < Len[i]) {
                ans = Len[i];
                pos = i;
            }
        }
        string ret;
        int size = 0;
        for (int i = pos - ans; i <= pos + ans; i++) {
            if (st[i] != '#')
                ret[++size] = st[i];
        }
        cout << endl << ret;
        return ret;
    }
};
