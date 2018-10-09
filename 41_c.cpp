class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        vector <int> bullet;
        int n = nums.size(), Max = -1;
        if (n == 0)
            return 1;
        for (int i = 0; i < n; i++) {
            if (Max < nums[i])
                Max = nums[i];
        }
        bullet.resize(Max + 5);
        for (int i = 0; i < n; i++) {
            if (nums[i] >= 0)
                bullet[nums[i]]++;
        }
        for (int i = 1; i < Max + 5; i++) {
            if (bullet[i] == 0)
                return i;
        }
    }
};
