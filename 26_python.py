class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        while i < len(nums):
            while i < len(nums) and j > 0 and nums[i] == nums[j - 1]:
                i += 1
            if i < len(nums):
                nums[j] = nums[i]
                i += 1
                j += 1
        return j