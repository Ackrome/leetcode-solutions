class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore
        n = len(nums)
        count1 = 0
        count2 = 0
        candidates = [None,None]
        for i in nums:
            if i == candidates[0]:
                count1+=1
            elif i == candidates[1]:
                count2+=1
            elif count1 == 0:
                candidates[0] = i
                count1+=1
            elif count2 == 0:
                candidates[1] = i
                count2+=1
            else:
                count2-=1
                count1-=1
        
        trucands = []
        for cand in candidates:
            if cand!=None:
                if nums.count(cand)>n//3:
                    trucands.append(cand)


        return trucands
        
