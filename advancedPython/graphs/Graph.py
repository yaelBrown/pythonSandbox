class Vertex:
  def __init__(self, n):
    self.name = n
    self.neighbors = []

  def printNeighbors(self):
    print(self.neighbors)


class Graph: 
  def __init__(self, edgelists, isDirected=False):
    self.verticies = {}
    self.isDirectedGraph = isDirected

    for start, end in edgelists:
      if start not in self.verticies:
        self.verticies[start] = Vertex(start)
      if end not in self.verticies:
        self.verticies[end] = Vertex(end)

      if end not in self.verticies[start].neighbors:
        self.verticies[start].neighbors.append(end)

      if not self.isDirected:
        if start not in self.verticies[end].neighbors:
          self.verticies[end].neighbors.append(start)
  
  def add_vertex(self, n):
    if n not in self.verticies:
      self.verticies[n] = Vertex(n)

  def add_edge(self, u, v):
    if u not in self.verticies:
      self.verticies[u] = Vertex(u)

    if v not in self.verticies:
      self.verticies[v] = Vertex(v)

    if v not in self.verticies[u].neighbors:
      self.verticies[u].neighbors.append(v)

      if not self.isDirected:
        if u not in self.verticies[v].neighbors:
          self.verticies[v].neighbors.append(u)

  def del_vertex(self, v):
    if v in self.verticies:
      del self.verticies[v]

  def del_edge(self, u, v):
    if u in self.verticies:
      if v in self.verticies[u].neighbors:
        self.verticies[u].neighbors.remove(v)

        if not self.isDirectedGraph:
          if u in self.verticies[v].neighbors:
            self.verticies[v].neighbors.remove(u)

  def printGraph(self):
    for k in self.verticies.items():
      print(k[0])
      print("neighbors: ")
      print(k[1].printNeighbors())
      print("\n")


if __name__ == '__main__':
  el = [
    ("a","b"),
    ("a","c"),
    ("a","d"),
    ("c","d"),
    ("d","e"),
    ("d","f"),
    ("f","a"),
  ]
  
  ud = Graph(el, True)

  ud.printGraph()
