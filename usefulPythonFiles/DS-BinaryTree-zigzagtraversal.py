class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  temp = []
  q = [root]
  rev = False
  
  while q or temp: 
    n = q.pop(0)
    temp.append(n)
    if not q:
      if rev:
        result.append(q.reverse)
      else: 
        result.append(q)
      
      temp = []

    if n.left:
      q.append(n.left)
    if n.right:
      q.append(n.right)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()








#LC 103



"""
Need to use 2 stacks, 

fill the second stack with the children of the first 
  reverse the way you add them on the second time
"""


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        s1 = [root]
        s2 = []
        level = []
        result = []
        while s1 or s2:
            while s1:
                root = s1.pop()
                level.append(root.val)
                if root.left:
                    s2.append(root.left)
                if root.right:
                    s2.append(root.right)
            result.append(level)
            level = []
            while s2:
                root = s2.pop()
                level.append(root.val)
                if root.right:
                    s1.append(root.right)
                if root.left:
                    s1.append(root.left)
            if level != []:
                result.append(level)
                level = []
        return 