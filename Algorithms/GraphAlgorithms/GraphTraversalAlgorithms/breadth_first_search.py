
# Breath First Search

class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False

class BreathFirstSearch(object):

    def bfs(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

    # BFS -> Queue ... DFS -> Stack but usually we implement it with recursion
        while queue:
            actualNode = queue.pop(0)
            print("%s" % actualNode.name)

            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.vsited = True
                    queue.append(n)


bfs = BreathFirstSearch()

Node1 = Node("A")
Node2 = Node("B")
Node3 = Node("C")
Node4 = Node("D")
Node5 = Node("E")

Node1.adjacencyList.append(Node2)
Node2.adjacencyList.append(Node3)
Node3.adjacencyList.append(Node4)
Node4.adjacencyList.append(Node5)

bfs.bfs(Node1)