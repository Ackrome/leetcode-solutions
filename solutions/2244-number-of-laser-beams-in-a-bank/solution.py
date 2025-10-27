class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if not bank:
            return 0

        res = []
        for i in range(len(bank)):
            cur = sum(list(map(lambda x : int(x), list(bank[i]))))
            if cur!=0:
                res.append(cur)
        
        if len(res)<=1:
            return 0
        answer = 0
        for x1,x2 in pairwise(res):
            answer+= len(list(product(range(x1), range(x2))))

        return answer
