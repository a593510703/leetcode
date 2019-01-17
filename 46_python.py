class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        vis = []
        for i in range(len(nums)):
            vis.append(0)
        N = len(nums)
        ans = []
        def dfs(now, n, vis):
            if n == N:
                ans.append(now.copy())
                return
            for i in range(len(nums)):
                if vis[i] == 0:
                    now.append(nums[i])
                    vis[i] = 1
                    dfs(now, len(now), vis)
                    vis[i] = 0
                    now.remove(nums[i])
        dfs([], 0, vis)
        return ans