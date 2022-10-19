#dijkstra algorithm for finding the shortest path
import sys
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=[[0 for i in range(self.V)] for j in range(self.V)]

    #print sol
    def print_sol(self,dist):
        print("printing solution :")
        print("Node \tWeight")
        for i in range(self.V):
            print(i,"\t",dist[i])

    #finding minkey
    def minKey(self,dist,sptset):
        min=sys.maxsize
        for i in range(self.V):
            if dist[i]<min and sptset[i]==False:
                min=dist[i]
                min_index=i
        return min_index

    #dijkstra algorithm
    def dijkstra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src]=0
        sptset=[False]*self.V
        for cout in range(self.V):
            x=self.minKey(dist,sptset)
            sptset[x]=True
            for y in range(self.V):
                if self.graph[x][y]>0 and sptset[y]==False and dist[y]>dist[x]+self.graph[x][y]:
                    dist[y]=dist[x]+self.graph[x][y]
        self.print_sol(dist)
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
 
g.dijkstra(0)












            
            
