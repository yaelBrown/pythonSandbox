# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right: return False
        if not root.left or not root.right: return False

        j, k = root.left, root.right
        q = []
        sym = True
        while sym:
            if j.left:
                if not k.right: 
                    return False
            
