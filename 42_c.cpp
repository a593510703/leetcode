class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = height.size() - 1, ans = 0;
        while (l < r) {
            if (height[l] < height[r]) {
                int Min = height[l];
                while (l < r && height[l] <= Min) {
                    ans += (Min - height[l++]);
                }
            }
            else {
                int Min = height[r];
                while (l < r && height[r] <= Min) {
                    ans += (Min - height[r--]);
                }
            }
        }
        return ans;
    }
};
