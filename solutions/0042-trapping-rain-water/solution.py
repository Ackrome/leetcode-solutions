class Solution:
    def trap(self, height: List[int]) -> int:
        # return sum([abs(height[i] - min(max(height[:i+1]),max(height[i:]))) for i in range(len(height))])
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        total_water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1
                
        return total_water

