class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                newTarget = target - nums[i] - nums[j]
                low, high = j+1, n-1
                while low<high:
                    if nums[low]+nums[high]<newTarget:
                        low+=1
                    elif nums[low]+nums[high]>newTarget:
                        high-=1
                    else:
                        output.append([nums[i], nums[j], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
        return output
