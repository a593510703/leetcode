class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size(), minLen = 2147483647;
        string ret;
        if (n == 0)
            return "";
        for (int i = 0; i < n; i++)
            if (strs[i].length() < minLen) {
                minLen = strs[i].length();
            }
        for (int len = 0; len <= minLen; len++) {
            for (int i = 1; i < n; i++) {
                if (strs[0][len] != strs[i][len]) {
                    for (int j = 0; j < len; j++) {
                        ret.push_back(strs[0][j]);
                    }
                    return ret;
                }
            }
        }
        for (int i = 0; i < minLen; i++) {
            ret.push_back(strs[0][i]);
        }
        return ret;
    }
};
