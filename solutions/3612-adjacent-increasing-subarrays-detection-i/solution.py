class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        
        n = len(nums)
        i = 0
        temp = 1
        while (i + k + 1) < n:
            if nums[i]<nums[i+1] and nums[i+k]<nums[i+k+1]:
                temp+=1
            else:
                temp = 1
            
            if temp>=k:
                return True
            i += 1
            
            if temp == 1 and n - i < 2*k:
                break
        return False

