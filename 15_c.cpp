class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        vector <vector <int> > ret;
        ret.resize(n << 4);
        for (int i = 0; i < n; i++) {
            ret[i].resize(3);
        }
        vector <int> tmp(3);
        sort(nums.begin(), nums.end());
        int size = 0;
        for (int i = 0; i < n; i++) {
            if (i >= 1 && nums[i - 1] == nums[i])
                continue;
            int target = 0 - nums[i];
            int left = i + 1;
            int right = n - 1;
            if (nums[i] > 0)
                break;
            while (left < right) {
                if (nums[left] + nums[right] > target)
                    right--;
                else if (nums[left] + nums[right] < target)
                    left++;
                else {
                    tmp[0] = -target, tmp[1] = nums[left], tmp[2] = nums[right];
                    sort(tmp.begin(), tmp.end());
                    ret[size++] = tmp;
                    left++;
                    right--;
                }
            }
        }
        ret.resize(size);
        ret.erase(unique(ret.begin(), ret.end()), ret.end());
        return ret;
    }
};
