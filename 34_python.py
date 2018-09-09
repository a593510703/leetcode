class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        l = mid = 0
        r = n - 1
        ret = []
        while r - l >= 0:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        if l < n and nums[l] == target:
           ret.append(l)
        l = mid = 0
        r = n - 1
        while r - l >= 0:
            mid = (l + r) >> 1
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        if r >= 0 and nums[r] == target:
            ret.append(r)
        if len(ret) == 2:
            return ret
        return [-1, -1]