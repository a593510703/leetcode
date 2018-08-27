static auto static_lambda = [] () {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    return 0;
}();
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size(), i = 0, j = 0, k = 0;
        vector <int> nums3;
        while (i < n1 && j < n2) {
            if (nums1[i] > nums2[j])
                nums3.push_back(nums2[j++]);
            else
                nums3.push_back(nums1[i++]);
        }
        int N = n1 + n2;
        while (i < n1)
            nums3.push_back(nums1[i++]);
        while (j < n2)
            nums3.push_back(nums2[j++]);
        if (N % 2 == 0)
            return 0.5 * (nums3[N / 2] + nums3[N / 2 - 1]);
        else
            return 1.0 * nums3[N / 2];
    }
};
