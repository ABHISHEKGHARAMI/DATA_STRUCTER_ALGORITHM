#intro to graph
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    #create the node of the graph

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[None]*self.V
    #creating the graph with adjacent list

    def add_edge(self,u,v):
        node1=node(v)
        node1.next=self.graph[u]
        self.graph[u]=node1

        #bidirectional graph

        node1=node(u)
        node1=self.graph[v]
        self.graph[v]=node1


    #printing the graph
    def print_graph(self):
        print("printing the graph")
        for i in range(self.V):
            print("node :",i)
            temp=self.graph[i]
            while temp:
                print("-> {}".format(temp.data),end=" ")
                temp=temp.next
            print("\n")
#n=int(input("Enter the number of vertices to be insert:"))
g1=Graph(5)
g1.add_edge(0,1)
g1.add_edge(1,2)
g1.add_edge(2,3)
g1.add_edge(3,4)
g1.add_edge(4,0)
g1.print_graph()

                
