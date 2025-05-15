class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        ans = []
        prev = None
        for i in range(n):
            
            if prev != groups[i]:            
                ans.append(words[i])
                prev = groups[i]
        return ans

            
        
        return ans
