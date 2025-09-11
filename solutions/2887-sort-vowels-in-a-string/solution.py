class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        vowels_s = []
        for item in s:
            if item.lower() in vowels:
                vowels_s.append(item)
        
        vowels_s.sort(key = lambda x: ord(x))

        result_s = []
        j = 0
        for item in s:
            if item in vowels:
                result_s.append(vowels_s[j])
                j += 1
            else:
                result_s.append(item)

        return "".join(result_s)

