# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        mid = left + (right - left) // 2
        while guess(mid)!=0:
            if guess(mid) == -1:
                right = mid
            else:
                left = mid + 1
            mid = left + (right - left) // 2
        return mid
