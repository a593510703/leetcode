class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ret = []
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                if nums[left] + nums[right] > target:
                    right = right - 1
                elif nums[left] + nums[right] < target:
                    left = left + 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    while left < right and nums[right] == nums[right + 1]:
                        right = right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
        return ret