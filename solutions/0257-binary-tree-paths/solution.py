# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        
        self.paths = []
        self.createPaths(root,[])
        print(self.paths)

        return list(map(lambda x: '->'.join(x), self.paths))
    
    def createPaths(self, root, path=[]):
        if root.left == None and root.right==None:
            self.paths.append(path+[str(root.val)])
        else:
            if root.left != None:
                self.createPaths(root.left, path+[str(root.val)])
            if root.right != None:
                self.createPaths(root.right, path+[str(root.val)])
               
