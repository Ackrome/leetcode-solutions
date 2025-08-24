# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level = 1
        self.result = [[root.val]]
        
        if root.left:
            self.tryLevelOrder(root.left,level+1)
        
        if root.right:
            self.tryLevelOrder(root.right,level+1)
        
        while [] in self.result:
            self.result.remove([])
            
        return self.result
        
        
    
    def tryLevelOrder(self, root: Optional[TreeNode], level):
        if len(self.result)<level:
            self.result.append([root.val])
        else:
            self.result[level-1].append(root.val)
        
        if root.left:
            self.tryLevelOrder(root.left,level+1)
        
        if root.right:
            self.tryLevelOrder(root.right,level+1)  
        
