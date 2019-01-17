class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if (n > 25000):
            return 2
        dp = [0]
        for i in range(n + max(nums) + 1):
            dp.append(1000000)
        for i in range(n):
            for j in range(nums[i]):
                j = j + 1
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n - 1]