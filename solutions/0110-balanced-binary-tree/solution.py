class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkLevel(root)!=-1
    def checkLevel(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.checkLevel(root.left)
        if left == -1:
            return -1
        
        right = self.checkLevel(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        
        return max(left,right) +1


