#union find algorithm for find the cycle in the graph
from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def find(self,parent,i):
        if parent[i]==-1:
            return i
        if parent[i]!=-1:
            return self.find(parent,parent[i])

    def union(self,parent,x,y):
        parent[x]=y


    def isCyclic(self):
        parent=[-1]*self.V
        for i in self.graph:
            for j in self.graph[i]:
                x=self.find(parent,i)
                y=self.find(parent,j)
                if x==y:
                    return True
                self.union(parent,x,y)


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
if g.isCyclic():
    print("The graph contains cycle.")
else:
    print("The graph don't contains cycle.")
