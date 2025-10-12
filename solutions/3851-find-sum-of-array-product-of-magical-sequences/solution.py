MODULO = 10**9 + 7

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(m, k, i, mask):
            if m < 0 or k < 0 or m + mask.bit_count() < 0:
                return 0

            if m == 0:
                if k == mask.bit_count():
                    return 1
                else:
                    return 0
            
            if i >= len(nums):
                return 0

            result = 0
            for c in range(m + 1):
                multip = math.comb(m, c) * pow(nums[i], c , MODULO) % MODULO
                mask_new= mask+ c
                result += multip * dp(m - c, k - mask_new % 2, i + 1, mask_new // 2)

            return result%MODULO

        return dp(m, k, 0, 0)
