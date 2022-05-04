from __future__ import print_function
from cmath import inf
from collections import deque
from xmlrpc.client import MININT


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
  s1 = [root]
  s2 = []

  while s1 or s2:
    while s1: 
      n = s1.pop(0)
      if s1:
        n.next = s1[0]
      else:
        n.next = None

      if n.left: 
        s2.append(n.left)
      if n.right:
        s2.append(n.right)

    while s2:
      n = s2.pop(0)
      if s2:
        n.next = s2[0]
      else: 
        n.next = None

      if n.left:
        s1.append(n.left)
      if n.right:
        s1.append(n.right)

  return

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()


