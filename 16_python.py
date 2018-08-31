class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            if nums[i] + nums[left] + nums[left + 1] > target:
                ans.append(nums[i] + nums[left] + nums[left + 1])
            elif nums[i] + nums[right] + nums[right - 1] < target:
                ans.append(nums[i] + nums[right] + nums[right - 1])
            else:
                while left < right:
                    x = nums[i] + nums[right] + nums[left]
                    ans.append(x)
                    if x < target:
                        left += 1
                    elif x > target:
                        right -= 1
                    else:
                        return target
        ans.sort(key=lambda x:abs(x - target))
        return ans[0]