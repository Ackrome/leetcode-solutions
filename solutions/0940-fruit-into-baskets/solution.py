class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        nums=[[1,fruits[0]]]
        cur = 1
        for i in range(1,len(fruits)):
            if fruits[i-1]==fruits[i]:
                cur+=1
                if i == len(fruits)-1:
                    nums[-1] = [cur,fruits[i]]
                    
            elif fruits[i-1]!=fruits[i]:
                nums[-1] = [cur,fruits[i-1]]
                nums.append([1,fruits[i]])
                cur = 1
        
        numlen = len(nums)
        if numlen <= 2 or len(set([nums[i][1] for i in range(numlen)]))<=2:
            return sum([nums[i][0] for i in range(numlen)])
        
        else:

            cur_pair = set()
            cur_q, max_q = 0,0
            for i, [q,type] in enumerate(nums):
                if type in cur_pair:
                    cur_q += q
                else:
                    if i!=0:
                        cur_q = nums[i-1][0] + q
                        cur_pair = {nums[i-1][1],type}
                    else:
                        cur_q = q
                        cur_pair = {type}
                    
                max_q = max(max_q,cur_q)
                
        return max_q
