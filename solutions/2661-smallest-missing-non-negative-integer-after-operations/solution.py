class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        counts = [0]*value
        for i in range(n):
            counts[(nums[i] % value + value) % value] += 1
        
        k = 0
        while True:
            rem = k % value
            if counts[rem]==0:
                return k
            else:
                counts[rem] -= 1
                k+=1
