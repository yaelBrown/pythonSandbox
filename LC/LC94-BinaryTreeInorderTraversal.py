"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None: 
            return []
        
        if root.left is None and root.right is None: 
            return [root.val]
        
        def trvsl(r, o):
            if r.left is not None:
                trvsl(r.left, o)
            
            o.append(r.val)
            
            if r.right is not None:
                trvsl(r.right, o)
            
            return

                
            
                
        out = []
        
        trvsl(root, out)
        
        return out
        
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
      if not root: return []
      stack = []
      stack.append(root)

      while len(stack) > 0:
        # finish iterative inorder traversal
        pass
    
    