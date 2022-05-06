class Solution:
    def isValidBST(self, root: TreeNode) -> bool: 
                
        def validate(node, left, right):
            if not node: 
                return True
            if not (node.val > left and node.val < right):
                return False
            
            # remember to add node.val to the return of the recursive call
            return (validate(node.left, left, node.val) and
            validate(node.right, node.val, right))
        

        return  validate(root, float('-inf'), float('inf'))



"""
    import sys
    sys.maxint
    sys.minint

    is alternate for max integer.
"""