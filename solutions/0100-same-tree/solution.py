# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # Оба узла None
            return True
        if not p or not q:   # Один узел None, другой - нет
            return False
        if p.val != q.val:   # Значения не совпадают
            return False
        # Проверяем поддеревья
        return Solution.isSameTree(p.left, q.left) and Solution.isSameTree(p.right, q.right)
