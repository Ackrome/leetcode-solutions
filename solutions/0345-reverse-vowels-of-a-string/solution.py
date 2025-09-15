class Solution:
    def reverseVowels(self, s: str) -> str:
        vows = 'aeiouAEIOU'
        n = len(s)
        j = 0
        result = []
        vow_l = [i for i in range(n) if s[i] in vows][::-1]
        for item in s:
            if item in vows:
                result.append(s[vow_l[j]])
                j+=1
            else:
                result.append(item)
        return ''.join(result)

