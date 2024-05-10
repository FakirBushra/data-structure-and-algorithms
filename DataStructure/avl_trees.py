# AVL Trees (Balanced Binary Trees)

class Node(object):

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.rightChild = None
        self.leftChild = None


class AVL(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)
        if data < node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        return self.settleViolation(data, node)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)

        else:
            if not node.leftChild and not node.rightChild:
                print("Removing leaf node... ")
                del node
                return None

            if not node.leftChild:
                print("Removing node with a right child...")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print("Removing node with a left child...")
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with two children... ")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        if not node:
            return node  # if the tree has just a single nde

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        balance = self.calcBalance(node)

        # Doubly left heavy situation
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)

        # Left right case
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        # Right right case
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.rotateLeft(node)

        # Right left case
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node

    def settleViolation(self, data, node):
        balance = self.calcBalance(node)

        # Case 1 : Doubly left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Doubly left heavy situation...")
            return self.rotateRight(node)

        # Case 2 : Doubly right heavy situation
        if balance < -1 and data > node.rightChild.data:
            print("Doubly right heavy situation...")
            return self.rotateLeft(node)

        # Case 3 : Left right heavy situation
        if balance > 1 and data > node.leftChild.data:
            print("Left right heavy situation")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        # Case 4 : Right left heavy situation
        if balance < -1 and data < node.rightChild.data:
            print("Right left heavy situation")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        return node

    def calcHeight(self, node):
        if not node:
            return -1
        return node.height

    # if it returns value > 1 ---> its a left heavy tree ---> right rotation
    # if it returns value < 1 ---> its a right heavy tree ---> left rotation
    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print("%d" % node.data)
        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def rotateRight(self, node):
        print("Rotating to the right on node ", node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.rightChild),
                                   self.calcHeight(tempLeftChild.rightChild)) + 1

        return tempLeftChild

    def rotateLeft(self, node):
        print("Rotating to the left on node ", node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t

        node.height = max(self.calcHeight(node.rightChild), self.calcHeight(node.leftChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.rightChild),
                                    self.calcHeight(tempRightChild.leftChild)) + 1

        return tempRightChild


avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(6)
avl.insert(15)

avl.traverse()
avl.remove(15)
avl.remove(20)
avl.traverse()
