'''
https://leetcode.com/problems/course-schedule-ii/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

from typing import List,Dict

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
    

    def DFSTopologicalSort(self, vertex: int, visited: List[int],topoSort: List[int]):
        visited[vertex] = True
        for neighbour in self.getEdges(vertex):
            if not visited[neighbour]:
                self.DFSTopologicalSort(neighbour,visited,topoSort)
                topoSort[self.currLabel] = vertex
                self.currLabel -= 1
  

    def getTopologicalSort(self) -> List[int]:
        visited = [False]*self.v
        topoSort = [None]*self.v
        self.currLabel = self.v - 1
        for vertex in range(self.v):
            if not visited[vertex]:
                self.DFSTopologicalSort(vertex, visited,topoSort)
        topoSort[self.currLabel] = vertex
        return topoSort

def findOrder( numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph: DirectedGraph = DirectedGraph(numCourses)
    for edge in prerequisites:
        graph.buildEdges(edge=edge)
    return graph.getTopologicalSort()

if __name__ == '__main__':
    print(findOrder(2,[[1,0]]))
    print(findOrder(2,[[0,1]]))