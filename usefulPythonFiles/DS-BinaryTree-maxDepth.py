# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        stack = [[root, 1]]
        d = 0
        out = 0
        while stack:
            n, d = stack.pop(0)
            
            if n:
                out = max(out, d)
                if n.left:
                    stack.append([n.left, d + 1])
                if n.right:
                    stack.append([n.right, d+1])
                    
        return out
            
            
            