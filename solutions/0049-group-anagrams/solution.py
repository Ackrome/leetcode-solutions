from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resd = defaultdict(list)
        for i in strs:
            resd[''.join(sorted(list(i)))].append(i)
        return list(resd.values())
