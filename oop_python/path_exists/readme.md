## DESIGN & RUNTIME COMPLEXITY ANALYSIS

Following is the pseudo code for the problem - 
1. Build graph from the value of `n` and list of edges
    a. When graph class is initialized, create a list adjacency form of graph with all vertices and zero edges
    b. For each edge, populate the edges for each vertex

2. Perform DFS to find, if path exists between given vertex

### First attempt
```
        graph = Graph(n)                                        \\ O(n) -> creates a empty hashmap for each n
        for item in edges:                                      \\ O(e) -> loops through for each edge
            graph.buildEdges(item)                              \\ O(1)

        stack: Stack = Stack()                                  \\ O(1)
        unexplored: Dict[int,bool] = {}                         \\ O(1)
        stack.push(source)                                      \\ O(1)

        while not stack.is_empty():                             \\ O(n) -> explores each vertex only once
            vertex = stack.pop()                                \\ O(1)
            if vertex == destination:
                return True
            if unexplored.get(vertex,False) == False:
                unexplored[vertex] = True
                for item in graph.getEdges(vertex):              \\ O(e`) -> Number of edges for a node
                    stack.push(item)
        return False
```

The runtime for the solution is O(2n+e+e\`). Even though `2n` has a constant factor `2`. We can improve building graph