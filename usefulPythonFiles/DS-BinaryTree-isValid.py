class Solution:
    def isValidBST(self, root: TreeNode) -> bool: 
        
        def validate(node, left, right):
            if not node: 
                return True
            if not (node.val < right and node.val > left):
                return False

        return  validate(root, float('-inf'), float('inf'))



"""
    import sys
    sys.maxint
    sys.minint

    is alternate for max integer.
"""