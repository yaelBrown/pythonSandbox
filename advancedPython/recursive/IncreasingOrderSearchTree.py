# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def _dfs(r, sl):
          sl = [r.val]
          
          if r.left != None:
            sl = sl + _dfs(r.left, sl)
            
          if r.right != None:
            sl = sl + _dfs(r.right, sl)
            
          return sl
        
        _ = _dfs(root, [])
        _.sort()
        
        def _insertRight(v, r):          
          if r.right == None: 
            r.right = TreeNode(v)
            return
          else:
            _insertRight(v, r.right)
        
        out = TreeNode(_[0])
        
        for i in _:
          if i == _[0]:
            continue
          _insertRight(i, out)
        
        return out