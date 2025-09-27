class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zerocnt = 1, 0
        for i in nums:
            if i !=0:
                prod*=i
            else:
                zerocnt +=1
        
        if zerocnt > 1:
            return [0]*len(nums)
        
        elif zerocnt != 0:
            return [0 if num!=0 else int(prod) for num in nums]

        else:
            return [int(prod/num) for num in nums]
