class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = 0
        squared = 0
        while squared < num:
            root+=1
            squared = root*root

        return squared==num
