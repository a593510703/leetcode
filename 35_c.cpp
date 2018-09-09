class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();
        int l = 0, r = n - 1, mid;
        while (r - l >= 0) {
            mid = (l + r) >> 1;
            if (nums[mid] >= target)
                r = mid - 1;
            else
                l = mid + 1;
        }
        //printf("%d", mid);
        return l;
    }
};
