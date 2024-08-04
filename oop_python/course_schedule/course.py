from typing import List, Dict

class DirectedGraph:
    def __init__(self,n):
        self.graph: Dict[int,List[int]] = {}
        self.v = n

    def buildEdges(self,edge:List[int]):
        if not self.graph.get(edge[0],False):
            self.graph[edge[0]] = [edge[1]]
        else:
            self.graph[edge[0]].append(edge[1])
    
    def getEdges(self,vertex:int)->List[int]:
        return self.graph.get(vertex,[])
    
    def isCyclicRecursion(self,node:int, visited:List[bool], recursion:List[bool]) -> bool:
        visited[node] = True
        recursion[node] = True

        for neighbour in self.getEdges(node):
            if not visited[neighbour]:
                if self.isCyclicRecursion(neighbour,visited,recursion):
                    return True
            elif recursion[neighbour]:
                return True
        recursion[node] = False
        return False

    def isCyclic(self) -> bool:
        visited = [False]*self.v
        recursion = [False]*self.v
        for vertex in range(self.v):
            if not visited[vertex]:
                if self.isCyclicRecursion(vertex,visited,recursion):
                    return True
        return False

def canFinish( numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph: DirectedGraph = DirectedGraph(numCourses)
    for edge in prerequisites:
        graph.buildEdges(edge=edge)
    return not graph.isCyclic()

if __name__ == '__main__':
    output: bool = canFinish(2,[[0,1]])
    assert output, "Incorrect implementation"

    output: bool = canFinish(2,[[0,1],[1,0]])
    assert not output, "Incorrect implementation"