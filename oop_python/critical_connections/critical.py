'''
Given a network of servers where each server is connected to every other server directly or indirectly through the bidirectional connections in the network, find all the critical connections.

A connection in a connected network is said to be critical if removing it disconnects the network.
'''

from typing import List, Dict, Any, Set

class Vertex:
    def __init__(self,value:int):
        self.value: int = value
        self.neigbour: int = 0
        self.neighbours: List['Vertex'] = []
    
    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.value == other.value
        return False

    def __hash__(self):
        return self.value

class Graph:
    def __init__(self,n:int):
        self.graph: Dict[int,List[Vertex]] = {}
        self.vertexSet: Set['Vertex'] = set()
        # for i in range(n):
        #     self.graph[i] = []

    def __getVertex(self,value:int):
        for item in self.vertexSet:
            if item.value == value:
                return item
        return None
    
    def buildEdges(self,edge:List[int]):
        vertex1: Vertex = self.__getVertex(edge[0]) if self.__getVertex(edge[0]) else Vertex(edge[0])
        vertex2: Vertex = self.__getVertex(edge[1]) if self.__getVertex(edge[1]) else Vertex(edge[1])

        if not self.graph.get(vertex1,False):
            self.graph[vertex1] = [vertex2]
        else:
            self.graph[vertex1].append(vertex2)

        if not self.graph.get(vertex2,False):
            self.graph[vertex2] = [vertex1]
        else:
            self.graph[vertex2].append(vertex1)

        vertex1.neigbour += 1
        vertex1.neighbours.append(vertex2)
        
        vertex2.neigbour += 1
        vertex2.neighbours.append(vertex1)

        self.vertexSet.add(vertex1)
        self.vertexSet.add(vertex2)
        
    def getEdges(self,vertex:int)->List[int]:
        return self.graph.get(vertex)
    
    def getVertices(self) -> Set[Vertex]:
        return self.vertexSet
    
def find_critical_connections(number_of_servers, connections):
    """
    Args:
     number_of_servers(int32)
     connections(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    graph:Graph = Graph(number_of_servers)
    for connection in connections:
        graph.buildEdges(connection)

    paths: Dict[int,int] =  {}
    for vertex in graph.getVertices():
        if vertex.neigbour == 1:
            if paths.get(vertex.value,False) or paths.get(vertex.neighbours[0].value,False):
                pass
            else:
                paths[vertex.value] = vertex.neighbours[0].value
    
    
    return list(paths.items()) if paths else [[-1,-1]]

if __name__ == '__main__':
    print (find_critical_connections(5,[[1, 0],[0, 2],[2, 1],[0, 3],[3, 4]]))
