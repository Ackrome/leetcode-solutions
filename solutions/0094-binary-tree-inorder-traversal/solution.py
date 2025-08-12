# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        if root.left==root.right==None:
            return [root.val]
        
        res = []
        if root.left!=None:
            res += self.inorderTraversal(root.left)       
        
        res = res + [root.val]
        if root.right!=None:
            res += self.inorderTraversal(root.right)
        
        return res
