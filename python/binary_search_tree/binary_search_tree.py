from node import Node


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(None, None, None, value)
        else:
            previous = self.root
            iterator = self.root
            left = None
            while iterator is not None:
                previous = iterator
                if value < iterator.getValue():
                    iterator = iterator.getLeft()
                    left = True
                else:
                    iterator = iterator.getRight()
                    left = False

            newnode = Node(previous, iterator.getLeft(), iterator.getRight(),
                           value)

            if left is True:
                previous.setLeft(newnode)
            elif left is False:
                previous.setRight(newnode)

            iterator.setParent(newnode)

    def delete(self, value):
        pass

    def find(self, value):
        iterator = self.root
        while iterator is not None:
            if iterator.getValue() == value:
                return iterator
            elif iterator.getValue() > value:
                iterator = iterator.getLeft()
            else:
                iterator = iterator.getRight()

        return False

    def preOrder(self):
        pass

    def inOrder(self):
        pass

    def postOrder(self):
        pass
