def find_level_averages(root):
  q = [root]
  temp = []
  out = []

  def find_avg(l):
    return float(sum(l)/len(l))

  while q: 
    n = q.pop(0)
    temp.append(n.val)
    if len(q) == 0:
      out.append(find_avg(temp))
      temp = []
    
    if n.left: 
      q.append(n.left)
    if n.right:
      q.append(n.right)

  return out







def find_level_averages(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  while queue:
    levelSize = len(queue)
    levelSum = 0.0
    for _ in range(levelSize):
      currentNode = queue.popleft()
      # add the node's value to the running sum
      levelSum += currentNode.val
      # insert the children of current node to the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    # append the current level's average to the result array
    result.append(levelSum / levelSize)

  return result