from typing import List, Dict, Any

class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item: Any) -> None:
        """Add an item to the stack."""
        self.items.append(item)

    def pop(self) -> Any:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self) -> Any:
        """Return the top item from the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)

    def __repr__(self) -> str:
        """Return a string representation of the stack."""
        return f"Stack({self.items})"

class Graph:
    def __init__(self,n:int):
        self.graph: Dict[int,List[int]] = {}
        for i in range(n):
            self.graph[i] = []

    def buildEdges(self,edge:List[int]):
        self.graph[edge[0]].append(edge[1])
        self.graph[edge[1]].append(edge[0])

    def getEdges(self,vertex:int)->List[int]:
        return self.graph.get(vertex)


def validPath( n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = Graph(n)
    for item in edges:
        graph.buildEdges(item)

    stack: Stack = Stack()
    unexplored: Dict[int,bool] = {}
    stack.push(source)

    while not stack.is_empty():
        vertex = stack.pop()
        if vertex == destination:
            return True
        if unexplored.get(vertex,False) == False:
            unexplored[vertex] = True
            for item in graph.getEdges(vertex):
                stack.push(item)
    return False

if __name__ == '__main__':
    '''
    Basic test cases
    '''
    found: bool = validPath(3,[[0,1],[1,2],[2,0]], source = 0, destination = 2)

    assert found, "In Correct DFS logic"

    found: bool = validPath(6,[[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5)

    assert not found, "Path doesnt exist"

    '''
    Corner Cases
    '''

    found: bool = validPath(10,[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]],7,5)

    assert found, 'There is a valid path'
