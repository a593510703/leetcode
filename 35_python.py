class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l = mid = 0
        r = n - 1
        while r - l >= 0:
            mid = (l + r) >> 1
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l