class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        water = 0
        while left < right:
            if water < min(height[left], height[right]) * (right - left):
                water = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return water