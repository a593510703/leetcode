class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(0, n):
            x = target - nums[i]
            for j in range(i + 1, n):
                if nums[j] == x:
                    return [i, j]