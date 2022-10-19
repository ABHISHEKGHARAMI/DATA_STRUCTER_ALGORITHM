##find mother from a graph using the dfs
from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def Dfsutill(self,v,visited):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.Dfsutill(i,visited)

    def find_mother(self):
        visited=[False]*self.V
        v=0
        for i in range(self.V):
            if visited[i]==False:
                self.Dfsutill(i,visited)
                v=i
        visited=[False]*self.V
        self.Dfsutill(v,visited)
        if any(i==False for i in visited):
            return -1
        else:
            return v
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print ("A mother vertex is " + str(g.find_mother()))
        
