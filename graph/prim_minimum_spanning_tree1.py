#prims algorithm for minimum spanning tree
import sys
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for i in range(self.V)] for j in range(self.V)]

    def printMst(self,parent):
        print('Edges Weight')
        for i in range(1,self.V):
            print(parent[i],'-',i,'\t',self.graph[i][parent[i]])

    #find the minimum edge
    def minKey(self,key,mstset):
        min=sys.maxsize
        for v in range(self.V):
            if key[v]<min and mstset[v]==False:
                min=key[v]
                min_index=v
        return min_index

    #construct the prim's mst
    def primMst(self):
        key=[sys.maxsize]*self.V
        parent=[None]*self.V
        key[0]=0
        mstset=[False]*self.V
        parent[0]=-1
        for cout in range(self.V):
            u=self.minKey(key,mstset)
            mstset[u]=True
            for v in range(self.V):
                if self.graph[u][v]>0 and mstset[v]==False and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u
        self.printMst(parent)


g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
 
g.primMst();
                
