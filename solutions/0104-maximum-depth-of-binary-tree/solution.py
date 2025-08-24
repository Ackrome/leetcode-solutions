# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.level = 0
        if root:
            self.level = 1
        else:
            return 0
        
        if any([root.right, root.left]):
            self.tryLevelOrder(root, 1)
        
        return self.level

        
    def tryLevelOrder(self, root: Optional[TreeNode], level):
        self.level = max(self.level, level)
        
        if root.left:
            self.tryLevelOrder(root.left,level+1)
        
        if root.right:
            self.tryLevelOrder(root.right,level+1)
