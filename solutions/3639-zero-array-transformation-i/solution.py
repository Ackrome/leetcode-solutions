class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        
        # Обработка запросов с использованием разностного массива
        for start, end in queries:
            diff[start] += 1
            if end + 1 < n:
                diff[end + 1] -= 1
        
        # Вычисление префиксной суммы и проверка условий
        current = 0
        for i in range(n):
            current += diff[i]
            if current < nums[i]:
                return False
        return True
