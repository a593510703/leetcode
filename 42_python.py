class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        Min = 0
        ans = 0
        while l < r:
            if height[l] < height[r]:
                Min = height[l]
                while l < r and Min >= height[l]:
                    ans += (Min - height[l])
                    l += 1
            else:
                Min = height[r]
                while l < r and Min >= height[r]:
                    ans += (Min - height[r])
                    r -= 1
        return ans