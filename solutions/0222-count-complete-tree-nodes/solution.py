# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.count(root)

    def count(self, root) -> int:
        if not root:
            return 0
        else:
            left = self.count(root.left) if root.left else 0
            right = self.count(root.right) if root.right else 0

            return left + right + 1
        
