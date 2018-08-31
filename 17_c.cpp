class Solution {
public:
    vector<string> letterCombinations(string digits) {
        map <char, string> Map;
        vector <string> ans(0);
        queue <string> q;
        Map['2'] = "abc", Map['3'] = "def";
        Map['4'] = "ghi", Map['5'] = "jkl", Map['6'] = "mno";
        Map['7'] = "pqrs", Map['8'] = "tuv", Map['9'] = "wxyz";
        int len = digits.length(), x = 1;
        if (len == 0)
            return ans;
        for (int i = 0; i < len; i++) {
            x *= Map[digits[i]].length();
        }
        string s = "a";
        for (int i = 0; i < Map[digits[0]].length(); i++) {
            s[0] = Map[digits[0]][i];
            q.push(s);
        }
        while (q.size() != x) {
            string sta = q.front();
            q.pop();
            int Len = sta.length();
            for (int i = 0; i < Map[digits[Len]].length(); i++) {
                sta.push_back(Map[digits[Len]][i]);
                q.push(sta);
                sta.pop_back();
            }
        }
        while (!q.empty()) {
            ans.push_back(q.front());
            q.pop();
        }
        return ans;
    }
};
