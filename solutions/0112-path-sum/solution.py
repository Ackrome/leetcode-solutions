class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sums = []
        if root:
            self.findSums(root)
            
        return targetSum in self.sums
        
    
    def findSums(self,root: Optional[TreeNode], sumBefore: int = 0):
        
        if sumBefore == 0:
            sumNow = root.val
        else:
            sumNow = root.val + sumBefore
        
        if root.left == root.right == None:
            self.sums.append(sumNow)
        
        else:
            if root.left:
                self.findSums(root.left,sumNow)
            if root.right:
                self.findSums(root.right,sumNow)
