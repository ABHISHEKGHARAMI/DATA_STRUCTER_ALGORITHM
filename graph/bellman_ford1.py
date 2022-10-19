#another shortest path algorithm
#greedy algorithm
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=[]

    #add edge the vertices
    def add_edge(self,u,v,w):
        self.graph.append([u,v,w])

    #print solution
    def print_sol(self,dist):
        print("printing the solution :")
        print("Vertex \tWeight")
        for i in range(self.V):
            print(i,"\t",dist[i])

    #bellman ford algorithm
    def bellman_ford(self,src):
        #step1: fill the distance
        dist=[float('Inf')]*self.V
        dist[src]=0

        #step 2: relax the v-1 edges
        for _ in range(self.V-1):
            for u,v,w in self.graph:
                if dist[u]!=float('Inf') and dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w

        #step 3: find the negative cycle
        for u,v,w in self.graph:
            if dist[u]!=float('Inf') and dist[u]+w<dist[v]:
                print("Graph contains negative cycle..")
        self.print_sol(dist)

g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)










        
        
