## DESIGN & RUNTIME COMPLEXITY ANALYSIS

Breadth first search is used to count the number of connected components.

Following is the design for the solution - 
1. Create an array of all vertices 
2. For each of vertex, 
    a. perform BFS.
    b. If BFS is complete, increment the count of connected component


## RUNTIME

'''
    graph = Graph()                                                         -> O(1)
    for item in edges:                                                      -> O(N)
        graph.buildEdges(item)                                              -> O(1)

    arrayOfVertices = [x for x in range(n)]                                 -> O(N)
    explored: Dict[int:bool] = {}                                           -> O(1)
    numberOfComponent: int = 0                                              -> O(1)

    for vertex in arrayOfVertices:                                          -> O(N)
        if not explored.get(vertex,False):                                  -> O(1)
            numberOfComponent += 1                                          -> O(1)
            q = Queue()                                                     -> O(1)
            q.put(vertex)                                                   -> O(1)
            while not q.empty():                                            -> O(E)
                explore = q.get()
                print ("Explore: ", explore,graph.getEdges(explore))
                for edge in graph.getEdges(explore):                        -> O(E)
                    if not explored.get(edge,False):
                        explored[edge] = True
                        q.put(edge)

    return numberOfComponent
'''

The runtime is ~ 3\*O(N) + 2\*O(E), which can be considered as O(N+E). However, runtime can be improved.
Instead of creating graph for all vertices, the graph could be created only for edges defined. Rest of the
vertices would count as disconnected/isloated component.