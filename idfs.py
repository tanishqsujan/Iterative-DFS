#This class represents a directed graph using adjacency list representation

class Graph:
    def __init__(self, V): # Constructor
        self.V = V  # No. of vertices
        self.adj = [[] for i in range(V)]  # Adjacency lists
        
    def addEdge(self, v, w):
        self.adj[v].append(w) #Add w to v's list
    
    #prints all not yet visited vertices reachable from s
    def DFS(self, s): #prints all vertices in DFS manner from given source
        visited = [False for i in range(self.V)] # Initially mark all vertices as not visited
    
        #Create a stack for DFS
        stack = []
    
        #push the current source node
        stack.append(s)
    
        while (len(stack)):
            #Pop a vertex from stack and print it
            s = stack[-1]
            stack.pop()
        
            #Stack may contain the same vertex twice. We need to print the popped item only if it is not visited
        
            if (not visited[s]):
                print(s, end= ' ')
                visited[s] = True
            
            #Get all adjacent vertices of the popped vertex s. If an adjacent has not been visited, then push it to the stack
            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)
                
#Driver program to test methods of graph class
g = Graph(5) #Total 5 vertices in graph
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(1, 4)

print("Following is Depth First Traversal")
g.DFS(0)    
         