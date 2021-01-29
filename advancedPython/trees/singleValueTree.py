class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr

# complete the function below

def findSingleValueTrees(root):
  ptr = root.val
  cnt = 0

  lVal = None
  rVal = None
  
  if root.left_ptr != None: 
    cnt += _singleValTrees(root.left_ptr, cnt)
    lVal = root.left_ptr.val

  if root.right_ptr != None: 
    cnt += _singleValTrees(root.right_ptr, cnt)
    rVal = root.right_ptr.val

  _ = [ptr, lVal, rVal]
  temp = []
  c2 = 0
  
  for i in _:
    if i != None: 
      temp.append(i)
  c2 += 1

  if len(set(temp)) == 1:
    cnt += 1

  return cnt

def _singleValTrees(root, count):
  if root.left_ptr == None and root.right_ptr == None: 
    return count
  else:
    _ = [] 
    curCnt = 0
    if root.left_ptr.val != None:
      _.append(root.left_ptr.val)
      curCnt += _singleValTrees(root.left_ptr, curCnt)

    if root.right_ptr.val != None:
      _.append(root.right_ptr.val)
      curCnt += _singleValTrees(root.right_ptr, curCnt)

    if len(set(_)) == 1:
      curCnt += 1

    return curCnt