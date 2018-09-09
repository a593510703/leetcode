class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        int l = 0, r = n - 1, mid;
        vector <int> ret;
        while (r - l >= 0) {
            mid = (l + r) >> 1;
            if (nums[mid] >= target)
                r = mid - 1;
            else
                l = mid + 1;
        }
        if (l < n && nums[l] == target)
            ret.push_back(l);
        l = 0, r = n - 1;
        while (r - l >= 0) {
            mid = (l + r) >> 1;
            if (nums[mid] <= target)
                l = mid + 1;
            else
                r = mid - 1;
        }
        if (r >= 0 && nums[r] == target)
            ret.push_back(r);
        if (ret.size() == 2)
            return ret;
        else {
            vector <int> ans;
            ans.push_back(-1);
            ans.push_back(-1);
            return ans;
        }
    }
};
