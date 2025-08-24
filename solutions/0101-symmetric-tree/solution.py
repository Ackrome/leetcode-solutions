# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root.right
        return self.areSymmetric(p,q)
    
    def areSymmetric(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:  # Оба узла None
            return True
        if not p or not q:   # Один узел None, другой - нет
            return False
        if p.val != q.val:   # Значения не совпадают
            return False
        # Проверяем поддеревья
        return self.areSymmetric(p.left, q.right) and self.areSymmetric(p.right, q.left)
        
