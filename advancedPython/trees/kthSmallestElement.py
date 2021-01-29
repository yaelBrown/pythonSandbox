'''
    For your reference:
    
    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''

def kth_smallest_element(root, k):
  if k == 1:
    return root.val
  else: 
    # find smallest element
    if root.left_ptr != None: 
      return kthHelper(root.left_ptr, k, cnt)



def kthHelper(root, k, cnt):
  if root.left_ptr != None: 
    return kthHelper(root.left_ptr, k, cnt)

  if root.left_ptr == None:
    return root.val

    # ??