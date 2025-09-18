class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = list(set(range(1,n+1)).difference(set(nums)))
        print(res)
        return res

        
