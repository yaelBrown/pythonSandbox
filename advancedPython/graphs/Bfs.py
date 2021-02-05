from Graph import Graph

class Bfs(Graph):
  def __init__(edgeLists, isDirected=False):
    super().__init__(edgeLists, isDirected)
    q = List()

  def bfs(self, root, target=None):
    self.q.clear()
    visited = List()

    for c in root.neighbors:
      self.q.append(c)

    while self.q:
      cur = self.q.pop(0)
      
      if target:
        if cur == target:
          return cur

      for c in cur.neighbors:
        self.q.append(c)

      visited.append(cur)

    return visited



if __name__ == "__main__":
  print("this is working")