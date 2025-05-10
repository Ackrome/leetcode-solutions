class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        M = num//1000
        res += 'M'*M
        
        res += self.RomanNumerals(num//100%10, 'C','D','M')
        res += self.RomanNumerals(num//10%10, 'X','L','C')
        res += self.RomanNumerals(num%10, 'I','V','X')

        return res
    
    def RomanNumerals(self, number, main, halfmore, more):
        if number < 4:
            return main*number
        elif number == 4:
            return main + halfmore
        elif  9 > number >= 5:
            return halfmore + main*(number-5)
        else:
            return main + more
