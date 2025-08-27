class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.checkChildren(root)
        
    def checkChildren(self,root: Optional[TreeNode],level:int = 0) -> int:
        if root:
                
            if root.right and root.left:
                left =  self.checkChildren(root.left,level)
                right =  self.checkChildren(root.right,level)
                
                return min(left,right)+1
                
            elif root.right:

                return self.checkChildren(root.right,level+1)
            
            elif root.left:

                return self.checkChildren(root.left,level+1)

            else:
                return level+1
            
        else:
            return level
            
