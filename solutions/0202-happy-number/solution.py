class Solution:
    def isHappy(self, n: int) -> bool:
        squares = dict(list(zip(list(map(str, range(10))), list(map(lambda x: x**2, range(10))))))
        print(squares)

        one_reached = False
        ns = []
        cur = n
        while (cur not in ns) and one_reached!=True:
            ns.append(cur)
            res = 0
            for i in str(cur):
                res+= squares[i]
            if res == 1:
                return True
            
            cur = res
        
        return False
