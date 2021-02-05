from Graph import Graph

class Dfs(Graph):
  def __init__(self, edgeLists, isDirected=False):
    super().__init__(edgeLists, isDirected)
    s = List()

  def dfs(self, root, target=None):
    self.s.clear()
    visited = List()

    for c in root.neighbors:
      self.s.append(c)
    
    while self.s:
      cur = self.s.pop(len(self.s.pop) - 1)
      visited.append(cur)

      if cur.neighbors:
        for n in cur.neighbors:
          self.s.append(n)
          # ?

  
  if __name__ == "__main__":
    print("dfs is working")