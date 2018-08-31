class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size(), size = 0, left, right;
        vector <int> ans(n << 2);
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n - 2; i++) {
            left = i + 1;
            right = n - 1;
            if (nums[i] + nums[left] + nums[left + 1] > target)
                ans[size++] = nums[i] + nums[left] + nums[left + 1];
            else if (nums[i] + nums[right - 1] + nums[right] < target)
                ans[size++] = nums[i] + nums[right - 1] + nums[right];
            else {
                while (left < right) {
                    int x = nums[i] + nums[left] + nums[right];
                    ans[size++] = x;
                    if (x < target)
                        left++;
                    else if (x > target)
                        right--;
                    else
                        return target;
                }
            }
        }
        int delta = 2147483647, pos;
        for (int i = 0; i < size; i++) {
            if (abs(ans[i] - target) < delta) {
                delta = abs(ans[i] - target);
                pos = i;
            }
        }
        return ans[pos];
    }
};
