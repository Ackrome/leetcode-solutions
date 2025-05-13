class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        threesome = list()
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    threesome.append([nums[i], nums[left], nums[right]])
                    # Пропуск дубликатов для left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Пропуск дубликатов для right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return threesome
