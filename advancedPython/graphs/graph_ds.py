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

      if not isDirected:
        if start not in self.verticies[end].neighbors:
          self.verticies[end].neighbors.append(start)


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
