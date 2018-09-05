vector <string> ans;
void dfs(string s, int l, int r, int n) {
    if (s.length() == n * 2) {
        ans.push_back(s);
        return ;
    }
    string ss = s;
    if (l < n) {
        s.push_back('(');
        dfs(s, l + 1, r, n);
    }
    if (l > r) {
        ss.push_back(')');
        dfs(ss, l, r + 1, n);
    }
}
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        ans.clear();
        string nil = "";
        dfs(nil, 0, 0, n);
        return ans;
    }
};
