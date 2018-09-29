class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[i]: i为末尾的最大和
        dp[i + 1] =   a[i + 1] (dp[i] + a[i + 1] < 0)
                      dp[i] + a[i + 1] (dp[i] + a[i + 1] >= 0)
        """
        n = len(nums)
        dp = [0] * n
        ans = 0
        Max = -2147483647
        if nums[0] > 0:
            dp[0] = nums[0]
        for i in range(n - 1):
            if dp[i] + nums[i + 1] < 0 and nums[i + 1] > 0:
                dp[i + 1] = nums[i + 1]
            elif dp[i] + nums[i + 1] < 0:
                dp[i + 1] = 0
            else:
                dp[i + 1] = dp[i] + nums[i + 1]
        for i in range(n):
            if dp[i] > ans:
                ans = dp[i]
            if nums[i] > Max:
                Max = nums[i]
        if Max < 0:
            return Max
        else:
            return ans