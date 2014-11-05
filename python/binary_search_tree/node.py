

class Node:

    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.value = None

    def __init__(self, pnode, lnode, rnode, value):
        self.parent = pnode
        self.left = lnode
        self.right = rnode
        self.value = value

    def setParent(self, node):
        self.parent = node

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setValue(self, value):
        self.value = value

    def getParent(self):
        return self.parent

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value
