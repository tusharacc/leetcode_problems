'''
Given a strongly connected directed graph, return its transpose. 
The graph will be given as a reference to one of its nodes; the rest of the graph can be discovered by walking its edges.
'''
from queue import Queue

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def create_node(parent,child,nodes):
    parentPrime = None
    childPrime = None
    for item in nodes:
        if item.value == parent.value:
            parentPrime = item
        if item.value == child.value:
            childPrime = item
    if parentPrime == None:
        parentPrime = GraphNode(parent.value)
        nodes.append(parentPrime)
    
    if childPrime == None:
        childPrime = GraphNode(child.value)
        nodes.append(childPrime)
    
    childPrime.neighbors.append(parentPrime)

def create_transpose(node):
    """
    Args:
     node(GraphNode_int32)
    Returns:
     GraphNode_int32
    """
    # Write your code here.
    q:Queue[GraphNode] = Queue()
    q.put(node)
    nodes = []
    visited = {}
    while not q.empty():
        item: GraphNode = q.get()
        if not visited.get(item.value, False):
            visited[item.value] = True
            for child in item.neighbors:
                q.put(child)
                newRelation = create_node(item,child,nodes)
                
    return nodes[0]

if __name__ == '__main__':
    oneGraphNode = GraphNode(1)
    twoGraphNode = GraphNode(2)
    threeGraphNode = GraphNode(3)
    oneGraphNode.neighbors.append(twoGraphNode)
    twoGraphNode.neighbors.append(threeGraphNode)
    threeGraphNode.neighbors.append(oneGraphNode)

    create_transpose(oneGraphNode)
    print ("Hi")