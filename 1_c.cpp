class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector <int> ans;
        map <int, pair <int, int> > Map;
        for (int i = 0; i < n; i++)
            Map[nums[i]] = make_pair(1, i);
        for (int i = 0; i < n; i++) {
            if (Map[target - nums[i]].first && Map[target - nums[i]].second != i) {
                ans.push_back(i);
                ans.push_back(Map[target - nums[i]].second);
                break;
            }
        }
	    return ans;
    }
};
