from typing import List, Dict
from queue import Queue

class DirectedGraph:
    def __init__(self,n:int):
        self.graph: Dict[int,List[int]] = {}
        for i in range(1,n+1):
            for j in range(1,7):
                if i+j <= n:
                    self.buildEdges([i,i+j])
                else:
                    break

    def buildEdges(self,edge:List[int]):
        if not self.graph.get(edge[0],False):
            self.graph[edge[0]] = [edge[1]]
        else:
            self.graph[edge[0]].append(edge[1])

    def minimumSteps(self,startNode: int, endNode: int) -> int:
        q = Queue()
        q.put(startNode)
        steps: int = 0
        visited = {}
        while not q.empty():
            node:int = q.get()
            visited[node] = True
            children = self.getEdges(node)
            steps += 1
            for child in children:
                if child == endNode:
                    return steps
                if not visited.get(child,False):
                    q.put(child)
    
    def getEdges(self,vertex:int)->List[int]:
        return self.graph.get(vertex,[])

def minimum_number_of_rolls(n, moves):
    dag: DirectedGraph = DirectedGraph(n)
    for k,v in enumerate(moves):
        if v != -1:
            dag.buildEdges([k+1,v+1])

    numberOfSteps: int = dag.minimumSteps(1,n)
    # import graph
    # graph.draw_graph(dag)
    return numberOfSteps

if __name__ == '__main__':
    input = {
                "n": 6,
                "moves": []
            }
    assert minimum_number_of_rolls(input["n"], input["moves"]) == 1, "For n == 7, minimum number of moves is 1"

    input["n"] = 8
    assert minimum_number_of_rolls(input["n"], input["moves"]) == 2, "For n == 8, minimum number of moves is 2"

    input["n"] = 20
    input["moves"] = [-1, 18, -1, -1, -1, -1, -1, -1, 2, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1]

    assert minimum_number_of_rolls(input["n"], input["moves"]) == 2, "For n == 20, minimum number of moves is 2"