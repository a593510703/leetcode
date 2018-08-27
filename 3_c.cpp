static const auto io_speed_up = []()
{
	std::ios::sync_with_stdio(false);
	cin.tie(nullptr);
	return 0;
}();
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int len = s.length(), j, vis[2600], ans = -1;
        for (int i = 0; i < len; i++) {
            memset(vis, 0, sizeof(vis));
            j = i;
            while (!vis[s[j]] && j < len)
                vis[s[j++]] = 1;
            ans = max(ans, j - i);
        }
        return ans == -1 ? 0 : ans;
    }
};
