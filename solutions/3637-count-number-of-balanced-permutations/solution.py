class Solution(object):
    def countBalancedPermutations(self, num):
        modulo = 10**9+7
        len_s = len(num)
        
        total = sum(int(c) for c in num)
        if total % 2:
            return 0
        
        fact = [1]*(len_s+1)
        inv = [1]*(len_s+1)
        invFact = [1]*(len_s+1)
        
        for i in range(1,len_s+1):
            fact[i] = fact[i-1]*i % modulo
            
        for i in range(2,len_s+1):
            inv[i] = modulo - (modulo//i)*inv[modulo%i] % modulo
            
        for i in range(1,len_s+1):
            invFact[i] = invFact[i-1]*inv[i] % modulo
        
        halfSum = total//2
        halfLen = len_s//2
        dp = [[0]*(halfLen+1) for _ in range(halfSum+1)]
        dp[0][0] = 1
        digits = [0]*10
        
        for c in num:
            d = int(c)
            digits[d] += 1
            for i in range(halfSum, d-1, -1):
                for j in range(halfLen, 0, -1):
                    dp[i][j] = (dp[i][j] + dp[i-d][j-1]) % modulo
                    
        res = dp[halfSum][halfLen]
        res = res * fact[halfLen] % modulo * fact[len_s-halfLen] % modulo
        for cnt in digits: res = res * invFact[cnt] % modulo
        
        return res
