# Ternary Tearch Trees

class Node(object):

    def __init__(self, character):
        self.character = character
        self.leftChild = None
        self.middleChild = None
        self.rightChild = None
        self.value = 0


class TST(object):

    def __init__(self):
        self.rootNode = None

    def put(self, key, value):
        self.rootNode = self.putItem(self.rootNode, key, value, 0)

    def putItem(self, node, key, value, index):
        c = key[index]

        if node == None:
            node = Node(c)

        if c < node.character:
            node.leftChild = self.putItem(node.leftChild, key, value, index)
        elif c > node.character:
            node.rightChild = self.putItem(node.rightChild, key, value, index)
        elif index < len(key) - 1:
            node.middleChild = self.putItem(node.middleChild, key, value, index + 1)
        else:
            node.value = value

        return node

    def get(self, key):
        node = self.getItem(self.rootNode, key, 0)
        if node == None:
            return -1

        return node.value

    def getItem(self, node, key, index):
        if node == None:
            return None

        c = key[index]

        if c < node.character:
            return self.getItem(node.leftChild, key, index)
        elif c > node.character:
            return self.getItem(node.rightChild, key, index)
        elif index < len(key) - 1:
            return self.getItem(node.middleChild, key, index + 1)
        else:
            return node


if __name__ == "__main__":
    tst = TST()

    tst.put("apple", 2)
    tst.put("orange", 3)
    tst.put("banana", 4)

    print(tst.get("orange"))
