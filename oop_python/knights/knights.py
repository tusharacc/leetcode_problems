from typing import List, Dict, Tuple, Any
from queue import Queue

class Node:
    instances: Dict[int, 'Node']  = {}
    def __init__(self,x:int,y:int):
        self.x: int = x
        self.y: int = y

    def isSame(self, anotherObj: Any) -> bool:
        return self.__eq__(anotherObj)
    
    def getHash(self):
        hash: int = self.__hash__()
        Node.instances[hash] = self

    @classmethod
    def getInstance(hash:int)->'Node':
        return Node.instances.get(hash,None)
    
    def __hash__(self) -> int:
        # Combine x and y into a single hash value
        return hash((self.x, self.y))
    
    def __eq__(self, other:Any):
        if not isinstance(other, Node):
            return False
        return self.x == other.x and self.y == other.y

class ChessBoard:
    def __init__(self,maxRow,maxCol):
        self.maxRow = maxRow - 1
        self.maxCol = maxCol - 1

    def getPotentialKnightMove(self,node:Node) -> List[Node]:
        cartesian: List[Tuple[int,int]] = [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        potential: List[Tuple[int,int]] = []
        for item in cartesian:
            newRow = item[0] + node.x
            newCol = item[1] + node.y

            if newRow <= self.maxRow and newCol <= self.maxCol and newRow >= 0 and newCol >= 0:
                potential.append(Node(newRow, newCol))
        return potential    
    
class Graph:
    def __init__(self):
        self.graph: Dict[Node, List[Node]] = {}
        self.childToParent: Dict[int,'Node'] = {}

    def __mapChildrenToParent(self,child:Node, parent: Node):
        self.childToParent[child.getHash()] = parent

    def addChildren(self,parentNode: Node, childNode: Node):
        self.__mapChildrenToParent(childNode, parentNode)
        if self.graph.get(parentNode, None) == None:
            self.graph[parentNode.getHash()] = [childNode]
        else:
            self.graph[parentNode.getHash()].append(childNode)

    def alreadyVisited(self, parentNode: Node, childNode: Node) -> bool:
        if self.graph.get(parentNode.getHash(), None) == None:
            return False
        else:
            for item in self.graph[parentNode.getHash()]:
                if item.isSame(childNode):
                    return True
            return False
    
    def isVisted(self,node:Node):
        if self.graph.get(node.getHash(),None) == None:
            return False
        return True
    
    def returnItems(self) -> List:
        return self.items()

def traceBack(node:Node, graph: Graph, chessBoard: ChessBoard, startNode: Node) -> int:
    length = 1
    while True:
        parentNode: Node = Node.getInstance(node.getHash())
        if parentNode.isSame(startNode):
            return length
        length += 1


def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    maxRow, maxCol = rows, cols
    chessBoard: ChessBoard = ChessBoard(maxRow=maxRow, maxCol=maxCol)
    destNode: Node = Node(end_row, end_col)
    startNode: Node = Node(start_row, start_col)
    graph: Graph = Graph()
    q: Queue = Queue()
    q.put(startNode)
    if startNode.isSame(destNode):
        return 0
    while not q.empty():
        node: Node = q.get()
        potentialChildren: List[Node] = chessBoard.getPotentialKnightMove(node)
        for item in potentialChildren:
            if graph.isVisted(item):
                continue
            if item.isSame(destNode):
                return traceBack(node, graph, chessBoard, startNode)
            if not graph.alreadyVisited(node, item):
                q.put(item)
                graph.addChildren(node, item)

    return -1

if __name__ == '__main__':
    print (find_minimum_number_of_moves(5,5,0,0,4,1))






    