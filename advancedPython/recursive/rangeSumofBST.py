# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root == None:
          return 0
          
        def _dfs(r, l, h):
          sum = 0
        
          if r.val >= l and r.val <= h:
            sum += r.val
          
          if r.left != None:
            sum += _dfs(r.left, l, h)
            
          if r.right != None: 
            sum += _dfs(r.right, l, h)
            
          return sum
  
        return _dfs(root, low, high)
        
        
        
        