# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse = []
        self.preorder(root)
        return self.traverse
    
    def preorder(self, root:Optional[TreeNode]):
        if root:
            self.traverse.append(root.val)
            
            if root.left:
                self.preorder(root.left)
            
            if root.right:
                self.preorder(root.right)
