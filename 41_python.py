class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        Max = max(nums) + 10
        bullet = [0 for x in range(Max)]
        for x in nums:
            if x > 0:
                bullet[x] += 1
        for x in range(1, Max):
            if bullet[x] == 0:
                return x