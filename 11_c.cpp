class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size(), left = 0, right = n - 1, water = 0;
        while (left < right) {
            if (water < min(height[left], height[right]) * (right - left))
                water = min(height[left], height[right]) * (right - left);
            if (height[left] < height[right])
                left++;
            else
                right--;
        }
        return water;
    }
};
