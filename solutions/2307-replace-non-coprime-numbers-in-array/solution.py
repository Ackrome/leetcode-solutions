class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        n = len(nums)
        countr = 0
        res = []
        for item in nums:
            res.append(item)
            while len(res)>1:
                a,b = res[-2],res[-1]
                gcd_now = self.gcd(a,b)
                if gcd_now==1:
                    break
                else:
                    res.pop()
                    res[-1]=(a*b)//gcd_now

        return res

    
    def gcd(self,a,b):
        while b:
            a, b = b, a%b
        return a
