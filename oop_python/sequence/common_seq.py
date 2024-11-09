from typing import List
from queue import Queue

class Node:
    def __init__(self,value:str, leftOut:str=""):
        self.currentString = value
        self.leftOutString = leftOut
        self.left = None
        self.right = None

    def __eq__(self, __value: 'Node') -> bool:
        if self.currentString == __value.currentString and self.leftOutString == __value.leftOutString:
            return True
        return False
    
    def __str__(self) -> str:
        return f"current string: {self.currentString}, leftoutString: {self.leftOutString}"

class BinaryTree:
    def __init__(self, root: Node, left:Node, right:Node):
        self.root = root
        self.left = left
        self.right = right

    def __isNotExplored(self,explored:List[Node],node:Node) -> bool:
        return False
    
    def __bfs(self,nodeToBeSearched:Node) -> Node:
        q = Queue()
        q.put(self.root)
        explored: List[Node] = []
        while not q.empty():
            node:Node = q.get()
            if self.__isNotExplored():    
                q.put(node.left)
                q.put(node.right)
                explored.append(node)
                if node.__eq__(nodeToBeSearched):
                    return node
        raise ValueError(f"Incorrect BFS Impelmentation, Node {nodeToBeSearched} not found")

    def addChild(parent:Node, leftRightInd: bool):
        #TO DO BFS, Get Node



def helper(inputStr:str, startPos:int ,result:List[str], currentStr: str):
    if startPos == len(inputStr):
        result.append(currentStr)
        return
    currentStr += inputStr[startPos]
    helper(inputStr,startPos+1,result,currentStr)
    currentStr = currentStr[:-1]
    helper(inputStr,startPos+1,result,currentStr)


def commonSequence(a:str) -> List[str]:
    result: List[str] = []
    helper(a,0,result,"")
    return result

if __name__ == '__main__':
    print (commonSequence('ABC'))