class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums):
            return []
        elif len(nums)==1:
            return [str(nums[0])]
        elif len(nums)==2 and nums[1]-nums[0]>1:
            return [str(nums[0]),str(nums[1])]

        cur = 0
        n = len(nums)
        res = []
        for i in range(1,n):
            if nums[i]-nums[i-1]==1:
                continue
            elif nums[i]-nums[i-1]>1:
                if cur==i-1:
                    res.append(f"{nums[cur]}")
                    cur = i
                else:
                    res.append(f"{nums[cur]}->{nums[i-1]}")
                    if i == (n-1):
                        res.append(f"{nums[i]}")

                    cur = i

        if f"{nums[cur]}->{nums[i]}" not in res and i!=cur:
            res.append(f"{nums[cur]}->{nums[i]}")
        elif str(nums[i]) not in res[-1]:
            res.append(str(nums[i]))
        return res
