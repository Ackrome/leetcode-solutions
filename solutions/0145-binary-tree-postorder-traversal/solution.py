class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse = []
        self.postorder(root)
        return self.traverse
    
    def postorder(self, root:Optional[TreeNode]):
        if root:
            if root.left:
                self.postorder(root.left)
            
            if root.right:
                self.postorder(root.right)
                
            self.traverse.append(root.val)
