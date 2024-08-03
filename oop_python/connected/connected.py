'''
Given an undirected graph, find its total number of connected components.
'''
from typing import List, Dict, Any
from queue import Queue

class Graph:
    def __init__(self):
        self.graph: Dict[int,List[int]] = {}
        # for i in range(n):
        #     self.graph[i] = []

    def buildEdges(self,edge:List[int]):
        if not self.graph.get(edge[0],False):
            self.graph[edge[0]] = [edge[1]]
        else:
            self.graph[edge[0]].append(edge[1])

        if not self.graph.get(edge[1],False):
            self.graph[edge[1]] = [edge[0]]
        else:
            self.graph[edge[1]].append(edge[0])

        
    def getEdges(self,vertex:int)->List[int]:
        return self.graph.get(vertex,[])

def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    graph = Graph()
    for item in edges:
        graph.buildEdges(item)

    arrayOfVertices = [x for x in range(n)]
    explored: Dict[int:bool] = {}
    numberOfComponent: int = 0

    for vertex in arrayOfVertices:
        if not explored.get(vertex,False):
            numberOfComponent += 1
            q = Queue()
            q.put(vertex)
            while not q.empty():
                explore = q.get()
                print ("Explore: ", explore,graph.getEdges(explore))
                for edge in graph.getEdges(explore):
                    if not explored.get(edge,False):
                        explored[edge] = True
                        q.put(edge)

    return numberOfComponent

if __name__ == '__main__':
    numberOfConnectedComponents = number_of_connected_components(50,[[0, 0],[1, 1],[2, 2]])
    # assert numberOfConnectedComponents == 2, "Incorrect number of connected components"