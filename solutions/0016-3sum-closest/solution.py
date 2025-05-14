class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        closest = float('inf')
        mind = float('inf')

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                cur_diff = abs(target - current_sum)
                
                if cur_diff < mind: 
                    mind = cur_diff
                    closest = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest
