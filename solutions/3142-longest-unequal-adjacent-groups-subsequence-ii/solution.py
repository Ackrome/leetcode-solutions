class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:        
        n = len(words)
        graph = [[] for _ in range(n)]
        
        # Построение списка смежности
        for i in range(n):
            for j in range(i + 1, n):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if sum(c1 != c2 for c1, c2 in zip(words[i], words[j])) == 1:
                        graph[i].append(j)

        # DP для поиска максимальной длины
        dp = [1] * n
        prev = [-1] * n
        for i in range(n):
            for j in graph[i]:
                if dp[j] < dp[i] + 1:
                    dp[j] = dp[i] + 1
                    prev[j] = i
                    
        # Восстановление пути
        max_len = max(dp)
        path = []
        curr = dp.index(max_len)
        while curr != -1:
            path.append(curr)
            curr = prev[curr]
        
        return [words[i] for i in reversed(path)]
