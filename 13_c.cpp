class Solution {
public:
    int romanToInt(string s) {
        int len = s.length(), ans = 0;
        map <char, int> Map1;
        map <string, int> Map2;
        Map1['I'] = 1, Map1['V'] = 5, Map1['X'] = 10, Map1['L'] = 50;
        Map1['C'] = 100, Map1['D'] = 500, Map1['M'] = 1000;
        Map2["CM"] = 900, Map2["CD"] = 400, Map2["XC"] = 90;
        Map2["XL"] = 40, Map2["IX"] = 9, Map2["IV"] = 4;
        for (int i = 0; i < len; i++) {
            char sub[2];
            sub[0] = s[i], sub[1] = s[i + 1];
            string Sub(sub);
            if (Map2[Sub] != 0) {
                ans += Map2[Sub];
                i++;
                continue;
            }
            ans += Map1[s[i]];
        }
        return ans;
    }
};
