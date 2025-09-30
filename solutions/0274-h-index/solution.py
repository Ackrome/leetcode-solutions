class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse = True)
        return max([i+1 for i in range(len(citations)) if citations[i] >= i+1], default=0)
            
