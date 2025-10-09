class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        answer = ''
        negative = num < 0
        num = abs(num)
        while num > 0:
            answer += str(num % 7)
            num //= 7
        return '-' + answer[::-1] if negative else answer[::-1]
