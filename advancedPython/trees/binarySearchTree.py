class Node: 
  def __init__(self, value = None):
    self.value = value
    self.leftChild = None
    self.rightChild = None

class BinarySearchTree: 
  def __init__(self, value = None):
    self.root = Node(value)

  def insert(self, value):
    if self.root.value == value:
      self._already_in_list(value)
    
    if self.root.value == None:
      self.root = Node(value)
    else:
      if value < self.root.value: 
        if self.root.leftChild == None: 
          self.root.leftChild = Node(value)
        else: 
          return self._insert(value, self.root.leftChild)

      if value > self.root.value: 
        if self.root.rightChild == None: 
          self.root.rightChild = Node(value)
        else: 
          return self._insert(value, self.root.rightChild)
      
  def _insert(self, value, root):
    if root.value == value:
      self._already_in_list(value)

    if value < root.value: 
      if root.leftChild == None: 
        root.leftChild = Node(value)
      else: 
        return self._insert(value, root.leftChild)
    
    if value > root.value: 
      if root.rightChild == None:
        root.rightChild = Node(value)
      else: 
        return self._insert(value, root.rightChild)
    

  def print_tree(self):
    if self.root == None: 
      return print("There is no root/nodes!")
    else: 
      print(f"{self.root.value}")

    if self.root.leftChild != None: 
      return self._print_tree(self.root.leftChild)
    else: 
      print("No left child")

    if self.root.rightChild != None:
      return self._print_tree(self.root.rightChild)
    else: 
      return print("No right child")

  def _print_tree(self, root):
    print(f"{root.value}")

    if root.leftChild == None: 
      return print("No left child")
    else: 
      return self._print_tree(root.leftChild)

    if root.rightChild == None: 
      return print("No right child")
    else: 
      return self._print_tree(root.rightChild)

  
  def _already_in_list(self, value):
    return print(f"{value} is already in BST!")







if __name__ == "__main__":
  import random

  bst = BinarySearchTree()

  vals = [random.randint(0, 100) for _ in range(50)]


  print(vals)


  valsMid = vals[int(len(vals) / 2)]
  print(f"\nInserting vals mid: {valsMid}\n")
  bst.insert(valsMid)


  for i in vals:
    print(f"inserting {i}")
    bst.insert(i)

  print("\nprint bst")
  bst.print_tree()
