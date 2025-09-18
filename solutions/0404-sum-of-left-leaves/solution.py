# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.neededsum = 0
        self.findLefts(root)
        return self.neededsum

    def findLefts(self, root: Optional[TreeNode], isleft: Optional[bool] = False):
        if root:
            
            if root.left:
                self.findLefts(root.left, True)
                hasleft = 1
            else:
                hasleft = 0

            if root.right:
                self.findLefts(root.right)
                hasright = 1
            else:
                hasright = 0
            
            if hasleft+hasright==0 and isleft:
                self.neededsum+=root.val
